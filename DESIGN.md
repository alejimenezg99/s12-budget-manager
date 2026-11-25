# Design rationale

All validation rules live in one module, `validation.py`, and every transaction is created through a single entry point, `build_transaction`, whether it comes from the user typing in the CLI or from a row in the CSV file. I chose this because validation scattered across several functions tends to produce inconsistent rules: the same amount could be accepted from the menu and rejected from the file. With one entry point, an invalid value is rejected in the same way and with the same actionable message wherever it comes from, and the rules can be tested in one place without the menu or any file. The other layers stay simple: `services.py` applies business logic only to transactions that are already valid, `storage.py` only reads and writes the file, and `cli.py` only asks for input and shows results or error messages.

## Other decisions

* `Decimal` instead of `float` for money (avoids 0.1 + 0.2 errors).
* Unknown categories are rejected, never silently mapped to `other` (never silently correct ambiguous data).
* Separate category sets for income and expense; category validation depends on kind.
* `totals_by_category` receives an already filtered list so income and expense categories (e.g. `gifts`) are not mixed.
* The CLI writes to `data/transactions.csv`, so the sample file is never overwritten.
* `restval=""` in `DictReader` so incomplete rows produce a validation message instead of a crash.
