# 미국 특허 소송 방어 가이드라인

[상위 목차(ko/README.md)](README.md)


> **면책고지(Disclaimer):** 본 가이드라인은 내부 정보 제공 목적이며 법률 자문(legal advice)이 아닙니다. 특허 소송은 사실관계 및 관할에 따라 크게 달라집니다. 어떠한 법적 조치 또는 중대한 의사결정을 하기 전에 반드시 자격을 갖춘 미국 특허 소송 변호사를 선임하십시오.

---

## 목적 및 범위 (Purpose & Scope)

이 저장소는 미국 특허 침해 주장에 대응하는 **기업 법무 및 IP 팀(corporate legal and IP teams)** 을 위한 실무적·운영적 가이드라인을 제공합니다. 주요 대상은 다음과 같습니다.

- 특허 소송 포트폴리오를 관리하는 **사내 IP 변호사(in-house IP counsel)**
- 사업부와 외부 대리인을 조율하는 **IP 매니저(IP managers)**
- 전문 분야 외의 특허 분쟁을 다루는 **기업 법무 일반 담당자(corporate legal generalists)**
- 제품이 침해 혐의를 받는 **사업부 리더(business unit leaders)**

초점은 **방어(defensive)** 입니다. 대형 기술, 전자, 제조 기업은 특히 비실시기관(NPEs/patent trolls)의 주요 표적이며, 본 가이드라인은 최초 경고장부터 재판, 항소, 선제적 포트폴리오 관리까지 특허 방어의 전체 생애주기를 다룹니다.

