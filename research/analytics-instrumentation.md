# Consent-aware product analytics and user testing events

[← Research hub](README.md) · [Product analytics quality](../docs/product-analytics-quality.md)

## Measurement plan

Choose a critical user journey, such as visit → signup → first task → success → return. Define each event once with exact trigger, properties, owner and exclusions. Count **successful task completion** separately from button clicks and page views.

| Event | Exact trigger | Useful safe dimensions | Risk |
| --- | --- | --- | --- |
| signup_started | User begins signup | channel, app_version | Do not send email |
| signup_completed | Server confirms account creation | app_version | Avoid duplicate events |
| task_started | User enters primary task | task_key, platform | Avoid free-text inputs |
| task_completed | Backend confirms desired outcome | task_key, duration_bucket | Client click may be false success |
| task_failed | Verified failure state | error_class, task_key | Do not log secrets |
| feedback_submitted | Intake stored successfully | category, app_version | Never send raw feedback |

## Implementation and validation

1. Publish a schema and owner before instrumenting.
2. Gate optional analytics on applicable consent; preserve necessary product operations separately.
3. Test identity transitions, retries, offline events and duplicate submission.
4. Reconcile funnel counts against backend source-of-truth for sample synthetic users.
5. Monitor event volume and cost, and verify opt-out and deletion flows.
6. Segment results by representative device/network/locale only when privacy-safe and statistically appropriate.

## Analysis caution

Small samples can be directional but not representative. Correlation between a new UI and improved clicks does not prove causation. Report denominator, window, exclusions and uncertainty; never invent conversion rates.

References: [PostHog docs](https://posthog.com/docs), [Amplitude docs](https://amplitude.com/docs), [W3C privacy](https://www.w3.org/Privacy/).
