# Web3 wallet, transaction and smart-contract UX

[← Founder resources](../README.md) · [Test cases](test-case-catalog.md) · [Templates](../templates/README.md)

## Who this is for

Founders building wallet-connected web apps, on-chain membership and transaction flows.

## Why it matters

Irreversible actions, network changes, approval screens and gas fees require greater user clarity and specialized security review.

## Frequent mistakes

- Signing or approving transactions without explaining chain/token and costs.
- Treating a connected wallet as a server authentication session.
- Unclear pending, rejected and reverted transaction status.
- Using mainnet accounts/assets for open usability tests.

## Test scenarios

1. **Connect/disconnect and switch supported networks.** Record setup, expected outcome, actual outcome, impact, build/device, owner and comparable retest.
2. **Reject wallet request and recover without stuck spinner.** Record setup, expected outcome, actual outcome, impact, build/device, owner and comparable retest.
3. **Show chain, estimated fees and irreversible action before confirmation.** Record setup, expected outcome, actual outcome, impact, build/device, owner and comparable retest.
4. **Simulate failed/reverted transaction on authorized testnet.** Record setup, expected outcome, actual outcome, impact, build/device, owner and comparable retest.
5. **Verify signature/session nonce freshness and origin binding.** Record setup, expected outcome, actual outcome, impact, build/device, owner and comparable retest.
6. **Review contracts for access controls and emergency stop behavior.** Record setup, expected outcome, actual outcome, impact, build/device, owner and comparable retest.

## Founder workflow

1. Choose the top one to three real user journeys relevant to your product.
2. Prepare synthetic data and an authorized test environment. Do not share production credentials or personal records.
3. Write observable pass/fail criteria *before* executing the happy path and the failure/recovery scenarios.
4. Run the checks with appropriate devices, identities and permissions. Do not assume an automated tool proves the complete journey.
5. File reproducible defects, assign severity based on harm, fix in a versioned build and retest.
6. Decide go/no-go; block on critical privacy, money, safety, irreversible-data or core-task risks.

## Primary references and tools

| Resource | Value |
| --- | --- |
| [Ethereum developer docs](https://ethereum.org/en/developers/docs/) | Primary documentation and implementation patterns |
| [OpenZeppelin Contracts](https://docs.openzeppelin.com/contracts) | Primary documentation and implementation patterns |
| [OWASP Smart Contract Top 10](https://scs.owasp.org/) | Primary documentation and implementation patterns |
| [EIP-4361 Sign-In with Ethereum](https://eips.ethereum.org/EIPS/eip-4361) | Primary documentation and implementation patterns |

## Expected deliverable

Testnet transaction/recovery matrix, wallet UX issues and specialized security review handoff.

**Do:** keep assumptions and evidence separate, disclose uncertainty and verify current rules before release. **Don't:** imply testing coverage beyond what was executed, or expose real users and assets to experiments without permission.

_Last edited: 2026-11-23. External policies and tool capabilities can change._
