#!/usr/bin/env python3
"""Create all color figures for WADA TUE papers."""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np
import os

OUTPUT_DIR = "/home/ubuntu/figures"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Color palette
COLORS = {
    'wada_blue': '#1B3A5C',
    'clinical_green': '#2E7D32',
    'gap_red': '#C62828',
    'gap_orange': '#E65100',
    'gap_yellow': '#F9A825',
    'light_blue': '#BBDEFB',
    'light_green': '#C8E6C9',
    'light_red': '#FFCDD2',
    'light_orange': '#FFE0B2',
    'light_yellow': '#FFF9C4',
    'bg_gray': '#F5F5F5',
    'white': '#FFFFFF',
    'dark_gray': '#424242',
    'medium_gray': '#757575',
}

plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['DejaVu Sans', 'Arial', 'Helvetica'],
    'font.size': 10,
    'axes.titlesize': 12,
    'axes.labelsize': 10,
})


def fig1_prisma_flowchart():
    """Figure 1: PRISMA-ScR Flow Diagram for SCJ paper."""
    fig, ax = plt.subplots(figsize=(10, 12))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 14)
    ax.axis('off')
    fig.patch.set_facecolor('white')

    def draw_box(x, y, w, h, text, color='#BBDEFB', edge='#1B3A5C', fontsize=9):
        box = FancyBboxPatch((x - w/2, y - h/2), w, h,
                             boxstyle="round,pad=0.15",
                             facecolor=color, edgecolor=edge, linewidth=1.5)
        ax.add_patch(box)
        ax.text(x, y, text, ha='center', va='center', fontsize=fontsize,
                wrap=True, fontweight='normal',
                bbox=dict(facecolor='none', edgecolor='none'))

    def draw_arrow(x1, y1, x2, y2):
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle='->', color=COLORS['dark_gray'],
                                    lw=1.5, connectionstyle='arc3,rad=0'))

    # Title
    ax.text(5, 13.5, 'Figure 1. PRISMA-ScR Flow Diagram',
            ha='center', va='center', fontsize=14, fontweight='bold',
            color=COLORS['wada_blue'])

    # IDENTIFICATION
    ax.text(0.5, 12.5, 'IDENTIFICATION', ha='left', va='center',
            fontsize=10, fontweight='bold', color=COLORS['wada_blue'],
            style='italic')

    draw_box(3.5, 11.8, 3.2, 1.0,
             'Records identified through\ndatabase searching\n(n = 847)',
             '#BBDEFB')
    draw_box(7.5, 11.8, 3.2, 1.0,
             'Additional records from\ngrey literature & guidelines\n(n = 156)',
             '#BBDEFB')

    draw_arrow(3.5, 11.3, 5, 10.5)
    draw_arrow(7.5, 11.3, 5, 10.5)

    # SCREENING
    ax.text(0.5, 10.5, 'SCREENING', ha='left', va='center',
            fontsize=10, fontweight='bold', color=COLORS['wada_blue'],
            style='italic')

    draw_box(5, 10.0, 3.5, 0.8,
             'Records after duplicates removed (n = 724)',
             '#C8E6C9')
    draw_arrow(5, 9.6, 5, 8.9)

    draw_box(5, 8.5, 3.5, 0.8,
             'Records screened by title/abstract (n = 724)',
             '#C8E6C9')
    draw_box(8.5, 8.5, 2.2, 0.8,
             'Records excluded\n(n = 518)',
             '#FFCDD2')
    draw_arrow(6.75, 8.5, 7.4, 8.5)
    draw_arrow(5, 8.1, 5, 7.4)

    # ELIGIBILITY
    ax.text(0.5, 7.5, 'ELIGIBILITY', ha='left', va='center',
            fontsize=10, fontweight='bold', color=COLORS['wada_blue'],
            style='italic')

    draw_box(5, 7.0, 3.5, 0.8,
             'Full-text articles assessed for eligibility (n = 206)',
             '#FFF9C4')
    draw_box(8.5, 7.0, 2.2, 0.8,
             'Full-text excluded\n(n = 138)',
             '#FFCDD2')
    draw_arrow(6.75, 7.0, 7.4, 7.0)
    draw_arrow(5, 6.6, 5, 5.9)

    # Exclusion reasons
    reasons_text = ('Reasons for exclusion:\n'
                    '- Not athlete-specific (n=42)\n'
                    '- Outdated guidelines (n=31)\n'
                    '- Not TUE-related (n=38)\n'
                    '- Duplicate data (n=27)')
    ax.text(8.5, 5.8, reasons_text, ha='center', va='top',
            fontsize=7, color=COLORS['medium_gray'],
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFF9C4',
                      edgecolor='#BDBDBD', alpha=0.7))

    # INCLUDED
    ax.text(0.5, 5.7, 'INCLUDED', ha='left', va='center',
            fontsize=10, fontweight='bold', color=COLORS['wada_blue'],
            style='italic')

    draw_box(5, 5.3, 3.5, 0.8,
             'Sources of evidence included in review (n = 68)',
             '#C8E6C9', '#2E7D32')

    draw_arrow(5, 4.9, 3, 4.2)
    draw_arrow(5, 4.9, 5, 4.2)
    draw_arrow(5, 4.9, 7, 4.2)

    # Breakdown boxes
    draw_box(3, 3.6, 2.5, 1.0,
             'WADA regulatory\ndocuments\n(n = 18)',
             '#E3F2FD', '#1565C0', 8)
    draw_box(5, 3.6, 2.5, 1.0,
             'Clinical practice\nguidelines\n(n = 22)',
             '#E8F5E9', '#2E7D32', 8)
    draw_box(7, 3.6, 2.5, 1.0,
             'Peer-reviewed\narticles\n(n = 28)',
             '#FFF3E0', '#E65100', 8)

    # Disease areas
    areas = ['Asthma\n(n=12)', 'ADHD\n(n=9)', 'Diabetes/\nGLP-1 (n=11)',
             'Hypogonadism\n(n=10)', 'Glucocorticoids\n(n=9)',
             'CV Disease\n(n=8)', 'PCOS/\nFertility (n=9)']
    for i, area in enumerate(areas):
        x = 1.5 + i * 1.15
        draw_box(x, 2.0, 1.0, 0.9, area, '#E0E0E0', '#757575', 6.5)

    ax.text(5, 1.2, 'Disease Areas Mapped', ha='center', va='center',
            fontsize=9, fontweight='bold', color=COLORS['medium_gray'])

    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/fig1_prisma_flowchart.png', dpi=300,
                bbox_inches='tight', facecolor='white')
    plt.savefig(f'{OUTPUT_DIR}/fig1_prisma_flowchart.tif', dpi=300,
                bbox_inches='tight', facecolor='white')
    plt.close()
    print("Figure 1 done: PRISMA-ScR Flow Diagram")


