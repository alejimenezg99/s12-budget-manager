"""Tests for the services functions."""

# Imports

from decimal import Decimal
from s12_budget_manager.services import transaction_id, add_transaction, filter_by_kind, summarize, totals_by_category

# 1. First id of an empty list

assert transaction_id([]) == "T001"

# 2. Gap in ids: next id is based on the largest, not on the length

gap_list = []
add_transaction(gap_list, "2026-09-04", "expense", "groceries", "10", "EUR")
add_transaction(gap_list, "2026-09-05", "expense", "rent", "500", "EUR")
add_transaction(gap_list, "2026-09-06", "income", "salary", "1000", "EUR")
gap_list.pop(1)
assert transaction_id(gap_list) == "T004"

# 3. Invalid data does not leave anything in the list

invalid_list = []
try:
    add_transaction(invalid_list, "2026-09-04", "expense", "groceries", "-5", "EUR")
    assert False, "should have raised ValueError"
except ValueError as e:
    assert "greater than 0" in str(e)
assert len(invalid_list) == 0

# 4. Summary of an empty list

empty_summary = summarize([])
assert empty_summary["Income"] == Decimal("0")
assert empty_summary["Expenses"] == Decimal("0")
assert empty_summary["Balance"] == Decimal("0")

# 5. Summary with one income and one expense

summary_list = []
add_transaction(summary_list, "2026-09-04", "income", "salary", "1000", "EUR")
add_transaction(summary_list, "2026-09-05", "expense", "groceries", "18.50", "EUR")
summary = summarize(summary_list)
assert summary["Income"] == Decimal("1000")
assert summary["Expenses"] == Decimal("18.50")
assert summary["Balance"] == Decimal("981.50")

# 6. Totals by category only for expenses

category_list = []
add_transaction(category_list, "2026-09-04", "expense", "groceries", "10", "EUR")
add_transaction(category_list, "2026-09-05", "expense", "groceries", "5.50", "EUR")
add_transaction(category_list, "2026-09-06", "income", "gifts", "50", "EUR")
expense_totals = totals_by_category(filter_by_kind(category_list, "expense"))
assert expense_totals["groceries"] == Decimal("15.50")
assert "gifts" not in expense_totals

print("All tests passed!")
