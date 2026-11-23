# Integrating feedback into your product and delivery system

[← Research hub](README.md) · [Feedback schema](../templates/feedback-intake-schema.md) · [Triage](../templates/feedback-triage.md)

## Reference architecture

```text
App feedback widget / survey / support email / moderated session
  -> consent + input validation + abuse/rate limit
  -> private intake endpoint or approved automation
  -> feedback database (raw, access-controlled, retention-limited)
  -> redacted issue/triage queue (GitHub, Notion, Linear, etc.)
  -> owner + severity + fix/version
  -> comparable retest + participant follow-up (if consented)
  -> release notes + product learning
```

## Minimal data contract

Use a random feedback ID, source, product version, optional pseudonymous user reference, task, category, rating if appropriate, description, consent flags, created timestamp, status and triage owner. Do not send full IP addresses, tokens, medical records, payment references or contact details into public issue bodies.

## In-product integration steps

1. Add a discoverable **Send feedback** entry in navigation and contextual failure states. Make submission accessible by keyboard and screen reader.
2. Offer categories: bug, usability friction, feature request, billing, accessibility and safety. Provide a safe private route for security reports.
3. Validate length and attachment type, rate limit spam, protect against HTML/script injection and acknowledge submission with a tracking reference.
4. Store raw text and consent flags in a restricted database. Scrub secrets and PII before forwarding summaries to an issue tracker.
5. Deduplicate by product, task, version and failure fingerprint; do not merge distinct user harms blindly.
6. Route P0 safety/money/privacy issues to the accountable owner; route suggestions to a separate discovery queue.
7. Link fix commit and release version. Request follow-up only if consented, then record retest as passed/failed/not attempted.

## Example event taxonomy

| Event | Trigger | Safe properties |
| --- | --- | --- |
| feedback_opened | User opens widget | screen_key, app_version |
| feedback_submitted | Valid intake accepted | feedback_id, category, app_version |
| feedback_failed | Intake error | error_class, app_version |
| issue_triaged | Reviewer assigns severity | feedback_id, severity, issue_id |
| fix_retested | Comparable test executed | issue_id, outcome, build |

Never put free-text feedback or personal contact information in analytics event properties.

## GitHub integration

Create a **private** issue with redacted reproduction steps and synthetic account details; add severity, app type and release labels. Keep original participant text in a restricted research store. GitHub Issues APIs and third-party automations may need tokens with narrow scopes; store them only on the server. No GitHub Actions are required for manual issue triage.

## Notion integration

Use a private feedback database with properties: source, task, issue link, severity, status, owner, date and retest. Store participant identifiers in a restricted research area, not a public product backlog. Confirm actual database permissions before integrating.

## Kenya deployment checks

Validate Kenya phone-number handling only if contact is needed; allow anonymous feedback when possible. Confirm ODPC obligations, vendor data flows and cross-border transfer requirements for the actual company. Include English/Kiswahili copy where appropriate.

## Integration acceptance scenarios

- Duplicate webhook creates one logical feedback item.
- User can submit feedback on slow mobile data and recover from a timeout without losing text.
- Malicious markup is rendered as text, not executed.
- Non-consented recording or analytics does not start.
- A private message never appears in a public issue.
- Deletion/retention request removes or appropriately handles records across vendors.
- Fix is not marked verified until a comparable test is actually run.

References: [GitHub Issues API](https://docs.github.com/en/rest/issues/issues), [OWASP Input Validation](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html), [ODPC](https://www.odpc.go.ke/).
