---
name: ai-rag-evaluation
description: Run a repeatable founder quality review for retrieval-augmented generation grounding and citation qa.
---

# Retrieval-augmented generation grounding and citation QA — reusable skill

[← Skills](../README.md) · [Guide](../../docs/ai-rag-evaluation.md)

## Goal

Produce evidence-backed release findings without inventing test results.

## Inputs

Product/build identifier, owner, target audience, safe test accounts, representative devices and applicable primary documentation.

## Procedure

1. Prepare gold questions with verified sources and impossible-answer cases.
2. Test document permissions before retrieval and citation display.
3. Check citations point to the claim actually supported.
4. Measure retrieval misses, stale index, context truncation and answer abstention.
5. Compare baseline after changing embeddings, prompts or model.
6. Rank findings by impact and assign fix owners.
7. Repeat failed scenarios on the deployed fix and record changed outcome.

## Output

Versioned scenario matrix, expected/actual observations, redacted evidence, severity, fix owner and retest status.

## Safety

Use only authorized environments and synthetic data. Never publish private participant information, production credentials or billing records. Manual and specialist review remains necessary for high-impact claims.
