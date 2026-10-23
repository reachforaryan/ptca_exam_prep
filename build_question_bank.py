#!/usr/bin/env python3
"""
Merges and validates all 500 PTCA questions across:
  - data/domain_a1.json (PTCA-F-001 .. PTCA-F-095)
  - data/domain_a2.json (PTCA-F-096 .. PTCA-F-190)
  - data/domain_b.json  (PTCA-M-001 .. PTCA-M-100)
  - data/domain_c.json  (PTCA-P-001 .. PTCA-P-130)
  - data/domain_d.json  (PTCA-D-001 .. PTCA-D-080)
Outputs:
  - questions.json
  - questions.js (for standalone file:// usage)
"""

import json
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"

PART_FILES = [
    ("domain_a1.json", 95),
    ("domain_a2.json", 95),
    ("domain_b.json", 100),
    ("domain_c.json", 130),
    ("domain_d.json", 80),
]


def main():
    all_questions = []
    seen_ids = set()

    for fname, expected_count in PART_FILES:
        fpath = DATA_DIR / fname
        if not fpath.exists():
            print(f"[ERROR] Missing {fpath}", file=sys.stderr)
            sys.exit(1)
        with open(fpath, "r", encoding="utf-8") as f:
            items = json.load(f)
        print(f"Loaded {fname}: {len(items)} questions (expected {expected_count})")
        if len(items) != expected_count:
            print(f"[WARN] {fname} has {len(items)} != {expected_count}", file=sys.stderr)

        for q in items:
            qid = q["id"]
            if qid in seen_ids:
                raise ValueError(f"Duplicate question ID: {qid}")
            seen_ids.add(qid)
            # Validate required fields
            for req in ("id", "domain", "domain_code", "subtopic", "difficulty", "stem", "options", "correct", "explanation"):
                if req not in q:
                    raise ValueError(f"Missing {req} in {qid}")
            all_questions.append(q)

    print(f"Total merged questions: {len(all_questions)}")

    q_json_path = BASE_DIR / "questions.json"
    with open(q_json_path, "w", encoding="utf-8") as f:
        json.dump(all_questions, f, indent=2, ensure_ascii=False)

    q_js_path = BASE_DIR / "questions.js"
    with open(q_js_path, "w", encoding="utf-8") as f:
        f.write("window.PTCA_QUESTIONS = ")
        json.dump(all_questions, f, indent=2, ensure_ascii=False)
        f.write(";\n")

    print(f"Successfully wrote {q_json_path} and {q_js_path}")


if __name__ == "__main__":
    main()
