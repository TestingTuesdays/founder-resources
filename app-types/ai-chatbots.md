# AI chatbots, assistants and agent products — testing and release playbook

[← All app types](README.md) · [Kenya hub](../kenya/README.md) · [Quality templates](../templates/README.md)

## Product quality goal

Grounding, safety, tool permissions, data isolation, feedback and cost.

## High-risk scenarios

1. Prompt injection. Use a synthetic case, expected result, observed result and comparable retest.
2. tool misuse. Use a synthetic case, expected result, observed result and comparable retest.
3. unavailable answer. Use a synthetic case, expected result, observed result and comparable retest.
4. citations. Use a synthetic case, expected result, observed result and comparable retest.
5. personal data in traces. Use a synthetic case, expected result, observed result and comparable retest.
6. model regression. Use a synthetic case, expected result, observed result and comparable retest.

## Founder testing plan

1. Identify a real target user and a critical task, then define pass/fail before testing.
2. Include an unauthorized access attempt, provider outage, duplicate/retry and accessibility test where relevant.
3. Check Kenyan payment methods, data protection, connectivity, locale and sector permissions if serving Kenya.
4. Document the difference between software QA and any required licensing or expert review.
5. Assign severity, fix owner and versioned retest; do not label unexecuted tests passed.

## Primary references

- [OWASP GenAI](https://genai.owasp.org/)
- [OpenAI Evals](https://github.com/openai/evals)

**Scope:** educational QA guidance; market, legal and provider rules must be checked for the specific business.
