# Design-Arounds and Defensive Patent Portfolio

> **Quick Reference:** A design-around is the most complete solution to a patent threat — it eliminates ongoing infringement, removes injunction risk, and cuts off future damages. A strong defensive patent portfolio provides cross-license leverage against competitors and deters NPE targeting. Both require long-term investment and coordination between legal and engineering teams.

---

## 1. Design-Arounds as a Litigation Defense Tool

A design-around modifies the accused product so that it no longer practices the patent claims — either by removing a claimed element, performing a claimed function in a different way, or using an alternative technology.

### Why Design-Arounds Matter

1. **Eliminates ongoing infringement:** Once implemented, damages for future sales stop accruing
2. **Removes injunction risk:** A successful design-around moots any injunctive relief claim
3. **Reduces damages exposure:** Limits damages to the pre-design-around period
4. **Evidence of good faith:** Prompt implementation weighs against willfulness and enhanced damages
5. **Settlement leverage:** Demonstrating a viable design-around reduces plaintiff's negotiating power

### When to Initiate Design-Around Work

| Timing | Scenario | Notes |
|---|---|---|
| **Before suit (FTO stage)** | Ideal — design changes are cheapest during development | Privilege protected from inception; no past damages period |
| **After demand letter** | Good — before suit is filed; damages period not yet running | Implement promptly; document the decision and timeline |
| **After complaint filed** | Acceptable — stops accrual of future damages | Past infringement damages still apply to pre-design-around sales |
| **After Markman ruling** | Triggered by adverse construction | Court's interpretation guides which elements to avoid |
| **During/after trial** | Late but still valuable for injunction defense | Shows remediation effort; can inform ongoing royalty rate |

---

## 2. Design-Around Methodology

### Step 1: Map the Claims to Be Avoided

Work from the asserted claims (particularly after Markman, from the court-construed claims):
- List every **element** of each independent claim
- Identify which elements are present in the accused product
- For each present element: can it be removed, modified, or replaced?

```
Claim element analysis:
  Element A: [present in product] → Can we remove it? → Alternative: [non-infringing approach]
  Element B: [present in product] → Can we modify it? → Alternative: [different implementation]
  Element C: [not present] → No action needed
  Element D: [present in product] → Can we substitute? → Alternative: [prior art approach]
```

**Target:** Remove or change at least ONE element of EACH independent claim being asserted. Absence of any single element eliminates literal infringement of that claim.

### Step 2: Evaluate Design-Around Options

For each claim element to be avoided, evaluate alternatives:

| Alternative | Technical Feasibility | Time to Implement | Legal Risk |
|---|---|---|---|
| Remove the feature entirely | High (if feature is non-essential) | Low | Lowest (element absent) |
| Implement using prior art method | High | Low–Medium | Low (if prior art predates patent) |
| Implement in structurally different way | Medium (requires engineering) | Medium | Medium (DOE risk if "substantially same") |
| Implement using licensed technology | High | Low–Medium | Low (if license scope is clear) |

### Step 3: Legal Review of Design-Around

The engineering team must work **with and through IP counsel** on the design-around. Do NOT have engineers independently develop and implement design-arounds without legal guidance — the legal analysis of whether the design-around actually avoids infringement is critical.

**Privilege protection during design-around work:**
- All communications between engineers and IP counsel about the design-around are **attorney-client privileged** — keep them that way
- Engineers should NOT document their own infringement/non-infringement analysis in emails or documents
- IP counsel should direct the technical investigation: "Please advise me on the technical feasibility of [alternative approach] so I can provide legal advice"

### Step 4: Legal Opinion on Design-Around Adequacy

Obtain a written opinion from outside patent counsel confirming the design-around does not infringe:
- Same standards as an FTO opinion
- Must address both literal infringement and doctrine of equivalents
- Should address all asserted claims, including dependent claims that may cover the new design

### Step 5: Implementation and Documentation

- Document the design-around implementation date precisely (this is the date damages stop for the new design)
- Retain version control records, build logs, and deployment records proving when the new version shipped
- If possible, obtain a **covenant not to sue** from the plaintiff covering the design-around (as part of settlement)
- Update product documentation to reflect the new implementation

---

## 3. Building a Defensive Patent Portfolio

### Why Defensive Patents Matter for Large Companies

A strong patent portfolio serves multiple defensive functions:

| Function | How Defensive Patents Help |
|---|---|
| **Cross-license leverage** | When a competitor sues you, your patents give you the ability to countersue and negotiate a mutual cross-license — often resolving both suits without payment |
| **Deterrence** | A large portfolio deters competitors from filing offensive suits (they know you can countersue) |
| **NPE defense** | NPEs are less deterred by your patents (they make no products to be enjoined), but a large portfolio increases the NPE's risk of an IPR counter-challenge from your portfolio |
| **Injunction defense** | Your own portfolio can be used offensively via ITC to create leverage if a competitor seeks an injunction against you |

### Portfolio Building Strategy

**Identify technology gaps:** Map your patent portfolio against your core product technology areas. Where are you weak? Where are competitors strong?

**File continuations strategically:** Continuation applications claiming different aspects of your innovations keep options open as the competitive landscape evolves. Your own continuation strategy mirrors the threat you face from NPE continuation filings.

**Acquire defensive patents:** Consider acquiring patents that:
- Block competitors' key products
- Cover technology areas where NPEs are active
- Can be used as cross-license currency with known patent-aggressive companies

### Defensive Patent Aggregator Programs

Several organizations exist specifically to provide patent defense through pooled portfolios:

