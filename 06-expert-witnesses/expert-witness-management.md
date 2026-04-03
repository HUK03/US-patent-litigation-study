# Expert Witness Management

> **Quick Reference:** Patent cases are won and lost on expert testimony. Technical experts shape the jury's understanding of infringement and invalidity; damages experts determine the magnitude of the verdict. Retain experts early, vet them thoroughly, and prepare them as if their deposition and trial testimony are the most important events in the case.

---

## 1. Categories of Experts Needed for Defense

| Expert Type | When Needed | Primary Role |
|---|---|---|
| **Technical expert (non-infringement)** | Required in virtually all cases | Opine that accused product does not satisfy one or more claim elements; explain how the accused product works |
| **Technical expert (invalidity)** | Required in virtually all cases | Opine that prior art anticipates or renders obvious the asserted claims; define POSITA |
| **Damages expert** | Required in virtually all cases | Calculate a reasonable royalty from defendant's perspective; rebut plaintiff's royalty model |
| **Industry/licensing expert** | Valuable in many cases | Testify about customary licensing practices and rates in the technology field |
| **Claim construction expert** | Optional | Support defendant's claim construction positions (sometimes same as technical expert) |

In straightforward cases, the same technical expert may cover both non-infringement and invalidity. In complex cases with multiple patents or highly disparate technical issues, separate experts for each may be appropriate.

---

## 2. Selecting Technical Experts

### Essential Qualifications

1. **Matches the POSITA definition** — The expert's credentials should align with how the court defines the person of ordinary skill in the art. If the POSITA is defined as having a master's degree in computer science + 3 years of industry experience, the expert should have at least those credentials (ideally more)

2. **Technical depth in the accused technology** — An expert in "electrical engineering generally" is insufficient for a case involving 5G signal processing or machine learning algorithms. Verify the expert has **published work, industry experience, or demonstrated projects** in the specific technology at issue

3. **Independence from the company** — The expert must not have current employment, consulting, or financial relationships with the defendant that could compromise perceived objectivity

4. **Prior patent testimony experience** — An expert who has been deposed and testified at trial in patent cases is far better equipped to handle adversarial examination than a first-timer. Review prior transcripts

5. **No disqualifying prior positions** — Search for prior publications, presentations, deposition testimony, or declarations in other cases where the expert took positions inconsistent with what you need them to say. Plaintiff's counsel will find these

### Red Flags to Screen Out

- Prior testimony for patent plaintiffs asserting similar technology
- Publications arguing that prior art in your case does NOT invalidate similar patents
- Financial relationships with patent aggregators or NPE investors
- Prior inconsistent positions on claim construction of similar terms
- History of excluded testimony under Daubert

### Practical Vetting Checklist

