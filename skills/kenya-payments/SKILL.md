---
name: kenya-payments
description: Audit Kenya-specific founder requirements and test cases for kenya payments: m-pesa, psps and reconciliation.
---

# Kenya skill: Kenya payments: M-Pesa, PSPs and reconciliation

[← Skills](../README.md) · [Kenya guide](../../kenya/payments.md)

## Inputs

Business entity and activity description, current official source documents, authorized staging environment, synthetic user data, representative Kenyan locale/device and a named reviewer.

## Procedure

1. Describe the actual activity and identify any relevant licensing, tax, privacy or provider onboarding questions.
2. Record current provider/regulator primary sources and what remains uncertain.
3. Test: STK push initiated but user cancels or prompt expires.
4. Test: Callback duplicated, delayed, missing or out of order.
5. Test: Transaction reference mismatch, partial reversal or refund.
6. Test: Duplicate click after network loss; idempotency key enforcement.
7. Test: Wrong MSISDN formatting or shared device.
8. Test: Payout/settlement amount differs from order ledger.
9. Rank failures by harm, money, privacy and blocked task impact; assign owner.
10. Retest the deployed fix and document the observed result.

## Exit criteria

An evidence-backed test matrix, regulatory decision log (verified/unverified), owner and retest outcome. Do not call the app compliant without qualified review or claim merchant approval without provider confirmation.

## Safety

No real money, private personal data, account credentials or unapproved security tests in public reports. Use provider sandboxes where available.
