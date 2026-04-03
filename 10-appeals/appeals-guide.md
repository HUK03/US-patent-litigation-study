# Appeals Guide

> **Quick Reference:** The Federal Circuit has exclusive appellate jurisdiction over all patent cases. It reviews claim construction de novo — which means even a correct trial result can be reversed. Decide whether to appeal based on preserved legal errors, not just disagreement with the outcome.

---

## 1. The Federal Circuit's Exclusive Jurisdiction

The **Court of Appeals for the Federal Circuit** (Fed. Cir.) has exclusive jurisdiction over appeals in patent cases from US district courts (28 U.S.C. § 1295(a)(1)). This means all patent appeals go to one court, regardless of which district court decided the case.

**Importance for strategy:** Federal Circuit precedent is the controlling law on all patent legal issues. Unlike most areas of law where regional circuit precedent controls, patent law is nationally uniform. Understanding Federal Circuit trends is essential for predicting case outcomes.

---

## 2. Timing: Notice of Appeal

- **Deadline:** 30 days from the entry of the final judgment (28 U.S.C. § 2107; Fed. R. App. P. 4(a)(1)(B) — 60 days if the United States is a party)
- **Final judgment requirement:** In most cases, a final judgment is not entered until: the jury verdict is reduced to a judgment, all post-trial motions are resolved, and injunction issues are resolved
- **Multiple parties:** If one party appeals, other parties have 14 days after the first notice of appeal (or the original 30-day deadline, whichever is later) to file their own notice

**Critical:** Missing the notice of appeal deadline is **jurisdictional** — courts cannot extend it. Calendar this deadline immediately after a verdict.

---

## 3. Deciding Whether to Appeal

### The Appeal Decision Framework

```
Step 1: Was legal error committed at the district court?
  ├── Adverse claim construction (de novo review — strongest Federal Circuit issue)
  ├── SJ denial that should have been granted (de novo review)
  ├── JMOL denial on insufficient evidence (substantial evidence review)
  ├── Erroneous jury instruction (harmless error analysis)
  └── Exclusion/admission of expert testimony (abuse of discretion)

Step 2: Was the error preserved?
  ├── Did we object at trial? (Required for most evidentiary issues)
  ├── Did we move for JMOL? (Required for sufficiency of evidence challenge)
  └── Was the claim construction challenge raised before the district court?

Step 3: Is the error outcome-determinative?
  ├── Would a correct claim construction change the infringement result?
  └── Would corrected jury instructions change the damages result?

Step 4: What is the cost-benefit of appeal?
  ├── Additional cost: $500K–$1.5M (briefing through decision)
  ├── Timeline: 18–30 months from notice of appeal to decision
  ├── Reversal probability: ~35–45% in patent cases (Federal Circuit reversal rate)
  ├── Remaining product risk: Is the accused product still being sold?
  └── Settlement opportunity: Post-verdict, pre-appeal settlement often more favorable than post-appeal
```

---

## 4. Standards of Review — Know Your Leverage

Different issues receive different deference on appeal. Focus your appeal on issues with favorable review standards.

| Issue | Standard of Review | Implications |
|---|---|---|
| **Claim construction** | **De novo** (legal conclusions); clear error (subsidiary facts per *Teva*, 2015) | Strongest appellate ground — Federal Circuit can and does reverse claim construction freely |
| **Patent eligibility (§ 101)** | **De novo** | Entirely fresh look; significant reversal possibility for software/AI patents |
| **Summary judgment** | **De novo** | No deference to district court; strong appellate review |
| **Jury infringement verdict** | Substantial evidence | High bar to reverse — jury verdicts are deferred to |
| **Jury invalidity verdict** | Substantial evidence | High bar to reverse |
| **Jury damages verdict** | Substantial evidence + de novo on legal errors in damages methodology | Mixed — mathematical errors get fresh review; factual estimates deferred |
| **Expert exclusion (Daubert)** | Abuse of discretion | High bar — court deferred to district court's gatekeeping |
| **Injunction / enhanced damages** | Abuse of discretion | High bar — discretionary decisions deferred to |
| **Attorney fees (§ 285)** | Abuse of discretion | High bar |

