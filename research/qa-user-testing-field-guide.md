# Practical QA and real-user testing field guide

## Start with a risk, not a tool
Choose one critical journey, expected result, target user, test environment, test data and failure severity. A passing automated test does not prove usability. A preference survey does not prove task completion. Keep production secrets and participant recordings out of public issues.

| Layer | Low-cost starting tools | When to consider paid tooling |
|---|---|---|
| Unit | Vitest, Jest, pytest | Coverage trends or large-scale parallelization |
| Browser E2E | Playwright, Cypress | Real-device/browser matrix and parallel cloud runs |
| Mobile | Maestro, Appium, Android emulator, Xcode simulator | Physical device coverage and remote labs |
| API | Bruno, Postman, REST Assured, Pact | Shared contracts, monitoring and collaboration |
| Visual | Playwright screenshots, Storybook | Cross-browser visual baselines and review |
| Accessibility | axe-core, Lighthouse, NVDA, TalkBack, VoiceOver | Expert audit and assisted testing |
| Performance | k6, Locust, Artillery, Lighthouse | Load infrastructure and continuous monitoring |
| Security | OWASP ZAP, Semgrep, dependency audit | Authorized expert review, compliance and triage |
| Analytics | Product events and a privacy-safe funnel | Higher-volume cohorts and experiments |
| User research | Consented interviews, task observation, simple forms | Targeted recruitment, remote panels and synthesis |
| AI | Promptfoo, DeepEval, local labeled cases | Managed eval, traces and review workflows |
| Email | Mailpit, local sandbox | Cross-client rendering and deliverability analysis |

## Weekly founder workflow
Before session: choose one task and expected evidence; prepare synthetic test accounts, device matrix and consent script. During: moderator reads neutral task, observes without coaching, marks independent success / assisted / failed / abandoned, records elapsed time only if relevant and permission-safe notes. QA reproduces separately with exact build, device, OS, network, expected/actual. After: prioritize safety/data loss and blocked core journeys, assign one owner and due date; fix; retest comparable scenario; record what changed. Do not count unattempted tests as passes.

## Real-user recruiting
Define behavior-based screening (e.g. merchants who reconcile mobile payments weekly), recruit from relevant communities with permission, offer transparent compensation without requiring positive feedback, minimize data and accommodate accessibility/language needs. Start with a small qualitative round of 3–5 matched users; treat findings as directional, not population estimates. Recruit new users for first-use learning and comparable users for retest. Avoid using founders as substitutes for target customers. Separate consent for recordings, quotes and sharing. For Kenya include low-cost Android, mobile data, intermittent connections, English/Swahili where appropriate, and authorized payment sandboxes. Do not assume every Kenyan user shares a device, network or language.

## Templates
Task card: product/build | target persona | scenario | starting state | goal | success condition | timebox | safety/consent.
Observation: task ID | anonymous participant ID | outcome | obstacle | evidence reference | moderator assistance | follow-up question.
Bug: title | environment | steps | expected | actual | reproducibility | severity | sanitized evidence | owner | retest.
Recruitment screener: relevant behavior | frequency | device/accessibility needs (optional) | availability | consent | compensation terms.
Research decision: hypothesis | sample and recruitment | task outcomes (counts/denominator) | patterns | contradictory evidence | action | retest date.
Release gate: critical flows, negative paths, accessibility, rollback, monitoring, data integrity; any unresolved high-risk issue requires explicit decision by owner.

## Specialist checks
Fintech: sandbox payment initiation, timeout, duplicate callback, reconciliation, refund and offline retry; no real money without authorization.
Health: accessibility, consent, safe failure, data deletion and clinical review; no diagnosis claims from QA.
Marketplaces: inventory concurrency, search, seller/buyer permissions, failed payment, refund.
AI: labeled gold set, grounding, abstention, prompt injection resilience, latency/cost, human review; no real sensitive prompts.
SaaS: tenant isolation, auth recovery, invite, billing, cancellation, export.
Mobile: permissions denied, background/foreground, low storage, flaky network, battery and physical device.
Hardware: simulator/bench test, sensor failure, telemetry loss, safe stop and physical safety review.

## Tool acquisition and ROI
Use free or local baseline first, then choose paid access only for a specific uncovered risk. Compare device minutes, seats, panel incentives, storage, data residency, export and renewal. See [QA and startup perks](../perks/qa-research-and-startup-expansion.md). Provider pricing and licenses must be checked before use. No vendor endorsement or confirmed community deal.
