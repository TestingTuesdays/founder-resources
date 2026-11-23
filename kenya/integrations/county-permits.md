# County permits, field operations and regulated marketplace discovery

[← Kenya hub](../README.md) · [Integration index](README.md) · [Test case template](../../templates/test-case.md)

## Why this matters

A national website does not settle county permits or physical business licensing.

## Step-by-step founder workflow

1. Describe where physical goods/services are provided and by whom.
2. List each county of operations and the specific physical activity.
3. Identify county permits and sector regulator approvals potentially relevant.
4. Confirm whether platform is a directory, seller, intermediary or regulated operator.
5. Document source, current fee/expiry if verified, authority and owner.
6. Avoid making approval claims until confirmed by responsible office or counsel.
7. Retest operational workflows after approval conditions change.

## Required test evidence

| Scenario | Expected state | Actual result | Severity | Owner / retest |
| --- | --- | --- | --- | --- |
| Successful authorized path | Documented expected outcome | Not run | | |
| Provider/network timeout | Safe retry or pending | Not run | | |
| Duplicate event/request | One logical outcome | Not run | | |
| Unauthorized or malformed input | Safely denied | Not run | | |
| Reversal/cleanup where relevant | Consistent records | Not run | | |

## Official starting points

- [Kenya Law](https://new.kenyalaw.org/)
- [Kenya Government](https://www.kenya.go.ke/)

**Scope:** this is a test and implementation planning guide, not a live integration, guaranteed merchant onboarding, regulatory certification or legal/tax advice. Provider contracts, credentials, callbacks and current rules must be verified for the actual account.

_Last curated: 2026-11-23._
