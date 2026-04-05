# 미국 특허 소송 방어 지침

> **면책 고지:** 이 지침은 내부 정보 제공 목적으로만 작성되었으며 법적 조언을 구성하지 않습니다. 특허 소송은 사안별·관할별로 크게 다릅니다. 중요한 법적 결정을 내리기 전에 반드시 자격을 갖춘 미국 특허 소송 전문 변호사를 선임하십시오.

---

## 목적 및 범위

이 저장소는 미국 특허 침해 주장에 대응하는 **기업 법무 및 IP 팀**을 위한 실무적·운영적 지침을 제공합니다. 이 콘텐츠는 주로 다음 대상자를 위해 설계되었습니다:

- **사내 IP 법무** — 특허 소송 포트폴리오를 관리하는 담당자
- **IP 매니저** — 사업부와 외부 법률 자문 사이를 조율하는 담당자
- **기업 법무 제너럴리스트** — 전문 분야 외의 특허 분쟁을 접하게 된 담당자
- **사업부 리더** — 자사 제품이 침해 혐의를 받고 있는 담당자

이 지침의 초점은 **방어**에 있습니다. 대형 기술·전자·제조 기업들은 특히 NPE(비실시 주체/특허 트롤)로부터 특허 소송의 빈번한 표적이 됩니다. 이 지침은 첫 번째 요구 서한(demand letter)부터 재판, 항소, 선제적 포트폴리오 관리에 이르기까지 특허 방어의 전체 생애주기를 다룹니다.

