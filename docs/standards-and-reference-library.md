# Standards and trusted primary-source references

[← Resource home](../README.md) · [Release risk index](production-risk-index.md)

This reference page helps founders distinguish norms and official policy from a vendor's marketing. It is **not** a substitute for a qualified audit or legal advice.

| Domain | Official reference | Why read it |
| --- | --- | --- |
| Authorization and APIs | [Open source](https://owasp.org/projects/api-security-project) | Risks including broken object-level authorization |
| Web accessibility | [Open source](https://www.w3.org/TR/WCAG22/) | WCAG 2.2 as a testable reference |
| iOS review | [Open source](https://developer.apple.com/app-store/review/guidelines/) | App completeness, review access and metadata |
| Android app quality | [Open source](https://developer.android.com/quality) | Quality guidance and platform behavior |
| AI risk profile | [Open source](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence) | Risk assessment and evaluation |

## How to evaluate a claim

1. Find the official standards body, platform policy or provider terms.
2. Note its version, publication/update date, target product and jurisdictions.
3. Identify specific applicable requirements; do not assume every clause applies to your app.
4. Convert each relevant rule into a test with an observable expected result.
5. Test on actual build/device/account and retain safe evidence.
6. Revisit before major launches, regulatory changes or app-store submissions.

## Common false assurances

- A high accessibility scanner score is not accessibility certification.
- A secure framework is not proof your authorization logic is correct.
- An app-store submission is not approved publication.
- Model-graded AI evaluations without calibrated real tasks cannot prove reliability.

_Last reviewed: 2026-11-23; current policies must be checked again before release._
