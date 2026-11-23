---
name: kenya-tax-invoicing
description: Audit Kenya-specific founder requirements and test cases for kenya tax, kra and etims readiness.
---

# Kenya skill: Kenya tax, KRA and eTIMS readiness

[← Skills](../README.md) · [Kenya guide](../../kenya/tax-invoicing.md)

## Inputs

Business entity and activity description, current official source documents, authorized staging environment, synthetic user data, representative Kenyan locale/device and a named reviewer.

## Procedure

1. Describe the actual activity and identify any relevant licensing, tax, privacy or provider onboarding questions.
2. Record current provider/regulator primary sources and what remains uncertain.
3. Test: Invoice generated for completed sale.
4. Test: Cancelled/refunded sale reconciles without duplicate revenue.
5. Test: KES rounding and tax calculation consistent.
6. Test: Invoice fields and records retained as required.
7. Test: Offline issuance or provider outage has safe recovery.
8. Rank failures by harm, money, privacy and blocked task impact; assign owner.
9. Retest the deployed fix and document the observed result.

## Exit criteria

An evidence-backed test matrix, regulatory decision log (verified/unverified), owner and retest outcome. Do not call the app compliant without qualified review or claim merchant approval without provider confirmation.

## Safety

No real money, private personal data, account credentials or unapproved security tests in public reports. Use provider sandboxes where available.
