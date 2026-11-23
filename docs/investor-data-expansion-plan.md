# Investor data qualification and expansion backlog

[← Investor catalog](../investors/README.md) · [Methodology](../investors/qualification-method.md)

## Proposed entities

Investors (canonical name, type, sector, stage, geography, status); funds (vintage, mandate, size, source); companies (entity, website, operating countries); deals (investor, company, date, round, amount, source, direct versus LP versus debt); accelerators and grants (eligibility, deadlines, award type); founder education; social platform formats.

## Publication gates

- Verify Kenya investment from official portfolio or dated announcement, not just pan-African mandate.
- Preserve `unknown` for ticket size, current fund deployment, application route or contact not independently verified.
- Do not mix LP/fund commitments, debt, equity and accelerator awards.
- Require source URL, checked date, canonical ID, status and editor for promoted records.
- Add a local CSV validator, deduplication and contributor submission form.
- Build a filterable static directory by sector, stage, instrument, country and evidence status after data quality review.
- Keep GitHub Actions disabled; validate locally.

## Delivery issues

Schema normalization; evidence backfill; sector coverage; current fund checks; official portfolio research; investor outreach data separation; static searchable UI; source freshness. No claim of exhaustive coverage until audited.

## Tracking issue

[GitHub issue #1 — qualified Kenya investor and startup data system](https://github.com/TestingTuesdays/founder-resources/issues/1) tracks source validation, normalization, sector coverage, local quality checks and a searchable directory. No GitHub Actions will be enabled.
