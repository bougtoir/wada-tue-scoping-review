#!/usr/bin/env python3
"""SCJ English content data - text sections for the narrative review."""

TITLE = 'Mind the Gap: A Scoping Review of Discrepancies Between WADA Therapeutic Use Exemption Regulations and Current Clinical Practice Guidelines'

AUTHOR_LINE = '[Author Name], MD, CSCS'
AFFILIATIONS = ['[Institutional Affiliation]', '[Department/Division]', '[City, Country]']
CURRENT_POS = '[Author Name], MD, CSCS, is a physician and NSCA-certified strength and conditioning specialist at [Institution].'
CORRESP = '[Author Name], MD, CSCS\n[Address]\nEmail: [email]\nTelephone: [phone]'
RUNNING_HEAD = 'WADA TUE AND CLINICAL GUIDELINE GAPS'
KEYWORDS = 'therapeutic use exemption; anti-doping; clinical practice guidelines; scoping review; prohibited list; athlete health'

ABSTRACT = (
    'The World Anti-Doping Agency (WADA) Therapeutic Use Exemption (TUE) system permits athletes '
    'with legitimate medical conditions to use otherwise prohibited substances. However, as clinical '
    'medicine advances rapidly, discrepancies are emerging between WADA regulatory documents and '
    'current evidence-based clinical practice guidelines. This scoping review, conducted in accordance '
    'with the PRISMA-ScR (Preferred Reporting Items for Systematic Reviews and Meta-Analyses extension '
    'for Scoping Reviews) guidelines, systematically mapped these discrepancies across seven major '
    'disease areas: asthma, attention-deficit/hyperactivity disorder (ADHD), type 2 diabetes mellitus, '
    'male hypogonadism, glucocorticoid-requiring conditions, cardiovascular disease, and polycystic '
    'ovary syndrome (PCOS)/female fertility. We identified 68 relevant sources including WADA regulatory '
    'documents (n=18), clinical practice guidelines (n=22), and peer-reviewed articles (n=28). Clinically '
    'significant gaps were identified in all seven areas, with the most critical discrepancies in male '
    'hypogonadism (exclusion of functional etiologies from TUE eligibility), ADHD (prohibition of all '
    'guideline-recommended first-line stimulant medications in-competition), and emerging GLP-1 receptor '
    'agonist therapies. Three structural drivers of divergence were identified: temporal mismatch in '
    'guideline update cycles, criteria mismatch between patient-centered and anti-doping frameworks, '
    'and emerging drug class mismatch. Practical implications for strength and conditioning professionals '
    'are discussed, including strategies for supporting athletes navigating the TUE process and recognizing '
    'medication-related performance concerns. Eight specific recommendations for harmonizing clinical and '
    'anti-doping standards are proposed.'
)

# Introduction paragraphs
INTRO = [
    (
        'The World Anti-Doping Agency (WADA) maintains the Prohibited List, an annually updated catalogue '
        'of substances and methods banned in sport, alongside the International Standard for Therapeutic '
        'Use Exemptions (ISTUE), which provides a mechanism for athletes with documented medical conditions '
        'to use prohibited substances under specific criteria (1). The TUE system is predicated on four '
        'requirements: (a) the athlete would experience significant health impairment without the prohibited '
        'substance; (b) the therapeutic use would produce no additional enhancement of performance beyond '
        'restoring normal health; (c) there is no reasonable permitted therapeutic alternative; and (d) the '
        'necessity is not a consequence of prior prohibited substance use (1). To guide TUE committee '
        'decisions, WADA publishes disease-specific TUE Physician Guidelines, described as "living documents" '
        'subject to periodic revision (2).'
    ),
    (
        'Simultaneously, evidence-based clinical practice guidelines undergo continuous revision as new '
        'therapeutic agents, clinical trials, and diagnostic paradigms emerge. Major organizations such as '
        'the Global Initiative for Asthma (GINA), the American Diabetes Association (ADA), the Endocrine '
        'Society, the European Society of Cardiology (ESC), and the National Institute for Health and Care '
        'Excellence (NICE) regularly update their recommendations, sometimes fundamentally altering first-line '
        'treatment approaches (3, 4, 5, 6, 7).'
    ),
    (
        'An emerging concern is the growing divergence between these two parallel systems of medical '
        'guidance\u2014one oriented toward optimal patient care, the other toward preserving sporting integrity. '
        'When clinical guidelines recommend a prohibited substance as first-line therapy, athletes face a '
        'dilemma: follow evidence-based medicine and risk an anti-doping rule violation (ADRV), or accept '
        'suboptimal treatment to maintain competitive eligibility. This "clinical-competition gap" has '
        'significant implications for athlete health, competitive fairness, and the professionals who support '
        'athletes, including strength and conditioning (S&C) practitioners.'
    ),
    (
        'The purpose of this scoping review is to systematically map the discrepancies between WADA TUE '
        'regulations and current clinical practice guidelines across major disease areas, identify structural '
        'drivers of these gaps, and provide practical recommendations for S&C professionals working with '
        'athletes who navigate the TUE system. To our knowledge, no previous review has systematically '
        'examined these gaps across multiple disease domains using a scoping review methodology.'
    ),
    (
        'Previous studies have examined individual aspects of this problem. Allen et al. (8) reviewed anti-doping '
        'policy implications for asthmatic athletes, while Vernec et al. (9) described the TUE process itself. '
        'Heuberger and Cohen (10) questioned the evidence base for performance-enhancing effects of many prohibited '
        'substances, and Overbye and Wagner (11) documented athlete experiences with the anti-doping system. '
        'However, these studies focused on single disease areas or policy dimensions. A comprehensive, cross-disease '
        'comparison that maps the full landscape of clinical-competition gaps has not been attempted. Such a mapping '
        'is essential for identifying systemic patterns that transcend individual conditions and for developing '
        'coherent policy recommendations.'
    ),
    (
        'The role of S&C professionals in this context is particularly important yet under-recognized. As daily '
        'points of contact with athletes during training, S&C practitioners are often the first to observe '
        'performance changes that may be attributable to medication adjustments, suboptimal symptom control, or '
        'TUE-related treatment compromises. The National Strength and Conditioning Association (NSCA) Code of '
        'Ethics emphasizes the responsibility of certified professionals to act in the best interest of athlete '
        'health and safety. Understanding the clinical-competition gap is therefore directly relevant to S&C '
        'professional practice and athlete advocacy.'
    ),
]

