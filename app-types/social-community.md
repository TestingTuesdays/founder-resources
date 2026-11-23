# Social, dating and community apps — founder testing playbook

[← App-type index](README.md) · [Kenya launch guide](../kenya/README.md) · [Test template](../templates/test-case.md)

## Product-quality goal

Identity, reporting, abuse, consent, child safety and user-generated content.

## Minimum test matrix

1. **Block not enforced.** Set up a synthetic scenario, record expected versus actual outcome, severity, owner and retest.
2. **unsolicited contact.** Set up a synthetic scenario, record expected versus actual outcome, severity, owner and retest.
3. **impersonation.** Set up a synthetic scenario, record expected versus actual outcome, severity, owner and retest.
4. **location privacy.** Set up a synthetic scenario, record expected versus actual outcome, severity, owner and retest.
5. **deleted content retained.** Set up a synthetic scenario, record expected versus actual outcome, severity, owner and retest.
6. **underage access.** Set up a synthetic scenario, record expected versus actual outcome, severity, owner and retest.

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

- [ODPC](https://www.odpc.go.ke/)
- [OWASP Cheat Sheets](https://cheatsheetseries.owasp.org/)
- [Google Play policies](https://support.google.com/googleplay/android-developer/)

## Ship decision

Block release for unresolved privacy, money loss, unauthorized access, physical harm or unusable primary workflows. Run comparable tests after fixing issues.

_Last curated: 2026-11-23. Program and regulatory requirements require current verification._
