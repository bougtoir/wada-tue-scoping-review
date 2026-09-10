#!/usr/bin/env python3
"""Build the R2 marked main-body .docx.

Compares the R1-submitted main body (base) against the R2-revised file
paragraph by paragraph and renders word-level differences: deletions in
blue strikethrough, insertions in red, unchanged text in black. All other
paragraph formatting (indent, alignment, citation superscripts) is taken
from the R2 file.
"""
import difflib
import os
import re
import subprocess
import sys
import tempfile

from docx import Document
from docx.shared import Pt, RGBColor
from docx.oxml.ns import qn

BLUE = RGBColor(0x00, 0x00, 0xFF)
RED = RGBColor(0xFF, 0x00, 0x00)
BLACK = RGBColor(0x00, 0x00, 0x00)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# R1-submitted main body is the pre-edit version of the same file in git
# history (commit e59dc6c on the R1 submission branch).
R1_BASE_COMMIT = "e59dc6c8e108552028e43d4d294c67d36ae659ae"
R1_BASE_RELPATH = (
    "wada-tue-scoping-review/manuscripts/SCJ_Narrative_Review_mainbody.docx"
)


def _r1_base_path():
    """Materialize the R1-submitted mainbody docx from git history."""
    repo_root = os.path.dirname(BASE_DIR)
    blob = subprocess.run(
        ["git", "-C", repo_root, "show", f"{R1_BASE_COMMIT}:{R1_BASE_RELPATH}"],
        check=True, capture_output=True,
    ).stdout
    fd, path = tempfile.mkstemp(suffix=".docx")
    with os.fdopen(fd, "wb") as f:
        f.write(blob)
    return path
NEW_PATH = os.path.join(BASE_DIR, "manuscripts", "SCJ_Narrative_Review_mainbody.docx")
OUT_PATH = os.path.join(BASE_DIR, "manuscripts", "SCJ_Narrative_Review_mainbody_marked.docx")


def _tokenize(text):
    return re.findall(r"\S+\s*", text)


def _word_diff_runs(old_text, new_text):
    old_tokens = _tokenize(old_text)
    new_tokens = _tokenize(new_text)
    runs = []
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(
        None, old_tokens, new_tokens
    ).get_opcodes():
        if tag == "equal":
            runs.append(("".join(new_tokens[j1:j2]), BLACK, False))
        elif tag == "delete":
            runs.append(("".join(old_tokens[i1:i2]), BLUE, True))
        elif tag == "insert":
            runs.append(("".join(new_tokens[j1:j2]), RED, False))
        elif tag == "replace":
            runs.append(("".join(old_tokens[i1:i2]), BLUE, True))
            runs.append(("".join(new_tokens[j1:j2]), RED, False))
    return runs


def _styled_run(p, text, color, strike, size, bold):
    r = p.add_run(text)
    r.font.name = "Times New Roman"
    r.font.size = Pt(size)
    r.font.bold = bold
    r.font.color.rgb = color
    r.font.strike = strike
    rpr = r._element.get_or_add_rPr()
    rfonts = rpr.find(qn("w:rFonts"))
    if rfonts is None:
        rfonts = rpr.makeelement(qn("w:rFonts"), {})
        rpr.append(rfonts)
    rfonts.set(qn("w:ascii"), "Times New Roman")
    rfonts.set(qn("w:hAnsi"), "Times New Roman")
    rfonts.set(qn("w:eastAsia"), "Times New Roman")
    return r


def build_marked(base_path, new_path, out_path):
    base_doc = Document(base_path)
    new_doc = Document(new_path)
    base_texts = [p.text for p in base_doc.paragraphs]
    new_texts = [p.text for p in new_doc.paragraphs]
    if len(base_texts) != len(new_texts):
        raise SystemExit(
            f"paragraph count differs: base={len(base_texts)} new={len(new_texts)}"
        )

    changed = 0
    for i, (old_t, new_t) in enumerate(zip(base_texts, new_texts)):
        if old_t == new_t:
            continue
        changed += 1
        p = new_doc.paragraphs[i]
        bold = any(r.font.bold for r in p.runs)
        for r in list(p.runs):
            r._element.getparent().remove(r._element)
        for text, color, strike in _word_diff_runs(old_t, new_t):
            if text:
                _styled_run(p, text, color, strike, size=12, bold=bold)
    new_doc.save(out_path)
    print(f"marked: {changed} changed paragraphs -> {out_path}")


if __name__ == "__main__":
    base = sys.argv[1] if len(sys.argv) > 1 else _r1_base_path()
    build_marked(base, NEW_PATH, OUT_PATH)