| Organization | Model | Best For |
|---|---|---|
| **LOT Network** (License on Transfer) | Members grant each other a license if a patent is transferred to an NPE | Broad protection from transferred patents; largest network (>4,000 members) |
| **Open Invention Network (OIN)** | Free royalty cross-license for Linux-related patents among members | Linux/open-source technology users; free to join |
| **Unified Patents** | Collective IPR challenges to bad NPE patents; zone memberships | Targeted defense against specific NPEs; cost-efficient IPR |
| **RPX Corporation** | Acquires and licenses patents from NPEs; member companies get broad licenses | Comprehensive NPE defense program; fee-based membership |

🌏 **Korean Company Portfolio Recommendation:** All major Korean technology companies should be members of LOT Network and OIN, and should evaluate RPX membership. Samsung, LG, and SK have large existing portfolios but should evaluate Unified Patents zone memberships to cost-efficiently challenge NPE patents in their key technology sectors (OLED displays, memory, 5G, NAND flash, etc.).

---

## 4. Patent Marking Compliance

Under 35 U.S.C. § 287, a patent owner cannot recover **pre-suit damages** unless:
1. The patented product was marked with the patent number, OR
2. The infringer had actual notice of the infringement

For defendants, this means: **failure to mark by the patent holder reduces damages exposure**. If the plaintiff or its licensees sell a patented product without proper marking, the damages period starts only from the date of actual notice (demand letter or complaint), not from the actual start of infringement.

**Investigate marking compliance:**
- Does the plaintiff or its licensees sell products practicing the asserted patent?
- If so, are those products properly marked?
- If not properly marked, damages are limited to the period after actual notice

### Virtual Marking (Post-AIA)

Under the America Invents Act, patent owners may use **virtual marking** — placing "Patent" or "Pat." on the product followed by a URL that lists the applicable patent numbers. This satisfies the marking requirement without requiring product label changes for new patents.

---

## 5. Standards Body Participation and FRAND Commitments

For Korean technology companies deeply involved in standards development (3GPP for 5G/LTE, IEEE for Wi-Fi, HDMI, DisplayPort, etc.):

### Managing SEP Exposure

**As a licensor:** If your company holds Standard Essential Patents (SEPs) declared to standards bodies, FRAND (Fair, Reasonable, and Non-Discriminatory) licensing obligations apply. Breach of FRAND obligations is a defense that accused infringers increasingly use successfully.

**As a licensee (defendant in SEP case):** 
- If the asserted patent is declared essential to a standard you implement, demand FRAND rates
- FRAND rates are calculated based on the patent's contribution to the standard (not the entire standard's value); apply SSPPU analysis
- In ITC proceedings: FRAND commitments can support a public interest defense against exclusion orders
- Samsung Display's use of the ITC against BOE (2024–2025) illustrates Korean companies' effective offensive use of ITC for SEP enforcement

---

## 6. Patent Watch Programs

A systematic patent monitoring program provides early warning of new threats and competitive developments.

### What to Monitor

| Category | Monitoring Method | Frequency |
|---|---|---|
| **NPE portfolio acquisitions** | RPX, Lex Machina alerts for NPE activity in your tech sectors | Weekly |
| **Competitor new patent filings** | USPTO and EPO assignment/publication alerts for key competitors | Monthly |
| **Continuation filings in known patent families** | Google Patents, PatSnap alerts on identified patent families | Monthly |
| **PTAB proceedings on patents in your sector** | PTAB case search; Docket Navigator | Monthly |
| **ITC filings in your technology sector** | ITC EDIS system; Lex Machina | Weekly |
| **Litigation filings naming your industry peers** | PACER alerts; Lex Machina company monitoring | Weekly |

### Responding to Patent Watch Alerts

When a watch alert identifies a new patent or assignment relevant to your products:

```
New patent alert received
        │
        ├── Is it assigned to a known NPE? → Escalate to IP counsel immediately
        ├── Does it cover our current products? → Commission FTO analysis
        ├── Does it cover our next-generation products? → Integrate into next product FTO gate
        ├── Is it in a continuation family already on our watch list? → Compare claims to earlier analysis
        └── Is it clearly not relevant? → Document and close
```

🌏 **Korean Company Watch Program:** Given Samsung's frequency of NPE targeting (new suit approximately every 5 days), a dedicated patent watch team with real-time monitoring is essential — not a quarterly batch review. Consider embedding patent watch functions within both the US legal team and the Korean headquarters IP team, with daily cross-communication protocols.

---

## 7. 2026 Update Addendum: ODP Diligence and Trade-Secret Spillover Risk

### A. ODP/PTA Audit Rules for Portfolio and M&A Reviews

For any family where a PTA-extended patent carries the longest term, require a prosecution-timeline audit:

1. Identify earliest-filed and earliest-issued family member
2. Map expiration dates with/without PTA
3. Classify risk under current *Cellect*/*Allergan* boundaries

If a later-filed patent is the practical term extender, reflect potential ODP invalidation risk in valuation.

### B. Clean-Room Protocol as a Default Hiring/Integration Control

Where teams hire from competitors or ingest external code artifacts, require documented clean-room controls:

- Personnel segregation
- Access controls and repository partitioning
- Instruction logs and compliance attestations
- Independent verification trail for resulting implementation

### C. Global Punitive Exposure Snapshot (Management Briefing Table)

| Jurisdiction / claim type | 2025–2026 enforcement signal | Manual implication |
|---|---|---|
| U.S. patent | Enhanced damages capped by statute (up to treble) | Keep willfulness controls and opinion process current |
| U.S. trade secret | Large exemplary awards remain possible | Elevate clean-room and employee mobility controls |
| Korea patent/trade secret | Expanded punitive multipliers in force | Align KR/US compliance playbooks |
| China IP courts | Increasing punitive-award usage trend | Model China litigation downside explicitly |
| Brazil patent | No classic punitive damages, but coercive daily fines possible | Monitor injunction-compliance operations closely |

