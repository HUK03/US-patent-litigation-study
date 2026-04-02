# US Patent Litigation: Lifecycle Overview

> **Quick Reference:** This document provides orientation on the full patent litigation lifecycle for defendants. Use it to understand where you are in a case, what comes next, and who needs to be involved at each stage.

---

## 1. The US Patent Litigation Landscape for Defendants

### Volume and Stakes

US patent litigation is the most costly and complex form of intellectual property dispute in the world. Key facts for corporate defendants:

- Over **3,500 patent suits** are filed in US federal district courts annually
- The median cost to defend a patent case through trial exceeds **$3–5 million** (and frequently $10–30M+ for high-stakes cases)
- **NPEs (Non-Practicing Entities / "patent trolls")** file the majority of suits against large technology and electronics companies
- The average time from filing to trial in major patent districts ranges from **2.5 to 4+ years** (district court); ITC proceedings resolve in **10–12 months**

### Who Sues Large Corporations

| Plaintiff Type | Description | Typical Goal | Defense Priority |
|---|---|---|---|
| **NPE / Patent Troll** | Holds patents, does not make products | Licensing revenue / settlement | Invalidity (IPR), non-infringement, damages apportionment |
| **Patent Assertion Entity (PAE)** | Sophisticated NPE with litigation-as-business model | Maximum damages or portfolio license | All of the above + early settlement analysis |
| **Competitor** | Operating company in same market | Injunction, damages, leverage | Non-infringement, cross-license, countersuits |
| **Inventor/University** | Original patent holder asserting rights | Licensing, recognition | Invalidity, prosecution history estoppel |
| **Standard Body Licensors** | Holders of SEPs (Standard Essential Patents) | FRAND royalties | FRAND rate defense, SSPPU apportionment |

### 🌏 Korean/Foreign Company Alert

Korean companies — particularly Samsung, LG, SK, and Hyundai/Kia group entities — are among the **most targeted defendants by NPEs** in the US. Samsung faces a new NPE patent suit approximately every 5 days and was the single most-targeted large company as of 2024 (208 of 404 cases against it filed by NPEs). Foreign companies have **no TC Heartland venue protection** and can be sued in any US district. See [Venue & Jurisdiction](../02-case-initiation/venue-and-jurisdiction.md).

---

## 2. Litigation Lifecycle: Text Flowchart

The following represents the typical lifecycle of a defended patent case. Items in `[brackets]` indicate parallel proceedings that may run simultaneously with district court litigation.

