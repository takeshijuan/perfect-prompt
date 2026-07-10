# Bug: CSV export drops rows with commas in the customer name

## Environment

- app version 2.3.1, production

## Steps to reproduce

1. Create a customer named "Acme, Inc."
2. Open Reports > Customers and click Export CSV.
3. Open the downloaded file.

## Expected

One row per customer, with the name quoted: "Acme, Inc."

## Actual

Rows whose customer name contains a comma are split across two lines, and the row count no longer matches the report. Log line: `csv_writer: wrote 118 rows, expected 120`.

## Notes

Export code lives in app/reports/export.py; the writer joins fields with ",".join(...) instead of using the csv module.
