# Conducting useful user testing

[← Research hub](README.md) · [Session template](../templates/usability-session.md)

## Choose a method based on the question

| Question | Method | What it proves / does not prove |
| --- | --- | --- |
| Can a first-time user complete a task? | Moderated usability session | Observed behavior; not statistical market demand |
| Where do users fail at scale? | Instrumented funnel + sampled session review | Behavioral pattern; not necessarily cause |
| Which label is understood? | First-click or comprehension test | Findability/meaning; not retention |
| What do users say they want? | Interview or survey | Stated preference; not actual usage |
| Is a change better? | Comparable retest or controlled experiment | Measured outcome under stated conditions |
| Does app work in Kenya? | Real device, mobile data, language and payment-app switching | Tested context only; not every Kenyan user |

## Prepare

- Define one product task in plain language: “You need to send a receipt to a customer; show how.” Do not instruct which button to press.
- Recruit the *intended user*, not only friends or developers. Screen for relevant experience and device access without collecting unnecessary sensitive data.
- Write task success criteria before testing: unassisted success, assisted success, incomplete, not attempted.
- Prepare fictional accounts and a resettable build; test sign-up, core value and failure recovery separately.
- Explain voluntary participation, recording choice, compensation, retention and withdrawal route. Do not make marketing consent a prerequisite.

## Suggested 30-minute moderated session

| Time | Activity | Moderator behavior |
| --- | --- | --- |
| 0–4 min | Consent and context | Explain that product, not participant, is being tested |
| 4–6 min | Task setup | Read neutral task once |
| 6–18 min | User attempts task | Observe; do not coach or defend UI |
| 18–23 min | Follow-up questions | “What did you expect?” / “Where were you uncertain?” |
| 23–27 min | Additional failure state | Test one recovery path if safe |
| 27–30 min | Close | Explain follow-up and data handling |

## Unmoderated testing

Keep tasks short and unambiguous, test the prototype link yourself, define the start state, provide accessible alternatives and use a post-task question. Exclude invalid or abandoned attempts transparently; do not invent completion rates.

## Record evidence

For each task record anonymized participant ID, build, device, language, network, success state, time if measured, observed friction, exact non-identifying quote if consented, severity and proposed retest. Separate **what happened** from **what we think caused it**.

## After the session

Group repeated problems by task and severity. Create one issue per reproducible defect, link supporting redacted evidence privately, assign owner, deploy fix and retest with comparable tasks. Follow up with participants only if they agreed.

## Kenya considerations

Include older Android devices, shared phones, mobile data constraints, Kiswahili/English and other target languages, KES and M-Pesa prompt switching where relevant. Do not generalize from Nairobi tech-community participants to all Kenyan users.

References: [GOV.UK user research](https://www.gov.uk/service-manual/user-research), [Nielsen Norman Group](https://www.nngroup.com/), [W3C WAI](https://www.w3.org/WAI/).
