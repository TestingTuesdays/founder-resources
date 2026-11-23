# Hardware, IoT & connected products

[← Resource home](../README.md) · [Test catalog](test-case-catalog.md) · [Report a bug](../templates/bug-report.md)

## Why this matters

Verify device safety, offline behavior, onboarding, firmware and service reliability.

## Typical founder mistakes

- Testing only with a developer-connected device
- No safe response to power or connectivity loss
- Not verifying firmware update rollback or device ownership transfer
- Using consumer telemetry as a substitute for physical safety testing

## Run these tests

1. **Provisioning on new phone/router with invalid credentials.** Write precondition, expected and actual result, build/version, device, severity, owner and retest status.
2. **Power loss during device operation and update.** Write precondition, expected and actual result, build/version, device, severity, owner and retest status.
3. **Bluetooth/Wi-Fi interference and network recovery.** Write precondition, expected and actual result, build/version, device, severity, owner and retest status.
4. **Firmware version migration and rollback strategy.** Write precondition, expected and actual result, build/version, device, severity, owner and retest status.
5. **Factory reset/ownership transfer and credential revocation.** Write precondition, expected and actual result, build/version, device, severity, owner and retest status.
6. **Device telemetry dropout and false-positive/negative alarms.** Write precondition, expected and actual result, build/version, device, severity, owner and retest status.

## Recommended workflow

Build a device/software/failure matrix with explicit safety stops. Test under supervised conditions and validate electrical, mechanical, wireless, privacy and regulatory obligations with qualified specialists before real-world deployment.

## Tools and official references

| Resource | Use it for |
| --- | --- |
| [ESP-IDF docs](https://docs.espressif.com/projects/esp-idf/en/stable/) | Embedded development |
| [Zephyr docs](https://docs.zephyrproject.org/latest/) | RTOS and testing |
| [PlatformIO](https://platformio.org/) | Embedded workflow |
| [Wireshark](https://www.wireshark.org/) | Network diagnostics |
| [OWASP IoT](https://owasp.org/www-project-internet-of-things/) | IoT threat awareness |

## Do / don't

**Do:** test with representative people and devices, capture non-sensitive evidence, verify failure/recovery, assign ownership and retest the shipped fix.

**Don't:** rely solely on tool scores, copy unverified claims from a vendor, expose customer data, or call an unobserved outcome a passed test.

## Session deliverable

Bring one specific workflow, a safe build/test account, two or more reproducible observations, a severity-ranked fix list, and an agreed follow-up. [Use the session template](../templates/usability-session.md) and [retest sheet](../templates/retest.md).

_Last reviewed: 2026-11-23. Prices, support and platform rules may change._