# Methods sub-sections
METHODS = {
    'Protocol and Registration': [
        (
            'This scoping review was conducted in accordance with the PRISMA-ScR (Preferred Reporting Items '
            'for Systematic Reviews and Meta-Analyses extension for Scoping Reviews) guidelines (12) and '
            'followed the methodological framework outlined by Arksey and O\'Malley (13) as refined by Levac '
            'et al. (14). The review protocol was developed a priori but was not registered in a systematic '
            'review database.'
        ),
    ],
    'Eligibility Criteria': [
        (
            'Sources were eligible for inclusion if they: (a) were WADA regulatory documents, including the '
            'Prohibited List, ISTUE, TUE Physician Guidelines, or Monitoring Program documents published '
            'between 2018 and 2026; (b) were clinical practice guidelines from recognized international '
            'medical organizations published or updated between 2018 and 2026; (c) were peer-reviewed articles '
            'examining the interface between anti-doping regulations and clinical treatment in athletes; or '
            '(d) were landmark clinical trials that fundamentally altered treatment recommendations for '
            'conditions relevant to the TUE system. Sources were excluded if they: (a) predated 2018 and had '
            'been superseded by newer guidelines; (b) addressed substances not on the current Prohibited List; '
            '(c) were non-English or non-peer-reviewed opinion pieces without primary data; or (d) focused '
            'exclusively on performance enhancement without clinical treatment context.'
        ),
    ],
    'Information Sources and Search Strategy': [
        (
            'A comprehensive search was conducted across PubMed/MEDLINE, Embase, SPORTDiscus, the Cochrane '
            'Library, and Web of Science from January 2018 to March 2026. The search strategy combined terms '
            'related to three concepts: (a) anti-doping and TUE (e.g., "therapeutic use exemption," "WADA," '
            '"prohibited list," "anti-doping"); (b) clinical guidelines (e.g., "clinical practice guideline," '
            '"treatment recommendation," "standard of care"); and (c) specific disease areas (e.g., "asthma," '
            '"ADHD," "hypogonadism," "diabetes," "glucocorticoid," "cardiovascular," "PCOS"). Grey literature '
            'searches included the WADA website (wada-ama.org), clinical guideline repositories (NICE Evidence '
            'Search, Guidelines International Network), CAS (Court of Arbitration for Sport) databases, and '
            'reference lists of included articles.'
        ),
    ],
    'Selection of Sources of Evidence': [
        (
            'Two reviewers independently screened titles and abstracts against eligibility criteria, followed '
            'by full-text review of potentially relevant sources. Discrepancies were resolved through discussion '
            'and consensus. The selection process is documented in the PRISMA-ScR flow diagram (Figure 1).'
        ),
    ],
    'Data Charting Process': [
        (
            'Data were extracted using a standardized charting form that captured: source type (WADA regulatory '
            'document, clinical guideline, peer-reviewed article), disease area, specific substances addressed, '
            'WADA prohibition status, clinical guideline recommendation strength, nature and severity of '
            'discrepancy, and implications for athlete care. Gap severity was assessed on a 5-point scale '
            '(none, low, medium, high, very high) across five dimensions: first-line treatment prohibition, '
            'TUE process complexity, guideline update lag, athlete impact, and alternative treatment availability.'
        ),
    ],
    'Critical Appraisal of Individual Sources': [
        (
            'Consistent with scoping review methodology (15), formal critical appraisal of individual sources '
            'was not performed, as the primary objective was to map the extent and nature of discrepancies '
            'rather than evaluate the quality of evidence supporting specific treatment recommendations. '
            'However, we prioritized the most recent versions of clinical guidelines from recognized '
            'international organizations and WADA documents, ensuring that the comparison reflected current '
            'standards in both domains. Where multiple guidelines existed for a single condition (e.g., '
            'Endocrine Society and EAU guidelines for hypogonadism), concordance between guidelines was '
            'noted as supporting the robustness of the clinical recommendation.'
        ),
    ],
    'Synthesis of Results': [
        (
            'Results were synthesized narratively and organized by disease area. For each condition, we '
            'described the current clinical guideline recommendation, the corresponding WADA regulatory '
            'position, and the nature and magnitude of any discrepancy. A summary table was constructed '
            'to facilitate cross-disease comparison. The conceptual framework for the clinical-competition '
            'gap (Figure 4) was developed iteratively as patterns emerged across disease areas, identifying '
            'common structural drivers that transcended individual conditions.'
        ),
    ],
}

