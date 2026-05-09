#!/usr/bin/env python3
"""Generate individual editable PPT files for each figure (SCJ submission).

All figures are created using native PowerPoint shapes, text boxes, and tables
so they are fully editable in PowerPoint/Keynote.
"""
import os
from pptx import Presentation
from pptx.util import Inches, Pt, Emu, Cm
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.oxml.ns import qn

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(SCRIPT_DIR, '..', 'manuscripts', 'individual_figures')
os.makedirs(OUT_DIR, exist_ok=True)

SLIDE_W = Inches(13.333)
SLIDE_H = Inches(7.5)

# Colors
WADA_BLUE = RGBColor(0x1B, 0x3A, 0x5C)
CLINICAL_GREEN = RGBColor(0x2E, 0x7D, 0x32)
GAP_RED = RGBColor(0xC6, 0x28, 0x28)
DARK_GRAY = RGBColor(0x42, 0x42, 0x42)
ORANGE = RGBColor(0xE6, 0x51, 0x00)


def add_title(slide, text, top=Inches(0.2)):
    """Add a centered title text box."""
    txBox = slide.shapes.add_textbox(Inches(0.5), top, Inches(12.3), Inches(0.6))
    tf = txBox.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    run = p.add_run()
    run.text = text
    run.font.bold = True
    run.font.size = Pt(20)
    run.font.color.rgb = WADA_BLUE
    return txBox


def add_caption(slide, text, top=Inches(6.8)):
    """Add a centered caption text box."""
    txBox = slide.shapes.add_textbox(Inches(0.5), top, Inches(12.3), Inches(0.6))
    tf = txBox.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    run = p.add_run()
    run.text = text
    run.font.size = Pt(12)
    run.font.italic = True
    run.font.color.rgb = DARK_GRAY
    return txBox


def add_box(slide, left, top, width, height, text, fill_rgb, border_rgb,
            font_size=Pt(10), bold=False, text_color=DARK_GRAY):
    """Add a rounded rectangle with centered text."""
    shape = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill_rgb
    shape.line.color.rgb = border_rgb
    shape.line.width = Pt(1.5)
    tf = shape.text_frame
    tf.word_wrap = True
    tf.paragraphs[0].alignment = PP_ALIGN.CENTER
    p = tf.paragraphs[0]
    p.space_before = Pt(0)
    p.space_after = Pt(0)
    run = p.add_run()
    run.text = text
    run.font.size = font_size
    run.font.bold = bold
    run.font.color.rgb = text_color
    # Vertical centering
    tf.paragraphs[0].alignment = PP_ALIGN.CENTER
    shape.text_frame.margin_top = Pt(4)
    shape.text_frame.margin_bottom = Pt(4)
    return shape


def add_connector(slide, start_x, start_y, end_x, end_y):
    """Add a simple line connector (arrow)."""
    connector = slide.shapes.add_connector(
        1,  # straight connector
        start_x, start_y, end_x, end_y)
    connector.line.color.rgb = DARK_GRAY
    connector.line.width = Pt(1.5)
    # Add arrowhead
    line = connector.line
    line.end_marker_style = 2  # Triangle arrowhead
    return connector


def new_prs():
    """Create a new presentation with widescreen slides."""
    prs = Presentation()
    prs.slide_width = SLIDE_W
    prs.slide_height = SLIDE_H
    return prs


