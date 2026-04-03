# Freedom to Operate (FTO) Analysis

> **Quick Reference:** FTO analysis answers: "Can we make/sell/use this product without infringing a third party's patent?" Conducted before product launch, it identifies risks while design changes are still cheap. Conducted during litigation, it maps the landscape for design-arounds and supports a good-faith defense.

---

## 1. FTO as a Proactive Defense Tool

Freedom to Operate analysis is fundamentally **preventive** — it identifies patent infringement risks before a product is launched or a feature is deployed, when avoidance is cheapest and easiest. Its value for a patent defendant includes:

1. **Pre-launch risk identification:** Allows design modifications before the product ships
2. **Design-around documentation:** Creates a record of good-faith investigation — powerful evidence against willfulness
3. **Valuation for licensing negotiations:** Knowing which patents are problematic gives leverage in license negotiations
4. **Acquisition due diligence:** Identifies IP encumbrances before M&A transactions
5. **Early warning system:** Systematic FTO programs often flag threats months before NPEs file suit

---

## 2. When to Commission an FTO Analysis

### Product Lifecycle Integration

Integrate FTO analysis into the product development gate process:

| Stage | FTO Activity |
|---|---|
| **Concept / Early R&D** | Landscape search to identify relevant patent families; design freedom scan |
| **Prototype / MVP** | Focused FTO on key novel features; identify specific risk patents |
| **Pre-launch (3–6 months before release)** | **Full FTO opinion**: written legal opinion from outside counsel on specific high-risk patents |
| **Post-launch monitoring** | Continuation watch; new filings from identified patent holders |
| **Annual review** | Update FTO for significant patent landscape changes or product updates |

### Triggering Events Requiring FTO Analysis

- New product launch with genuinely novel technical features
- Acquisition of a company (due diligence)
- Demand letter or industry news about a competitor's patent activity
- Competitor announcement of patent licensing campaign
- Company's entry into a new technology space or geographic market
- IPO preparation (investors require IP diligence)

---

## 3. FTO Analysis Methodology

### Step 1: Define the Product/Technology to Be Analyzed

Precisely define what is being analyzed:
- Which specific product features are at issue?
- What is the implementation technology (hardware, software algorithm, manufacturing process)?
- Which geographic markets (US, EU, Korea, Japan, China)?

FTO analysis is not a search of "everything" — it is targeted to the specific technology and market.

### Step 2: Patent Landscape Search

**Search strategy:**
- Define claim-mapped search queries: translate each technical feature into patent search terms
- Search USPTO, EPO, WIPO databases; use commercial databases (Derwent, PatSnap, Questel)
- Search by: keyword + IPC classification code + assignee (competitors, known NPE portfolios)
- Date range: patents with remaining term that cover the technology as of the product launch date

**Prioritize for review:**
- In-force patents (not expired, not cancelled)
- Independent claims (broader scope)
- Patents held by active litigants (NPEs known to assert in your technology space)
- Standard-essential patent declarations (check ETSI, IEEE, 3GPP databases for SEP declarations)

### Step 3: Claim Mapping and Risk Tiering

For each identified patent that appears potentially relevant, map its independent claims against the product:

| Risk Level | Criteria | Action |
|---|---|---|
| **High** | Claims appear to read on the product; strong valid claim; active patent holder | Seek written FTO opinion; evaluate design-around immediately |
| **Medium** | Claims may read on the product under some constructions; validity uncertain | Monitor; detailed analysis before launch; consider design-around |
| **Low** | Claims don't read on product; patent expired or cancelled; invalid on its face | Document conclusion; continue development |
| **Cleared** | Claims definitively do not read on product after detailed analysis | Document conclusion; file in FTO record |

### Step 4: Written FTO Opinion

For High-risk patents, obtain a **written FTO opinion** from outside patent counsel:
- Formal legal memorandum addressed to the company by a US-licensed patent attorney
- Non-infringement analysis: does the product practice each element of each asserted claim?
- Invalidity analysis: is the claim likely invalid (prior art, § 101)?
- Conclusion and risk assessment
- Must be prepared in good faith based on a thorough investigation

