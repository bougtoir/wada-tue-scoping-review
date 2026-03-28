#!/usr/bin/env python3
"""Create PPTX figure files (English + Japanese) for WADA TUE manuscripts.

- Code-generated charts (fig2, fig3, fig5): embedded as images
- Flowcharts/diagrams (fig1, fig4): built with editable PowerPoint shapes
"""

from pptx import Presentation
from pptx.util import Inches, Pt, Cm, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
import os

FIG_DIR = '/home/ubuntu/figures'
OUT_DIR = '/home/ubuntu'

# ── Colour constants ──────────────────────────────────────────────
WADA_BLUE   = RGBColor(0x1B, 0x3A, 0x5C)
CLIN_GREEN  = RGBColor(0x2E, 0x7D, 0x32)
GAP_RED     = RGBColor(0xC6, 0x28, 0x28)
DARK_GRAY   = RGBColor(0x42, 0x42, 0x42)
WHITE       = RGBColor(0xFF, 0xFF, 0xFF)

# Lighter fills
LIGHT_BLUE  = RGBColor(0xBB, 0xDE, 0xFB)
LIGHT_GREEN = RGBColor(0xC8, 0xE6, 0xC9)
LIGHT_RED   = RGBColor(0xFF, 0xCD, 0xD2)
LIGHT_YELLOW = RGBColor(0xFF, 0xF9, 0xC4)
LIGHT_ORANGE = RGBColor(0xFF, 0xE0, 0xB2)
VERY_LIGHT_BLUE = RGBColor(0xE3, 0xF2, 0xFD)
VERY_LIGHT_GREEN = RGBColor(0xE8, 0xF5, 0xE9)
VERY_LIGHT_RED = RGBColor(0xFF, 0xEB, 0xEE)
VERY_LIGHT_ORANGE = RGBColor(0xFF, 0xF3, 0xE0)
MEDIUM_GRAY = RGBColor(0x75, 0x75, 0x75)
BG_GRAY     = RGBColor(0xE0, 0xE0, 0xE0)


def _add_textbox(slide, left, top, width, height, text, font_size=10,
                 bold=False, color=DARK_GRAY, alignment=PP_ALIGN.CENTER,
                 font_name='Calibri'):
    """Add a simple text box."""
    txBox = slide.shapes.add_textbox(left, top, width, height)
    tf = txBox.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = text
    p.font.size = Pt(font_size)
    p.font.bold = bold
    p.font.color.rgb = color
    p.font.name = font_name
    p.alignment = alignment
    return txBox


def _add_rounded_rect(slide, left, top, width, height, text,
                      fill_color=LIGHT_BLUE, line_color=WADA_BLUE,
                      font_size=9, bold=False, text_color=DARK_GRAY,
                      font_name='Calibri'):
    """Add a rounded rectangle with centered text."""
    shape = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill_color
    shape.line.color.rgb = line_color
    shape.line.width = Pt(1.5)
    tf = shape.text_frame
    tf.word_wrap = True
    tf.paragraphs[0].alignment = PP_ALIGN.CENTER
    for i, line in enumerate(text.split('\n')):
        if i == 0:
            p = tf.paragraphs[0]
        else:
            p = tf.add_paragraph()
            p.alignment = PP_ALIGN.CENTER
        p.text = line
        p.font.size = Pt(font_size)
        p.font.bold = bold
        p.font.color.rgb = text_color
        p.font.name = font_name
    # vertical centre
    tf.paragraphs[0].space_before = Pt(0)
    return shape


def _add_connector(slide, x1, y1, x2, y2, color=DARK_GRAY, width=Pt(1.5)):
    """Add a straight connector line (with arrow)."""
    connector = slide.shapes.add_connector(
        1, x1, y1, x2, y2)  # 1 = straight connector
    connector.line.color.rgb = color
    connector.line.width = width
    # Add arrowhead
    connector.begin_x = x1
    connector.begin_y = y1
    connector.end_x = x2
    connector.end_y = y2
    return connector


