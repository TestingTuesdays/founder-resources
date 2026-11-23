#!/usr/bin/env python3
"""Unit tests for local market economics calculations."""
import unittest
from market_profitability import model

BASE = {"market":"Synthetic","currency":"USD","price":"100","variable_cost":"25","cac":"50","customers":"10","fixed_cost":"100","refund_loss":"0","retained_fraction":"1"}

class MarketTests(unittest.TestCase):
    def test_basic(self):
        r = model(BASE)
        self.assertEqual(r["contribution_per_customer"], "75")
        self.assertEqual(r["after_acquisition_per_customer"], "25")
        self.assertEqual(r["period_net_contribution_after_acquisition_and_fixed_cost"], "150")
    def test_retention(self):
        r = model({**BASE, "retained_fraction":"0.5"})
        self.assertEqual(r["expected_retained_customers"], "5.0")
        self.assertEqual(r["period_net_contribution_after_acquisition_and_fixed_cost"], "-225.0")
    def test_no_break_even_on_negative_contribution(self):
        r = model({**BASE,"price":"10"})
        self.assertIsNone(r["break_even_customers_if_positive_contribution"])
    def test_reject_invalid(self):
        for bad in ({"retained_fraction":"1.1"},{"cac":"-1"},{"price":"NaN"}):
            with self.assertRaises(ValueError):
                model({**BASE,**bad})

if __name__ == "__main__":
    unittest.main()
