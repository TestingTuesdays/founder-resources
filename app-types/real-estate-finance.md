# Property investment and rent-finance apps — testing and release playbook

[← All app types](README.md) · [Kenya hub](../kenya/README.md) · [Quality templates](../templates/README.md)

## Product quality goal

Investor suitability, title verification, rent collection, disputes and disclosures.

## High-risk scenarios

1. Unverified property listing. Use a synthetic case, expected result, observed result and comparable retest.
2. duplicate rent. Use a synthetic case, expected result, observed result and comparable retest.
3. investor promise. Use a synthetic case, expected result, observed result and comparable retest.
4. KYC. Use a synthetic case, expected result, observed result and comparable retest.
5. repayment timing. Use a synthetic case, expected result, observed result and comparable retest.

## Founder testing plan

1. Identify a real target user and a critical task, then define pass/fail before testing.
2. Include an unauthorized access attempt, provider outage, duplicate/retry and accessibility test where relevant.
3. Check Kenyan payment methods, data protection, connectivity, locale and sector permissions if serving Kenya.
4. Document the difference between software QA and any required licensing or expert review.
5. Assign severity, fix owner and versioned retest; do not label unexecuted tests passed.

## Primary references

- [Capital Markets Authority Kenya](https://www.cma.or.ke/)
- [Kenya Lands Ministry](https://lands.go.ke/)

**Scope:** educational QA guidance; market, legal and provider rules must be checked for the specific business.
