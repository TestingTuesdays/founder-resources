# Quality evidence standard for founder resources

[← Documentation](README.md) · [Contributing](../CONTRIBUTING.md)

## What counts as evidence

- **Observed:** test actually executed on a named build/environment, with expected and actual result.
- **Reproduced:** defect repeated under recorded conditions.
- **Fixed:** implementation changed but not necessarily verified.
- **Retested:** comparable scenario run on new build and result recorded.
- **Not attempted:** scenario exists but has no execution evidence.
- **Unknown:** data or source insufficient for a conclusion.

## Required fields

| Field | Example without private data |
| --- | --- |
| Scenario | PAY-KEN-02: duplicate callback |
| Build | Git SHA or release identifier |
| Environment | Provider sandbox, synthetic order |
| Expected | One logical ledger transition |
| Actual | Not attempted / observed behavior |
| Impact | Money, privacy, safety, accessibility or task blockage |
| Owner | Role or private issue reference |
| Retest | Build and outcome, if performed |

## Editorial depth

Guides should explain *why a failure matters*, prerequisites, normal and failure paths, realistic acceptance criteria, localization/accessibility, limitations and primary sources. Avoid repetitive generic sentences that add no actionable information. Numbering steps is fine for procedures; **do not hard-code counts of docs, skills, tools or app categories into section titles** because those counts become stale.

## Review and maintenance

Check local links and perks catalog manually. No hosted GitHub Actions are configured. External provider terms and laws need source review at time of use. Never publish customer data or imply testing occurred when it did not.
