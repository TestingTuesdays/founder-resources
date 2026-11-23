# Localization & global readiness

[← Resource home](../README.md) · [Test catalog](test-case-catalog.md) · [Report a bug](../templates/bug-report.md)

## Why this matters

Make content, flows, payments and formats usable in each intended locale.

## Typical founder mistakes

- Hardcoding US date, time, phone and address assumptions
- Translating labels without testing layout or context
- Concatenating sentence fragments that cannot be translated naturally
- Assuming machine translation meets legal or clinical wording needs

## Run these tests

1. **Long translated strings do not truncate essential actions.** Write precondition, expected and actual result, build/version, device, severity, owner and retest status.
2. **Arabic RTL layout with mixed English/numerals.** Write precondition, expected and actual result, build/version, device, severity, owner and retest status.
3. **Plural categories and variable substitution.** Write precondition, expected and actual result, build/version, device, severity, owner and retest status.
4. **Daylight saving boundary and cross-time-zone appointment.** Write precondition, expected and actual result, build/version, device, severity, owner and retest status.
5. **Phone numbers, names, addresses and currency use locale-aware handling.** Write precondition, expected and actual result, build/version, device, severity, owner and retest status.
6. **Translated transactional emails, push notifications and store pages are verified.** Write precondition, expected and actual result, build/version, device, severity, owner and retest status.

## Recommended workflow

Separate translatable content from code, pseudolocalize, perform automated checks for missing strings and run human language/context review on critical tasks. Plan for longer text, RTL, slow networks and local regulations.

## Tools and official references

| Resource | Use it for |
| --- | --- |
| [Crowdin](https://crowdin.com/) | Translation platform |
| [Lokalise](https://lokalise.com/) | Localization workflows |
| [Phrase](https://phrase.com/) | Translation management |
| [Weblate](https://weblate.org/) | Open-source localization |
| [Tolgee](https://tolgee.io/) | In-context localization |
| [i18next](https://www.i18next.com/) | JavaScript i18n |
| [FormatJS](https://formatjs.github.io/) | ICU message formatting |
| [Unicode CLDR](https://cldr.unicode.org/) | Locale formatting data |
| [W3C i18n](https://www.w3.org/International/) | Globalization engineering guidance |

## Do / don't

**Do:** test with representative people and devices, capture non-sensitive evidence, verify failure/recovery, assign ownership and retest the shipped fix.

**Don't:** rely solely on tool scores, copy unverified claims from a vendor, expose customer data, or call an unobserved outcome a passed test.

## Session deliverable

Bring one specific workflow, a safe build/test account, two or more reproducible observations, a severity-ranked fix list, and an agreed follow-up. [Use the session template](../templates/usability-session.md) and [retest sheet](../templates/retest.md).

_Last reviewed: 2026-11-23. Prices, support and platform rules may change._
