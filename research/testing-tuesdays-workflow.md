# Testing Tuesdays research-to-shipping workflow

[← Research hub](README.md) · [Session kit](../docs/testing-tuesdays-session-kit.md)

## Before a session

Founder submits product URL/build, intended user, one task, sandbox credentials (shared privately, never in public GitHub), constraints and feedback contact. Organizer matches testers based on task relevance and access needs; do not guarantee attendance or acceptance.

## During testing

- Confirm consent and recording choices.
- Ask participant to attempt task unassisted; observe actual result.
- Record anonymized context, device/network, blocker and exact reproduction path.
- Ask neutral follow-up questions; avoid soliciting positive ratings.
- End with one prioritized issue and a retest plan.

## After testing

| State | Meaning | Required evidence |
| --- | --- | --- |
| New | Observation submitted | Task, build and source |
| Triaged | Reviewed for impact | Severity, owner, reproduction |
| In progress | Fix assigned | Issue/branch reference |
| Ready for retest | Fix deployed | Build and environment |
| Verified | Comparable test passed | Retest observation |
| Reopened | Failure remains | Updated reproduction |
| Closed without fix | Explicit decision | Reason and owner |

## Founder deliverable

A short ship-back note with original problem, fix, deployed version, retest result and remaining limitations. Publish only non-identifying summaries with permission. Keep participant records in private systems and honor retention/deletion practices.
