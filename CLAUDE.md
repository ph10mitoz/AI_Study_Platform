# AI Study Book — Project Context

## Who I am
- Engineering student at IME (Rio de Janeiro), 4th semester as of Nov 2026.
- Already covered the math foundations of the ML track (calculus, linear algebra, probability) — verify with a quick diagnostic before each stage, do not assume.
- Long-term goal: ML/deep learning/data science for international projects, summer research (e.g. ETH Student Summer Research Fellowship via SiROP) and research in Rio.

## How you (Claude Code) must work with me
- Tone: sincere and direct. No filler, no automatic praise for my ideas. Act as an expert consultant; rely on facts, not invented theory. Say when I am wrong.
- Answers: not too long, but well explained.
- When I ask for a plan or suggestion: analyze facts, then end with a short briefing.
- **Teach first, code second.** For every chapter/task: (1) explain the concept and the math, (2) give me a practical exercise/project tied to that content, (3) I write my own solution and my own prediction BEFORE any AI-written code, (4) only then compare with an AI solution and review mine (correctness, edge cases, complexity) — this comparison is also what feeds my level assessment (junior/pleno/senior) per area.
- Never hand me a full solution before I attempted it, unless I explicitly ask.
- Log my mistakes in `progress/` for the review record, but flashcards are not mistake-only: every chapter/task generates flashcards from its key concepts (definitions, formulas, core ideas) automatically, regardless of whether I got the exercise right. These go into spaced repetition (SM-2) and must be reachable at any time, not just when I'm on that chapter — in the platform this is a dedicated "Flashcards" view/tab.

## Learning goal
Understand AI from scratch: the math behind it, from the moment a model is trained to the moment it answers. Then the tools of ML/DL and AI development (PyTorch, Hugging Face, FastAPI, Docker, experiment tracking, LLM APIs, agents, MCP). Every topic comes with a practical exercise or project.

## The platform being built
A local flashcard + Q&A platform to keep topics active and record what I study, and to evaluate my progress per area.
- Phase 1: Markdown files + a small Python script that extracts key-concept flashcards from each chapter/task (plus mistake logs as review notes), with spaced repetition (SM-2).
- Phase 2: web app (FastAPI + lightweight frontend), then database and logins only when there is content worth logging into.

## Targets
- Inputs (main score, weekly): projects shipped, commits, one public write-up per project.
- Outcomes (bonus, monthly): GitHub stars, LinkedIn views, real logins on my app, revenue (last, small targets such as 10 real logins).

## The three fronts (one product, built incrementally)
A shared context (this file + `estudo/ROADMAP.md` + `estudo/progress/`) drives three fronts, each its own folder, each at a different maturity:
- `estudo/` — the study track. Has a concrete next step, build here first.
- `oportunidades/` — curated collection of scholarships/exchanges/programs (ML/DL/AI/data science), adaptive to my profile and what I'm learning. Idea-stage only, see its README.
- `noticias/` — curated digest (not raw feed) of specific labs/authors I follow, reviewed with summary + link, tied to my current study stage. Idea-stage only, see its README.
Cross-linking is intentional: a finished chapter can unlock a related opportunity/news item; an opportunity with a near deadline can reprioritize what to study next. The link runs through the shared context, not directly between items.

## Files
- `estudo/ROADMAP.md` — stages, workflow per chapter, level rubric.
- `estudo/SOURCES.md` — where to collect study material (loose list).
- `estudo/CONTENT_LIBRARY.md` — verified catalog of real sources, mapped to roadmap stages.
- `estudo/progress/` — one file per stage (my prediction, my code, AI comparison, mistakes, flashcards).
- `estudo/cards/` — generated flashcards (key concepts + mistakes), reviewed via SM-2, reachable any time regardless of current stage.
- `estudo/scripts/` — Phase 1 tools, stdlib-only Python, no web framework: `extract_cards.py` parses `progress/*.md` into `cards/cards.json` (idempotent, by id); `review.py` runs the SM-2 review loop for whatever is due; `sm2.py` is the scheduling algorithm; `build_dashboard.py` renders `CONTENT_LIBRARY.md` into `estudo/dashboard/index.html`, a static read-only page (search + filter by verification status) to review source quality without digging through raw markdown. Full Phase 2 (FastAPI + real frontend) only after the per-chapter workflow proves out with real content.
- `estudo/mockup/index.html` — **visual mockup only**, hand-written static HTML/CSS/JS, no server, no real backend, no real AI evaluation. Built to let me judge the intended UI (Trilha/Flashcards/Progresso, per-chapter Conteúdo/Cursos/Atividades/Projeto tabs, level that updates as "evaluations" are simulated) before committing to real Phase 2 infra. State lives in `localStorage` only (per-browser, fake). Content inside uses the real Track 1 catalog (IMPA GPT series + Karpathy Zero to Hero) so the layout judgment is meaningful, but nothing here is wired to real progress data — do not treat anything in this file as a source of truth for actual study progress.
- `oportunidades/README.md`, `noticias/README.md` — design notes for the other two fronts, not yet built.
