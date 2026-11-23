# Testing Tuesdays founder session kit

[← Founder resources](../README.md) · [Start guide](START-HERE.md) · [Participant recruitment](participant-recruitment.md)

**Working products. Real users. Better releases.** This public educational kit is a reusable way to bring a functional product to a Testing Tuesdays-style session; it does not confer cohort admission, RSVP or confirmed event entry. Private organizer rules and schedule remain in the official program workspace.

## Before the session

1. Write a single **observable task** that a user can complete on your current build. Example: “You have to update your subscription before the next renewal. Show what you would do.”
2. Define the intended user, safe demo URL, 2–3 synthetic test accounts and a way to reset state between participants.
3. Set success criterion, known risks, available browsers/devices, and one feature that must not be tested with personal data.
4. Create a consent and accessibility plan; participants can decline recording while still participating when feasible.
5. Prepare a one-page task sheet, not a sales pitch; no need to disclose sensitive business metrics.

## Thirty-minute test block

| Minute | Activity | Rule |
| --- | --- | --- |
| 0–3 | Introductions, consent and safety | Participation voluntary; product is being evaluated, not the user |
| 3–5 | State user-context task | Do not reveal button or path |
| 5–15 | Independent attempt | Observe without coaching; note failures and recovery |
| 15–19 | Neutral follow-up | Ask expectations and frustration, not leading opinions |
| 19–24 | Summarize observations | Separate facts from proposed fixes |
| 24–28 | Rank most important issue | Severity from user impact, not founder preference |
| 28–30 | Assign next fix and comparable retest | Capture owner, build and due date |

## Report format

**Task / persona / build:** …  
**Observed outcome:** unassisted / assisted / incomplete / not attempted  
**Key observations:** …  
**Severity and reason:** …  
**Fix, owner and due session:** …  
**Retest build/date/outcome:** …

## What to avoid

- No live customer accounts, unreleased payment credentials, identifiable user recordings in public resources or “testers must approve us” pressure.
- Do not present another founder's peer test as independent target-user research.
- Do not count a feature demo, ticket closure or merged PR as a successful retest.
- Do not promise public registration before organizers confirm it.

[Copyable usability session template](../templates/usability-session.md) · [Bug report](../templates/bug-report.md) · [Ship-back](../templates/retest.md).
