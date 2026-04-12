# US Patent Litigation Defense Guidelines

> **Disclaimer:** These guidelines are for internal informational purposes only and do not constitute legal advice. Patent litigation is highly fact-specific and jurisdiction-dependent. Always retain qualified US patent litigation counsel before taking any legal action or making any significant decision.

---

## Purpose & Scope

This repository provides practical, operational guidelines for **corporate legal and IP teams** defending against US patent infringement claims. The content is designed primarily for:

- **In-house IP counsel** managing patent litigation portfolios
- **IP managers** coordinating between business units and outside counsel
- **Corporate legal generalists** who encounter patent disputes outside their specialty
- **Business unit leaders** whose products are accused of infringement

The focus is **defensive** — large technology, electronics, and manufacturing companies are among the most frequent targets of patent suits, particularly from Non-Practicing Entities (NPEs/patent trolls). These guidelines address the full lifecycle of patent defense, from the first demand letter through trial, appeal, and proactive portfolio management.

> **Note for Korean and Foreign Companies:** Throughout this repository, sections marked with 🌏 highlight specific considerations for non-US (particularly Korean) companies defending patent suits in the United States. Foreign companies face unique venue exposure, discovery challenges, and procedural risks that require special attention. See the [Foreign Company Considerations Overview](#foreign-company-considerations) below.

---

## How to Navigate This Repository

| Phase | Document | Key Topics |
|---|---|---|
| **Overview** | [Litigation Lifecycle Overview](00-overview/litigation-lifecycle-overview.md) | Full lifecycle, roles, cost expectations |
| **Pre-Litigation** | [Threat Assessment](01-pre-litigation/threat-assessment.md) | Demand letters, triage, DJ strategy |
| | [Litigation Hold & Evidence Preservation](01-pre-litigation/litigation-hold-evidence-preservation.md) | Hold notices, ESI, spoliation risk |
| **Case Initiation** | [Initial Case Assessment](02-case-initiation/initial-case-assessment.md) | First 2 weeks, invalidity/infringement analysis |
| | [Venue & Jurisdiction](02-case-initiation/venue-and-jurisdiction.md) | TC Heartland, foreign defendant rules, transfer |
| | [Early Case Strategy](02-case-initiation/early-case-strategy.md) | Defense theory, § 101 motions, willfulness |
| | [ITC Section 337 Defense Playbook](02-case-initiation/itc-section-337-defense-playbook.md) | ITC timeline, domestic industry, remedy mitigation |
| **Post-Grant Proceedings** | [IPR/PGR Overview](03-post-grant-proceedings/ipr-pgr-overview.md) | Mechanics, estoppel, comparison table |
| | [IPR/PGR Strategy & Timing](03-post-grant-proceedings/ipr-pgr-strategy-and-timing.md) | Decision tree, petitions, stay motions |
| | [IPR Defense Playbook](03-post-grant-proceedings/ipr-defense-playbook.md) | 30-day readiness, Fintiv resilience, estoppel control |
| | [Ex Parte Reexamination](03-post-grant-proceedings/ex-parte-reexamination.md) | When to use vs. IPR |
| **Claim Construction** | [Claim Construction Strategy](04-claim-construction/claim-construction-strategy.md) | Markman prep, term selection, prosecution history |
| **Discovery** | [Discovery Strategy](05-discovery/discovery-strategy.md) | Production, interrogatories, depositions |
| | [Privilege & Work Product](05-discovery/privilege-and-work-product-protection.md) | In-house privilege, opinion of counsel, FRE 502(d) |
| **Expert Witnesses** | [Expert Witness Management](06-expert-witnesses/expert-witness-management.md) | Selection, Daubert, deposition prep |
| **Damages Defense** | [Damages Defense Strategy](07-damages-defense/damages-defense-strategy.md) | Georgia-Pacific, apportionment, willfulness |
| **Settlement** | [Settlement & Licensing Strategy](08-settlement-and-licensing/settlement-and-licensing-strategy.md) | Decision matrix, negotiation, license terms |
| **Trial** | [Trial Preparation Guide](09-trial-preparation/trial-preparation-guide.md) | SJ motions, MIL, jury selection, eBay |
| **Appeals** | [Appeals Guide](10-appeals/appeals-guide.md) | Federal Circuit, standards of review |
| **Portfolio Mgmt** | [Freedom to Operate](11-portfolio-management/freedom-to-operate.md) | FTO methodology, product launch gate |
| | [Design-Arounds & Defensive Portfolio](11-portfolio-management/design-arounds-and-defensive-portfolio.md) | Design-around, defensive patents, LOT/OIN |
| **Reference** | [Key Deadlines Reference](appendices/key-deadlines-reference.md) | All critical litigation deadlines |
| | [Glossary](appendices/glossary.md) | 50+ key terms defined |
| | [Vendor & Resource Guide](appendices/vendor-and-resource-guide.md) | Tools, databases, service providers |

---

## Quick Access: First 72 Hours Checklist

When a demand letter or complaint arrives, time is critical. Use this checklist immediately:

- [ ] **Do NOT respond** to any demand letter without counsel review
- [ ] **Preserve all communications** — forward to IP/legal immediately; instruct staff not to delete
- [ ] **Identify the patent(s) asserted** — look up on USPTO.gov (Google Patents)
- [ ] **Identify the accused product(s)** — determine which business unit is involved
- [ ] **Trigger litigation hold** if a complaint has been filed or suit is reasonably anticipated
- [ ] **Check response deadlines** — 21 days to answer a complaint (extensions available)
- [ ] **Assess IPR petition deadline** — 1 year from service of complaint; begin clock immediately
- [ ] **Brief management** — document the briefing (preserve privilege)
- [ ] **Contact outside counsel** — if not pre-selected, initiate selection process immediately

→ Full detail: [Threat Assessment](01-pre-litigation/threat-assessment.md) | [Litigation Hold](01-pre-litigation/litigation-hold-evidence-preservation.md)

---

## Foreign Company Considerations

🌏 **Korean and other foreign companies face a distinct set of challenges in US patent litigation.** Key issues unique to foreign defendants:

### Venue Exposure
Unlike US domestic companies protected by *TC Heartland* (2017), **foreign corporations can be sued in any US federal district** under *In re HTC Corp.* (Fed. Cir. 2018), citing 28 U.S.C. § 1391(c)(3). NPE plaintiffs actively exploit this by filing in plaintiff-friendly districts (especially E.D. Texas or W.D. Texas) even when the foreign company has no operations there. As of 2025, over 40 such cases targeting foreign parents were filed in E.D. Texas in a single year.
→ See: [Venue & Jurisdiction](02-case-initiation/venue-and-jurisdiction.md)

### Discovery Asymmetry
Korean companies are accustomed to Korean litigation practice, which has **no US-style broad pretrial discovery**. US Rule 26 discovery requires preservation and production of all potentially relevant documents — including emails, messaging apps (KakaoTalk), source code, and financial records. Failure to comply can result in severe sanctions including adverse inference jury instructions.
→ See: [Litigation Hold](01-pre-litigation/litigation-hold-evidence-preservation.md) | [Discovery Strategy](05-discovery/discovery-strategy.md)

### ITC Section 337 Exposure
Foreign companies importing products into the US can face ITC investigations, which move to trial within 10–12 months and can result in import bans. Korean companies are both frequent **targets** (especially from US competitors) and active **users** of the ITC as an offensive weapon (e.g., Samsung Display v. BOE, 2024–2025).
→ See: [ITC Section 337 Defense Playbook](02-case-initiation/itc-section-337-defense-playbook.md) | [Initial Case Assessment](02-case-initiation/initial-case-assessment.md)

### NPE Targeting
Korean technology companies — especially Samsung, LG, and SK group companies — are among the **most targeted defendants** by US NPEs. Samsung faces a new NPE patent suit approximately every 5 days. The concentrated product portfolios and deep pockets of Korean conglomerates make them disproportionate targets.

---

## Key Statute & Rule References

| Citation | Subject |
|---|---|
| 35 U.S.C. § 101 | Patent-eligible subject matter |
| 35 U.S.C. § 102 | Novelty / Anticipation |
| 35 U.S.C. § 103 | Obviousness |
| 35 U.S.C. § 112 | Written description / Enablement / Definiteness |
| 35 U.S.C. § 271 | Infringement |
| 35 U.S.C. § 284 | Damages |
| 35 U.S.C. § 285 | Attorney's fees (exceptional cases) |
| 35 U.S.C. § 311–319 | Inter Partes Review |
| 35 U.S.C. § 315(b) | IPR one-year bar |
| 35 U.S.C. § 315(e) | IPR estoppel |
| 28 U.S.C. § 1400(b) | Patent venue (domestic defendants) |
| 28 U.S.C. § 1391(c)(3) | General venue (foreign defendants — any district) |
| Fed. R. Civ. P. 26 | Discovery scope and limits |
| Fed. R. Evid. 502(d) | Clawback orders / privilege waiver protection |

---

## Maintenance & Updates

These guidelines are maintained by the IP Legal team. Major US patent law developments — particularly significant Federal Circuit or Supreme Court decisions — should trigger a review of affected sections. Key recent developments reflected in this version (as of April 2026):

- *In re HTC Corp.* (Fed. Cir. 2018) — Foreign defendant venue (any district rule)
- *Halo Electronics v. Pulse* (SCOTUS 2016; Fed. Cir. Feb. 2025 remand) — Willfulness standard
- *Ingenico Inc. v. IOENGINE, LLC* (Fed. Cir. May 2025) — IPR estoppel scope (product prior art not estopped)
- *Recentive Analytics v. Fox Corp.* (Fed. Cir. April 2025) — AI/ML § 101 invalidity
- *EcoFactor v. Google* (Fed. Cir. en banc 2025) — Comparable license apportionment
- *Rex Medical v. Intuitive Surgical* (Fed. Cir. Sept. 2025) — Damages apportionment mandatory
- PTAB FY2025 statistics — Institution rate dropped to 50%; ~80% claim invalidation at FWD
