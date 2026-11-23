# E-commerce and retail apps — founder testing playbook

[← App-type index](README.md) · [Kenya launch guide](../kenya/README.md) · [Test template](../templates/test-case.md)

## Product-quality goal

Catalog accuracy, checkout, delivery, refunds and consumer trust.

## Minimum test matrix

1. **Out-of-stock checkout.** Set up a synthetic scenario, record expected versus actual outcome, severity, owner and retest.
2. **duplicate order.** Set up a synthetic scenario, record expected versus actual outcome, severity, owner and retest.
3. **wrong shipping fee.** Set up a synthetic scenario, record expected versus actual outcome, severity, owner and retest.
4. **cash-on-delivery.** Set up a synthetic scenario, record expected versus actual outcome, severity, owner and retest.
5. **M-Pesa pending.** Set up a synthetic scenario, record expected versus actual outcome, severity, owner and retest.
6. **return and cancellation.** Set up a synthetic scenario, record expected versus actual outcome, severity, owner and retest.
7. **vendor fraud.** Set up a synthetic scenario, record expected versus actual outcome, severity, owner and retest.

## What founders often miss

- Backend authorization and payment settlement are not guaranteed by a successful UI.
- Real devices, low bandwidth, long names, Swahili and English content, accessible controls and realistic errors matter.
- User research needs consent, safe data and a genuine target audience.
- Sector-specific rules depend on what the product actually does, not only its marketing category.

## Kenya-specific decision points

1. Decide whether you are only a software supplier or also performing a regulated activity such as payment services, healthcare, lending, transport, education or utilities.
2. Check whether your data collection, processor contracts and cross-border transfers trigger obligations under Kenyan data-protection law.
3. Verify which payment providers onboard your **legal entity** and which local payment methods are available.
4. Test Kenyan phone numbers, KES display, address formats, time zone (Africa/Nairobi), intermittent connectivity and accessible user journeys.
5. Record unresolved questions for qualified local counsel or sector regulator; do not claim automatic approval.

## Official starting points (not legal conclusions)

- [Kenya Competition Authority](https://www.cak.go.ke/)
- [Paystack](https://paystack.com/docs/)
- [Safaricom Daraja](https://developer.safaricom.co.ke/)

## Ship decision

Block release for unresolved privacy, money loss, unauthorized access, physical harm or unusable primary workflows. Run comparable tests after fixing issues.

_Last curated: 2026-11-23. Program and regulatory requirements require current verification._
