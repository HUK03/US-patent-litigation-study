# Initial Case Assessment

> **Quick Reference:** A complaint has been served. You have 21 days to answer (extensions are routinely available but must be requested immediately). This document covers what to do in the first two weeks and how to frame a realistic initial assessment for management.

---

## 1. First Two Weeks After Service: Action Checklist

### Day 1–3
- [ ] Confirm date and method of service; calendar **21-day answer deadline**
- [ ] Immediately contact pre-designated outside patent litigation counsel (or begin RFP process)
- [ ] Issue / confirm litigation hold notice (see [Litigation Hold](../01-pre-litigation/litigation-hold-evidence-preservation.md))
- [ ] Obtain extension of time to answer (typically 30–60 additional days by stipulation; file motion if needed)
- [ ] Begin IPR petition clock calculation: **365 days from date of service** (35 U.S.C. § 315(b))
- [ ] Obtain complaint, patent(s), and exhibits from court docket (PACER)
- [ ] Identify which claims are asserted (if not specified, plaintiff must identify later per local patent rules)
- [ ] Identify the accused product(s) and map them to business units

### Day 3–7
- [ ] Internal kickoff meeting with IP counsel, litigation counsel, and business unit leads
- [ ] Assign responsibilities: technical analysis, financial data gathering, prior art search
- [ ] Begin prosecution history review (download from USPTO Patent Center)
- [ ] Conduct preliminary invalidity search (§ 101, § 102, § 103, § 112)
- [ ] Begin preliminary claim mapping: do the claim elements read on accused product?
- [ ] Identify the litigation venue (district court) and review applicable local patent rules
- [ ] Check for co-defendants: are other companies sued on the same patent? Possible coordination?

### Day 7–14
- [ ] Draft preliminary case assessment memo (template below)
- [ ] Develop phase-gated litigation budget estimate
- [ ] Determine whether to file § 101 motion early (Alice/Mayo challenge)
- [ ] Make preliminary IPR go/no-go decision (full analysis due before 365-day deadline)
- [ ] Brief management/board as appropriate (document briefing; maintain privilege)
- [ ] 🌏 If ITC Section 337 complaint was filed simultaneously, coordinate both defenses immediately

---

## 2. Internal Kickoff Meeting Agenda Template

```
PATENT LITIGATION KICKOFF MEETING
[PRIVILEGED AND CONFIDENTIAL]

Date: ___________
Attendees: IP Counsel, Litigation Counsel, Business Unit Lead, Engineering Lead, Finance

1. Case Overview (15 min)
   • Complaint summary: plaintiff, patents asserted, accused products
   • Key dates: answer deadline, IPR deadline, estimated trial date
   • Venue: district, assigned judge, relevant local patent rules

2. Business Unit Briefing (20 min)
   • What is the accused product/feature? When was it launched?
   • Who designed/built it? (Identify custodians for litigation hold)
   • Are there design documents, prior art from our own R&D?
   • Is the accused feature core or peripheral to the product?

3. Preliminary Legal Analysis (15 min)
   • First impression: Is infringement colorable?
   • Any obvious invalidity grounds?
   • IPR viability: Are there strong § 102/103 prior art references?
   • § 101 Alice challenge feasibility?

4. Immediate Actions (10 min)
   • Confirm litigation hold is in place
   • Assign tasks: technical analysis, prior art search, financial data
   • Outside counsel engagement and budget authorization

5. Next Steps and Timeline
   • Who does what by when
   • Next check-in date
```

---

## 3. Reading the Complaint

### Identifying the Asserted Claims
Patent complaints often assert the patent generally without specifying which claims are infringed. Under most district courts' local patent rules:
- **Plaintiff must serve infringement contentions** within a set period (typically 14–45 days after the Rule 16 conference), including claim charts mapping each accused product to each asserted claim
- Until infringement contentions are served, you are defending against the entire patent
- Early focus: read **independent claims** (usually claim 1, and any other independent claims), as dependent claims require proving the independent claim first

### Understanding the Claim Structure
```
Independent Claim (e.g., Claim 1):
  "A [device/method/system] comprising:
   [Element A];
   [Element B]; and
   [Element C]."

Dependent Claim (e.g., Claim 3):
  "The [device] of claim 1, wherein [Element B] further comprises [D]."
```

To infringe a claim, every element of that claim must be present in the accused product (the "all-elements rule"). The absence of even one claim element = no literal infringement. However, the "doctrine of equivalents" may still apply if the accused product performs substantially the same function in substantially the same way to achieve substantially the same result.

