# Discovery Strategy

> **Quick Reference:** Patent discovery is asymmetric — plaintiffs seek your technical and financial documents; you seek their licensing history and inventor records. Manage your production carefully (scope, privilege, source code protocols) while aggressively pursuing comparable license data that is critical for damages defense.

---

## 1. What Makes Patent Discovery Different

Patent cases involve several categories of discovery unique to IP litigation:

- **Technical documents** (source code, design specs) that require special production protocols
- **Financial data** (product revenue, cost, profit) that directly feeds damages calculations
- **Inventor testimony** (depositions of named inventors — often no longer employed by the plaintiff)
- **Prosecution history** (public, but completeness must be verified)
- **Licensing history** (the most valuable discovery for damages defense — comparable licenses)
- **Standard-essential patent (SEP) records** (if applicable — FRAND rate analysis)

---

## 2. Local Patent Rules: Automatic Disclosures

Most major patent districts have **local patent rules** requiring automatic disclosure of infringement contentions and invalidity contentions on a fixed schedule, without waiting for formal discovery requests.

| Disclosure | Party | Typical Deadline | What Is Required |
|---|---|---|---|
| **Infringement contentions** | Plaintiff | 14–45 days after Rule 26(f) conference | Claim charts mapping each asserted claim to each accused product; identification of accused products |
| **Invalidity contentions** | Defendant | 14–45 days after plaintiff's contentions | Prior art charts for each asserted claim; identification of all § 101, § 102, § 103, § 112 grounds |
| **Claim construction charts** | Both | Per local rules | Each party's proposed constructions for disputed terms |
| **Document production** | Both | Upon serving contentions | Documents supporting contentions (prior art, technical documents) |

**Critical:** Invalidity contentions lock in your prior art positions. Prior art **not identified** in timely invalidity contentions generally **cannot be used** at trial unless leave to amend is granted — courts apply a "good cause" standard and routinely deny late amendments. Invest heavily in the invalidity contentions.

---

## 3. Defendant's Document Production Strategy

### Scope Management

The defendant's goal is to produce documents that are **relevant and proportionate** under Fed. R. Civ. P. 26(b)(1), while minimizing:
- Over-production of competitively sensitive business information
- Waiver of privilege
- Exposure of trade secrets beyond what is needed

**Use a tiered custodian approach:**
1. **Core custodians** (engineers who designed accused feature, product managers): Full production
2. **Peripheral custodians** (tangentially related teams): Narrower scope; negotiate with plaintiff
3. **Senior executives**: Limit to communications directly about the accused product/patent; resist "apex deposition" tactics

### Technical Documents

| Category | Production Strategy |
|---|---|
| **Design specifications and architecture docs** | Produce but redact unrelated product information; mark highly confidential |
| **Source code** | Special protocol required (see below) |
| **CAD/hardware schematics** | Produce with "Highly Confidential — Attorneys' Eyes Only" designation |
| **Bug reports and test results** | Relevant only if they describe the accused feature; scope carefully |
| **Product roadmaps** | Highly sensitive; limit scope to accused feature; redact unrelated business strategy |

### Source Code Production Protocol

Source code requires special protection. Standard provisions in a protective order for source code:
- Production on **dedicated, standalone, air-gapped laptop** (no internet connection)
- Inspection at counsel's office only (no remote access)
- No printing, copying, photographing, or transmitting source code
- Limited number of persons authorized to access (typically outside counsel and retained experts only)
- Log of all access maintained
- Plaintiff's expert may request up to [X] pages of printing per day, with defense review of printouts

🌏 **Korean Company Source Code Note:** For Korean companies, source code may be stored in Korean repositories (e.g., internal Git servers in Korea). Coordinate production logistics between Korea-based IT teams and US outside counsel early. Ensure the protective order addresses source code stored abroad.

### Financial Documents

Plaintiff will request revenue, cost, and profit data for all accused products. This data feeds their damages calculation.

**Defendant's strategy:**
- Produce revenue data **scoped to the accused feature or component**, not the entire product, where feasible
- If product-level revenue is what the accounting system captures, consider whether a feature-level analysis is possible (supports apportionment argument)
- Produce at the level of granularity required by the protective order's "Highly Confidential — Attorneys' Eyes Only" tier
- Do NOT produce forward-looking financial projections unless clearly relevant and ordered by the court

---

## 4. What to Seek from Plaintiff: Priority Discovery

### Comparable Licenses — The Most Valuable Discovery for Damages Defense

The defendant's single most important discovery target is **prior licenses the patentee has granted** on the same patent or comparable patents. Under the Georgia-Pacific framework, prior licenses are the most direct evidence of a reasonable royalty.

**Discovery requests to file:**
- All license agreements covering the asserted patent(s)
- License agreements covering patents in the same family (continuations, divisionals)
- License agreements covering patents in the same technology field (for comparability analysis)
- Settlement agreements that included license components from other litigations involving the same patent
- Correspondence about royalty rates, licensing demands, and negotiations

**Why this matters:** A patentee who licensed the same patent to Defendant A for $0.50/unit cannot credibly demand $5.00/unit from you. If prior licenses exist at lower rates, they are powerful anchors for the damages expert analysis.

### Inventor Records

- Inventor lab notebooks, conception records, and reduction-to-practice documentation
- Communications between inventors and patent prosecution counsel
- Prior publications, presentations, and thesis work by inventors (potential § 102 prior art from inventors themselves)
- Communications between inventors suggesting they were aware of prior art (impeachment)

