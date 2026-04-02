# Litigation Hold and Evidence Preservation

> **Quick Reference:** A litigation hold must be issued **immediately** upon receipt of a complaint or when suit becomes "reasonably anticipated." Failure to preserve relevant documents can result in severe sanctions — including adverse jury instructions — even if the deletion was routine and inadvertent.

---

## 1. When Does the Preservation Obligation Arise?

The duty to preserve evidence arises when litigation is **reasonably anticipated** — which is **earlier** than most companies expect.

| Triggering Event | Preservation Obligation Arises? |
|---|---|
| Complaint served | **Yes — immediately** |
| Demand letter received asserting specific patent infringement | **Yes — immediately** (suit is reasonably anticipated) |
| Internal decision to file a declaratory judgment action | **Yes — immediately** |
| Informal letter suggesting company "may be infringing" | Likely yes — assess with counsel |
| General industry licensing campaign letter | Assess with counsel; often yes if company is named |
| Internal awareness that a competitor may assert its patents | Possibly — document the analysis with counsel |

**Rule:** When in doubt, issue the hold. The cost of over-preserving is far lower than the cost of sanctions for under-preserving.

---

## 2. Consequences of Failing to Preserve: Spoliation

**Spoliation** is the destruction, alteration, or failure to preserve evidence when a duty to preserve exists. Consequences under Fed. R. Civ. P. 37(e):

| Severity | Conduct | Available Sanctions |
|---|---|---|
| **Severe** | Intentional destruction to prevent use in litigation | Adverse inference jury instruction (jury told to assume lost evidence was unfavorable to the spoliating party); case-dispositive sanctions; default judgment |
| **Significant** | Negligent destruction causing prejudice | Order to pay opposing party's discovery costs; preclusion of evidence; adverse instruction |
| **Moderate** | Routine deletion that violates a hold obligation | Monetary sanctions; extended discovery; curative measures |

A single adverse inference instruction in a patent case effectively destroys credibility before the jury. **Spoliation sanctions have been awarded against large technology companies in multiple high-profile cases.**

---

## 3. Litigation Hold Notice: What Must Be Covered

### Who Receives the Litigation Hold Notice?

**Primary Custodians** (must always receive the hold):
- Engineers and product managers responsible for the accused product/technology
- Technical leads and architects for accused features
- Finance/accounting staff managing revenue data for accused products
- IP/patent team members who have reviewed the patent or related art
- Business development staff involved in any licensing discussions
- Any employee who has had direct contact with the opposing party regarding the patent

**IT and Records Management:**
- IT department (to suspend routine deletion/auto-delete policies)
- Records management / legal ops team
- Cloud storage administrators

**Other Personnel (as appropriate):**
- Sales team members whose communications about the accused product may be relevant
- Executive communications about the accused technology or patent
- Third-party vendors / contractors with relevant data

### What Categories of Documents Must Be Preserved?

