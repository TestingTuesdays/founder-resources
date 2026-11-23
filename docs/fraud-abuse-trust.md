# Fraud, abuse, moderation and platform trust

[← Resource home](../README.md) · [Release gate](release-readiness.md) · [Testing templates](../templates/README.md)

## For whom

Marketplaces, community apps, fintech, social products and services with user-generated content.

## The failure you are trying to prevent

Product quality is about actual user outcomes, not only whether a build compiles. Verify a realistic journey and the ways it can fail, then retest after changes.

## Common mistakes

- No response path for harassment, spam or account takeovers
- Only client-side blocking, leaving API access open
- Moderators seeing excessive personal data
- False positives with no appeal or audit trail
- Not testing payment disputes or seller impersonation

## Run this test plan

1. **Block user and enforce on API/messages/search.** Record version/environment, starting state, expected result, actual observation, impact, owner and retest outcome.
2. **Report content and test acknowledgement/triage.** Record version/environment, starting state, expected result, actual observation, impact, owner and retest outcome.
3. **Rate-limit repeated fraudulent signup or messaging.** Record version/environment, starting state, expected result, actual observation, impact, owner and retest outcome.
4. **Test moderator least privilege and audit history.** Record version/environment, starting state, expected result, actual observation, impact, owner and retest outcome.
5. **Appeal an incorrect action and restore state if approved.** Record version/environment, starting state, expected result, actual observation, impact, owner and retest outcome.
6. **Simulate charge disputes and duplicate refunds in sandbox.** Record version/environment, starting state, expected result, actual observation, impact, owner and retest outcome.

## Working method

**Prepare:** select three high-risk tasks and a realistic device, account and permission profile. Use fictional data; do not disclose user recordings, credentials or restricted company information.

**Observe:** run both successful and failure/recovery paths. Distinguish a user's observed behavior from the researcher's proposed solution.

**Prioritize:** flag data loss, harm, exposed private information and blocked primary user actions before cosmetic problems. Record any accepted risk with an accountable owner.

**Verify:** deploy a versioned fix, repeat the same task under comparable conditions and record improved/unchanged/worse/pending outcome.

## Official documentation and useful tools

| Reference | When it helps |
| --- | --- |
| [OWASP Automated Threats](https://owasp.org/www-project-automated-threats-to-web-applications/) | Primary documentation, methods or diagnostics |
| [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/) | Primary documentation, methods or diagnostics |
| [Stripe fraud docs](https://docs.stripe.com/radar) | Primary documentation, methods or diagnostics |
| [Google Play UGC policy entry](https://support.google.com/googleplay/android-developer/) | Primary documentation, methods or diagnostics |
| [Apple Review Guidelines](https://developer.apple.com/app-store/review/guidelines/) | Primary documentation, methods or diagnostics |

## Completion evidence

Abuse-case table, moderator role model, enforcement and appeals checks, and incident ownership.

## Don't overclaim

A single pass does not prove all users, devices, jurisdictions or failure conditions are covered. Tool limits and external rules evolve. Recheck official sources before a regulated or commercially consequential release.

_Last curated: 2026-11-23._
