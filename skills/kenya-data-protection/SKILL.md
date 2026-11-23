---
name: kenya-data-protection
description: Audit Kenya-specific founder requirements and test cases for kenya data protection, odpc and consent.
---

# Kenya skill: Kenya data protection, ODPC and consent

[← Skills](../README.md) · [Kenya guide](../../kenya/data-protection.md)

## Inputs

Business entity and activity description, current official source documents, authorized staging environment, synthetic user data, representative Kenyan locale/device and a named reviewer.

## Procedure

1. Describe the actual activity and identify any relevant licensing, tax, privacy or provider onboarding questions.
2. Record current provider/regulator primary sources and what remains uncertain.
3. Test: User can see privacy notice before data collection.
4. Test: Withdraw marketing consent without disabling essential service.
5. Test: Unauthorized user cannot access records.
6. Test: Export/deletion requests follow documented process.
7. Test: Processor and cross-border transfers have recorded safeguards.
8. Test: Breach escalation owner and incident log exist.
9. Rank failures by harm, money, privacy and blocked task impact; assign owner.
10. Retest the deployed fix and document the observed result.

## Exit criteria

An evidence-backed test matrix, regulatory decision log (verified/unverified), owner and retest outcome. Do not call the app compliant without qualified review or claim merchant approval without provider confirmation.

## Safety

No real money, private personal data, account credentials or unapproved security tests in public reports. Use provider sandboxes where available.