**Technical Documentation (most critical):**
- [ ] Design specifications, architecture documents, and technical white papers for the accused product/feature
- [ ] Source code version history (all versions going back to the patent's priority date)
- [ ] Software build records, changelogs, commit histories (Git/SVN logs)
- [ ] CAD files, schematics, hardware specifications
- [ ] Product roadmaps and feature planning documents
- [ ] Test plans, test results, bug reports related to the accused feature
- [ ] Manufacturing process documentation (if process patent)

**Communications:**
- [ ] Email (all accounts — corporate and personal if used for work)
- [ ] Instant messages: Slack, Microsoft Teams, KakaoTalk (business), WeChat, etc.
- [ ] Text messages related to the accused technology
- [ ] Meeting minutes and presentation materials discussing the accused product/feature
- [ ] Internal memoranda about the patent or potential infringement issues

**Business and Financial Records:**
- [ ] Revenue, sales, and pricing data for accused products (past 6+ years)
- [ ] Cost accounting records for accused products
- [ ] Marketing materials and product collateral for accused products

**Prior Art and IP Records:**
- [ ] Company publications, papers, presentations that predate the patent priority date
- [ ] Any prior art identified internally related to the patent technology
- [ ] Company's own patent applications in the same technology area
- [ ] Prior art search results or FTO analyses related to the technology

**Third-Party and Contractual Records:**
- [ ] Any prior license discussions or agreements related to the asserted patent
- [ ] Supplier/vendor agreements related to accused components
- [ ] Standards body submissions in the technology area (if SEP)

---

## 4. IT Coordination Checklist

IT must take these steps **within 48 hours** of receiving the litigation hold instruction:

**Email Systems:**
- [ ] Suspend auto-delete, archive purge, and retention policies for affected custodians
- [ ] Place a legal hold on identified custodians' email accounts (Exchange/Google Workspace/Office 365)
- [ ] Preserve email for the period from [product launch date / patent priority date] to present
- [ ] Document the date and method of hold implementation

**Collaboration and Messaging Platforms:**
- [ ] Suspend deletion in Slack, Microsoft Teams, or equivalent
- [ ] Preserve all channels and direct messages relevant to accused product/feature
- [ ] 🌏 **KakaoTalk Business / Kakao Work:** For Korean company employees, ensure business messaging platforms are captured; personal KakaoTalk on work devices may also be subject to hold
- [ ] Preserve video/audio recordings of relevant meetings (Zoom, Teams recordings)

**Code Repositories:**
- [ ] Suspend any code purge or cleanup scripts on relevant repositories
- [ ] Preserve all branches, tags, commit history, and associated metadata
- [ ] Back up repository to litigation archive

**File Storage:**
- [ ] Suspend deletion policies on relevant shared drives (Google Drive, SharePoint, OneDrive, NAS)
- [ ] Preserve all document management systems (e.g., Confluence, SharePoint)
- [ ] Capture and preserve cloud storage (AWS S3 buckets, Azure Blob, etc.) containing product data

**Backup and Disaster Recovery:**
- [ ] Preserve any backup tapes/images from the relevant time period
- [ ] Do NOT overwrite routine backups until the hold is released

**Departing Employees:**
- [ ] IT must flag any custodian who separates from the company during litigation
- [ ] Preserve departing employee's data before account deactivation
- [ ] Obtain signed confirmation from HR that departing custodian data was preserved

---

## 5. 🌏 Foreign Company (Korean) Specific Considerations

Korean companies face unique challenges in implementing US-style litigation holds:

### Geographic Scope
The litigation hold **applies globally** — including:
- Korean headquarters (Seoul / Suwon / Incheon operations)
- Korean subsidiaries and affiliates
- Any foreign employee working on the accused product

Korean-language documents (including Korean emails, KakaoTalk messages, internal memos in Korean) are **fully subject to US discovery** and must be preserved. They will need to be translated if produced.

### Korean Personal Information Protection Act (PIPA) Tension
Korean PIPA protects personal information of Korean employees. US courts are aware of this tension but **do not generally accept PIPA as a complete defense** to US document production. Apply the five-factor *Aérospatiale* comity analysis:
1. Importance of the documents to the US litigation
2. Specificity of the request
3. Whether the information originated in the US
4. Availability of alternative means of obtaining the information
5. The extent to which non-compliance would undermine important interests of the US

**Practical approach:** Implement the hold immediately (preserving all data), and address PIPA-related production concerns later with outside counsel when actual production requests are received. **Preservation and production are separate questions** — preserve everything; fight about production scope later.

### KakaoTalk and Korean Messaging Apps
US courts have required production of KakaoTalk messages in cases involving Korean parties. The legal team should:
- Identify all work-related KakaoTalk channels used by custodians
- Preserve the native Korean-language content
- Do not delete channels or message histories pending review

### Translation Costs — Budget Now
In major patent cases, Korean-language document translation has cost companies **millions of dollars**. Early budgeting for translation services is essential:
- Estimate volume of Korean documents based on custodian count and time period
- Identify qualified technical/legal translation vendors with USPTO experience
- Consider Technology Assisted Review (TAR) tools that support Korean language

---

## 6. Custodian Management During Litigation

### Initial Custodian Interviews
Within 30 days of issuing the litigation hold, conduct custodian interviews (preferably by outside counsel) to:
- Confirm receipt and understanding of the hold notice
- Identify additional custodians not initially captured
- Locate non-standard data sources (personal devices used for work, home computers, personal email)
- Identify any documents already deleted (and document the circumstances)

### Ongoing Custodian Management
- **Re-notify custodians** if the case scope expands (new patents added, new accused products)
- **New hires:** If a new employee joins and has relevant knowledge/documents, add them to the hold
- **Departing employees:** Preserve their data before offboarding; document the preservation in writing
- **Annual reminder notices:** For long-running litigation, send reminders to all custodians at least annually

### Custodian Acknowledgment Form
All custodians should sign an acknowledgment confirming they received and understand the hold. Maintain a log of:
- Date hold notice sent
- Date acknowledgment received
- Date of any follow-up or re-notification
- Any exceptions or issues reported

---

## 7. Litigation Hold Release Protocol

The preservation obligation **does not automatically end** when litigation settles or judgment is entered. Hold the following before releasing:

- [ ] Final judgment entered AND appeal period expired (30 days for notice of appeal)
- [ ] If appealed: Federal Circuit decision issued and certiorari period expired
- [ ] All post-trial motions resolved
- [ ] All related cases involving the same patent(s) resolved
- [ ] Obtain written authorization from lead litigation counsel to release

**Upon release:**
- Notify IT to resume normal retention/deletion policies for identified custodians
- Notify custodians in writing that the hold is released
- Retain documentation of the hold itself (notices, custodian lists, acknowledgments) for at least 3 years after release

---

## 8. Sample Litigation Hold Notice Template

```
[PRIVILEGED AND CONFIDENTIAL — ATTORNEY-CLIENT COMMUNICATION]

To: [Custodian Name]
From: Legal Department / IP Counsel
Date: [Date]
Re: LITIGATION HOLD — [Case Name / Patent Number]

This notice is a legal hold notice issued by the Legal Department. You are required
to preserve ALL documents and information that may be relevant to the matter
described below. Please read this notice carefully.

MATTER DESCRIPTION:
Our company has received a patent infringement demand / has been served with a
complaint concerning [describe accused product/technology] in connection with
US Patent No. [Patent Number].

YOUR OBLIGATIONS:
Effective immediately, you must:
1. PRESERVE all documents, files, and records (electronic and physical) relating
   to [accused product/feature/technology], including but not limited to:
   [list specific categories relevant to custodian's role]

2. SUSPEND any routine deletion, archiving, or cleanup that would destroy
   relevant information. This applies to:
   - Email (all accounts)
   - Instant messages (Teams, Slack, KakaoTalk, etc.)
   - Files on your computer, shared drives, and cloud storage
   - Any other records related to the matter

3. NOTIFY the Legal Department immediately if you are aware of any relevant
   documents that may have been deleted or altered.

4. RETURN the signed acknowledgment below by [date].

This obligation continues until you receive a written release from the Legal
Department. Questions? Contact [Name, email, phone].

I acknowledge that I have received, read, and understand this litigation hold notice.

Signature: _______________ Date: _______________
Name: _______________
Department: _______________
```
