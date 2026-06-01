import json
import os
from datetime import datetime
from pathlib import Path

DATA_FILE = Path.home() / ".finance_tracker.json"


def load_data() -> list[dict]:
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE) as f:
        return json.load(f)


def save_data(data: list[dict]) -> None:
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)


def add_expense(description: str, amount: float, category: str) -> dict:
    data = load_data()
    expense = {
        "id": len(data) + 1,
        "description": description,
        "amount": amount,
        "category": category,
        "date": datetime.now().isoformat(),
    }
    data.append(expense)
    save_data(data)
    return expense


def get_expenses(period: str = "all") -> list[dict]:
    data = load_data()
    now = datetime.now()

    if period == "day":
        return [e for e in data if datetime.fromisoformat(e["date"]).date() == now.date()]
    elif period == "month":
        return [e for e in data if
                datetime.fromisoformat(e["date"]).year == now.year and
                datetime.fromisoformat(e["date"]).month == now.month]
    elif period == "year":
        return [e for e in data if datetime.fromisoformat(e["date"]).year == now.year]
    return data