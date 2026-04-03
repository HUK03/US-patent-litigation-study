# Trial Preparation Guide

> **Quick Reference:** Patent trials last 5–10 days. The jury is lay. Complexity must be translated into simple narratives. Prepare summary judgment and pre-trial motions to narrow issues before trial; prepare every witness and demonstrative exhibit as if the case depends on it — it probably does.

---

## 1. The Path from Close of Expert Discovery to Trial

```
Close of Expert Discovery
        │
        ▼ (30-60 days)
Summary Judgment Motions filed
        │
        ▼ (30-90 days for briefing + hearing)
Summary Judgment Ruling
        │
        ▼ (30-60 days)
Pre-Trial Order due (joint submission)
Motions in Limine filed
        │
        ▼ (14-30 days)
MIL Opposition Briefs
Pre-Trial Conference
        │
        ▼
TRIAL
        │
        ▼ (post-verdict)
Post-Trial Motions (JMOL, new trial, enhanced damages, injunction, attorney fees)
        │
        ▼ (if appealing)
Notice of Appeal (30 days from final judgment)
```

---

## 2. Summary Judgment Strategy

Summary judgment under Fed. R. Civ. P. 56 is available when there is "no genuine dispute as to any material fact" and the moving party is entitled to judgment as a matter of law. Patent defendants should file SJ motions aggressively when the record supports it.

### Best SJ Opportunities for Defendants

**Non-infringement SJ:**
- One or more claim elements are **clearly absent** from the accused product based on undisputed technical facts
- Most effective when the absence of an element is shown by the accused product's own technical documentation
- Particularly strong after a favorable Markman ruling that adopted narrow claim constructions

**§ 101 Invalidity SJ:**
- Most likely SJ ground in software/AI patent cases
- Decided as a matter of law (no jury); district court decides on full record
- Strengthened by *Recentive Analytics* (Fed. Cir. 2025): generic ML application to new domain = ineligible
- File even if a Rule 12(b)(6) § 101 motion was denied at the pleadings stage — the record is now fuller

**§ 102/103 Invalidity SJ:**
- Harder to win because invalidity must be proven by clear and convincing evidence — but when a single prior art reference clearly discloses every claim element, SJ is appropriate
- Expert testimony supporting invalidity is usually required at SJ stage

**Prosecution History Estoppel (bars doctrine of equivalents):**
- If the applicant clearly narrowed a claim to overcome prior art, DOE is barred as a matter of law
- SJ of no DOE is appropriate where the prosecution record is clear and undisputed

### Partial Summary Judgment

Even if full SJ on liability is unavailable, pursue **partial SJ** to:
- Exclude specific accused products from the case (narrows damages base)
- Limit damages period (e.g., establish the earliest possible damages date)
- Establish that willfulness is not supported as a matter of law (cuts off enhanced damages threat)

---

## 3. Motions in Limine — Defendant's Checklist

Motions in limine exclude evidence or argument from trial before the jury hears it. File these MILs as a matter of course in every patent case:

| MIL | Argument |
|---|---|
| **Exclude improper royalty base** | Plaintiff may not present testimony using entire product revenue as royalty base without first making an EMVR showing outside the jury's presence |
| **Exclude unapportioned comparable license testimony** | Expert failed to apportion multi-patent licenses; testimony is unreliable under *Rex Medical* (2025) |
| **Exclude willfulness evidence (if appropriate)** | Where pre-suit conduct is not at issue; or where opinion of counsel defense has been asserted |
| **Exclude reference to other patent verdicts** | Prior verdicts in unrelated cases are irrelevant and unfairly prejudicial (FRE 403) |
| **Exclude "patent troll" or "NPE" characterizations** | If plaintiff will argue we should be punished for litigating against an NPE; prejudicial label |
| **Exclude undisclosed theories** | Plaintiff may not raise damages or infringement theories not disclosed in expert reports |
| **Limit inventor testimony** | Inventor testimony about what the claims mean is inadmissible extrinsic evidence post-Markman |

### Anticipating Plaintiff's MILs Against Us

Prepare to oppose these common plaintiff MILs:
- Motion to exclude reference to IPR proceedings (courts are split; most allow some reference)
- Motion to exclude design-around evidence (argue it shows good faith and cuts against willfulness)
- Motion to exclude evidence of plaintiff's litigation funding (some courts allow; others exclude)

---

## 4. Jury Selection in Patent Cases

### What to Look For in Patent Jurors

**Potential positives for defendant:**
- Engineers or technical professionals (understand complexity; less likely to be swayed by simple "they copied us" narrative)
- Business owners or people with commercial experience (understand competitive pressures)
- People who have experienced patent claims that seemed overreaching
- Prior jury service (experienced, understands the process)

**Potential concerns for defendant:**
- Strong emotional identification with individual inventors / "underdog" narratives
- Very strong anti-big-company sentiment (a modest amount is inevitable and manageable)
- People who distrust technology companies generally

### 🌏 Korean Company Jury Considerations

When a Korean company is the defendant:
- Be alert to jurors with strong prejudices against foreign companies or economic nationalism
- Humanize the Korean company early — show US employees, US customers, US contributions
- Address the "foreign company" framing preemptively: prepare voir dire questions about whether jurors can fairly evaluate a foreign company

