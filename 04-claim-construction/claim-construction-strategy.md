# Claim Construction Strategy

> **Quick Reference:** Claim construction (the Markman hearing) is often the single most important event in a patent case. A favorable construction can eliminate infringement; an unfavorable one can make an otherwise strong defense collapse. Prepare as if this hearing is the trial.

---

## 1. Why Claim Construction Is the Central Battlefield

Patent claims define the legal boundary of the patent monopoly. The meaning of claim terms — determined by the court as a matter of law — governs everything that follows:

- **Non-infringement:** If a claim term is construed narrowly enough that the accused product falls outside its scope, there is no infringement
- **Invalidity:** If a claim term is construed broadly, it may read on prior art and be invalid
- **Damages scope:** A broader construction = larger number of accused products = higher damages

Unlike trial, Markman rulings are decided **by the judge alone** (no jury), making the outcome more predictable — and more critical to invest in deeply.

**Standard of review on appeal:** Claim construction is reviewed **de novo** by the Federal Circuit (with subsidiary factual findings reviewed for clear error under *Teva Pharmaceuticals USA, Inc. v. Sandoz, Inc.*, SCOTUS 2015). This means a district court's Markman ruling can be reversed on appeal even without trial error.

---

## 2. Sources of Claim Meaning — Hierarchy

Claim terms are construed using **intrinsic evidence** first, then extrinsic evidence only if ambiguity remains:

### Intrinsic Evidence (Always Preferred)

**1. Claim language itself**
The starting point. Claims are read in light of the ordinary meaning of their terms. The same term used in different claims of the same patent is presumed to have the same meaning throughout.

**2. Specification (written description + figures)**
The specification is "the single best guide to the meaning of a disputed term." Key principles:
- The specification may define a term explicitly ("as used herein, 'module' means...")
- The specification may disclaim certain scope ("the present invention does NOT include...")
- Embodiments in the specification can inform — but usually do NOT limit — claim scope (*Phillips v. AWH*, Fed. Cir. 2005 en banc)

**Defense strategy:** Identify passages in the specification that describe the invention **narrowly** — particularly descriptions of "the present invention," explicit disclaimers, and figures showing only one implementation. Use these to argue for narrow constructions that read out the accused product.

**3. Prosecution history**
The file wrapper (prosecution history) shows arguments the applicant made to overcome examiner rejections. These can create **prosecution history estoppel** — the applicant cannot recapture scope disclaimed to obtain the patent.

**Defense strategy:** This is one of the most powerful tools. If the applicant narrowed a claim or distinguished prior art during prosecution, that narrowing limits the doctrine of equivalents and informs literal claim construction. Always download and read the full prosecution history for every asserted patent.

### Extrinsic Evidence (Lower Weight)

- **Expert testimony** about what a POSITA would understand the term to mean (useful for highly technical terms)
- **Technical dictionaries** at the time of the invention
- **Prior art references** showing how the term was used in the field

Courts rely on extrinsic evidence only to supplement or confirm intrinsic evidence analysis. Extrinsic evidence **cannot contradict** intrinsic evidence.

---

## 3. Selecting Claim Terms to Contest

Most local patent rules limit the total number of disputed claim terms (typically 10 per side, 20 total). Choose terms strategically:

### Priority 1: Terms That Read Out the Accused Product

Identify claim terms where a **narrow, correct construction** would mean the accused product does not meet the limitation. These are your highest-value terms — winning this construction wins on non-infringement.

### Priority 2: Terms That Render Claims Invalid

Identify terms where your **broader construction** would make the claim read on prior art (thus invalid). This is a secondary but important strategy: if the court construes the term broadly (as plaintiff wants), argue in the alternative that the broad claim is anticipated or obvious.

### Priority 3: Terms That Limit Damages Scope

