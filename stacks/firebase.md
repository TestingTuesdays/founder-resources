# Firebase / Firestore / Cloud Functions — testing framework recipe

[← Stack index](README.md) · [User research](../research/README.md) · [Evidence standard](../docs/quality-evidence-standard.md)

## Recommended framework layers

Firebase Emulator Suite; Rules Unit Testing; Jest/Vitest.

## What to test at each layer

Security rules: user A cannot read B; functions: retries and idempotency; E2E: auth, offline persistence and account deletion.

## Suggested smoke-test matrix

| Scenario | Layer | Expected outcome | Evidence |
| --- | --- | --- | --- |
| Core user task | E2E on representative device | Unassisted completion | Not run |
| Validation and empty states | Unit/component | Clear, accessible recovery | Not run |
| Unauthorized cross-account access | Integration/API | Server denies | Not run |
| Provider timeout or duplicate event | Integration | Safe retry and one logical outcome | Not run |
| Slow mobile network | E2E/device | Preserved state and truthful status | Not run |
| Fix regression | Same layer as original defect | Previous failure no longer reproducible | Not run |

## Setup and release workflow

1. Choose one unit runner, one integration approach and one end-to-end runner rather than adding every tool.
2. Create deterministic synthetic fixtures and isolated test services.
3. Automate the critical paths locally; retain manual moderated user testing for comprehension and accessibility.
4. Capture build SHA, command, environment, expected/actual result and redacted evidence.
5. Fix, retest and release only after the risk owner approves. GitHub Actions remain intentionally disabled in this resource repository.

## Stack-specific caution

Run Firestore/Auth emulators locally and use seeded fixtures; never confuse emulator acceptance with deployed rules.

## Official references

- [Firebase Emulator Suite](https://firebase.google.com/docs/emulator-suite)
- [Security Rules tests](https://firebase.google.com/docs/rules/unit-tests)

These are selection starting points; tool compatibility and supported versions must be checked against the project's installed stack.
