#!/usr/bin/env python3
"""Build SCJ Full Narrative Review English .docx from content data."""
import sys
sys.path.insert(0, '/home/ubuntu')
from create_scj_review_part1 import *
from scj_en_content import *

doc = Document()
setup_styles(doc)

# ===== NONBLINDED TITLE PAGE =====
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = p.add_run(TITLE)
run.bold = True; run.font.size = Pt(14)

doc.add_paragraph()
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = p.add_run(AUTHOR_LINE); run.font.size = Pt(12)

doc.add_paragraph()
for aff in AFFILIATIONS:
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(aff); run.font.size = Pt(10); run.italic = True

doc.add_paragraph()
p = doc.add_paragraph()
run = p.add_run('Current Position: '); run.bold = True; run.font.size = Pt(10)
run = p.add_run(CURRENT_POS); run.font.size = Pt(10)

doc.add_paragraph()
p = doc.add_paragraph()
run = p.add_run('Corresponding Author: '); run.bold = True; run.font.size = Pt(10)
run = p.add_run(CORRESP); run.font.size = Pt(10)

doc.add_page_break()

# ===== BLINDED TITLE PAGE =====
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = p.add_run(TITLE)
run.bold = True; run.font.size = Pt(14)

doc.add_paragraph()
p = doc.add_paragraph()
run = p.add_run('Running Head: '); run.bold = True; run.font.size = Pt(10)
run = p.add_run(RUNNING_HEAD); run.font.size = Pt(10)

doc.add_paragraph()
p = doc.add_paragraph()
run = p.add_run('Keywords: '); run.bold = True; run.font.size = Pt(10)
run = p.add_run(KEYWORDS); run.font.size = Pt(10)

doc.add_page_break()

# ===== ABSTRACT =====
add_heading_styled(doc, 'ABSTRACT', 1)
add_body_ni(doc, ABSTRACT)
doc.add_page_break()

# ===== INTRODUCTION =====
add_heading_styled(doc, 'INTRODUCTION', 1)
for para in INTRO:
    add_body(doc, para)

# ===== METHODS =====
add_heading_styled(doc, 'METHODS', 1)
for sub_title, paras in METHODS.items():
    add_heading_styled(doc, sub_title, 2)
    for para in paras:
        add_body(doc, para)

# ===== RESULTS =====
add_heading_styled(doc, 'RESULTS', 1)
add_heading_styled(doc, 'Source Selection', 2)
add_body(doc, RESULTS_SOURCE)

doc.add_paragraph()
add_figure(doc, 'fig1_prisma_flowchart.png',
           'Figure 1. PRISMA-ScR flow diagram illustrating the source selection process.')

add_heading_styled(doc, 'Overview of Clinical-Competition Gaps', 2)
add_body(doc, RESULTS_OVERVIEW)

doc.add_paragraph()
add_figure(doc, 'fig2_gap_heatmap.png',
           'Figure 2. Clinical-competition gap risk matrix by disease area and assessment dimension.')

# Disease-specific results
for disease_title, paras in DISEASE_RESULTS.items():
    add_heading_styled(doc, disease_title, 2)
    for para in paras:
        add_body(doc, para)

# Cross-cutting analysis
add_heading_styled(doc, 'Cross-Cutting Analysis: Structural Drivers of Divergence', 2)
add_body(doc, CROSS_CUTTING)
add_body(doc, CROSS_CUTTING_2)

doc.add_paragraph()
add_figure(doc, 'fig3_timeline.png',
           'Figure 3. Timeline of clinical guideline updates versus WADA TUE regulatory changes (2018\u20132026).')

# ===== DISCUSSION =====
add_heading_styled(doc, 'DISCUSSION', 1)
for para in DISCUSSION:
    add_body(doc, para)

# ===== PRACTICAL APPLICATIONS =====
add_heading_styled(doc, 'PRACTICAL APPLICATIONS', 1)
add_body(doc, PRACTICAL_INTRO)

for bold_part, rest in PRACTICAL_ITEMS:
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Cm(1.27)
    p.paragraph_format.first_line_indent = Cm(-0.63)
    run = p.add_run('\u2022 ')
    run.font.size = Pt(12)
    run = p.add_run(bold_part)
    run.bold = True; run.font.size = Pt(12)
    run = p.add_run(rest)
    run.font.size = Pt(12)

doc.add_paragraph()
add_figure(doc, 'fig5_severity_bar.png',
           'Figure 5. Clinical-competition gap severity by disease area and assessment dimension.')

# ===== RECOMMENDATIONS =====
add_heading_styled(doc, 'RECOMMENDATIONS FOR HARMONIZATION', 1)
add_body(doc, RECS_INTRO)

for i, rec in enumerate(RECS, 1):
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Cm(1.27)
    p.paragraph_format.first_line_indent = Cm(-0.63)
    run = p.add_run(f'{i}. ')
    run.bold = True; run.font.size = Pt(12)
    run = p.add_run(rec)
    run.font.size = Pt(12)

# ===== CONCLUSION =====
add_heading_styled(doc, 'CONCLUSION', 1)
for para in CONCLUSION:
    add_body(doc, para)

doc.add_page_break()

# ===== REFERENCES =====
add_heading_styled(doc, 'REFERENCES', 1)
for ref in REFS:
    add_ref(doc, ref)

output_path = os.path.join(OUTPUT_DIR, 'SCJ_Narrative_Review_English.docx')
doc.save(output_path)
print(f"Saved: {output_path}")

# Count approximate words
import re
word_count = 0
for para in doc.paragraphs:
    word_count += len(re.findall(r'\w+', para.text))
print(f"Approximate word count: {word_count}")