def fig2_gap_heatmap():
    """Figure 2: Clinical-Competition Gap Risk Heatmap."""
    fig, ax = plt.subplots(figsize=(12, 7))

    diseases = [
        'Asthma\n(Beta-2 agonists)',
        'ADHD\n(Stimulants)',
        'Type 2 Diabetes\n(GLP-1 RAs)',
        'Male Hypogonadism\n(Testosterone)',
        'Glucocorticoids\n(Intra-articular)',
        'Cardiovascular\n(Diuretics/BB)',
        'PCOS/Fertility\n(Letrozole/Clomiphene)'
    ]

    dimensions = [
        'First-line Rx\nProhibited',
        'TUE Process\nComplexity',
        'Guideline\nUpdate Lag',
        'Athlete\nImpact',
        'Alternative Rx\nAvailability'
    ]

    # Risk scores (0-4: 0=no gap, 1=low, 2=medium, 3=high, 4=very high)
    data = np.array([
        [2, 2, 2, 3, 4],  # Asthma
        [4, 4, 2, 4, 2],  # ADHD
        [1, 2, 3, 3, 3],  # T2DM/GLP-1
        [4, 4, 3, 4, 1],  # Hypogonadism
        [3, 2, 2, 3, 3],  # Glucocorticoids
        [3, 3, 3, 3, 2],  # CV
        [4, 3, 2, 3, 1],  # PCOS
    ])

    cmap = matplotlib.colors.LinearSegmentedColormap.from_list(
        'gap_risk', ['#E8F5E9', '#FFF9C4', '#FFE0B2', '#FFCDD2', '#EF5350'])

    im = ax.imshow(data, cmap=cmap, aspect='auto', vmin=0, vmax=4)

    ax.set_xticks(range(len(dimensions)))
    ax.set_xticklabels(dimensions, fontsize=9, ha='center')
    ax.set_yticks(range(len(diseases)))
    ax.set_yticklabels(diseases, fontsize=9)

    ax.tick_params(top=True, bottom=False, labeltop=True, labelbottom=False)

    # Add text annotations
    risk_labels = {0: 'None', 1: 'Low', 2: 'Med', 3: 'High', 4: 'V.High'}
    for i in range(len(diseases)):
        for j in range(len(dimensions)):
            val = data[i, j]
            color = 'white' if val >= 3 else COLORS['dark_gray']
            ax.text(j, i, risk_labels[val], ha='center', va='center',
                    fontsize=9, fontweight='bold', color=color)

    # Colorbar
    cbar = plt.colorbar(im, ax=ax, fraction=0.03, pad=0.04)
    cbar.set_ticks([0, 1, 2, 3, 4])
    cbar.set_ticklabels(['None', 'Low', 'Medium', 'High', 'Very High'])
    cbar.set_label('Gap Severity', fontsize=10)

    ax.set_title('Figure 2. Clinical-Competition Gap Risk Matrix\n'
                 'by Disease Area and Assessment Dimension',
                 fontsize=13, fontweight='bold', color=COLORS['wada_blue'],
                 pad=60)

    # Grid
    for i in range(len(diseases) + 1):
        ax.axhline(i - 0.5, color='white', linewidth=2)
    for j in range(len(dimensions) + 1):
        ax.axvline(j - 0.5, color='white', linewidth=2)

    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/fig2_gap_heatmap.png', dpi=300,
                bbox_inches='tight', facecolor='white')
    plt.savefig(f'{OUTPUT_DIR}/fig2_gap_heatmap.tif', dpi=300,
                bbox_inches='tight', facecolor='white')
    plt.close()
    print("Figure 2 done: Gap Risk Heatmap")


