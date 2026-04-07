# Early Case Strategy

> **Quick Reference:** The strategic decisions made in the first 90 days of litigation disproportionately shape outcomes. This document addresses framing the defense theory, early motion opportunities, willfulness management, and the IPR/district court parallel track decision.

---

## 1. Framing the Defense Theory: Non-Infringement vs. Invalidity

One of the earliest strategic decisions is whether to lead with **non-infringement**, **invalidity**, or both. There is no single right answer — the correct choice depends on the strength of the available arguments.

| Strategy | When It Makes Sense | Advantages | Risks |
|---|---|---|---|
| **Lead with non-infringement** | Claim mapping shows clear missing element(s); product can be changed to avoid infringement | Clean, simple message to jury; limits damages exposure if validity lost; no risk of IPR estoppel issues | If claim is construed broadly, non-infringement argument collapses |
| **Lead with invalidity** | Strong prior art exists; patent is broad or likely over-claimed | Can moot the case entirely; IPR route available; invalidity binds the world | Clear and convincing evidence standard; prior art must be compelling |
| **Both (parallel)** | Most cases — both defenses have merit | Belt-and-suspenders approach; one defense can rescue the other | Jury confusion; resource-intensive; requires coordination across district court and PTAB |
| **Design-around as primary track** | Core feature is genuinely at risk; non-infringing alternative is technically feasible | Eliminates ongoing infringement; reduces damages period; removes injunction risk | Time and cost of re-design; may not eliminate past damages; must be documented carefully |

**General rule:** Even if non-infringement is the primary defense, always investigate invalidity — a credible invalidity defense strengthens settlement leverage and provides an escape route if non-infringement arguments fail at Markman.

---

## 2. § 101 Alice/Mayo Challenge — Early Motion Opportunity

A § 101 challenge (patent-ineligible subject matter) can be raised early — even on a motion to dismiss under Rule 12(b)(6) or on an early motion for summary judgment — without completing full fact discovery. This makes it one of the most cost-effective defenses when available.

### Is a § 101 Motion Viable? — Decision Checklist

```
Step 1: Does the patent cover:
  ├── Software / computer-implemented methods?  → HIGH viability
  ├── AI / machine learning applications?       → HIGH viability (Recentive Analytics, 2025)
  ├── Business methods?                         → HIGH viability
  ├── Data processing / analytics?              → HIGH viability
  ├── Mechanical devices?                       → LOW viability (§ 101 rarely applies)
  └── Biotech / diagnostics?                    → Moderate (Mayo applies to diagnostics)

Step 2: Does the claim do more than apply an abstract idea on a generic computer?
  ├── Claims a specific technical improvement to computer operation?  → Lower § 101 risk
  ├── Specifies unconventional hardware or algorithms?               → Lower § 101 risk
  └── Just says "apply [abstract idea] using a computer/network"?    → HIGH § 101 vulnerability

Step 3: What is the district's track record on § 101 motions?
  ├── N.D. Cal.: Active § 101 jurisprudence; receptive to early motions
  ├── D. Del.: Mixed; some judges prefer full record before deciding
  └── W.D. Tex. / E.D. Tex.: § 101 motions possible but less routinely granted at pleadings stage
```

### Key § 101 Precedents to Apply

- *Alice Corp. v. CLS Bank Int'l* (SCOTUS 2014) — two-step test framework
- *Mayo Collaborative Services v. Prometheus Labs* (SCOTUS 2012) — natural phenomena
- *Recentive Analytics, Inc. v. Fox Corp.* (Fed. Cir. April 2025) — **landmark AI/ML ruling**: applying known machine learning methods to a new data domain does not confer § 101 eligibility; improved accuracy from a generic ML model does not qualify as a "technological improvement"
- *Hawk Technology Systems v. Castle Retail* (Fed. Cir. 2023) — software patent (video surveillance) invalidated; "focus of the claimed advance" test

### Early § 101 Motion: Pros vs. Cons

| Pros | Cons |
|---|---|
| Decided on pleadings — no expensive discovery | Some courts (D. Del.) prefer full record |
| Cost-effective: decided before major costs accumulate | Federal Circuit reversal rate on § 101 can be unpredictable |
| Sets favorable framing early | May not succeed; alerting plaintiff to strengthen their § 102/103 defense |
| Does not implicate IPR estoppel | Plaintiff may amend claims / seek leave to re-plead |

