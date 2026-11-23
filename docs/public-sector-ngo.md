# Public-sector, NGO and civic-tech readiness

[← Resource home](../README.md) · [Release gate](release-readiness.md) · [Testing templates](../templates/README.md)

## For whom

Founders serving schools, governments, nonprofits and community organizations.

## The failure you are trying to prevent

Product quality is about actual user outcomes, not only whether a build compiles. Verify a realistic journey and the ways it can fail, then retest after changes.

## Common mistakes

- Excluding people with low literacy or assistive technology
- Losing essential records in offline field workflows
- Assuming all workers have continuous connectivity
- Recording sensitive beneficiary data in demos
- Promising interoperability or procurement compliance without evidence

## Run this test plan

1. **Test plain-language task understanding with intended service users.** Record version/environment, starting state, expected result, actual observation, impact, owner and retest outcome.
2. **Use device keyboard/screen-reader and local-language task scripts.** Record version/environment, starting state, expected result, actual observation, impact, owner and retest outcome.
3. **Exercise offline data collection, conflict and consent withdrawal.** Record version/environment, starting state, expected result, actual observation, impact, owner and retest outcome.
4. **Review role access to beneficiary records and retention.** Record version/environment, starting state, expected result, actual observation, impact, owner and retest outcome.
5. **Test CSV/PDF exports with accessible formatting and safe data.** Record version/environment, starting state, expected result, actual observation, impact, owner and retest outcome.
6. **Document legal/procurement and security requirements per buyer.** Record version/environment, starting state, expected result, actual observation, impact, owner and retest outcome.

## Working method

**Prepare:** select three high-risk tasks and a realistic device, account and permission profile. Use fictional data; do not disclose user recordings, credentials or restricted company information.

**Observe:** run both successful and failure/recovery paths. Distinguish a user's observed behavior from the researcher's proposed solution.

**Prioritize:** flag data loss, harm, exposed private information and blocked primary user actions before cosmetic problems. Record any accepted risk with an accountable owner.

**Verify:** deploy a versioned fix, repeat the same task under comparable conditions and record improved/unchanged/worse/pending outcome.

## Official documentation and useful tools

| Reference | When it helps |
| --- | --- |
| [GOV.UK Service Manual](https://www.gov.uk/service-manual) | Primary documentation, methods or diagnostics |
| [W3C WAI](https://www.w3.org/WAI/) | Primary documentation, methods or diagnostics |
| [UNICEF digital public goods](https://www.unicef.org/innovation/digitalpublicgoods) | Primary documentation, methods or diagnostics |
| [Digital Public Goods Alliance](https://digitalpublicgoods.net/) | Primary documentation, methods or diagnostics |
| [OpenAPI Specification](https://spec.openapis.org/oas/latest.html) | Primary documentation, methods or diagnostics |

## Completion evidence

Inclusive service journey, data-handling map, offline and accessibility verification, buyer-specific obligation checklist.

## Don't overclaim

A single pass does not prove all users, devices, jurisdictions or failure conditions are covered. Tool limits and external rules evolve. Recheck official sources before a regulated or commercially consequential release.

_Last curated: 2026-11-23._
