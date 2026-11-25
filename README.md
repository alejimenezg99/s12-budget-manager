# Budget Manager
A Python program designed for recording income, expenses and creating simple summaries.

## Setup
Python version 3.14 is required and uv with its command `uv sync`.

## Run

* Setup: `uv sync`
* Try with sample data (optional): `cp data/sample_transactions.csv data/transactions.csv`
* Run: `uv run s12-budget-manager`

## Example

```
$ uv run s12-budget-manager
Skipped 6 invalid rows
Row 4: date '2026-02-30' is not valid in YYYY-MM-DD format
...
Type the number corresponding to an option from above: 3
Income: 5550, Expenses: 456.29, Balance: 5093.71
Expenses by category:
Rent, 200
Groceries, 145.30
...
```

## Test

Run each test file from the project folder:

```
uv run python tests/test_validation.py
uv run python tests/test_services.py
```

Each test file prints `All tests passed!` if every check succeeds. If a check fails, Python shows an `AssertionError` with the line that failed.

## Known limitations

* Amounts in scientific notation (e.g. `1e30`) are accepted.
* Dates without dashes (e.g. `20260904`) are accepted.
* If day and month are swapped and both are ≤ 12 (e.g. `2026-04-09` meant as 4 September), the date is accepted as typed.
* The currency error message says "EUR" literally; it does not update if more currencies are added.
* After `T999`, ids grow to 4 digits (`T1000`).
* Duplicate ids inside the CSV are not detected; both rows are loaded.
* Only the first error per row is reported.
* Invalid rows reported at load time are dropped on the next save.
* When adding a transaction, all fields are requested before validation; if one is invalid, the user must start again.

## Exit ticket

* What did you verify? The amount test fails when given a valid value ("12"): the safety net works.
* Which boundary changed your design? `2026-02-30`: correct format but impossible date; the error message was changed because it wrongly said the format was wrong.
* What would you refactor next? In Release 2, validate each field as soon as it is typed in `add_flow`, so the user only re-enters the wrong value instead of all five.