---

## 3. Scheduling Order Strategy

The scheduling order locks in key dates for the entire case. Negotiation of the scheduling order is a critical early strategic opportunity.

### Key Strategic Choices in Scheduling Order Negotiations

**Markman Timing:**
- **Early Markman** (before fact discovery closes): Can provide early resolution on claim scope; favorable if your constructions would be adopted; risky if you need discovery to support your constructions
- **Late Markman** (after fact discovery, often with summary judgment): Allows more complete record; damages discovery can be scoped to Markman outcome; preferred in complex technical cases

**Fact and Expert Discovery Sequencing:**
- Prefer **staggered expert deadlines**: Opening reports first, rebuttal period of at least 60–90 days (needed to respond to plaintiff's damages model)
- Avoid compressed schedules — NPEs often push for fast track; resist unless your defenses are already well-developed

**Invalidity Contentions Deadline:**
- Under most local patent rules (e.g., N.D. Cal., D. Del.), defendant must serve invalidity contentions within 45–60 days of the scheduling conference
- Invalidity contentions lock in prior art positions — prior art not disclosed in contentions generally cannot be used later unless leave to amend is granted (difficult to obtain)
- **Budget significant resources for the invalidity contentions deadline** — it is one of the most important early litigation tasks

**Number of Claim Terms for Markman:**
- Local rules typically limit the number of disputed terms (e.g., N.D. Cal. Patent Local Rule: 10 terms per side, 20 total)
- Negotiate for more terms if the patent has many important limitations
- Prioritize: claim terms where your construction (1) reads out the accused product, or (2) renders claims invalid

---

## 4. Willfulness and Enhanced Damages Management

Willful infringement can result in enhanced damages up to **3x** under 35 U.S.C. § 284 (*Halo Electronics v. Pulse Electronics*, Supreme Court 2016).

### What Is Willful Infringement?
Under *Halo*:
- Standard: Did the defendant act "deliberately or intentionally" in infringing the patent?
- Burden: Preponderance of the evidence (not clear and convincing)
- **Important 2025 update:** *Halo v. Pulse* returned to the Federal Circuit (Feb. 2025). The court reaffirmed that a jury's willfulness finding is "but one factor" in enhanced damages — willfulness is necessary but NOT sufficient. The district court retains discretion to deny enhancement even after a willfulness verdict. Enhanced damages require truly "egregious" conduct.

### Cutting Off Willfulness Exposure

**From the complaint date:** Once a complaint is filed, knowledge of the patent is established. After the complaint, any ongoing infringement can constitute willful infringement. Defendant should:
- Promptly investigate the patent and accused product
- Consider design-arounds (document the investigation)
- Consider obtaining an opinion of counsel

**Pre-suit willfulness:** Plaintiff must prove defendant had **actual knowledge** of the patent (not merely constructive notice). Receipt of a demand letter establishes knowledge. The *Read Corp.* factors (applied post-*Halo*) include whether the defendant had a good-faith belief in non-infringement or invalidity.

### Opinion of Counsel

A written, competent opinion of counsel from a qualified patent attorney concluding that the patent is invalid or not infringed provides powerful evidence against willfulness. Key considerations:

| Question | Answer |
|---|---|
| When should we obtain an opinion? | As early as possible after becoming aware of the patent — ideally before or shortly after the complaint |
| Who should author the opinion? | Independent outside patent counsel (not litigation counsel in the case) |
| What must the opinion cover? | Non-infringement analysis AND/OR invalidity analysis; must be thorough, not conclusory |
| Does obtaining an opinion waive privilege? | Potentially yes — reliance on the opinion as a defense may waive privilege over the opinion and related communications; counsel must assess the scope of waiver |
| Is an opinion required? | No — but failing to obtain one weighs in favor of willfulness per *Read Corp.* factor 2 |

🌏 **Korean Company Note:** Opinions from Korean patent attorneys working in the US on US patents may have limited privilege protection in US courts (patent agents and foreign attorneys may not be entitled to attorney-client privilege in the same way US licensed attorneys are). Obtain opinions from US-licensed patent attorneys.

---

## 5. Counterclaim Strategy

### Standard Counterclaims (Always File)
In virtually every patent case, defendant should file counterclaims for:
1. **Declaratory judgment of non-infringement** of the asserted patent(s)
2. **Declaratory judgment of invalidity** of the asserted patent(s)

These counterclaims ensure the case cannot be dismissed as moot by the patentee if the patentee tries to voluntarily dismiss without a final invalidity determination.

### Exceptional Cases: Antitrust and Inequitable Conduct Counterclaims

**Inequitable conduct:** If the patent was procured through intentional withholding of material prior art or material misrepresentations to the USPTO, the entire patent may be rendered **unenforceable**. Standard: *Therasense* (Fed. Cir. 2011) — requires clear and convincing evidence of (1) but-for materiality and (2) specific intent to deceive. Difficult to prove but a complete defense.

**Walker Process antitrust:** If the plaintiff knowingly asserted a patent it obtained through fraud on the USPTO (and meets Sherman Act market power/injury requirements), antitrust damages (trebled) are available. High bar; use carefully.

**Sham litigation (PREI antitrust):** A lawsuit can constitute tortious interference or antitrust violation if it is both objectively baseless AND brought with intent to use the litigation process itself as an anticompetitive weapon. Even higher bar.

### 🌏 Korean Company Counterclaim Opportunity: Cross-License Leverage

For Korean technology companies with significant patent portfolios of their own, **evaluate whether the plaintiff's products infringe any of your patents**. A credible cross-patent claim:
- Creates settlement leverage (mutual threat → cross-license)
- Shifts litigation posture from pure defense to mutual exchange
- Is especially powerful against operating company competitors (less effective against pure NPEs that make no products)

---

## 6. IPR/PGR Parallel Track Decision

A full IPR strategy analysis is covered in [IPR/PGR Strategy & Timing](../03-post-grant-proceedings/ipr-pgr-strategy-and-timing.md). At this early stage, the key decision is:

**Early IPR Go/No-Go:** Should we file an IPR petition?

```
□ Is there strong prior art (§ 102/103 based on patents or publications)?
□ Have we identified at least 2–3 strong references predating the priority date?
□ Is the patent's validity genuinely vulnerable?
□ Have we checked: can we obtain a stay of district court litigation if IPR is instituted?
   (Stay probability: High in NDCA; Low in WDTX/EDTX)
□ Are we within the 1-year deadline? (365 days from service of complaint)
□ Have we analyzed IPR estoppel implications? (Post-Ingenico 2025: product art not estopped)

If YES to most of the above: File IPR petition(s)
```

**Fintiv timing issue (2025):** PTAB has increased discretionary denials of IPR petitions where parallel district court litigation is advanced. Under *Apple v. Fintiv* (PTAB 2020), PTAB considers:
- How close is the trial date? (Too close = denial risk)
- Has the district court case advanced substantially? (SJ motions filed = denial risk)
- Is there overlap between IPR grounds and district court invalidity contentions?

**Best practice:** File IPR petitions **as early as possible** — ideally within 3–6 months of complaint service — to maximize PTAB institution probability and stay leverage.

---

## 9. 2026 Update Addendum: Early Merits Screens for § 101 and Skinny-Label Risk

### A. § 101 Screen for Result-Oriented Functional Claiming

In first-round merits review, flag patents that claim outcomes without concrete technical implementation detail. Where the specification and claim language support it, evaluate an early Rule 12(b)(6) eligibility motion before full claim construction.

### B. Reverse Lesson for Internal Drafting Quality

Coordinate with prosecution counsel to ensure new filings include technical mechanisms/algorithms, not only functional end results, to improve resilience against future § 101 attacks.

### C. Hatch-Waxman / Skinny-Label Compliance (Cross-Functional)

For carved-out generic launches, legal review should extend beyond FDA label text to non-label communications:

- Press releases
- Investor relations decks/calls
- Sales enablement scripts
- Website taxonomy and metadata

Any wording that could be read as encouraging patented use should trigger pre-clearance escalation.

