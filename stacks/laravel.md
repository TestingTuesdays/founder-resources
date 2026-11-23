# Laravel / PHP — testing framework recipe

[← Stack index](README.md) · [User research](../research/README.md) · [Evidence standard](../docs/quality-evidence-standard.md)

## Recommended framework layers

Pest or PHPUnit; Laravel HTTP tests; Dusk where appropriate.

## What to test at each layer

Unit: services and policies; feature: HTTP routes, queues, mail and database; browser: payment and onboarding journey.

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

Use RefreshDatabase and fake notifications/payments; verify authorization policies and queued retries.

## Official references

- [Laravel testing](https://laravel.com/docs/testing)
- [Pest](https://pestphp.com/)
- [Laravel Dusk](https://laravel.com/docs/dusk)

These are selection starting points; tool compatibility and supported versions must be checked against the project's installed stack.
