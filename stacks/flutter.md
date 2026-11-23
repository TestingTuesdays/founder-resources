# Flutter app QA starter

[← Stack recipes](README.md) · [QA guide](../docs/qa-automation.md) · [Release gate](../docs/release-readiness.md)

## When to use

Use for cross-platform mobile apps.

## Founder checklist

- [ ] Define three actual user journeys and success criteria.
- [ ] Run clean signup, returning login, failure/recovery and logout.
- [ ] Test narrow mobile/older device, low bandwidth, keyboard and assistive technologies.
- [ ] Check authorization and data access at the backend, not merely in the UI.
- [ ] Test actual money and notification paths in provider sandboxes.
- [ ] Confirm logs, monitoring, backup/restore, rollback and support ownership.
- [ ] Repeat task after each fix; keep evidence tied to build and environment.

## Stack-specific considerations

Test widgets and business logic with Flutter test tooling, integration flows on actual devices, permission denied, upgrade migration, text scaling, localization and app review. Verify stores separately.

## Tools and developer references

- [Flutter testing](https://docs.flutter.dev/testing)
- [Flutter accessibility](https://docs.flutter.dev/ui/accessibility-and-internationalization/accessibility)
- [Flutter internationalization](https://docs.flutter.dev/ui/accessibility-and-internationalization/internationalization)

## Do not skip

Use fictional test accounts, avoid public secrets and confirm up-to-date vendor and store policy. Do not claim complete security, accessibility or test coverage solely from this starter checklist.

**Output:** test matrix, priority issues, release decision and comparable retest evidence.
