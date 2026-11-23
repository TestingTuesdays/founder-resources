#!/usr/bin/env python3
"""Local standard-library regression tests for the static HTML metadata auditor."""
import tempfile
import unittest
from pathlib import Path
from audit_static_html import audit

GOOD = """<!doctype html><html lang="en"><head>
<title>Example founder app</title>
<meta name="description" content="Useful and accurate product description">
<meta property="og:title" content="Example founder app">
<meta property="og:description" content="Useful and accurate product description">
<meta property="og:image" content="https://example.org/og.png">
<link rel="canonical" href="https://example.org/">
<script type="application/ld+json">{"@context":"https://schema.org","@type":"Organization","name":"Example"}</script>
</head><body><h1>Example founder app</h1><img alt="" src="decorative.png"></body></html>"""

class AuditTests(unittest.TestCase):
    def check(self, html):
        with tempfile.TemporaryDirectory() as folder:
            p = Path(folder) / "index.html"
            p.write_text(html, encoding="utf-8")
            return audit(p)
    def test_good_page(self):
        self.assertEqual(self.check(GOOD)["findings"], [])
    def test_missing_metadata(self):
        codes = {x["code"] for x in self.check("<html><body><h2>Hi</h2><img src='a.png'></body></html>")["findings"]}
        self.assertTrue({"TITLE_MISSING", "H1_COUNT", "LANG_MISSING", "IMG_ALT_MISSING"}.issubset(codes))
    def test_invalid_jsonld(self):
        broken = GOOD.replace('{"@context":"https://schema.org","@type":"Organization","name":"Example"}', '{not valid}')
        self.assertIn("JSONLD_INVALID", {x["code"] for x in self.check(broken)["findings"]})
    def test_duplicate_h1(self):
        self.assertIn("H1_COUNT", {x["code"] for x in self.check(GOOD.replace("</body>", "<h1>Again</h1></body>"))["findings"]})

if __name__ == "__main__":
    unittest.main()
