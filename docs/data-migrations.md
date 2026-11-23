# Data quality, migrations & backups

[← Resource home](../README.md) · [Release checklist](release-readiness.md)

## Why founders should care

Most serious launch incidents are integrity bugs, not cosmetic defects.

## Common mistakes

- Assuming a successful demo or dashboard proves the experience works for all users.
- Ignoring errors, permission boundaries, mobile constraints and exceptional states.
- Launching without a responsible owner, observable outcome or fallback.
- Using vendor tooling without checking costs, data protection or real capabilities.

## Core test scenarios

1. **Schema migration works with existing non-empty records.** Record build/environment, expected vs actual, user impact and follow-up.
2. **Forward deploy and rollback keep compatible readers.** Record build/environment, expected vs actual, user impact and follow-up.
3. **Concurrent edits do not overwrite data unexpectedly.** Record build/environment, expected vs actual, user impact and follow-up.
4. **Import with malformed rows is rejected/partially handled safely.** Record build/environment, expected vs actual, user impact and follow-up.
5. **Backup restore checked in isolated environment.** Record build/environment, expected vs actual, user impact and follow-up.
6. **Timezone, decimal and null values round-trip correctly.** Record build/environment, expected vs actual, user impact and follow-up.

## Practical workflow

1. Identify the most important user task and a measurable success criterion.
2. Use safe synthetic data and a representative device/locale/account.
3. Test the expected route **and** failure/recovery case; observe results, not assumptions.
4. Check privacy/security, accessibility and reliability considerations where relevant.
5. File a reproducible issue, assign an owner and retest after the deployed fix.

## Trusted tools and reference material

| Reference | What it helps with |
| --- | --- |
| [PostgreSQL docs](https://www.postgresql.org/docs/) | Database practices |
| [Prisma Migrate](https://www.prisma.io/docs/orm/prisma-migrate) | Schema migration |
| [Supabase database docs](https://supabase.com/docs/guides/database) | Managed Postgres |
| [Great Expectations](https://greatexpectations.io/) | Data validation |
| [OpenTelemetry](https://opentelemetry.io/) | Change monitoring |

## Go/no-go consideration

Do not call this area ready if the core journey can cause loss of data, money, privacy or user access without a documented safe recovery path. Regulations and provider requirements change: review official documentation for your specific product and market.

_Last curated: 2026-11-23._
