# 30 common founder testing mistakes

[← Home](../README.md) · [Test cases](test-case-catalog.md)

| # | Mistake | Correction |
| --- | --- | --- |
| 1 | Testing only the happy path | Try invalid inputs, failures, cancellations and retries |
| 2 | Demonstrating instead of observing | Use a neutral unassisted task |
| 3 | Only recruiting friends | Recruit actual target users |
| 4 | Using opinions as success metrics | Record behavior and task outcome |
| 5 | Not retesting the same task | Compare outcome on versioned builds |
| 6 | Treating a build as launch-ready | Run a release gate and smoke tests |
| 7 | Skipping narrow mobile screens | Test on representative phones |
| 8 | Ignoring keyboard access | Complete full journey with keyboard |
| 9 | Trusting accessibility scanners alone | Add screen-reader and human checks |
| 10 | Never testing reset-token expiry | Try expired, reused and invalid links |
| 11 | Checking access only in UI | Enforce server-side object authorization |
| 12 | Forgetting tenant isolation | Test cross-organization access attempts |
| 13 | Committing secrets | Scan and rotate leaked keys |
| 14 | Using genuine customer accounts | Use synthetic, restricted test data |
| 15 | Publishing user recordings | Get consent; redact and restrict |
| 16 | Ignoring duplicate submits | Make operations idempotent |
| 17 | Assuming webhooks arrive once | Retry, reorder and replay in sandbox |
| 18 | Only testing paid conversion | Test decline, cancel, refund, trial end |
| 19 | No deletion/export path | Implement published and legal obligations |
| 20 | Hardcoding US conventions | Use locale-based dates, currency and names |
| 21 | Translating without layout checks | Pseudolocalize and test RTL |
| 22 | Only fast-network testing | Simulate latency and offline |
| 23 | Optimizing one Lighthouse score | Use real-user task and performance metrics |
| 24 | Every check is full e2e | Balance unit, integration and e2e tests |
| 25 | Disabling flaky tests quietly | Track and fix cause |
| 26 | No incident owner or rollback | Assign and practice them |
| 27 | Assuming store upload is approval | Check review rules and metadata |
| 28 | Assuming permissions granted | Test denial and revocation |
| 29 | AI evaluated by three prompts | Build representative versioned evals |
| 30 | Counting closed ticket as validated | Require comparable observed retest |

Pick five relevant mistakes. For each record: workflow, reproduced observation, severity, fix owner, regression test and retest result. Use [the bug report template](../templates/bug-report.md).
