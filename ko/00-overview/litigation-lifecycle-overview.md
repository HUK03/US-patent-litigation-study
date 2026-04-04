# 미국 특허 소송(US Patent Litigation): 라이프사이클 개요

> **빠른 참조(Quick Reference):** 이 문서는 피고(defendant) 관점에서 특허 소송 전체 라이프사이클을 한눈에 파악하도록 돕습니다. 현재 사건이 어느 단계에 있는지, 다음 단계가 무엇인지, 단계별로 누가 관여해야 하는지를 확인할 때 사용하세요.

---

## 1. 피고 관점의 미국 특허 소송 지형(US Patent Litigation Landscape)

### 사건 규모와 리스크(Volume and Stakes)

미국 특허 소송은 전 세계 지식재산(IP) 분쟁 중 비용과 복잡성이 가장 큰 영역에 속합니다. 기업 피고(corporate defendant) 기준 핵심 포인트는 다음과 같습니다.

- 미국 연방지방법원(US federal district courts)에 매년 **3,500건 이상 특허소송(patent suits)** 이 제기됩니다.
- 특허 사건을 1심 재판(trial)까지 방어(defense)하는 데 드는 중간값 비용(median cost)은 **$3M–$5M 이상**이며, 고위험 사건은 **$10M–$30M+**가 흔합니다.
- **비실시주체(NPE, Non-Practicing Entity / "patent troll")** 가 대형 기술·전자 기업을 상대로 한 소송의 다수를 제기합니다.
- 주요 특허재판지(patent districts)에서 제소부터 재판까지 평균 기간은 **2.5~4년+**이며, 국제무역위원회(ITC) 사건은 통상 **10~12개월** 내 결론이 납니다.

### 대기업을 제소하는 원고 유형(Who Sues Large Corporations)

| 원고 유형(Plaintiff Type) | 설명(Description) | 전형적 목표(Typical Goal) | 방어 우선순위(Defense Priority) |
|---|---|---|---|
| **NPE / Patent Troll** | 특허는 보유하나 제품은 생산하지 않음 | 라이선스 수익/합의금 | 무효(invalidity, IPR), 비침해(non-infringement), 손해배상 안분(damages apportionment) |
| **특허공격주체(PAE, Patent Assertion Entity)** | 소송 비즈니스 모델을 가진 고도화된 NPE | 최대 손해배상 또는 포트폴리오 라이선스 | 위 항목 + 조기 합의 분석(early settlement analysis) |
| **경쟁사(Competitor)** | 동일 시장의 운영회사(operating company) | 금지명령(injunction), 손해배상, 협상 레버리지 | 비침해, 크로스 라이선스(cross-license), 반소(countersuits) |
| **발명자/대학(Inventor/University)** | 원특허권자(original patent holder)의 권리 행사 | 라이선스, 명예/인정 | 무효, 출원경과금반언(prosecution history estoppel) |
| **표준특허 라이선서(Standard Body Licensors)** | 표준필수특허(SEP, Standard Essential Patent) 보유자 | FRAND 로열티 | FRAND 요율 방어(FRAND rate defense), SSPPU 안분(SSPPU apportionment) |

### 🌏 한국/외국 기업 경보(Korean/Foreign Company Alert)

한국 기업, 특히 삼성(Samsung), LG, SK, 현대·기아(Hyundai/Kia) 계열은 미국에서 **NPE의 주요 타깃 피고**입니다. 삼성은 대략 5일에 1건 수준으로 신규 NPE 소송에 노출된 시기가 있었고, 2024년 기준 가장 많이 제소된 대기업으로 집계된 바 있습니다. 외국 기업(foreign companies)은 **TC Heartland 판례에 따른 재판지 보호(TC Heartland venue protection)** 를 일반적으로 기대하기 어려워, 미국 내 다양한 지방법원에서 제소될 수 있습니다. 자세한 내용은 [재판지 및 관할(Venue & Jurisdiction)](../02-case-initiation/venue-and-jurisdiction.md)을 보세요.