### Identifying the Damages Theory
The complaint should indicate (at least broadly) the type of damages sought:
- "Damages in an amount to be proven at trial" — standard (could be reasonable royalty or lost profits)
- Injunctive relief — particularly threatening for operating companies; NPEs rarely obtain injunctions post-*eBay*
- Enhanced damages (willful infringement) — check whether pre-suit knowledge is alleged
- Attorney's fees under § 285 (exceptional cases)

---

## 4. Preliminary Invalidity Analysis

Invalidity is one of the most powerful defenses. A patent is invalid if it fails to meet any statutory requirement.

### § 102 — Anticipation (Prior Art)
A claim is anticipated if a **single prior art reference** discloses every element of the claim. Key prior art sources:
- Prior patents and published patent applications (US and foreign)
- Academic papers and conference proceedings
- Product manuals, datasheets, technical specifications
- **Company's own prior products, publications, and presentations** (frequently overlooked but highly valuable — our own prior art is the most credible)
- Open source code repositories (GitHub commit histories with dates)
- Industry standards documents

**Priority date:** Prior art must predate the patent's **priority date** (usually the earliest filing date in the patent family, not necessarily the issue date). Always verify the actual priority date from the prosecution history.

### § 103 — Obviousness
A claim is obvious if it would have been obvious to a **person of ordinary skill in the art (POSITA)** at the time of the invention, in light of the prior art (including combinations of multiple references).

Defense arguments:
- Two or more prior art references together disclose all claim elements
- Motivation to combine the references existed (established by design need, common knowledge, or explicit suggestion in prior art)
- No reasonable expectation of success would have discouraged the combination

### § 101 — Patent-Eligible Subject Matter (Alice/Mayo)
Under *Alice Corp. v. CLS Bank* (2014) and *Mayo Collaborative Services v. Prometheus* (2012):
1. **Step 1:** Is the claim directed to an abstract idea, natural phenomenon, or law of nature?
2. **Step 2:** If yes, does the claim add "something more" — an inventive concept that transforms the nature of the claim?

Software, AI/ML, and business method patents are especially vulnerable. **Recent 2025 precedent:** *Recentive Analytics, Inc. v. Fox Corp.* (Fed. Cir. April 2025) held that applying **known machine learning methods to a new data domain** is patent-ineligible under § 101 — merely applying generic ML models does not represent a "technological improvement."

**Filing timing for § 101 motion:** Early § 101 challenges (Rule 12(b)(6) or early summary judgment) are often cost-effective — decided on the pleadings without full discovery — but success depends heavily on how the claims are written. Consult outside counsel on district-specific § 101 success rates.

### § 112 — Written Description, Enablement, and Definiteness
- **Written description:** The specification must demonstrate the inventor actually possessed the claimed invention at the time of filing. Relevant for later-filed continuation claims that are broader than what the specification describes
- **Enablement:** The specification must enable a POSITA to make and use the full scope of the claimed invention without undue experimentation
- **Definiteness** (*Nautilus v. Biosig*, 2014): Claims must be definite enough that a POSITA would understand the scope of the claims with **"reasonable certainty"**. Vague functional claim language is especially vulnerable

---

## 5. Preliminary Non-Infringement Analysis

### Claim Element Mapping

For each asserted claim, map each claim element against the accused product:

| Claim Element | Present in Product? | Source of Evidence | Risk Level |
|---|---|---|---|
| [Element A as construed broadly] | Yes / No / Uncertain | [Design doc, source code, datasheet] | High / Med / Low |
| [Element B] | ... | ... | ... |
| [Element C] | ... | ... | ... |

**If ANY element is absent:** No literal infringement. But analyze doctrine of equivalents (DOE) — does the product perform substantially the same function, in substantially the same way, to achieve substantially the same result?

### Common Non-Infringement Arguments

1. **Missing element:** The accused product lacks a required claim element
2. **Different construction:** Under the proper (narrow) construction of a term, the accused product does not satisfy the element
3. **Method claim all-steps rule:** For method claims, all steps must be performed by the defendant (or attributable to the defendant under *Akamai* joint infringement analysis)
4. **Prosecution history estoppel:** Plaintiff narrowed claims during prosecution to overcome prior art; cannot now expand scope through DOE
5. **Product versus process:** Accused product is made by a different process than claimed

---

## 6. Outside Counsel Selection and Budget

