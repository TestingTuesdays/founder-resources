# Religious, faith and community platforms — testing and release playbook

[← All app types](README.md) · [Kenya hub](../kenya/README.md) · [Quality templates](../templates/README.md)

## Product quality goal

Donations, event capacity, volunteer safety, privacy and accessibility.

## High-risk scenarios

1. Recurring donation cancellation. Use a synthetic case, expected result, observed result and comparable retest.
2. mosque/church event signup. Use a synthetic case, expected result, observed result and comparable retest.
3. volunteer role. Use a synthetic case, expected result, observed result and comparable retest.
4. safeguarding report. Use a synthetic case, expected result, observed result and comparable retest.
5. payment refund. Use a synthetic case, expected result, observed result and comparable retest.

## Founder testing plan

1. Identify a real target user and a critical task, then define pass/fail before testing.
2. Include an unauthorized access attempt, provider outage, duplicate/retry and accessibility test where relevant.
3. Check Kenyan payment methods, data protection, connectivity, locale and sector permissions if serving Kenya.
4. Document the difference between software QA and any required licensing or expert review.
5. Assign severity, fix owner and versioned retest; do not label unexecuted tests passed.

## Primary references

- [ODPC](https://www.odpc.go.ke/)
- [W3C WAI](https://www.w3.org/WAI/)

**Scope:** educational QA guidance; market, legal and provider rules must be checked for the specific business.