# ============================================================
# FIGURE 1: PRISMA-ScR Flow Diagram
# ============================================================
def create_figure_1():
    prs = new_prs()
    slide = prs.slides.add_slide(prs.slide_layouts[6])

    add_title(slide, 'Figure 1. PRISMA-ScR Flow Diagram')

    # Column centers
    col_left = Inches(2.5)
    col_right = Inches(7.5)
    col_center = Inches(5.0)
    box_w = Inches(3.0)
    box_h = Inches(0.7)
    excl_w = Inches(2.5)

    # IDENTIFICATION
    y = Inches(1.0)
    add_box(slide, col_left, y, box_w, box_h,
            'Records from database searching\n(n = 847)',
            RGBColor(0xBB, 0xDE, 0xFB), RGBColor(0x1B, 0x3A, 0x5C), Pt(9))
    add_box(slide, col_right, y, box_w, box_h,
            'Additional records from\ngrey literature & guidelines (n = 156)',
            RGBColor(0xBB, 0xDE, 0xFB), RGBColor(0x1B, 0x3A, 0x5C), Pt(9))

    # After duplicates
    y2 = Inches(2.0)
    add_box(slide, Inches(4.2), y2, Inches(4.5), box_h,
            'Records after duplicates removed (n = 724)',
            RGBColor(0xC8, 0xE6, 0xC9), CLINICAL_GREEN, Pt(10))

    # Screening
    y3 = Inches(3.0)
    add_box(slide, Inches(4.2), y3, Inches(4.5), box_h,
            'Records screened by title/abstract (n = 724)',
            RGBColor(0xC8, 0xE6, 0xC9), CLINICAL_GREEN, Pt(10))
    add_box(slide, Inches(9.5), y3, excl_w, box_h,
            'Records excluded (n = 518)',
            RGBColor(0xFF, 0xCD, 0xD2), GAP_RED, Pt(9))

    # Eligibility
    y4 = Inches(4.0)
    add_box(slide, Inches(4.2), y4, Inches(4.5), box_h,
            'Full-text assessed for eligibility (n = 206)',
            RGBColor(0xFF, 0xF9, 0xC4), RGBColor(0xF9, 0xA8, 0x25), Pt(10))
    add_box(slide, Inches(9.5), y4, excl_w, box_h,
            'Full-text excluded (n = 138)',
            RGBColor(0xFF, 0xCD, 0xD2), GAP_RED, Pt(9))

    # Included
    y5 = Inches(5.0)
    add_box(slide, Inches(4.2), y5, Inches(4.5), box_h,
            'Sources included in review (n = 68)',
            RGBColor(0xC8, 0xE6, 0xC9), RGBColor(0x2E, 0x7D, 0x32), Pt(11), True)

    # Breakdown
    y6 = Inches(6.0)
    add_box(slide, Inches(2.0), y6, Inches(2.8), Inches(0.6),
            'WADA regulatory docs (n = 18)',
            RGBColor(0xE3, 0xF2, 0xFD), RGBColor(0x15, 0x65, 0xC0), Pt(9))
    add_box(slide, Inches(5.2), y6, Inches(2.8), Inches(0.6),
            'Clinical practice guidelines (n = 22)',
            RGBColor(0xE8, 0xF5, 0xE9), CLINICAL_GREEN, Pt(9))
    add_box(slide, Inches(8.4), y6, Inches(2.8), Inches(0.6),
            'Peer-reviewed articles (n = 28)',
            RGBColor(0xFF, 0xF3, 0xE0), ORANGE, Pt(9))

    # Phase labels
    phases = [('IDENTIFICATION', Inches(1.0)), ('SCREENING', Inches(3.0)),
              ('ELIGIBILITY', Inches(4.0)), ('INCLUDED', Inches(5.0))]
    for label, ytop in phases:
        txBox = slide.shapes.add_textbox(Inches(0.3), ytop, Inches(1.8), Inches(0.5))
        tf = txBox.text_frame
        run = tf.paragraphs[0].add_run()
        run.text = label
        run.font.size = Pt(8)
        run.font.bold = True
        run.font.italic = True
        run.font.color.rgb = WADA_BLUE

    add_caption(slide, 'Figure 1. PRISMA-ScR flow diagram illustrating the source selection process.')

    path = os.path.join(OUT_DIR, 'Figure_1.pptx')
    prs.save(path)
    print(f'Saved: {path}')


