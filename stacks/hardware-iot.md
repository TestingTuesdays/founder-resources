# IoT / firmware / device dashboards — testing framework recipe

[← Stack index](README.md) · [User research](../research/README.md) · [Evidence standard](../docs/quality-evidence-standard.md)

## Recommended framework layers

pytest; hardware-in-loop bench tests; MQTT clients; Playwright.

## What to test at each layer

Firmware: unit and simulated sensor tests; integration: telemetry replay and reconnection; E2E: device onboarding, alerts and dashboard.

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

Test OTA rollback, power loss, stale data and physical safety on an isolated bench before field trials.

## Official references

- [Zephyr testing](https://docs.zephyrproject.org/latest/develop/test/index.html)
- [MQTT](https://mqtt.org/)
- [OWASP IoT](https://owasp.org/www-project-internet-of-things/)

These are selection starting points; tool compatibility and supported versions must be checked against the project's installed stack.
