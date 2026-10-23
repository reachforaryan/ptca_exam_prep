# PTCA Certification Exam Prep — 500-Question Study Workbench

A lightweight, syllabus-aligned 500-question MCQ workbench for the Linux Foundation **PyTorch Certified Associate (PTCA)** certification (`LFD2000`–`LFD2003`).

## Domain Breakdown

| Domain | Weight | Questions | IDs |
| :--- | :---: | :---: | :--- |
| **A. PyTorch Fundamentals** | 38% | 190 | `PTCA-F-001` – `PTCA-F-190` |
| **B. Model Development** | 20% | 100 | `PTCA-M-001` – `PTCA-M-100` |
| **C. Performance & Optimization** | 26% | 130 | `PTCA-P-001` – `PTCA-P-130` |
| **D. Data Handling** | 16% | 80 | `PTCA-D-001` – `PTCA-D-080` |
| **Total** | **100%** | **500** | |

---

## Quick Setup & Usage

No third-party dependencies are required—only **Python 3** (standard library) and a browser.

### Option 1: Run with Local SQLite + JSON Persistence (Recommended)

Start the lightweight local server to automatically save your answers, flags, and personal study notes to `ptca_study.db` (SQLite) and `user_notes.json`:

```bash
git clone https://github.com/reachforaryan/ptca_exam_prep.git
cd ptca_exam_prep
python3 server.py
```

Then open **[http://127.0.0.1:8765](http://127.0.0.1:8765)** in your browser.
*(Pass a custom port if needed: `python3 server.py 9000`)*

### Option 2: Open Directly as a Static Page (Zero Server)

You can also open `index.html` directly in your browser (`file://`). Progress and notes will fall back to browser `localStorage`, and you can use **Export Notes** / **Import Notes** in the header to back up or restore your study data as JSON.

---

## Rebuilding the Question Bank (Optional)

If you edit any domain generator scripts inside `data/`, regenerate and validate the 500-question bank with:

```bash
python3 build_question_bank.py
```

## Keyboard Shortcuts

- `1`–`4` or `A`–`D`: Select option A–D
- `Enter`: Submit answer (in Multi-Select or Mock Mode)
- `←` / `→`: Previous / Next question
- `F`: Flag / bookmark current question