# ============================================================
# FIGURE 2: Conceptual Framework
# ============================================================
def create_figure_2():
    prs = new_prs()
    slide = prs.slides.add_slide(prs.slide_layouts[6])

    add_title(slide, 'Figure 2. Conceptual Framework:\nThe Clinical-Competition Gap in Anti-Doping',
              top=Inches(0.1))

    # LEFT: Clinical Practice Guidelines
    left_box = add_box(slide, Inches(0.8), Inches(1.2), Inches(4.5), Inches(2.2),
                       'CLINICAL PRACTICE\nGUIDELINES\n\nGINA (Asthma)\nADA (Diabetes)\nEndocrine Society\nESC (Cardiology)\nNICE (ADHD)',
                       RGBColor(0xE8, 0xF5, 0xE9), CLINICAL_GREEN, Pt(11), False, RGBColor(0x1B, 0x5E, 0x20))

    # RIGHT: WADA Regulations
    right_box = add_box(slide, Inches(8.0), Inches(1.2), Inches(4.5), Inches(2.2),
                        'WADA ANTI-DOPING\nREGULATIONS\n\nProhibited List\nISTUE Standards\nTUE Physician Guidelines\nMonitoring Program\nADAMS System',
                        RGBColor(0xE3, 0xF2, 0xFD), RGBColor(0x15, 0x65, 0xC0), Pt(11), False, RGBColor(0x0D, 0x47, 0xA1))

    # Label arrows
    txBox = slide.shapes.add_textbox(Inches(4.0), Inches(3.5), Inches(2.0), Inches(0.4))
    tf = txBox.text_frame
    tf.paragraphs[0].alignment = PP_ALIGN.CENTER
    run = tf.paragraphs[0].add_run()
    run.text = 'Evidence-based\nrecommendations'
    run.font.size = Pt(8)
    run.font.italic = True
    run.font.color.rgb = CLINICAL_GREEN

    txBox2 = slide.shapes.add_textbox(Inches(7.3), Inches(3.5), Inches(2.0), Inches(0.4))
    tf2 = txBox2.text_frame
    tf2.paragraphs[0].alignment = PP_ALIGN.CENTER
    run2 = tf2.paragraphs[0].add_run()
    run2.text = 'Regulatory\nrestrictions'
    run2.font.size = Pt(8)
    run2.font.italic = True
    run2.font.color.rgb = RGBColor(0x15, 0x65, 0xC0)

    # CENTER: Clinical-Competition Gap
    gap_box = add_box(slide, Inches(4.0), Inches(4.0), Inches(5.3), Inches(1.5),
                      'CLINICAL-COMPETITION GAP\n\nUpdate timing lag | Divergent criteria\nProhibited first-line Rx | TUE process barriers',
                      RGBColor(0xFF, 0xEB, 0xEE), GAP_RED, Pt(12), True, RGBColor(0xB7, 0x1C, 0x1C))

    # BOTTOM: Impact on Athletes
    impact_box = add_box(slide, Inches(2.5), Inches(5.8), Inches(8.3), Inches(1.2),
                         'IMPACT ON ATHLETES\n\nSuboptimal treatment | Delayed care access | ADRV risk\nPrivacy concerns | Geographic disparities | Career impact',
                         RGBColor(0xFF, 0xF3, 0xE0), ORANGE, Pt(10), False, RGBColor(0xBF, 0x36, 0x0C))

    # Recommendations
    rec_box = add_box(slide, Inches(2.5), Inches(7.1), Inches(8.3), Inches(0.35),
                      'RECOMMENDATIONS: Harmonize updates | Streamline TUE | Educate clinicians',
                      RGBColor(0xE0, 0xE0, 0xE0), RGBColor(0x75, 0x75, 0x75), Pt(9), True, DARK_GRAY)

    path = os.path.join(OUT_DIR, 'Figure_2.pptx')
    prs.save(path)
    print(f'Saved: {path}')