```
THREAT RECEIVED
(Demand letter / C&D / notice of infringement)
        │
        ▼
PRE-LITIGATION PHASE
• Threat triage and assessment
• Litigation hold issued (if suit reasonably anticipated)
• Patent/claimant background research
• Preliminary infringement & validity analysis
• Declaratory judgment strategy consideration
        │
        ▼
COMPLAINT FILED & SERVED
• Answer deadline: 21 days (extension available)
• Litigation hold confirmed and expanded
• Outside counsel retained / activated
• Initial case assessment memo drafted
• [ITC § 337 Investigation may be filed simultaneously]
        │
    ┌───┴───────────────────────────────────┐
    ▼                                       ▼
DISTRICT COURT                     [IPR / PGR at PTAB]
LITIGATION                          • File within 1 year of service
                                    • Petition filing: ~$50–150K
                                    • Institution decision: ~6 months
                                    • FWD: 12 months after institution
                                    • [Motion to Stay district court]
    │
    ▼
CASE INITIATION (Months 1–6)
• Rule 26(f) conference
• Scheduling order negotiated
• Local patent rules: infringement contentions (plaintiff)
• Local patent rules: invalidity contentions (defendant)
• Early case strategy finalized
• § 101 motion filed (if Alice challenge available)
        │
        ▼
CLAIM CONSTRUCTION (Markman) (Months 6–18, varies by district)
• Claim terms identified and briefed
• Markman hearing before judge
• Claim construction order issued
• Strategy adjusted based on ruling
        │
        ▼
FACT DISCOVERY (Months 6–24)
• Document production (both sides)
• Source code review
• Interrogatories / requests for admission
• Inventor depositions
• Corporate (30(b)(6)) depositions
• Third-party subpoenas
        │
        ▼
EXPERT DISCOVERY (Months 18–30)
• Opening expert reports (infringement, invalidity, damages)
• Rebuttal expert reports
• Expert depositions
• Daubert motions (to exclude experts)
        │
        ▼
SUMMARY JUDGMENT (Months 24–36)
• Motions for SJ on non-infringement and/or invalidity
• SJ opposition and reply
• Hearing and ruling
        │
        ▼
PRE-TRIAL (Months 30–42)
• Pre-trial order
• Motions in limine
• Jury instructions negotiated
• Exhibit lists finalized
• Voir dire questions prepared
        │
        ▼
TRIAL (typically 5–10 days)
• Jury selection (voir dire)
• Opening statements
• Plaintiff's case (infringement, damages)
• Defendant's case (non-infringement, invalidity, damages defense)
• Closing arguments
• Jury deliberations
• Verdict
        │
        ▼
POST-TRIAL (Months 1–6 after verdict)
• JMOL motion (Rule 50(b)) — attack legally insufficient verdict
• New trial motion (Rule 59)
• Enhanced damages briefing (if willfulness found)
• Attorney fee motion (§ 285)
• Injunction proceedings (eBay four-factor test)
        │
        ▼
APPEAL TO FEDERAL CIRCUIT
• Notice of appeal: 30 days from final judgment
• Briefing: ~12–18 months
• Oral argument (usually 15 minutes per side)
• Decision: typically 6–12 months after argument
        │
        ▼
(POSSIBLE REMAND / SUPREME COURT CERTIORARI)
```

---

## 3. Key Decision Points and Gate Reviews

Use this table at each major milestone to assess whether to continue fighting, shift strategy, or pursue settlement.

| Gate | Trigger | Key Question | Criteria for Continued Defense | Document |
|---|---|---|---|---|
| **G-1: Pre-Suit** | Demand letter received | Fight or engage? | Strong invalidity/non-infringement; DJ jurisdiction; high damages exposure | [Threat Assessment](../01-pre-litigation/threat-assessment.md) |
| **G-2: Complaint Filed** | Complaint served | IPR? Which defense theory? | Prior art availability; claim scope; one-year clock | [IPR/PGR Strategy](../03-post-grant-proceedings/ipr-pgr-strategy-and-timing.md) |
| **G-3: Post-Markman** | Claim construction order | Did constructions help or hurt? | Unfavorable construction → reassess; design-around possible? | [Claim Construction](../04-claim-construction/claim-construction-strategy.md) |
| **G-4: Post-Expert Reports** | Exchange of opening reports | Can we win on the merits? | Strong expert opinions; damages exposure quantified | [Expert Witnesses](../06-expert-witnesses/expert-witness-management.md) |
| **G-5: Pre-Trial** | SJ rulings complete | Trial risk assessment | Key issues remain; jury risk manageable; litigation cost justified | [Trial Preparation](../09-trial-preparation/trial-preparation-guide.md) |
| **G-6: Post-Verdict** | Jury verdict | Appeal? | Legal errors preserved; likelihood of reversal >30%; product still at issue | [Appeals Guide](../10-appeals/appeals-guide.md) |

---

## 4. Parallel Proceedings: District Court and PTAB

One of the most important strategic decisions is whether to **file IPR/PGR petitions at the USPTO Patent Trial and Appeal Board (PTAB)** while defending the district court case. These proceedings run in parallel and interact in critical ways.

```
District Court Case                    PTAB (IPR/PGR)
─────────────────                      ──────────────
Complaint filed (Day 0)
                                       ← IPR petition deadline: 365 days
IPR filed (e.g., Day 180)
                                       Institution decision (~Day 360)
Markman hearing (~Month 12)           ──────── Motion to Stay ──────────→
                                       PTAB trial begins (~Month 18)
Fact discovery (~Months 12–24)
                                       Final Written Decision (~Month 30)
Expert discovery (~Months 24–30)
                                       ← Cancellation affects district court
Summary judgment (~Months 28–36)
```

