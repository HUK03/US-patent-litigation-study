# Venue and Jurisdiction in US Patent Litigation

> **Quick Reference:** Where a patent case is filed can be as consequential as the merits. For US domestic defendants, *TC Heartland* (2017) provides significant protections. For Korean and other foreign companies, those protections **do not apply** — you can be sued in any US district.

---

## 1. Why Venue Matters Enormously

The choice of venue affects:
- **Time to trial** (from 18 months in W.D. Tex. to 4+ years in N.D. Cal.)
- **Judge assignment** (some judges are statistically more favorable to defendants on § 101, Markman, or summary judgment)
- **Jury pool** (technical sophistication, attitudes toward large corporations and NPEs)
- **Local patent rules** (timing of contentions, number of claim terms for Markman)
- **Availability of stay** pending IPR (varies dramatically by district)
- **Enhanced damages / attorney fee awards** (some districts more willing to find exceptional cases)

NPE plaintiffs are highly sophisticated venue shoppers. Defending in a plaintiff-preferred venue like E.D. Texas significantly increases both the cost and risk of litigation.

---

## 2. The TC Heartland Rule — For US Domestic Defendants

*TC Heartland LLC v. Kraft Foods Group Brands LLC* (Supreme Court, 2017) held that the patent venue statute, **28 U.S.C. § 1400(b)**, is the **exclusive** basis for patent venue for US domestic defendants. Under § 1400(b), a US defendant may only be sued in a district where it:

1. **Resides** (for a corporation: state of incorporation — typically Delaware), **OR**
2. **Has committed acts of infringement AND has a regular and established place of business**

**Practical impact:** TC Heartland largely eliminated the Eastern District of Texas as a default venue for US domestic companies that are incorporated in Delaware or California and have no physical presence in EDTX.