# ============================================================
# FIGURE 3: Gap Risk Matrix (Heatmap as Table)
# ============================================================
def create_figure_3():
    prs = new_prs()
    slide = prs.slides.add_slide(prs.slide_layouts[6])

    add_title(slide, 'Figure 3. Clinical-Competition Gap Risk Matrix\nby Disease Area and Assessment Dimension',
              top=Inches(0.1))

    diseases = [
        'Asthma (Beta-2 agonists)',
        'ADHD (Stimulants)',
        'Type 2 Diabetes (GLP-1 RAs)',
        'Male Hypogonadism (Testosterone)',
        'Glucocorticoids (Intra-articular)',
        'Cardiovascular (Diuretics/BB)',
        'PCOS/Fertility (Letrozole/Clomiphene)'
    ]
    dimensions = [
        'First-line Rx\nProhibited',
        'TUE Process\nComplexity',
        'Guideline\nUpdate Lag',
        'Athlete\nImpact',
        'Alternative Rx\nAvailability'
    ]
    # Severity scores (0-4)
    data = [
        [2, 2, 2, 3, 4],  # Asthma
        [4, 4, 2, 4, 2],  # ADHD
        [1, 2, 3, 3, 3],  # T2DM
        [4, 4, 3, 4, 1],  # Hypogonadism
        [3, 2, 2, 3, 3],  # GC
        [3, 3, 3, 3, 2],  # CV
        [4, 3, 2, 3, 1],  # PCOS
    ]
    risk_labels = {0: 'None', 1: 'Low', 2: 'Med', 3: 'High', 4: 'V.High'}
    # Color mapping
    severity_colors = {
        0: RGBColor(0xE8, 0xF5, 0xE9),
        1: RGBColor(0xC8, 0xE6, 0xC9),
        2: RGBColor(0xFF, 0xF9, 0xC4),
        3: RGBColor(0xFF, 0xE0, 0xB2),
        4: RGBColor(0xEF, 0x53, 0x50),
    }

    rows = len(diseases) + 1  # header + data
    cols = len(dimensions) + 1  # row header + data

    tbl_left = Inches(1.0)
    tbl_top = Inches(1.3)
    tbl_w = Inches(11.3)
    tbl_h = Inches(5.0)

    table_shape = slide.shapes.add_table(rows, cols, tbl_left, tbl_top, tbl_w, tbl_h)
    table = table_shape.table

    # Set column widths
    table.columns[0].width = Inches(3.3)
    for j in range(1, cols):
        table.columns[j].width = Inches(1.6)

    # Header row
    header_cell = table.cell(0, 0)
    header_cell.text = 'Disease Area'
    for j, dim in enumerate(dimensions):
        cell = table.cell(0, j + 1)
        cell.text = dim

    # Data rows
    for i, disease in enumerate(diseases):
        table.cell(i + 1, 0).text = disease
        for j, score in enumerate(data[i]):
            cell = table.cell(i + 1, j + 1)
            cell.text = risk_labels[score]
            # Color fill
            fill = cell.fill
            fill.solid()
            fill.fore_color.rgb = severity_colors[score]

    # Format all cells
    for i in range(rows):
        for j in range(cols):
            cell = table.cell(i, j)
            for paragraph in cell.text_frame.paragraphs:
                paragraph.alignment = PP_ALIGN.CENTER
                for run in paragraph.runs:
                    run.font.size = Pt(10) if i > 0 else Pt(9)
                    run.font.bold = (i == 0 or j == 0)
            cell.vertical_anchor = MSO_ANCHOR.MIDDLE

    # Header row color
    for j in range(cols):
        cell = table.cell(0, j)
        cell.fill.solid()
        cell.fill.fore_color.rgb = RGBColor(0xE3, 0xF2, 0xFD)

    # Row header column color
    for i in range(1, rows):
        cell = table.cell(i, 0)
        cell.fill.solid()
        cell.fill.fore_color.rgb = RGBColor(0xF5, 0xF5, 0xF5)

    add_caption(slide,
                'Figure 3. Clinical-competition gap risk matrix by disease area and assessment dimension.\n'
                'Severity: None (0), Low (1), Medium (2), High (3), Very High (4).',
                top=Inches(6.5))

    path = os.path.join(OUT_DIR, 'Figure_3.pptx')
    prs.save(path)
    print(f'Saved: {path}')


