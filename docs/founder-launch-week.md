# Founder launch-week quality playbook

[← Home](../README.md) · [Release gate](release-readiness.md) · [Session kit](testing-tuesdays-session-kit.md)

## T-7 to T-4 days — prove critical tasks

- Confirm three tasks and measurable success criteria; run a usability session with an intended user.
- Exercise authorization, payment, cancellation, help and data access; fix release-blocking issues.
- Test mobile narrow layouts, keyboard, screen reader, slow networks and target locale.
- Write a rollback and recovery plan with an owner.

## T-3 to T-1 days — rehearse release

- Freeze high-risk feature expansion and approve scope. Test migrations on realistic synthetic data.
- Monitor errors, latency, storage, queue failures and usage budgets.
- Validate store submissions and reviewer access if mobile.
- Verify support mailbox, receipts, monitoring alerts, privacy and operational contacts.

## Launch day — release with controls

- Record build SHA, environment, start time and reviewer.
- Use staged deployment / flags for riskier features and observe core task behavior.
- Run smoke tests with fictional data after production deployment.
- Check unexpected errors, payment state, security signals and spend.
- Stop or roll back on explicit thresholds; do not trade real user safety for launch announcements.

## T+1 to T+7 — retest and learn

- Compare real-user task success, retention and support issues with baseline.
- Fix the highest-impact regressions, retest comparable tasks and record what genuinely improved.
- Write a short incident/learning note without exposing private records.
- Reconcile paid provider charges and startup-credit expiration where applicable.

## Launch decision document

**Release version:** …  **Owner:** …  **Critical tasks tested:** …  **Known blockers:** …  **Approved residual risks:** …  **Rollback trigger/owner:** …  **Observed post-launch result:** …

Use [release checklist](../templates/release-checklist.md), [quality scorecard](../templates/founder-scorecard.md) and [retest log](../templates/retest.md).