**Critical interaction points:**
- A successful IPR can **cancel asserted claims**, mooting the district court case
- An **IPR estoppel** (§ 315(e)) prevents the petitioner from raising in district court any invalidity ground that "was raised or reasonably could have been raised" in the IPR — but *Ingenico Inc. v. IOENGINE* (Fed. Cir. May 2025) held this estoppel applies **only to § 102/103 printed publication grounds**, not to product prior art, public use, or on-sale invalidity
- A **stay of district court proceedings** pending IPR can save millions in litigation costs — but success rates vary dramatically by district (see [IPR/PGR Strategy](../03-post-grant-proceedings/ipr-pgr-strategy-and-timing.md))

---

## 5. Roles and Responsibilities Matrix

| Activity | In-House IP Counsel | In-House Litigation Counsel | Business Unit / Engineering | Outside Counsel | Management/Board |
|---|---|---|---|---|---|
| Threat triage | **Lead** | Consult | Inform | Consult | Brief |
| Litigation hold | Lead | **Lead** | Comply | Advise | N/A |
| Outside counsel selection | **Lead** | Co-lead | N/A | N/A | Approve (large cases) |
| Budget approval | Recommend | Recommend | N/A | Provide estimates | **Approve** |
| IPR petition decision | **Co-lead** | Consult | N/A | **Co-lead** | Brief |
| Technical/prior art analysis | Consult | N/A | **Lead** | Lead | N/A |
| Settlement authority | Recommend | Recommend | Input | Advise | **Approve** |
| Trial decisions | Consult | **Lead** | Support | **Lead** | Approve major decisions |

---

## 6. Cost and Resource Expectations by Phase

The following are **rough order-of-magnitude** estimates for a moderately complex district court patent case (single patent, medium-value product). High-stakes cases (multi-patent, multi-billion dollar products) can be 3–5x higher.

| Phase | Typical Cost Range | Key Cost Drivers |
|---|---|---|
| Pre-litigation threat assessment | $15K–$50K | Invalidity search depth, complexity of technology |
| Case initiation & early motions | $100K–$300K | § 101 motions, answer preparation |
| IPR petition (if filed) | $50K–$150K per petition | Number of claims challenged, expert declaration |
| Claim construction / Markman | $150K–$400K | Number of terms, tutorial preparation |
| Fact discovery | $500K–$2M | Volume of documents, number of depositions |
| Expert reports & depositions | $300K–$1M | Number of experts, complexity of technical/damages issues |
| Summary judgment | $200K–$600K | Number of motions, complexity |
| Trial | $500K–$2M+ | Length, number of witnesses, demonstratives |
| Post-trial & appeal | $200K–$800K | Complexity of legal issues |
| **Total (typical range)** | **$2M–$8M** | |
| **High-stakes case** | **$10M–$30M+** | |

> These figures reflect outside counsel fees only. Internal costs (management time, IT, translation for foreign companies) add significantly.

---

## 7. The ITC Section 337 Track

For foreign companies importing products into the US, an **ITC Section 337 investigation** can run alongside — or instead of — district court litigation. Key differences:

| Feature | District Court | ITC Section 337 |
|---|---|---|
| Time to hearing | 2–5 years | **10–12 months** |
| Remedy | Damages + injunction | **Import ban (exclusion order)** — no damages |
| Summary judgment | Common | Rare (summary determination) |
| Burden of proof (invalidity) | Clear and convincing | Clear and convincing |
| Settlement rate | ~95% | ~55% |
| Domestic industry required? | No | **Yes** (technical + economic prong) |
| Presidential review | No | Yes (60-day review period) |
| Parallel PTAB proceedings | Yes | Yes (IPR highly recommended) |

🌏 For Korean companies, the ITC is especially important because: (1) products are often manufactured abroad and imported into the US; (2) the fast track creates intense settlement pressure; and (3) Korean companies increasingly use the ITC offensively (e.g., Samsung Display's exclusion order against BOE for OLED patent infringement and trade secret misappropriation, settled November 2025).
