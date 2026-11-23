#!/usr/bin/env python3
"""Check local Markdown links in this repository. External URLs are not fetched."""
from pathlib import Path
from urllib.parse import unquote, urlsplit
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r'(?<!!)\[[^\]]*\]\(([^)]+)\)')
problems = []
checked = 0
for doc in sorted(ROOT.rglob("*.md")):
    if ".git" in doc.parts:
        continue
    text = doc.read_text(encoding="utf-8")
    for line, raw in enumerate(text.splitlines(), 1):
        for dest in LINK.findall(raw):
            url = dest.strip().split(" ", 1)[0].strip("<>")
            if url.startswith(("#", "mailto:", "tel:", "data:")):
                continue
            parsed = urlsplit(url)
            if parsed.scheme or parsed.netloc:
                continue
            target = (doc.parent / unquote(parsed.path)).resolve()
            checked += 1
            if not target.is_relative_to(ROOT) or not target.exists():
                problems.append(f"{doc.relative_to(ROOT)}:{line}: {url}")
print(f"Checked {checked} local Markdown links across {len(list(ROOT.rglob('*.md')))} documents.")
if problems:
    print("Broken local links:\n" + "\n".join(problems))
    sys.exit(1)
print("All checked local links resolve.")
