#!/usr/bin/env python3
"""Convert Carpentries Workbench fenced-div callouts to Just the Docs HTML."""

import re
import sys
from pathlib import Path

CALLOUT_MAP = {
    "objectives":  ("objectives",  "Learning Objectives"),
    "questions":   ("questions",   "Questions"),
    "keypoints":   ("keypoints",   "Key Points"),
    "challenge":   ("challenge",   "Challenge"),
    "solution":    ("solution",    "Solution"),
    "callout":     ("callout",     "Note"),
    "prereq":      ("prereq",      "Prerequisites"),
    "discussion":  ("discussion",  "Discussion"),
    "checklist":   ("checklist",   "Checklist"),
    "testimonial": ("testimonial", "Testimonial"),
    "warning":     ("warning",     "Warning"),
}


def convert(text: str) -> str:
    # Carpentries fenced divs: lines of ≥3 colons optionally followed by a class name
    open_re  = re.compile(r'^:{3,}\s*(\w+)\s*$', re.MULTILINE)
    close_re = re.compile(r'^:{3,}\s*$',          re.MULTILINE)

    lines = text.splitlines(keepends=True)
    out   = []
    i     = 0

    while i < len(lines):
        line = lines[i].rstrip('\n')
        m = re.match(r'^:{3,}\s*(\w+)\s*$', line)
        if m:
            kind = m.group(1).lower()
            css_class, label = CALLOUT_MAP.get(kind, (kind, kind.capitalize()))
            # Collect body until matching close fence
            body_lines = []
            i += 1
            while i < len(lines):
                inner = lines[i].rstrip('\n')
                if re.match(r'^:{3,}\s*$', inner):
                    i += 1
                    break
                body_lines.append(lines[i])
                i += 1

            body = "".join(body_lines)

            if css_class == "solution":
                # Render solutions as a collapsible <details>
                out.append(f'<details markdown="1">\n<summary>{label}</summary>\n\n')
                out.append(body)
                out.append("</details>\n\n")
            else:
                out.append(f'<div class="carpentries-{css_class}" markdown="1">\n')
                out.append(f'**{label}**\n\n')
                out.append(body)
                out.append("</div>\n\n")
        else:
            out.append(lines[i])
            i += 1

    return "".join(out)


def convert_file(src: Path, dst: Path):
    text    = src.read_text(encoding="utf-8")
    # Strip Carpentries-specific front matter fields that Just the Docs ignores
    text    = re.sub(r'^(teaching|exercises|editor_options|source|bibliography):[^\n]*\n',
                     '', text, flags=re.MULTILINE)
    result  = convert(text)
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(result, encoding="utf-8")
    print(f"  {src} → {dst}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: convert_carpentries.py <src_file_or_dir> <dst_file_or_dir>")
        sys.exit(1)
    src = Path(sys.argv[1])
    dst = Path(sys.argv[2])
    if src.is_dir():
        for md in sorted(src.glob("*.md")):
            convert_file(md, dst / md.name)
        for rmd in sorted(src.glob("*.Rmd")):
            convert_file(rmd, dst / (rmd.stem + ".md"))
    else:
        convert_file(src, dst)
