# B2B SaaS and enterprise admin — testing and release playbook

[← All app types](README.md) · [Kenya hub](../kenya/README.md) · [Quality templates](../templates/README.md)

## Product quality goal

SSO/SAML, seats, roles, audit trails, tenant isolation, invoices, enterprise onboarding.

## High-risk scenarios

1. Invited member removed. Use a synthetic case, expected result, observed result and comparable retest.
2. role changed. Use a synthetic case, expected result, observed result and comparable retest.
3. tenant export. Use a synthetic case, expected result, observed result and comparable retest.
4. annual invoice. Use a synthetic case, expected result, observed result and comparable retest.
5. data retention. Use a synthetic case, expected result, observed result and comparable retest.
6. support impersonation. Use a synthetic case, expected result, observed result and comparable retest.

## Founder testing plan

1. Identify a real target user and a critical task, then define pass/fail before testing.
2. Include an unauthorized access attempt, provider outage, duplicate/retry and accessibility test where relevant.
3. Check Kenyan payment methods, data protection, connectivity, locale and sector permissions if serving Kenya.
4. Document the difference between software QA and any required licensing or expert review.
5. Assign severity, fix owner and versioned retest; do not label unexecuted tests passed.

## Primary references

- [OWASP ASVS](https://asvs.owasp.org/)
- [OpenID Connect](https://openid.net/developers/how-connect-works/)

**Scope:** educational QA guidance; market, legal and provider rules must be checked for the specific business.