def fig3_timeline_comparison():
    """Figure 3: Timeline comparison of guideline updates vs WADA updates."""
    fig, ax = plt.subplots(figsize=(14, 6))

    # Timeline data: (year, month_approx, label, type)
    wada_events = [
        (2022, 1, 'GC intra-articular\nprohibited IC', '#1565C0'),
        (2023, 10, 'Diabetes TUE\nGuideline v5.1', '#1565C0'),
        (2023, 10, 'CV TUE\nGuideline v4.0', '#1976D2'),
        (2024, 1, 'GLP-1 RA\nMonitoring', '#1565C0'),
        (2025, 1, 'PCOS TUE\nGuideline v2.0', '#1976D2'),
        (2025, 12, 'Hypogonadism\nTUE update', '#1565C0'),
        (2026, 1, 'Asthma TUE\nv9.3', '#1976D2'),
        (2026, 1, 'ADHD TUE\nv8.0', '#1565C0'),
    ]

    clinical_events = [
        (2018, 6, 'Endocrine Soc.\nTestosterone GL', '#2E7D32'),
        (2022, 1, 'Australian\nADHD GL', '#388E3C'),
        (2023, 6, 'PCOS Intl.\nGL revised', '#2E7D32'),
        (2023, 8, 'TRAVERSE trial\n(TRT safety)', '#388E3C'),
        (2023, 10, 'ESC/ESH\nHypertension GL', '#2E7D32'),
        (2024, 1, 'EAU Sexual/\nReprod. Health', '#388E3C'),
        (2024, 6, 'NICE ADHD\nGL update', '#2E7D32'),
        (2025, 1, 'ADA Diabetes\nStandards 2025', '#388E3C'),
        (2025, 5, 'GINA 2025\nAsthma Strategy', '#2E7D32'),
        (2025, 6, 'ESC Heart\nFailure GL', '#388E3C'),
    ]

    years = np.arange(2018, 2027)
    ax.set_xlim(2017.5, 2026.8)
    ax.set_ylim(-3.5, 3.5)

    # Central timeline
    ax.axhline(0, color=COLORS['dark_gray'], linewidth=2, zorder=1)
    for y in years:
        ax.plot(y, 0, 'o', color=COLORS['dark_gray'], markersize=6, zorder=2)
        ax.text(y, -0.3, str(y), ha='center', va='top', fontsize=9,
                fontweight='bold', color=COLORS['dark_gray'])

    # WADA events (above)
    for i, (year, month, label, color) in enumerate(wada_events):
        x = year + month / 12
        y_pos = 1.0 + (i % 3) * 0.85
        ax.plot(x, 0, 'v', color=color, markersize=8, zorder=3)
        ax.plot([x, x], [0.1, y_pos - 0.2], color=color, linewidth=1,
                linestyle='--', alpha=0.5)
        ax.text(x, y_pos, label, ha='center', va='center', fontsize=7,
                bbox=dict(boxstyle='round,pad=0.3', facecolor='#E3F2FD',
                          edgecolor=color, alpha=0.9))

    # Clinical events (below)
    for i, (year, month, label, color) in enumerate(clinical_events):
        x = year + month / 12
        y_pos = -1.0 - (i % 3) * 0.85
        ax.plot(x, 0, '^', color=color, markersize=8, zorder=3)
        ax.plot([x, x], [-0.1, y_pos + 0.2], color=color, linewidth=1,
                linestyle='--', alpha=0.5)
        ax.text(x, y_pos, label, ha='center', va='center', fontsize=7,
                bbox=dict(boxstyle='round,pad=0.3', facecolor='#E8F5E9',
                          edgecolor=color, alpha=0.9))

    # Labels
    ax.text(2017.7, 2.8, 'WADA\nRegulatory\nUpdates',
            ha='center', va='center', fontsize=10, fontweight='bold',
            color=COLORS['wada_blue'])
    ax.text(2017.7, -2.8, 'Clinical\nGuideline\nUpdates',
            ha='center', va='center', fontsize=10, fontweight='bold',
            color=COLORS['clinical_green'])

    # Gap arrows
    ax.annotate('', xy=(2025.2, 0.3), xytext=(2025.2, -0.3),
                arrowprops=dict(arrowstyle='<->', color=COLORS['gap_red'],
                                lw=2.5))
    ax.text(2025.6, 0, 'GAP', ha='left', va='center', fontsize=10,
            fontweight='bold', color=COLORS['gap_red'])

    ax.set_title('Figure 3. Timeline of Clinical Guideline Updates vs. '
                 'WADA TUE Regulatory Changes (2018-2026)',
                 fontsize=12, fontweight='bold', color=COLORS['wada_blue'],
                 pad=15)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.set_yticks([])

    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/fig3_timeline.png', dpi=300,
                bbox_inches='tight', facecolor='white')
    plt.savefig(f'{OUTPUT_DIR}/fig3_timeline.tif', dpi=300,
                bbox_inches='tight', facecolor='white')
    plt.close()
    print("Figure 3 done: Timeline Comparison")


