#!/usr/bin/env python3
"""Build separate SCJ title page and main-body .docx files."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from create_scj_review_part1 import *
from scj_en_content import *


def build_title_page_docx(path):
    doc = Document()
    setup_styles(doc)

    # Nonblinded title page
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(TITLE)
    run.bold = True
    run.font.size = Pt(14)

    doc.add_paragraph()
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(AUTHOR_LINE)
    run.font.size = Pt(12)

    doc.add_paragraph()
    for aff in AFFILIATIONS:
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(aff)
        run.font.size = Pt(10)
        run.italic = True

    doc.add_paragraph()
    p = doc.add_paragraph()
    run = p.add_run("Current Position: ")
    run.bold = True
    run.font.size = Pt(10)
    run = p.add_run(CURRENT_POS)
    run.font.size = Pt(10)

    doc.add_paragraph()
    p = doc.add_paragraph()
    run = p.add_run("Corresponding Author: ")
    run.bold = True
    run.font.size = Pt(10)
    run = p.add_run(CORRESP)
    run.font.size = Pt(10)

    doc.add_page_break()

    # Blinded title page
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(TITLE)
    run.bold = True
    run.font.size = Pt(14)

    doc.add_paragraph()
    p = doc.add_paragraph()
    run = p.add_run("Running Head: ")
    run.bold = True
    run.font.size = Pt(10)
    run = p.add_run(RUNNING_HEAD)
    run.font.size = Pt(10)

    doc.add_paragraph()
    p = doc.add_paragraph()
    run = p.add_run("Keywords: ")
    run.bold = True
    run.font.size = Pt(10)
    run = p.add_run(KEYWORDS)
    run.font.size = Pt(10)

    doc.save(path)
    print(f"Saved title page: {path}")


def build_mainbody_docx(path):
    doc = Document()
    setup_styles(doc)

    # ABSTRACT
    add_heading_styled(doc, "ABSTRACT", 1)
    add_body_ni(doc, ABSTRACT)
    doc.add_page_break()

    # INTRODUCTION
    add_heading_styled(doc, "INTRODUCTION", 1)
    for para in INTRO:
        add_body(doc, para)

    # METHODS
    add_heading_styled(doc, "METHODS", 1)
    for sub_title, paras in METHODS.items():
        add_heading_styled(doc, sub_title, 2)
        for para in paras:
            add_body(doc, para)

    # RESULTS
    add_heading_styled(doc, "RESULTS", 1)

    add_heading_styled(doc, "Population and Epidemiological Context", 2)
    add_body(doc, RESULTS_CONTEXT)

    add_heading_styled(doc, "Overview of Clinical-Competition Gaps", 2)
    add_body(doc, RESULTS_OVERVIEW)

    for disease_title, paras in DISEASE_RESULTS.items():
        add_heading_styled(doc, disease_title, 2)
        for para in paras:
            add_body(doc, para)

    add_heading_styled(doc, "Cross-Cutting Analysis: Structural Drivers of Divergence", 2)
    add_body(doc, CROSS_CUTTING)
    add_body(doc, CROSS_CUTTING_2)

    # DISCUSSION
    add_heading_styled(doc, "DISCUSSION", 1)
    for para in DISCUSSION:
        add_body(doc, para)

    add_heading_styled(doc, "Recommendations for Harmonization", 2)
    add_body(doc, RECS_INTRO)
    for i, rec in enumerate(RECS, 1):
        p = doc.add_paragraph()
        p.paragraph_format.left_indent = Cm(1.27)
        p.paragraph_format.first_line_indent = Cm(-0.63)
        run = p.add_run(f"{i}. ")
        run.bold = True
        run.font.size = Pt(12)
        run = p.add_run(rec)
        run.font.size = Pt(12)

    # PRACTICAL APPLICATIONS
    add_heading_styled(doc, "PRACTICAL APPLICATIONS", 1)
    add_body(doc, PRACTICAL_INTRO)
    for bold_part, rest in PRACTICAL_ITEMS:
        p = doc.add_paragraph()
        p.paragraph_format.left_indent = Cm(1.27)
        p.paragraph_format.first_line_indent = Cm(-0.63)
        run = p.add_run("\u2022 ")
        run.font.size = Pt(12)
        run = p.add_run(bold_part)
        run.bold = True
        run.font.size = Pt(12)
        run = p.add_run(rest)
        run.font.size = Pt(12)

    # DISCLOSURES
    add_heading_styled(doc, "DISCLOSURES", 1)
    for label, text in DISCLOSURES:
        p = doc.add_paragraph()
        p.paragraph_format.first_line_indent = Cm(1.27)
        run = p.add_run(label + ": ")
        run.bold = True
        run.font.size = Pt(12)
        run = p.add_run(text)
        run.font.size = Pt(12)

    doc.add_page_break()

    # REFERENCES
    add_heading_styled(doc, "REFERENCES", 1)
    for ref in REFS:
        add_ref(doc, ref)

    # FIGURE LEGENDS
    doc.add_page_break()
    add_heading_styled(doc, "FIGURE LEGENDS", 1)
    for legend in FIGURE_LEGENDS:
        add_figure_legend(doc, legend)

    doc.save(path)
    print(f"Saved mainbody: {path}")


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    title_path = os.path.join(OUTPUT_DIR, "SCJ_Title_Page.docx")
    mainbody_path = os.path.join(OUTPUT_DIR, "SCJ_Narrative_Review_mainbody.docx")
    build_title_page_docx(title_path)
    build_mainbody_docx(mainbody_path)


if __name__ == "__main__":
    main()
