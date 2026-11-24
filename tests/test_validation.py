"""Tests for the validations functions."""

# Imports

from datetime import date
from decimal import Decimal
from s12_budget_manager.validation import validate_date, validate_kind, validate_category, validate_amount, validate_currency, build_transaction

# 1. Tests on build_transaction function

test = build_transaction("T001", "2026-09-04", "expense", "groceries", "18.50", "eur")
assert test.amount == Decimal("18.50")
assert test.currency == "EUR"
assert test.date == date(2026, 9, 4)
assert test.category == "groceries"

#2. Test on errors

try:
    validate_amount("0")
    assert False, "should have raised ValueError"
except ValueError as e:
    assert "greater than 0" in str(e)

try:
    validate_amount("Twelve")
    assert False, "should have raised ValueError"
except ValueError as e:
    assert "not a valid amount" in str(e)

try:
    validate_category("rent", "income")
    assert False, "should have raised ValueError"
except ValueError as e:
    assert "not valid for income" in str(e)

print("All tests passed!")