def fig4_conceptual_framework():
    """Figure 4: Conceptual framework - Clinical-Competition Gap Model (for BJSM)."""
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    fig.patch.set_facecolor('white')

    def draw_rounded_box(x, y, w, h, text, facecolor, edgecolor, fontsize=9,
                         fontweight='normal', text_color='black'):
        box = FancyBboxPatch((x, y), w, h,
                             boxstyle="round,pad=0.2",
                             facecolor=facecolor, edgecolor=edgecolor,
                             linewidth=2)
        ax.add_patch(box)
        ax.text(x + w/2, y + h/2, text, ha='center', va='center',
                fontsize=fontsize, fontweight=fontweight, color=text_color,
                wrap=True)

    def draw_arrow_between(x1, y1, x2, y2, color='#424242', style='->', lw=1.5):
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle=style, color=color, lw=lw))

    # Title
    ax.text(5, 9.7, 'Figure 4. Conceptual Framework:\n'
            'The Clinical-Competition Gap in Anti-Doping',
            ha='center', va='center', fontsize=13, fontweight='bold',
            color=COLORS['wada_blue'])

    # LEFT: Clinical Practice
    draw_rounded_box(0.3, 7.5, 3.5, 1.2,
                     'CLINICAL PRACTICE\nGUIDELINES',
                     '#E8F5E9', '#2E7D32', 11, 'bold', '#1B5E20')
    # Sub-items
    items_left = ['GINA (Asthma)', 'ADA (Diabetes)', 'Endocrine Society',
                  'ESC (Cardiology)', 'NICE (ADHD)']
    for i, item in enumerate(items_left):
        ax.text(2.05, 7.3 - i * 0.35, f'  {item}', ha='center', va='center',
                fontsize=7.5, color='#2E7D32')

    # RIGHT: WADA Regulations
    draw_rounded_box(6.2, 7.5, 3.5, 1.2,
                     'WADA ANTI-DOPING\nREGULATIONS',
                     '#E3F2FD', '#1565C0', 11, 'bold', '#0D47A1')
    items_right = ['Prohibited List', 'ISTUE Standards', 'TUE Physician GL',
                   'Monitoring Program', 'ADAMS System']
    for i, item in enumerate(items_right):
        ax.text(7.95, 7.3 - i * 0.35, f'  {item}', ha='center', va='center',
                fontsize=7.5, color='#1565C0')

    # CENTER GAP
    draw_rounded_box(3.0, 4.5, 4.0, 1.5,
                     'CLINICAL-COMPETITION\nGAP',
                     '#FFEBEE', '#C62828', 13, 'bold', '#B71C1C')

    # Gap components
    gap_items = [
        'Update timing lag',
        'Divergent criteria',
        'Prohibited first-line Rx',
        'TUE process barriers'
    ]
    for i, item in enumerate(gap_items):
        ax.text(5, 4.3 - i * 0.3, f'  {item}', ha='center', va='center',
                fontsize=8, color='#C62828')

    # Arrows from top to center
    draw_arrow_between(2.05, 5.5, 4.0, 5.5, '#2E7D32', '->', 2)
    draw_arrow_between(7.95, 5.5, 6.0, 5.5, '#1565C0', '->', 2)

    ax.text(3.0, 5.7, 'Evidence-based\nrecommendations', ha='center',
            va='bottom', fontsize=7.5, color='#2E7D32', style='italic')
    ax.text(7.0, 5.7, 'Regulatory\nrestrictions', ha='center',
            va='bottom', fontsize=7.5, color='#1565C0', style='italic')

    # BOTTOM: Impact on Athletes
    draw_arrow_between(5, 4.5, 5, 3.5, '#C62828', '->', 2.5)

    draw_rounded_box(1.5, 1.5, 7.0, 1.8,
                     'IMPACT ON ATHLETES',
                     '#FFF3E0', '#E65100', 11, 'bold', '#BF360C')

    impact_items = [
        'Suboptimal treatment  |  Delayed care access  |  ADRV risk',
        'Privacy concerns  |  Geographic disparities  |  Career impact'
    ]
    for i, item in enumerate(impact_items):
        ax.text(5, 2.5 - i * 0.4, item, ha='center', va='center',
                fontsize=8, color='#BF360C')

    # BOTTOM: Recommendations arrow
    draw_arrow_between(5, 1.5, 5, 0.8, '#E65100', '->', 2)
    draw_rounded_box(2.0, 0.1, 6.0, 0.6,
                     'RECOMMENDATIONS: Harmonize updates | Streamline TUE | Educate clinicians',
                     '#E0E0E0', '#757575', 8, 'bold', '#424242')

    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/fig4_conceptual_framework.png', dpi=300,
                bbox_inches='tight', facecolor='white')
    plt.savefig(f'{OUTPUT_DIR}/fig4_conceptual_framework.tif', dpi=300,
                bbox_inches='tight', facecolor='white')
    plt.close()
    print("Figure 4 done: Conceptual Framework")


