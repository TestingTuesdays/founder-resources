#!/usr/bin/env python3
"""Validate perks catalog: evidence, uniqueness, official links, editorial fields."""
import csv
import sys
from pathlib import Path
from urllib.parse import urlsplit
from datetime import date
path=Path(__file__).resolve().parents[1]/"perks/catalog.csv"
required={"program","category","geography","benefit","application_route","verification_status","official_url","caveats","reviewed_date"}
statuses={"Official terms reviewed","Program discovery — recheck","Lead — offer not verified","Official program discovery","Discovery only"}
problems=[]
with path.open(newline="",encoding="utf-8") as file:
    reader=csv.DictReader(file)
    if not required.issubset(reader.fieldnames or []):
        sys.exit("Catalog missing required columns")
    rows=list(reader)
names=set()
for i,r in enumerate(rows,2):
    name=r["program"].strip().casefold()
    if not name or name in names: problems.append(f"row {i}: duplicate/blank program")
    names.add(name)
    if any(not r[k].strip() for k in required): problems.append(f"row {i}: empty required field")
    if r["verification_status"] not in statuses: problems.append(f"row {i}: invalid evidence status")
    u=urlsplit(r["official_url"])
    if u.scheme!="https" or not u.netloc: problems.append(f"row {i}: expected HTTPS official URL")
    try: date.fromisoformat(r["reviewed_date"])
    except ValueError: problems.append(f"row {i}: date must be YYYY-MM-DD")
if len(rows)<20: problems.append("Catalog unexpectedly small")
print(f"Validated {len(rows)} startup programs and leads.")
if problems:
    print("\n".join(problems))
    sys.exit(1)
