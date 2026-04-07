# Privilege and Work Product Protection

> **Quick Reference:** Attorney-client privilege in patent cases is easily waived — especially by in-house counsel who mix legal and business roles, or by defendants who choose to rely on an opinion of counsel as a willfulness defense. Plan your privilege architecture at the start of the case.

---

## 1. Attorney-Client Privilege in Patent Cases — Special Considerations

### The Basic Rule
Communications are privileged when:
1. Made between an **attorney and client**
2. In **confidence**
3. For the **purpose of obtaining or providing legal advice**

In patent litigation, the most common privilege issue is communications between **in-house patent counsel** and business/engineering teams — where the line between legal advice and business advice is frequently blurred.

### The In-House Counsel Dual-Role Problem

In-house patent counsel often simultaneously:
- Provide legal analysis of patent claims (clearly privileged)
- Participate in business strategy decisions about product development (not privileged)
- Advise on licensing deal structures (mixed — legal vs. business advice)
- Manage external counsel relationships (administrative — not clearly privileged)

**Courts look to the "primary purpose" of each communication** — was it seeking legal advice, or was it seeking business guidance that happened to come from a lawyer?

### Best Practices for In-House Patent Counsel

| Practice | Why |
|---|---|
| **Head communications with a privilege header** | "Attorney-Client Privileged — Legal Advice Requested" signals legal purpose |
| **Segregate legal analysis from business recommendations** | Write a "legal memo" separately from the "business recommendation memo" |
| **Do not CC non-lawyers on privileged communications** | Adding business stakeholders to a privileged email chain destroys privilege |
| **Do not forward privileged memos to non-lawyer recipients** | Even one non-lawyer recipient can destroy privilege for the entire chain |
| **Use "PRIVILEGED AND CONFIDENTIAL" header consistently** | Creates record of intent; easier to log in privilege reviews |
| **When attending business meetings, document legal role** | Write a follow-up memo: "My role at the meeting was to provide legal advice on [X]" |

### Patent Agent Privilege

US-licensed patent agents (registered to practice before the USPTO, but not licensed attorneys) may have a **limited privilege** for communications related to **USPTO proceedings** (prosecution, IPR). This was recognized in *In re Queen's University at Kingston* (Fed. Cir. 2016), but is limited to patent prosecution matters and does not extend to litigation-related communications.

🌏 **Korean Company Alert:** Korean patent attorneys (변리사, byeonrisa) who are not also licensed US attorneys do **not** have US attorney-client privilege protection for communications used in US litigation. Communications with Korean patent agents about US patent prosecution or litigation must be carefully analyzed before production. Retain US-licensed patent counsel for all US litigation communications.

---

## 2. Opinion of Counsel and the Willfulness Trap

### When and Why to Obtain an Opinion

A written **opinion of counsel** (a formal legal memorandum from outside patent counsel concluding the patent is invalid and/or not infringed) is the most effective evidence against enhanced damages in a willfulness case.

**Timing:** Obtain the opinion as early as possible — ideally before the infringing activity begins, or at the latest within a few months of becoming aware of the patent. An opinion obtained after the lawsuit is filed has diminished probative value.

**What the opinion should cover:**
- The specific claims asserted (or likely to be asserted)
- A complete invalidity analysis (§ 102/103/101/112 as applicable)
- A complete non-infringement analysis (claim-by-claim, element-by-element)
- The POSITA definition and the author's credentials

### The Privilege Waiver Problem

Choosing to **rely on** an opinion of counsel as a defense to willfulness **waives attorney-client privilege** over that opinion and related communications. The scope of the waiver is governed by Fed. R. Evid. 502 and case-specific rulings, but typically includes:

| Waived | Generally NOT Waived |
|---|---|
| The opinion itself (content + reasoning) | Opinions from different counsel on different patents |
| Communications between client and opinion counsel about the subject matter of the opinion | Litigation counsel's trial strategy |
| Documents opinion counsel reviewed | Work product of litigation counsel |
| Other opinions from the same counsel on the same patent | Opinions obtained but not relied upon (though risky — some courts hold otherwise) |

**Key decision:** Before disclosing an opinion of counsel to the jury, carefully analyze the full scope of the resulting waiver. Disclosing one opinion may require producing other related opinions. Consult with litigation counsel and opinion counsel before making this election.

### Selective Reliance Risk

Do NOT selectively disclose a favorable opinion while withholding an unfavorable one from the same counsel — courts treat this as improper selective waiver and may sanction or draw adverse inferences.

---

## 3. Common Interest Privilege with Co-Defendants

When multiple defendants are sued on the same patent, sharing information and legal strategy is essential — but must be done carefully to preserve privilege.

### Requirements for Common Interest Privilege

1. **Common legal interest:** The parties must share a common legal interest (e.g., both are defendants accused of infringing the same claims)
2. **Communication in furtherance of the common interest:** The communication must be made to advance the shared legal defense
3. **Written common interest agreement:** Execute a written agreement at the outset documenting the common interest relationship

### Common Interest Agreement — Key Provisions

```
Key terms to include:
- Identification of the common legal interest (the specific litigation)
- Parties to the agreement
- Confirmation that shared materials remain privileged
- Agreement not to disclose shared materials to third parties
- Provision for what happens if parties' interests diverge
- Governing law and dispute resolution
```

### When Common Interest Fails

