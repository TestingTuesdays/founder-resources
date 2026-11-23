---
name: kenya-sector-licensing
description: Audit Kenya-specific founder requirements and test cases for kenya sector regulator discovery checklist.
---

# Kenya skill: Kenya sector regulator discovery checklist

[← Skills](../README.md) · [Kenya guide](../../kenya/sector-licensing.md)

## Inputs

Business entity and activity description, current official source documents, authorized staging environment, synthetic user data, representative Kenyan locale/device and a named reviewer.

## Procedure

1. Describe the actual activity and identify any relevant licensing, tax, privacy or provider onboarding questions.
2. Record current provider/regulator primary sources and what remains uncertain.
3. Test: Service description matches actual regulated function.
4. Test: Required permits/approvals are not claimed without evidence.
5. Test: Safety escalation owner assigned.
6. Test: Provider terms match actual entity and market.
7. Rank failures by harm, money, privacy and blocked task impact; assign owner.
8. Retest the deployed fix and document the observed result.

## Exit criteria

An evidence-backed test matrix, regulatory decision log (verified/unverified), owner and retest outcome. Do not call the app compliant without qualified review or claim merchant approval without provider confirmation.

## Safety

No real money, private personal data, account credentials or unapproved security tests in public reports. Use provider sandboxes where available.
