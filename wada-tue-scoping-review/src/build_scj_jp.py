#!/usr/bin/env python3
"""Build SCJ Full Narrative Review Japanese .docx from content data."""
import sys
sys.path.insert(0, '/home/ubuntu')
from create_scj_review_part1 import *
from scj_jp_content import *
from scj_en_content import REFS  # References stay in English

doc = Document()
setup_styles(doc)

# ===== NONBLINDED TITLE PAGE =====
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = p.add_run(TITLE_JP)
run.bold = True; run.font.size = Pt(14)

doc.add_paragraph()
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = p.add_run(AUTHOR_LINE_JP); run.font.size = Pt(12)

doc.add_paragraph()
for aff in AFFILIATIONS_JP:
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(aff); run.font.size = Pt(10); run.italic = True

doc.add_paragraph()
p = doc.add_paragraph()
run = p.add_run('現職: '); run.bold = True; run.font.size = Pt(10)
run = p.add_run(CURRENT_POS_JP); run.font.size = Pt(10)

doc.add_paragraph()
p = doc.add_paragraph()
run = p.add_run('責任著者: '); run.bold = True; run.font.size = Pt(10)
run = p.add_run(CORRESP_JP); run.font.size = Pt(10)

doc.add_page_break()

# ===== BLINDED TITLE PAGE =====
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = p.add_run(TITLE_JP)
run.bold = True; run.font.size = Pt(14)

doc.add_paragraph()
p = doc.add_paragraph()
run = p.add_run('ランニングヘッド: '); run.bold = True; run.font.size = Pt(10)
run = p.add_run(RUNNING_HEAD_JP); run.font.size = Pt(10)

doc.add_paragraph()
p = doc.add_paragraph()
run = p.add_run('キーワード: '); run.bold = True; run.font.size = Pt(10)
run = p.add_run(KEYWORDS_JP); run.font.size = Pt(10)

doc.add_page_break()

# ===== ABSTRACT =====
add_heading_styled(doc, '抄録', 1)
add_body_ni(doc, ABSTRACT_JP)
doc.add_page_break()

# ===== INTRODUCTION =====
add_heading_styled(doc, '序論', 1)
for para in INTRO_JP:
    add_body(doc, para)

# ===== METHODS =====
add_heading_styled(doc, '方法', 1)
for sub_title, paras in METHODS_JP.items():
    add_heading_styled(doc, sub_title, 2)
    for para in paras:
        add_body(doc, para)

# ===== RESULTS =====
add_heading_styled(doc, '結果', 1)
add_heading_styled(doc, 'エビデンス源の選択', 2)
add_body(doc, RESULTS_SOURCE_JP)

doc.add_paragraph()
add_figure(doc, 'fig1_prisma_flowchart.png',
           'Figure 1. エビデンス源選択プロセスを示すPRISMA-ScRフロー図')

add_heading_styled(doc, '臨床─競技ギャップの概要', 2)
add_body(doc, RESULTS_OVERVIEW_JP)

doc.add_paragraph()
add_figure(doc, 'fig2_gap_heatmap.png',
           'Figure 2. 疾患領域および評価次元別の臨床─競技ギャップリスクマトリックス')

# Disease-specific results
for disease_title, paras in DISEASE_RESULTS_JP.items():
    add_heading_styled(doc, disease_title, 2)
    for para in paras:
        add_body(doc, para)

# Cross-cutting analysis
add_heading_styled(doc, '横断的分析：乖離の構造的要因', 2)
add_body(doc, CROSS_CUTTING_JP)
add_body(doc, CROSS_CUTTING_2_JP)

doc.add_paragraph()
add_figure(doc, 'fig3_timeline.png',
           'Figure 3. 臨床ガイドライン更新とWADA TUE規制変更のタイムライン（2018〜2026年）')

# ===== DISCUSSION =====
add_heading_styled(doc, '考察', 1)
for para in DISCUSSION_JP:
    add_body(doc, para)

# ===== PRACTICAL APPLICATIONS =====
add_heading_styled(doc, '実践的応用', 1)
add_body(doc, PRACTICAL_INTRO_JP)

for bold_part, rest in PRACTICAL_ITEMS_JP:
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
           'Figure 5. 疾患領域および評価次元別の臨床─競技ギャップ重症度')

# ===== RECOMMENDATIONS =====
add_heading_styled(doc, '調和に向けた提言', 1)
add_body(doc, RECS_INTRO_JP)

for i, rec in enumerate(RECS_JP, 1):
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Cm(1.27)
    p.paragraph_format.first_line_indent = Cm(-0.63)
    run = p.add_run(f'{i}. ')
    run.bold = True; run.font.size = Pt(12)
    run = p.add_run(rec)
    run.font.size = Pt(12)

# ===== CONCLUSION =====
add_heading_styled(doc, '結論', 1)
for para in CONCLUSION_JP:
    add_body(doc, para)

doc.add_page_break()

# ===== REFERENCES (English) =====
add_heading_styled(doc, '参考文献', 1)
for ref in REFS:
    add_ref(doc, ref)

output_path = os.path.join(OUTPUT_DIR, 'SCJ_Narrative_Review_Japanese.docx')
doc.save(output_path)
print(f"Saved: {output_path}")