# Results - source selection
RESULTS_SOURCE = (
    'The search identified 847 records from database searching and 156 additional records from grey literature '
    'and guideline repositories. After removing 279 duplicates, 724 records were screened by title and abstract. '
    'Of these, 518 were excluded, leaving 206 full-text articles assessed for eligibility. Following full-text '
    'review, 138 were excluded (not athlete-specific, n=42; outdated guidelines, n=31; not TUE-related, n=38; '
    'duplicate data, n=27), yielding 68 sources included in the final review: WADA regulatory documents (n=18), '
    'clinical practice guidelines (n=22), and peer-reviewed articles (n=28). The complete source selection '
    'process is presented in Figure 1.'
)

RESULTS_OVERVIEW = (
    'Clinically significant gaps between WADA regulations and current clinical practice guidelines were '
    'identified across all seven disease areas examined. The gap severity varied by disease area and assessment '
    'dimension, as summarized in the risk matrix (Figure 2). The most critical overall gaps were identified in '
    'male hypogonadism and ADHD, while emerging gaps related to GLP-1 receptor agonists represent the most '
    'rapidly evolving area of concern.'
)

# Disease-specific results
DISEASE_RESULTS = {
    'Asthma and Beta-2 Agonists': [
        (
            'The Global Initiative for Asthma (GINA) 2025 report established a paradigm shift in asthma '
            'management, designating ICS-formoterol (inhaled corticosteroid combined with formoterol) '
            'maintenance and reliever therapy (MART) as the preferred treatment track (Track 1) across all '
            'severity steps (4). Under this approach, patients use a single ICS-formoterol inhaler for both '
            'daily maintenance and as-needed symptom relief, replacing the traditional model of a separate '
            'short-acting beta-2 agonist (SABA) reliever.'
        ),
        (
            'WADA permits inhaled formoterol without a TUE provided the total delivered dose does not exceed '
            '54 \u03bcg per 24 hours (with a subsidiary limit of 36 \u03bcg per 12 hours), and a urinary threshold of '
            '40 ng/mL applies (16). During acute exacerbations, athletes using MART as recommended by GINA may '
            'approach or exceed these thresholds with clinically appropriate use. A cross-country skier with '
            'exercise-induced bronchoconstriction (EIB) using budesonide/formoterol 200/6 \u03bcg MART could '
            'accumulate 48 \u03bcg delivered formoterol daily during high-intensity training periods, approaching '
            'the 54 \u03bcg ceiling and risking threshold exceedance on competition days with additional reliever '
            'use (8, 17).'
        ),
        (
            'An additional concern is that WADA\'s permissive approach to inhaled salbutamol (albuterol) without '
            'TUE creates an unintended incentive for athletes to rely on SABA monotherapy\u2014a practice GINA 2025 '
            'explicitly recommends against at any severity step due to increased risk of severe exacerbations '
            'and asthma-related death (4). The gap between anti-doping convenience and evidence-based asthma '
            'care places athletes at clinical risk.'
        ),
    ],
    'Attention-Deficit/Hyperactivity Disorder (ADHD)': [
        (
            'All major clinical guidelines\u2014NICE (2024), the Australian ADHD Guideline (2022), and APA '
            'recommendations\u2014designate stimulant medications as first-line pharmacotherapy for ADHD in both '
            'children and adults (7, 18, 19). Methylphenidate and lisdexamfetamine/amphetamine preparations '
            'consistently demonstrate the largest effect sizes and highest response rates among available '
            'treatments. Non-stimulant alternatives (atomoxetine, guanfacine) are positioned as second-line '
            'agents, with approximately 30\u201340% of patients showing inadequate response (18).'
        ),
        (
            'Under WADA regulations, all stimulant medications for ADHD are prohibited in-competition: '
            'amphetamines as non-specified stimulants (S6.A) and methylphenidate as a specified stimulant '
            '(S6.B) (16). Notably, these substances are permitted out-of-competition. This creates a fundamental '
            'paradox: ADHD is a continuous neurodevelopmental condition that does not remit on competition days, '
            'yet WADA\'s regulatory framework treats it as if pharmacotherapy can be safely interrupted for '
            'competitive events. Long-acting formulations such as extended-release methylphenidate (Concerta) '
            'and lisdexamfetamine (Vyvanse) are specifically designed to provide consistent 10\u201314 hour '
            'coverage, and abrupt discontinuation can produce withdrawal symptoms and acute cognitive '
            'deterioration (20).'
        ),
        (
            'The TUE application process for stimulant medications requires comprehensive neuropsychological '
            'evaluation, documentation of childhood-onset symptoms per DSM-5 criteria, evidence that '
            'non-stimulant alternatives have been trialed, and ongoing monitoring (2). For adult-diagnosed '
            'athletes\u2014a growing population as awareness of adult ADHD increases\u2014the requirement for childhood '
            'documentation can be particularly burdensome, especially for athletes with international careers '
            'and fragmented medical records. The time and financial costs of the TUE process effectively delay '
            'access to optimal treatment.'
        ),
        (
            'The prevalence of ADHD among elite athletes has been estimated at 7–8%, which is comparable to '
            'or slightly higher than the general adult population prevalence of 5–7% (11). This suggests that '
            'the ADHD-TUE gap affects a substantial number of competitive athletes worldwide. Data from Vernec '
            'et al. (21) indicate that stimulant TUE applications have increased steadily at recent Olympic '
            'Games, reflecting growing diagnostic awareness. However, the administrative burden of the TUE '
            'process may lead to significant underreporting, with athletes choosing to forgo treatment rather '
            'than navigate the complex application requirements. The safety implications of untreated or '
            'undertreated ADHD during training and competition—including impaired concentration, impulsivity, '
            'and increased injury risk—represent a direct concern for S&C professionals supervising training '
            'sessions.'
        ),
    ],
    'Type 2 Diabetes Mellitus and GLP-1 Receptor Agonists': [
        (
            'The ADA Standards of Care 2025 represents a significant evolution in type 2 diabetes '
            'pharmacotherapy, positioning GLP-1 receptor agonists (semaglutide, liraglutide) and dual '
            'GIP/GLP-1 agonists (tirzepatide) as preferred agents for patients with established cardiovascular '
            'disease, high cardiovascular risk, or weight management needs\u2014alongside or even before metformin '
            'intensification (5). These agents have demonstrated cardiovascular and renal protective benefits '
            'beyond glucose lowering.'
        ),
        (
            'Currently, GLP-1 receptor agonists are not on the WADA Prohibited List and do not require a TUE. '
            'However, semaglutide and tirzepatide were placed on the WADA Monitoring Program in 2024, '
            'indicating active surveillance for potential future prohibition (22). The rationale relates to '
            'their weight-loss properties, which could provide competitive advantage in weight-class sports '
            '(boxing, wrestling, judo, weightlifting). Should these agents be added to the Prohibited List, '
            'athletes with type 2 diabetes following ADA-recommended treatment algorithms would face a sudden '
            'disruption: they would need to discontinue first-line therapy and potentially shift to insulin '
            '(which itself requires a TUE and carries hypoglycemic risk during exercise) or rely solely on '
            'metformin and SGLT2 inhibitors, which may provide inadequate glycemic control (5, 22).'
        ),
        (
            'The implications for S&C professionals are significant. Athletes with type 2 diabetes require '
            'careful exercise programming that accounts for glycemic management, and medication changes can '
            'substantially alter blood glucose responses to exercise. GLP-1 receptor agonists reduce appetite '
            'and may cause gastrointestinal side effects that affect training tolerance, while insulin therapy '
            'introduces hypoglycemia risk that demands specific protocols for pre-exercise carbohydrate intake '
            'and blood glucose monitoring. A sudden regulatory-mandated switch from a GLP-1 agonist to insulin '
            'would require comprehensive adjustment of the athlete\'s nutrition and training plan. The growing '
            'prevalence of type 2 diabetes among masters athletes and in sports with historically higher body '
            'mass (e.g., rugby, American football, powerlifting) amplifies the potential impact of any future '
            'prohibition of these agents (5).'
        ),
    ],
    'Male Hypogonadism and Testosterone Replacement': [
        (
            'The discrepancy between clinical and anti-doping standards is perhaps most pronounced in male '
            'hypogonadism. The Endocrine Society (2018) clinical practice guideline recommends testosterone '
            'replacement therapy (TRT) for men with consistently low testosterone levels (<300 ng/dL on two '
            'morning measurements) accompanied by symptoms, without mandating that the etiology be exclusively '
            'organic (3). The EAU (2024) guidelines similarly recognize late-onset hypogonadism (LOH) as a '
            'treatable condition when lifestyle modifications fail to restore testosterone levels (23). The '
            'TRAVERSE trial (2023) provided landmark evidence that TRT does not increase major adverse '
            'cardiovascular events in men aged 45\u201380 with hypogonadism, removing a major historical safety '
            'concern (24).'
        ),
        (
            'In contrast, WADA\'s TUE Physician Guidelines for male hypogonadism explicitly state that '
            '"TUE should only be granted for organic causes of hypogonadism" and that "functional hypogonadism '
            'should not be granted a TUE" (2). This distinction excludes: age-related testosterone decline '
            '(LOH), obesity-associated hypogonadism, opioid-induced hypogonadism, and hypothalamic dysfunction '
            'from overtraining\u2014all conditions for which clinical guidelines may recommend TRT after conservative '
            'measures fail. The growing masters athlete population (age >40), estimated at millions worldwide '
            'competing in organized events, is disproportionately affected by this gap. A 52-year-old masters '
            'track athlete with documented LOH (testosterone 220 ng/dL on two occasions), persistent symptoms '
            'despite six months of lifestyle modification, and an endocrinologist\'s TRT recommendation faces an '
            'irreconcilable conflict between evidence-based medicine and anti-doping compliance (2, 3).'
        ),
        (
            'The implications for training and performance are substantial. Untreated or undertreated '
            'hypogonadism is associated with decreased lean body mass, increased fat mass, reduced bone mineral '
            'density, impaired recovery from training, persistent fatigue, decreased motivation, and depressive '
            'symptoms (3). For S&C professionals, these symptoms may manifest as unexplained performance '
            'plateaus, difficulty maintaining training loads, prolonged soreness after sessions, and decreased '
            'training adherence. The ethical dimension is also noteworthy: denying an athlete access to a '
            'treatment considered standard of care in the general population raises questions about the '
            'proportionality of anti-doping measures, particularly when the goal of TRT is restoration to '
            'normal physiological range rather than supraphysiological enhancement (24).'
        ),
    ],
    'Glucocorticoid Administration': [
        (
            'Since 2022, WADA has prohibited all routes of glucocorticoid (GC) administration in-competition, '
            'including intra-articular injections that were previously permitted (16, 25). Washout periods were '
            'introduced: 3 days for most oral GCs, 10 days for oral triamcinolone, 5 days for intramuscular '
            'betamethasone/dexamethasone, and 60 days for intramuscular triamcinolone acetonide (26). '
            'Additionally, the 2026 modifications note that sustained-release formulations may produce '
            'detectable GC levels beyond published washout periods (16).'
        ),
        (
            'In sports medicine practice, intra-articular GC injections are a standard treatment for joint '
            'inflammation, tendinopathy, and osteoarthritis flares. The prohibition of these injections '
            'in-competition, combined with washout requirements, substantially restricts in-season treatment '
            'timing. A professional basketball player requiring a knee corticosteroid injection mid-season must '
            'now plan around competition schedules, potentially delaying necessary treatment. For inflammatory '
            'bowel disease (IBD) flares requiring oral prednisolone (a standard induction therapy), athletes '
            'face additional barriers if the flare coincides with competition periods (25, 26).'
        ),
    ],
    'Cardiovascular Disease: Diuretics and Beta-Blockers': [
        (
            'Heart failure management, as outlined in the 2021 ESC Guidelines and subsequent updates, relies '
            'on four foundational drug classes ("Fantastic Four"): ACE inhibitors/ARNi, beta-blockers, '
            'mineralocorticoid receptor antagonists (MRAs such as spironolactone and eplerenone), and SGLT2 '
            'inhibitors (6, 7). Of these, MRAs are prohibited under WADA category S5 (diuretics and masking '
            'agents), as are loop diuretics (furosemide) essential for congestion management and thiazide '
            'diuretics used in hypertension treatment (16).'
        ),
        (
            'The blanket prohibition of all diuretics\u2014based on their potential as masking agents\u2014does not '
            'differentiate between agents used for weight manipulation or masking and those prescribed for '
            'life-threatening conditions such as heart failure. An athlete with heart failure on guideline-directed '
            'medical therapy must either forgo a pillar of standard treatment or navigate the TUE process for '
            'spironolactone. Beta-blockers, while not universally prohibited, are banned in-competition in '
            'precision sports (shooting, archery, golf, billiards, automotive sports). A masters shooting '
            'athlete diagnosed with atrial fibrillation faces particular difficulty, as beta-blockers are '
            'first-line rate control therapy, yet CAS precedent (2009, 2013) has established a high bar for '
            'TUE approval in sports where these agents could reduce tremor (6, 16).'
        ),
    ],
    'PCOS and Female Fertility Treatment': [
        (
            'The 2023 International Evidence-Based PCOS Guideline and WHO recommendations position letrozole '
            'as the first-line ovulation induction agent for PCOS-related infertility, with clomiphene as '
            'second-line (27). Both agents are always prohibited under WADA category S4 (anti-estrogens and '
            'aromatase inhibitors) (16). Spironolactone, recommended for PCOS-associated hirsutism, is '
            'prohibited as a diuretic (S5). Female athletes pursuing fertility treatment must obtain a TUE for '
            'time-limited, cycle-specific medication use, requiring disclosure of private reproductive health '
            'information to sporting authorities\u2014a privacy concern that may deter athletes from seeking '
            'treatment (2, 27).'
        ),
    ],
}

