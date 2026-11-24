"""Load and save CSV files with transactions"""

# Imports
import csv
from pathlib import Path
from s12_budget_manager.validation import build_transaction

# Define a constant that has the attributes of a Transaction

FIELDNAMES = ["id", "date", "kind", "category", "amount", "currency"]

# Define a function that save transactions into a csv

def save_transactions(path, transactions):
    with open (path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(FIELDNAMES)
        for transaction in transactions:
            writer.writerow([transaction.id, transaction.date, transaction.kind, transaction.category, transaction.amount, transaction.currency])

# Define a function that reads a csv of transactions

def load_transactions(path):
    transactions = []
    errors = []
    if not Path(path).exists():
        return transactions, errors
    with open (path, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f, restval="")
        for row_number, row in enumerate(reader, start=2):
            try:
                new_transaction = build_transaction(row["id"], row["date"], row["kind"], row["category"], row["amount"], row["currency"])
                transactions.append(new_transaction)
            except ValueError as e:
                errors.append(f"Row {row_number}: {e}")
    return transactions, errors
