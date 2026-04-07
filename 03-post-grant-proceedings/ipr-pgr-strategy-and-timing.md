# IPR/PGR Strategy and Timing

> **Quick Reference:** Filing an IPR petition early (within 3–6 months of the complaint) maximizes both PTAB institution probability and district court stay leverage. In FY2025, the institution rate dropped to 50% — petition quality is now the decisive factor.

---

## 1. The IPR Go/No-Go Decision Framework

Before committing to file an IPR petition (~$75K–$150K per petition), work through this decision tree:

```
Step 1: Timing check
  ├── Calculate the 1-year bar date: service date + 365 days
  ├── Is there sufficient time to prepare a quality petition? (Allow 60–90 days minimum)
  └── Has the one-year window already passed? → IPR is BARRED; consider ex parte reexam instead

Step 2: Prior art quality check
  ├── Have we identified at least 2–3 strong prior art references predating the priority date?
  ├── Are those references patents or printed publications? (Product prior art cannot be used in IPR)
  ├── Does at least one reference anticipate (§ 102) or render obvious (§ 103) the asserted claims?
  └── Are the references truly NOT cumulative of what the examiner already considered?

Step 3: Claim vulnerability assessment
  ├── Are the asserted claims genuinely over-broad given the prior art?
  ├── Did the applicant narrow claims during prosecution (estoppel risk) or are the claims still broad?
  └── Are there multiple independent claims, or only one (concentrates risk)?

Step 4: Estoppel risk analysis
  ├── If we file and receive a FWD, we are estopped in district court from § 102/103 printed-publication grounds
  ├── Do we have STRONGER § 102/103 arguments we want to preserve for district court instead?
  ├── Do we have product-based prior art? (Post-Ingenico 2025: NOT estopped — file IPR AND keep product art)
  └── Is § 101 or § 112 a stronger argument? (Cannot use in IPR; not estopped regardless)

Step 5: Stay probability analysis
  ├── What district is the case in? (See stay rates below)
  ├── How advanced is the district court case? (Early = higher stay probability)
  └── Is the cost savings from a stay worth the IPR investment?

DECISION:
  ├── File IPR: Steps 1–3 all favorable + estoppel risk manageable
  ├── File ex parte reexam instead: Past 1-year bar; want anonymity; lower quality art
  └── Don't file IPR: Prior art is weak; estoppel risk too high; § 101/§ 112 is the better path
```

---

## 2. Fintiv Discretionary Denial Risk — The Critical 2025 Issue

Under *Apple Inc. v. Fintiv, Inc.* (PTAB 2020), the PTAB may **discretionarily deny** IPR institution when parallel district court litigation is too advanced. This has become the dominant reason for denials in FY2025.

### The Six Fintiv Factors

| Factor | Favors Institution (file early) | Favors Denial (case too advanced) |
|---|---|---|
| 1. Stay pending IPR | District court has granted or likely to grant stay | Court refuses stays |
| 2. Trial date | Trial date is far off (>18 months) | Trial scheduled within 12 months |
| 3. Investment in district court | Case just filed; minimal resources spent | Markman completed; discovery underway |
| 4. Overlap with district court | IPR grounds are distinct from district court invalidity contentions | Identical grounds in both forums |
| 5. Parties | Same parties | Same parties (no advantage either way) |
| 6. Merits | Strong petition on the merits | Weak petition |

**FY2025 discretionary denial data:**
- Overall institution rate dropped to **50%** (from 68% in FY2024)
- In Q4 FY2025 (July–Sept), monthly institution rates fell to **20–27%**
- Fintiv-based denials are the primary driver of this decline

### Strategies to Defeat Fintiv Denial

1. **File early** — The single most effective countermeasure. File within 3–6 months of the complaint, before any scheduling order or trial date exists
2. **Move to stay the district court case** simultaneously — A pending or granted stay cuts against Fintiv Factor 1 and 2
3. **Choose non-overlapping grounds** — Use different prior art in the IPR petition than in district court invalidity contentions (Factor 4)
4. **Sotera stipulation** — File a stipulation in district court agreeing not to pursue in district court any grounds raised or that could have been raised in the IPR; courts have found this neutralizes Fintiv concerns (*Sotera Wireless v. Masimo*, PTAB 2020)

🌏 **Korean Company Fintiv Note:** If the Korean company is being sued in W.D. Tex. (12–18 month trial dates), Fintiv Factor 2 is immediately unfavorable. File the IPR **within the first 90 days** of the complaint if at all possible, and simultaneously move to stay the district court case.

---

## 3. Selecting Claims and Grounds for the Petition

### Which Claims to Challenge

**Minimum:** Always challenge the **asserted claims** — i.e., the claims plaintiff is actually relying on in the district court case

