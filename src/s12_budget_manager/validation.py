"""Input validation and error messages"""

# Imports

from s12_budget_manager.models import Transaction, VALID_KINDS, VALID_INCOME, VALID_EXPENSES, VALID_CURRENCIES
from datetime import date
from decimal import Decimal
from decimal import InvalidOperation

# Functions

def validate_date(raw) -> date:
    try:
        parsed_date = date.fromisoformat(raw.strip())
    except ValueError:
        raise ValueError(f"date '{raw}' is not valid in YYYY-MM-DD format")
    return parsed_date

def validate_kind(raw) -> str:
    parsed_kind = raw.strip().lower()
    if parsed_kind not in VALID_KINDS:
        raise ValueError(f"'{raw}' not valid. Input must be either income or expense")
    return parsed_kind

def validate_category(raw, kind) -> str:
    category = raw.strip().lower()
    if kind == "income":
        allowed_set = VALID_INCOME
    else:
        allowed_set = VALID_EXPENSES
    if category not in allowed_set:
        raise ValueError(f"category '{raw}' is not valid for {kind}.")
    return category

def validate_amount(raw) -> Decimal:
    try:
        parsed_amount = Decimal(raw.strip())
    except InvalidOperation:
        raise ValueError(f"'{raw}' is not a valid amount with 2 decimals. Make sure that the decimal uses '.' and not ','")
    if not parsed_amount.is_finite():
        raise ValueError(f"Finite number is needed.")
    elif parsed_amount <= 0:
        raise ValueError(f"Amount has to be greater than 0, '{raw}' was typed")
    elif parsed_amount.as_tuple().exponent < -2:
        raise ValueError(f"'{raw}' must have at most 2 decimals")
    else:
        return parsed_amount

def validate_currency(raw) -> str:
    parsed_currency = raw.strip().upper()
    if parsed_currency not in VALID_CURRENCIES:
        raise ValueError(f"currency can only be EUR, '{raw}' was given as input")
    return parsed_currency

def build_transaction(id, raw_date, raw_kind, raw_category, raw_amount, raw_currency) -> Transaction:
    date_var = validate_date(raw_date)
    kind_var = validate_kind(raw_kind)
    category_var = validate_category(raw_category, kind_var)
    amount_var = validate_amount(raw_amount)
    currency_var = validate_currency(raw_currency)
    return Transaction(id, date_var, kind_var, category_var, amount_var, currency_var)

