---
name: data-migration-review
description: Verify schema/data migrations, backward compatibility and recovery before deployment.
---

# Data migration review

[← Skills](../README.md) · [Data quality guide](../../docs/data-migrations.md)

## Inputs

Migration diff, schema contract, representative synthetic dataset, backup/restore procedure and rollback owner.

## Procedure

1. Identify altered tables/fields, readers/writers and default/null behavior.
2. Test migration with existing and edge-case records, not only empty database.
3. Validate simultaneous old/new application versions where rollout requires it.
4. Check counts, constraints, precision, timezone handling and corruption detection.
5. Exercise restore or forward-fix in isolated staging, with clear stop conditions.
6. Record results, owner and deploy/rollback order.

## Done when

Data integrity and recovery have actual test evidence. Never trial destructive migrations against real production data without authorized change controls.