**Privilege:** Written FTO opinions are attorney-client privileged — keep them confidential. Do not circulate to non-lawyers except through counsel. The analysis can be relied upon as evidence of good faith in future litigation, but relying on it may waive privilege (see [Privilege & Work Product](../05-discovery/privilege-and-work-product-protection.md)).

---

## 4. FTO Monitoring and Updates

### Continuation Patent Watch

The most common FTO failure mode: a technology is cleared against a parent patent, but the patent holder files a **continuation application** with broader or differently-written claims — catching products that were previously cleared.

**Monitoring program:**
- Set up automated alerts (Google Patents, USPTO Patent Center, commercial watch services) for:
  - New filings by patent holders whose patents you have analyzed
  - New continuations in identified patent families
  - New assignments of relevant patents (NPE acquisitions)
- Review alert results monthly or quarterly
- Re-analyze for FTO impact when new continuation claims issue

### Competitor Patent Monitoring

For Korean companies operating in highly competitive technology spaces (semiconductors, displays, mobile, electric vehicles):
- Monitor competitor patent filings (Samsung, LG, SK, Qualcomm, Apple, etc.) for new patents in your product areas
- Track NPE acquisitions of patents from competitors or distressed companies
- Monitor patent assertion history of known NPEs in your technology space (Lex Machina, RPX)

---

## 5. FTO Opinion Scope and Communication

### Communicating FTO Results to Business Teams

**The privilege problem:** If you share a written legal opinion with business teams, you risk waiving privilege. Use these approaches:
- Share a **high-level summary** (no legal conclusions) with business leadership
- Provide **business-friendly risk ratings** (green/yellow/red) without disclosing the legal analysis
- Have counsel present the findings **verbally** in a meeting documented only by counsel's notes
- If written communication is necessary, have counsel prepare a separate **business summary** that does not contain legal conclusions

### FTO for Acquisitions

In M&A transactions, FTO analysis is a core IP due diligence item:
- Identify patents in the target company's technology that are subject to third-party IP claims
- Identify whether the target company has received demand letters or is subject to litigation holds
- Review the target's own patent portfolio for assertion risk against the acquirer's existing products
- IP reps and warranties in the acquisition agreement should be calibrated to FTO findings

🌏 **Korean Company FTO Note:** Korean companies entering US markets face a uniquely dense patent landscape — especially in semiconductors, displays, mobile communications, and automotive electronics. Commission FTO analysis before US market entry for any new product line. A systematic FTO program is one of the most cost-effective risk management tools available. Given Samsung's exposure (a new NPE suit approximately every 5 days), proactive FTO combined with a strong defensive patent portfolio is essential.

---

## 6. FTO Product Launch Gate Checklist

Use this checklist as a gate review before any significant product launch:

```
PRE-LAUNCH IP GATE REVIEW
Product: _______________  Launch Date Target: _______________

PATENT LANDSCAPE
□ Patent landscape search completed for key features?
□ High-risk patents identified and analyzed?
□ Written FTO opinions obtained for all High-risk patents?
□ All opinions reviewed by IP counsel and documented?

RISK ASSESSMENT
□ All identified patents tiered (High/Medium/Low/Cleared)?
□ All High-risk patents either cleared, designed around, or licensed?
□ Any unresolved Medium-risk patents documented with monitoring plan?
□ Standard-essential patent (SEP) exposure analyzed?

DESIGN-AROUNDS
□ Any required design-arounds implemented and confirmed non-infringing?
□ Design-around implementation documented (date, rationale, technical details)?

MONITORING
□ Continuation patent watch program set up for all identified patent families?
□ Monitoring alerts configured for key patent holders?

SIGN-OFF
□ IP Counsel: _______________  Date: _______________
□ Business Lead: _______________  Date: _______________
```
