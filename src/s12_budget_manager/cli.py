# command-line interaction

# Imports

from s12_budget_manager.storage import load_transactions, save_transactions
from s12_budget_manager.services import add_transaction, summarize, totals_by_category, filter_by_kind

# Constant

DATA_PATH = "data/transactions.csv"

# Function with Menu printed

def show_menu():
    print("1) Add a transaction")
    print("2) List transactions")
    print("3) Summary of transactions")
    print("4) Exit")

# Add a new transaction from user input

def add_flow(transactions):
    raw_date = input("Date (YYYY-MM-DD): ")
    raw_kind = input("Kind (income/expense): ")
    raw_category = input("Category from defined fields: ")
    raw_amount = input("Positive amount in #.#0 format (e.g. 18.50): ")
    raw_currency = input("Currency (EUR): ")
    try:
        new_transaction = add_transaction(transactions, raw_date, raw_kind, raw_category, raw_amount, raw_currency)
        save_transactions(DATA_PATH, transactions)
        print(f"Added {new_transaction.id}")
    except ValueError as e:
        print(f"Error: {e}")

# Listing all transactions

def list_flow(transactions):
    if len(transactions) == 0:
        print("No transactions yet.")
    else:
        for transaction in transactions:
            print(f"{transaction.id} {transaction.date} {transaction.kind} {transaction.category} {transaction.amount} {transaction.currency}")

# Create a report

def summary_flow(transactions):
    summary = summarize(transactions)
    print(f"Income: {summary["Income"]}, Expenses: {summary["Expenses"]}, Balance: {summary["Balance"]}")
    total_by_cat = totals_by_category(filter_by_kind(transactions, "expense"))
    print("Expenses by category:")
    for category, amount in total_by_cat.items():
        print(f"{category.capitalize()}, {amount}")

# Main function

def main():
    transactions, errors = load_transactions(DATA_PATH)
    if len(errors) > 0:
        print (f"Skipped {len(errors)} invalid rows")
        for e in errors:
            print(e)
    while True:
        show_menu()
        selection = input("Type the number corresponding to an option from above: ").strip()
        if selection == "1":
            add_flow(transactions)
        elif selection == "2":
            list_flow(transactions)
        elif selection == "3":
            summary_flow(transactions)
        elif selection == "4":
            print("Goodbye!")
            break
        else:
            print (f"Invalid option '{selection}'. Choose 1-4")
