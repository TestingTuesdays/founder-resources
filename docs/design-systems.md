# Product design systems & UI consistency

[← Resource home](../README.md) · [Release checklist](release-readiness.md)

## Why founders should care

Inconsistent controls, states and typography make seemingly simple tasks confusing.

## Common mistakes

- Assuming a successful demo or dashboard proves the experience works for all users.
- Ignoring errors, permission boundaries, mobile constraints and exceptional states.
- Launching without a responsible owner, observable outcome or fallback.
- Using vendor tooling without checking costs, data protection or real capabilities.

## Core test scenarios

1. **Buttons, forms and dialogs use consistent semantics.** Record build/environment, expected vs actual, user impact and follow-up.
2. **Empty/loading/error/success states exist for each major component.** Record build/environment, expected vs actual, user impact and follow-up.
3. **Keyboard focus and screen-reader announcements work.** Record build/environment, expected vs actual, user impact and follow-up.
4. **Dark mode, zoom and narrow screens remain readable.** Record build/environment, expected vs actual, user impact and follow-up.
5. **Components behave consistently when reused.** Record build/environment, expected vs actual, user impact and follow-up.

## Practical workflow

1. Identify the most important user task and a measurable success criterion.
2. Use safe synthetic data and a representative device/locale/account.
3. Test the expected route **and** failure/recovery case; observe results, not assumptions.
4. Check privacy/security, accessibility and reliability considerations where relevant.
5. File a reproducible issue, assign an owner and retest after the deployed fix.

## Trusted tools and reference material

| Reference | What it helps with |
| --- | --- |
| [Figma](https://www.figma.com/) | Design library and prototyping |
| [Storybook](https://storybook.js.org/) | Component states and documentation |
| [Chromatic](https://www.chromatic.com/) | Visual regression |
| [Material Design](https://m3.material.io/) | UI patterns |
| [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/) | Platform patterns |
| [WAI APG](https://www.w3.org/WAI/ARIA/apg/) | Accessible widgets |

## Go/no-go consideration

Do not call this area ready if the core journey can cause loss of data, money, privacy or user access without a documented safe recovery path. Regulations and provider requirements change: review official documentation for your specific product and market.

_Last curated: 2026-11-23._
