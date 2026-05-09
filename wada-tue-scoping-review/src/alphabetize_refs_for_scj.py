#!/usr/bin/env python3
"""
Alphabetize references per SCJ Author Guidelines and renumber all in-text citations.

SCJ requires: "All references should be alphabetized by the last name of the lead author.
Numbers should then be assigned to each reference. Parenthetical numbers in the text
[(1); (4, 5); (1-3, 5, 6, 10)] should correspond to the numbered alphabetized reference list."
"""
import re
import sys
import os

SRC = os.path.dirname(os.path.abspath(__file__))

# ===== Read content files =====
en_path = os.path.join(SRC, 'scj_en_content.py')
jp_path = os.path.join(SRC, 'scj_jp_content.py')

with open(en_path, 'r') as f:
    en_text = f.read()

with open(jp_path, 'r') as f:
    jp_text = f.read()

# ===== Parse REFS block from EN =====
refs_match = re.search(r'REFS = \[\n(.*?)\n\]', en_text, re.DOTALL)
assert refs_match, "Could not find REFS block"

refs_block = refs_match.group(1)
# Parse individual reference strings
ref_entries = re.findall(r"'(\d+)\.\s+(.+?)'(?:,|\s*$)", refs_block, re.DOTALL)

# Build dict: old_number -> full ref text (without number prefix)
old_refs = {}
for num_str, content in ref_entries:
    # Clean up whitespace from multi-line strings
    content = re.sub(r'\s+', ' ', content.strip())
    old_refs[int(num_str)] = content

print(f"Parsed {len(old_refs)} references")

# ===== Sort alphabetically by first author =====
def sort_key(item):
    """Extract first author's last name for sorting."""
    num, text = item
    # Skip leading org names that start with common patterns
    # The text starts right after the number+period
    # For orgs like "World Anti-Doping Agency", "American Diabetes Association", etc.
    # we use the full name as-is for alphabetization
    first_word = text.split('.')[0].split(',')[0].strip()
    return first_word.lower()

sorted_refs = sorted(old_refs.items(), key=sort_key)

# Build old-to-new mapping
old_to_new = {}
for new_num, (old_num, _) in enumerate(sorted_refs, 1):
    old_to_new[old_num] = new_num

# Show mapping
print("\n=== Alphabetical Reordering ===")
for new_num, (old_num, text) in enumerate(sorted_refs, 1):
    short = text[:80] + '...' if len(text) > 80 else text
    print(f"  [{old_num}] -> [{new_num}] {short}")

# ===== Build new REFS block =====
new_ref_lines = []
for new_num, (_, text) in enumerate(sorted_refs, 1):
    new_ref_lines.append(f"    '{new_num}. {text}',")

new_refs_block = 'REFS = [\n' + '\n'.join(new_ref_lines) + '\n]'

# ===== Citation replacement function =====
valid_old = set(old_refs.keys())

def replace_citations(text, mapping, valid):
    """Replace citation numbers in parenthetical references."""
    def repl(m):
        open_p = m.group(1)
        nums_str = m.group(2)
        close_p = m.group(3)
        nums = [int(x.strip()) for x in nums_str.split(',')]
        if all(n in valid for n in nums):
            new_nums = sorted(mapping[n] for n in nums)
            return open_p + ', '.join(str(n) for n in new_nums) + close_p
        return m.group(0)
    return re.sub(r'([（(])(\d+(?:,\s*\d+)*)([）)])', repl, text)

# ===== Apply to EN file =====
# Split into pre-REFS and post-REFS
en_pre = en_text[:refs_match.start()]
en_post = en_text[refs_match.end():]

# Replace citations in pre-REFS text
en_pre = replace_citations(en_pre, old_to_new, valid_old)

# Reassemble
new_en = en_pre + new_refs_block + en_post

with open(en_path, 'w') as f:
    f.write(new_en)
print(f"\nUpdated: {en_path}")

# ===== Apply to JP file =====
jp_text = replace_citations(jp_text, old_to_new, valid_old)

with open(jp_path, 'w') as f:
    f.write(jp_text)
print(f"Updated: {jp_path}")

# ===== Verification =====
print("\n=== Verification ===")
# Re-read and check all citation numbers are valid
with open(en_path, 'r') as f:
    check_text = f.read()

# Find all citations
all_cites = re.findall(r'[（(](\d+(?:,\s*\d+)*)[）)]', check_text)
max_new = len(sorted_refs)
for cite in all_cites:
    nums = [int(x.strip()) for x in cite.split(',')]
    for n in nums:
        if n < 1 or n > max_new:
            print(f"  WARNING: Citation ({n}) out of range 1-{max_new}")

print(f"Total references: {max_new}")
print("Done.")
