# Release engineering, CI/CD and deployment safety

[← Resource home](../README.md) · [Release gate](release-readiness.md) · [Testing templates](../templates/README.md)

## For whom

Teams with a working application preparing repeatable staging-to-production changes.

## The failure you are trying to prevent

Product quality is about actual user outcomes, not only whether a build compiles. Verify a realistic journey and the ways it can fail, then retest after changes.

## Common mistakes

- Committing straight to production with no staging verification
- Schema change breaking previously deployed clients
- Rollback reverting code but not incompatible data
- Feature flag forgotten after a launch
- Unclear owner for smoke tests and post-release monitoring

## Run this test plan

1. **Deploy from a clean commit to an isolated preview/staging environment.** Record version/environment, starting state, expected result, actual observation, impact, owner and retest outcome.
2. **Seed fictional accounts, exercise three critical tasks and their failures.** Record version/environment, starting state, expected result, actual observation, impact, owner and retest outcome.
3. **Apply migrations with existing records and a staged old-client compatibility check.** Record version/environment, starting state, expected result, actual observation, impact, owner and retest outcome.
4. **Gate feature exposure by account and verify kill switch.** Record version/environment, starting state, expected result, actual observation, impact, owner and retest outcome.
5. **Roll back an intentionally faulty staging release while preserving data.** Record version/environment, starting state, expected result, actual observation, impact, owner and retest outcome.
6. **Verify release notes, ownership, alert thresholds and support escalation.** Record version/environment, starting state, expected result, actual observation, impact, owner and retest outcome.

## Working method

**Prepare:** select three high-risk tasks and a realistic device, account and permission profile. Use fictional data; do not disclose user recordings, credentials or restricted company information.

**Observe:** run both successful and failure/recovery paths. Distinguish a user's observed behavior from the researcher's proposed solution.

**Prioritize:** flag data loss, harm, exposed private information and blocked primary user actions before cosmetic problems. Record any accepted risk with an accountable owner.

**Verify:** deploy a versioned fix, repeat the same task under comparable conditions and record improved/unchanged/worse/pending outcome.

## Official documentation and useful tools

| Reference | When it helps |
| --- | --- |
| [GitHub deployment environments](https://docs.github.com/en/actions/reference/workflows-and-actions/deployments-and-environments) | Primary documentation, methods or diagnostics |
| [Vercel deployments](https://vercel.com/docs/deployments) | Primary documentation, methods or diagnostics |
| [Cloudflare Pages](https://developers.cloudflare.com/pages/) | Primary documentation, methods or diagnostics |
| [Argo Rollouts](https://argo-rollouts.readthedocs.io/) | Primary documentation, methods or diagnostics |
| [OpenFeature](https://openfeature.dev/) | Primary documentation, methods or diagnostics |
| [Sentry releases](https://docs.sentry.io/product/releases/) | Primary documentation, methods or diagnostics |

## Completion evidence

A release record with immutable build, staging results, named owner, feature flags, rollback evidence and post-release observations.

## Don't overclaim

A single pass does not prove all users, devices, jurisdictions or failure conditions are covered. Tool limits and external rules evolve. Recheck official sources before a regulated or commercially consequential release.

_Last curated: 2026-11-23._
