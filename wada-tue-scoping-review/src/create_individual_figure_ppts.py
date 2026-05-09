#!/usr/bin/env python3
"""Generate individual PPT files for each figure (SCJ submission requirement)."""
import os
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.enum.text import PP_ALIGN
from PIL import Image

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FIG_DIR = os.path.join(SCRIPT_DIR, '..', 'figures')
OUT_DIR = os.path.join(SCRIPT_DIR, '..', 'manuscripts', 'individual_figures')
os.makedirs(OUT_DIR, exist_ok=True)

SLIDE_W = Inches(13.333)
SLIDE_H = Inches(7.5)

FIGURES = [
    ('fig1_prisma_flowchart.png',
     'Figure 1',
     'PRISMA-ScR flow diagram illustrating the source selection process.'),
    ('fig4_conceptual_framework.png',
     'Figure 2',
     'Conceptual framework: structural drivers of clinical-competition divergence.'),
    ('fig2_gap_heatmap.png',
     'Figure 3',
     'Clinical-competition gap risk matrix by disease area and assessment dimension.'),
    ('fig3_timeline.png',
     'Figure 4',
     'Timeline of clinical guideline updates versus WADA TUE regulatory changes (2018\u20132026).'),
    ('fig5_severity_bar.png',
     'Figure 5',
     'Clinical-competition gap severity by disease area and assessment dimension.'),
]


def create_individual_ppt(fig_file, title, caption):
    prs = Presentation()
    prs.slide_width = SLIDE_W
    prs.slide_height = SLIDE_H

    slide = prs.slides.add_slide(prs.slide_layouts[6])  # Blank

    # Title
    txBox = slide.shapes.add_textbox(Inches(0.5), Inches(0.2), Inches(12.3), Inches(0.6))
    tf = txBox.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    run = p.add_run()
    run.text = title
    run.font.bold = True
    run.font.size = Pt(24)

    # Image
    fig_path = os.path.join(FIG_DIR, fig_file)
    if os.path.exists(fig_path):
        img = Image.open(fig_path)
        img_w, img_h = img.size

        max_w = Inches(11.0)
        max_h = Inches(5.0)

        emu_w = int(img_w * 914400 / 96)
        emu_h = int(img_h * 914400 / 96)

        scale_w = max_w / emu_w
        scale_h = max_h / emu_h
        scale = min(scale_w, scale_h, 1.0)

        final_w = int(emu_w * scale)
        final_h = int(emu_h * scale)

        left = int((SLIDE_W - final_w) / 2)
        top = Inches(1.0)

        slide.shapes.add_picture(fig_path, left, top, final_w, final_h)

    # Caption
    txBox3 = slide.shapes.add_textbox(Inches(0.5), Inches(6.5), Inches(12.3), Inches(0.8))
    tf3 = txBox3.text_frame
    tf3.word_wrap = True
    p3 = tf3.paragraphs[0]
    p3.alignment = PP_ALIGN.CENTER
    run3 = p3.add_run()
    run3.text = f'{title}. {caption}'
    run3.font.size = Pt(14)
    run3.font.italic = True

    # Save as individual file named by figure number
    fig_num = title.replace('Figure ', '')
    safe_name = f'Figure_{fig_num}.pptx'
    path = os.path.join(OUT_DIR, safe_name)
    prs.save(path)
    print(f'Saved: {path}')


if __name__ == '__main__':
    for fig_file, title, caption in FIGURES:
        create_individual_ppt(fig_file, title, caption)
    print(f'\nAll {len(FIGURES)} individual figure PPT files saved to {OUT_DIR}')
