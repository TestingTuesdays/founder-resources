# AI-agent tool permission and prompt-injection testing

[← Founder resources](../README.md) · [Test cases](test-case-catalog.md) · [Templates](../templates/README.md)

## Who this is for

Founders shipping agents that browse, retrieve documents or act on user accounts.

## Why it matters

Model text is not an authorization decision, and retrieved content can contain malicious instructions.

## Frequent mistakes

- Trusting tool arguments constructed by a model without server checks.
- Treating website or document instructions as higher priority than user policy.
- Using one test prompt as a safety evaluation.
- Allowing destructive external actions without explicit confirmation.

## Test scenarios

1. **Untrusted retrieved page asks for secrets and agent refuses or ignores it.** Record setup, expected outcome, actual outcome, impact, build/device, owner and comparable retest.
2. **Cross-tenant retrieval fails at tool backend, not only in prompt.** Record setup, expected outcome, actual outcome, impact, build/device, owner and comparable retest.
3. **Tool write requires authenticated user permission and narrow scope.** Record setup, expected outcome, actual outcome, impact, build/device, owner and comparable retest.
4. **High-impact irreversible action requires appropriate confirmation.** Record setup, expected outcome, actual outcome, impact, build/device, owner and comparable retest.
5. **Invalid tool response, timeout and retry do not escalate privileges.** Record setup, expected outcome, actual outcome, impact, build/device, owner and comparable retest.
6. **Eval set includes expected refusals, allowed actions and false positives.** Record setup, expected outcome, actual outcome, impact, build/device, owner and comparable retest.

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
| [OWASP GenAI project](https://genai.owasp.org/) | Primary documentation and implementation patterns |
| [NIST Generative AI Profile](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence) | Primary documentation and implementation patterns |
| [OpenAI Evals](https://github.com/openai/evals) | Primary documentation and implementation patterns |
| [promptfoo](https://www.promptfoo.dev/) | Primary documentation and implementation patterns |

## Expected deliverable

Versioned attack/allowed-case eval matrix and server authorization evidence with action audit trail.

**Do:** keep assumptions and evidence separate, disclose uncertainty and verify current rules before release. **Don't:** imply testing coverage beyond what was executed, or expose real users and assets to experiments without permission.

_Last edited: 2026-11-23. External policies and tool capabilities can change._
