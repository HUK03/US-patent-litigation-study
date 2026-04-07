# Damages Defense Strategy

> **Quick Reference:** Damages defense is as important as liability defense. In 2024, total patent damages across 72 jury verdicts reached $4.19 billion. The Federal Circuit's 2024–2025 decisions strongly favor defendants who challenge apportionment rigorously — use *Rex Medical*, *Provisur*, and *EcoFactor* en banc to attack plaintiff's royalty model at every stage.

---

## 1. Overview of Patent Damages Under 35 U.S.C. § 284

The statute requires damages "adequate to compensate for the infringement, but in no event less than a reasonable royalty." Three types of damages are available:

| Type | Description | When Available |
|---|---|---|
| **Reasonable royalty** | What a willing licensor and willing licensee would have agreed to in a hypothetical negotiation just before infringement began | Always (minimum floor) |
| **Lost profits** | Plaintiff's actual profit losses from defendant's infringement | Requires patentee to be a market participant and satisfy Panduit four-factor test |
| **Enhanced damages** | Up to 3× compensatory damages for willful infringement | Discretionary; requires egregious conduct (*Halo* standard) |

**For NPE plaintiffs:** Lost profits are essentially never available — NPEs don't make products. Reasonable royalty is the only damages theory.

---

## 2. The Reasonable Royalty Framework: Georgia-Pacific

The leading framework for calculating a reasonable royalty is the **15-factor Georgia-Pacific test** from *Georgia-Pacific Corp. v. U.S. Plywood Corp.* (S.D.N.Y. 1970). Courts instruct juries to consider all relevant factors; defendants should use each factor to argue for a lower royalty.

| # | Factor | Defendant's Typical Argument |
|---|---|---|
| 1 | Royalties received by patentee for licensing the patent in suit | Prior licenses at lower rates anchor the royalty down |
| 2 | Rates paid by licensee for use of other patents comparable to patent in suit | Industry rates for similar technology are lower |
| 3 | Nature and scope of the license (exclusive vs. non-exclusive; territory) | Hypothetical license is non-exclusive, limited in scope = lower value |
| 4 | Patentee's established policy and marketing program | NPEs have no manufacturing business to protect; lower rate |
| 5 | Commercial relationship between licensor and licensee (competitors vs. non-competitors) | If parties are competitors, royalty may be structured differently |
| 6 | Effect of selling patented specialty in promoting sales of other products | Accused feature drives negligible demand for the overall product |
| 7 | Duration of patent and term of license | Patent is near expiration; shorter value |
| 8 | Established profitability of the product made under the patent | Low product margins; limited ability to pay |
| 9 | Utility and advantages of the patent over old modes | Patent provides minimal incremental advantage over prior art alternatives |
| 10 | Nature of the patented invention; commercial embodiments | Simple, incremental improvement; easily designed around |
| 11 | Extent to which infringer has used the invention | Accused feature is peripheral, rarely used |
| 12 | Portion of profit that may be customary to allow for use of the invention | Industry customary rate is low |
| 13 | Portion of realizable profit that should be credited to the invention | Apportionment: only the patent's contribution, not the whole product |
| 14 | Opinion testimony of qualified experts | Defendant's damages expert opinion at lower rate |
| 15 | Amount that a licensor and licensee would have agreed upon at the time infringement began | Hypothetical negotiation anchored to actual comparable licenses |

---

## 3. Apportionment — The Most Important Defense Principle

**Apportionment is not optional** — it is constitutionally required by *Garretson v. Clark* (SCOTUS 1884) and repeatedly reaffirmed by the Federal Circuit. The royalty must be tied to the patented **feature's** contribution to the overall product's value, not the entire product.

### The Smallest Saleable Patent-Practicing Unit (SSPPU)

The SSPPU doctrine (articulated in *Lucent Technologies v. Gateway*, Fed. Cir. 2009; *LaserDynamics v. Quanta*, Fed. Cir. 2012) requires using the **smallest unit that practices the patent** as the starting point for the royalty base, rather than the entire product.

**Examples:**
- Accused feature = Wi-Fi chip in a laptop → Royalty base = Wi-Fi chip (not the entire laptop)
- Accused feature = image compression algorithm in a smartphone → Royalty base = software module value (not the phone)
- Accused method = one step in a multi-step manufacturing process → Royalty base = the value attributable to that step

