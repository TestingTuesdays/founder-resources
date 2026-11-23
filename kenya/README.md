# Building and testing apps for Kenya

[← Founder resources](../README.md) · [App-type playbooks](../app-types/README.md) · [Kenya perks](../perks/kenya-nairobi.md)

A founder-friendly, **Kenya-specific** guide to payments, privacy, compliance discovery, localization, mobile UX and operational quality. **Do not mistake this for a legal opinion or a list of guaranteed provider approvals.**

## Detailed implementation recipes

[Seven provider and implementation QA recipes](integrations/README.md) cover STK Push, collections and payouts, provider evaluation, ODPC data maps, eTIMS, field research and county permits. Each has a matching reusable skill.

## Start by risk

- [Kenya payments: M-Pesa, PSPs and reconciliation](payments.md) · [Reusable skill](../skills/kenya-payments/SKILL.md)
- [Kenya data protection, ODPC and consent](data-protection.md) · [Reusable skill](../skills/kenya-data-protection/SKILL.md)
- [Kenya fintech, lending and payment regulation discovery](fintech-compliance.md) · [Reusable skill](../skills/kenya-fintech-compliance/SKILL.md)
- [Kenya consumer protection and e-commerce launch](consumer-ecommerce.md) · [Reusable skill](../skills/kenya-consumer-ecommerce/SKILL.md)
- [Kenya tax, KRA and eTIMS readiness](tax-invoicing.md) · [Reusable skill](../skills/kenya-tax-invoicing/SKILL.md)
- [Kenyan localization, accessibility and low-bandwidth UX](localization-access.md) · [Reusable skill](../skills/kenya-localization-access/SKILL.md)
- [Kenya SMS, USSD and communications product QA](sms-ussd.md) · [Reusable skill](../skills/kenya-sms-ussd/SKILL.md)
- [Kenya digital health and sensitive patient data](health-digital.md) · [Reusable skill](../skills/kenya-health-digital/SKILL.md)
- [Kenya sector regulator discovery checklist](sector-licensing.md) · [Reusable skill](../skills/kenya-sector-licensing/SKILL.md)

## Kenya-first release matrix

| Concern | What to check |
| --- | --- |
| Payments | M-Pesa STK, callback, reversal, settlement, duplicate requests and provider onboarding |
| Privacy | ODPC guidance, lawful processing, retention, sensitive data and vendors |
| Tax | KRA eTIMS and other obligations as applicable to your entity and activity |
| Localization | KES, +254 and international numbers, Africa/Nairobi, Kiswahili and English |
| Connectivity | Older Android phones, mobile data, offline recovery and shared-device privacy |
| Sector | Whether the activity triggers CBK, CA, EPRA, NTSA, health, education or county oversight |
| User trust | Accurate pricing, clear cancellation, fraud reporting and accessible support |

## Important distinctions

- A **payment API integration** is not the same as being a licensed payment service provider.
- A **sandbox** is not production merchant approval.
- An **app-store listing** is not medical, financial or regulatory authorization.
- A **Kenyan user base** does not automatically mean a provider supports Kenya-incorporated merchants.
- **Compliance requirements** depend on the legal entity, exact activity, users, location and evolving law.

## Official discovery sources

[CBK](https://www.centralbank.go.ke/) · [ODPC](https://www.odpc.go.ke/) · [KRA](https://www.kra.go.ke/) · [Kenya Law](https://new.kenyalaw.org/) · [Communications Authority](https://www.ca.go.ke/) · [Safaricom Daraja](https://developer.safaricom.co.ke/).

**Editorial note:** regulator and provider links are starting points. Specific statutory thresholds, rates, licensing exemptions and deadlines require current primary-document verification and qualified local advice. This library does not certify compliance.

## Provider selection data

Use the [Kenya provider evaluation questions](../data/kenya-provider-questions.csv) to compare merchant onboarding, supported payment rails, settlement, fees, privacy and regulatory questions. Populate answers from current written provider sources, not guesses.

## Incorporation and cross-border fundraising

- [Kenyan company filing and ongoing obligations](company-filing.md)
- [US-incorporated company operating in Kenya](../growth/fundraising-us-kenya-structure.md)
- [Kenya investor directory](../investors/README.md)
