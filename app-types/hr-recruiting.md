# Hiring, recruiting and HR systems — testing and release playbook

[← All app types](README.md) · [Kenya hub](../kenya/README.md) · [Quality templates](../templates/README.md)

## Product quality goal

Candidate privacy, fair screening, permissions, contracts and retention.

## High-risk scenarios

1. Duplicate applications. Use a synthetic case, expected result, observed result and comparable retest.
2. bias in ranking. Use a synthetic case, expected result, observed result and comparable retest.
3. export permissions. Use a synthetic case, expected result, observed result and comparable retest.
4. offer expiry. Use a synthetic case, expected result, observed result and comparable retest.
5. right-to-delete request. Use a synthetic case, expected result, observed result and comparable retest.

## Founder testing plan

1. Identify a real target user and a critical task, then define pass/fail before testing.
2. Include an unauthorized access attempt, provider outage, duplicate/retry and accessibility test where relevant.
3. Check Kenyan payment methods, data protection, connectivity, locale and sector permissions if serving Kenya.
4. Document the difference between software QA and any required licensing or expert review.
5. Assign severity, fix owner and versioned retest; do not label unexecuted tests passed.

## Primary references

- [ODPC](https://www.odpc.go.ke/)
- [ILO](https://www.ilo.org/)

**Scope:** educational QA guidance; market, legal and provider rules must be checked for the specific business.