def _add_arrow_shape(slide, left, top, width, height, color=DARK_GRAY):
    """Add a down-arrow shape."""
    shape = slide.shapes.add_shape(
        MSO_SHAPE.DOWN_ARROW, left, top, width, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = color
    shape.line.fill.background()
    return shape


# ══════════════════════════════════════════════════════════════════
#  FIGURE 1 – PRISMA-ScR Flow Diagram (editable shapes)
# ══════════════════════════════════════════════════════════════════
def slide_fig1_prisma(prs, lang='en'):
    """Build PRISMA flow diagram with editable shapes."""
    slide = prs.slides.add_slide(prs.slide_layouts[6])  # blank layout

    # --- title ---
    titles = {
        'en': 'Figure 1. PRISMA-ScR Flow Diagram',
        'jp': 'Figure 1. PRISMA-ScR フロー図'
    }
    _add_textbox(slide, Cm(1), Cm(0.3), Cm(22), Cm(1.2),
                 titles[lang], 18, True, WADA_BLUE)

    # --- SECTION LABELS ---
    section_labels = {
        'en': ['IDENTIFICATION', 'SCREENING', 'ELIGIBILITY', 'INCLUDED'],
        'jp': ['同定', 'スクリーニング', '適格性評価', '採択']
    }
    section_y = [Cm(1.8), Cm(5.5), Cm(8.8), Cm(12.0)]
    for lbl, sy in zip(section_labels[lang], section_y):
        _add_textbox(slide, Cm(0.3), sy, Cm(3.5), Cm(0.8),
                     lbl, 10, True, WADA_BLUE, PP_ALIGN.LEFT)

    # --- IDENTIFICATION ---
    box_texts_id = {
        'en': [
            'Records identified through\ndatabase searching\n(n = 847)',
            'Additional records from\ngrey literature & guidelines\n(n = 156)'
        ],
        'jp': [
            'データベース検索による\n同定記録\n(n = 847)',
            '灰色文献・ガイドライン\nリポジトリからの追加記録\n(n = 156)'
        ]
    }
    _add_rounded_rect(slide, Cm(3.5), Cm(1.8), Cm(7), Cm(2.5),
                      box_texts_id[lang][0], LIGHT_BLUE, WADA_BLUE, 10)
    _add_rounded_rect(slide, Cm(13), Cm(1.8), Cm(7), Cm(2.5),
                      box_texts_id[lang][1], LIGHT_BLUE, WADA_BLUE, 10)

    # Arrows down from identification
    _add_arrow_shape(slide, Cm(6.5), Cm(4.4), Cm(0.5), Cm(0.8), DARK_GRAY)
    _add_arrow_shape(slide, Cm(16), Cm(4.4), Cm(0.5), Cm(0.8), DARK_GRAY)

    # --- SCREENING ---
    scr_texts = {
        'en': [
            'Records after duplicates removed\n(n = 724)',
            'Records screened by\ntitle/abstract\n(n = 724)',
            'Records excluded\n(n = 518)'
        ],
        'jp': [
            '重複除去後の記録\n(n = 724)',
            'タイトル・アブストラクト\nスクリーニング\n(n = 724)',
            '除外された記録\n(n = 518)'
        ]
    }
    _add_rounded_rect(slide, Cm(5.5), Cm(5.5), Cm(12.5), Cm(1.5),
                      scr_texts[lang][0], LIGHT_GREEN, CLIN_GREEN, 10)
    _add_arrow_shape(slide, Cm(11.5), Cm(7.1), Cm(0.5), Cm(0.6), DARK_GRAY)
    _add_rounded_rect(slide, Cm(5.5), Cm(7.8), Cm(8), Cm(1.8),
                      scr_texts[lang][1], LIGHT_GREEN, CLIN_GREEN, 10)
    _add_rounded_rect(slide, Cm(16), Cm(7.8), Cm(5.5), Cm(1.8),
                      scr_texts[lang][2], LIGHT_RED, GAP_RED, 10)

    # Arrow right to excluded
    # Arrow down to eligibility
    _add_arrow_shape(slide, Cm(9.2), Cm(9.7), Cm(0.5), Cm(0.6), DARK_GRAY)

    # --- ELIGIBILITY ---
    elig_texts = {
        'en': [
            'Full-text articles assessed\nfor eligibility\n(n = 206)',
            'Full-text excluded (n = 138)\n\nReasons:\n'
            '- Not athlete-specific (n=42)\n- Outdated guidelines (n=31)\n'
            '- Not TUE-related (n=38)\n- Duplicate data (n=27)'
        ],
        'jp': [
            '適格性評価対象の\n全文論文\n(n = 206)',
            '全文除外 (n = 138)\n\n除外理由:\n'
            '- アスリート非特異的 (n=42)\n- 旧式ガイドライン (n=31)\n'
            '- TUE非関連 (n=38)\n- 重複データ (n=27)'
        ]
    }
    _add_rounded_rect(slide, Cm(5.5), Cm(10.5), Cm(8), Cm(1.8),
                      elig_texts[lang][0], LIGHT_YELLOW, RGBColor(0xF9, 0xA8, 0x25), 10)
    _add_rounded_rect(slide, Cm(15.5), Cm(10.2), Cm(7), Cm(3.5),
                      elig_texts[lang][1], LIGHT_RED, GAP_RED, 8)

    _add_arrow_shape(slide, Cm(9.2), Cm(12.4), Cm(0.5), Cm(0.6), DARK_GRAY)

    # --- INCLUDED ---
    incl_texts = {
        'en': 'Sources included in review\n(n = 68)',
        'jp': 'レビューに採択された文献\n(n = 68)'
    }
    _add_rounded_rect(slide, Cm(5.5), Cm(13.2), Cm(8), Cm(1.5),
                      incl_texts[lang], LIGHT_GREEN, CLIN_GREEN, 11, True)

    # Three breakdown boxes
    breakdown = {
        'en': ['WADA regulatory\ndocuments (n=18)',
               'Clinical practice\nguidelines (n=22)',
               'Peer-reviewed\narticles (n=28)'],
        'jp': ['WADA規制文書\n(n=18)',
               '臨床診療\nガイドライン (n=22)',
               '査読付き論文\n(n=28)']
    }
    colors_bd = [VERY_LIGHT_BLUE, VERY_LIGHT_GREEN, VERY_LIGHT_ORANGE]
    borders_bd = [WADA_BLUE, CLIN_GREEN, RGBColor(0xE6, 0x51, 0x00)]
    for i, (txt, fc, bc) in enumerate(zip(breakdown[lang], colors_bd, borders_bd)):
        _add_rounded_rect(slide, Cm(3.5 + i * 6.5), Cm(15.2), Cm(5.5), Cm(1.8),
                          txt, fc, bc, 9, True)

    return slide


# ══════════════════════════════════════════════════════════════════
#  FIGURE 2 – Gap Heatmap (image embed)
# ══════════════════════════════════════════════════════════════════
def slide_fig2_heatmap(prs, lang='en'):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    titles = {
        'en': 'Figure 2. Clinical-Competition Gap Risk Matrix',
        'jp': 'Figure 2. 臨床─競技ギャップ リスクマトリックス'
    }
    _add_textbox(slide, Cm(1), Cm(0.3), Cm(22), Cm(1.2),
                 titles[lang], 18, True, WADA_BLUE)
    img_path = os.path.join(FIG_DIR, 'fig2_gap_heatmap.png')
    slide.shapes.add_picture(img_path, Cm(1), Cm(1.8), Cm(22), Cm(14.5))
    return slide


# ══════════════════════════════════════════════════════════════════
#  FIGURE 3 – Timeline (image embed)
# ══════════════════════════════════════════════════════════════════
def slide_fig3_timeline(prs, lang='en'):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    titles = {
        'en': 'Figure 3. Timeline: Clinical Guidelines vs WADA Regulatory Changes (2018–2026)',
        'jp': 'Figure 3. タイムライン：臨床ガイドライン更新 vs WADA規制変更（2018–2026）'
    }
    _add_textbox(slide, Cm(0.5), Cm(0.3), Cm(23), Cm(1.2),
                 titles[lang], 16, True, WADA_BLUE)
    img_path = os.path.join(FIG_DIR, 'fig3_timeline.png')
    slide.shapes.add_picture(img_path, Cm(0.5), Cm(1.8), Cm(23), Cm(14.5))
    return slide


# ══════════════════════════════════════════════════════════════════
#  FIGURE 4 – Conceptual Framework (editable shapes)
# ══════════════════════════════════════════════════════════════════
def slide_fig4_framework(prs, lang='en'):
    slide = prs.slides.add_slide(prs.slide_layouts[6])

    titles = {
        'en': 'Figure 4. Conceptual Framework: The Clinical-Competition Gap',
        'jp': 'Figure 4. 概念的枠組み：臨床─競技ギャップモデル'
    }
    _add_textbox(slide, Cm(1), Cm(0.3), Cm(22), Cm(1.2),
                 titles[lang], 18, True, WADA_BLUE)

    # --- LEFT: Clinical Practice Guidelines ---
    clin_title = {
        'en': 'CLINICAL PRACTICE\nGUIDELINES',
        'jp': '臨床診療\nガイドライン'
    }
    _add_rounded_rect(slide, Cm(0.8), Cm(2.0), Cm(8), Cm(2.5),
                      clin_title[lang], VERY_LIGHT_GREEN, CLIN_GREEN, 14, True,
                      RGBColor(0x1B, 0x5E, 0x20))

    clin_items = {
        'en': ['GINA (Asthma)', 'ADA (Diabetes)', 'Endocrine Society (Testosterone)',
               'ESC/ESH (Cardiology)', 'NICE (ADHD)', 'PCOS Intl. Guideline'],
        'jp': ['GINA（喘息）', 'ADA（糖尿病）', '内分泌学会（テストステロン）',
               'ESC/ESH（心臓病）', 'NICE（ADHD）', 'PCOS国際ガイドライン']
    }
    item_text = '\n'.join(clin_items[lang])
    _add_textbox(slide, Cm(1), Cm(4.6), Cm(7.5), Cm(4),
                 item_text, 9, False, CLIN_GREEN, PP_ALIGN.LEFT)

    # --- RIGHT: WADA Regulations ---
    wada_title = {
        'en': 'WADA ANTI-DOPING\nREGULATIONS',
        'jp': 'WADAアンチ・ドーピング\n規制'
    }
    _add_rounded_rect(slide, Cm(15.2), Cm(2.0), Cm(8), Cm(2.5),
                      wada_title[lang], VERY_LIGHT_BLUE, WADA_BLUE, 14, True,
                      RGBColor(0x0D, 0x47, 0xA1))

    wada_items = {
        'en': ['Prohibited List (annual)', 'ISTUE Standards', 'TUE Physician Guidelines',
               'Monitoring Program', 'ADAMS System'],
        'jp': ['禁止表（年次更新）', 'ISTUE基準', 'TUE医師ガイドライン',
               'モニタリングプログラム', 'ADAMSシステム']
    }
    item_text_w = '\n'.join(wada_items[lang])
    _add_textbox(slide, Cm(15.5), Cm(4.6), Cm(7.5), Cm(3.5),
                 item_text_w, 9, False, WADA_BLUE, PP_ALIGN.LEFT)

    # --- Arrow from left to center ---
    _add_textbox(slide, Cm(7), Cm(4.5), Cm(3), Cm(1),
                 '→', 28, True, CLIN_GREEN)
    # --- Arrow from right to center ---
    _add_textbox(slide, Cm(14), Cm(4.5), Cm(3), Cm(1),
                 '←', 28, True, WADA_BLUE)

    # --- CENTER GAP BOX ---
    gap_title = {
        'en': 'CLINICAL-COMPETITION\nGAP',
        'jp': '臨床─競技\nギャップ'
    }
    _add_rounded_rect(slide, Cm(8), Cm(3.5), Cm(8), Cm(2.5),
                      gap_title[lang], VERY_LIGHT_RED, GAP_RED, 16, True,
                      RGBColor(0xB7, 0x1C, 0x1C))

    gap_drivers = {
        'en': ['• Update timing lag',
               '• Divergent diagnostic criteria',
               '• Prohibited first-line therapies',
               '• TUE process barriers'],
        'jp': ['• 更新タイミングの遅延',
               '• 診断基準の相違',
               '• 第一選択薬の禁止',
               '• TUEプロセスの障壁']
    }
    _add_textbox(slide, Cm(8.5), Cm(6.2), Cm(7), Cm(3),
                 '\n'.join(gap_drivers[lang]), 10, False, GAP_RED, PP_ALIGN.LEFT)

    # --- Down arrow ---
    _add_arrow_shape(slide, Cm(11.7), Cm(9.0), Cm(0.6), Cm(1.2), GAP_RED)

    # --- IMPACT ON ATHLETES ---
    impact_title = {
        'en': 'IMPACT ON ATHLETES',
        'jp': 'アスリートへの影響'
    }
    _add_rounded_rect(slide, Cm(3), Cm(10.5), Cm(18), Cm(2),
                      impact_title[lang], VERY_LIGHT_ORANGE,
                      RGBColor(0xE6, 0x51, 0x00), 14, True,
                      RGBColor(0xBF, 0x36, 0x0C))

    impact_items = {
        'en': 'Suboptimal treatment  |  Delayed care access  |  ADRV risk  |  Privacy concerns  |  Geographic disparities  |  Career impact',
        'jp': '次善の治療  |  ケアアクセスの遅延  |  ADRV リスク  |  プライバシー懸念  |  地理的格差  |  キャリアへの影響'
    }
    _add_textbox(slide, Cm(3.5), Cm(12.6), Cm(17), Cm(1.2),
                 impact_items[lang], 9, False,
                 RGBColor(0xBF, 0x36, 0x0C))

    # --- Down arrow ---
    _add_arrow_shape(slide, Cm(11.7), Cm(13.8), Cm(0.6), Cm(0.8),
                     RGBColor(0xE6, 0x51, 0x00))

    # --- RECOMMENDATIONS ---
    rec_text = {
        'en': 'RECOMMENDATIONS: Harmonize updates | Streamline TUE | Educate clinicians',
        'jp': '提言：更新の調和 | TUEの簡素化 | 臨床医への教育'
    }
    _add_rounded_rect(slide, Cm(3), Cm(14.8), Cm(18), Cm(1.5),
                      rec_text[lang], BG_GRAY, MEDIUM_GRAY, 10, True, DARK_GRAY)

    return slide


# ══════════════════════════════════════════════════════════════════
#  FIGURE 5 – Severity Bar Chart (image embed)
# ══════════════════════════════════════════════════════════════════
def slide_fig5_severity(prs, lang='en'):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    titles = {
        'en': 'Figure 5. Clinical-Competition Gap Severity by Disease Area',
        'jp': 'Figure 5. 疾患領域別 臨床─競技ギャップ重症度'
    }
    _add_textbox(slide, Cm(1), Cm(0.3), Cm(22), Cm(1.2),
                 titles[lang], 18, True, WADA_BLUE)
    img_path = os.path.join(FIG_DIR, 'fig5_severity_bar.png')
    slide.shapes.add_picture(img_path, Cm(1), Cm(1.8), Cm(22), Cm(14.5))
    return slide


# ══════════════════════════════════════════════════════════════════
#  BUILD PRESENTATIONS
# ══════════════════════════════════════════════════════════════════
def build_pptx(lang='en'):
    prs = Presentation()
    # Set slide size to widescreen (13.333 x 7.5 inches = standard 16:9)
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    slide_fig1_prisma(prs, lang)
    slide_fig2_heatmap(prs, lang)
    slide_fig3_timeline(prs, lang)
    slide_fig4_framework(prs, lang)
    slide_fig5_severity(prs, lang)

    suffix = 'English' if lang == 'en' else 'Japanese'
    out_path = os.path.join(OUT_DIR, f'WADA_TUE_Figures_{suffix}.pptx')
    prs.save(out_path)
    print(f'Saved: {out_path}  ({len(prs.slides)} slides)')
    return out_path


if __name__ == '__main__':
    build_pptx('en')
    build_pptx('jp')
    print('\nDone – both PPTX files created.')
