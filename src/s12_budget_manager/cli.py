# command-line interaction

# Imports

from s12_budget_manager.storage import load_transactions

# Constant

DATA_PATH = "data/transactions.csv"

def show_menu():
    print("1) Add a transaction")
    print("2) List transactions")
    print("3) Summary of transactions")
    print("4) Exit")

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
            print("Not implemented yet!")
        elif selection == "2":
            print("Not implemented yet!")
        elif selection == "3":
            print("Not implemented yet!")
        elif selection == "4":
            print("Goodbye!")
            break
        else:
            print (f"Invalid option '{selection}'. Choose 1-4")