# ============================================================
# FIGURE 4: Timeline
# ============================================================
def create_figure_4():
    prs = new_prs()
    slide = prs.slides.add_slide(prs.slide_layouts[6])

    add_title(slide, 'Figure 4. Timeline of Clinical Guideline Updates vs.\nWADA TUE Regulatory Changes (2018\u20132026)',
              top=Inches(0.1))

    # Central timeline line
    line_y = Inches(3.75)
    line = slide.shapes.add_connector(1, Inches(1.0), line_y, Inches(12.3), line_y)
    line.line.color.rgb = DARK_GRAY
    line.line.width = Pt(2)

    # Year markers
    years = list(range(2018, 2027))
    for i, year in enumerate(years):
        x = Inches(1.2 + i * 1.23)
        txBox = slide.shapes.add_textbox(x, Inches(3.85), Inches(0.8), Inches(0.3))
        tf = txBox.text_frame
        tf.paragraphs[0].alignment = PP_ALIGN.CENTER
        run = tf.paragraphs[0].add_run()
        run.text = str(year)
        run.font.size = Pt(8)
        run.font.bold = True

    # WADA events (above line)
    wada_events = [
        (2022, 'GC intra-articular\nprohibited IC'),
        (2023.8, 'Diabetes TUE\nGuideline v5.1'),
        (2024, 'GLP-1 RA\nMonitoring'),
        (2025, 'PCOS TUE GL v2.0\nHypogonadism update'),
        (2026, 'Asthma TUE v9.3\nADHD TUE v8.0'),
    ]

    # Label: WADA
    txBox = slide.shapes.add_textbox(Inches(0.2), Inches(1.5), Inches(1.5), Inches(0.5))
    tf = txBox.text_frame
    run = tf.paragraphs[0].add_run()
    run.text = 'WADA\nRegulatory\nUpdates'
    run.font.size = Pt(9)
    run.font.bold = True
    run.font.color.rgb = WADA_BLUE

    for year_pos, label in wada_events:
        x = Inches(1.2 + (year_pos - 2018) * 1.23)
        y_idx = wada_events.index((year_pos, label))
        y = Inches(1.5 + (y_idx % 2) * 0.9)
        box = add_box(slide, x, y, Inches(1.8), Inches(0.7), label,
                      RGBColor(0xE3, 0xF2, 0xFD), RGBColor(0x15, 0x65, 0xC0), Pt(7))

    # Clinical events (below line)
    clinical_events = [
        (2018.5, 'Endocrine Soc.\nTestosterone GL'),
        (2022, 'Australian\nADHD GL'),
        (2023.5, 'PCOS Intl GL\nTRAVERSE trial'),
        (2024.5, 'NICE ADHD\nEAU Reprod Health'),
        (2025.4, 'GINA 2025\nADA Diabetes 2025'),
    ]

    # Label: Clinical
    txBox = slide.shapes.add_textbox(Inches(0.2), Inches(4.8), Inches(1.5), Inches(0.5))
    tf = txBox.text_frame
    run = tf.paragraphs[0].add_run()
    run.text = 'Clinical\nGuideline\nUpdates'
    run.font.size = Pt(9)
    run.font.bold = True
    run.font.color.rgb = CLINICAL_GREEN

    for year_pos, label in clinical_events:
        x = Inches(1.2 + (year_pos - 2018) * 1.23)
        y_idx = clinical_events.index((year_pos, label))
        y = Inches(4.5 + (y_idx % 2) * 0.9)
        box = add_box(slide, x, y, Inches(1.8), Inches(0.7), label,
                      RGBColor(0xE8, 0xF5, 0xE9), CLINICAL_GREEN, Pt(7))

    # GAP label
    gap_box = slide.shapes.add_textbox(Inches(11.5), Inches(3.4), Inches(1.0), Inches(0.7))
    tf = gap_box.text_frame
    tf.paragraphs[0].alignment = PP_ALIGN.CENTER
    run = tf.paragraphs[0].add_run()
    run.text = 'GAP'
    run.font.size = Pt(14)
    run.font.bold = True
    run.font.color.rgb = GAP_RED

    add_caption(slide,
                'Figure 4. Timeline of clinical guideline updates versus WADA TUE regulatory changes (2018\u20132026).',
                top=Inches(6.8))

    path = os.path.join(OUT_DIR, 'Figure_4.pptx')
    prs.save(path)
    print(f'Saved: {path}')


