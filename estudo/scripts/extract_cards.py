"""Scans estudo/progress/*.md and appends new flashcards to cards/cards.json.

Existing cards (matched by id) are left untouched, so SM-2 state survives
re-runs after you edit a progress file.
"""

import hashlib
import json
import re
from datetime import date
from pathlib import Path

PROGRESS_DIR = Path(__file__).resolve().parent.parent / "progress"
CARDS_FILE = Path(__file__).resolve().parent.parent / "cards" / "cards.json"

SECTION_ORIGIN = {
    "Mistakes (become high-priority flashcards)": "mistake",
    "Key-concept flashcards (always generated, regardless of mistakes)": "concept",
}

QA_PATTERN = re.compile(
    r"-\s*Q:\s*(?P<question>.+?)\n\s*A:\s*(?P<answer>.+?)(?=\n-\s*Q:|\n##|\Z)",
    re.DOTALL,
)


def card_id(stage: str, question: str) -> str:
    digest = hashlib.sha1(question.strip().lower().encode("utf-8")).hexdigest()[:10]
    return f"{stage}-{digest}"


def parse_stage_file(path: Path) -> list[dict]:
    text = path.read_text(encoding="utf-8")
    stage = path.stem
    cards = []

    for heading, origin in SECTION_ORIGIN.items():
        section_match = re.search(
            rf"##\s*{re.escape(heading)}\s*\n(?P<body>.*?)(?=\n##|\Z)", text, re.DOTALL
        )
        if not section_match:
            continue
        body = section_match.group("body")
        for qa in QA_PATTERN.finditer(body):
            question = qa.group("question").strip()
            answer = qa.group("answer").strip()
            if question == "..." or answer == "...":
                continue
            cards.append(
                {
                    "id": card_id(stage, question),
                    "question": question,
                    "answer": answer,
                    "stage": stage,
                    "origin": origin,
                }
            )
    return cards


def main() -> None:
    CARDS_FILE.parent.mkdir(parents=True, exist_ok=True)
    existing = json.loads(CARDS_FILE.read_text(encoding="utf-8")) if CARDS_FILE.exists() else {}

    today = date.today().isoformat()
    added = 0

    for path in sorted(PROGRESS_DIR.glob("*.md")):
        if path.name == "_template.md":
            continue
        for card in parse_stage_file(path):
            if card["id"] in existing:
                continue
            existing[card["id"]] = {
                **card,
                "created": today,
                "due": today,
                "repetitions": 0,
                "interval": 0,
                "easiness": 2.5,
            }
            added += 1

    CARDS_FILE.write_text(json.dumps(existing, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"{added} new card(s) added. Total: {len(existing)}.")


if __name__ == "__main__":
    main()
