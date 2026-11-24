"""The data the application works with.""" 
# Transaction schema / domain model

# Definition of a transaction

class Transaction:
    def __init__(self, id, date, kind, category, amount, currency):
        self.id = id
        self.date = date
        self.kind = kind
        self.category = category
        self.amount = amount
        self.currency = currency

