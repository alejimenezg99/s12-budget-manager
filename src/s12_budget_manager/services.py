# budget logic: add, filter, summarize

# Imports

from datetime import date
from decimal import Decimal
from s12_budget_manager.models import Transaction
from s12_budget_manager.validation import validate_date, validate_kind, validate_category, validate_amount, validate_currency, build_transaction

# Assign an ID

def transaction_id(transactions) -> str:
    id_num = 0
    for transaction in transactions:
        num = int(transaction.id[1:])
        id_num = max(id_num, num)
    return f"T{id_num+1:03d}"

# Create a new transaction

def add_transaction(transactions, raw_date, raw_kind, raw_category, raw_amount, raw_currency) -> Transaction:
    new_id = transaction_id(transactions)
    new_transaction = build_transaction(new_id, raw_date, raw_kind, raw_category, raw_amount, raw_currency)
    transactions.append(new_transaction)
    return new_transaction

# Filter 1: By kind

def filter_by_kind(transactions, kind) -> list:
    new_list = [transaction for transaction in transactions if transaction.kind == kind]
    return new_list

# Filter 2: Summary of transactions

def summarize(transactions) -> dict:
    income = Decimal("0")
    expense = Decimal("0")
    for transaction in transactions:
        if transaction.kind == "income":
            income += transaction.amount
        else:
            expense += transaction.amount
    return {"Income": income, "Expenses": expense, "Balance" : income - expense}

# Filter 3: Total expenses by category

def totals_by_category(transactions) -> dict:
    totals_by = dict()
    for transaction in transactions:
        if transaction.category not in totals_by.keys():
            totals_by[transaction.category] = Decimal("0")
        totals_by[transaction.category] += transaction.amount
    return totals_by