Identify terms where construction can narrow the population of "accused products" (e.g., a method claim's "user" term — does it require a human, or does automated processing count?). Narrowing here reduces the royalty base.

### Avoid Contesting Marginal Terms

Don't waste precious term slots on:
- Terms whose construction won't affect the outcome either way
- Terms where the intrinsic record strongly supports plaintiff's construction
- Terms that are well-established in the technical field with only one reasonable meaning

---

## 4. The Markman Hearing: Preparation Process

### Claim Construction Briefing Schedule (Typical)

```
1. Exchange claim terms in dispute (based on local rules)
2. Meet and confer to reduce disputes
3. Opening Markman briefs (defendant's and plaintiff's — filed simultaneously or staggered)
4. Responsive/reply Markman briefs
5. Technology tutorial (submitted to court separately)
6. Markman hearing (oral argument before the judge)
7. Claim construction order (days to months after hearing)
```

### Markman Brief Preparation Checklist

- [ ] Identify all claim terms genuinely in dispute (not just ones you can win)
- [ ] Download and review the full prosecution history for every asserted patent and all continuations/parents
- [ ] Identify every argument applicant made to the examiner about the disputed terms
- [ ] Map the specification figures and embodiments to each disputed term
- [ ] Prepare claim charts showing: (a) plaintiff's proposed construction + product mapping, (b) defendant's proposed construction + why product doesn't qualify
- [ ] Identify prosecution history estoppel arguments for each term
- [ ] Draft proposed constructions for each term in plain, precise language
- [ ] Prepare supporting expert declaration if technical terms require expert explanation

### Technology Tutorial

Many courts request a technology tutorial before the Markman hearing to educate the judge on the technical field. This is a significant opportunity:

**Defendant's tutorial strategy:**
- Present the technology neutrally but frame it in a way that contextualizes the problem the patent claims to solve
- Show that the "invention" is incremental, or was already well-known in the field
- Introduce the POSITA concept early — set the level of technical sophistication
- Keep it simple: assume the judge has no engineering background

---

## 5. Indefiniteness Arguments (§ 112(b))

Under *Nautilus, Inc. v. Biosig Instruments, Inc.* (SCOTUS 2014), a claim is indefinite if it fails to inform, with **"reasonable certainty,"** those skilled in the art about the scope of the invention.

### Common Indefiniteness Arguments for Patent Defendants

| Claim Language | Indefiniteness Argument |
|---|---|
| Functional claiming ("means for [function]") | If § 112(f) (means-plus-function) applies, the specification must disclose corresponding structure |
| Relative terms ("substantially," "approximately," "about") | Indefinite if the specification provides no objective standard for the degree of approximation |
| Claim mixes method and apparatus | Mixed claim types can be indefinite if the limitations cannot be harmonized |
| Computer-implemented functions without disclosed algorithms | *Williamson v. Citrix* (Fed. Cir. 2015): generic "module" language invokes means-plus-function treatment; if no algorithm is disclosed, indefinite |

**Timing:** Indefiniteness is a § 112 argument — it can be raised at Markman (as a claim construction issue) or later on summary judgment. Raising it at Markman is efficient if the indefiniteness is apparent from the claim language and prosecution history alone.

---

## 6. Coordinating PTAB and District Court Claim Construction

If you are pursuing IPR in parallel with district court litigation, **inconsistent claim construction positions** across the two forums can create credibility problems and judicial estoppel issues.

### The Phillips Standard Alignment (Post-2018)
Since January 2018, PTAB uses the **Phillips** claim construction standard (ordinary meaning to a POSITA in light of the specification), the same standard used in district court. This eliminates the pre-2018 BRI/Phillips tension.

### Coordination Principles

1. **Do not adopt a PTAB claim construction that contradicts your district court position** — courts can take judicial notice of PTAB proceedings; inconsistency will be exploited by plaintiff
2. **If PTAB construes a term narrowly** (benefiting your invalidity argument), assess whether that narrow construction also hurts your non-infringement argument in district court — sometimes the narrow PTAB construction that invalidates the patent also means the patent covers your product
3. **If Markman goes badly** (court adopts broad construction): this makes IPR invalidity arguments more powerful, but also increases infringement risk — reassess the litigation strategy after an adverse Markman ruling

### After an Adverse Claim Construction

An unfavorable Markman ruling does not end the case, but requires immediate strategy reassessment:

```
Unfavorable claim construction received
        │
        ├── Does the broad construction now read on prior art? → Strengthen invalidity arguments
        ├── Is there still a non-infringement argument? → Identify remaining absent elements
        ├── Is a design-around now feasible? → Engage engineering team through counsel immediately
        ├── Does the ruling change damages exposure? → Update damages model
        └── Is interlocutory appeal appropriate? (Rarely — requires certification under 28 U.S.C. § 1292(b))
```

**Motion for reconsideration:** File promptly (within 14 days per most local rules) if the court made a factual or legal error — but only for genuine errors, not simply disagreement with the result. Courts are reluctant to reconsider Markman orders absent clear error.

---

## 7. Oral Argument at the Markman Hearing

### Preparation

- Prepare **demonstrative slides** with the claim language, key specification excerpts, and prosecution history highlights
- Prepare for the judge's likely questions: "What would a skilled person understand this to mean?" "What does the specification say?" "Did the applicant surrender this scope during prosecution?"
- Practice presenting your construction in a single sentence first, then supporting it — don't bury the lead

### Handling the Hearing

- **Lead with your strongest term** — judges' attention peaks at the start
- **Quote the specification directly** when possible — don't paraphrase
- **Use prosecution history quotes** — "The applicant specifically told the examiner that [term] does not include [scope]..."
- If asked whether the court should adopt a construction you haven't argued: "Your Honor, any construction that [achieves X result you need] is acceptable to defendant"
- Do NOT concede terms under pressure at oral argument without conferring with co-counsel

🌏 **Korean Company Note:** If Korean-speaking engineers or Korean-language technical documents need to be incorporated into Markman arguments (e.g., showing your product's architecture in Korean technical documentation), prepare certified translations well in advance of briefing. Last-minute translation of technical documents creates quality risk.