CROSS_CUTTING = (
    'Three structural factors underlie the identified gaps (Figure 3). First, a temporal mismatch exists '
    'between clinical guideline update cycles and WADA regulatory revisions. Clinical guidelines such as '
    'GINA and ADA Standards of Care are updated annually, while WADA TUE Physician Guidelines, though '
    'described as living documents, show variable revision frequencies with lags of 1\u20133 years in some '
    'disease areas (Table 1). Second, a criteria mismatch distinguishes patient-centered clinical '
    'decision-making (based on symptoms, biomarkers, and quality of life) from anti-doping criteria '
    'emphasizing prevention of performance enhancement. The organic versus functional hypogonadism '
    'distinction exemplifies this divergence. Third, an emerging drug class mismatch arises as novel '
    'therapeutics (GLP-1 receptor agonists, SGLT2 inhibitors) are incorporated into clinical practice '
    'faster than WADA\'s regulatory framework can evaluate their potential for misuse (2, 16, 22).'
)

CROSS_CUTTING_2 = (
    'The temporal mismatch is particularly well illustrated by comparing update frequencies. GINA has '
    'published annual updates every year since 2014, with major revisions in 2019 (abolishing Step 1 '
    'SABA-only treatment) and 2025 (establishing the two-track system). The ADA Standards of Care is '
    'updated annually with a comprehensive revision cycle. In contrast, some WADA TUE Physician '
    'Guidelines have remained unchanged for 3–4 years despite significant clinical developments in '
    'the corresponding disease area. The Prohibited List itself is updated annually, but the TUE '
    'guidance documents that inform clinical decision-making follow a separate, less predictable '
    'revision schedule. This creates a window during which newly recommended first-line therapies '
    'may conflict with TUE guidance that has not yet incorporated the new evidence (2, 16).'
)

