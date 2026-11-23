---
name: kenya-consumer-ecommerce
description: Audit Kenya-specific founder requirements and test cases for kenya consumer protection and e-commerce launch.
---

# Kenya skill: Kenya consumer protection and e-commerce launch

[← Skills](../README.md) · [Kenya guide](../../kenya/consumer-ecommerce.md)

## Inputs

Business entity and activity description, current official source documents, authorized staging environment, synthetic user data, representative Kenyan locale/device and a named reviewer.

## Procedure

1. Describe the actual activity and identify any relevant licensing, tax, privacy or provider onboarding questions.
2. Record current provider/regulator primary sources and what remains uncertain.
3. Test: Cart shows true final amount.
4. Test: Refund and failed delivery have clear status.
5. Test: Cancellation request can be submitted.
6. Test: Misleading stock/discount claims corrected.
7. Test: Customer support accessible on mobile.
8. Rank failures by harm, money, privacy and blocked task impact; assign owner.
9. Retest the deployed fix and document the observed result.

## Exit criteria

An evidence-backed test matrix, regulatory decision log (verified/unverified), owner and retest outcome. Do not call the app compliant without qualified review or claim merchant approval without provider confirmation.

## Safety

No real money, private personal data, account credentials or unapproved security tests in public reports. Use provider sandboxes where available.