---

## 2. 소송 라이프사이클 텍스트 플로우차트(Litigation Lifecycle: Text Flowchart)

아래는 피고가 방어하는 전형적 특허 사건의 흐름입니다. `[대괄호]`는 지방법원 사건과 병행(parallel)될 수 있는 절차를 의미합니다.

```
위협 접수(THREAT RECEIVED)
(경고장 Demand Letter / 중지요청 C&D / 침해통지 Notice of Infringement)
        │
        ▼
소송 전 단계(PRE-LITIGATION PHASE)
• 위협 분류 및 평가(threat triage and assessment)
• 소송보존명령(litigation hold) 발령(합리적으로 소송이 예상되는 경우)
• 특허/권리자 배경조사
• 예비 침해·무효 분석(preliminary infringement & validity analysis)
• 확인의 소(Declaratory Judgment, DJ) 전략 검토
        │
        ▼
소장 제기 및 송달(COMPLAINT FILED & SERVED)
• 답변서(Answer) 기한: 21일(연장 가능)
• 소송보존명령 확인 및 확대
• 외부 소송대리인(outside counsel) 선임/가동
• 초기 사건평가 메모(initial case assessment memo) 작성
• [ITC §337 조사(Investigation) 병행 제기 가능]
        │
    ┌───┴───────────────────────────────────┐
    ▼                                       ▼
지방법원 소송(DISTRICT COURT)           [PTAB의 IPR / PGR]
                                         • 송달 후 1년 내 제기(file within 1 year)
                                         • 청원 비용: 약 $50K–$150K
                                         • 개시결정(institution decision): 약 6개월
                                         • 최종서면결정(FWD): 개시 후 12개월
                                         • [지방법원 절차중지 신청(Motion to Stay)]
    │
    ▼
사건 초기(CASE INITIATION, 1~6개월)
• Rule 26(f) 협의(conference)
• 스케줄링 오더(scheduling order) 협의
• 지역 특허규칙(local patent rules): 침해 주장서(plaintiff infringement contentions)
• 지역 특허규칙(local patent rules): 무효 주장서(defendant invalidity contentions)
• 초기 사건 전략 확정
• §101 신청(Alice challenge 가능 시)
        │
        ▼
청구항 해석(Claim Construction/Markman) (6~18개월, 법원별 상이)
• 쟁점 용어 식별·서면 공방
• 마크만 심리(Markman hearing)
• 청구항 해석 명령(claim construction order)
• 판결 취지에 따른 전략 조정
        │
        ▼
사실심리 디스커버리(Fact Discovery, 6~24개월)
• 문서제출(document production)
• 소스코드 검토(source code review)
• 인터로가토리/자백요청(interrogatories / requests for admission)
• 발명자 증언녹취(inventor depositions)
• 법인대표 증언녹취(30(b)(6) depositions)
• 제3자 소환장(third-party subpoenas)
        │
        ▼
전문가 디스커버리(Expert Discovery, 18~30개월)
• 전문가 초기보고서(opening expert reports: 침해/무효/손해배상)
• 반박보고서(rebuttal reports)
• 전문가 증언녹취(expert depositions)
• 다우버트 신청(Daubert motions, 전문가 증거 배제)
        │
        ▼
약식판결(Summary Judgment, 24~36개월)
• 비침해/무효 약식판결 신청
• 반대서면 및 답변서
• 심문 및 결정
        │
        ▼
재판 전 단계(PRE-TRIAL, 30~42개월)
• 재판전명령(pre-trial order)
• 증거배제 신청(motions in limine)
• 배심지시안(jury instructions) 협의
• 증거목록(exhibit lists) 확정
• 배심선발 질문(voir dire questions) 준비
        │
        ▼
본안 재판(TRIAL, 통상 5~10일)
• 배심원 선정(voir dire)
• 개시진술(opening statements)
• 원고 입증(침해/손해배상)
• 피고 입증(비침해/무효/손해배상 방어)
• 최후변론(closing arguments)
• 평의(jury deliberations)
• 평결(verdict)
        │
        ▼
재판 후 절차(POST-TRIAL, 평결 후 1~6개월)
• JMOL 신청(Rule 50(b), 법적으로 불충분한 평결 공격)
• 신규재판 신청(new trial motion, Rule 59)
• 증액손해배상(enhanced damages) 관련 서면
• 변호사보수 신청(attorney fee motion, §285)
• 금지명령 절차(injunction proceedings, eBay 4요소 테스트)
        │
        ▼
연방순회항소법원 항소(APPEAL TO FEDERAL CIRCUIT)
• 항소통지(notice of appeal): 최종판결 후 30일
• 서면공방(briefing): 약 12~18개월
• 구두변론(oral argument): 통상 당사자별 15분
• 판결(decision): 변론 후 통상 6~12개월
        │
        ▼
(환송 가능성/대법원 상고허가 certiorari 가능성)
```