# Discussion paragraphs
DISCUSSION = [
    (
        'This scoping review represents, to our knowledge, the first systematic mapping of discrepancies '
        'between WADA TUE regulations and current clinical practice guidelines across multiple disease '
        'domains. Our findings reveal that the clinical-competition gap is not isolated to a single condition '
        'but represents a systemic pattern affecting seven major disease areas with varying degrees of severity.'
    ),
    (
        'The implications of these gaps extend beyond regulatory inconvenience. Athletes may receive '
        'suboptimal medical care when clinicians, aware of anti-doping constraints, prescribe second-line '
        'agents to avoid TUE complexity. The TUE process itself, while necessary, imposes time, financial, '
        'and privacy burdens that may deter athletes from seeking appropriate treatment\u2014particularly in '
        'conditions such as ADHD or PCOS where stigma compounds procedural barriers. Geographic disparities '
        'in TUE access further exacerbate these issues, as athletes in resource-limited settings face greater '
        'difficulty obtaining specialist evaluations and documentation required for TUE applications (2, 21).'
    ),
    (
        'The concept of "no additional performance enhancement beyond restoring normal health" is inherently '
        'challenging to operationalize. For testosterone replacement, even physiological-range restoration may '
        'influence body composition and recovery. For stimulant medications in ADHD, delineating cognitive '
        'normalization from enhancement is conceptually problematic. For beta-2 agonists, the boundary between '
        'bronchodilation and potential systemic anabolic effects remains debated (28). These ambiguities create '
        'uncertainty for both clinicians and TUE committees, potentially leading to inconsistent decisions '
        'across jurisdictions.'
    ),
    (
        'The findings of this review align with and extend previous work in the field. Heuberger and '
        'Cohen (10) found limited evidence for performance-enhancing effects of many prohibited substances, '
        'raising questions about the scientific basis for some prohibitions. Our analysis adds a clinical '
        'dimension to this concern by demonstrating that prohibition of specific agents creates measurable '
        'gaps in patient care. Stuart et al. (29) documented increasing TUE application volumes, which '
        'our disease-specific analysis helps to contextualize—the growing burden reflects both increased '
        'awareness and the expanding scope of conditions affected by clinical-competition gaps. The '
        'geographic disparities in TUE access reported by Vernec et al. (21) take on additional '
        'significance when considered alongside our finding that some disease areas (e.g., ADHD, '
        'hypogonadism) require particularly complex and well-documented TUE applications.'
    ),
    (
        'From an ethical perspective, the clinical-competition gap raises fundamental questions about '
        'the duty of care owed to athletes. The World Medical Association Declaration of Geneva '
        'establishes that patient health shall be the physician\'s first consideration. When anti-doping '
        'regulations effectively compel physicians to prescribe second-line treatments, a tension '
        'emerges between anti-doping compliance and the ethical obligation to provide optimal care. '
        'This tension is particularly acute for physician-athletes (such as the author of this review), '
        'who experience the dual perspective of clinician and competitor. S&C professionals, while not '
        'prescribers, share in this ethical responsibility through their role in monitoring athlete '
        'well-being and advocating for appropriate medical care.'
    ),
    (
        'Several limitations of this review should be acknowledged. First, as a scoping review, we mapped the '
        'breadth of evidence rather than systematically appraising the quality of individual sources. Second, '
        'our gap severity ratings, while based on structured criteria, involve subjective judgment. Third, the '
        'review focused on the regulatory text of WADA documents and clinical guidelines; actual TUE approval '
        'rates and clinical experiences may differ from what policy documents suggest. Fourth, the rapidly '
        'evolving nature of both clinical guidelines and WADA regulations means that specific details may '
        'change; the structural analysis and recommendations, however, address persistent systemic issues.'
    ),
]