**Beyond minimum:**
- Challenge independent claims that would render dependent claims invalid if cancelled
- Consider challenging claims in related continuation patents (same family) that are not yet asserted but could be asserted after the current patent is invalidated
- **Do not** challenge every claim in the patent — PTAB expects focused petitions; challenging marginal claims wastes word count and dilutes the petition's strength

### Anticipation (§ 102) vs. Obviousness (§ 103)

| Ground | When to Use | Advantage | Risk |
|---|---|---|---|
| **§ 102 Anticipation** | Single reference discloses every element | Cleaner; stronger; harder to design around | Requires perfect element-by-element mapping in one reference |
| **§ 103 Obviousness** | Need to combine 2–3 references | More flexible; can capture broader claim scope | Must establish motivation to combine and reasonable expectation of success |

**Best practice:** Lead with § 102 anticipation where available; add § 103 combinations as backup for claims or elements not fully disclosed in a single reference.

### How Many Grounds Per Claim?

PTAB word limits constrain petitions (14,000 words for petition). Typical approach:
- 1–2 § 102 grounds per claim
- 1–2 § 103 grounds per claim (often combining the § 102 reference with a secondary reference)
- Total: 3–4 grounds per claim, 2–4 claims challenged per petition

For multi-claim patents with many asserted claims, consider **multiple petitions** (serial petitioning has been restricted, but parallel petitions filed on the same day covering different claims are permitted).

---

## 4. Coordinating with Co-Defendants

When multiple defendants are sued on the same patent, coordination opportunities exist:

**Joined petitions:** One defendant files, others join (joinder under § 315(c)) within one month of institution. Advantages: share costs; co-petitioners benefit from the same IPR. Limitation: joinder petitioner cannot add new grounds beyond those in the original petition.

**Parallel petitions from different defendants:** Each defendant files their own petition. Advantages: each can include their best prior art; PTAB may deny one but institute the other.

**Coordination pitfalls:**
- Sharing invalidity claim charts between co-defendants **before** filing can create privity issues (affecting the 1-year bar calculation)
- Ensure separate outside PTAB counsel for each entity to maintain distinct RPI status if needed

---

## 5. Petition Structure and Drafting

A well-crafted IPR petition is the single most important factor in institution. PTAB APJs review hundreds of petitions; clarity and focus win.

### Required Petition Elements (37 C.F.R. § 42.104)

1. **Real party in interest** — List all RPIs, including parent companies and controlling entities
2. **Grounds for standing** — Confirm petitioner has not been served with a complaint more than 1 year before filing
3. **Identification of challenged claims** — List each claim being challenged
4. **Grounds of unpatentability** — For each claim: which ground (§ 102 / § 103), which reference(s)
5. **Claim construction** — Petitioner's proposed construction of disputed terms (post-2018: Phillips standard)
6. **Supporting evidence** — Exhibit list with prior art references, expert declaration

### Expert Declaration (Exhibit 1001 / 1002 structure)

An expert declaration is essentially mandatory for a strong petition. The expert should:
- Establish credentials matching the POSITA definition
- Provide the POSITA skill level definition (education + experience)
- Walk through each claim element and how the prior art discloses it
- For § 103: address motivation to combine and reasonable expectation of success
- Avoid conclusory statements — every opinion must be supported by reasoning

### Common Petition Weaknesses (Reasons PTAB Denies Institution)

| Weakness | How to Avoid |
|---|---|
| Prior art was already before the examiner | Only use art NOT cited in the prosecution history, or show examiner misunderstood it |
| Vague motivation-to-combine analysis | Explicitly cite prior art teachings, design needs, or industry standards motivating the combination |
| Claim construction too aggressive | Use Phillips standard; don't over-broaden claims to make them easier to map to prior art |
| Fintiv concerns (trial too close) | File early; consider Sotera stipulation |
| RPI disclosure inadequate | Fully disclose all affiliates, funders, controlling parties |

---

## 6. Motion to Stay District Court Litigation

If PTAB institutes IPR, immediately consider filing a motion to stay the district court case. A stay can save millions in district court litigation costs.

### Three-Factor Stay Test

Courts apply a three-factor balancing test:

| Factor | Analysis |
|---|---|
| **Simplification of issues** | Will IPR likely simplify district court? (Yes if claims cancelled or confirmed) |
| **Stage of litigation** | How far has the district court case progressed? (Earlier = more favorable for stay) |
| **Undue prejudice to patent owner** | Is the patentee a competitor facing market harm? (NPEs rarely face "undue prejudice") |

### Stay Grant Rates by District (Approximate, Recent Data)

| District | Stay Likelihood (Post-Institution) | Notes |
|---|---|---|
| N.D. Cal. | **High (~60–70%)** | Technology-sophisticated judges; favor IPR efficiency |
| D. Del. | **Moderate (~40–50%)** | Varies by judge; Judge Andrews generally skeptical |
| E.D. Tex. | **Low (~20–30%)** | Historically resistant; improving slightly post-2023 |
| W.D. Tex. (Waco) | **Low–Moderate (~25–35%)** | Judge Albright generally reluctant; Federal Circuit has reversed |