---

## 3. 핵심 의사결정 게이트(Key Decision Points and Gate Reviews)

각 마일스톤에서 “계속 방어할지”, “전략을 전환할지”, “합의할지”를 점검하는 표입니다.

| 게이트(Gate) | 트리거(Trigger) | 핵심 질문(Key Question) | 방어 지속 기준(Criteria for Continued Defense) | 참조 문서(Document) |
|---|---|---|---|---|
| **G-1: 제소 전(Pre-Suit)** | 경고장 수령 | 다툴지, 협의할지? | 강한 무효/비침해, DJ 관할 성립, 높은 손해배상 노출 | [위협 평가(Threat Assessment)](../01-pre-litigation/threat-assessment.md) |
| **G-2: 제소 직후(Complaint Filed)** | 소장 송달 | IPR 제기 여부? 핵심 방어이론은? | 선행기술(prior art) 존재, 청구항 범위, 1년 제소시효(one-year clock) | [IPR/PGR 전략](../03-post-grant-proceedings/ipr-pgr-strategy-and-timing.md) |
| **G-3: 마크만 후(Post-Markman)** | 청구항 해석 명령 | 해석이 유리/불리한가? | 불리한 해석이면 재평가, 설계우회(design-around) 가능성 | [청구항 해석(Claim Construction)](../04-claim-construction/claim-construction-strategy.md) |
| **G-4: 전문가 보고서 후(Post-Expert Reports)** | 초기 전문가 보고서 교환 | 본안 승소 가능성은? | 강한 전문가 의견, 손해배상 노출 정량화 | [전문가 증인(Expert Witnesses)](../06-expert-witnesses/expert-witness-management.md) |
| **G-5: 재판 전(Pre-Trial)** | SJ 결정 완료 | 재판 리스크 수용 가능한가? | 핵심 쟁점 존속, 배심 리스크 관리 가능, 비용 대비 타당 | [재판 준비(Trial Preparation)](../09-trial-preparation/trial-preparation-guide.md) |
| **G-6: 평결 후(Post-Verdict)** | 배심 평결 | 항소할 것인가? | 법률오류 보존, 파기 가능성 >30%, 제품 이슈 지속 | [항소 가이드(Appeals Guide)](../10-appeals/appeals-guide.md) |

---

## 4. 병행절차: 지방법원과 PTAB(Parallel Proceedings)

전략상 가장 중요한 선택 중 하나는, 지방법원 방어와 동시에 **특허심판원(PTAB) IPR/PGR**을 제기할지 여부입니다. 두 절차는 병행되며 서로 강하게 영향을 줍니다.

```
지방법원 사건(District Court)         PTAB(IPR/PGR)
──────────────────────             ──────────────
소장 제기(Day 0)
                                     ← IPR 제기 마감: 365일
IPR 제기(예: Day 180)
                                     개시결정(Institution, ~Day 360)
Markman 심리(~Month 12)            ───── 절차중지(Motion to Stay) ───→
                                     PTAB 본심리 시작(~Month 18)
사실심리 디스커버리(~Months 12–24)
                                     최종서면결정(Final Written Decision, ~Month 30)
전문가 디스커버리(~Months 24–30)
                                     ← 청구항 취소 시 지방법원 사건에 직접 영향
약식판결(~Months 28–36)
```