# Practical applications
PRACTICAL_INTRO = (
    'The findings of this review have direct implications for strength and conditioning professionals who '
    'work closely with athletes managing medical conditions. The following practical recommendations are offered:'
)

PRACTICAL_ITEMS = [
    ('Recognize medication-related performance changes. ',
     'S&C professionals should be aware that athletes transitioning between medications due to TUE constraints '
     'may experience performance fluctuations. An athlete switching from a stimulant to a non-stimulant ADHD '
     'medication may show decreased focus during training. An athlete discontinuing testosterone replacement '
     'may experience fatigue, decreased recovery capacity, and mood changes. Adjusting training load and '
     'expectations during medication transitions is essential.'),
    ('Understand the TUE timeline. ',
     'TUE applications can take 21\u201330 days for processing. S&C professionals should encourage athletes to '
     'initiate the TUE process well before competitive seasons. For athletes with chronic conditions (asthma, '
     'ADHD, diabetes), annual TUE renewal should be incorporated into pre-season planning alongside '
     'periodization.'),
    ('Monitor athletes on permitted alternatives. ',
     'When athletes use second-line medications to avoid TUE requirements (e.g., atomoxetine instead of '
     'methylphenidate for ADHD, non-diuretic antihypertensives instead of thiazides), S&C professionals should '
     'monitor for suboptimal symptom control that may affect training quality and safety. Unexplained changes '
     'in an athlete\'s focus, energy, respiratory function, or cardiovascular symptoms warrant referral back to '
     'the prescribing physician.'),
    ('Support asthma management beyond SABA. ',
     'S&C professionals should understand that modern asthma guidelines (GINA 2025) recommend against SABA-only '
     'treatment. Athletes with asthma should be encouraged to follow their physician\'s prescribed controller '
     'regimen (typically ICS-formoterol MART), even though SABA alone is more "convenient" from an anti-doping '
     'perspective. Proper inhaler technique and pre-exercise medication timing should be part of the training '
     'environment.'),
    ('Facilitate communication. ',
     'S&C professionals are uniquely positioned to bridge the gap between athletes, physicians, and anti-doping '
     'authorities. Maintaining awareness of the WADA Prohibited List (updated annually each January, with a '
     'summary of changes available on wada-ama.org) and encouraging athletes to use WADA\'s medication check '
     'tools can prevent inadvertent violations.'),
    ('Address masters athlete concerns. ',
     'The growing masters athlete population faces particular challenges with age-related conditions '
     '(hypogonadism, cardiovascular disease, type 2 diabetes). S&C professionals working with masters athletes '
     'should proactively discuss medication status and TUE requirements as part of health screening and '
     'program design.'),
    ('Advocate for athlete health. ',
     'When S&C professionals observe that anti-doping constraints are negatively affecting an athlete\'s health '
     'or well-being, they should advocate for the athlete to seek appropriate medical care and TUE application, '
     'rather than accepting suboptimal treatment as inevitable.'),
]

