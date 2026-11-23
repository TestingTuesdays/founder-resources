#!/usr/bin/env python3
"""Offline country/segment profitability model; all inputs supplied by founder, no invented market data."""
import argparse
import csv
import json
from decimal import Decimal, InvalidOperation
from pathlib import Path

FIELDS = ("price", "variable_cost", "cac", "customers", "fixed_cost", "refund_loss", "retained_fraction")
def dec(row, key):
    try:
        x = Decimal(str(row[key]))
    except (KeyError, InvalidOperation, TypeError) as exc:
        raise ValueError(f"Invalid or missing {key}") from exc
    if not x.is_finite() or x < 0:
        raise ValueError(f"{key} must be finite and nonnegative")
    return x

def model(row):
    values = {k: dec(row, k) for k in FIELDS}
    if values["retained_fraction"] > 1:
        raise ValueError("retained_fraction must be between 0 and 1")
    price, cost, cac = (values[k] for k in ("price", "variable_cost", "cac"))
    refund = values["refund_loss"]
    customers = values["customers"]
    fixed = values["fixed_cost"]
    retained = values["retained_fraction"]
    contribution = price - cost - refund
    acquired_margin = contribution - cac
    retained_customers = customers * retained
    period_net = retained_customers * contribution - customers * cac - fixed
    return {
        "market": row.get("market", "unspecified"),
        "currency": row.get("currency", "unspecified"),
        "contribution_per_customer": str(contribution),
        "after_acquisition_per_customer": str(acquired_margin),
        "expected_retained_customers": str(retained_customers),
        "period_net_contribution_after_acquisition_and_fixed_cost": str(period_net),
        "break_even_customers_if_positive_contribution": str(fixed / contribution) if contribution > 0 else None,
        "assumptions": "Single-period illustrative model; retained_fraction applies to this period only, no tax or capital modeling",
    }

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv_path", type=Path)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    with args.csv_path.open(encoding="utf-8-sig", newline="") as fp:
        reader = csv.DictReader(fp)
        if not reader.fieldnames or not all(x in reader.fieldnames for x in FIELDS):
            parser.error("Missing required columns: " + ", ".join(FIELDS))
        try:
            results = [model(row) for row in reader]
        except ValueError as exc:
            parser.error(str(exc))
    if not results:
        parser.error("No market rows")
    if args.json:
        print(json.dumps(results, indent=2))
    else:
        for r in results:
            print(f"{r['market']} ({r['currency']}): period net contribution = {r['period_net_contribution_after_acquisition_and_fixed_cost']}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
