import json
import csv
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

DATA_FILE = Path.home() / ".finance_tracker.json"


def load_data() -> List[Dict]:
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE) as f:
        return json.load(f)


def save_data(data: List[Dict]) -> None:
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)


def add_expense(description: str, amount: float, category: str) -> Dict:
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


def delete_expense(expense_id: int) -> Optional[Dict]:
    data = load_data()
    match = next((e for e in data if e["id"] == expense_id), None)
    if not match:
        return None
    data = [e for e in data if e["id"] != expense_id]
    save_data(data)
    return match


def get_expenses(period: str = "all") -> List[Dict]:
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


def export_to_csv(filepath: str) -> int:
    data = load_data()
    if not data:
        return 0
    with open(filepath, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "date", "description", "category", "amount"])
        writer.writeheader()
        writer.writerows(data)
    return len(data)
