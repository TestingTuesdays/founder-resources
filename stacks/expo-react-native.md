# Expo and React Native mobile QA starter

[← Stack recipes](README.md) · [QA guide](../docs/qa-automation.md) · [Release gate](../docs/release-readiness.md)

## When to use

Use when the app is built in React Native / Expo.

## Founder checklist

- [ ] Define three actual user journeys and success criteria.
- [ ] Run clean signup, returning login, failure/recovery and logout.
- [ ] Test narrow mobile/older device, low bandwidth, keyboard and assistive technologies.
- [ ] Check authorization and data access at the backend, not merely in the UI.
- [ ] Test actual money and notification paths in provider sandboxes.
- [ ] Confirm logs, monitoring, backup/restore, rollback and support ownership.
- [ ] Repeat task after each fix; keep evidence tied to build and environment.

## Stack-specific considerations

Verify native permissions, EAS build profiles, deep links, notifications, background/resume, major iOS and Android versions, store metadata and crash visibility. Do not assume emulator equals physical device.

## Tools and developer references

- [Expo EAS Build](https://docs.expo.dev/build/introduction/)
- [Expo EAS Submit](https://docs.expo.dev/submit/introduction/)
- [Maestro](https://maestro.mobile.dev/)
- [React Native accessibility](https://reactnative.dev/docs/accessibility)

## Do not skip

Use fictional test accounts, avoid public secrets and confirm up-to-date vendor and store policy. Do not claim complete security, accessibility or test coverage solely from this starter checklist.

**Output:** test matrix, priority issues, release decision and comparable retest evidence.
