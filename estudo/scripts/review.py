"""Interactive CLI: reviews every flashcard due today using SM-2."""

import json
import sys
from datetime import date, timedelta
from pathlib import Path

from sm2 import schedule

sys.stdout.reconfigure(encoding="utf-8")

CARDS_FILE = Path(__file__).resolve().parent.parent / "cards" / "cards.json"


def load_cards() -> dict:
    if not CARDS_FILE.exists():
        return {}
    return json.loads(CARDS_FILE.read_text(encoding="utf-8"))


def save_cards(cards: dict) -> None:
    CARDS_FILE.write_text(json.dumps(cards, indent=2, ensure_ascii=False), encoding="utf-8")


def main() -> None:
    cards = load_cards()
    today = date.today()
    due = [c for c in cards.values() if date.fromisoformat(c["due"]) <= today]
    due.sort(key=lambda c: c["due"])

    if not due:
        print("Nenhum flashcard pendente hoje.")
        return

    print(f"{len(due)} flashcard(s) pendente(s).\n")

    for card in due:
        print(f"[{card['stage']} | {card['origin']}]")
        print(f"Q: {card['question']}")
        input("(Enter pra ver a resposta) ")
        print(f"A: {card['answer']}")

        quality = None
        while quality is None:
            raw = input("Sua nota de 0 (esqueceu) a 5 (lembrou fácil): ").strip()
            if raw.isdigit() and 0 <= int(raw) <= 5:
                quality = int(raw)
            else:
                print("Digite um número de 0 a 5.")

        repetitions, interval, easiness = schedule(
            quality, card["repetitions"], card["interval"], card["easiness"]
        )
        card["repetitions"] = repetitions
        card["interval"] = interval
        card["easiness"] = round(easiness, 2)
        card["due"] = (today + timedelta(days=interval)).isoformat()

        print(f"-> próxima revisão em {interval} dia(s).\n")
        save_cards(cards)

    print("Revisão concluída.")


if __name__ == "__main__":
    main()
