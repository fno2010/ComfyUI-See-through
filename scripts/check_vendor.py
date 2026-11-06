#!/usr/bin/env python3
"""Fail if the vendored See-through tree reintroduces generic import names."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VENDOR = ROOT / "see-through"
BAD_IMPORT = re.compile(
    r"^[ \t]*(?:from|import)[ \t]+(?:modules|utils|annotators)(?:\.|\s|$)",
    re.MULTILINE,
)
REQUIRED = (
    VENDOR / "seethrough_modules" / "__init__.py",
    VENDOR / "seethrough_utils" / "__init__.py",
    VENDOR / "seethrough_annotators" / "__init__.py",
)

errors: list[str] = []
for path in sorted(VENDOR.rglob("*.py")):
    if BAD_IMPORT.search(path.read_text(encoding="utf-8", errors="replace")):
        errors.append(f"legacy import in {path.relative_to(ROOT)}")
for path in REQUIRED:
    if not path.is_file():
        errors.append(f"missing package marker: {path.relative_to(ROOT)}")
if not (ROOT / "UPSTREAM.md").is_file():
    errors.append("missing UPSTREAM.md")

if errors:
    print("vendor check failed:", file=sys.stderr)
    print("\n".join(f"  - {e}" for e in errors), file=sys.stderr)
    raise SystemExit(1)
print("vendor namespace check: ok")
