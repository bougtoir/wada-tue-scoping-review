#!/usr/bin/env python3
"""Renumber SCJ citations in order of first appearance, update content files, rebuild docx."""
import re
import sys

sys.path.insert(0, '/home/ubuntu')

# ===== STEP 1: Determine citation order from English content =====
from scj_en_content import (
    ABSTRACT, INTRO, METHODS, RESULTS_SOURCE, RESULTS_OVERVIEW,
    DISEASE_RESULTS, CROSS_CUTTING, CROSS_CUTTING_2, DISCUSSION,
    PRACTICAL_INTRO, PRACTICAL_ITEMS, RECS_INTRO, RECS, CONCLUSION, REFS
)

# Collect all text in document order (matches build_scj_en.py section order)
all_text = []
all_text.append(ABSTRACT)
for p in INTRO:
    all_text.append(p)
for k in METHODS:
    for p in METHODS[k]:
        all_text.append(p)
all_text.append(RESULTS_SOURCE)
all_text.append(RESULTS_OVERVIEW)
for k in DISEASE_RESULTS:
    for p in DISEASE_RESULTS[k]:
        all_text.append(p)
all_text.append(CROSS_CUTTING)
all_text.append(CROSS_CUTTING_2)
for p in DISCUSSION:
    all_text.append(p)
all_text.append(PRACTICAL_INTRO)
for b, r in PRACTICAL_ITEMS:
    all_text.append(b + r)
all_text.append(RECS_INTRO)
for r in RECS:
    all_text.append(r)
for p in CONCLUSION:
    all_text.append(p)

# Find all citation numbers in order of first appearance
# Pattern matches (N) or (N, M, ...) where N,M are integers
valid = set(range(1, len(REFS) + 1))  # valid ref numbers: 1..48
seen = set()
order = []

for t in all_text:
    for m in re.finditer(r'\((\d+(?:,\s*\d+)*)\)', t):
        nums = [int(x.strip()) for x in m.group(1).split(',')]
        # Only treat as citation if ALL numbers are valid ref numbers (1-48)
        if all(n in valid for n in nums):
            for n in nums:
                if n not in seen:
                    seen.add(n)
                    order.append(n)

# Build mapping: old_number -> new_number
mapping = {old: new for new, old in enumerate(order, 1)}

print(f"=== Citation Renumbering ===")
print(f"Cited references: {len(order)} out of {len(REFS)} total")
print(f"\nOld -> New mapping:")
for old in order:
    print(f"  [{old}] -> [{mapping[old]}]")

# ===== STEP 2: Replacement function =====
def replace_cites(text, mapping, valid):
    """Replace citation numbers in both half-width () and full-width （） parenthetical references."""
    def repl(m):
        open_paren = m.group(1)
        nums_str = m.group(2)
        close_paren = m.group(3)
        nums = [int(x.strip()) for x in nums_str.split(',')]
        if all(n in valid for n in nums):
            new_nums = sorted(mapping[n] for n in nums)
            return open_paren + ', '.join(str(n) for n in new_nums) + close_paren
        return m.group(0)
    return re.sub(r'([（(])(\d+(?:,\s*\d+)*)([）)])', repl, text)

# ===== STEP 3: Update scj_en_content.py =====
with open('/home/ubuntu/scj_en_content.py', 'r') as f:
    en_lines = f.readlines()

# Locate REFS block
refs_start = None
refs_end = None
for i, line in enumerate(en_lines):
    if refs_start is None and line.strip().startswith('REFS = ['):
        refs_start = i
    elif refs_start is not None and refs_end is None and line.strip() == ']':
        refs_end = i
        break

assert refs_start is not None and refs_end is not None, "Could not find REFS block"
print(f"\nREFS block in scj_en_content.py: line {refs_start+1} to {refs_end+1}")

# Parse individual ref lines to dict
ref_lines_by_num = {}
for i in range(refs_start + 1, refs_end):
    line = en_lines[i]
    m = re.match(r"(\s*')(\d+)\.\s", line)
    if m:
        num = int(m.group(2))
        ref_lines_by_num[num] = line

