#!/usr/bin/env python3
"""Offline single-period cohort economics. User-provided assumptions only; no market data."""
import argparse
import csv
import json
from decimal import Decimal, InvalidOperation, ROUND_CEILING
from pathlib import Path

FIELDS = ("price", "variable_cost", "cac", "customers", "fixed_cost", "refund_loss", "retained_fraction")
def dec(row, key):
    try:
        value = Decimal(str(row[key]))
    except (KeyError, InvalidOperation, TypeError) as exc:
        raise ValueError(f"Invalid or missing {key}") from exc
    if not value.is_finite() or value < 0:
        raise ValueError(f"{key} must be finite and nonnegative")
    return value

def model(row):
    v = {key: dec(row, key) for key in FIELDS}
    if v["retained_fraction"] > 1:
        raise ValueError("retained_fraction must be between 0 and 1")
    if v["customers"] != v["customers"].to_integral_value():
        raise ValueError("customers must be a whole number")
    currency = str(row.get("currency", "")).strip()
    market = str(row.get("market", "")).strip()
    if not market or not currency:
        raise ValueError("market and currency are required")
    contribution = v["price"] - v["variable_cost"] - v["refund_loss"]
    acquired_margin = contribution - v["cac"]
    effective_per_acquired = v["retained_fraction"] * contribution - v["cac"]
    retained_customers = v["customers"] * v["retained_fraction"]
    period_net = v["customers"] * effective_per_acquired - v["fixed_cost"]
    # Break-even must use the same retention/CAC assumptions as period net.
    break_even = (v["fixed_cost"] / effective_per_acquired).to_integral_value(rounding=ROUND_CEILING) if effective_per_acquired > 0 else None
    return {
        "market": market,
        "currency": currency,
        "contribution_per_retained_customer": str(contribution),
        "after_acquisition_per_customer_before_retention": str(acquired_margin),
        "expected_retained_customers": str(retained_customers),
        "net_per_acquired_customer_after_retention_and_cac": str(effective_per_acquired),
        "period_net_contribution_after_acquisition_and_fixed_cost": str(period_net),
        "break_even_acquired_customers_in_this_period": str(break_even) if break_even is not None else None,
        "assumptions": "Single-period illustration: all acquired customers incur CAC; only retained fraction contributes revenue; excludes tax, debt, working capital, FX and multi-period LTV",
    }

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("csv_path", type=Path)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    try:
        with args.csv_path.open(encoding="utf-8-sig", newline="") as stream:
            reader = csv.DictReader(stream)
            if not reader.fieldnames or not all(x in reader.fieldnames for x in FIELDS + ("market", "currency")):
                ap.error("Missing required columns: " + ", ".join(("market", "currency") + FIELDS))
            results = [model(row) for row in reader]
    except (OSError, UnicodeError, csv.Error, ValueError) as exc:
        ap.error(str(exc))
    if not results:
        ap.error("No market rows")
    if args.json:
        print(json.dumps(results, indent=2))
    else:
        for row in results:
            print(f"{row['market']} ({row['currency']}): period net = {row['period_net_contribution_after_acquisition_and_fixed_cost']}; break-even acquired customers = {row['break_even_acquired_customers_in_this_period'] or 'not attainable'}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
