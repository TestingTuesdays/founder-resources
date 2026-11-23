# Cross-channel attribution and distribution metrics

[← Distribution operations](README.md) · [Experiment worksheet](../../templates/distribution-experiment.md)

## Goal

Avoid counting the same user as a conversion multiple times.

## Practical execution

1. Define source, medium, campaign, creative and content IDs consistently.
2. Instrument server-confirmed signup, activation, purchase and retention separately.
3. Capture attribution consent and avoid personal identifiers in URLs.
4. Test direct traffic, missing UTM, app-store transitions and delayed payments.
5. Reconcile platform-reported conversions with backend events and refunds.
6. Review CAC, payback, retention, complaints and uncertainty by country and channel.

## Evidence and stop conditions

| Item | Record |
| --- | --- |
| Segment and country | Actual buyer and market, not broad population |
| Hypothesis | Specific behavior and expected result |
| Source | Official provider/policy source and checked date |
| Creative | Version, language, disclosure and rights |
| Attribution | UTM, server event and consent mechanism |
| Success | Qualified activation and retained value event |
| Guardrails | Complaints, refunds, safety, CAC and privacy |
| Decision | Continue, revise, stop or inconclusive |

Do not invent campaign results or assume platform algorithms, payment access or local licensing. Compare outcomes against the original hypothesis and record the owner.

[Reusable skill](../../skills/distribution-measurement/SKILL.md).
