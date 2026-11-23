# Low-cost founder test stack without hosted CI

[← Tool directory](README.md) · [Manual checks](../docs/manual-quality-checks.md)

The aim is a reliable weekly founder testing cycle without paying for unnecessary tools. Free availability varies by plan and can change; verify official terms.

| Need | Local or open tooling | Founder task |
| --- | --- | --- |
| Browser functional tests | [Playwright](https://playwright.dev/) | Run critical journey with a local browser |
| Unit tests | [Vitest](https://vitest.dev/) | Cover business rules and validators |
| Component tests | [Testing Library](https://testing-library.com/) | Test labels, errors and user interactions |
| Accessibility rule checks | [axe-core](https://github.com/dequelabs/axe-core), [WAVE](https://wave.webaim.org/) | Add keyboard and screen-reader manual tests |
| Network/device debugging | [Chrome DevTools](https://developer.chrome.com/docs/devtools/) | Simulate slow network, storage and CPU |
| Web page diagnostics | [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/) | Measure baseline and trace problems |
| API exploration | [Bruno](https://www.usebruno.com/), [Postman](https://www.postman.com/) | Check auth, errors and contract behavior |
| Basic load simulation | [k6](https://grafana.com/oss/k6/), [Locust](https://locust.io/) | Test authorized staging only |
| Secret scanning | [Gitleaks](https://github.com/gitleaks/gitleaks) | Run locally before publishing |
| Localization | [Weblate](https://weblate.org/), [Tolgee](https://tolgee.io/) | Manage strings and review translations |
| Documentation links | [scripts/check_links.py](../scripts/check_links.py) | Verify internal links manually |
| Perks data format | [scripts/validate_perks.py](../scripts/validate_perks.py) | Catch duplicate/invalid catalog entries |

## Suggested low-cost workflow

1. Run a neutral real-user test; write an observation, not a guessed diagnosis.
2. Reproduce the issue locally on a real target device or browser profile.
3. Add a focused test at the cheapest appropriate layer.
4. Run unit/component, smoke e2e, accessibility spot check and link/perk checks locally.
5. Send a reviewable PR with evidence. Do not enable automatic Actions merely for docs.
6. After publishing, retest real behavior and log outcomes.

**Safety:** local testing does not remove the obligation to protect credentials, private recordings, accessibility, safety or customer information.