**핵심 상호작용 포인트(Critical interaction points):**
- IPR 성공 시 주장 청구항(asserted claims)이 **취소(cancellation)** 되어 지방법원 사건이 실익을 잃을 수 있습니다.
- IPR 금반언(IPR estoppel, §315(e))은 IPR에서 “제기했거나 합리적으로 제기할 수 있었던” 무효 주장을 지방법원에서 제한할 수 있습니다. 다만 *Ingenico Inc. v. IOENGINE* (Fed. Cir., 2025년 5월)에서는 금반언 범위를 **§102/§103 인쇄간행물(printed publication) 근거**로 한정하고, 제품 선행기술(product prior art)·공용(public use)·판매(on-sale) 근거에는 일반적으로 미치지 않는다고 보았습니다.
- IPR 계류 중 지방법원 **절차중지(stay)** 가 인용되면 소송비를 크게 줄일 수 있으나, 인용률은 재판지(district)별 편차가 큽니다.

---

## 5. 역할·책임 매트릭스(Roles and Responsibilities)

| 활동(Activity) | 사내 IP 변호사(In-House IP Counsel) | 사내 소송 변호사(In-House Litigation Counsel) | 사업부/엔지니어링(BU/Engineering) | 외부 대리인(Outside Counsel) | 경영진/이사회(Management/Board) |
|---|---|---|---|---|---|
| 위협 분류(threat triage) | **주도(Lead)** | 협의(Consult) | 통지(Inform) | 협의 | 브리핑(Brief) |
| 소송보존명령(litigation hold) | 주도 | **주도** | 준수(Comply) | 자문(Advise) | 해당없음(N/A) |
| 외부 대리인 선정 | **주도** | 공동주도(Co-lead) | N/A | N/A | 승인(대형사건) |
| 예산 승인 | 권고(Recommend) | 권고 | N/A | 추정치 제공 | **승인(Approve)** |
| IPR 제기 결정 | **공동주도** | 협의 | N/A | **공동주도** | 브리핑 |
| 기술/선행기술 분석 | 협의 | N/A | **주도** | 주도 | N/A |
| 합의 권한(settlement authority) | 권고 | 권고 | 의견제공(Input) | 자문 | **승인** |
| 재판 전략 결정 | 협의 | **주도** | 지원(Support) | **주도** | 주요 의사결정 승인 |

---

## 6. 단계별 비용 및 리소스 전망(Cost and Resource Expectations)

아래 수치는 중간 복잡도 사건(단일 특허, 중간 가치 제품) 기준의 **대략적 범위(rough order-of-magnitude)** 입니다. 고위험 사건(복수 특허, 초고가 매출 제품)은 3~5배 이상이 될 수 있습니다.

| 단계(Phase) | 통상 비용 범위(Typical Cost Range) | 주요 비용 동인(Key Cost Drivers) |
|---|---|---|
| 제소 전 위협평가 | $15K–$50K | 선행기술 조사 깊이, 기술 복잡도 |
| 사건 개시/초기 신청 | $100K–$300K | §101 신청, 답변서 준비 |
| IPR 청원(제기 시) | 건당 $50K–$150K | 다툴 청구항 수, 전문가 선언서 |
| 청구항 해석/Markman | $150K–$400K | 쟁점 용어 수, 기술설명(tutorial) 준비 |
| 사실심리 디스커버리 | $500K–$2M | 문서량, 증언녹취 횟수 |
| 전문가 보고/증언녹취 | $300K–$1M | 전문가 수, 기술·손해배상 이슈 복잡도 |
| 약식판결 | $200K–$600K | 신청 건수, 법리 복잡도 |
| 본안 재판 | $500K–$2M+ | 기간, 증인 수, 시각자료(demonstratives) |
| 재판 후/항소 | $200K–$800K | 법률쟁점 복잡도 |
| **합계(통상 범위)** | **$2M–$8M** |  |
| **고위험 사건** | **$10M–$30M+** |  |

