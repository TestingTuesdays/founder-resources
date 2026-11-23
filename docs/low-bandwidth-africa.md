# Low-bandwidth, older devices and Nairobi user conditions

[← Resource home](../README.md) · [Release gate](release-readiness.md) · [Testing templates](../templates/README.md)

## For whom

Consumer, marketplace, education, civic and fintech products serving mixed networks and older phones.

## The failure you are trying to prevent

Product quality is about actual user outcomes, not only whether a build compiles. Verify a realistic journey and the ways it can fail, then retest after changes.

## Common mistakes

- Only testing on expensive Wi-Fi-connected hardware
- Large JavaScript bundles, hero videos or unnecessary polling
- Forms losing state after network drops or payment redirects
- Assuming English-only flows or one payment method
- Confusing offline replay with duplicate submissions

## Run this test plan

1. **Simulate slow cellular, high latency and intermittent packet loss.** Record version/environment, starting state, expected result, actual observation, impact, owner and retest outcome.
2. **Test on an older low-memory Android device with limited storage.** Record version/environment, starting state, expected result, actual observation, impact, owner and retest outcome.
3. **Start a long form offline; reconnect and verify preservation and idempotency.** Record version/environment, starting state, expected result, actual observation, impact, owner and retest outcome.
4. **Check whether low-data mode, image compression or text fallback works.** Record version/environment, starting state, expected result, actual observation, impact, owner and retest outcome.
5. **Use realistic East African names, phone input and locale formats.** Record version/environment, starting state, expected result, actual observation, impact, owner and retest outcome.
6. **Test service interruptions without generating duplicate orders, payments or alerts.** Record version/environment, starting state, expected result, actual observation, impact, owner and retest outcome.

## Working method

**Prepare:** select three high-risk tasks and a realistic device, account and permission profile. Use fictional data; do not disclose user recordings, credentials or restricted company information.

**Observe:** run both successful and failure/recovery paths. Distinguish a user's observed behavior from the researcher's proposed solution.

**Prioritize:** flag data loss, harm, exposed private information and blocked primary user actions before cosmetic problems. Record any accepted risk with an accountable owner.

**Verify:** deploy a versioned fix, repeat the same task under comparable conditions and record improved/unchanged/worse/pending outcome.

## Official documentation and useful tools

| Reference | When it helps |
| --- | --- |
| [Chrome DevTools network throttling](https://developer.chrome.com/docs/devtools/network/) | Primary documentation, methods or diagnostics |
| [WebPageTest](https://www.webpagetest.org/) | Primary documentation, methods or diagnostics |
| [web.dev performance](https://web.dev/learn/performance) | Primary documentation, methods or diagnostics |
| [Android Vitals](https://developer.android.com/topic/performance/vitals) | Primary documentation, methods or diagnostics |
| [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/) | Primary documentation, methods or diagnostics |
| [Workbox](https://developer.chrome.com/docs/workbox) | Primary documentation, methods or diagnostics |

## Completion evidence

A per-device/network matrix, observed failures, traffic budget and recovery design with comparable retests.

## Don't overclaim

A single pass does not prove all users, devices, jurisdictions or failure conditions are covered. Tool limits and external rules evolve. Recheck official sources before a regulated or commercially consequential release.

_Last curated: 2026-11-23._