### Outside Counsel Selection Criteria

| Criterion | What to Evaluate |
|---|---|
| **Technology expertise** | Does the firm have partners with deep technical background matching the accused technology (electrical/software/mechanical)? |
| **Litigation track record** | Win rates in the asserted venue? Federal Circuit success rate? |
| **PTAB experience** | IPR petition success rate? (Critical — must file within 1 year) |
| **Venue experience** | Do they regularly practice in the district where the case is pending? |
| **In-house communication style** | Responsive to in-house requests? Will they explain strategy clearly? |
| **Staffing model** | Who actually does the work — partners or associates? |
| **Fee structure** | Hourly? AFA (alternative fee arrangement)? Hybrid capped fee? |

🌏 **Korean Company Note:** Select outside counsel with **Korean-speaking staff or Korea-desk capabilities** — essential for reviewing Korean-language documents, coordinating with Korea-based engineers and executives, and managing international discovery logistics. Major US patent litigation firms (e.g., Kirkland & Ellis, Quinn Emanuel, Gibson Dunn) have dedicated Korea-desk practices.

### Phase-Gated Litigation Budget Template

| Phase | Estimated Cost | Trigger / Decision Point |
|---|---|---|
| Case initiation & early motions | $100K–$300K | Complaint served |
| IPR petition (if filed) | $75K–$150K/petition | Decision due by Day 365 |
| Claim construction / Markman | $200K–$500K | Scheduling order entered |
| Fact discovery | $500K–$2M | Post-Markman |
| Expert reports | $400K–$1M | Post-fact discovery |
| Summary judgment | $200K–$600K | Post-expert discovery |
| Trial | $500K–$3M | Post-SJ rulings |
| Post-trial / appeal | $200K–$800K | After verdict |
| **Total estimated range** | **$2M–$8M+** | |

---

## 7. Case Assessment Memo Template

Circulate this memo (marked Privileged) within 14 days of receiving the complaint:

```
PRELIMINARY CASE ASSESSMENT MEMORANDUM
[PRIVILEGED AND CONFIDENTIAL — ATTORNEY-CLIENT COMMUNICATION]

To: [Management/Legal Leadership]
From: IP Counsel / Outside Counsel
Date: [Date]
Re: [Plaintiff] v. [Company], [District] — Patent No. [X]

EXECUTIVE SUMMARY
[2–3 sentence summary of the case and key recommendation]

1. CASE BACKGROUND
   • Plaintiff: [identity, type — NPE/competitor/individual]
   • Patents asserted: [numbers, titles, technology]
   • Accused products: [description, revenue]
   • Venue: [district, judge, local rules summary]
   • Key dates: Answer [date], IPR deadline [date], estimated trial [year]

2. INVALIDITY ASSESSMENT
   Strength: [ ] Strong  [ ] Moderate  [ ] Weak
   Best grounds: [§ 101 / § 102 / § 103 / § 112]
   IPR viability: [ ] Yes — file  [ ] Possible — investigate  [ ] No
   Notes: [prior art summary]

3. NON-INFRINGEMENT ASSESSMENT
   Strength: [ ] Strong  [ ] Moderate  [ ] Weak
   Key arguments: [missing elements, claim construction]
   Notes: [preliminary claim chart summary]

4. DAMAGES EXPOSURE
   Accused product US revenue: $[X] (past 6 years)
   Estimated reasonable royalty range: $[X] – $[Y]
   Willfulness risk: [ ] High  [ ] Medium  [ ] Low
   Injunction risk: [ ] High  [ ] Low (NPE cases: very low post-eBay)

5. SETTLEMENT ANALYSIS
   Estimated litigation cost to trial: $[X]
   Settlement range analysis: $[X] – $[Y]
   Recommendation: [ ] Pursue settlement  [ ] Defend through discovery  [ ] Defend to verdict

6. RECOMMENDED ACTIONS
   Immediate (within 30 days):
   □ File IPR petition(s)
   □ File § 101 motion
   □ Begin invalidity search
   □ Other: ___
   
   Short-term (30–90 days):
   □ Respond to infringement contentions
   □ Prepare invalidity contentions
   □ Other: ___

7. BUDGET
   Phase 1 (initiation through Markman): $[X]
   Phase 2 (discovery): $[X]
   Phase 3 (trial): $[X]
   IPR petition (separate): $[X]
   Total estimated: $[X]

Outside counsel: [Firm], lead partner [Name]
```
