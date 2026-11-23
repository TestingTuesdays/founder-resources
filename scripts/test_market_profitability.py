#!/usr/bin/env python3
"""Regression tests for local single-period profitability calculations."""
import unittest
from market_profitability import model

BASE = {"market": "Synthetic", "currency": "USD", "price": "100", "variable_cost": "25", "cac": "50", "customers": "10", "fixed_cost": "100", "refund_loss": "0", "retained_fraction": "1"}

class MarketTests(unittest.TestCase):
    def test_full_retention(self):
        r = model(BASE)
        self.assertEqual(r["contribution_per_retained_customer"], "75")
        self.assertEqual(r["net_per_acquired_customer_after_retention_and_cac"], "25")
        self.assertEqual(r["period_net_contribution_after_acquisition_and_fixed_cost"], "150")
        self.assertEqual(r["break_even_acquired_customers_in_this_period"], "4")
    def test_half_retention_is_unprofitable_per_acquired_customer(self):
        r = model({**BASE, "retained_fraction": "0.5"})
        self.assertEqual(r["period_net_contribution_after_acquisition_and_fixed_cost"], "-225.0")
        self.assertIsNone(r["break_even_acquired_customers_in_this_period"])
    def test_break_even_rounds_up(self):
        r = model({**BASE, "cac": "20", "fixed_cost": "101"})
        self.assertEqual(r["break_even_acquired_customers_in_this_period"], "2")
    def test_no_break_even_if_negative_contribution(self):
        self.assertIsNone(model({**BASE, "price": "10"})["break_even_acquired_customers_in_this_period"])
    def test_reject_invalid(self):
        for bad in ({"retained_fraction": "1.1"}, {"cac": "-1"}, {"price": "NaN"}, {"customers": "1.5"}, {"market": ""}):
            with self.subTest(bad=bad), self.assertRaises(ValueError):
                model({**BASE, **bad})

if __name__ == "__main__":
    unittest.main()
