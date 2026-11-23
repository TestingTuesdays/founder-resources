---
name: production-incident-drill
description: Rehearse detection, user impact assessment, rollback and recovery on safe environments.
---

# Production incident and rollback drill

[← Skills](../README.md) · [Operations](../../docs/support-operations.md)

## Required inputs

System diagram, test environment, alert owner, recovery objective, rollback steps and synthetic data.

## Procedure

1. Select one realistic fault: deploy regression, slow provider, failed background job or database outage.
2. Confirm alerts and detect the fault without introducing harm to real users.
3. Record user impact and identify the incident commander.
4. Revert the change or recover state with agreed procedure.
5. Re-run smoke tests and check data consistency.
6. Write a blameless learning note with follow-ups and owner.

## Done when

Detection, escalation, restoration, data validation and communication are recorded with evidence. Never intentionally disrupt production without explicit authorization and controls.