**Practical tip:** File the stay motion **within days** of the PTAB institution decision. Delay signals you are not seriously seeking a stay and weakens the argument that the district court case should pause.

---

## 7. PTAB Trial Proceedings: What Happens After Institution

```
Institution Decision (Day 0 of PTAB trial)
        │
        ▼ (3 months)
Patent Owner Response (POR)
• Full written argument with evidence
• May introduce new prior art (to distinguish, not to attack petitioner's art)
• New expert declaration addressing petitioner's arguments
• Motion to Amend (propose substitute claims) — rarely granted; ~15% success rate
        │
        ▼ (3 months)
Petitioner Reply
• Responds to POR; cannot introduce new grounds
• Supplemental expert declaration
        │
        ▼ (1 month)
Patent Owner Sur-Reply (limited)
        │
        ▼
Oral Argument (upon request — almost always granted)
• Each side: 20–30 minutes before 3-APJ panel
• APJs ask pointed questions about claim construction and prior art mapping
        │
        ▼ (by 12-month statutory deadline)
Final Written Decision (FWD)
```

### Oral Argument Strategy

- APJs have read all briefs thoroughly — don't repeat the written argument
- Prepare to be challenged on your **weakest** elements
- Practice answering: "Isn't your motivation-to-combine argument just hindsight?"
- For petitioner: be prepared to defend why institution was correct; address patent owner's best arguments directly

---

## 8. Settlement During IPR and Post-IPR Strategy

### Settlement During IPR

IPR can be terminated by joint motion if the parties reach a settlement. Key points:
- PTAB may still issue a FWD even after settlement if it believes it serves the public interest
- A settlement that terminates an IPR does NOT eliminate estoppel if a FWD was already issued
- Settlement licenses negotiated in the shadow of IPR often reflect reduced royalty rates

### After a Favorable FWD (Claims Cancelled)

- Cancelled claims are **automatically** unenforceable — no separate district court motion needed
- If the district court case was stayed: jointly notify the court; case is likely dismissed as moot
- If not stayed: move for summary judgment of non-infringement (no valid claim to infringe)
- Patent owner may appeal the FWD to the Federal Circuit (standard: substantial evidence for factual findings; de novo for legal conclusions)

### After an Unfavorable FWD (Claims Confirmed)

- § 315(e) estoppel now applies in district court for all grounds raised or reasonably could have been raised
- Post-*Ingenico* (2025): product prior art, prior use, and on-sale bar remain available in district court
- § 101 and § 112 grounds remain available in district court (were never raiseable in IPR)
- Appeal the FWD to the Federal Circuit within 63 days of the FWD

🌏 **Korean Company Post-IPR Note:** If the PTAB cancels the asserted claims, Korean companies should immediately seek dismissal or summary judgment in district court AND evaluate whether related continuation patents in the same family are also vulnerable to IPR challenge (NPEs frequently hold continuation patent families where some claims may survive even if the primary patent is invalidated).

---

## 8. 2026 Update Addendum: PTAB Realignment and Estoppel-Limited Playbooks

### A. Replace "IPR-First" with a Portfolio of Parallel Validity Attacks

As of Q1 2026, many defense teams have shifted from a default IPR-first approach to a split-track plan because institution outcomes are materially less predictable than in prior years. Manual users should run a budget-and-risk branch at case intake:

- **Branch 1 (IPR path):** Use only when prior art is non-cumulative and merits are strong enough to survive discretionary denial scrutiny
- **Branch 2 (District-court invalidity path):** Assume no stay and no institution; build full invalidity record from day one
- **Branch 3 (EPR supplement):** Preserve an ex parte reexamination option as a low-estoppel pressure tool

| Technology sector (post-Mar. 2025 trend) | Observed institution range | Defense planning implication |
|---|---|---|
| Electrical / Electronics | ~29% | File only with strongest art; district-court backup is mandatory |
| Mechanical / Business methods | ~44% | Selective filing; prioritize grounds likely to survive discretionary screens |
| Biopharma / Chemical | ~56% | IPR remains relatively viable but still requires a no-institution contingency |

### B. Estoppel Management After *Ingenico* (Fed. Cir. 2025)

Update internal estoppel checklists to reflect that § 315(e) estoppel is tied to legal grounds, not all possible reuse of the same printed publications in every context. In parallel district-court workups, coordinate with trial counsel on whether shared references can support distinct non-IPR theories (for example, product/prior-use/on-sale frameworks where factually supportable).

### C. Include EPR as a Deliberate Fallback, Not a Last Resort

Where IPR institution risk is elevated, include an EPR decision gate in the first 60–90 day playbook. The objective is to avoid all-or-nothing reliance on PTAB institution and maintain pressure on validity through multiple forums.

