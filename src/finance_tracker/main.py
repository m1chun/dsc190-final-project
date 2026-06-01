import argparse
from datetime import datetime
from . import db


def cmd_add(args):
    expense = db.add_expense(args.description, args.amount, args.category)
    print(f"✅ Added: {expense['description']} — ${expense['amount']:.2f} [{expense['category']}]")


def cmd_summary(args):
    period = args.period
    expenses = db.get_expenses(period)

    if not expenses:
        print(f"No expenses found for: {period}")
        return

    label = {"day": "Today", "month": "This Month", "year": "This Year", "all": "All Time"}[period]
    total = sum(e["amount"] for e in expenses)

    print(f"\n📊 {label} Summary")
    print("=" * 40)

    # Group by category
    by_category = {}
    for e in expenses:
        by_category.setdefault(e["category"], []).append(e)

    for cat, items in sorted(by_category.items()):
        cat_total = sum(i["amount"] for i in items)
        print(f"\n  {cat.upper()} (${cat_total:.2f})")
        for item in items:
            date = datetime.fromisoformat(item["date"]).strftime("%b %d")
            print(f"    {date}  {item['description']:<25} ${item['amount']:.2f}")

    print("\n" + "=" * 40)
    print(f"  TOTAL: ${total:.2f}")
    print()


def cmd_list(args):
    expenses = db.get_expenses("all")
    if not expenses:
        print("No expenses logged yet.")
        return
    recent = expenses[-10:][::-1]
    print(f"\n{'ID':<5} {'Date':<12} {'Description':<25} {'Category':<12} {'Amount':>8}")
    print("-" * 65)
    for e in recent:
        date = datetime.fromisoformat(e["date"]).strftime("%b %d, %Y")
        print(f"{e['id']:<5} {date:<12} {e['description']:<25} {e['category']:<12} ${e['amount']:>7.2f}")
    print()


def main():
    parser = argparse.ArgumentParser(prog="finance", description="Personal Finance Tracker")
    subparsers = parser.add_subparsers(dest="command")

    # add
    add_parser = subparsers.add_parser("add", help="Add an expense")
    add_parser.add_argument("description", type=str)
    add_parser.add_argument("amount", type=float)
    add_parser.add_argument("category", type=str)

    # summary
    summary_parser = subparsers.add_parser("summary", help="Summarize expenses")
    summary_parser.add_argument("period", choices=["day", "month", "year", "all"])

    # list
    subparsers.add_parser("list", help="List recent expenses")

    args = parser.parse_args()

    if args.command == "add":
        cmd_add(args)
    elif args.command == "summary":
        cmd_summary(args)
    elif args.command == "list":
        cmd_list(args)
    else:
        parser.print_help()