# Offline market profitability calculator

[← Markets](README.md) · [Modeling framework](profitability-framework.md) · [Synthetic example input](../data/market-profitability-example.csv)

The dependency-free Python 3 calculator accepts **founder-supplied assumptions only**. It is a **single-period acquisition cohort** model, not a real market ranking, LTV forecast or tax computation.

```sh
python3 scripts/market_profitability.py data/market-profitability-example.csv
python3 scripts/market_profitability.py data/market-profitability-example.csv --json
python3 -m unittest discover -s scripts -p 'test_market_profitability.py'
```

Required columns: `market,currency,price,variable_cost,cac,customers,fixed_cost,refund_loss,retained_fraction`. Monetary values must use the **same currency and period** per row. `customers` is a nonnegative integer of newly acquired customers; `retained_fraction` ranges from 0 to 1.

## Exact interpretation

- **Contribution per retained customer** = price − variable cost − refund loss.
- **Expected retained customers** = acquired customers × retained fraction.
- **Net per acquired customer** = retained fraction × contribution per retained customer − CAC.
- **Period net** = acquired customers × net per acquired customer − fixed cost.
- **Break-even acquired customers** = round up(fixed cost / net per acquired customer), *only when net per acquired customer is positive*. Otherwise there is no finite break-even under the assumptions.

The break-even calculation now uses the **same retention and acquisition assumptions** as the period net. Earlier versions divided fixed cost by pre-acquisition contribution and could give a misleading break-even count.

The model assumes all acquired customers incur CAC, while only retained customers generate this period's revenue. It excludes taxes, debt, working capital, FX conversion, delayed collections, changing cohorts and multi-period LTV. Different currencies cannot be ranked by raw amounts.

The fixture is entirely synthetic. Validate the underlying data with paid pilots and accounting review. The presence of tests does not establish that they have run. GitHub Actions remains disabled.
