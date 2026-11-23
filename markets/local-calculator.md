# Offline market profitability calculator

[← Markets](README.md) · [Modeling framework](profitability-framework.md) · [Example input](../data/market-profitability-example.csv)

A **dependency-free Python 3** calculator compares market-specific *user-supplied* assumptions. No API keys, external data feeds, hosted CI or claimed country profitability.

```sh
python3 scripts/market_profitability.py data/market-profitability-example.csv
python3 scripts/market_profitability.py data/market-profitability-example.csv --json
python3 -m unittest discover -s scripts -p 'test_market_profitability.py'
```

Input columns: `market,currency,price,variable_cost,cac,customers,fixed_cost,refund_loss,retained_fraction`. All monetary values in the **same currency and period** per row. `retained_fraction` is between 0 and 1; `customers` is the cohort acquired in the period. Compare markets only after normalizing currencies and comparable periods externally.

The model reports contribution per customer, after-CAC contribution, expected retained customer count, period net contribution after acquisition and fixed cost, and a simplistic fixed-cost break-even threshold. **Do not confuse that break-even with a full cash-flow model**: retention is a single-period factor, CAC is charged to all acquired customers, and the script excludes tax, debt, working capital, FX conversions and multi-period LTV. The sample markets are entirely synthetic.

A successful calculation does not verify its inputs. Run a paid pilot and source-review before investment decisions. No GitHub Actions are enabled.