**Post-*Rex Medical* (Sept. 2025) standard for comparable licenses:** When using a comparable license as evidence of the royalty rate, if that license covers **more than just the patent in suit** (i.e., covers multiple patents), the expert must apportion the license value attributable to the specific patent in suit. Failure to do so = exclusion under Daubert.

### The Entire Market Value Rule (EMVR) — A High Bar for Plaintiffs

Under the EMVR, a plaintiff CAN use the entire product's revenue as the royalty base if the patented feature **is the basis for customer demand** for the entire product. This is a very high bar:
- The patented feature must be what drives customers to buy the product (not just a contributing feature)
- Courts rarely allow EMVR, especially for multi-feature technology products
- *Provisur v. Weber* (Fed. Cir. Oct. 2024): Reinforced that plaintiff must provide particularized evidence of customer demand driven specifically by the patented feature before invoking EMVR

**Defense strategy:** Attack every attempt to use the full product revenue as the royalty base. Require the plaintiff to demonstrate that the accused feature, alone, drives customer demand for the entire product — virtually impossible for one feature of a complex smartphone, laptop, or industrial machine.

### Apportionment Methodology Options for Defendants

| Method | Description | Best For |
|---|---|---|
| **Comparable license adjustment** | Find licenses for similar technology; adjust to the patent's contribution | When comparable licenses are available |
| **Income approach** | Calculate incremental profits attributable to the patented feature vs. non-infringing alternative | When accused feature has measurable incremental value |
| **Cost approach** | Estimate cost to implement a design-around (non-infringing alternative) | When design-around is feasible and inexpensive |
| **Survey evidence** | Survey consumers to determine willingness to pay for the patented feature specifically | For consumer products where feature value can be isolated |

---

## 4. Comparable License Analysis — Attacking Plaintiff's Evidence

Comparable licenses are the most powerful damages evidence — which is exactly why defendants must scrutinize plaintiff's license selection and adjustment methodology.

### What Makes a License "Comparable"?

A license is comparable if it is sufficiently similar in:
1. **Technology:** Does the license cover the same or closely related technology?
2. **Time period:** Was the license negotiated around the same time as the hypothetical negotiation date?
3. **Economic circumstances:** Were the economic terms similar (e.g., lump sum vs. running royalty; territory)?
4. **Relationship between parties:** Were the parties in a similar relationship (horizontal competitors vs. licensor-licensee)?

### Strategies to Attack Plaintiff's Comparable Licenses

| Attack Vector | Argument |
|---|---|
| **Multi-patent license** | The license covers dozens of patents; plaintiff's expert failed to apportion to just this patent (*Rex Medical*, 2025) |
| **Settlement license** | Licenses obtained to settle litigation reflect litigation risk, not true market value; they systematically overstate royalty rates |
| **Portfolio cross-license** | A mutual cross-license reflects both parties' portfolios; the rates cannot be extracted for a single patent |
| **Different technology** | The licensed technology is not comparable; no analysis of the technical differences |
| **Different time period** | Market conditions have changed since the comparable license was executed |
| **No adjustment methodology** | Plaintiff's expert acknowledged the license needed adjustment but provided no principled method |

---

## 5. Willfulness and Enhanced Damages Defense

### The Two-Step Analysis Post-*Halo*

*Halo Electronics v. Pulse Electronics* (SCOTUS 2016) established:
1. **Willfulness** (jury question): Did defendant act "deliberately or intentionally" in infringing the patent? Standard: preponderance of the evidence.
2. **Enhanced damages** (court discretion): Were the circumstances "egregious" enough to warrant 2× or 3× damages? Standard: abuse of discretion review.

**Key 2025 update:** *Halo v. Pulse* returned to the Federal Circuit (Feb. 2025). The court affirmed the district court's *refusal* to enhance damages despite a willfulness jury verdict, holding:
- A willfulness finding is "but one factor" — it opens the door but does not compel enhancement
- Enhanced damages require truly **egregious** conduct: "wanton, malicious, bad-faith, deliberate, consciously wrongful, flagrant"

### *Read Corp.* Factors — Applied in Every Post-*Halo* Enhanced Damages Analysis

Courts apply these nine factors to decide whether to enhance:

