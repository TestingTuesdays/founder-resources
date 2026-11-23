# Accessibility & inclusive design

[← Resource home](../README.md) · [Test catalog](test-case-catalog.md) · [Report a bug](../templates/bug-report.md)

## Why this matters

Make critical tasks operable for people using keyboards, assistive technology and different visual, motor and cognitive capabilities.

## Typical founder mistakes

- Equating an automated scan score with accessibility compliance
- Invisible focus or inaccessible custom controls
- Using color alone to indicate errors
- Shipping critical videos without appropriate captions or transcripts

## Run these tests

1. **Complete primary flow using only Tab, Shift+Tab, Enter, Space and arrows.** Write precondition, expected and actual result, build/version, device, severity, owner and retest status.
2. **Read form labels, errors and dialogs with screen reader.** Write precondition, expected and actual result, build/version, device, severity, owner and retest status.
3. **Zoom text to 200% and verify essential content is not clipped.** Write precondition, expected and actual result, build/version, device, severity, owner and retest status.
4. **Respect reduced-motion and text-size preferences.** Write precondition, expected and actual result, build/version, device, severity, owner and retest status.
5. **Check accessible name, target size and focus return after modal closes.** Write precondition, expected and actual result, build/version, device, severity, owner and retest status.
6. **Test with disabled users.** Write precondition, expected and actual result, build/version, device, severity, owner and retest status.

## Recommended workflow

Use applicable WCAG 2.2 Level AA as a practical baseline, test keyboard and screen readers manually, and validate critical tasks with disabled participants. Automated scanning supports but does not replace specialist review.

## Tools and official references

| Resource | Use it for |
| --- | --- |
| [WCAG 2.2](https://www.w3.org/TR/WCAG22/) | Authoritative web criteria |
| [WAI tutorials](https://www.w3.org/WAI/tutorials/) | Implementation patterns |
| [axe-core](https://github.com/dequelabs/axe-core) | Automated rule checks |
| [WAVE](https://wave.webaim.org/) | Accessible-page inspection |
| [Accessibility Insights](https://accessibilityinsights.io/) | Guided checks |
| [NVDA](https://www.nvaccess.org/) | Windows screen reader |
| [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/) | Contrast checking |

## Do / don't

**Do:** test with representative people and devices, capture non-sensitive evidence, verify failure/recovery, assign ownership and retest the shipped fix.

**Don't:** rely solely on tool scores, copy unverified claims from a vendor, expose customer data, or call an unobserved outcome a passed test.

## Session deliverable

Bring one specific workflow, a safe build/test account, two or more reproducible observations, a severity-ranked fix list, and an agreed follow-up. [Use the session template](../templates/usability-session.md) and [retest sheet](../templates/retest.md).

_Last reviewed: 2026-11-23. Prices, support and platform rules may change._