### Prior Litigation Documents

- Documents produced in prior litigations involving the same patent (if available through PACER)
- Prior claim construction orders involving the same patent — binding? At minimum, persuasive
- Prior damages expert reports involving the same patent (highly valuable for damages cross-examination)

### Claimant's Finances (for NPEs)

For NPE plaintiffs: discover their business model, investor arrangements, and funding sources. Litigation funding agreements may be discoverable if the funder controls litigation strategy (some courts require disclosure).

---

## 5. Key Interrogatories for Patent Defendants

File these interrogatories at the outset of fact discovery:

| Interrogatory | Purpose |
|---|---|
| Identify all persons with knowledge of the conception and reduction to practice of the asserted claims | Identifies inventors and witnesses; sources of § 102 prior invention/prior art knowledge |
| Identify all licenses, covenants not to sue, and settlement agreements related to the asserted patents | Core damages discovery |
| Identify all prior art known to plaintiff or its predecessors before filing the patent application | Potential inequitable conduct / materiality arguments |
| Identify plaintiff's domestic industry for ITC purposes (if parallel ITC proceeding) | ITC domestic industry analysis |
| State the basis for each claim of willful infringement | Forces plaintiff to specify when and how they allege knowledge |
| Identify all prior litigations involving the asserted patents, including all claim construction and invalidity rulings | Issue preclusion research |
| Identify all products or services plaintiff contends practice the asserted patents | Technical prong of domestic industry; FRAND analysis if SEP |

---

## 6. Deposition Strategy

### Inventor Depositions — Critical Targets

Deposing the named inventors is often the highest-value discovery for defendants:

**Goals of inventor depositions:**
1. Establish what was (and was not) actually invented — limits over-broad claim constructions
2. Elicit admissions about prior art the inventor knew about
3. Identify any prior public disclosure or use that predates the patent filing
4. Establish the POSITA skill level (often inventors describe themselves as experts — use this against overbroad claim arguments)
5. Explore conception and reduction-to-practice dates (potentially earlier § 102(g) prior art by others)

**Preparation:** Review all inventor correspondence, lab notebooks, and publications before the deposition. Have prosecution history ready.

### Corporate (30(b)(6)) Deposition Defense

When plaintiff notices a 30(b)(6) deposition of your company, the witness preparation is critical:

- Carefully review and narrow the noticed topics — object to overly broad topics and negotiate scope
- Select witnesses who are well-prepared on their specific topics (don't use one witness for all topics)
- The 30(b)(6) witness's testimony **binds the company** — prepare thoroughly; avoid speculation
- Privilege: the witness may be asked about communications with counsel; prepare the witness to recognize and assert privilege appropriately
- 🌏 For Korean companies: Korean executive witnesses may need interpreter assistance; provide interpreters for both preparation and the deposition itself

### Third-Party Subpoenas

Use Rule 45 subpoenas to obtain:
- Prior art from former employers, universities, or standards bodies
- Comparable license data from prior licensees of the same patent
- Technical documentation from component suppliers whose products are used in the accused device

---

## 7. E-Discovery Management

### Proportionality Arguments

Under Fed. R. Civ. P. 26(b)(1), discovery must be **proportional to the needs of the case**, considering:
- Amount in controversy
- Importance of the issues
- Parties' resources
- Access to the information from other sources
- Burden and expense

Use proportionality to resist overbroad document requests:
- Resist requests for all communications company-wide about the accused product
- Negotiate time period limitations (e.g., limit to 3–5 years before and after patent filing)
- Resist requests for documents in custodians with only tangential relevance

### Protective Order Negotiation

Negotiate a comprehensive protective order at the outset. Key provisions:

| Provision | Defendant's Interest |
|---|---|
| **Confidentiality tiers** | At minimum: "Confidential" and "Highly Confidential — Attorneys' Eyes Only" (AEO); source code tier for code |
| **AEO access list** | Limit access to outside counsel and retained experts only (not plaintiff's in-house team) |
| **Source code protocol** | Air-gapped laptop, no printing without approval, access log |
| **Prosecution bar** | Prohibit plaintiff's prosecution counsel who receive AEO materials from prosecuting related patents |
| **Clawback provision** | FRE 502(d) order confirming that inadvertent production does not waive privilege |

🌏 **Korean Company Protective Order Note:** Request a provision that explicitly addresses cross-border discovery — confirming that production of Korean documents under the order does not constitute a waiver of Korean law protections and that the receiving party will not use such documents in any Korean proceedings without further court order.

---

## 8. Discovery Disputes

### Meet and Confer First

Local rules universally require a good-faith meet and confer before filing any discovery motion. Document the meet and confer in writing (email confirmation).

### Escalation Hierarchy

```
Dispute arises
    │
    ▼
Meet and confer (required): attempt to resolve informally
    │
    ▼ (if unresolved)
Letter to opposing counsel documenting positions
    │
    ▼ (if still unresolved)
Discovery dispute letter to magistrate judge (most districts)
OR motion to compel / motion for protective order
    │
    ▼
Magistrate judge hearing (often by phone)
    │
    ▼ (if adverse ruling)
Objection to district judge (14 days; "clearly erroneous or contrary to law" standard — high bar)
```

**Practical note:** Most discovery disputes are resolved before reaching the magistrate judge. The goal is to have a documented record of reasonable positions — this protects against sanctions and demonstrates good faith to the court.
