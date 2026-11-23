# Retrieval-augmented generation grounding and citation QA

[← Resources](../README.md) · [Founder test cases](test-case-catalog.md) · [Release readiness](release-readiness.md)

## Why this matters

A confident AI answer can be false, unsupported, stale or based on unauthorized documents.

## Common founder mistakes

- Testing only a single ideal account or device.
- Confusing a successful demo with an independently observed user outcome.
- Failing to test errors, permissions, migration or recovery.
- Publishing claims or private records without a verifiable source and permission.

## Practical test scenarios

1. Prepare gold questions with verified sources and impossible-answer cases. Record the starting state, expected result, actual result, build and owner.
2. Test document permissions before retrieval and citation display. Record the starting state, expected result, actual result, build and owner.
3. Check citations point to the claim actually supported. Record the starting state, expected result, actual result, build and owner.
4. Measure retrieval misses, stale index, context truncation and answer abstention. Record the starting state, expected result, actual result, build and owner.
5. Compare baseline after changing embeddings, prompts or model. Record the starting state, expected result, actual result, build and owner.

## Repeatable workflow

1. Identify the intended user, critical task and failure risk.
2. Prepare fictional test data and an authorized environment.
3. Define success criteria and run both happy and failure paths.
4. Capture privacy-safe evidence and assign defects by user impact.
5. Fix the issue, publish a versioned build and retest under comparable conditions.

## Primary references

- [Ragas](https://docs.ragas.io/)
- [OpenAI Evals](https://github.com/openai/evals)
- [OWASP GenAI](https://genai.owasp.org/)

## Done when

There is a completed test matrix with actual observations, known limitations, owner, fix link and retest outcome. Do not claim compliance or production safety based only on a tool's score.

_Last curated: 2026-11-23._
