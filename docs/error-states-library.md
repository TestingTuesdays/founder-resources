# Error, empty, loading and recovery states every founder should test

[← Founder resources](../README.md) · [Test catalog](test-case-catalog.md)

| State | User-facing expectation | Typical test |
| --- | --- | --- |
| First-run empty state | Explain the next action in plain language | New account with no records |
| Zero search results | Offer useful filters or alternative | Deliberately unmatched query |
| Loading beyond expected time | Clear progress, no false success | Slow network |
| Client validation error | Explain and preserve entered data | Invalid required field |
| Server rejection | Safe message and recovery | Invalid/expired token |
| Expired login | Avoid silent data loss; offer secure re-auth | Mid-form expiration |
| Permission denied | Explain limitation without leaking another user's details | Attempt unauthorized action |
| Offline | Explain queued vs unavailable actions | Disconnect during task |
| Partial upload | Resumable/restartable status | Interrupted file transfer |
| Payment pending | No premature entitlement; safe status | Delayed provider event |
| Duplicate submission | Prevent unintended double action | Rapid click/replay |
| Background job failure | Track retry, owner and user-visible status | Queue outage |
| Rate limit | Bounded retry and actionable message | Controlled 429 test |
| Deleted or unavailable record | Safe 404/410-style recovery | Old shared link |
| Critical incident | User communication and support route | Controlled outage drill |

## Accessibility and internationalization

Make errors programmatically associated with fields, announce status where appropriate, preserve focus and avoid color-only meaning. Test localization, long strings, RTL where applicable and low-literacy clarity. Error messages should not disclose stack traces, secrets or sensitive existence checks.

## Acceptance criteria

For every state, record trigger, expected behavior, actual behavior, recovery action, accountable owner, severity, affected device and retest. The best error page cannot replace a safe backend state.

[W3C form errors](https://www.w3.org/WAI/tutorials/forms/notifications/) · [OWASP Error Handling Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Error_Handling_Cheat_Sheet.html).
