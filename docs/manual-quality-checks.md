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
