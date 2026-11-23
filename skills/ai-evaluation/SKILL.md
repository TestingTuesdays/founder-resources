---
name: ai-evaluation
description: Detect safety, truthfulness, grounding, permission and quality regressions.
---

# AI and agent regression evaluation

[← Skills](../README.md) · [Topic guide](../../docs/ai-evaluation.md)

## Objective

Detect safety, truthfulness, grounding, permission and quality regressions.

## Required inputs

Versioned model/prompt/tool schema, gold examples, acceptance criteria.

## Procedure

1. Define tasks, harms, boundary conditions and metrics.
2. Prepare normal, adversarial, unknown-answer and multilingual examples.
3. Check prompt injection, unauthorized tool use and data leakage.
4. Evaluate grounding, structured outputs, cost and latency.
5. Review sample failures with humans and compare baseline.
6. Version results and block regressions on critical behaviors.

## Done when

Evaluation report with dataset version, failure classes and decision.

## Safety and evidence

Use permissioned systems and synthetic data. Obtain research consent where applicable, redact personal information, preserve actual vs expected outcomes, and never state a check passed without running it. Human review remains necessary for high-risk conclusions.

## Copyable records

[Bug report](../../templates/bug-report.md) · [Testing session](../../templates/usability-session.md) · [Retest](../../templates/retest.md).
