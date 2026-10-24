#!/usr/bin/env python3
"""Tiny brand-leak checker: ensures no foreign brand names slipped into the page.

Usage: python3 scripts/style_audit.py
Exit 0 = clean, 1 = leak found.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BANNED = [
    "hiddify", "hiddifi", "v2ray", "v2box", "nakoray", "nekoray",
    "gameblack", "marzban", "x-ui", "xui", "sanai", "sanaei",
    "bento",
]

TEXT_FILES = ["index.html", "README.md", "data/config.json", "docs/screenshot-placeholder.md"]
ALLOW_IN = {"README.md"}  # credits may mention inspirations


def main() -> int:
    leaks = []
    for rel in TEXT_FILES:
        p = ROOT / rel
        if not p.exists():
            continue
        text = p.read_text(encoding="utf-8", errors="replace")
        for word in BANNED:
            # allowlist: app-grid links & URL schemes legitimately contain client names
            if rel in ("index.html", "data/config.json") and word in ("hiddify", "v2ray", "v2box", "nekoray", "nakoray"):
                continue
            for m in re.finditer(re.escape(word), text, re.IGNORECASE):
                line = text.count("\n", 0, m.start()) + 1
                leaks.append(f"{rel}:{line}: {word}")
    # credits exception: README may name the bento-style inspiration once
    leaks = [lk for lk in leaks if not (lk.startswith("README.md") and "bento" in lk)]
    if leaks:
        print("BRAND LEAKS FOUND:")
        for lk in leaks:
            print(" -", lk)
        return 1
    print("style_audit: clean ✔ (StarForge PRO only)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
