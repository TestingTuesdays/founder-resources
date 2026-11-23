# Zero-CI local HTML metadata auditor

[← Tools](README.md) · [SEO skills](../design-growth/README.md)

The repository includes a **dependency-free Python 3** script to inspect local static HTML without using hosted runners or sending pages to a third party.

```sh
python3 scripts/audit_static_html.py path/to/exported/site
python3 scripts/audit_static_html.py path/to/index.html --json
python3 -m unittest discover -s scripts -p 'test_audit_static_html.py'
```

The command exits nonzero when it finds missing title, language, description, canonical, Open Graph fields, image alt attributes, multiple/missing H1, or invalid JSON-LD. The checks are **heuristics**: canonical and social image URL correctness, structured data semantic validity, robots directives, real browser rendering, accessibility and search indexing require additional review. It reads existing HTML, not JSX/TSX source or a running Next.js server. For JS-rendered apps, audit an actual server-rendered/exported HTML response.

No GitHub Actions are configured. Run locally before review; do not imply that the audit certifies SEO or accessibility.
