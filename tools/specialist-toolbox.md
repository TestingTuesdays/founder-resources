# Specialist founder QA and product tools

[← Tool directory](README.md) · [App playbooks](../app-types/README.md) · [Skills](../skills/README.md)

These are **tool discovery references**, not endorsements, verified free plans or proof of current pricing. Prefer open-source/local tools when they meet the need; verify provider terms and data-handling before uploading private data.

## Mobile testing and performance

| Tool | Use | Selection caveat |
| --- | --- | --- |
| [Maestro](https://maestro.mobile.dev/) | Mobile UI flows | Test on actual target OS/device |
| [Appium](https://appium.io/) | Cross-platform app automation | Requires maintained device drivers |
| [Firebase Test Lab](https://firebase.google.com/docs/test-lab) | Device lab | Check quotas and data collection |
| [Android Studio Profiler](https://developer.android.com/studio/profile) | Memory, CPU and network | Android-specific |
| [Xcode Instruments](https://developer.apple.com/xcode/features/) | iOS profiling | Requires Apple tooling |
| [WebPageTest](https://www.webpagetest.org/) | Realistic web performance | Check test location/device |

## Accessibility, usability and visual quality

| Tool | Use | Selection caveat |
| --- | --- | --- |
| [axe-core](https://github.com/dequelabs/axe-core) | Automated accessibility rules | Cannot replace manual testing |
| [Accessibility Insights](https://accessibilityinsights.io/) | Guided accessibility checks | Manual task review still needed |
| [Pa11y](https://pa11y.org/) | CLI accessibility tests | Test real task flows |
| [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/) | Performance and accessibility hints | Lab results are not field results |
| [Storybook](https://storybook.js.org/) | Component states | Cover error/empty/loading states |
| [BackstopJS](https://github.com/garris/BackstopJS) | Visual regression | Review differences, not just pixels |

## APIs, security and observability

| Tool | Use | Selection caveat |
| --- | --- | --- |
| [Bruno](https://www.usebruno.com/) | Local API collections | Never commit secrets |
| [Schemathesis](https://schemathesis.readthedocs.io/) | API schema-driven tests | Authorized endpoints only |
| [Pact](https://pact.io/) | Consumer-driven contracts | Maintain contracts with releases |
| [OWASP ZAP](https://www.zaproxy.org/) | Authorized web security testing | Never scan unowned systems |
| [Gitleaks](https://github.com/gitleaks/gitleaks) | Secret scanning | Remove exposed keys and rotate |
| [OSV-Scanner](https://google.github.io/osv-scanner/) | Dependency vulnerabilities | Verify advisories and fix impact |
| [OpenTelemetry](https://opentelemetry.io/) | Traces and metrics | Redact sensitive data |
| [Grafana k6](https://grafana.com/oss/k6/) | Load and reliability | Obtain permission; use staging |

## AI and search quality

| Tool | Use | Selection caveat |
| --- | --- | --- |
| [promptfoo](https://www.promptfoo.dev/) | Prompt/model regression and red-team evals | Use controlled data and tools |
| [Ragas](https://docs.ragas.io/) | RAG evaluation | Calibrate metrics against humans |
| [DeepEval](https://deepeval.com/) | LLM evaluation | Check version and data handling |
| [Langfuse](https://langfuse.com/) | LLM tracing and quality | Scrub prompts and PII |
| [Google Search Console](https://search.google.com/search-console/about) | Indexing and search performance | No ranking guarantees |
| [Rich Results Test](https://search.google.com/test/rich-results) | Structured-data eligibility checks | Syntax alone does not earn rich results |
| [Schema Markup Validator](https://validator.schema.org/) | Schema.org syntax | Must match visible content |

## Payments and Kenya-specific integrations

| Resource | Use | Caution |
| --- | --- | --- |
| [Safaricom Daraja](https://developer.safaricom.co.ke/) | M-Pesa developer entry point | Sandbox is not merchant approval |
| [Paystack docs](https://paystack.com/docs/) | Payment API integration | Verify merchant entity eligibility |
| [Flutterwave docs](https://developer.flutterwave.com/) | Payment API integration | Verify supported methods/settlement |
| [CBK](https://www.centralbank.go.ke/) | Regulatory discovery | Current activity-specific rules apply |
| [ODPC](https://www.odpc.go.ke/) | Data protection | Not a substitute for legal review |
| [KRA](https://www.kra.go.ke/) | Tax and eTIMS | Accountant review may be needed |

## Tool-selection worksheet

Define the specific task, data sensitivity, expected coverage, supported OS/country, price/seat costs, exportability, manual maintenance and proof that a tool helped catch a real defect. A free tier or startup perk is not assumed unless verified directly.
