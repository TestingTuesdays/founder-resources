# Backups, disaster recovery and incident simulation

[← Founder resources](../README.md) · [Test cases](test-case-catalog.md) · [Templates](../templates/README.md)

## Who this is for

Products with important data, subscriptions, jobs and multi-region dependencies.

## Why it matters

A nightly backup is not a recovery plan until a restore works and the business has agreed on possible data loss.

## Frequent mistakes

- Never testing restore.
- Keeping backups under identical credentials and failure domain.
- Documenting RTO/RPO without measuring a drill.
- Rolling back code after irreversible schema changes.

## Test scenarios

1. **Restore representative backup into isolated test environment.** Record setup, expected outcome, actual outcome, impact, build/device, owner and comparable retest.
2. **Compare record counts, ownership and integrity checks.** Record setup, expected outcome, actual outcome, impact, build/device, owner and comparable retest.
3. **Measure end-to-end restore time and data age.** Record setup, expected outcome, actual outcome, impact, build/device, owner and comparable retest.
4. **Rotate compromised access and protect backup credentials.** Record setup, expected outcome, actual outcome, impact, build/device, owner and comparable retest.
5. **Recover queue/outbox state without duplicate side effects.** Record setup, expected outcome, actual outcome, impact, build/device, owner and comparable retest.
6. **Reconcile customer communications and post-incident retest.** Record setup, expected outcome, actual outcome, impact, build/device, owner and comparable retest.

## Founder workflow

1. Choose the top one to three real user journeys relevant to your product.
2. Prepare synthetic data and an authorized test environment. Do not share production credentials or personal records.
3. Write observable pass/fail criteria *before* executing the happy path and the failure/recovery scenarios.
4. Run the checks with appropriate devices, identities and permissions. Do not assume an automated tool proves the complete journey.
5. File reproducible defects, assign severity based on harm, fix in a versioned build and retest.
6. Decide go/no-go; block on critical privacy, money, safety, irreversible-data or core-task risks.

## Primary references and tools

| Resource | Value |
| --- | --- |
| [NIST contingency planning](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final) | Primary documentation and implementation patterns |
| [PostgreSQL backup docs](https://www.postgresql.org/docs/current/backup.html) | Primary documentation and implementation patterns |
| [AWS Well-Architected reliability](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html) | Primary documentation and implementation patterns |
| [Google Cloud architecture reliability](https://cloud.google.com/architecture/framework/reliability) | Primary documentation and implementation patterns |

## Expected deliverable

Measured RTO/RPO drill report, recovery owner, unresolved risks and the next drill date.

**Do:** keep assumptions and evidence separate, disclose uncertainty and verify current rules before release. **Don't:** imply testing coverage beyond what was executed, or expose real users and assets to experiments without permission.

_Last edited: 2026-11-23. External policies and tool capabilities can change._
