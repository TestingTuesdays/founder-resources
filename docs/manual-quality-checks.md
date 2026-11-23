# Zero-CI documentation and product quality checks

[← Home](../README.md) · [Contribution guide](../CONTRIBUTING.md)

## Why no automatic GitHub Actions?

This resource repository is documentation-first. The previously configured push/PR Actions job was removed to conserve GitHub Actions minutes. **No workflow is required to publish Markdown updates.**

## Run locally when editing the repository

From repository root using a local Python 3 installation:

```sh
python3 scripts/check_links.py
python3 scripts/validate_perks.py
```

These checks consume no GitHub-hosted runner minutes. They verify **local Markdown links** and **perks catalog format**, not the availability of all external URLs, award eligibility, correctness of a claim, or website deployment.

## Manual editorial review

1. Inspect changed Markdown on mobile-width preview; keep descriptive headings and visible link text.
2. Check that the README, category list, skill index and contribution docs link to new pages.
3. Confirm tool names, official URLs and eligibility are not copied from outdated promotions.
4. Check in-context dates and avoid unsupported rankings, discounts or compliance claims.
5. Keep user research, account data, invoices and credentials out of public issues and commits.
6. For new perks, update catalog CSV, readable directory and Kenya shortlist when relevant.
7. Request peer review for security, medical, privacy and policy-sensitive guidance.

## Review without automation

Review diffs in GitHub; for new link targets, click relative links. Run both scripts on a contributor's local machine and paste the result in PR description. Maintainers can merge after manual review; CI is not a dependency. Review again if provider terms change.

## Audit consistency before publishing

- Compare README counts and navigation with the actual repository tree; never preserve stale totals.
- Check every skill's frontmatter `name`, `description`, topic link, required inputs, safety limits and expected output.
- Check every perks row against the readable directory and distinguish confirmed terms from unverified leads.
- Test that issue templates open through GitHub's **New issue** interface; links to raw YAML are source references, not forms.
- Do not re-enable hosted GitHub Actions without explicit approval.

## Local HTML metadata check

For an HTML export or saved server-rendered page, run:

```sh
python3 scripts/audit_static_html.py path/to/site --json
python3 -m unittest discover -s scripts -p 'test_audit_static_html.py'
```

These are local heuristics, not live crawling, indexing proof or a guarantee of search rankings. Keep GitHub Actions disabled.

## Avoid stale counts in navigation

Do not place hard-coded counts of skills, documents, tools or app types in headers and link labels. Prefer descriptive section names so navigation stays accurate when contributors add material. Procedural steps may remain numbered when order matters.

Use the [quality evidence standard](quality-evidence-standard.md) to separate plans from executed results.

## Market profitability local model

```sh
python3 scripts/market_profitability.py data/market-profitability-example.csv --json
python3 -m unittest discover -s scripts -p 'test_market_profitability.py'
```

The fixtures are synthetic. These checks require no GitHub Actions and do not validate commercial assumptions, tax or market rankings.
