# Security, privacy & trust

[← Resource home](../README.md) · [Test catalog](test-case-catalog.md) · [Report a bug](../templates/bug-report.md)

## Why this matters

Protect user data and prevent privilege escalation, unauthorized access and unsafe processing.

## Typical founder mistakes

- Checking roles in the UI but not on the server
- Testing with real customer data
- Leaving secrets in logs or source control
- Assuming an automated vulnerability scanner is a penetration test

## Run these tests

1. **User A cannot fetch User B's object by URL/ID.** Write precondition, expected and actual result, build/version, device, severity, owner and retest status.
2. **Tenant A cannot export or search Tenant B records.** Write precondition, expected and actual result, build/version, device, severity, owner and retest status.
3. **Password reset link expires and cannot be reused.** Write precondition, expected and actual result, build/version, device, severity, owner and retest status.
4. **Files reject dangerous sizes/types and malformed names.** Write precondition, expected and actual result, build/version, device, severity, owner and retest status.
5. **Public bundle and logs contain no secrets.** Write precondition, expected and actual result, build/version, device, severity, owner and retest status.
6. **Payment webhook rejects invalid signatures and replayed events.** Write precondition, expected and actual result, build/version, device, severity, owner and retest status.
7. **Account deletion and retention match published promises.** Write precondition, expected and actual result, build/version, device, severity, owner and retest status.

## Recommended workflow

Threat-model sensitive workflows, enforce least privilege and authorization at data boundaries, scan secrets and dependencies, review access logs and test privacy promises. Only security-test systems you own or have permission to assess. Requirements vary by jurisdiction and sector.

## Tools and official references

| Resource | Use it for |
| --- | --- |
| [OWASP ASVS](https://asvs.owasp.org/) | Application-security verification |
| [OWASP Cheat Sheets](https://cheatsheetseries.owasp.org/) | Implementation guidance |
| [OWASP MASVS](https://mas.owasp.org/) | Mobile security |
| [OWASP ZAP](https://www.zaproxy.org/) | Authorized web security testing |
| [CodeQL](https://codeql.github.com/) | Static code analysis |
| [Semgrep](https://semgrep.dev/) | Security rules |
| [Gitleaks](https://github.com/gitleaks/gitleaks) | Secret scanning |
| [NIST SSDF](https://csrc.nist.gov/projects/ssdf) | Secure development lifecycle |

## Do / don't

**Do:** test with representative people and devices, capture non-sensitive evidence, verify failure/recovery, assign ownership and retest the shipped fix.

**Don't:** rely solely on tool scores, copy unverified claims from a vendor, expose customer data, or call an unobserved outcome a passed test.

## Session deliverable

Bring one specific workflow, a safe build/test account, two or more reproducible observations, a severity-ranked fix list, and an agreed follow-up. [Use the session template](../templates/usability-session.md) and [retest sheet](../templates/retest.md).

_Last reviewed: 2026-11-23. Prices, support and platform rules may change._
