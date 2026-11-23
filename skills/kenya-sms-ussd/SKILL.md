---
name: kenya-sms-ussd
description: Audit Kenya-specific founder requirements and test cases for kenya sms, ussd and communications product qa.
---

# Kenya skill: Kenya SMS, USSD and communications product QA

[← Skills](../README.md) · [Kenya guide](../../kenya/sms-ussd.md)

## Inputs

Business entity and activity description, current official source documents, authorized staging environment, synthetic user data, representative Kenyan locale/device and a named reviewer.

## Procedure

1. Describe the actual activity and identify any relevant licensing, tax, privacy or provider onboarding questions.
2. Record current provider/regulator primary sources and what remains uncertain.
3. Test: USSD session timeout and resume.
4. Test: SMS delivered late, duplicated or failed.
5. Test: Opt-out respected.
6. Test: Wrong number or recycled number privacy.
7. Test: Short code unprovisioned on a carrier.
8. Test: Delivery receipt does not imply user read message.
9. Rank failures by harm, money, privacy and blocked task impact; assign owner.
10. Retest the deployed fix and document the observed result.

## Exit criteria

An evidence-backed test matrix, regulatory decision log (verified/unverified), owner and retest outcome. Do not call the app compliant without qualified review or claim merchant approval without provider confirmation.

## Safety

No real money, private personal data, account credentials or unapproved security tests in public reports. Use provider sandboxes where available.
