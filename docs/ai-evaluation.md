# AI applications, agents & evaluation

[← Resource home](../README.md) · [Test catalog](test-case-catalog.md) · [Report a bug](../templates/bug-report.md)

## Why this matters

Test probabilistic outputs and agent tool permissions alongside normal product reliability.

## Typical founder mistakes

- Treating a few attractive demos as evaluation
- Letting an AI judge itself without calibrated human examples
- Allowing model text to bypass tool authorization
- Failing to version prompts, data, models and tool schemas

## Run these tests

1. **Known-answer and impossible-answer prompts.** Write precondition, expected and actual result, build/version, device, severity, owner and retest status.
2. **Outdated, ambiguous and multilingual inputs.** Write precondition, expected and actual result, build/version, device, severity, owner and retest status.
3. **Prompt injection inside retrieved webpages/documents.** Write precondition, expected and actual result, build/version, device, severity, owner and retest status.
4. **Agent tries a tool beyond user's permission.** Write precondition, expected and actual result, build/version, device, severity, owner and retest status.
5. **Citation grounding and source attribution.** Write precondition, expected and actual result, build/version, device, severity, owner and retest status.
6. **Malformed JSON and unavailable external tool.** Write precondition, expected and actual result, build/version, device, severity, owner and retest status.
7. **Latency, retries, cost limit and regression after model change.** Write precondition, expected and actual result, build/version, device, severity, owner and retest status.

## Recommended workflow

Create a representative, versioned evaluation set with expected/acceptable behaviors. Include adverse and multilingual cases. Run regression checks before model/prompt changes, and require explicit authorization and human review for consequential external actions.

## Tools and official references

| Resource | Use it for |
| --- | --- |
| [OpenAI Evals](https://github.com/openai/evals) | Evaluation toolkit |
| [OpenAI eval guide](https://platform.openai.com/docs/guides/evals) | Evaluation methods |
| [Langfuse](https://langfuse.com/) | Tracing and evaluation |
| [Arize Phoenix](https://phoenix.arize.com/) | LLM observability |
| [Ragas](https://docs.ragas.io/) | RAG evaluation |
| [promptfoo](https://www.promptfoo.dev/) | Prompt evaluations/red teaming |
| [OWASP GenAI](https://genai.owasp.org/) | Generative-AI threat guidance |
| [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework) | AI risk management |

## Do / don't

**Do:** test with representative people and devices, capture non-sensitive evidence, verify failure/recovery, assign ownership and retest the shipped fix.

**Don't:** rely solely on tool scores, copy unverified claims from a vendor, expose customer data, or call an unobserved outcome a passed test.

## Session deliverable

Bring one specific workflow, a safe build/test account, two or more reproducible observations, a severity-ranked fix list, and an agreed follow-up. [Use the session template](../templates/usability-session.md) and [retest sheet](../templates/retest.md).

_Last reviewed: 2026-11-23. Prices, support and platform rules may change._