print(f"Parsed {len(ref_lines_by_num)} reference entries")

# Build new REFS lines in citation-order, renumbered
new_ref_lines = []
for new_num, old_num in enumerate(order, 1):
    old_line = ref_lines_by_num[old_num]
    # Replace only the leading reference number
    new_line = re.sub(r"^(\s*')(\d+)\.", lambda m: m.group(1) + str(new_num) + '.', old_line)
    new_ref_lines.append(new_line)

# Replace citations in text part (everything before REFS block)
text_before = ''.join(en_lines[:refs_start])
text_before = replace_cites(text_before, mapping, valid)

# Everything after the closing ] of REFS
text_after = ''.join(en_lines[refs_end + 1:])

# Assemble new file
new_en = text_before + 'REFS = [\n' + ''.join(new_ref_lines) + ']\n' + text_after

with open('/home/ubuntu/scj_en_content.py', 'w') as f:
    f.write(new_en)
print("Updated: scj_en_content.py")

# ===== STEP 4: Update scj_jp_content.py =====
with open('/home/ubuntu/scj_jp_content.py', 'r') as f:
    jp_text = f.read()

jp_text = replace_cites(jp_text, mapping, valid)

with open('/home/ubuntu/scj_jp_content.py', 'w', encoding='utf-8') as f:
    f.write(jp_text)
print("Updated: scj_jp_content.py")

# ===== STEP 5: Verify the changes =====
print("\n=== Verification ===")

# Re-import to check
# Need to clear cached modules
for mod_name in list(sys.modules.keys()):
    if 'scj_' in mod_name:
        del sys.modules[mod_name]

from scj_en_content import REFS as NEW_REFS

print(f"New REFS count: {len(NEW_REFS)} (was {len(REFS)})")
print("\nFirst 5 new references:")
for r in NEW_REFS[:5]:
    print(f"  {r[:100]}...")

# Verify all citations in text are within new valid range
new_valid = set(range(1, len(NEW_REFS) + 1))

# Re-import fresh content
from scj_en_content import (
    ABSTRACT as A2, INTRO as I2, METHODS as M2, 
    RESULTS_SOURCE as RS2, RESULTS_OVERVIEW as RO2,
    DISEASE_RESULTS as DR2, CROSS_CUTTING as CC2, 
    CROSS_CUTTING_2 as CC22, DISCUSSION as D2,
    PRACTICAL_INTRO as PI2, PRACTICAL_ITEMS as PIT2,
    RECS_INTRO as RI2, RECS as R2, CONCLUSION as CO2
)

all_new_text = []
all_new_text.append(A2)
for p in I2: all_new_text.append(p)
for k in M2:
    for p in M2[k]: all_new_text.append(p)
all_new_text.append(RS2)
all_new_text.append(RO2)
for k in DR2:
    for p in DR2[k]: all_new_text.append(p)
all_new_text.append(CC2)
all_new_text.append(CC22)
for p in D2: all_new_text.append(p)
all_new_text.append(PI2)
for b, r in PIT2: all_new_text.append(b + r)
all_new_text.append(RI2)
for r in R2: all_new_text.append(r)
for p in CO2: all_new_text.append(p)

all_cited_new = set()
for t in all_new_text:
    for m in re.finditer(r'\((\d+(?:,\s*\d+)*)\)', t):
        nums = [int(x.strip()) for x in m.group(1).split(',')]
        if all(1 <= n <= 100 for n in nums):
            for n in nums:
                all_cited_new.add(n)

print(f"\nCited numbers in updated text: {sorted(all_cited_new)}")
expected = set(range(1, len(order) + 1))
if all_cited_new == expected:
    print("PASS: All citations are sequential 1..N")
else:
    missing = expected - all_cited_new
    extra = all_cited_new - expected
    if missing:
        print(f"Missing: {sorted(missing)}")
    if extra:
        print(f"Extra: {sorted(extra)}")

print("\nRenumbering complete.")
