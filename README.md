# Finance Tracker

A command-line tool for tracking personal expenses. Log spending by category
and summarize by day, month, year, or all time. Data is stored locally in your
home directory.

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

### Summarize expenses
```bash
uv run finance summary <period>
```
Periods: `day`, `month`, `year`, `all`

Example:
```bash
uv run finance summary month
```

### List recent expenses
```bash
uv run finance list
```

## Installation

```bash
uv add "git+https://github.com/<your-username>/dsc190-final-project.git"
```