# Recommendations
RECS_INTRO = 'Based on this review, we propose eight recommendations for reducing the clinical-competition gap:'

RECS = [
    'Establish a formal mechanism to review and update WADA TUE Physician Guidelines within 12 months of major clinical guideline revisions (e.g., GINA, ADA, Endocrine Society updates).',
    'Re-evaluate the organic/functional distinction for male hypogonadism TUEs in light of the Endocrine Society\u2019s symptom-plus-biochemistry approach and the growing masters athlete population.',
    'Conduct a formal impact assessment on athletes with type 2 diabetes before adding GLP-1 receptor agonists to the Prohibited List.',
    'Review formoterol dose thresholds in the context of GINA 2025 MART recommendations to ensure athletes can follow guideline-directed asthma therapy without ADRV risk.',
    'Re-evaluate the in-competition-only prohibition of stimulant medications for ADHD, considering the pharmacokinetics of long-acting formulations and the clinical inappropriateness of competition-day discontinuation.',
    'Differentiate diuretic prohibition based on masking potential, considering a streamlined TUE process for MRAs (spironolactone/eplerenone) prescribed for heart failure.',
    'Simplify and digitize TUE applications through ADAMS system improvements, multilingual support, and standardized documentation templates to reduce access disparities.',
    'Integrate anti-doping pharmacology education into medical school curricula, residency training, and continuing medical education to improve prescriber awareness of the Prohibited List.',
]

# Conclusion
CONCLUSION = [
    (
        'This scoping review identified systematic discrepancies between WADA TUE regulations and current '
        'clinical practice guidelines across seven major disease areas. These gaps arise from structural '
        'mismatches in update timing, diagnostic and treatment criteria, and the pace of pharmaceutical '
        'innovation. The consequences fall disproportionately on athletes, who may receive suboptimal care, '
        'face burdensome administrative processes, or risk inadvertent anti-doping violations when following '
        'evidence-based treatment recommendations.'
    ),
    (
        'The TUE system remains essential for balancing athlete health with sporting integrity. However, its '
        'effectiveness depends on alignment with current medical evidence. The recommendations proposed in this '
        'review offer a practical roadmap for harmonization that preserves anti-doping principles while ensuring '
        'athletes have access to the standard of medical care available to the general population. S&C '
        'professionals, as daily points of contact with athletes, play a critical role in recognizing, '
        'navigating, and advocating for solutions to the clinical-competition gap.'
    ),
]

