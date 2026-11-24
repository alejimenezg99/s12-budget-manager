"""The data the application works with.""" 

# Imports:

from datetime import date
from decimal import Decimal

# Definition of constants such as kind, category and currency

VALID_KINDS = {"income", "expense"}

VALID_INCOME = {"salary", "gifts", "financial", "other"}

VALID_EXPENSES = {"rent", "restaurants", "groceries", "transport", "social", "gifts", "other"}

VALID_CURRENCIES = {"EUR"}


# Definition of a transaction

class Transaction:
    def __init__(self, id: str, date: date, kind: str, category: str, amount: Decimal, currency: str):
        self.id = id
        self.date = date
        self.kind = kind
        self.category = category
        self.amount = amount
        self.currency = currency