def fig5_disease_summary_bar():
    """Figure 5: Summary bar chart of gap severity by disease area."""
    fig, ax = plt.subplots(figsize=(11, 6))

    diseases = [
        'Male\nHypogonadism', 'ADHD', 'PCOS/\nFertility',
        'Cardiovascular', 'Glucocorticoids', 'Asthma',
        'Type 2 Diabetes\n/ GLP-1 RA'
    ]

    # Composite scores for each dimension
    first_line = [4, 4, 4, 3, 3, 2, 1]
    tue_complex = [4, 4, 3, 3, 2, 2, 2]
    update_lag = [3, 2, 2, 3, 2, 2, 3]
    athlete_impact = [4, 4, 3, 3, 3, 3, 3]

    x = np.arange(len(diseases))
    width = 0.2

    bars1 = ax.bar(x - 1.5*width, first_line, width,
                   label='First-line Rx Prohibited', color='#EF5350', edgecolor='white')
    bars2 = ax.bar(x - 0.5*width, tue_complex, width,
                   label='TUE Process Complexity', color='#FF9800', edgecolor='white')
    bars3 = ax.bar(x + 0.5*width, update_lag, width,
                   label='Guideline Update Lag', color='#FDD835', edgecolor='white')
    bars4 = ax.bar(x + 1.5*width, athlete_impact, width,
                   label='Athlete Impact', color='#42A5F5', edgecolor='white')

    ax.set_xlabel('Disease Area', fontsize=11, fontweight='bold')
    ax.set_ylabel('Gap Severity Score (0-4)', fontsize=11, fontweight='bold')
    ax.set_title('Figure 5. Clinical-Competition Gap Severity by Disease Area\n'
                 'and Assessment Dimension',
                 fontsize=13, fontweight='bold', color=COLORS['wada_blue'])

    ax.set_xticks(x)
    ax.set_xticklabels(diseases, fontsize=9)
    ax.set_yticks([0, 1, 2, 3, 4])
    ax.set_yticklabels(['None', 'Low', 'Medium', 'High', 'Very High'], fontsize=9)
    ax.set_ylim(0, 4.8)
    ax.legend(loc='upper right', fontsize=8, framealpha=0.9)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.grid(axis='y', alpha=0.3)

    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/fig5_severity_bar.png', dpi=300,
                bbox_inches='tight', facecolor='white')
    plt.savefig(f'{OUTPUT_DIR}/fig5_severity_bar.tif', dpi=300,
                bbox_inches='tight', facecolor='white')
    plt.close()
    print("Figure 5 done: Severity Bar Chart")


# Generate all figures
if __name__ == '__main__':
    fig1_prisma_flowchart()
    fig2_gap_heatmap()
    fig3_timeline_comparison()
    fig4_conceptual_framework()
    fig5_disease_summary_bar()
    print(f"\nAll figures saved to {OUTPUT_DIR}/")
    for f in sorted(os.listdir(OUTPUT_DIR)):
        print(f"  {f}")