> **한국 및 해외 기업 안내(Note for Korean and Foreign Companies):** 저장소 전반에서 🌏 표시는 미국에서 특허 소송을 방어하는 비미국 기업(특히 한국 기업)을 위한 특수 고려사항을 강조합니다. 해외 기업은 고유한 재판지 노출(venue exposure), 증거개시(discovery) 부담, 절차상 리스크를 가지므로 별도 주의가 필요합니다. 아래 [해외 기업 고려사항 개요](#foreign-company-considerations)를 확인하세요.

---

## 저장소 탐색 방법 (How to Navigate This Repository)

| 단계(Phase) | 문서(Document) | 핵심 주제(Key Topics) |
|---|---|---|
| **개요(Overview)** | [소송 생애주기 개요](00-overview/litigation-lifecycle-overview.md) | 전체 생애주기, 역할, 비용 기대치 |
| **소송 전(Pre-Litigation)** | [위협 평가](01-pre-litigation/threat-assessment.md) | 경고장, 분류(triage), DJ 전략 |
| | [소송보존 및 증거보전](01-pre-litigation/litigation-hold-evidence-preservation.md) | 보존 통지, ESI, 증거훼손(spoliation) 위험 |
| **사건 개시(Case Initiation)** | [초기 사건 평가](02-case-initiation/initial-case-assessment.md) | 첫 2주, 무효/침해 분석 |
| | [재판지 및 관할](02-case-initiation/venue-and-jurisdiction.md) | TC Heartland, 해외 피고 규칙, 이송 |
| | [초기 사건 전략](02-case-initiation/early-case-strategy.md) | 방어 이론, § 101 모션, 고의침해(willfulness) |
| | [ITC Section 337 방어 플레이북](02-case-initiation/itc-section-337-defense-playbook.md) | ITC 일정, domestic industry, 구제수단 방어 |
| **등록 후 절차(Post-Grant Proceedings)** | [IPR/PGR 개요](03-post-grant-proceedings/ipr-pgr-overview.md) | 절차 구조, 금반언(estoppel), 비교표 |
| | [IPR/PGR 전략 및 타이밍](03-post-grant-proceedings/ipr-pgr-strategy-and-timing.md) | 의사결정 트리, 청구서, 소송정지(stay) 신청 |
| | [IPR 방어 플레이북](03-post-grant-proceedings/ipr-defense-playbook.md) | 30일 준비체계, Fintiv 대응, estoppel 통제 |
| | [직권 재심사(Ex Parte Reexamination)](03-post-grant-proceedings/ex-parte-reexamination.md) | IPR 대비 활용 시점 |
| **청구항 해석(Claim Construction)** | [청구항 해석 전략](04-claim-construction/claim-construction-strategy.md) | Markman 준비, 쟁점 용어 선정, 출원경과 |
| **증거개시(Discovery)** | [증거개시 전략](05-discovery/discovery-strategy.md) | 문서제출, 질의서(interrogatories), 증언녹취(depositions) |
| | [특권 및 워크프로덕트](05-discovery/privilege-and-work-product-protection.md) | 사내 특권, 변호사의견(opinion of counsel), FRE 502(d) |
| **전문가 증인(Expert Witnesses)** | [전문가 증인 관리](06-expert-witnesses/expert-witness-management.md) | 선정, Daubert, 증언 준비 |
| **손해배상 방어(Damages Defense)** | [손해배상 방어 전략](07-damages-defense/damages-defense-strategy.md) | Georgia-Pacific, 안분(apportionment), 고의침해 |
| **합의(Settlement)** | [합의 및 라이선싱 전략](08-settlement-and-licensing/settlement-and-licensing-strategy.md) | 의사결정 매트릭스, 협상, 라이선스 조건 |
| **재판(Trial)** | [재판 준비 가이드](09-trial-preparation/trial-preparation-guide.md) | SJ 모션, MIL, 배심원 선정, eBay |
| **항소(Appeals)** | [항소 가이드](10-appeals/appeals-guide.md) | Federal Circuit, 심사 기준 |
| **포트폴리오 관리(Portfolio Mgmt)** | [실시자유(FTO)](11-portfolio-management/freedom-to-operate.md) | FTO 방법론, 제품 출시 게이트 |
| | [디자인어라운드 및 방어 포트폴리오](11-portfolio-management/design-arounds-and-defensive-portfolio.md) | 디자인어라운드, 방어 특허, LOT/OIN |
| **참고(Reference)** | [핵심 기한 레퍼런스](appendices/key-deadlines-reference.md) | 모든 중요 소송 기한 |
| | [용어집](appendices/glossary.md) | 50개 이상 핵심 용어 정의 |
| | [벤더 및 리소스 가이드](appendices/vendor-and-resource-guide.md) | 도구, 데이터베이스, 서비스 제공자 |

---

## 빠른 접근: 최초 72시간 체크리스트 (Quick Access: First 72 Hours Checklist)

경고장 또는 소장이 도착하면 시간이 핵심입니다. 즉시 아래 체크리스트를 사용하십시오.

- [ ] 변호사 검토 없이 어떤 경고장에도 **응답하지 말 것**
- [ ] 모든 커뮤니케이션 **보존** — 즉시 IP/법무 전달, 삭제 금지 지시
- [ ] 주장된 특허 식별 — USPTO.gov(또는 Google Patents) 조회
- [ ] 피소 제품 식별 — 관련 사업부 확인
- [ ] 소장 접수 또는 합리적 소송 예상 시 **소송보존조치(litigation hold) 발동**
- [ ] 답변 기한 확인 — 통상 21일(연장 가능)
- [ ] IPR 청구 기한 평가 — 소장 송달 후 1년, 즉시 기산
- [ ] 경영진 브리핑 — 브리핑 문서화(특권 보전)
- [ ] 외부 대리인 연락 — 사전 선정이 없으면 즉시 선정 절차 개시

→ 상세: [위협 평가](01-pre-litigation/threat-assessment.md) | [소송보존](01-pre-litigation/litigation-hold-evidence-preservation.md)

---

## Foreign Company Considerations

🌏 **한국 및 기타 해외 기업은 미국 특허 소송에서 별도의 도전 과제에 직면합니다.** 해외 피고에게 고유한 핵심 이슈는 다음과 같습니다.

### 재판지 노출(Venue Exposure)
미국 내 기업은 *TC Heartland* (2017)의 보호를 받지만, **해외 법인은 28 U.S.C. § 1391(c)(3) 및 *In re HTC Corp.* (Fed. Cir. 2018)에 따라 미국 어느 연방지방법원에서도 피소될 수 있습니다.** 원고(NPE)는 이를 이용해 원고 친화적 관할(특히 E.D. Texas, W.D. Texas)에 제소합니다. 2025년 기준 해외 모회사를 겨냥한 유사 사건이 E.D. Texas에서 단일 연도에 40건 이상 제기되었습니다.
→ 참조: [재판지 및 관할](02-case-initiation/venue-and-jurisdiction.md)

### 증거개시 비대칭(Discovery Asymmetry)
한국 기업은 미국식 광범위 사전 증거개시에 익숙하지 않은 경우가 많습니다. 미국 Rule 26 증거개시는 잠재적으로 관련된 모든 자료(이메일, 메신저(KakaoTalk), 소스코드, 재무자료)를 보존·제출하도록 요구합니다. 불이행 시 불리한 배심 지시(adverse inference) 등 중대한 제재 위험이 있습니다.
→ 참조: [소송보존](01-pre-litigation/litigation-hold-evidence-preservation.md) | [증거개시 전략](05-discovery/discovery-strategy.md)

### ITC Section 337 노출
미국으로 제품을 수입하는 해외 기업은 ITC 조사 대상이 될 수 있으며, 10~12개월 내 재판으로 진행되어 수입금지로 이어질 수 있습니다. 한국 기업은 ITC에서 자주 **피소(target)** 될 뿐 아니라 **공격적 수단(user)** 으로도 활용합니다(예: Samsung Display v. BOE, 2024–2025).
→ 참조: [ITC Section 337 방어 플레이북](02-case-initiation/itc-section-337-defense-playbook.md) | [초기 사건 평가](02-case-initiation/initial-case-assessment.md)

### NPE 타깃팅
한국 기술기업(특히 삼성, LG, SK 계열)은 미국 NPE에게 **가장 자주 표적화되는 피고군**입니다. 삼성은 평균 약 5일마다 신규 NPE 특허 소송에 직면합니다. 한국 대기업의 집중된 제품 포트폴리오와 높은 지불능력은 이들을 비례 이상으로 매력적인 타깃으로 만듭니다.

---

## 핵심 법령 및 규칙 참조 (Key Statute & Rule References)

| 인용(Citation) | 주제(Subject) |
|---|---|
| 35 U.S.C. § 101 | 특허적격성(Patent-eligible subject matter) |
| 35 U.S.C. § 102 | 신규성 / 선행성(Novelty / Anticipation) |
| 35 U.S.C. § 103 | 비자명성(Obviousness) |
| 35 U.S.C. § 112 | 기재요건 / 실시가능요건 / 명확성 |
| 35 U.S.C. § 271 | 침해(Infringement) |
| 35 U.S.C. § 284 | 손해배상(Damages) |
| 35 U.S.C. § 285 | 변호사비(예외적 사건) |
| 35 U.S.C. § 311–319 | 당사자계 재심(IPR) |
| 35 U.S.C. § 315(b) | IPR 1년 제한(one-year bar) |
| 35 U.S.C. § 315(e) | IPR 금반언(estoppel) |
| 28 U.S.C. § 1400(b) | 특허 재판지(국내 피고) |
| 28 U.S.C. § 1391(c)(3) | 일반 재판지(해외 피고 — 전 지역 가능) |
| Fed. R. Civ. P. 26 | 증거개시 범위와 한계 |
| Fed. R. Evid. 502(d) | 클로백 명령 / 특권 포기 방지 |

---

## 유지보수 및 업데이트 (Maintenance & Updates)

본 가이드라인은 IP Legal 팀이 관리합니다. 주요 미국 특허법 변화(특히 Federal Circuit 또는 연방대법원 판결)는 관련 섹션 업데이트를 촉발해야 합니다. 이 버전(2026년 4월 기준)에 반영된 최근 동향:

- *In re HTC Corp.* (Fed. Cir. 2018) — 해외 피고 재판지(전 지역 가능)
- *Halo Electronics v. Pulse* (SCOTUS 2016; Fed. Cir. 2025년 2월 환송심) — 고의침해 기준
- *Ingenico Inc. v. IOENGINE, LLC* (Fed. Cir. 2025년 5월) — IPR 금반언 범위
- *Recentive Analytics v. Fox Corp.* (Fed. Cir. 2025년 4월) — AI/ML § 101 무효
- *EcoFactor v. Google* (Fed. Cir. 전원합의체 2025) — 비교가능 라이선스 안분
- *Rex Medical v. Intuitive Surgical* (Fed. Cir. 2025년 9월) — 손해배상 안분 의무화
- PTAB FY2025 통계 — 개시율 50%로 하락; FWD에서 약 80% 청구항 무효화

---
이전 문서: 없음
다음 문서: [미국 특허 소송: 생애주기 개요](00-overview/litigation-lifecycle-overview.md)
