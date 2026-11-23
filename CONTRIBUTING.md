# Contributing to Testing Tuesdays Founder Resources

[← Home](README.md) · [Startup perks](perks/README.md) · [Skills](skills/README.md) · [Templates](templates/README.md)

We welcome founders, engineers, UX researchers, QA specialists, translators, accessibility practitioners and Kenyan/African ecosystem partners. The aim is **accurate, actionable, maintainable founder knowledge**, not advertising.

## How to contribute

| I want to… | Open this |
| --- | --- |
| Suggest a useful tool or official resource | [Resource form](.github/ISSUE_TEMPLATE/resource_submission.yml) |
| Submit or correct a startup credit or perk | [Perk form](.github/ISSUE_TEMPLATE/perk_submission.yml) |
| Add a repeatable testing skill | [Skill proposal](.github/ISSUE_TEMPLATE/skill_submission.yml) |
| Correct a broken link or outdated claim | [Correction form](.github/ISSUE_TEMPLATE/correction.yml) |
| Make a prepared edit | [Open a pull request](https://github.com/TestingTuesdays/founder-resources/pulls) |

**Copyable contribution formats:** [Resource submission](templates/resource-submission.md), [Perk research](templates/perk-research.md), [Skill proposal](templates/skill-submission.md), [Private perk tracker](templates/perk-tracker.md).

## Resource editorial standard

Explain the founder problem, target user, prerequisites, practical steps, expected result and failure recovery. Cite the vendor/standards body's own documentation. Describe observed testing versus documentation-only research truthfully. Identify hidden costs and exclusions; include free/community alternatives where useful. Write for someone who may never have used the tool.

## Perk editorial standard

Each entry needs provider, official URL, offer type, advertised maximum **versus typical/conditional award**, eligibility by region and incorporation, company age, funding, partner affiliation, previous credit limitations, services covered, expiry, application deadline, payment/renewal and review date.

Use one of four labels: **Official terms reviewed**, **Program discovery — recheck**, **Lead — offer not verified**, or **Official program discovery**. A tool's normal free tier is not automatically a startup-specific credit. A Nairobi accelerator is not a free unlimited cloud coupon. Member-exclusive Testing Tuesdays perks must be explicitly verified before claiming partnership.

## Pull request quality gates

1. Edit the relevant topic guide and navigation links; for perks update both `perks/catalog.csv` and the readable directory.
2. Keep relative links valid. Run `python3 scripts/check_links.py` and `python3 scripts/validate_perks.py` locally; **do not enable GitHub Actions** for routine docs. See [manual guide](docs/manual-quality-checks.md).
3. Document official sources and the date last reviewed. Never paste large copied source passages.
4. Include an honest practical example, and note what has *not* been verified.
5. Declare affiliate/referral/sponsorship relationships; no paid rankings or undisclosed affiliate links.
6. Never commit passwords, private cohort reports, application details, participant identities or real screenshots containing personal data.
7. Review changes for mobile reading, keyboard accessibility, clear headings, missing links and jargon.
8. Avoid legally ungrounded claims, false compliance certifications or guaranteed credit awards.

## Maintainer review workflow

**Intake → deduplicate → source verify → eligibility/country review → safety/privacy review → edit navigation/data → manual local checks → reviewer approval → merge → schedule recheck.**

Prioritize inaccuracies that could cause billing surprises, dangerous testing, blocked app submission or misleading startup funding expectations. For rapidly changing perks, aim to recheck at least quarterly or sooner after a policy change. Mark an unverified lead honestly instead of removing a useful discovery trail.

## Versioning and maintenance

Keep factual change notes in PRs. Use issue forms for external changes and broken links. Community submissions do not imply endorsement or give contributors access to private participant information. Do not create a sponsor-benefit promise until accepted in writing by both parties.
