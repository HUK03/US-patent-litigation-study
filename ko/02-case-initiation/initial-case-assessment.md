# 초기 사건 평가 (Initial Case Assessment)

> **빠른 참조(Quick Reference):** 소장이 송달되었습니다. 답변 기한은 21일입니다(연장은 통상 가능하지만 즉시 요청해야 함). 이 문서는 최초 2주 동안 무엇을 해야 하는지와 경영진 대상 현실적 초기 평가 프레임을 다룹니다.

---

## 1. 송달 후 첫 2주: 실행 체크리스트

### Day 1–3
- [ ] 송달 일자·방식 확인, **답변 21일 기한** 캘린더 등록
- [ ] 사전 지정 외부 특허소송 대리인(Outside counsel) 즉시 연락(또는 RFP 시작)
- [ ] 소송보존조치(litigation hold) 발령/확인([소송보존](../01-pre-litigation/litigation-hold-evidence-preservation.md) 참조)
- [ ] 답변 기한 연장 확보(통상 합의로 30–60일 추가; 필요 시 모션)
- [ ] IPR 기한 계산 시작: **송달일부터 365일**(35 U.S.C. § 315(b))
- [ ] 도켓(PACER)에서 소장·특허·첨부자료 확보
- [ ] 주장 청구항(asserted claims) 식별(미기재 시 로컬 규칙에 따라 후속 특정)
- [ ] 피소 제품(들)과 관련 사업부 매핑

### Day 3–7
- [ ] IP 변호사, 소송변호사, 사업부 리드 내부 킥오프 회의
- [ ] 책임 배정: 기술분석, 재무데이터 수집, 선행기술 검색
- [ ] 출원경과(prosecution history) 검토 시작(USPTO Patent Center 다운로드)
- [ ] 예비 무효성 검색 시작(§ 101, § 102, § 103, § 112)
- [ ] 예비 클레임 매핑 시작: 청구항 요소가 피소 제품에 읽히는가?
- [ ] 소송 재판지(지방법원) 및 로컬 특허규칙 확인
- [ ] 공동피고(co-defendants) 확인: 동일 특허로 타사도 피소되었는가? 공조 가능성?

### Day 7–14
- [ ] 예비 사건평가 메모 작성(아래 템플릿)
- [ ] 단계별(phase-gated) 소송예산 추정 개발
- [ ] § 101 초기 모션(Alice/Mayo) 제기 여부 판단
- [ ] IPR 예비 go/no-go 결정(365일 마감 전 정밀분석 완료)
- [ ] 경영진/이사회 브리핑(브리핑 문서화 + 특권 유지)
- [ ] 🌏 ITC Section 337 소장이 동시 제기된 경우 즉시 양 트랙 방어 연계

---

## 2. 내부 킥오프 회의 아젠다 템플릿

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

## 3. 소장 읽기(Reading the Complaint)

### 주장 청구항 식별(Identifying the Asserted Claims)
특허소장은 구체 청구항을 적시하지 않고 특허 전체를 주장하는 경우가 많습니다. 대부분 법원의 로컬 특허규칙에 따라:
- **원고는 침해주장서(infringement contentions)** 를 일정 기간 내(통상 Rule 16 회의 후 14–45일) 제출해야 하며, 각 피소제품과 각 주장청구항 매핑 클레임차트를 포함
- 침해주장서 제출 전까지는 사실상 특허 전체를 방어해야 함
- 초기에는 **독립항(independent claims)** 중심으로 검토(종속항은 독립항 입증이 선행)

### 청구항 구조 이해
```
Independent Claim (e.g., Claim 1):
  "A [device/method/system] comprising:
   [Element A];
   [Element B]; and
   [Element C]."

Dependent Claim (e.g., Claim 3):
  "The [device] of claim 1, wherein [Element B] further comprises [D]."
```

어떤 청구항을 침해하려면 해당 청구항의 모든 요소가 피소제품에 존재해야 합니다(all-elements rule). 요소 하나라도 없으면 문언침해(literal infringement)는 성립하지 않습니다. 다만, 실질적으로 동일한 기능·방법·결과라면 균등론(doctrine of equivalents)이 적용될 수 있습니다.

### 손해배상 이론 식별
소장은 통상 최소한의 손해배상 유형을 시사해야 합니다.
- "재판에서 입증될 금액의 손해배상" — 일반적 표현(합리적 로열티/일실이익 가능)
- 금지명령(injunctive relief) — 운영회사 사건에서 위협 큼; NPE는 *eBay* 이후 드묾
- 가중손해배상(enhanced damages, willfulness) — 소 제기 전 인지 주장 여부 확인
- § 285 변호사비(예외적 사건) 청구

---

## 4. 예비 무효성 분석 (Preliminary Invalidity Analysis)

무효성은 가장 강력한 방어 수단 중 하나입니다. 특허가 법정 요건을 충족하지 못하면 무효입니다.

### § 102 — 신규성 결여/선행기술 대비 동일성(Anticipation)
**단일 선행기술(single reference)** 이 청구항의 모든 요소를 개시하면 해당 청구항은 무효입니다. 주요 선행기술 소스:
- 선행 특허 및 공개특허(미국/해외)
- 학술논문 및 학회 발표
- 제품 매뉴얼, 데이터시트, 기술명세
- **자사 과거 제품/공개물/발표자료**(자주 간과되나 매우 중요)
- 오픈소스 저장소(GitHub 커밋 일자)
- 산업 표준 문서

