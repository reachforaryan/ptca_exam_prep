(function () {
  "use strict";

  const LOCAL_STORAGE_KEY = "ptca_workbench_state_v1";
  const THEME_KEY = "ptca_workbench_theme";

  let allQuestions = Array.isArray(window.PTCA_QUESTIONS) ? window.PTCA_QUESTIONS : [];
  let filteredQuestions = [];
  let currentIndex = 0;

  // userState[qid] = { selected: [], submitted: false, isCorrect: false, note: "", bookmarked: false, updatedAt: 0 }
  let userState = {};
  let backendAvailable = false;

  // Modes: "PRACTICE" | "MOCK" | "NOTES"
  let currentMode = "PRACTICE";
  let mockQuestions = [];
  let mockSubmitted = false;
  let mockSecondsLeft = 120 * 60;
  let mockTimerInterval = null;

  // Filters
  let activeStatusFilter = "ALL";
  let noteSaveTimer = null;

  // DOM Elements
  const elStorageDot = document.getElementById("storage-dot");
  const elStorageText = document.getElementById("storage-text");
  const elStatAnswered = document.getElementById("stat-answered");
  const elStatCorrect = document.getElementById("stat-correct");
  const elStatWrong = document.getElementById("stat-wrong");
  const elStatNotes = document.getElementById("stat-notes");

  const elFilterSearch = document.getElementById("filter-search");
  const elFilterDomain = document.getElementById("filter-domain");
  const elFilterSubtopic = document.getElementById("filter-subtopic");
  const elFilterDifficulty = document.getElementById("filter-difficulty");
  const elStatusPills = document.querySelectorAll(".status-pill");
  const elGridCountLabel = document.getElementById("grid-count-label");
  const elQuestionGrid = document.getElementById("question-grid");

  const elTabPractice = document.getElementById("tab-practice");
  const elTabMock = document.getElementById("tab-mock");
  const elTabNotes = document.getElementById("tab-notes");

  const elMockBanner = document.getElementById("mock-banner");
  const elMockTimerDisplay = document.getElementById("mock-timer-display");
  const elBtnMockSubmit = document.getElementById("btn-mock-submit");
  const elBtnMockNew = document.getElementById("btn-mock-new");

  const elQuestionView = document.getElementById("question-view");
  const elNotesAnalyticsView = document.getElementById("notes-analytics-view");

  const elQIdBadge = document.getElementById("q-id-badge");
  const elQDomainBadge = document.getElementById("q-domain-badge");
  const elQSubtopicBadge = document.getElementById("q-subtopic-badge");
  const elQDiffBadge = document.getElementById("q-diff-badge");
  const elQMultiBadge = document.getElementById("q-multi-badge");
  const elQPositionText = document.getElementById("q-position-text");
  const elBtnBookmark = document.getElementById("btn-bookmark");

  const elQStem = document.getElementById("q-stem");
  const elQCodeWrap = document.getElementById("q-code-wrap");
  const elQCode = document.getElementById("q-code");
  const elBtnCopyCode = document.getElementById("btn-copy-code");
  const elQOptions = document.getElementById("q-options");

  const elBtnPrev = document.getElementById("btn-prev");
  const elBtnNext = document.getElementById("btn-next");
  const elBtnCheckMulti = document.getElementById("btn-check-multi");
  const elBtnRetryOne = document.getElementById("btn-retry-one");

  const elExplanationBox = document.getElementById("q-explanation-box");
  const elVerdictTitle = document.getElementById("q-verdict-title");
  const elCorrectLetterPill = document.getElementById("q-correct-letter-pill");
  const elExplanationText = document.getElementById("q-explanation-text");
  const elOptionBreakdown = document.getElementById("q-option-breakdown");
  const elQCompetency = document.getElementById("q-competency");
  const elQSource = document.getElementById("q-source");

  const elNoteInput = document.getElementById("q-note-input");
  const elNoteStatus = document.getElementById("q-note-status");

  const elDomainAnalyticsBars = document.getElementById("domain-analytics-bars");
  const elNotesViewFilter = document.getElementById("notes-view-filter");
  const elNotesReviewList = document.getElementById("notes-review-list");

  const elBtnExport = document.getElementById("btn-export");
  const elInputImport = document.getElementById("input-import");
  const elBtnResetAll = document.getElementById("btn-reset-all");
  const elBtnTheme = document.getElementById("btn-theme");

  function getEntry(qid) {
    if (!userState[qid]) {
      userState[qid] = {
        selected: [],
        submitted: false,
        isCorrect: false,
        note: "",
        bookmarked: false,
        updatedAt: 0,
      };
    }
    return userState[qid];
  }

  function saveToLocalStorage() {
    try {
      localStorage.setItem(LOCAL_STORAGE_KEY, JSON.stringify(userState));
    } catch (e) {
      console.warn("LocalStorage write error:", e);
    }
  }

  function loadFromLocalStorage() {
    try {
      const raw = localStorage.getItem(LOCAL_STORAGE_KEY);
      if (raw) {
        const parsed = JSON.parse(raw);
        if (parsed && typeof parsed === "object") {
          userState = parsed;
        }
      }
    } catch (e) {
      console.warn("LocalStorage read error:", e);
    }
  }

  async function initStorageSync() {
    loadFromLocalStorage();
    try {
      const res = await fetch("/api/state", { cache: "no-store" });
      if (res.ok) {
        const data = await res.json();
        if (data && data.ok) {
          backendAvailable = true;
          const serverState = data.state || {};
          // Merge local and server by updatedAt
          const merged = Object.assign({}, serverState);
          for (const [qid, loc] of Object.entries(userState)) {
            if (!merged[qid] || (loc.updatedAt || 0) > (merged[qid].updatedAt || 0)) {
              merged[qid] = loc;
            }
          }
          userState = merged;
          saveToLocalStorage();
          await fetch("/api/bulk_save", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ state: userState }),
          });
          elStorageDot.classList.remove("local");
          elStorageText.textContent = "SQLite + JSON Saved";
          return;
        }
      }
    } catch (_) {
      // Running as static file:// or without server.py
    }
    backendAvailable = false;
    elStorageDot.classList.add("local");
    elStorageText.textContent = "Browser Storage (Export JSON anytime)";
  }

  async function persistQuestionState(qid, statusLabelEl) {
    const entry = getEntry(qid);
    entry.updatedAt = Date.now() / 1000;
    saveToLocalStorage();
    updateGlobalStats();

    const timeStr = new Date().toLocaleTimeString([], { hour: "2-digit", minute: "2-digit", second: "2-digit" });
    if (backendAvailable) {
      try {
        const res = await fetch("/api/save", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ questionId: qid, item: entry }),
        });
        if (res.ok) {
          if (statusLabelEl) {
            statusLabelEl.textContent = `Saved to SQLite & user_notes.json · ${timeStr}`;
          }
          return;
        }
      } catch (_) {
        backendAvailable = false;
      }
    }
    if (statusLabelEl) {
      statusLabelEl.textContent = `Saved in browser · ${timeStr}`;
    }
  }

  function arraysMatch(a, b) {
    if (!Array.isArray(a) || !Array.isArray(b)) return false;
    if (a.length !== b.length) return false;
    const sa = [...a].sort();
    const sb = [...b].sort();
    return sa.every((v, i) => v === sb[i]);
  }

  function formatInlineCode(text) {
    if (!text) return "";
    const escaped = String(text)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;");
    return escaped.replace(/`([^`]+)`/g, "<code>$1</code>");
  }

  function populateSubtopics() {
    const domainVal = elFilterDomain.value;
    const subs = new Set();
    allQuestions.forEach((q) => {
      if (domainVal === "ALL" || q.domain_code === domainVal) {
        subs.add(q.subtopic);
      }
    });
    const prevVal = elFilterSubtopic.value;
    elFilterSubtopic.innerHTML = '<option value="ALL">All Subtopics</option>';
    Array.from(subs)
      .sort()
      .forEach((s) => {
        const opt = document.createElement("option");
        opt.value = s;
        opt.textContent = s;
        elFilterSubtopic.appendChild(opt);
      });
    if (Array.from(subs).includes(prevVal)) {
      elFilterSubtopic.value = prevVal;
    }
  }

  function applyFilters() {
    if (currentMode === "MOCK") {
      filteredQuestions = mockQuestions;
      elGridCountLabel.textContent = `Mock Exam: ${filteredQuestions.length} questions`;
      if (currentIndex >= filteredQuestions.length) currentIndex = 0;
      renderGrid();
      renderCurrentQuestion();
      return;
    }

    const search = elFilterSearch.value.trim().toLowerCase();
    const domain = elFilterDomain.value;
    const subtopic = elFilterSubtopic.value;
    const diff = elFilterDifficulty.value;

    filteredQuestions = allQuestions.filter((q) => {
      if (domain !== "ALL" && q.domain_code !== domain) return false;
      if (subtopic !== "ALL" && q.subtopic !== subtopic) return false;
      if (diff !== "ALL" && q.difficulty !== diff) return false;

      const st = getEntry(q.id);
      if (activeStatusFilter === "UNANSWERED" && st.submitted) return false;
      if (activeStatusFilter === "WRONG" && (!st.submitted || st.isCorrect)) return false;
      if (activeStatusFilter === "CORRECT" && (!st.submitted || !st.isCorrect)) return false;
      if (activeStatusFilter === "BOOKMARKED" && !st.bookmarked) return false;
      if (activeStatusFilter === "HAS_NOTE" && (!st.note || !st.note.trim())) return false;

      if (search) {
        const hay = `${q.id} ${q.subtopic} ${q.stem} ${q.code || ""} ${q.competency || ""} ${st.note || ""}`.toLowerCase();
        if (!hay.includes(search)) return false;
      }
      return true;
    });

    elGridCountLabel.textContent = `Showing ${filteredQuestions.length} of ${allQuestions.length} questions`;
    if (currentIndex >= filteredQuestions.length) {
      currentIndex = 0;
    }
    renderGrid();
    renderCurrentQuestion();
  }

  function updateGlobalStats() {
    let answered = 0;
    let correct = 0;
    let wrong = 0;
    let notes = 0;

    allQuestions.forEach((q) => {
      const st = userState[q.id];
      if (!st) return;
      if (st.submitted) {
        answered++;
        if (st.isCorrect) correct++;
        else wrong++;
      }
      if (st.note && st.note.trim().length > 0) {
        notes++;
      }
    });

    elStatAnswered.textContent = `${answered}/${allQuestions.length}`;
    elStatCorrect.textContent = String(correct);
    elStatWrong.textContent = String(wrong);
    elStatNotes.textContent = String(notes);
  }

  function renderGrid() {
    elQuestionGrid.innerHTML = "";
    const frag = document.createDocumentFragment();

    filteredQuestions.forEach((q, idx) => {
      const st = getEntry(q.id);
      const btn = document.createElement("button");
      btn.type = "button";
      btn.className = "q-grid-cell";
      if (idx === currentIndex) btn.classList.add("current");

      if (currentMode === "MOCK" && !mockSubmitted) {
        if (st.selected && st.selected.length > 0) {
          btn.classList.add("is-answered-mock");
        }
      } else if (st.submitted) {
        btn.classList.add(st.isCorrect ? "is-correct" : "is-wrong");
      }

      const shortNum = q.id.replace("PTCA-", "");
      btn.textContent = shortNum;
      btn.title = `${q.id} — ${q.subtopic}`;

      if (st.note && st.note.trim()) {
        const dotN = document.createElement("span");
        dotN.className = "cell-dot-note";
        btn.appendChild(dotN);
      }
      if (st.bookmarked) {
        const dotB = document.createElement("span");
        dotB.className = "cell-dot-bookmark";
        btn.appendChild(dotB);
      }

      btn.addEventListener("click", () => {
        currentIndex = idx;
        if (currentMode === "NOTES") {
          setMode("PRACTICE");
        } else {
          renderGrid();
          renderCurrentQuestion();
        }
      });

      frag.appendChild(btn);
    });

    elQuestionGrid.appendChild(frag);
  }

  function renderCurrentQuestion() {
    if (filteredQuestions.length === 0) {
      elQIdBadge.textContent = "No Match";
      elQDomainBadge.textContent = "-";
      elQSubtopicBadge.textContent = "-";
      elQStem.textContent = "No questions match the current filter criteria. Try clearing the search box or switching status pills.";
      elQCodeWrap.style.display = "none";
      elQOptions.innerHTML = "";
      elExplanationBox.style.display = "none";
      return;
    }

    const q = filteredQuestions[currentIndex];
    const st = getEntry(q.id);

    elQIdBadge.textContent = q.id;
    elQDomainBadge.textContent = q.domain;
    elQSubtopicBadge.textContent = q.subtopic;

    elQDiffBadge.textContent = q.difficulty;
    elQDiffBadge.className = "badge " + (
      q.difficulty === "Easy"
        ? "badge-easy"
        : q.difficulty === "Hard"
        ? "badge-hard"
        : "badge-medium"
    );

    const isMulti = Boolean(q.multi_select || (q.correct && q.correct.length > 1));
    if (isMulti) {
      elQMultiBadge.style.display = "inline-flex";
      elQMultiBadge.textContent = `Select ${q.correct.length === 2 ? "TWO" : "ALL that apply"}`;
    } else {
      elQMultiBadge.style.display = "none";
    }

    elQPositionText.textContent = `${currentIndex + 1} of ${filteredQuestions.length}`;
    elBtnBookmark.textContent = st.bookmarked ? "★ Bookmarked" : "☆ Bookmark";
    elBtnBookmark.classList.toggle("btn-primary", Boolean(st.bookmarked));

    elQStem.innerHTML = formatInlineCode(q.stem);

    if (q.code && q.code.trim()) {
      elQCodeWrap.style.display = "block";
      elQCode.textContent = q.code;
    } else {
      elQCodeWrap.style.display = "none";
      elQCode.textContent = "";
    }

    // Render Options A, B, C, D
    elQOptions.innerHTML = "";
    const showGraded = (currentMode === "PRACTICE" && st.submitted) || (currentMode === "MOCK" && mockSubmitted);

    ["A", "B", "C", "D"].forEach((letter) => {
      if (!q.options || !(letter in q.options)) return;
      const btn = document.createElement("button");
      btn.type = "button";
      btn.className = "option-btn";

      const isSelected = st.selected.includes(letter);
      const isActualCorrect = q.correct.includes(letter);

      if (showGraded) {
        btn.classList.add("locked");
        if (isActualCorrect) {
          btn.classList.add("correct-choice");
        } else if (isSelected && !isActualCorrect) {
          btn.classList.add("wrong-choice");
        }
      } else if (isSelected) {
        btn.classList.add("selected");
      }

      const keySpan = document.createElement("span");
      keySpan.className = "option-key";
      keySpan.textContent = letter;

      const textSpan = document.createElement("span");
      textSpan.className = "option-text";
      textSpan.innerHTML = formatInlineCode(q.options[letter]);

      btn.appendChild(keySpan);
      btn.appendChild(textSpan);

      if (showGraded) {
        const tag = document.createElement("span");
        tag.className = "option-tag";
        if (isActualCorrect && isSelected) {
          tag.textContent = "✓ Your Answer (Correct)";
          btn.appendChild(tag);
        } else if (isActualCorrect && !isSelected) {
          tag.textContent = "✓ Correct Answer";
          btn.appendChild(tag);
        } else if (!isActualCorrect && isSelected) {
          tag.textContent = "✗ Your Choice";
          btn.appendChild(tag);
        }
      }

      btn.addEventListener("click", () => handleOptionSelect(q, letter, isMulti));
      elQOptions.appendChild(btn);
    });

    elBtnPrev.disabled = currentIndex === 0;
    elBtnNext.disabled = currentIndex >= filteredQuestions.length - 1;

    // Multi-select check button & Retry button visibility
    if (currentMode === "PRACTICE") {
      if (isMulti && !st.submitted) {
        elBtnCheckMulti.style.display = "inline-flex";
        elBtnCheckMulti.disabled = st.selected.length === 0;
      } else {
        elBtnCheckMulti.style.display = "none";
      }
      elBtnRetryOne.style.display = st.submitted ? "inline-flex" : "none";
    } else {
      elBtnCheckMulti.style.display = "none";
      elBtnRetryOne.style.display = "none";
    }

    // Explanation panel
    if (showGraded) {
      elExplanationBox.style.display = "block";
      elExplanationBox.className = "explanation-box " + (st.isCorrect ? "verdict-correct" : "verdict-wrong");

      const correctStr = q.correct.join(", ");
      const userStr = st.selected.length ? st.selected.join(", ") : "None";

      if (st.isCorrect) {
        elVerdictTitle.textContent = `Correct! Option ${correctStr} is the right answer.`;
      } else {
        elVerdictTitle.textContent = `Incorrect — You chose ${userStr}, but the correct answer is ${correctStr}.`;
      }
      elCorrectLetterPill.textContent = `Correct: ${correctStr}`;
      elExplanationText.innerHTML = formatInlineCode(q.explanation);

      // Option-by-option breakdown
      elOptionBreakdown.innerHTML = "";
      if (q.option_explanations) {
        ["A", "B", "C", "D"].forEach((letter) => {
          const expText = q.option_explanations[letter];
          if (!expText) return;
          const div = document.createElement("div");
          div.className = "opt-exp-item";
          const isCorr = q.correct.includes(letter);
          const isUserWrong = st.selected.includes(letter) && !isCorr;
          if (isCorr) div.classList.add("is-correct-opt");
          if (isUserWrong) div.classList.add("is-user-wrong-opt");

          const prefix = isCorr
            ? `<strong>Option ${letter} (Correct):</strong> `
            : isUserWrong
            ? `<strong>Option ${letter} (Your Choice — Incorrect):</strong> `
            : `<strong>Option ${letter}:</strong> `;
          div.innerHTML = prefix + formatInlineCode(expText);
          elOptionBreakdown.appendChild(div);
        });
      }

      elQCompetency.textContent = q.competency || q.subtopic;
      elQSource.textContent = q.source || "Linux Foundation PTCA Pathway / PyTorch Docs";
    } else {
      elExplanationBox.style.display = "none";
    }

    // Personal Note input
    elNoteInput.value = st.note || "";
    elNoteStatus.textContent = st.note
      ? "Saved in SQLite & user_notes.json"
      : "Auto-saves as you type";
  }

  function handleOptionSelect(q, letter, isMulti) {
    const st = getEntry(q.id);
    if (currentMode === "PRACTICE" && st.submitted) {
      return; // Already graded; click "Clear My Answer" to retry
    }
    if (currentMode === "MOCK" && mockSubmitted) {
      return;
    }

    if (!isMulti) {
      st.selected = [letter];
      if (currentMode === "PRACTICE") {
        st.submitted = true;
        st.isCorrect = arraysMatch(st.selected, q.correct);
      }
    } else {
      if (st.selected.includes(letter)) {
        st.selected = st.selected.filter((x) => x !== letter);
      } else {
        st.selected = [...st.selected, letter].sort();
      }
      // In practice mode, if they selected the exact required count (e.g. 2 for Select TWO), auto-grade or let them click Check Answer
      if (currentMode === "PRACTICE" && q.correct.length > 1 && st.selected.length === q.correct.length) {
        st.submitted = true;
        st.isCorrect = arraysMatch(st.selected, q.correct);
      }
    }

    persistQuestionState(q.id);
    renderGrid();
    renderCurrentQuestion();
  }

  function checkMultiSelectNow() {
    if (filteredQuestions.length === 0) return;
    const q = filteredQuestions[currentIndex];
    const st = getEntry(q.id);
    if (st.selected.length === 0) return;
    st.submitted = true;
    st.isCorrect = arraysMatch(st.selected, q.correct);
    persistQuestionState(q.id);
    renderGrid();
    renderCurrentQuestion();
  }

  function clearSingleQuestionAttempt() {
    if (filteredQuestions.length === 0) return;
    const q = filteredQuestions[currentIndex];
    const st = getEntry(q.id);
    st.selected = [];
    st.submitted = false;
    st.isCorrect = false;
    persistQuestionState(q.id);
    renderGrid();
    renderCurrentQuestion();
  }

  function toggleBookmark() {
    if (filteredQuestions.length === 0) return;
    const q = filteredQuestions[currentIndex];
    const st = getEntry(q.id);
    st.bookmarked = !st.bookmarked;
    persistQuestionState(q.id);
    renderGrid();
    renderCurrentQuestion();
  }

  // Mock Exam Engine (60 questions weighted: 23 A, 12 B, 16 C, 9 D)
  function sampleArray(arr, count) {
    const copy = [...arr];
    for (let i = copy.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [copy[i], copy[j]] = [copy[j], copy[i]];
    }
    return copy.slice(0, count);
  }

  function startNewMockExam() {
    const domA = allQuestions.filter((q) => q.domain_code === "A");
    const domB = allQuestions.filter((q) => q.domain_code === "B");
    const domC = allQuestions.filter((q) => q.domain_code === "C");
    const domD = allQuestions.filter((q) => q.domain_code === "D");

    mockQuestions = [
      ...sampleArray(domA, 23),
      ...sampleArray(domB, 12),
      ...sampleArray(domC, 16),
      ...sampleArray(domD, 9),
    ];

    // Clear previous selections on these 60 questions while keeping notes
    mockQuestions.forEach((q) => {
      const st = getEntry(q.id);
      st.selected = [];
      st.submitted = false;
      st.isCorrect = false;
    });

    mockSubmitted = false;
    mockSecondsLeft = 120 * 60;
    elBtnMockSubmit.disabled = false;
    elBtnMockSubmit.textContent = "Submit & Score Exam";

    if (mockTimerInterval) clearInterval(mockTimerInterval);
    mockTimerInterval = setInterval(() => {
      if (mockSubmitted) return;
      mockSecondsLeft = Math.max(0, mockSecondsLeft - 1);
      const mins = Math.floor(mockSecondsLeft / 60);
      const secs = mockSecondsLeft % 60;
      elMockTimerDisplay.textContent = `${String(mins).padStart(2, "0")}:${String(secs).padStart(2, "0")}`;
      if (mockSecondsLeft === 0) {
        submitMockExam();
      }
    }, 1000);

    currentIndex = 0;
    applyFilters();
  }

  function submitMockExam() {
    if (mockSubmitted) return;
    mockSubmitted = true;
    if (mockTimerInterval) clearInterval(mockTimerInterval);

    let correctCount = 0;
    mockQuestions.forEach((q) => {
      const st = getEntry(q.id);
      st.submitted = true;
      st.isCorrect = arraysMatch(st.selected, q.correct);
      if (st.isCorrect) correctCount++;
    });

    const pct = Math.round((correctCount / mockQuestions.length) * 100);
    const passed = pct >= 75;
    elBtnMockSubmit.disabled = true;
    elBtnMockSubmit.textContent = `${passed ? "PASSED" : "NEEDS REVIEW"}: ${correctCount}/${mockQuestions.length} (${pct}%)`;

    saveToLocalStorage();
    if (backendAvailable) {
      fetch("/api/bulk_save", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ state: userState }),
      }).catch(() => {});
    }
    updateGlobalStats();
    renderGrid();
    renderCurrentQuestion();
  }

  // Notes & Analytics View
  function renderNotesAndAnalytics() {
    const domains = [
      { code: "A", name: "Domain A: PyTorch Fundamentals (38%)", targetWeight: "38%" },
      { code: "B", name: "Domain B: Model Development (20%)", targetWeight: "20%" },
      { code: "C", name: "Domain C: Performance & Optimization (26%)", targetWeight: "26%" },
      { code: "D", name: "Domain D: Data Handling (16%)", targetWeight: "16%" },
    ];

    elDomainAnalyticsBars.innerHTML = "";
    domains.forEach((d) => {
      const qs = allQuestions.filter((q) => q.domain_code === d.code);
      let attempted = 0;
      let corr = 0;
      qs.forEach((q) => {
        const st = getEntry(q.id);
        if (st.submitted) {
          attempted++;
          if (st.isCorrect) corr++;
        }
      });
      const acc = attempted > 0 ? Math.round((corr / attempted) * 100) : 0;

      const wrap = document.createElement("div");
      wrap.innerHTML = `
        <div class="domain-row-top">
          <span>${d.name}</span>
          <span class="tabular-nums">${corr}/${attempted} correct (${acc}% accuracy · ${qs.length} total Qs)</span>
        </div>
        <div class="progress-track">
          <div class="progress-fill" style="width: ${acc}%;"></div>
        </div>
      `;
      elDomainAnalyticsBars.appendChild(wrap);
    });

    const filterType = elNotesViewFilter.value;
    const matching = allQuestions.filter((q) => {
      const st = getEntry(q.id);
      if (filterType === "NOTES") return st.note && st.note.trim().length > 0;
      if (filterType === "WRONG") return st.submitted && !st.isCorrect;
      if (filterType === "BOOKMARKED") return st.bookmarked;
      return false;
    });

    elNotesReviewList.innerHTML = "";
    if (matching.length === 0) {
      elNotesReviewList.innerHTML = `<p style="color: var(--text-muted); font-size: 0.9rem;">No questions in this category yet. As you answer questions or write personal notes, they will appear here for rapid revision.</p>`;
      return;
    }

    matching.forEach((q) => {
      const st = getEntry(q.id);
      const card = document.createElement("div");
      card.className = "note-card";
      const statusBadge = st.submitted
        ? st.isCorrect
          ? `<span style="color: var(--correct-text); font-weight:700;">✓ Correct</span>`
          : `<span style="color: var(--wrong-text); font-weight:700;">✗ Wrong (Ans: ${q.correct.join(",")})</span>`
        : `<span style="color: var(--text-muted);">Unanswered</span>`;

      card.innerHTML = `
        <div style="display:flex; justify-content:space-between; gap:8px; margin-bottom:6px; font-size:0.8rem;">
          <span><strong>${q.id}</strong> · ${q.subtopic}</span>
          <span>${statusBadge}</span>
        </div>
        <div style="font-size:0.9rem; margin-bottom:8px;">${formatInlineCode(q.stem)}</div>
        ${
          st.note && st.note.trim()
            ? `<div style="background: var(--note-bg); border: 1px solid var(--note-border); padding: 8px 10px; border-radius: 6px; font-size: 0.85rem; color: var(--note-text);"><strong>My Note:</strong> ${formatInlineCode(st.note)}</div>`
            : ""
        }
      `;
      card.addEventListener("click", () => {
        elFilterDomain.value = "ALL";
        populateSubtopics();
        elFilterSubtopic.value = "ALL";
        elFilterDifficulty.value = "ALL";
        elFilterSearch.value = "";
        activeStatusFilter = "ALL";
        elStatusPills.forEach((p) => p.classList.toggle("active", p.dataset.status === "ALL"));
        setMode("PRACTICE");
        const idx = filteredQuestions.findIndex((item) => item.id === q.id);
        if (idx !== -1) {
          currentIndex = idx;
          renderGrid();
          renderCurrentQuestion();
        }
      });
      elNotesReviewList.appendChild(card);
    });
  }

  function setMode(mode) {
    currentMode = mode;
    elTabPractice.classList.toggle("active", mode === "PRACTICE");
    elTabMock.classList.toggle("active", mode === "MOCK");
    elTabNotes.classList.toggle("active", mode === "NOTES");

    elMockBanner.style.display = mode === "MOCK" ? "flex" : "none";
    elQuestionView.style.display = mode === "NOTES" ? "none" : "block";
    elNotesAnalyticsView.style.display = mode === "NOTES" ? "block" : "none";

    if (mode === "MOCK" && mockQuestions.length === 0) {
      startNewMockExam();
    } else if (mode === "NOTES") {
      renderNotesAndAnalytics();
    } else {
      applyFilters();
    }
  }

  // Event Listeners
  elTabPractice.addEventListener("click", () => setMode("PRACTICE"));
  elTabMock.addEventListener("click", () => setMode("MOCK"));
  elTabNotes.addEventListener("click", () => setMode("NOTES"));

  elBtnMockSubmit.addEventListener("click", submitMockExam);
  elBtnMockNew.addEventListener("click", startNewMockExam);
  elNotesViewFilter.addEventListener("change", renderNotesAndAnalytics);

  elFilterDomain.addEventListener("change", () => {
    populateSubtopics();
    currentIndex = 0;
    applyFilters();
  });
  elFilterSubtopic.addEventListener("change", () => {
    currentIndex = 0;
    applyFilters();
  });
  elFilterDifficulty.addEventListener("change", () => {
    currentIndex = 0;
    applyFilters();
  });
  elFilterSearch.addEventListener("input", () => {
    currentIndex = 0;
    applyFilters();
  });

  elStatusPills.forEach((pill) => {
    pill.addEventListener("click", () => {
      activeStatusFilter = pill.dataset.status;
      elStatusPills.forEach((p) => p.classList.toggle("active", p === pill));
      currentIndex = 0;
      applyFilters();
    });
  });

  elBtnPrev.addEventListener("click", () => {
    if (currentIndex > 0) {
      currentIndex--;
      renderGrid();
      renderCurrentQuestion();
    }
  });

  elBtnNext.addEventListener("click", () => {
    if (currentIndex < filteredQuestions.length - 1) {
      currentIndex++;
      renderGrid();
      renderCurrentQuestion();
    }
  });

  elBtnCheckMulti.addEventListener("click", checkMultiSelectNow);
  elBtnRetryOne.addEventListener("click", clearSingleQuestionAttempt);
  elBtnBookmark.addEventListener("click", toggleBookmark);

  elBtnCopyCode.addEventListener("click", () => {
    if (!elQCode.textContent) return;
    navigator.clipboard.writeText(elQCode.textContent).then(() => {
      elBtnCopyCode.textContent = "Copied!";
      setTimeout(() => {
        elBtnCopyCode.textContent = "Copy code";
      }, 1200);
    });
  });

  elNoteInput.addEventListener("input", () => {
    if (filteredQuestions.length === 0) return;
    const q = filteredQuestions[currentIndex];
    const st = getEntry(q.id);
    st.note = elNoteInput.value;
    elNoteStatus.textContent = "Saving note...";
    if (noteSaveTimer) clearTimeout(noteSaveTimer);
    noteSaveTimer = setTimeout(() => {
      persistQuestionState(q.id, elNoteStatus);
      renderGrid();
    }, 250);
  });

  // Export JSON
  elBtnExport.addEventListener("click", () => {
    const payload = {
      exportedAt: new Date().toISOString(),
      totalQuestions: allQuestions.length,
      state: userState,
    };
    const blob = new Blob([JSON.stringify(payload, null, 2)], { type: "application/json" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = `ptca_notes_and_progress_${new Date().toISOString().slice(0, 10)}.json`;
    a.click();
    URL.revokeObjectURL(url);
  });

  // Import JSON
  elInputImport.addEventListener("change", (ev) => {
    const file = ev.target.files && ev.target.files[0];
    if (!file) return;
    const reader = new FileReader();
    reader.onload = async (e) => {
      try {
        const parsed = JSON.parse(String(e.target.result));
        const incoming = parsed.state || parsed;
        if (incoming && typeof incoming === "object") {
          Object.assign(userState, incoming);
          saveToLocalStorage();
          if (backendAvailable) {
            await fetch("/api/bulk_save", {
              method: "POST",
              headers: { "Content-Type": "application/json" },
              body: JSON.stringify({ state: userState }),
            });
          }
          updateGlobalStats();
          applyFilters();
        }
      } catch (err) {
        alert("Could not parse JSON file: " + err.message);
      }
    };
    reader.readAsText(file);
  });

  // Reset Attempts (preserving personal notes!)
  elBtnResetAll.addEventListener("click", async () => {
    if (!confirm("Reset all answered question attempts? (Your personal notes and bookmarks WILL be kept safe!)")) {
      return;
    }
    Object.values(userState).forEach((st) => {
      st.selected = [];
      st.submitted = false;
      st.isCorrect = false;
      st.updatedAt = Date.now() / 1000;
    });
    saveToLocalStorage();
    if (backendAvailable) {
      await fetch("/api/reset", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ keepNotes: true }),
      }).catch(() => {});
    }
    updateGlobalStats();
    applyFilters();
  });

  // Theme Toggle
  function applyTheme(theme) {
    document.documentElement.setAttribute("data-theme", theme);
    elBtnTheme.textContent = theme === "dark" ? "Light Mode" : "Dark Mode";
    try {
      localStorage.setItem(THEME_KEY, theme);
    } catch (_) {}
  }

  elBtnTheme.addEventListener("click", () => {
    const cur = document.documentElement.getAttribute("data-theme") || "light";
    applyTheme(cur === "dark" ? "light" : "dark");
  });

  // Keyboard Navigation (A-D / 1-4, Left/Right, B for bookmark, N for note)
  document.addEventListener("keydown", (e) => {
    const tag = (e.target && e.target.tagName) || "";
    if (tag === "INPUT" || tag === "TEXTAREA" || tag === "SELECT") {
      if (e.key === "Escape") {
        e.target.blur();
      }
      return;
    }
    if (currentMode === "NOTES" || filteredQuestions.length === 0) return;

    const q = filteredQuestions[currentIndex];
    const isMulti = Boolean(q.multi_select || (q.correct && q.correct.length > 1));

    const keyUpper = e.key.toUpperCase();
    if (["A", "B", "C", "D"].includes(keyUpper)) {
      e.preventDefault();
      handleOptionSelect(q, keyUpper, isMulti);
    } else if (["1", "2", "3", "4"].includes(e.key)) {
      e.preventDefault();
      const map = { "1": "A", "2": "B", "3": "C", "4": "D" };
      handleOptionSelect(q, map[e.key], isMulti);
    } else if (e.key === "ArrowRight" || keyUpper === "J") {
      if (currentIndex < filteredQuestions.length - 1) {
        currentIndex++;
        renderGrid();
        renderCurrentQuestion();
      }
    } else if (e.key === "ArrowLeft" || keyUpper === "K") {
      if (currentIndex > 0) {
        currentIndex--;
        renderGrid();
        renderCurrentQuestion();
      }
    } else if (keyUpper === "B") {
      e.preventDefault();
      toggleBookmark();
    } else if (keyUpper === "N") {
      e.preventDefault();
      elNoteInput.focus();
    } else if (e.key === "Enter" && isMulti) {
      e.preventDefault();
      checkMultiSelectNow();
    }
  });

  // Bootstrap
  async function init() {
    const savedTheme = localStorage.getItem(THEME_KEY);
    if (savedTheme === "dark" || savedTheme === "light") {
      applyTheme(savedTheme);
    }

    if (allQuestions.length === 0) {
      try {
        const r = await fetch("questions.json");
        if (r.ok) {
          allQuestions = await r.json();
        }
      } catch (_) {}
    }

    await initStorageSync();
    populateSubtopics();
    updateGlobalStats();
    applyFilters();
  }

  init();
})();
