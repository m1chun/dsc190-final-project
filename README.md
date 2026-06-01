# Finance Tracker

A command-line tool for tracking personal expenses. Log spending by category
and summarize by day, month, year, or all time. Data is stored locally in your
home directory as a JSON file.

## Usage

### Add an expense
```bash
uv run finance add <description> <amount> <category>
```
Example:
```bash
uv run finance add "coffee" 4.50 food
uv run finance add "uber" 12.00 transport
uv run finance add "netflix" 17.99 subscriptions
```

### Delete an expense
```bash
uv run finance delete <id>
```
Example:
```bash
uv run finance delete 3
```

### Summarize expenses
```bash
uv run finance summary <period>
```
Periods: `day`, `month`, `year`, `all`

Each category shows its total and percentage of overall spending.

Example:
```bash
uv run finance summary month
uv run finance summary year
```

### List recent expenses
```bash
uv run finance list
```
Shows the 10 most recent expenses with their IDs, dates, categories, and amounts.

### Export to CSV
```bash
uv run finance export
uv run finance export --output ~/Desktop/expenses.csv
```
Exports all expenses to a CSV file (default: `expenses.csv` in current directory).

## Installation

```bash
uv add "git+https://github.com/m1chun/dsc190-final-project.git"
```
