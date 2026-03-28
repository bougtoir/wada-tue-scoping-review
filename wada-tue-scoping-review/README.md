# WADA TUE vs Clinical Guidelines — Scoping Review

A scoping review examining discrepancies between WADA Therapeutic Use Exemption (TUE) regulations and current evidence-based clinical practice guidelines across seven major disease areas.

## Manuscripts

| Target Journal | Type | Files |
|---|---|---|
| **BJSM** (British Journal of Sports Medicine) | Viewpoint (~1,500 words) | `manuscripts/BJSM_Viewpoint_English.docx`, `manuscripts/BJSM_Viewpoint_Japanese.docx` |
| **SCJ** (Strength and Conditioning Journal) | Full Narrative Review (~6,200 words, PRISMA-ScR) | `manuscripts/SCJ_Narrative_Review_English.docx`, `manuscripts/SCJ_Narrative_Review_Japanese.docx` |

## Figures

All figures are in `figures/` (PNG + TIFF). PowerPoint presentations with one figure per slide are in `presentations/`.

| Figure | Description |
|---|---|
| Fig 1 | PRISMA-ScR Flow Diagram |
| Fig 2 | Clinical-Competition Gap Risk Matrix (Heatmap) |
| Fig 3 | Timeline: Clinical Guidelines vs WADA Regulatory Changes (2018-2026) |
| Fig 4 | Conceptual Framework: The Clinical-Competition Gap |
| Fig 5 | Clinical-Competition Gap Severity by Disease Area |

## Project Structure

```
wada-tue-scoping-review/
├── manuscripts/          # Final .docx manuscripts (EN + JP)
├── figures/              # PNG and TIFF figure files
├── presentations/        # PowerPoint figure presentations (EN + JP)
├── src/                  # Python build scripts
│   ├── create_figures.py
│   ├── create_figures_pptx.py
│   ├── create_bjsm_viewpoint.py
│   ├── build_scj_en.py
│   ├── build_scj_jp.py
│   ├── scj_en_content.py
│   ├── scj_jp_content.py
│   ├── create_scj_review_part1.py
│   └── renumber_citations.py
└── reports/              # Background research reports
    ├── WADA_TUE_vs_Clinical_Guidelines_Report.md
    └── WADA_TUE_Target_Journals.md
```

## Author

[Author Name], MD, CSCS

## Format

- Double-spaced, Times New Roman 12pt, 2.54 cm margins
- Color figures embedded
- PRISMA-ScR compliant (SCJ manuscript)
