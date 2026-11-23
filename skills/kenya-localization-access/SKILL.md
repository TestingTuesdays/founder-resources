---
name: kenya-localization-access
description: Audit Kenya-specific founder requirements and test cases for kenyan localization, accessibility and low-bandwidth ux.
---

# Kenya skill: Kenyan localization, accessibility and low-bandwidth UX

[← Skills](../README.md) · [Kenya guide](../../kenya/localization-access.md)

## Inputs

Business entity and activity description, current official source documents, authorized staging environment, synthetic user data, representative Kenyan locale/device and a named reviewer.

## Procedure

1. Describe the actual activity and identify any relevant licensing, tax, privacy or provider onboarding questions.
2. Record current provider/regulator primary sources and what remains uncertain.
3. Test: Long Kiswahili strings and natural wording.
4. Test: +254 and other international phone formats.
5. Test: No-network retry and preserved form state.
6. Test: Accessible error message and keyboard focus.
7. Test: Payment prompt interruption or shared-device privacy.
8. Rank failures by harm, money, privacy and blocked task impact; assign owner.
9. Retest the deployed fix and document the observed result.

## Exit criteria

An evidence-backed test matrix, regulatory decision log (verified/unverified), owner and retest outcome. Do not call the app compliant without qualified review or claim merchant approval without provider confirmation.

## Safety

No real money, private personal data, account credentials or unapproved security tests in public reports. Use provider sandboxes where available.