- [ ] Google Scholar search of expert's publications
- [ ] PACER search for prior expert testimony (search expert's name in patent case filings)
- [ ] Check prior trial transcripts and depositions for prior inconsistent positions
- [ ] Verify credentials independently (university transcripts if needed)
- [ ] Conflict check with any past relationships with patent owner or plaintiff's counsel

---

## 3. Retaining Damages Experts

### The Qualifications Divide: Economist vs. IP Licensing Specialist

| Profile | When to Use | Strengths | Weaknesses |
|---|---|---|---|
| **Economic/finance PhD** | Complex cases; high damages; multiple accused products | Rigorous economic analysis; credible to courts on apportionment | May lack practical licensing experience; can come across as abstract |
| **IP licensing practitioner** | Industry-specific cases; SEP/FRAND disputes; cases where comparable licenses are central | Deep knowledge of real-world licensing norms; practical credibility | May lack economic rigor; academic credentials sometimes weaker |
| **Hybrid (economist with IP practice)** | Most cases | Best of both worlds | Scarce; expensive |

### Key Capabilities to Require

- Familiarity with and ability to apply the **Georgia-Pacific 15 factors** framework
- Experience with **apportionment** methodology and the SSPPU doctrine
- Experience analyzing and adjusting **comparable licenses** for differences in scope, technology, and economic circumstances
- Ability to explain complex financial analysis clearly to a lay jury
- Knowledge of the 2024–2025 damages case law developments (*EcoFactor* en banc, *Rex Medical*, *Provisur*)

### 2024–2025 Case Law Damages Experts Must Know

- ***EcoFactor v. Google*** (Fed. Cir. en banc 2025): Comparable license admissibility and built-in apportionment doctrine reshaped; expert must carefully justify comparability
- ***Rex Medical v. Intuitive Surgical*** (Fed. Cir. Sept. 2025): When a comparable license covers multiple patents, the expert **must** apportion the license value to the specific patent in suit — failure to do so = exclusion under Daubert
- ***Provisur v. Weber*** (Fed. Cir. Oct. 2024): Particularized apportionment evidence required before using entire product market value as royalty base
- ***Altria v. Reynolds*** (Fed. Cir. Dec. 2024): Lump-sum license with built-in apportionment can be admissible; cert. pending

---

## 4. Expert Disclosure Requirements (Rule 26(a)(2))

Expert witnesses retained specifically for litigation must provide a written report containing:

1. **Complete statement of all opinions** to be expressed and the basis and reasons for them
2. **Facts or data** considered in forming the opinions
3. **Exhibits** to be used as a summary of or support for the opinions
4. **Qualifications** of the expert, including publications for the past 10 years
5. **List of all other cases** in which the expert testified as an expert (previous 4 years)
6. **Statement of compensation** for the study and testimony

**Timing:** Opening reports are served on the schedule in the scheduling order (typically 30–60 days before close of expert discovery). Rebuttal reports follow within 30–60 days after opening reports.

### Post-2010 Rule 26 Protections for Draft Reports

Fed. R. Civ. P. 26(b)(4)(B) and (C) protect:
- **Draft expert reports** — not discoverable
- **Communications between the party's attorney and the expert** — not discoverable, EXCEPT:
  - Communications about compensation for the expert's study or testimony
  - Facts or data the attorney provided that the expert considered in forming opinions
  - Assumptions the attorney provided that the expert relied upon

**Practical implication:** Counsel may review and comment on draft expert reports without creating a discoverable record. But the factual inputs provided to the expert may be discoverable.

---

## 5. Daubert Challenges — Offense and Defense

*Daubert v. Merrell Dow Pharmaceuticals* (SCOTUS 1993) and Fed. R. Evid. 702 require the district court to act as "gatekeeper" — excluding expert testimony that is not based on sufficient facts or data, not the product of reliable principles and methods, or not reliably applied to the facts of the case.

### When to File a Daubert Motion Against Plaintiff's Expert

Target the plaintiff's **damages expert** in most cases — damages expert exclusions are far more common than technical expert exclusions, and a partially excluded damages opinion can dramatically reduce or eliminate the plaintiff's damages case.

**Most common grounds to exclude plaintiff's damages experts:**

| Ground | Recent Cases Supporting Exclusion |
|---|---|
| Failed to apportion comparable license covering multiple patents | *Rex Medical v. Intuitive Surgical* (Fed. Cir. 2025) |
| Used entire product revenue as royalty base without EMVR justification | *Provisur v. Weber* (Fed. Cir. 2024) |
| Comparable licenses not technically or economically comparable; no adjustment methodology | *EcoFactor en banc* context (2025) |
| Applied royalty rate without analyzing hypothetical negotiation date | Standard Georgia-Pacific failure |
| Relied on licenses obtained through litigation settlement without accounting for settlement dynamics | Baseline Daubert risk |

**Filing timing:** File Daubert motions after the close of expert discovery, typically simultaneously with summary judgment motions.

### Defending Against Daubert Challenges to Our Experts

When opposing counsel files a Daubert motion against your expert:
- **Analyze the motion carefully** — if the expert has a genuine methodology flaw, address it before trial (consider supplemental declaration)
- **Prepare a thorough opposition** — cite the expert's methodology, the facts they relied on, and why the methodology is accepted in the field
- **Request a Daubert hearing** — oral argument helps; judges sometimes exclude experts on papers without fully appreciating the methodology
- **Have the expert prepare a declaration** responding to the specific methodological challenges

---

## 6. Expert Deposition Preparation Checklist

Before the damages or technical expert's deposition, ensure:

**Three weeks before:**
- [ ] Review and re-read all expert reports (opening + rebuttal) line by line
- [ ] Prepare the expert for cross-examination on their weakest assumptions
- [ ] Identify all prior testimony, publications, and statements that plaintiff may use to impeach
- [ ] Conduct a mock cross-examination session

**One week before:**
- [ ] Review all documents the expert reviewed in forming opinions
- [ ] Identify any "hot documents" (internal emails, presentations) that plaintiff may use during the deposition
- [ ] Prepare the expert on privilege boundaries (what they cannot discuss)
- [ ] Confirm the expert understands: only answer the question asked; do not volunteer information

**The deposition:**
- [ ] Have counsel attend and be prepared to object (speaking objections not permitted, but form objections and privilege objections are appropriate)
- [ ] If the expert is asked about a document they have not seen, instruct them to review it carefully before answering
- [ ] Watch for "hypothetical question" traps that assume facts not in evidence

🌏 **Korean Company Note:** When the technical expert needs to review Korean-language technical documents about the accused product, ensure all relevant documents are translated before the expert is retained. An expert who says "I couldn't read the Korean documents so I relied on summaries" is highly vulnerable on cross-examination.

---

## 7. Trial Testimony Preparation

The week before trial, conduct intensive witness preparation:

**Technical expert trial prep:**
- Simplify technical concepts to a 6th-grade level — patent juries are typically non-technical
- Practice explaining the accused feature and the claim elements using clear analogies
- Prepare demonstrative exhibits: large-format claim charts, product diagrams, prior art timeline
- Practice direct examination sequence: credentials → POSITA definition → claim construction → non-infringement analysis → invalidity analysis

**Damages expert trial prep:**
- Prepare the hypothetical negotiation "story" — bring the jury into the imagined negotiation room
- Practice explaining apportionment in simple terms: "Of the $300 phone, only the [accused feature] is relevant; that feature is worth about $X"
- Prepare to defend the comparable license analysis: "I chose these licenses because..."
- Prepare for cross on any licenses the expert did NOT include (plaintiff will ask why)