# ============================================================
# FIGURE 5: Severity Bar Chart (as table with visual bars)
# ============================================================
def create_figure_5():
    prs = new_prs()
    slide = prs.slides.add_slide(prs.slide_layouts[6])

    add_title(slide, 'Figure 5. Clinical-Competition Gap Severity\nby Disease Area and Assessment Dimension',
              top=Inches(0.1))

    diseases = [
        'Male Hypogonadism',
        'ADHD',
        'PCOS/Fertility',
        'Cardiovascular',
        'Glucocorticoids',
        'Asthma',
        'Type 2 Diabetes / GLP-1 RA'
    ]
    # Scores per dimension
    first_line = [4, 4, 4, 3, 3, 2, 1]
    tue_complex = [4, 4, 3, 3, 2, 2, 2]
    update_lag = [3, 2, 2, 3, 2, 2, 3]
    athlete_impact = [4, 4, 3, 3, 3, 3, 3]

    dimensions = ['First-line Rx\nProhibited', 'TUE Process\nComplexity',
                  'Guideline\nUpdate Lag', 'Athlete\nImpact']
    all_data = [first_line, tue_complex, update_lag, athlete_impact]
    dim_colors = [
        RGBColor(0xEF, 0x53, 0x50),  # Red
        RGBColor(0xFF, 0x98, 0x00),  # Orange
        RGBColor(0xFD, 0xD8, 0x35),  # Yellow
        RGBColor(0x42, 0xA5, 0xF5),  # Blue
    ]

    # Create table
    rows = len(diseases) + 1
    cols = len(dimensions) + 1
    tbl_left = Inches(1.0)
    tbl_top = Inches(1.3)
    tbl_w = Inches(11.3)
    tbl_h = Inches(4.8)

    table_shape = slide.shapes.add_table(rows, cols, tbl_left, tbl_top, tbl_w, tbl_h)
    table = table_shape.table

    table.columns[0].width = Inches(3.3)
    for j in range(1, cols):
        table.columns[j].width = Inches(2.0)

    # Header
    table.cell(0, 0).text = 'Disease Area'
    for j, dim in enumerate(dimensions):
        table.cell(0, j + 1).text = dim

    # Data
    severity_labels = {0: 'None', 1: 'Low', 2: 'Medium', 3: 'High', 4: 'Very High'}
    for i, disease in enumerate(diseases):
        table.cell(i + 1, 0).text = disease
        for j, scores in enumerate(all_data):
            score = scores[i]
            cell = table.cell(i + 1, j + 1)
            cell.text = f'{severity_labels[score]} ({score})'
            # Intensity-based fill
            intensity = int(score * 63)
            base = dim_colors[j]
            # Lighten based on score
            r = min(255, base[0] + (255 - base[0]) * (4 - score) // 4)
            g = min(255, base[1] + (255 - base[1]) * (4 - score) // 4)
            b = min(255, base[2] + (255 - base[2]) * (4 - score) // 4)
            cell.fill.solid()
            cell.fill.fore_color.rgb = RGBColor(r, g, b)

    # Format all cells
    for i in range(rows):
        for j in range(cols):
            cell = table.cell(i, j)
            for paragraph in cell.text_frame.paragraphs:
                paragraph.alignment = PP_ALIGN.CENTER
                for run in paragraph.runs:
                    run.font.size = Pt(10) if i > 0 else Pt(9)
                    run.font.bold = (i == 0 or j == 0)
            cell.vertical_anchor = MSO_ANCHOR.MIDDLE

    # Header styling
    for j in range(cols):
        cell = table.cell(0, j)
        cell.fill.solid()
        cell.fill.fore_color.rgb = RGBColor(0xE3, 0xF2, 0xFD)

    # Legend
    legend_y = Inches(6.3)
    txBox = slide.shapes.add_textbox(Inches(1.0), legend_y, Inches(11.0), Inches(0.4))
    tf = txBox.text_frame
    tf.paragraphs[0].alignment = PP_ALIGN.CENTER
    run = tf.paragraphs[0].add_run()
    run.text = 'Severity Scale: None (0) | Low (1) | Medium (2) | High (3) | Very High (4)'
    run.font.size = Pt(10)
    run.font.italic = True

    add_caption(slide,
                'Figure 5. Clinical-competition gap severity by disease area and assessment dimension.',
                top=Inches(6.8))

    path = os.path.join(OUT_DIR, 'Figure_5.pptx')
    prs.save(path)
    print(f'Saved: {path}')


# ============================================================
if __name__ == '__main__':
    create_figure_1()
    create_figure_2()
    create_figure_3()
    create_figure_4()
    create_figure_5()
    print(f'\nAll 5 individual editable figure PPT files saved to {OUT_DIR}')