| Factor | Defense Argument |
|---|---|
| 1. Deliberate copying | We independently developed our product; no copying |
| 2. Investigation of patent / good-faith belief in invalidity or non-infringement | We investigated and obtained opinion of counsel |
| 3. Behavior as a party | We litigated in good faith; no misconduct |
| 4. Defendant's size and financial condition | Large company → higher ability to pay, but also more resources to properly investigate |
| 5. Closeness of the case | Infringement and validity are genuinely disputed; we had a reasonable defense |
| 6. Duration of misconduct | Infringement period was short; we moved quickly to design around |
| 7. Remedial action | We implemented design-arounds promptly |
| 8. Motivation for harm | No intent to harm patentee; just competing in the market |
| 9. Concealment | No concealment; we disclosed our product publicly |

### Cutting Off Willfulness Exposure

**Before suit:** Obtain a written opinion of counsel as early as possible after learning of the patent (see [Privilege & Work Product](../05-discovery/privilege-and-work-product-protection.md))

**After complaint is served:** Immediately investigate validity and non-infringement; document the investigation; consider implementing a design-around; consult with counsel about the strength of the case

**If design-around is implemented:** Document it thoroughly — evidence of prompt good-faith efforts to avoid infringement weighs heavily against enhanced damages

🌏 **Korean Company Note:** For Korean companies, large US patent damages verdicts are a major financial risk. Notable recent verdicts against Korean companies: *Collision Communications v. Samsung* ($445.5M, EDTX, 2025); *Netlist v. Micron* ($445M willful, 2024). A robust opinion of counsel program and proactive design-around practices are essential.

---

## 6. Lost Profits Defense (When Applicable)

For the rare cases where the plaintiff is a market participant seeking lost profits, apply the **Panduit four-factor test**:

1. **Demand for the patented product** — Plaintiff must show consumer demand specifically for the patented feature (not just demand for the accused product generally)
2. **Absence of acceptable non-infringing substitutes** — Defendant can defeat this by showing viable alternatives exist
3. **Manufacturing and marketing capacity** — Plaintiff had capacity to meet the demand they claim they lost
4. **Amount of profit plaintiff would have made** — Calculation of actual profit margin

**Key defense:** Factor 2 is usually the most vulnerable. Demonstrate that non-infringing substitutes (products or design-arounds) were available and acceptable to consumers — this breaks the causal link between infringement and lost profits.

---

## 7. Pre-Trial Damages Motions

### Daubert Motion Against Plaintiff's Damages Expert

File a Daubert motion immediately after plaintiff's opening expert reports are served. Target:
- Failure to apportion comparable licenses (*Rex Medical*, *Provisur*)
- Use of EMVR without justification
- Failure to properly apply hypothetical negotiation framework
- Cherry-picking comparables without analyzing the full license landscape
- Running royalty base improperly inflated to entire product revenue

### Motion in Limine to Exclude Improper Royalty Base

Even if the Daubert motion is denied, file a motion in limine to:
- Exclude reference to total product revenue in front of the jury without EMVR predicate showing
- Exclude mention of large damages verdicts in other cases (irrelevant; unfairly prejudicial)
- Limit damages testimony to properly apportioned SSPPU-based analysis

### Summary Judgment on Damages (Rare but Available)

In rare cases where the plaintiff's only damages theory is clearly improper as a matter of law, summary judgment on damages is available. More commonly, partial summary judgment limiting the scope of damages (e.g., ruling that certain products are not accused) reduces exposure.

---

## 8. 2026 Update Addendum: Geographic Limits, Willfulness Process, and Equity Defenses

### A. Separate US vs. Non-US Revenue in Day-1 Damages Modeling

Defense teams should require damages experts to build explicit segmentation for where the legally relevant infringing acts occurred. Do not allow blended global-revenue models without a location-of-use/copy/install analysis tied to asserted claims.

### B. Willfulness Mitigation Requires Formal Opinion Workflow

If competitor patents are known, implement a documented opinion-of-counsel workflow (trigger criteria, outside counsel engagement, decision memo). Commercial indemnity language alone is not a substitute for a reasoned legal non-infringement/invalidity analysis.

### C. Inequitable Conduct Budgeting Reality

Treat inequitable-conduct theories as high-burden, fact-intensive paths that often survive into later merits stages. Plan resources accordingly instead of assuming early summary disposition.

