#!/usr/bin/env python3
"""Update build_scj_response.py citation numbers to match current scj_en_content.py Vancouver numbering."""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import scj_en_content as content

CITATION_RE = re.compile(r'\(\s*\d{1,3}(?:\s*(?:,|-|–|—)\s*\d{1,3})*\s*\)')
NUM_RE = re.compile(r'\d{1,3}')


def scan(obj):
    if isinstance(obj, str):
        for m in CITATION_RE.finditer(obj):
            for n in NUM_RE.finditer(m.group(0)):
                yield int(n.group(0))
    elif isinstance(obj, (list, tuple)):
        for item in obj:
            yield from scan(item)
    elif isinstance(obj, dict):
        for v in obj.values():
            yield from scan(v)


def build_mapping():
    mapping = {}
    next_num = 1
    order = [
        'ABSTRACT', 'INTRO', 'METHODS', 'RESULTS_SOURCE', 'RESULTS_CONTEXT',
        'RESULTS_OVERVIEW', 'DISEASE_RESULTS', 'CROSS_CUTTING', 'CROSS_CUTTING_2',
        'DISCUSSION', 'RECS_INTRO', 'RECS', 'PRACTICAL_INTRO', 'PRACTICAL_ITEMS',
        'FIGURE_LEGENDS'
    ]
    for name in order:
        if not hasattr(content, name):
            continue
        val = getattr(content, name)
        for old in scan(val):
            if old not in mapping:
                mapping[old] = next_num
                next_num += 1
    return mapping


def replace_citations_in_text(text, mapping):
    def repl(match):
        group = match.group(0)
        nums = [int(n) for n in NUM_RE.findall(group)]
        new_nums = sorted({mapping[n] for n in nums})
        return '(' + ', '.join(str(n) for n in new_nums) + ')'
    return CITATION_RE.sub(repl, text)


def main():
    mapping = build_mapping()
    print(f'Loaded mapping with {len(mapping)} references')

    resp_path = os.path.join(os.path.dirname(__file__), 'build_scj_response.py')
    with open(resp_path, 'r', encoding='utf-8') as f:
        source = f.read()

    source = replace_citations_in_text(source, mapping)

    # Text cleanups
    source = source.replace(
        'All references have been re-verified, renumbered, and alphabetized by lead author per SCJ guidelines.',
        'All references have been re-verified and renumbered in order of appearance (Vancouver style).'
    )
    source = source.replace(
        'All references have been re-verified, renumbered, and numbered in order of appearance (Vancouver style).',
        'All references have been re-verified and renumbered in order of appearance (Vancouver style).'
    )
    # WADAs -> WADA's (not touching WADA's)
    source = re.sub(r"(?<!')WADAs(?![a-zA-Z])", r"WADA\\'s", source)

    with open(resp_path, 'w', encoding='utf-8') as f:
        f.write(source)
    print(f'Updated {resp_path}')


if __name__ == '__main__':
    main()