**Strongest appellate grounds:** Claim construction errors and § 101 errors. Both are reviewed de novo, and the Federal Circuit has actively reversed district courts on both in recent years.

---

## 5. Key Federal Circuit Practice Points

### Record Preservation

Everything on appeal must be **preserved in the district court record**:
- Objections to jury instructions must be made on the record during the jury instruction conference
- JMOL motions must be made at the close of evidence (Rule 50(a)) — without this, the post-trial Rule 50(b) motion is unavailable
- Claim construction arguments must be fully briefed in Markman proceedings
- Expert exclusion grounds must be raised in Daubert motions below

**Failure to preserve = plain error review** (essentially unreviewable).

### Briefing Requirements

- **Opening brief:** Filed by appellant; must contain all arguments
- **Response brief:** Filed by appellee; filed within 40 days of opening brief
- **Reply brief:** Filed by appellant; within 21 days of response brief
- **Word limits:** Opening and response briefs: 14,000 words; reply: 7,000 words
- **Appendix:** Joint appendix containing the key trial court record (filings, key exhibits, trial transcript excerpts)

### Oral Argument

Requested by either party; almost always granted. Typically 15 minutes per side (30 minutes total). The Federal Circuit is highly active from the bench — prepare for pointed questions on your weakest arguments.

---

## 6. Staying Enforcement of Judgment Pending Appeal

A money judgment can be enforced while appeal is pending. To **stay enforcement** pending appeal, the defendant must either:
1. Post a **supersedeas bond** in the full amount of the judgment (or as set by the court) under Fed. R. Civ. P. 62(b)
2. Obtain an **automatic stay** from the district court or Federal Circuit

**Automatic stay of injunctions:** Injunctions are automatically stayed if a timely notice of appeal is filed and the injunction itself is the subject of the appeal — but this only applies to injunctions, not money judgments.

**Bond considerations:** Large verdict → large bond. For a $200M verdict, a $200M+ bond may be required. This is a major financial commitment. Some courts allow a reduced bond upon a showing that the defendant has sufficient assets to satisfy the judgment.

🌏 **Korean Company Note:** Korean companies with significant US assets (real estate, bank accounts, equipment) may need to take steps to protect those assets from enforcement during the appeal period. Work with US counsel on whether to post a bond or seek other protective relief immediately after verdict.

---

## 7. PTAB Appeals — Federal Circuit Review of IPR FWDs

Final Written Decisions from PTAB IPR proceedings are also appealed to the Federal Circuit (35 U.S.C. § 319):

| Issue | Standard of Review |
|---|---|
| PTAB legal conclusions (claim construction, obviousness legal standard) | De novo |
| PTAB factual findings (prior art analysis, motivation to combine, secondary considerations) | Substantial evidence |
| PTAB discretionary denial (Fintiv) | Abuse of discretion (very difficult to reverse) |

**Timing:** Notice of appeal must be filed within **63 days** of the FWD (different from district court's 30-day rule).

**Who can appeal:** Both the petitioner (if claims survive) and the patent owner (if claims are cancelled) can appeal.

---

## 8. Post-Appeal Remand Proceedings

If the Federal Circuit reverses or vacates and remands:
- The district court must conduct further proceedings consistent with the Federal Circuit's ruling
- On remand for claim construction: the district court re-applies the corrected construction to the facts, potentially requiring new summary judgment briefing or a new trial
- On remand for damages: the district court may need to conduct a new damages trial (or conduct a new Daubert analysis of damages experts)
- On remand from PTAB: PTAB applies the Federal Circuit's legal guidance in additional proceedings

---

## 9. Cross-Appeals — When the Defendant Wins (Mostly) But Wants More

If the defendant wins on liability but the damages amount was still too high (or if the district court denied attorney fees that should have been awarded), the defendant may file a **cross-appeal**:

- Cross-appeal is filed within 14 days of the opposing party's notice of appeal (or within the original 30-day window)
- Enables the defendant to appeal aspects of the judgment adverse to it (e.g., damages calculation, denial of attorney fees) even while opposing the plaintiff's appeal of liability

**Practical consideration:** Weigh carefully whether a cross-appeal on damages helps or hurts — a successful cross-appeal that remands for recalculated damages may result in higher damages if the plaintiff's expert is better prepared on remand.