# References
REFS = [
    '1. World Anti-Doping Agency. World Anti-Doping Code 2021. Montreal: WADA; 2021.',
    '2. World Anti-Doping Agency. World Anti-Doping Code International Standard for Therapeutic Use Exemptions (ISTUE). Montreal: WADA; 2021.',
    '3. Bhasin S, Brito JP, Cunningham GR, et al. Testosterone therapy in men with hypogonadism: an Endocrine Society clinical practice guideline. J Clin Endocrinol Metab. 2018;103(5):1715\u20131744.',
    '4. Global Initiative for Asthma. Global Strategy for Asthma Management and Prevention. Fontana, WI: GINA; 2025.',
    '5. American Diabetes Association Professional Practice Committee. Standards of Care in Diabetes\u20142025. Diabetes Care. 2025;48(Suppl 1):S1\u2013S352.',
    '6. McDonagh TA, Metra M, Adamo M, et al. 2021 ESC Guidelines for the diagnosis and treatment of acute and chronic heart failure. Eur Heart J. 2021;42(36):3599\u20133726.',
    '7. Mancia G, Kreutz R, Brunstrom M, et al. 2023 ESH Guidelines for the management of arterial hypertension. J Hypertens. 2023;41(12):1874\u20132071.',
    '8. Allen H, Backhouse SH, Hull JH, Price OJ. Anti-doping policy, therapeutic use exemption and medication use in athletes with asthma: a narrative review. Sports Med. 2019;49(5):659\u2013668.',
    '9. Vernec A, Pipe A, Engel-Nitz NM. The World Anti-Doping Agency (WADA) Therapeutic Use Exemption (TUE) process. Clin J Sport Med. 2019;29(5):351\u2013355.',
    '10. Heuberger JAAC, Cohen AF. Review of WADA prohibited substances: limited evidence for performance-enhancing effects. Sports Med. 2019;49(4):525\u2013539.',
    '11. Overbye M, Wagner U. Experiences, attitudes and knowledge of elite athletes regarding anti-doping\u2014insights from a cross-national study. Eur J Sport Sci. 2014;14(Suppl 1):S149\u2013S160.',
    '12. Tricco AC, Lillie E, Zarin W, et al. PRISMA extension for scoping reviews (PRISMA-ScR): checklist and explanation. Ann Intern Med. 2018;169(7):467\u2013473.',
    '13. Arksey H, O\'Malley L. Scoping studies: towards a methodological framework. Int J Soc Res Methodol. 2005;8(1):19\u201332.',
    '14. Levac D, Colquhoun H, O\'Brien KK. Scoping studies: advancing the methodology. Implement Sci. 2010;5:69.',
    '15. Munn Z, Peters MDJ, Stern C, Tufanaru C, McArthur A, Aromataris E. Systematic review or scoping review? Guidance for authors when choosing between a systematic or scoping review approach. BMC Med Res Methodol. 2018;18(1):143.',
    '16. World Anti-Doping Agency. The 2026 Prohibited List International Standard. Montreal: WADA; 2025.',
    '17. World Anti-Doping Agency. TUE Physician Guidelines \u2013 Asthma. Version 9.3. Montreal: WADA; 2026.',
    '18. Australian ADHD Professionals Association. Australian Evidence-Based Clinical Practice Guideline for Attention Deficit Hyperactivity Disorder (ADHD). Melbourne: AADPA; 2022.',
    '19. National Institute for Health and Care Excellence. Attention deficit hyperactivity disorder: diagnosis and management. NICE guideline [NG87]. London: NICE; 2024 (updated).',
    '20. World Anti-Doping Agency. TUE Physician Guidelines \u2013 Attention Deficit Hyperactivity Disorder (ADHD). Version 8.0. Montreal: WADA; 2026.',
    '21. Vernec A, Healy D, Banon T, Petroczi A. Prevalence of therapeutic use exemptions at the Olympic Games and Paralympic Games: an analysis of data from 2016 to 2022. Br J Sports Med. 2024;58(17):966\u2013972.',
    '22. World Anti-Doping Agency. 2026 Monitoring Program. Montreal: WADA; 2025.',
    '23. European Association of Urology. EAU Guidelines on Sexual and Reproductive Health. Arnhem: EAU; 2024.',
    '24. Lincoff AM, Bhasin S, Flevaris P, et al. Cardiovascular safety of testosterone-replacement therapy. N Engl J Med. 2023;389(2):107\u2013117.',
    '25. World Anti-Doping Agency. Glucocorticoids and Therapeutic Use Exemptions Guidelines. Montreal: WADA; 2025.',
    '26. World Anti-Doping Agency. Glucocorticoids washout table\u20142026. Montreal: WADA; 2025.',
    '27. Teede HJ, Tay CT, Laven JJE, et al. Recommendations from the 2023 international evidence-based guideline for the assessment and management of polycystic ovary syndrome. J Clin Endocrinol Metab. 2023;108(10):2447\u20132469.',
    '28. Hostrup M, Jacobson GA, Jessen S, Lemminger AK. Beta2-adrenoceptor agonist doping of athletes: a systematic review and meta-analysis of performance-enhancing effects. Br J Sports Med. 2020;54(22):1348\u20131356.',
    '29. Stuart M, Mottram DR, Erskine PJ. Therapeutic use exemptions\u2014a review and analysis of TUE application trends across Olympic sports from 2015 to 2020. Drug Test Anal. 2022;14(5):890\u2013898.',
]

print("SCJ English content data loaded.")
