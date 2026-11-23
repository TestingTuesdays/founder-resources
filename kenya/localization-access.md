# Kenyan localization, accessibility and low-bandwidth UX

[← Kenya hub](README.md) · [App-type playbooks](../app-types/README.md) · [Testing template](../templates/test-case.md)

Kenyan users are not one language, device, literacy level or connectivity profile.

## Founder considerations

- Start with user research: English and Kiswahili may be priorities but other languages or accessible formats can matter.
- Use Africa/Nairobi time zone and appropriate KES formatting without assuming all customers use Kenyan phone numbers.
- Support +254 numbers, valid international numbers and diverse personal names.
- Check older Android devices, mobile data costs, screen readers, high zoom and intermittent connectivity.

## Minimum tests

1. **Long Kiswahili strings and natural wording.** Record expected/actual result, build, affected user, severity, owner and retest.
2. **+254 and other international phone formats.** Record expected/actual result, build, affected user, severity, owner and retest.
3. **No-network retry and preserved form state.** Record expected/actual result, build, affected user, severity, owner and retest.
4. **Accessible error message and keyboard focus.** Record expected/actual result, build, affected user, severity, owner and retest.
5. **Payment prompt interruption or shared-device privacy.** Record expected/actual result, build, affected user, severity, owner and retest.

## Implementation and compliance workflow

1. Document the legal entity, target users, product activities, payment/data flows and provider contracts.
2. Consult current primary regulator and provider documentation; do not infer eligibility from a sandbox API key.
3. Identify the relevant permission, registration, licensing, contract or tax question; record it as **unverified** until confirmed.
4. Run tests on synthetic accounts, sandbox payments and representative Kenyan devices/networks.
5. Get appropriate qualified local legal/accounting/sector review for obligations and approvals.
6. Fix high-risk issues, version the release and retest the affected user journey.

## Primary starting points

- [W3C Internationalization](https://www.w3.org/International/)
- [W3C WAI](https://www.w3.org/WAI/)
- [Unicode CLDR](https://cldr.unicode.org/)

## Evidence required

A product activity map, provider eligibility checklist, test results and a list of unresolved regulatory questions. This guide is not legal advice, proof of licensing, or a substitute for reading current Kenyan law.

_Last curated: 2026-11-23; rules and provider policies can change._
