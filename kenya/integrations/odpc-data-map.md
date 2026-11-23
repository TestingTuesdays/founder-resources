# ODPC-ready personal-data inventory and vendor map

[← Kenya hub](../README.md) · [Integration index](README.md) · [Test case template](../../templates/test-case.md)

## Why this matters

Data protection begins with understanding the actual records, access and processors.

## Step-by-step founder workflow

1. List each field collected, why, lawful basis to verify and user population.
2. Identify controllers/processors, cloud regions, third parties and transfer destinations.
3. Classify sensitive records, children and any high-risk automated decisions.
4. Record retention and deletion behavior including backups and analytics.
5. Test subject access, correction, withdrawal and deletion with synthetic accounts.
6. Review whether registration, DPIA or notification requirements apply to the business.
7. Have qualified local reviewer sign off unresolved obligations.

## Required test evidence

| Scenario | Expected state | Actual result | Severity | Owner / retest |
| --- | --- | --- | --- | --- |
| Successful authorized path | Documented expected outcome | Not run | | |
| Provider/network timeout | Safe retry or pending | Not run | | |
| Duplicate event/request | One logical outcome | Not run | | |
| Unauthorized or malformed input | Safely denied | Not run | | |
| Reversal/cleanup where relevant | Consistent records | Not run | | |

## Official starting points

- [ODPC](https://www.odpc.go.ke/)
- [Kenya Law](https://new.kenyalaw.org/)

**Scope:** this is a test and implementation planning guide, not a live integration, guaranteed merchant onboarding, regulatory certification or legal/tax advice. Provider contracts, credentials, callbacks and current rules must be verified for the actual account.

_Last curated: 2026-11-23._
