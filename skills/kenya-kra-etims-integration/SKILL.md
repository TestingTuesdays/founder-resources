---
name: kenya-kra-etims-integration
description: Perform an evidence-based Kenya-focused review of kra etims invoice and refund workflow qa.
---

# KRA eTIMS invoice and refund workflow QA — reusable skill

[← Skills](../README.md) · [Detailed guide](../../kenya/integrations/kra-etims-integration.md)

## Inputs

Real business activity description, current official provider/regulator documents, synthetic accounts, approved sandbox and named reviewer.

## Procedure

1. Confirm eTIMS and tax obligations for the legal entity with current KRA guidance.
2. Map order/payment/refund to invoice and credit note states.
3. Verify invoice identifiers and tax calculations in approved test environment.
4. Test partial refund, cancellation and delayed payment settlement.
5. Reconcile ledger, tax record and invoice without duplicate issuance.
6. Handle service outage or retry without duplicated tax documents.
7. Ask a Kenyan tax professional to validate the actual setup.

## Done when

A completed scenario matrix documents actual behavior, risk, owner, fix and comparable retest. Record any licensing, merchant onboarding or tax decision as **unverified** until confirmed with the competent source.

## Safety

Never use real customer records, production secrets or real money in open testing. Do not confuse a documented plan with an executed integration.
