# Regulated products & legal release considerations

[← Resource home](../README.md) · [Release checklist](release-readiness.md)

## Why founders should care

Security, privacy, consumer, medical, child, fintech and local market rules may impose additional obligations.

## Common mistakes

- Assuming a successful demo or dashboard proves the experience works for all users.
- Ignoring errors, permission boundaries, mobile constraints and exceptional states.
- Launching without a responsible owner, observable outcome or fallback.
- Using vendor tooling without checking costs, data protection or real capabilities.

## Core test scenarios

1. **Determine markets, user age and regulated functions before release.** Record build/environment, expected vs actual, user impact and follow-up.
2. **Document personal data flows and lawful basis/consent where applicable.** Record build/environment, expected vs actual, user impact and follow-up.
3. **Verify payment/store disclosures and cancellation terms.** Record build/environment, expected vs actual, user impact and follow-up.
4. **Check accessibility obligations for target jurisdiction.** Record build/environment, expected vs actual, user impact and follow-up.
5. **Review child safety and age assurance where applicable.** Record build/environment, expected vs actual, user impact and follow-up.
6. **Medical/financial decision support has qualified domain review and appropriate safeguards.** Record build/environment, expected vs actual, user impact and follow-up.

## Practical workflow

1. Identify the most important user task and a measurable success criterion.
2. Use safe synthetic data and a representative device/locale/account.
3. Test the expected route **and** failure/recovery case; observe results, not assumptions.
4. Check privacy/security, accessibility and reliability considerations where relevant.
5. File a reproducible issue, assign an owner and retest after the deployed fix.

## Trusted tools and reference material

| Reference | What it helps with |
| --- | --- |
| [FTC business guidance](https://www.ftc.gov/business-guidance) | US consumer/privacy guidance |
| [European Commission GDPR](https://commission.europa.eu/law/law-topic/data-protection_en) | EU privacy guidance |
| [FDA digital health](https://www.fda.gov/medical-devices/digital-health-center-excellence) | US health technology |
| [ICO guidance](https://ico.org.uk/for-organisations/) | UK data protection |
| [PCI Security Standards Council](https://www.pcisecuritystandards.org/) | Payment data standards |

## Go/no-go consideration

Do not call this area ready if the core journey can cause loss of data, money, privacy or user access without a documented safe recovery path. Regulations and provider requirements change: review official documentation for your specific product and market.

_Last curated: 2026-11-23._