### Voir Dire Questions for Patent Cases

Request the court ask (or ask directly in oral voir dire if permitted):
- Do you have any experience with patents — as an inventor, assignee, or in licensing?
- Have you ever been involved in a lawsuit involving intellectual property?
- Do you have any opinions about companies that hold patents but do not manufacture products?
- Do you believe that once a company is found to infringe a patent, it should pay large damages to compensate the patent owner?
- Is there anything about your background that might make it difficult to be fair to [large tech company / Korean company]?

---

## 5. Trial Narrative and Theme Development

### The Defendant's Story

Patent trials are storytelling exercises. The jury needs a simple, compelling narrative. Choose the right primary theme:

| Theme | When to Use |
|---|---|
| **"We innovated independently"** | Strongest when you can show internal development predating the patent |
| **"The patent is invalid — this was old technology"** | Strongest when prior art is vivid and easy to demonstrate |
| **"Our technology works differently"** | Strongest when the non-infringement argument turns on a clear technical distinction |
| **"They're overreaching — the patent doesn't cover what we do"** | Combine with narrow Markman constructions; accessible to lay jury |

**Avoid:** Leading with two competing themes (jury gets confused). Pick the strongest one and support the others as backstops.

### Handling the Large Corporation Dynamic

Juries can be suspicious of large defendants. Address this head-on in opening:
- Acknowledge the company's size; pivot to its positive contributions (jobs, products, innovation)
- Frame the case as about fair compensation, not large vs. small — "The real question is: what would a fair deal have looked like?"
- Emphasize legitimate process: "We investigated this patent carefully and consulted experts"

---

## 6. Injunctive Relief Defense Under *eBay*

*eBay Inc. v. MercExchange, LLC* (SCOTUS 2006) eliminated the automatic injunction presumption in patent cases. A patent owner must satisfy a **four-factor equitable test** for a permanent injunction:

| Factor | Defendant's Argument |
|---|---|
| **1. Irreparable harm** | NPE plaintiff does not compete; no irreparable harm from continued infringement; money damages adequate |
| **2. Inadequate remedy at law** | Ongoing royalty is a complete monetary remedy; no irreparable harm |
| **3. Balance of hardships** | Injunction would cause enormous hardship to defendant (force product redesign or shutdown) vs. minimal benefit to non-practicing plaintiff |
| **4. Public interest** | Injunction against widely-used product harms consumers and public |

**NPE injunctions post-*eBay*:** NPEs almost never obtain permanent injunctions. Courts have consistently held that NPEs have adequate remedy at law (ongoing royalty) and do not face irreparable harm. **This is one of the most important structural advantages for defendants against NPE plaintiffs.**

**Ongoing royalty:** If liability is found and no injunction is granted, the court may award an **ongoing royalty** for future infringement (set by the court, not the jury). The rate is typically higher than the past reasonable royalty (reflecting the post-verdict change in bargaining position) but is the primary vehicle for avoiding an injunction.

---

## 7. Post-Trial Motions

### Judgment as a Matter of Law (JMOL) — Rule 50(b)

JMOL is available when "a reasonable jury would not have a legally sufficient evidentiary basis to find for [the prevailing] party." Requirements:
- Must have moved for JMOL at the close of evidence under Rule 50(a) (renewed under 50(b) after verdict)
- Standard: No reasonable jury could have reached the verdict

Grounds for JMOL in patent cases:
- Jury's infringement verdict lacks substantial evidence (specific claim elements not proven)
- Jury's damages award is unsupported (no reasonable royalty basis for the amount awarded)
- Enhanced damages are inappropriate as a matter of law

### New Trial Motion — Rule 59

Available when the verdict is against the great weight of the evidence, or when trial error affected the outcome. Less favored than JMOL but can be combined with JMOL in the alternative.

### Remittitur

If the jury's damages award is "grossly excessive" or not supported by the evidence, the defendant may move for **remittitur** — reduction of the damages award. The court may order a new trial on damages unless plaintiff accepts the reduced amount. Courts have reduced multi-hundred-million-dollar patent verdicts to tens of millions on remittitur.

### Enhanced Damages Motion (if willfulness found)

If the jury found willfulness: brief the *Read Corp.* factors aggressively in opposition to any enhancement motion. Emphasize: good-faith investigation, promptness of design-around, closeness of the case, lack of deliberate copying.

### Attorney's Fees (§ 285)

Section 285 allows fee awards in "exceptional" cases. The standard (*Octane Fitness v. ICON Health*, SCOTUS 2014): a case is exceptional if it "stands out from others with respect to the substantive strength of a party's litigating position (considering both governing law and the facts of the case) or the unreasonable manner in which the case was litigated."

**Defendants can seek fees** when:
- Plaintiff's case was objectively baseless (weak infringement theory maintained despite clear evidence)
- Plaintiff litigated in bad faith or engaged in discovery misconduct
- Plaintiff's damages theories were frivolous

🌏 **Korean Company Trial Note:** For Korean companies defending at trial, consider whether Korean senior executives need to testify. If so: plan for interpretation, prepare intensively, and assess whether their live testimony (with potential language/cultural barriers) is more helpful or harmful than submission through deposition designation. This is a case-by-case judgment call that should be made with outside trial counsel.
