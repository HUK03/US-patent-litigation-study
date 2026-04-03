# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This is a **documentation-only repository** — there is no code, build system, or test suite. It contains operational patent litigation defense guidelines for corporate legal and IP teams, written from the **defendant's perspective**. All documents are in English. Documents carry an explicit disclaimer that they are not legal advice.

A recurring theme across all documents is the specific challenges faced by **Korean and other foreign companies** defending patent suits in the US (venue exposure, discovery asymmetry, NPE targeting).

## Document Architecture

Directories are numbered to match the litigation lifecycle in chronological order:

```
00-overview/          — Full lifecycle orientation, roles, cost expectations
01-pre-litigation/    — Demand letter triage, litigation hold
02-case-initiation/   — First 2 weeks protocol, venue, early strategy
03-post-grant-proceedings/ — IPR/PGR/ex parte reexamination at PTAB
04-claim-construction/     — Markman hearing strategy
05-discovery/         — Document production, privilege protection
06-expert-witnesses/  — Expert selection, Daubert strategy
07-damages-defense/   — Apportionment, Georgia-Pacific, willfulness
08-settlement-and-licensing/ — Settlement decision framework, license terms
09-trial-preparation/ — Summary judgment, MIL, jury selection, eBay
10-appeals/           — Federal Circuit standards and strategy
11-portfolio-management/ — FTO analysis, design-arounds, defensive portfolio
appendices/           — Key deadlines, glossary, vendor guide
```

**README.md is the single source of truth for planned structure.** Its navigation table lists all 20 planned documents (currently 7 exist). When adding a new document, update that table.

## Document Format Conventions

Every document follows this internal structure:

1. `# Title` — top-level heading
2. `> **Quick Reference:**` blockquote — one-sentence takeaway for the reader in a hurry
3. Numbered `##` sections ordered: narrative/overview → checklists → comparison tables → decision trees
4. `🌏` prefix on any section that addresses Korean or foreign company–specific considerations
5. Cross-references use relative markdown links: `[text](../NN-section/filename.md)`

## Legal Content Standards

- **Case citations:** `*Case Name* (Fed. Cir. YYYY)` or `(SCOTUS YYYY)` or `(PTAB YYYY)` — always italicize the case name in markdown
- **Statute citations:** `35 U.S.C. § XXX` — always include the title number and the `§` symbol
- **Standards of proof:** Explicitly distinguish "clear and convincing evidence" (district court invalidity) from "preponderance of the evidence" (PTAB invalidity)
- **Statistics** (IPR institution rates, cost ranges, timelines): Include the fiscal year or date so readers know how current the data is

### Key precedents already cited across existing documents

| Case | Court/Year | Key Holding |
|---|---|---|
| *TC Heartland v. Kraft Foods* | SCOTUS 2017 | Patent venue for US domestic defendants: § 1400(b) only |
| *In re HTC Corp.* | Fed. Cir. 2018 | Foreign defendants can be sued in any US district (§ 1391(c)(3)) |
| *Halo Electronics v. Pulse* | SCOTUS 2016; Fed. Cir. Feb. 2025 remand | Willfulness ≠ enhanced damages; court retains discretion |
| *Ingenico Inc. v. IOENGINE, LLC* | Fed. Cir. May 2025 | IPR § 315(e) estoppel does NOT apply to product prior art, prior use, or on-sale bar |
| *Recentive Analytics v. Fox Corp.* | Fed. Cir. April 2025 | Applying generic ML to a new data domain = § 101 ineligible |
| *EcoFactor v. Google* | Fed. Cir. en banc 2025 | Comparable license apportionment requirements |
| *Rex Medical v. Intuitive Surgical* | Fed. Cir. Sept. 2025 | Apportionment of comparable licenses is mandatory |
| *Ironburg Inventions v. Valve Corp.* | Fed. Cir. April 2023 | Patent owner bears burden of proving IPR estoppel; "reasonably could have raised" = diligent search |

## Contribution Workflow

- **Branch:** `claude/patent-dispute-guidelines-X5ESQ`
- Commit each new document as a **separate commit** with a message that describes the document's specific coverage (not just "add file")
- After completing all planned files, push with `git push -u origin claude/patent-dispute-guidelines-X5ESQ`
- Do not create a pull request unless the user explicitly requests it
