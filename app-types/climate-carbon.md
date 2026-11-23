# Climate, carbon and sustainability apps — testing and release playbook

[← All app types](README.md) · [Kenya hub](../kenya/README.md) · [Quality templates](../templates/README.md)

## Product quality goal

Measurement provenance, claims, sensors, reporting and verification.

## High-risk scenarios

1. Missing meter data. Use a synthetic case, expected result, observed result and comparable retest.
2. wrong unit. Use a synthetic case, expected result, observed result and comparable retest.
3. misleading carbon claim. Use a synthetic case, expected result, observed result and comparable retest.
4. double-counted credit. Use a synthetic case, expected result, observed result and comparable retest.
5. offline sync. Use a synthetic case, expected result, observed result and comparable retest.

## Founder testing plan

1. Identify a real target user and a critical task, then define pass/fail before testing.
2. Include an unauthorized access attempt, provider outage, duplicate/retry and accessibility test where relevant.
3. Check Kenyan payment methods, data protection, connectivity, locale and sector permissions if serving Kenya.
4. Document the difference between software QA and any required licensing or expert review.
5. Assign severity, fix owner and versioned retest; do not label unexecuted tests passed.

## Primary references

- [UNFCCC](https://unfccc.int/)
- [EPRA](https://www.epra.go.ke/)

**Scope:** educational QA guidance; market, legal and provider rules must be checked for the specific business.