> **한국 및 외국 기업을 위한 안내:** 이 저장소 전반에 걸쳐 🌏 표시가 된 섹션은 미국에서 특허 소송을 방어하는 비미국(특히 한국) 기업들을 위한 구체적인 고려 사항을 강조합니다. 외국 기업들은 관할 노출, 증거개시(discovery) 관련 도전과제, 그리고 특별한 주의를 요하는 절차적 위험에 직면합니다. 아래 [외국 기업 고려 사항](#외국-기업-고려-사항) 섹션을 참조하십시오.

---

## 이 저장소 탐색 방법

| 단계 | 문서 | 주요 주제 |
|---|---|---|
| **개요** | [소송 생애주기 개요](00-overview/litigation-lifecycle-overview.md) | 전체 생애주기, 역할, 비용 예상 |
| **소송 전** | [위협 평가](01-pre-litigation/threat-assessment.md) | 요구 서한, 분류, DJ 전략 |
| | [소송 보전 조치 및 증거 보존](01-pre-litigation/litigation-hold-evidence-preservation.md) | 보전 고지, ESI, 증거 훼손 위험 |
| **사건 개시** | [초기 사건 평가](02-case-initiation/initial-case-assessment.md) | 최초 2주, 무효·비침해 분석 |
| | [관할 및 재판 지역](02-case-initiation/venue-and-jurisdiction.md) | TC Heartland, 외국 피고 규칙, 이송 |
| | [초기 사건 전략](02-case-initiation/early-case-strategy.md) | 방어 이론, § 101 신청, 고의성 |
| **특허 등록 후 절차** | [IPR/PGR 개요](03-post-grant-proceedings/ipr-pgr-overview.md) | 절차 메커니즘, 금반언, 비교 표 |
| | [IPR/PGR 전략 및 타이밍](03-post-grant-proceedings/ipr-pgr-strategy-and-timing.md) | 의사결정 트리, 청원서, 정지 신청 |
| | [직권 재심사](03-post-grant-proceedings/ex-parte-reexamination.md) | IPR 대비 사용 시기 |
| **청구항 해석** | [청구항 해석 전략](04-claim-construction/claim-construction-strategy.md) | Markman 준비, 용어 선정, 출원 경과 |
| **증거개시** | [증거개시 전략](05-discovery/discovery-strategy.md) | 문서 제출, 질문서, 증언록 취득 |
| | [특권 및 업무 산출물 보호](05-discovery/privilege-and-work-product-protection.md) | 사내 특권, 법적 의견서, FRE 502(d) |
| **전문가 증인** | [전문가 증인 관리](06-expert-witnesses/expert-witness-management.md) | 선발, Daubert, 증언 준비 |
| **손해배상 방어** | [손해배상 방어 전략](07-damages-defense/damages-defense-strategy.md) | Georgia-Pacific, 배분, 고의성 |
| **합의** | [합의 및 라이선스 전략](08-settlement-and-licensing/settlement-and-licensing-strategy.md) | 의사결정 매트릭스, 협상, 라이선스 조건 |
| **재판** | [재판 준비 가이드](09-trial-preparation/trial-preparation-guide.md) | 약식판결 신청, MIL, 배심원 선발, eBay |
| **항소** | [항소 가이드](10-appeals/appeals-guide.md) | 연방 순회법원, 심사 기준 |
| **포트폴리오 관리** | [자유 실시 분석](11-portfolio-management/freedom-to-operate.md) | FTO 방법론, 제품 출시 관문 |
| | [설계 변경 및 방어적 포트폴리오](11-portfolio-management/design-arounds-and-defensive-portfolio.md) | 설계 변경, 방어 특허, LOT/OIN |
| **참고 자료** | [주요 기한 참조표](appendices/key-deadlines-reference.md) | 모든 중요 소송 기한 |
| | [용어 해설집](appendices/glossary.md) | 50개 이상의 주요 용어 정의 |
| | [공급업체 및 리소스 가이드](appendices/vendor-and-resource-guide.md) | 도구, 데이터베이스, 서비스 제공업체 |

---

## 빠른 참조: 최초 72시간 체크리스트

요구 서한 또는 소장이 도착하면 시간이 매우 중요합니다. 즉시 이 체크리스트를 사용하십시오:

- [ ] **법무 검토 없이 요구 서한에 절대 응답하지 마십시오**
- [ ] **모든 통신 내용을 보존하십시오** — 즉시 IP/법무팀에 전달하고 직원들에게 삭제 금지를 지시하십시오
- [ ] **주장된 특허를 확인하십시오** — USPTO.gov(Google Patents)에서 조회하십시오
- [ ] **침해 혐의 제품을 확인하십시오** — 관련 사업부를 파악하십시오
- [ ] **소장이 제출되었거나 소송이 합리적으로 예상된다면 소송 보전 조치를 발동하십시오**
- [ ] **응답 기한을 확인하십시오** — 소장에 대한 답변 기한은 21일 (연장 가능)
- [ ] **IPR 청원 기한을 확인하십시오** — 소장 송달일로부터 1년; 즉시 기산 시작
- [ ] **경영진에게 보고하십시오** — 보고 내용을 문서화하십시오 (특권 보존)
- [ ] **외부 법률 자문에 연락하십시오** — 사전에 선정되지 않은 경우 즉시 선정 절차를 시작하십시오

→ 상세 내용: [위협 평가](01-pre-litigation/threat-assessment.md) | [소송 보전 조치](01-pre-litigation/litigation-hold-evidence-preservation.md)

---

## 외국 기업 고려 사항

🌏 **한국 및 기타 외국 기업은 미국 특허 소송에서 고유한 도전과제에 직면합니다.** 외국 피고에게 특유한 주요 문제점:

### 관할 노출

*TC Heartland v. Kraft Foods* (SCOTUS 2017) 판례로 관할 보호를 받는 미국 내국법인과 달리, **외국 법인은 *In re HTC Corp.* (Fed. Cir. 2018)에 따라 28 U.S.C. § 1391(c)(3) 기준이 적용되어 미국의 사실상 모든 연방 지방법원에서 제소될 수 있습니다.** NPE 원고들은 외국 기업이 해당 지역에 실질 사업장이 없더라도 원고 친화적 재판지(특히 텍사스 동부/서부 지방법원)를 선택해 이를 적극 활용합니다. 2025년에도 외국 모회사를 겨냥한 사건이 집중 제기되었습니다.
→ 참조: [관할 및 재판 지역](02-case-initiation/venue-and-jurisdiction.md)

### 증거개시 비대칭

한국 기업들은 **미국식 광범위한 재판 전 증거개시(pretrial discovery)가 없는** 한국 소송 관행에 익숙합니다. 미국의 연방민사소송규칙(FRCP) Rule 26에 따른 증거개시는 이메일, 메신저 앱(카카오톡 포함), 소스 코드, 재무 기록 등 잠재적으로 관련 있는 모든 문서의 보존 및 제출을 요구합니다. 이를 준수하지 않을 경우 불리한 추론 배심원 지시(adverse inference jury instructions)를 포함한 엄중한 제재를 받을 수 있습니다.
→ 참조: [소송 보전 조치](01-pre-litigation/litigation-hold-evidence-preservation.md) | [증거개시 전략](05-discovery/discovery-strategy.md)

### ITC 337조 노출

미국으로 제품을 수입하는 외국 기업들은 ITC 조사에 직면할 수 있으며, ITC 절차는 10~12개월 내에 심리가 완료되고 수입 금지 조치가 내려질 수 있습니다. 한국 기업들은 빈번한 **표적**(특히 미국 경쟁사로부터)인 동시에 ITC를 공세적 수단으로 **활용**하기도 합니다(예: Samsung Display v. BOE, 2024~2025).
→ 참조: [초기 사건 평가](02-case-initiation/initial-case-assessment.md)

### NPE 표적화

삼성, LG, SK 그룹 계열사 등 한국 기술 기업들은 미국 NPE들이 **가장 많이 표적으로 삼는 피고** 중 하나입니다. 삼성은 약 5일마다 새로운 NPE 특허 소송에 직면합니다. 한국 대기업들의 집중된 제품 포트폴리오와 풍부한 자금력은 이들을 불균형적인 표적으로 만듭니다.

---

## 주요 법령 및 규정 참조

| 인용 | 주제 |
|---|---|
| 35 U.S.C. § 101 | 특허 적격 대상 |
| 35 U.S.C. § 102 | 신규성 / 선행 기술에 의한 무효 |
| 35 U.S.C. § 103 | 자명성 |
| 35 U.S.C. § 112 | 발명의 상세한 설명 / 실시 가능성 / 명확성 |
| 35 U.S.C. § 271 | 침해 |
| 35 U.S.C. § 284 | 손해배상 |
| 35 U.S.C. § 285 | 변호사 비용 (예외적 사건) |
| 35 U.S.C. § 311–319 | 당사자계 재심사(Inter Partes Review) |
| 35 U.S.C. § 315(b) | IPR 1년 제척기간 |
| 35 U.S.C. § 315(e) | IPR 금반언 |
| 28 U.S.C. § 1400(b) | 특허 소송 관할 (국내 피고) |
| 28 U.S.C. § 1391(c)(3) | 일반 관할 (외국 피고 — 모든 지방법원) |
| Fed. R. Civ. P. 26 | 증거개시 범위 및 제한 |
| Fed. R. Evid. 502(d) | 반환 명령 / 특권 포기 보호 |

---

## 유지보수 및 업데이트

이 지침은 IP 법무팀이 관리합니다. 중요한 미국 특허법 발전 — 특히 주요 연방 순회법원 또는 대법원 판결 — 은 영향을 받는 섹션의 검토를 촉발해야 합니다. 이 버전에 반영된 주요 최근 동향 (2026년 4월 기준):

- *In re HTC Corp.* (Fed. Cir. 2018) — 외국 피고 관할 (모든 지방법원 규칙)
- *Halo Electronics v. Pulse* (SCOTUS 2016; Fed. Cir. Feb. 2025 remand) — 고의 침해 기준
- *Ingenico Inc. v. IOENGINE, LLC* (Fed. Cir. May 2025) — IPR 금반언 범위 (제품 선행 기술은 금반언 미적용)
- *Recentive Analytics v. Fox Corp.* (Fed. Cir. April 2025) — AI/ML § 101 무효
- *EcoFactor v. Google* (Fed. Cir. en banc 2025) — 비교 라이선스 배분
- *Rex Medical v. Intuitive Surgical* (Fed. Cir. Sept. 2025) — 손해배상 배분 필수화
- PTAB FY2025 통계 — 심판 개시율 50%로 하락; 최종 판결에서 약 80% 청구항 무효화