> 위 수치는 외부 대리인 비용(outside counsel fees) 중심입니다. 내부 비용(경영진 투입시간, IT, 해외기업 번역/증거관리)은 별도로 크게 증가할 수 있습니다.

---

## 7. ITC Section 337 트랙

미국으로 제품을 수입(import)하는 외국 기업에는 **ITC Section 337 조사**가 지방법원 소송과 병행되거나 대체 경로가 될 수 있습니다.

| 항목(Feature) | 지방법원(District Court) | ITC Section 337 |
|---|---|---|
| 심리까지 기간 | 2~5년 | **10~12개월** |
| 구제수단(Remedy) | 손해배상 + 금지명령 | **수입금지(배제명령, exclusion order)** / 손해배상 없음 |
| 약식판결 활용 | 보편적(Common) | 제한적(Rare, summary determination) |
| 무효 입증책임 | 명백·확신 증명(clear and convincing) | 명백·확신 증명 |
| 합의율(settlement rate) | ~95% | ~55% |
| 국내산업 요건(domestic industry) | 불요 | **필요(기술요건+경제요건)** |
| 대통령 검토(Presidential review) | 없음 | 있음(60일) |
| PTAB 병행 | 가능 | 가능(IPR 병행 권장) |

🌏 한국 기업에 ITC가 특히 중요한 이유:
1) 제품의 해외 생산 후 미국 수입 구조가 많고,
2) 신속 절차로 합의 압박이 매우 크며,
3) 한국 기업도 공세적으로 ITC를 활용하는 추세가 있기 때문입니다.

---

## 8. 원문 대비 보완: 단계별 산출물(Deliverables by Phase)

| 단계 | 필수 산출물 | 오너 |
|---|---|---|
| Pre‑Litigation | 위협평가 메모, hold notice, 초기 클레임 차트 | 사내 IP/소송팀 |
| Case Initiation | ICA, 스케줄링 전략안, 무효 주장서 초안 | 외부 대리인 + 사내 소송팀 |
| PTAB 병행 | IPR/PGR Go‑NoGo 메모, prior art 패킷 | PTAB 팀 |
| Discovery | ESI 프로토콜, custodian 매트릭스, privilege 기준서 | discovery PM |
| Expert Phase | 전문가 범위문서, 핵심 쟁점표, 반박 로드맵 | 소송팀/전문가 |
| Trial Prep | 증인 북, 전시물 리스트, MIL 전략표 | 재판팀 |
| Post‑Trial | JMOL/Rule59 초안, 항소 체크리스트 | 항소팀 |

## 9. 원문 대비 보완: 실패 패턴과 대응

| 실패 패턴 | 영향 | 예방 조치 |
|---|---|---|
| 초기 사실관계 미정리 | 방어논리 흔들림 | Day 30 ICA 고정 |
| IPR 타이밍 지연 | Fintiv/estoppel 불리 | 3~6개월 내 제기 판단 |
| 디스커버리 범위 과다 | 비용 급증 | staged discovery 운영 |
| 손해모델 조기대응 부족 | 고액 평결 노출 | Daubert/MIL 동시 준비 |
| 재판 메시지 과복잡 | 배심 설득력 저하 | 2~3개 핵심 내러티브 유지 |

## 10. 원문 대비 보완: 경영진 보고 리듬

- 월간: 비용·리스크 대시보드
- 분기: 소송 포트폴리오/선례 영향
- 이벤트성: Markman, IPR institution, SJ, 평결 직후

경영진 보고서는 법리 상세보다 “의사결정 포인트 + 비용/사업 영향” 중심으로 구성합니다.