**"Regular and established place of business"** (*In re Cray*, Fed. Cir. 2017): Requires:
- A physical place in the district
- That is regular and established (not transient)
- Of the defendant (not merely of an employee's home)

Employee home offices do **not** constitute a "regular and established place of business" without more — though this remains heavily litigated.

---

## 3. 🌏 Venue for Foreign (Korean) Companies — Critical Difference

### The Controlling Rule: Any District

*In re HTC Corp.* (Fed. Cir. May 2018) resolved this critical question: **foreign (non-US) corporations are NOT governed by § 1400(b).** Instead, the general venue statute, **28 U.S.C. § 1391(c)(3)**, applies: *"a defendant not resident in the United States may be sued in any district."*

This was based on *Brunette Machine Works, Ltd. v. Kockum Industries, Inc.* (Supreme Court, 1972), which established that alien defendants may be sued in any district.

### What This Means for Korean Companies

| Company Structure | Venue Rule | Protection from EDTX? |
|---|---|---|
| **Korean parent only (no US sub)** | § 1391(c)(3) — any district | **None** |
| **US subsidiary only** | § 1400(b) — TC Heartland applies | **Yes** (if properly incorporated and no EDTX presence) |
| **Korean parent + US subsidiary (both named)** | § 1400(b) for US sub may control if US sub is indispensable | **Partial** — depends on whether Rule 19 joinder is required |
| **Korean parent (US sub omitted from complaint)** | § 1391(c)(3) for parent — any district | **None** (NPE bypass strategy) |

### The 2024–2025 "Foreign Entity Bypass" Strategy

NPE plaintiffs have developed an aggressive tactic: **suing only the Korean or foreign parent entity** while deliberately omitting its US subsidiary from the complaint, solely to exploit the "any district" rule and file in plaintiff-preferred EDTX or WDTX, bypassing TC Heartland protections that would otherwise apply to the US subsidiary.

**Over 40 such cases** were filed in E.D. Texas in 2025 alone targeting foreign parent companies in this manner.

**Korean companies' response options:**
1. **Rule 12(b)(3) venue challenge** (limited success — courts are split on whether omitting US sub defeats venue)
2. **Motion to transfer under § 1404(a)** (see below — most practical option)
3. **Rule 19 motion** to compel joinder of the US subsidiary (if the US sub is an indispensable party whose absence would defeat TC Heartland venue)

### Burden of Proof on Venue
Post-TC Heartland, the **party asserting proper venue bears the burden of proof**. Federal Circuit (not regional circuit) law governs patent venue questions.

---

## 4. Transfer of Venue Under 28 U.S.C. § 1404(a)

Even if venue is technically proper, a defendant can seek transfer to a more convenient forum under § 1404(a): *"For the convenience of parties and witnesses, in the interest of justice, a district court may transfer any civil action to any other district or division where it might have been brought."*

### Transfer Motion Strategy

**Timing is critical:** A venue transfer motion must be filed early — typically before or with the answer, or immediately after the answer — or it is deemed waived. Courts generally require filing before any substantive participation in the case (e.g., before substantive motion practice or scheduling order compliance).

**Standard in the Fifth Circuit (W.D. Tex. and E.D. Tex.) — *In re Apple* factors:**
1. Private factors:
   - Relative ease of access to sources of proof
   - Availability of compulsory process for witnesses
   - Cost of attendance for willing witnesses
   - Practical problems making trial easy, expeditious, and inexpensive

2. Public factors:
   - Court congestion / time to trial
   - Local interest in the controversy
   - Familiarity with applicable law
   - Unfairness of burdening citizens of an unrelated district

**Federal Circuit review:** Transfer denials can be challenged via mandamus petition to the Federal Circuit. The Federal Circuit has been active in reversing EDTX transfer denials (particularly against Apple, Samsung, and other large technology companies).

### Decision Framework: Should We Move to Transfer?

```
Is our venue genuinely inconvenient?
  ├── Most of our evidence is located elsewhere?  → Yes → Strong transfer argument
  ├── Most of our witnesses are located elsewhere? → Yes → Strong transfer argument  
  ├── The technology was developed elsewhere?      → Yes → Strong transfer argument
  └── Is there a significantly better venue available?
      ├── Our state of incorporation (e.g., Delaware)?
      ├── N.D. Cal. (if technology developed in Silicon Valley)?
      └── District where our primary facilities are located?

Is transfer likely to succeed given current case law?
  ├── W.D. Tex. / E.D. Tex.: Federal Circuit has been active in granting mandamus
  ├── D. Del.: Very limited basis to transfer out (most defendants are incorporated there)
  └── Other districts: Assess on facts

Timing: Has the scheduling order been entered? (Waiting too long = waiver risk)
```

---

## 5. District-Specific Considerations for Patent Defendants

| District | Time to Trial | Patent-Specific Notes | Transfer Success? | Stay Pending IPR? |
|---|---|---|---|---|
| **D. Del.** | 2–3 years | Most large companies incorporated here; sophisticated judges; limited discretion to transfer out | Low (incorporated here) | Moderate |
| **W.D. Tex. (Waco/Austin)** | 12–18 months | Fastest to trial; Judge Albright (Waco): extremely high patent filing volume, historically reluctant to transfer; 2024–2025: Federal Circuit has reversed several Albright transfer denials | Possible via mandamus | Low–Moderate |
| **E.D. Tex. (Marshall/Tyler)** | 18–30 months | Historic NPE favorite; local patent rules require fast contentions; experienced patent judges; jury pool traditionally plaintiff-friendly | Possible via mandamus | Low |
| **N.D. Cal. (San Jose/San Francisco)** | 3–5 years | Technology-sophisticated jury pool; active § 101 jurisprudence; higher bar for NPE cases; generally defendant-favorable | Low | High |
| **C.D. Cal. (Los Angeles)** | 2–3 years | Large docket; diverse outcomes by judge | Moderate | Moderate |
| **N.D. Ill. (Chicago)** | 2–4 years | Less common for patent cases; generally balanced | Low | Moderate |

🌏 **Korean Company Strategy:** Because Korean companies **cannot** invoke TC Heartland, the most effective venue strategy when sued in EDTX or WDTX is an aggressive § 1404(a) transfer motion to N.D. Cal. or D. Del., citing:
- Engineering teams located in California or abroad (not in Texas)
- Key witnesses in Korea (or no connection to Texas)
- No meaningful connection between Texas and the accused technology

---

## 6. Personal Jurisdiction — When to Challenge

Personal jurisdiction is rarely a winning argument in US patent cases because **the federal patent statute provides for nationwide service of process** (28 U.S.C. § 1694). However, challenges may be available when:
- The foreign parent has **no meaningful contacts with the US** at all (rare for large Korean companies with US sales)
- The plaintiff is suing a **Korean subsidiary** that genuinely has no US contacts independent of the parent

**Practical note:** For most large Korean technology companies with US sales operations, distributors, or retail presence, personal jurisdiction challenges are unlikely to succeed and may consume resources better spent elsewhere. Assess with outside counsel early.

---

## 7. Venue for Declaratory Judgment Actions by the Defendant

If you are considering filing a **proactive declaratory judgment (DJ) action** (see [Threat Assessment](../01-pre-litigation/threat-assessment.md)), venue for the DJ action is governed by the same § 1400(b) / § 1391(c)(3) rules as above from the defendant's perspective.

**Strategic goal:** File the DJ action in a favorable venue (N.D. Cal., D. Del.) **before** the patent holder files its suit in a plaintiff-preferred venue. The first-filed rule generally gives priority to the first-filed case (subject to the "customer-suit exception" and other exceptions).

**First-filed rule considerations:**
- Courts apply a rebuttable presumption in favor of the first-filed case
- Exceptions: anticipatory suit filed purely to grab venue (not a genuine dispute), customer suit, etc.
- Time the DJ filing carefully — too early risks DJ jurisdiction being challenged; too late means the plaintiff files first

---

## 8. 2026 Update Addendum: Transfer Motions Must Be Engineer-Evidence Driven

### A. Federal Circuit Trend for Practical Convenience Analysis

Recent mandamus practice reinforces that transfer outcomes often turn on where accused-product engineering work actually occurred, not abstract headcount comparisons or litigation gamesmanship.

### B. Declaration Package Checklist (Prepare Before Filing Transfer Motion)

Build a data-backed declaration set with in-house HR/engineering support:

- Developer location map for accused features
- Source-code repository commit density by geography
- Location of technical documents and relevant labs
- Witness role matrix (design/implementation/testing decision-makers)
- Minimal connection facts to the plaintiff-chosen district

### C. Internal Timing Rule

Adopt a standing rule that transfer evidence collection starts immediately upon service, so declarations are ready before substantive deadlines and before the record suggests tactical delay.

