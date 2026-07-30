#!/usr/bin/env python3
"""Update scj_en_content.py REFS and citations to match the attached trackchange mainbody (alphabetical)."""
import json
import os
import re
import sys
import zipfile
from lxml import etree
import tokenize
import io

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

CITE_RE = re.compile(r'(\(\s*\d{1,2}(?:\s*[-–—]\s*\d{1,2})?(?:\s*,\s*\d{1,2}(?:\s*[-–—]\s*\d{1,2})?)*\s*\))')
NUM_RE = re.compile(r'\d+')

def ref_sort_key(text):
    s = text.strip()
    if s.lower().startswith('the '):
        s = s[4:]
    words = re.findall(r"[A-Za-z'\u00C0-\u024F]+", s)
    return ' '.join(words[:2]).lower()

def map_text(text, mapping):
    def repl(m):
        inner = m.group(0)[1:-1]
        parts = re.split(r'(\s*[-–—,]\s*)', inner)
        out = []
        for p in parts:
            n = p.strip()
            if NUM_RE.fullmatch(n):
                out.append(str(mapping.get(int(n), n)))
            else:
                out.append(p)
        return '(' + ''.join(out) + ')'
    return CITE_RE.sub(repl, text)

def extract_visible_paras(docx_path):
    NS = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
    DEL_TAGS = {f'{{{NS["w"]}}}del', f'{{{NS["w"]}}}moveFrom'}
    def is_deleted(elem):
        for anc in elem.iterancestors():
            if anc.tag in DEL_TAGS:
                return True
        return False
    def para_text(p):
        parts = []
        for t in p.iter():
            if t.tag == f'{{{NS["w"]}}}t' or t.tag == f'{{{NS["w"]}}}delText':
                if not is_deleted(t):
                    parts.append(t.text or '')
        return ''.join(parts)
    with zipfile.ZipFile(docx_path) as z:
        xml = z.read('word/document.xml')
    root = etree.fromstring(xml)
    body = root.find('.//w:body', NS)
    paras = []
    for p in body.findall('.//w:p', NS):
        t = para_text(p)
        if t.strip():
            paras.append(t)
    return paras

def main():
    docx_path = '/home/ubuntu/attachments/96ef9444-26fc-45be-88ba-89e6e64a0f42/SCJ_1st_mainbody_trackchange.docx'
    src_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'scj_en_content.py')
    out_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'manuscripts')
    os.makedirs(out_dir, exist_ok=True)

    paras = extract_visible_paras(docx_path)
    ref_start = None
    fig_idx = None
    for i, t in enumerate(paras):
        if t.strip() == 'REFERENCES':
            ref_start = i
        if t.strip() == 'FIGURE LEGENDS':
            fig_idx = i
            break

    entries = []
    for t in paras[ref_start+1:fig_idx]:
        m = re.match(r'(\d+)\.\s*(.*)', t.strip())
        if m:
            entries.append((int(m.group(1)), m.group(2)))
    sorted_entries = sorted(entries, key=lambda x: (ref_sort_key(x[1]), x[1].lower()))
    mapping = {old: i+1 for i, (old, _) in enumerate(sorted_entries)}
    new_refs = [f'    "{i+1}. {text}"' for i, (_, text) in enumerate(sorted_entries)]

    # Save mapping
    with open(os.path.join(out_dir, 'citation_mapping.json'), 'w') as f:
        json.dump({str(k): v for k, v in mapping.items()}, f, indent=2)

    # Update source
    with open(src_path, 'r', encoding='utf-8') as f:
        source = f.read()

    ref_match = re.search(r'(REFS\s*=\s*\[).*?(\n\])', source, re.DOTALL)
    if not ref_match:
        raise ValueError('REFS list not found in scj_en_content.py')
    new_ref_block = ref_match.group(1) + '\n' + ',\n'.join(new_refs) + ref_match.group(2)
    source = source[:ref_match.start()] + new_ref_block + source[ref_match.end():]

    # Remap citations in string literals, skipping the REFS list
    out_tokens = []
    in_refs = False
    bracket_depth = 0
    prev_name = None
    for tok in tokenize.generate_tokens(io.StringIO(source).readline):
        if tok.type == tokenize.NAME and tok.string == 'REFS':
            prev_name = 'REFS'
        elif tok.type == tokenize.OP and tok.string == '=' and prev_name == 'REFS':
            # next non-comment token should be '['
            pass
        elif tok.type == tokenize.OP and tok.string == '[' and prev_name == 'REFS':
            in_refs = True
            bracket_depth = 1
            prev_name = None
        elif in_refs and tok.type == tokenize.OP:
            if tok.string == '[':
                bracket_depth += 1
            elif tok.string == ']':
                bracket_depth -= 1
                if bracket_depth == 0:
                    in_refs = False

        if tok.type == tokenize.STRING and not in_refs:
            s = tok.string
            prefix = ''
            quote = s
            for i, ch in enumerate(s):
                if ch in '"\'':
                    prefix = s[:i]
                    quote = s[i:]
                    break
            if quote.startswith('"""') or quote.startswith("'''"):
                q = quote[:3]
                content = quote[3:-3]
            else:
                q = quote[0]
                content = quote[1:-1]
            new_content = map_text(content, mapping)
            out_tokens.append(prefix + q + new_content + q)
        else:
            out_tokens.append(tok.string)

    out_source = ''.join(out_tokens)
    with open(src_path, 'w', encoding='utf-8') as f:
        f.write(out_source)
    print('Updated', src_path)
    print('Mapping', mapping)

if __name__ == '__main__':
    main()
