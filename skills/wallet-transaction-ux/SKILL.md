---
name: wallet-transaction-ux
description: Test wallet and on-chain transaction journeys for founders and reviewers working with authorized product environments.
---

# Test wallet and on-chain transaction journeys

[← All skills](../README.md) · [Topic guide](../../docs/web3-wallet-quality.md) · [Report template](../../templates/test-case.md)

## Goal

Produce evidence that a founder can use to decide whether a specific change is ready to ship.

## Inputs

Versioned product build, target user task, relevant official documentation, fictional test accounts, authorization to test, pass/fail criterion and accountable reviewer.

## Procedure

1. Use permissioned sandbox/testnet with negligible synthetic assets.
2. Test wallet connect, wrong chain, rejection and disconnect.
3. Explain transaction type, asset, chain and irreversible implications before signature.
4. Simulate reverted transaction and show helpful status/retry.
5. Check signed-message nonce, domain, expiry and server verification.
6. Have specialized reviewer inspect contract/approval risks before real value.

## Done when

Testnet transaction record, user-understandable status and security handoff.

## Record

| Field | Required evidence |
| --- | --- |
| Task and risk | Why a failure would matter |
| Environment | Build, device, locale, test identity, feature flag |
| Steps | Exact reproducible actions |
| Expected / actual | Observable behavior, not guesswork |
| Severity and owner | Realistic impact and next action |
| Fix and retest | Deployed version, same task, changed outcome |

## Safety and limitations

Use synthetic identities/data in permissioned environments. Never scan or stress unowned systems, expose secrets or publish customer/participant recordings. A proposed test is not a passed test; always differentiate performed work from guidance. Escalate security, safety or regulated-product blockers for independent review.
