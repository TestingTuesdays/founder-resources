---
name: pwa-offline-audit
description: Verify PWA offline and upgrade behavior for founders developing and testing real products.
---

# Verify PWA offline and upgrade behavior

[← All skills](../README.md) · [Practical guide](../../docs/pwa-offline.md)

## Goal

Make a founder's testing action repeatable and independently verifiable.

## Required inputs

An authorized product/environment, versioned build, representative sample accounts, explicit pass/fail criterion, and appropriate privacy/research permissions.

## Procedure

1. Identify which journeys genuinely work offline and which require network.
2. Test install, first offline load and network restoration on real target devices.
3. Queue a permitted action; ensure replay happens only once.
4. Sign out and change accounts; ensure cached private data is not exposed.
5. Deploy new service worker in staging and verify upgrade/rollback behavior.

## Done when

A capability matrix stating tested offline flows, sync behavior and unresolved storage/security risks.

## Restrictions

Do not state an outcome as passed until it was run. Use synthetic data for public examples and keep billing identifiers, participants' information, secrets and private accounts out of the open repository. Stop and escalate if the test could harm real customers or physical systems.

[Use a test case](../../templates/test-case.md) · [Report a bug](../../templates/bug-report.md) · [Verify a fix](../../templates/retest.md).
