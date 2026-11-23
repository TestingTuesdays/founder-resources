# Qualifying and maintaining Kenya investor data

[← Investors](README.md) · [Issue proposal](../docs/investor-data-expansion-plan.md)

## Verification levels

- **Official portfolio evidence:** fund's own site identifies a Kenya company or investment; record URL and company.
- **Official strategy verified; Kenya deal unverified:** official site establishes stage/sector/Africa mandate but not a specific Kenyan deal.
- **Research lead:** third-party ecosystem directory or name recognition; no primary deal confirmation yet.
- **Closed/inactive:** evidence of fund closure or strategy change; preserve historical entry but remove active claim.

## Required fields for each record

Canonical investor name, type, stage, sector tags, geography, ticket size (if officially published), latest fund, Kenya deal example, announcement date, primary source, source checked date, investment status (verified/unverified), current application route, restrictions, confidence, owner and next review date.

## Investor fit scoring (research aid, not objective truth)

| Criterion | 0 | 1 | 2 |
| --- | --- | --- | --- |
| Geography | Excluded | Pan-African, unconfirmed | Explicit Kenya mandate or Kenya portfolio |
| Stage | Outside mandate | Unknown | Published match |
| Sector | Excluded | Broad/unclear | Explicit match |
| Check size | Outside range | Unknown | Published range fits round |
| Recent deployment | No evidence | Historic only | Dated primary announcement within research window |

Score 0–10 and store underlying evidence. **A high score is not a guarantee of investment**. Do not penalize missing data as evidence of rejection; flag as unknown. Maintain separate outreach and diligence status from fit.

## Source workflow

1. Start with official investor website, portfolio, fund announcement and regulatory disclosures.
2. Identify the exact fund and investing entity, not just a parent brand.
3. Find a specific Kenya deal and date. If only an aggregator supports it, label unverified.
4. Record stage, sector and ticket only when supported; otherwise mark unknown.
5. Deduplicate aliases and distinguish direct equity, debt, accelerator awards and LP investments.
6. Recheck at outreach and on a quarterly editorial schedule; record owner and change history.
7. Never publish private email addresses, nonpublic investment terms or sensitive founder information.

## Quality gate for public promotion

Only promote a lead to **Kenya investment verified** with primary-source evidence or two credible independent sources explicitly naming investor, company, geography and transaction. Record the evidence date. Label current deployment **unverified** unless current fund statements substantiate it.