**우선일(priority date):** 선행기술은 특허의 **우선일** 이전이어야 합니다(통상 패밀리 최조 출원일). 출원경과에서 실제 우선일을 반드시 확인하십시오.

### § 103 — 비자명성 결여(Obviousness)
발명 당시 통상의 기술자(POSITA) 관점에서, 다수 선행기술의 결합으로 자명하면 무효입니다.

방어 논리:
- 둘 이상의 선행기술 결합으로 모든 청구항 요소 개시
- 결합 동기(motivation to combine) 존재(설계 필요, 공지기술, 선행기술의 명시 제안)
- 결합을 저해할 성공가능성 부재 주장 반박

### § 101 — 특허적격성(Patent-Eligible Subject Matter, Alice/Mayo)
*Alice* (2014), *Mayo* (2012) 프레임워크:
1. **Step 1:** 추상적 아이디어/자연현상/자연법칙에 지향되는가?
2. **Step 2:** 그렇다면 청구항이 발명의 본질을 변환하는 "무언가 더(inventive concept)"를 포함하는가?

소프트웨어, AI/ML, 비즈니스방법 특허는 취약한 편입니다. **2025년 판례:** *Recentive Analytics v. Fox* (Fed. Cir. 2025.4) — **기지의 ML 방법을 새로운 데이터 영역에 적용**하는 것만으로는 § 101 적격성 불충분.

**§ 101 모션 시기:** 초기 단계 Rule 12(b)(6) 또는 조기 SJ는 비용 효율적일 수 있으나, 성공 여부는 청구항 문언·관할별 성향에 크게 좌우됩니다.

### § 112 — 기재요건, 실시가능요건, 명확성
- **기재요건(written description):** 출원 시점에 발명을 실제 보유(possession)했음을 명세서가 보여야 함
- **실시가능요건(enablement):** 과도한 실험 없이 POSITA가 발명을 구현·사용 가능해야 함
- **명확성(definiteness)** (*Nautilus*, 2014): POSITA가 청구범위를 **"합리적 확실성(reasonable certainty)"** 으로 이해할 수 있어야 함

---

## 5. 예비 비침해 분석 (Preliminary Non-Infringement Analysis)

### 청구항 요소 매핑(Claim Element Mapping)

각 주장청구항별로 요소를 피소제품에 매핑하십시오.

| 청구항 요소 | 제품 내 존재 여부 | 증거 출처 | 리스크 수준 |
|---|---|---|---|
| [넓게 해석된 요소 A] | Yes / No / Uncertain | [설계문서, 소스코드, 데이터시트] | High / Med / Low |
| [요소 B] | ... | ... | ... |
| [요소 C] | ... | ... | ... |

**어느 한 요소라도 부재하면:** 문언침해 부정. 다만 균등론(DOE) 적용 가능성은 추가 검토.

### 일반적인 비침해 주장

1. **요소 부재(missing element):** 필수 청구항 요소가 피소제품에 없음
2. **해석 차이(different construction):** 올바른(협의) 용어 해석 하에서는 요소 충족 안 됨
3. **방법항 all-steps rule:** 방법항은 모든 단계 수행 입증 필요(또는 *Akamai* 공동침해 귀속)
4. **출원경과 금반언(prosecution history estoppel):** 심사과정 축소 후 DOE 확장 주장 제한
5. **제품 vs 공정 차이:** 피소제품이 청구된 공정과 다른 방식으로 제조됨

---

## 6. 외부 대리인 선정 및 예산

### 외부 대리인 선정 기준

| 기준 | 평가 포인트 |
|---|---|
| **기술 전문성** | 피소 기술(전기/소프트웨어/기계)과 매칭되는 파트너 역량 |
| **소송 실적** | 해당 재판지 승소율? Federal Circuit 성과? |
| **PTAB 경험** | IPR 청구서 성공률? (1년 내 제기 필수) |
| **재판지 경험** | 현재 사건 관할에서의 실무 경험 |
| **사내 커뮤니케이션 스타일** | 사내 요청 대응성, 전략 설명 명확성 |
| **인력 운영 모델** | 실제 수행 주체(파트너 vs 어소시에이트) |
| **보수 구조** | 시간당? AFA? 하이브리드 캡 방식? |

🌏 **한국 기업 참고:** **한국어 대응 인력 또는 코리아 데스크 역량**이 있는 로펌을 선택하십시오(한국어 문서 검토, 한국 엔지니어/임원 협업, 국제 증거개시 운영 필수).

### 단계별 소송예산 템플릿

| 단계 | 추정 비용 | 트리거/의사결정 시점 |
|---|---|---|
| 사건 개시 및 초기 모션 | $100K–$300K | 소장 송달 |
| IPR 청구(제기 시) | $75K–$150K/청구 | Day 365 전 결정 |
| 청구항 해석/Markman | $200K–$500K | 스케줄링 오더 |
| 사실증거개시 | $500K–$2M | Post-Markman |
| 전문가 보고서 | $400K–$1M | 사실증거개시 후 |
| 약식판결 | $200K–$600K | 전문가증거개시 후 |
| 재판 | $500K–$3M | SJ 이후 |
| 재판후/항소 | $200K–$800K | 평결 후 |
| **총 추정 범위** | **$2M–$8M+** | |

---

## 7. 사건평가 메모 템플릿

소장 수령 후 14일 내(Privileged 표시) 배포:

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
