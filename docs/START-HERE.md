# Founder start guide

[← Home](../README.md) · [Release gate](release-readiness.md) · [Test catalog](test-case-catalog.md)

## A product is ready to test when someone can perform a real task

Testing Tuesdays is a Nairobi-based, contribution-first testing community developed with Web3Clubs Nairobi. Bring a **working** MVP, functional beta, live app or safely demonstrable device—not a pitch alone. Founder cohort admission requires organizer approval and a reviewed outgoing product test first, unless an organizer grants an explicit exception. A referral or RSVP does not reserve a testing seat. [Program overview](https://app.notion.com/p/420c1f4ba97e81528057d64c6a5115c0).

## Practical session and launch resources

- [Testing Tuesdays session kit](testing-tuesdays-session-kit.md)
- [Founder launch-week checklist](founder-launch-week.md)
- [Recovery and error-state patterns](error-states-library.md)
- [Additional specialist guides](extended-topics.md)

## Your 60-minute quality audit

1. **10 min:** Write your top three user tasks, success criteria, likely failures and target audience.
2. **15 min:** Ask someone in the actual audience to complete one neutral task. Observe without teaching.
3. **10 min:** Test invalid inputs, wrong credentials, timeout, retry, empty result and cancellation.
4. **10 min:** Use a phone, keyboard, large text and an assistive-technology spot check.
5. **10 min:** Review errors, authorization boundaries, private data, slow connections and monitoring.
6. **5 min:** File the three most important findings; assign owner and comparable retest.

## Find your path

| Product type | Start with |
| --- | --- |
| New consumer web app | [Usability](usability.md), [Accessibility](accessibility.md), [Analytics](analytics-experiments.md) |
| B2B SaaS | [SaaS](saas.md), [Security](security-privacy.md), [Automation](qa-automation.md) |
| iOS/Android app | [Mobile app stores](mobile-app-stores.md), [Accessibility](accessibility.md) |
| AI product/agent | [AI evaluations](ai-evaluation.md), [Security](security-privacy.md) |
| Marketplace/community | [Consumer & marketplace](consumer-marketplace.md), [Security](security-privacy.md) |
| Connected device | [Hardware & IoT](hardware-connected.md), [Reliability](performance.md) |
| International product | [Localization](localization.md), [Accessibility](accessibility.md) |

## A complete report answers

What did they try? What did we expect? What really happened? On which build/device? How often and how harmful? Who owns the fix? Did a comparable retest improve the result?

**Never** upload customer data, API keys, private recordings or participant identifiers into this public repository. Use safe synthetic data, restricted records and consent-based research. [Copyable templates](../templates/README.md).
