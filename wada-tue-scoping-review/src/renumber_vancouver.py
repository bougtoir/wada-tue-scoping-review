#!/usr/bin/env python3
"""Renumber references in scj_en_content.py and build_scj_response.py to Vancouver order."""
import ast
import os
import re
import sys

CITATION_RE = re.compile(r"\(\s*\d{1,3}(?:\s*(?:,|-|–|—)\s*\d{1,3})*\s*\)")
NUM_RE = re.compile(r"\d{1,3}")

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


def collect_text(obj):
    """Recursively collect string text from content variables."""
    if isinstance(obj, str):
        return obj + "\n\n"
    if isinstance(obj, (list, tuple)):
        return "".join(collect_text(x) for x in obj)
    if isinstance(obj, dict):
        return "".join(collect_text(v) for v in obj.values())
    return ""


def get_citation_numbers(text):
    """Return old reference numbers in order of appearance in text."""
    numbers = []
    for m in CITATION_RE.finditer(text):
        for n in NUM_RE.finditer(m.group(0)):
            numbers.append(int(n.group(0)))
    return numbers


def replace_citations(text, mapping):
    """Replace citation groups using mapping, sorting new numbers within each group."""

    def repl(match):
        group = match.group(0)
        nums = [int(n) for n in NUM_RE.findall(group)]
        new_nums = sorted({mapping[n] for n in nums})
        return "(" + ", ".join(str(n) for n in new_nums) + ")"

    return CITATION_RE.sub(repl, text)


def build_mapping_from_module(module_globals):
    """Build old->new mapping by scanning variables in manuscript order."""
    order = [
        "ABSTRACT",
        "INTRO",
        "METHODS",
        "RESULTS_SOURCE",
        "RESULTS_CONTEXT",
        "RESULTS_OVERVIEW",
        "DISEASE_RESULTS",
        "CROSS_CUTTING",
        "CROSS_CUTTING_2",
        "DISCUSSION",
        "RECS_INTRO",
        "RECS",
        "PRACTICAL_INTRO",
        "PRACTICAL_ITEMS",
        "FIGURE_LEGENDS",
    ]
    full_text = "".join(
        collect_text(module_globals.get(name)) for name in order if name in module_globals
    )
    mapping = {}
    next_num = 1
    for old in get_citation_numbers(full_text):
        if old not in mapping:
            mapping[old] = next_num
            next_num += 1
    return mapping


def renumber_content_file(path, mapping):
    """Parse a Python content file, replace citations, reorder REFS, and write back."""
    with open(path, "r", encoding="utf-8") as f:
        source = f.read()
    tree = ast.parse(source)

    # Find REFS list node ids to avoid processing reference strings
    refs_node_ids = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == "REFS":
                    if isinstance(node.value, ast.List):
                        for elt in node.value.elts:
                            refs_node_ids.add(id(elt))

    class CitationTransformer(ast.NodeTransformer):
        def visit_Constant(self, node):
            if isinstance(node.value, str) and id(node) not in refs_node_ids:
                new_val = replace_citations(node.value, mapping)
                if new_val != node.value:
                    return ast.Constant(value=new_val)
            return node

    new_tree = CitationTransformer().visit(tree)
    ast.fix_missing_locations(new_tree)

    # Reorder REFS list by new number and update leading numbers
    for node in ast.walk(new_tree):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == "REFS":
                    if isinstance(node.value, ast.List):
                        elts = node.value.elts[:]
                        old_to_str = {}
                        for elt in elts:
                            if isinstance(elt, ast.Constant) and isinstance(elt.value, str):
                                m = re.match(r"(\d+)\.\s", elt.value)
                                if m:
                                    old_to_str[int(m.group(1))] = elt.value
                        ordered = []
                        for old, new in sorted(mapping.items(), key=lambda kv: kv[1]):
                            if old in old_to_str:
                                s = old_to_str[old]
                                s2 = re.sub(r"^\d+\.\s", f"{new}. ", s, count=1)
                                ordered.append(ast.Constant(value=s2))
                        # Append any refs not cited (orphan) at the end, renumbered
                        mapped_old = set(mapping.keys())
                        next_extra = max(mapping.values()) + 1 if mapping else 1
                        for old in sorted(old_to_str.keys()):
                            if old not in mapped_old:
                                s = old_to_str[old]
                                s2 = re.sub(r"^\d+\.\s", f"{next_extra}. ", s, count=1)
                                ordered.append(ast.Constant(value=s2))
                                next_extra += 1
                        node.value.elts = ordered

    new_source = ast.unparse(new_tree)
    if not new_source.startswith("#!"):
        new_source = "#!/usr/bin/env python3\n" + new_source
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_source)


def renumber_response_file(path, mapping):
    """Replace citations in response source with regex and fix wording."""
    with open(path, "r", encoding="utf-8") as f:
        source = f.read()
    source = replace_citations(source, mapping)
    source = source.replace(
        "All references have been re-verified, renumbered, and alphabetized by lead author per SCJ guidelines.",
        "All references have been re-verified and renumbered in order of appearance (Vancouver style).",
    )
    source = re.sub(r"(?<!')WADAs(?![a-zA-Z])", r"WADA\\'s", source)
    with open(path, "w", encoding="utf-8") as f:
        f.write(source)


def main():
    content_path = os.path.join(SCRIPT_DIR, "scj_en_content.py")
    # Load module to build mapping in manuscript order
    module_globals = {}
    with open(content_path, "r", encoding="utf-8") as f:
        exec(compile(f.read(), content_path, "exec"), module_globals)

    mapping = build_mapping_from_module(module_globals)
    print(f"Built Vancouver mapping with {len(mapping)} references")

    renumber_content_file(content_path, mapping)
    print(f"Renumbered {content_path}")

    response_path = os.path.join(SCRIPT_DIR, "build_scj_response.py")
    renumber_response_file(response_path, mapping)
    print(f"Updated {response_path}")


if __name__ == "__main__":
    main()
