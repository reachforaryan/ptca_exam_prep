#!/usr/bin/env python3
"""
Lightweight local server for the PTCA 500-Question Exam Workbench.
Uses ONLY Python standard library modules (http.server, sqlite3, json).
Persists all user answers, bookmarks, and personal notes to:
  1. SQLite database: ptca_study.db
  2. Human-readable JSON mirror: user_notes.json
"""

import http.server
import json
import os
import sqlite3
import sys
import time
from pathlib import Path
from urllib.parse import urlparse

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "ptca_study.db"
JSON_MIRROR_PATH = BASE_DIR / "user_notes.json"
DEFAULT_PORT = 8765


def init_db():
    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS question_progress (
            question_id TEXT PRIMARY KEY,
            selected_options TEXT NOT NULL DEFAULT '[]',
            submitted INTEGER NOT NULL DEFAULT 0,
            is_correct INTEGER NOT NULL DEFAULT 0,
            note TEXT NOT NULL DEFAULT '',
            bookmarked INTEGER NOT NULL DEFAULT 0,
            updated_at REAL NOT NULL DEFAULT 0
        )
        """
    )
    conn.commit()
    conn.close()


def get_all_state():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    rows = conn.execute("SELECT * FROM question_progress").fetchall()
    conn.close()
    state = {}
    for r in rows:
        try:
            sel = json.loads(r["selected_options"])
        except Exception:
            sel = []
        state[r["question_id"]] = {
            "selected": sel,
            "submitted": bool(r["submitted"]),
            "isCorrect": bool(r["is_correct"]),
            "note": r["note"] or "",
            "bookmarked": bool(r["bookmarked"]),
            "updatedAt": r["updated_at"],
        }
    return state


def write_json_mirror(state):
    try:
        with open(JSON_MIRROR_PATH, "w", encoding="utf-8") as f:
            json.dump(state, f, indent=2, ensure_ascii=False)
    except Exception as exc:
        print(f"[warn] Could not write JSON mirror: {exc}", file=sys.stderr)


def upsert_question_state(qid, item):
    conn = sqlite3.connect(DB_PATH)
    sel_json = json.dumps(item.get("selected", []))
    submitted = 1 if item.get("submitted") else 0
    is_correct = 1 if item.get("isCorrect") else 0
    note = str(item.get("note", ""))
    bookmarked = 1 if item.get("bookmarked") else 0
    updated_at = float(item.get("updatedAt") or time.time())
    conn.execute(
        """
        INSERT INTO question_progress (
            question_id, selected_options, submitted, is_correct, note, bookmarked, updated_at
        ) VALUES (?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT(question_id) DO UPDATE SET
            selected_options = excluded.selected_options,
            submitted = excluded.submitted,
            is_correct = excluded.is_correct,
            note = excluded.note,
            bookmarked = excluded.bookmarked,
            updated_at = excluded.updated_at
        """,
        (qid, sel_json, submitted, is_correct, note, bookmarked, updated_at),
    )
    conn.commit()
    conn.close()


def bulk_upsert_state(items_dict):
    conn = sqlite3.connect(DB_PATH)
    now = time.time()
    for qid, item in items_dict.items():
        if not isinstance(item, dict):
            continue
        sel_json = json.dumps(item.get("selected", []))
        submitted = 1 if item.get("submitted") else 0
        is_correct = 1 if item.get("isCorrect") else 0
        note = str(item.get("note", ""))
        bookmarked = 1 if item.get("bookmarked") else 0
        updated_at = float(item.get("updatedAt") or now)
        conn.execute(
            """
            INSERT INTO question_progress (
                question_id, selected_options, submitted, is_correct, note, bookmarked, updated_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(question_id) DO UPDATE SET
                selected_options = excluded.selected_options,
                submitted = excluded.submitted,
                is_correct = excluded.is_correct,
                note = excluded.note,
                bookmarked = excluded.bookmarked,
                updated_at = excluded.updated_at
            WHERE excluded.updated_at >= question_progress.updated_at
            """,
            (qid, sel_json, submitted, is_correct, note, bookmarked, updated_at),
        )
    conn.commit()
    conn.close()


def reset_attempts(keep_notes=True):
    conn = sqlite3.connect(DB_PATH)
    if keep_notes:
        conn.execute(
            """
            UPDATE question_progress
            SET selected_options = '[]', submitted = 0, is_correct = 0, updated_at = ?
            """,
            (time.time(),),
        )
    else:
        conn.execute("DELETE FROM question_progress")
    conn.commit()
    conn.close()


class PTCAHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(BASE_DIR), **kwargs)

    def log_message(self, fmt, *args):
        # Keep terminal output quiet and clean
        pass

    def _send_json(self, payload, status=200):
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        parsed = urlparse(self.path)
        if parsed.path == "/api/state":
            state = get_all_state()
            self._send_json({"ok": True, "storage": "sqlite+json", "state": state})
            return
        return super().do_GET()

    def do_POST(self):
        parsed = urlparse(self.path)
        length = int(self.headers.get("Content-Length", "0"))
        raw = self.rfile.read(length).decode("utf-8") if length > 0 else "{}"
        try:
            data = json.loads(raw)
        except Exception:
            self._send_json({"ok": False, "error": "Invalid JSON"}, status=400)
            return

        if parsed.path == "/api/save":
            qid = data.get("questionId")
            item = data.get("item", {})
            if not qid or not isinstance(item, dict):
                self._send_json({"ok": False, "error": "Missing questionId or item"}, status=400)
                return
            upsert_question_state(qid, item)
            state = get_all_state()
            write_json_mirror(state)
            self._send_json({"ok": True})
            return

        if parsed.path == "/api/bulk_save":
            items = data.get("state", {})
            if isinstance(items, dict):
                bulk_upsert_state(items)
            state = get_all_state()
            write_json_mirror(state)
            self._send_json({"ok": True, "state": state})
            return

        if parsed.path == "/api/reset":
            keep_notes = bool(data.get("keepNotes", True))
            reset_attempts(keep_notes=keep_notes)
            state = get_all_state()
            write_json_mirror(state)
            self._send_json({"ok": True, "state": state})
            return

        self._send_json({"ok": False, "error": "Not found"}, status=404)


def main():
    port = int(os.environ.get("PTCA_PORT", DEFAULT_PORT))
    init_db()
    if JSON_MIRROR_PATH.exists():
        try:
            with open(JSON_MIRROR_PATH, "r", encoding="utf-8") as f:
                existing = json.load(f)
            if isinstance(existing, dict) and existing:
                bulk_upsert_state(existing)
        except Exception:
            pass
    state = get_all_state()
    write_json_mirror(state)

    http.server.ThreadingHTTPServer.allow_reuse_address = True
    server = http.server.ThreadingHTTPServer(("127.0.0.1", port), PTCAHandler)
    print(f"PTCA Exam Workbench running at http://127.0.0.1:{port}")
    print(f"SQLite DB: {DB_PATH}")
    print(f"JSON Mirror: {JSON_MIRROR_PATH}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down PTCA Exam Workbench.")
        server.server_close()


if __name__ == "__main__":
    main()
