---
name: agent-tool-safety
description: Evaluate agent tool authorization and prompt injection for founders and reviewers working with authorized product environments.
---

# Evaluate agent tool authorization and prompt injection

[← All skills](../README.md) · [Topic guide](../../docs/ai-agent-permissions.md) · [Report template](../../templates/test-case.md)

## Goal

Produce evidence that a founder can use to decide whether a specific change is ready to ship.

## Inputs

Versioned product build, target user task, relevant official documentation, fictional test accounts, authorization to test, pass/fail criterion and accountable reviewer.

## Procedure

1. Map every tool to authenticated identity, resource scope and confirmation requirements.
2. Build benign and malicious inputs, including hostile retrieved documents.
3. Attempt cross-tenant retrieval and unauthorized write in sandbox.
4. Simulate unavailable tools, malformed outputs and repeated retries.
5. Score correct authorized actions, blocked actions and false positives.
6. Version prompt/model/tool schemas and rerun before deployment.

## Done when

Reproducible agent evaluation matrix including backend permission proofs.

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
