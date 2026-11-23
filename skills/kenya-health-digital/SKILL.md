---
name: kenya-health-digital
description: Audit Kenya-specific founder requirements and test cases for kenya digital health and sensitive patient data.
---

# Kenya skill: Kenya digital health and sensitive patient data

[← Skills](../README.md) · [Kenya guide](../../kenya/health-digital.md)

## Inputs

Business entity and activity description, current official source documents, authorized staging environment, synthetic user data, representative Kenyan locale/device and a named reviewer.

## Procedure

1. Describe the actual activity and identify any relevant licensing, tax, privacy or provider onboarding questions.
2. Record current provider/regulator primary sources and what remains uncertain.
3. Test: Patient/caregiver role separation.
4. Test: Wrong patient record access denied.
5. Test: Swahili instructions clinically reviewed.
6. Test: Offline sync does not mix patient records.
7. Test: Emergency escalation instructions accurate and safe.
8. Rank failures by harm, money, privacy and blocked task impact; assign owner.
9. Retest the deployed fix and document the observed result.

## Exit criteria

An evidence-backed test matrix, regulatory decision log (verified/unverified), owner and retest outcome. Do not call the app compliant without qualified review or claim merchant approval without provider confirmation.

## Safety

No real money, private personal data, account credentials or unapproved security tests in public reports. Use provider sandboxes where available.