Common interest privilege can be lost if:
- Parties' interests diverge (one defendant settles and becomes a witness against the others)
- Communications go beyond the scope of the shared legal interest (e.g., discussing business strategy unrelated to the litigation)
- One party breaches confidentiality obligations

---

## 4. Work Product Doctrine

The work product doctrine (Fed. R. Civ. P. 26(b)(3)) protects documents and tangible things **prepared in anticipation of litigation or for trial** by or for a party or its representative.

### Fact Work Product vs. Opinion Work Product

| Type | Protection | Overcome How? |
|---|---|---|
| **Fact work product** | Qualified — can be obtained by showing substantial need + inability to obtain equivalent without undue hardship | Rare in patent cases; might apply to factual investigation notes |
| **Opinion work product** (mental impressions, legal conclusions, litigation strategy) | **Near absolute** — essentially cannot be compelled | Almost never overcome |

**Protect opinion work product vigorously:** Counsel's strategic memoranda, case assessment memos, and annotated documents reflecting legal conclusions are fully protected.

### Work Product Waiver Risks in Patent Cases

| Risk Scenario | Consequence |
|---|---|
| Sharing attorney's notes with a non-litigation third party | May destroy work product protection |
| Expert witness reviews counsel's work product in preparing report | Rule 26 protects **draft expert reports and communications between counsel and expert** (post-2010 FRCP amendments) — but be careful about prior drafts shared with non-counsel |
| Business unit uses litigation-strategy memos for unrelated business decisions | Suggests the documents were not "primarily" prepared for litigation |

---

## 5. FRE 502(d) Clawback Orders — Essential in Large Cases

In patent cases involving large-scale document review (often hundreds of thousands of documents), **inadvertent production of privileged documents is almost inevitable**. Federal Rule of Evidence 502(d) provides a mechanism to protect against waiver from inadvertent production.

### How FRE 502(d) Works

The parties and court enter an order (typically as part of the ESI protocol or protective order) providing:
- Inadvertent production of privileged material **does not constitute waiver** in the current proceeding or in any other federal or state proceeding
- The producing party may "claw back" (retrieve) inadvertently produced privileged documents by notifying opposing counsel
- Upon receiving a clawback notice, receiving party must promptly return, sequester, or destroy the materials (no use in the proceeding)

**Critically:** A 502(d) order provides broader protection than the default 502(b) "inadvertent disclosure" standard, which requires case-by-case analysis. Always negotiate a 502(d) order in patent cases.

### FRE 502(d) Checklist

- [ ] Include 502(d) language in the protective order or as a standalone court order
- [ ] Implement privilege review processes that minimize inadvertent production (use TAR/AI tools with privilege keyword filtering)
- [ ] Maintain a privilege log from the outset — don't wait until the production deadline
- [ ] If you receive a clawback notice from opposing counsel: immediately segregate the documents and do not use them until the privilege dispute is resolved

---

## 6. Privilege Log Best Practices

A privilege log is required for all withheld documents. Patent privilege logs are heavily scrutinized by courts.

### Log Requirements

| Field | Required Information |
|---|---|
| Document date | Date of creation |
| Author(s) | Names and roles (identify lawyers) |
| Recipient(s) | Names and roles of all recipients |
| CC/BCC | All additional recipients |
| Description | Enough to assess privilege without disclosing privileged content |
| Privilege asserted | Attorney-client privilege / Work product / Both |
| Basis | Why privilege applies (e.g., "Request for legal advice re patent claim validity") |

### Common Privilege Log Errors

- **Too vague:** "Email regarding patent matter" — insufficient; describe the subject without revealing privileged content
- **Including non-lawyers in attorney-client privilege entries** — privilege requires lawyer involvement; CC'd business people without lawyers breaks privilege
- **Failure to include in-house counsel as author/recipient** — if a lawyer wasn't involved, it's not attorney-client privileged
- **Logging documents prepared before litigation was reasonably anticipated as work product** — work product requires anticipation of litigation at time of creation

### Categorical Privilege Logs

For very large productions, courts sometimes permit **categorical privilege logs** (grouping similar documents into categories rather than listing each individually). Negotiate this with opposing counsel and the court early — it significantly reduces privilege log burden for large Korean-language document sets.

🌏 **Korean Company Note:** When logging Korean-language privileged documents, provide English summaries of the document subject matter. Full translation is not required for the privilege log, but the description must be sufficient for the court to assess the privilege claim. Consider a categorical log approach for large volumes of Korean-language internal communications.

---

## 9. 2026 Update Addendum: Front-Load Privilege Process Under FRCP 16/26

### A. Mandatory Early Negotiation Items (FRCP 26(f)(3)(D))

At the Rule 26(f) conference, defense counsel should proactively negotiate and memorialize:

- Privilege assertion timing
- Categorical logging format and categories
- Metadata fields needed for dispute resolution
- Clawback mechanics and turnaround times

### B. Scheduling Order Integration (FRCP 16(b)(3)(B)(iv) + FRE 502(d))

Inside counsel should instruct outside counsel to request a 502(d) non-waiver order as a default item in the initial scheduling process, not as a later emergency motion.

### C. Categorical Logging Baseline for Patent Cases

Adopt standing categories (customize by case):

- Internal investigation memoranda
- Inventor–counsel communications
- Opinion-of-counsel files
- Litigation strategy and expert-prep communications (where protected)

This reduces late-stage, document-by-document log inflation and cost spikes.

