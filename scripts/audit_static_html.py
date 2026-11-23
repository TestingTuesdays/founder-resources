#!/usr/bin/env python3
"""Local, dependency-free SEO and metadata audit of HTML files; no network requests."""
import argparse
import json
from html.parser import HTMLParser
from pathlib import Path

class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.title = []
        self.in_title = False
        self.headings = []
        self.meta = {}
        self.links = []
        self.images = []
        self.lang = None
        self.jsonld = []
        self.in_jsonld = False
        self.jsonld_buffer = []
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "html":
            self.lang = a.get("lang")
        if tag == "title":
            self.in_title = True
        if tag in ("h1", "h2", "h3"):
            self.headings.append(tag)
        if tag == "meta":
            key = a.get("name") or a.get("property")
            if key:
                self.meta.setdefault(key.lower(), []).append(a.get("content", ""))
        if tag == "link":
            self.links.append(a)
        if tag == "img":
            self.images.append(a)
        if tag == "script" and a.get("type") == "application/ld+json":
            self.in_jsonld = True
            self.jsonld_buffer = []
    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False
        if tag == "script" and self.in_jsonld:
            self.in_jsonld = False
            self.jsonld.append("".join(self.jsonld_buffer))
    def handle_data(self, data):
        if self.in_title:
            self.title.append(data)
        if self.in_jsonld:
            self.jsonld_buffer.append(data)

def audit(path):
    p = Page()
    p.feed(path.read_text(encoding="utf-8"))
    findings = []
    def check(ok, code, message):
        if not ok:
            findings.append({"code": code, "message": message})
    title = "".join(p.title).strip()
    check(bool(title), "TITLE_MISSING", "Add a descriptive HTML title")
    check(bool(p.lang), "LANG_MISSING", "Set html lang to actual page language")
    check(p.headings.count("h1") == 1, "H1_COUNT", "Use one descriptive primary H1")
    check(bool(p.meta.get("description", [""])[0].strip()), "DESCRIPTION_MISSING", "Add unique useful meta description")
    check(any("canonical" in x.get("rel", "").lower().split() and x.get("href") for x in p.links), "CANONICAL_MISSING", "Review canonical URL")
    check(bool(p.meta.get("og:title", [""])[0].strip()), "OG_TITLE_MISSING", "Add matching Open Graph title")
    check(bool(p.meta.get("og:description", [""])[0].strip()), "OG_DESCRIPTION_MISSING", "Add Open Graph description")
    check(bool(p.meta.get("og:image", [""])[0].strip()), "OG_IMAGE_MISSING", "Add absolute share image URL")
    check(all("alt" in image for image in p.images), "IMG_ALT_MISSING", "Add appropriate alt attribute; decorative images may use empty alt")
    for i, payload in enumerate(p.jsonld, 1):
        try:
            json.loads(payload)
        except json.JSONDecodeError:
            findings.append({"code": "JSONLD_INVALID", "message": f"JSON-LD block {i} is invalid JSON"})
    return {"file": str(path), "title": title, "h1_count": p.headings.count("h1"), "images": len(p.images), "jsonld_blocks": len(p.jsonld), "findings": findings}

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("path", type=Path, help="HTML file or directory")
    ap.add_argument("--json", action="store_true", help="Machine-readable output")
    args = ap.parse_args()
    files = sorted(args.path.rglob("*.html")) if args.path.is_dir() else [args.path]
    if not files or not all(p.is_file() for p in files):
        ap.error("No readable HTML files found")
    results = [audit(p) for p in files]
    if args.json:
        print(json.dumps(results, indent=2))
    else:
        for result in results:
            print(f"{result['file']}: {len(result['findings'])} findings")
            for issue in result["findings"]:
                print(f"  {issue['code']}: {issue['message']}")
    return 1 if any(r["findings"] for r in results) else 0

if __name__ == "__main__":
    raise SystemExit(main())
