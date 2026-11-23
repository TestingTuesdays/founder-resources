---
name: kenya-fintech-compliance
description: Audit Kenya-specific founder requirements and test cases for kenya fintech, lending and payment regulation discovery.
---

# Kenya skill: Kenya fintech, lending and payment regulation discovery

[← Skills](../README.md) · [Kenya guide](../../kenya/fintech-compliance.md)

## Inputs

Business entity and activity description, current official source documents, authorized staging environment, synthetic user data, representative Kenyan locale/device and a named reviewer.

## Procedure

1. Describe the actual activity and identify any relevant licensing, tax, privacy or provider onboarding questions.
2. Record current provider/regulator primary sources and what remains uncertain.
3. Test: Product claims do not imply CBK authorization unless confirmed.
4. Test: Credit pricing and repayment disclosures match contract.
5. Test: Sensitive identity documents restricted by role.
6. Test: Refund, reversal and disputed transaction traceable.
7. Test: Customer complaints and fraud escalation documented.
8. Rank failures by harm, money, privacy and blocked task impact; assign owner.
9. Retest the deployed fix and document the observed result.

## Exit criteria

An evidence-backed test matrix, regulatory decision log (verified/unverified), owner and retest outcome. Do not call the app compliant without qualified review or claim merchant approval without provider confirmation.

## Safety

No real money, private personal data, account credentials or unapproved security tests in public reports. Use provider sandboxes where available.
