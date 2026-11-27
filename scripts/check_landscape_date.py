#!/usr/bin/env python3
"""Fail if docs/landscape.md was last searched too long ago (issue 67).

The landscape page must be re-searched before each release (docs/sourcing.md,
rule 6). This reads the page's `**Last searched: YYYY-MM-DD.**` line and exits
non-zero when the line is missing or the date is more than MAX_AGE_DAYS before
the reference date (today, or --today for tests).
"""
import argparse
import datetime as dt
import re
import sys

MAX_AGE_DAYS = 30
PATTERN = re.compile(r"^\*\*Last searched: (\d{4}-\d{2}-\d{2})\.\*\*", re.MULTILINE)
FIX = ("Re-run the landscape search, update docs/landscape.md, and set its "
       "'**Last searched: YYYY-MM-DD.**' line to the date of the search.")


def check(text: str, today: dt.date, max_age: int = MAX_AGE_DAYS) -> tuple[bool, str]:
    m = PATTERN.search(text)
    if not m:
        return False, f"docs/landscape.md has no '**Last searched: YYYY-MM-DD.**' line. {FIX}"
    try:
        searched = dt.date.fromisoformat(m.group(1))
    except ValueError:
        return False, f"docs/landscape.md has an invalid date '{m.group(1)}'. {FIX}"
    age = (today - searched).days
    if age < 0:
        return False, f"docs/landscape.md says it was searched on {searched}, after {today}. {FIX}"
    if age > max_age:
        return False, (f"docs/landscape.md was last searched on {searched}, {age} days before "
                       f"{today} (limit {max_age}). {FIX}")
    return True, f"docs/landscape.md last searched {searched} ({age} days ago, limit {max_age})."


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--file", default="docs/landscape.md")
    p.add_argument("--today", type=dt.date.fromisoformat, default=dt.date.today())
    p.add_argument("--max-age-days", type=int, default=MAX_AGE_DAYS)
    a = p.parse_args(argv)
    try:
        with open(a.file, encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        print(f"::error::{a.file} not found. {FIX}")
        return 1
    ok, msg = check(text, a.today, a.max_age_days)
    print(msg if ok else f"::error::{msg}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
