# Feedback intake data contract

| Field | Type | Required? | Notes |
| --- | --- | --- | --- |
| feedback_id | Random opaque ID | Yes | No embedded user identity |
| source | enum | Yes | app, survey, support, session |
| product_version | string | Yes | Versioned build |
| task_key | string | No | Non-identifying task |
| category | enum | Yes | bug, usability, feature, billing, accessibility, safety |
| description | text | Yes | Private; scrub before issue export |
| contact_reference | string | No | Restricted and consented |
| recording_consent | boolean | If recording | Separate from participation |
| followup_consent | boolean | If follow-up | Opt-in |
| created_at | ISO timestamp | Yes | Server-generated |
| status | enum | Yes | new, triaged, in_progress, ready_for_retest, verified, reopened, closed_without_fix |
| issue_ref | string | No | Private tracker reference |
| retention_until | date | Policy-dependent | Do not invent retention period |

Validate inputs, restrict access, rate limit, sanitize downstream display and maintain deletion/retention handling.
