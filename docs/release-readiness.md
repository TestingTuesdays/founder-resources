# Production release gate

[← Home](../README.md) · [Checklist template](../templates/release-checklist.md)

A launch is a **reversible, monitored product change**. Passing CI does not mean users can finish the task.

## Before shipping

- [ ] Three core journeys work from clean accounts on representative devices.
- [ ] Invalid, empty, error, loading, timeout, denied-permission and offline states are usable.
- [ ] Customer-facing copy, support, terms and privacy disclosures reflect actual behavior.
- [ ] Keyboard, screen reader, zoom and high-contrast checks cover critical flows.
- [ ] Auth, server-side object permissions, multi-tenancy, secrets, rate limits and dependencies checked.
- [ ] Payments, retries, refunds, webhook signatures and cancellation tested if applicable.
- [ ] Realistic slow-network and performance baseline recorded.
- [ ] Mobile/app-store or jurisdiction-specific regulations reviewed where relevant.
- [ ] Backup restore, reversible migration, rollback and error monitoring verified.
- [ ] Deployment owner, alerts, support contact, go/no-go decision and retest named.

## Severity guide

| Level | Meaning | Action |
| --- | --- | --- |
| P0 | Sensitive data exposure, money/data loss, unsafe result, unusable core task without workaround | Block launch |
| P1 | High-impact common task, serious accessibility/reliability issue | Fix before broad release |
| P2 | Material friction with viable workaround | Track with owner and date |
| P3 | Low-impact cosmetic issue | Backlog |

After deployment, smoke test with synthetic data, monitor real usage and crashes, and retest the original issue. An issue marked **closed** is not proof of resolution until behavior is verified.
