# 디스커버리 전략(Discovery Strategy)

> **빠른 참조(Quick Reference):** 디스커버리는 비용·리스크의 중심입니다. 범위 통제(scope control), 우선순위 수집(prioritized collection), 조기 쟁점화(early issue framing)가 방어 성패를 좌우합니다.

---

## 1. 디스커버리 목표 설정

피고 관점 목표는 세 가지입니다.
1. 원고 입증의 약점 드러내기(침해/손해/인과)
2. 피고 방어자료를 효율적으로 구축(비침해/무효/안분)
3. 비용 폭증을 막는 절차적 통제 확보

---

## 2. 초기 Rule 26(f) 협의 전략

협의에서 반드시 잡아야 할 항목:
- ESI 프로토콜(파일형식, metadata, dedup)
- 검색어(search terms) + TAR(Technology Assisted Review) 활용 여부
- 소스코드 열람 규칙(source code protocol)
- 생산 일정(staged production)

**원칙:** “모든 자료 일괄 제출”이 아니라 “쟁점 기반 단계적 제출(staged discovery)”을 제안합니다.

---

## 3. 수집·검토 워크플로우

### A. 수집(Collection)
- 핵심 custodian 우선 수집
- 중요 시스템(이메일/메신저/코드/매출DB) 선제 확보

### B. 처리(Processing)
- 중복 제거(deduplication)
- 언어 분류(한/영)
- 특권 후보(legal comms) 태깅

### C. 검토(Review)
- 쟁점별 태그세트(침해/무효/손해/의도)
- hot docs 큐 운영
- 생산 전 QC(기밀/개인정보/특권)

---

## 4. 소스코드 디스커버리(Source Code Discovery)

소스코드는 고위험 영역이므로 별도 프로토콜이 필요합니다.
- 접근 장소 제한(secure review room)
- 출력 제한(page cap, 승인절차)
- 검색 로그/접근 로그 보존
- 전문가 열람 권한 최소화(need-to-know)

---

## 5. 제3자 디스커버리(Third-Party Discovery)

대상:
- 부품 공급사(suppliers)
- 표준화 단체/시험기관
- 라이선스 협상 상대방

제3자 소환장(subpoena)은 범위를 좁게 설계해 회수율을 높이고, 과도한 부담 주장을 선제 차단합니다.

---

## 6. 비용 통제(Budget Control)

| 비용 드라이버 | 통제 방법 |
|---|---|
| 광범위 custodian | 우선순위 기반 1차/2차 분할 |
| 과도한 검색어 | 샘플링 기반 정제 |
| 번역량 폭증 | relevance 기준 선별 번역 |
| 무분별 출력 | code printing 규칙 강화 |

---

## 7. 한국기업 특화 포인트(🌏)

- KakaoTalk/내부 메신저 수집 정책을 미국 discovery 표준에 맞춰 문서화
- 한국 본사 서버 데이터의 국외이전 통제 절차와 미국 생산일정 정합화
- 한영 혼합 문서 검토를 위한 이중언어 리뷰팀 구성

---

## 8. 마일스톤 운영

- M1: 30일 내 핵심 문서 1차 생산
- M2: Markman 전 기술쟁점 관련 생산 완료
- M3: 전문가 보고서 전 손해자료 생산 완료

마일스톤 지연은 제재(sanctions)보다도 협상력 손실이 큽니다.

---

## 9. 체크리스트

- [ ] ESI 프로토콜 합의
- [ ] custodian 인터뷰 완료
- [ ] search term hit-rate 검증
- [ ] privilege 1차 태깅 완료
- [ ] production QC 로그 보관

---

## 10. 2차 보완: 검색어(Search Terms) 튜닝 프로토콜

1) seed term 세트 구성(제품명/코드명/특허번호/핵심기능)
2) hit-rate 샘플링(과다/과소 탐지)
3) precision-recall 균형 재조정
4) 법원/상대방 협의 로그 보존

| 문제 | 징후 | 조치 |
|---|---|---|
| 과다포집(over-collection) | 무관문서 비율 급증 | exclusion term 추가 |
| 과소포집(under-collection) | 핵심 custodian 문서 누락 | synonym/코드명 확장 |
| 언어편향 | 한국어 문서 누락 | 한글 키워드 병행 입력 |

## 11. 2차 보완: TAR/AI 리뷰 통제

- 학습셋(training set) 출처 문서화
- 모델 업데이트 주기 관리
- human-in-the-loop QC 유지
- 상대방 이의 대비 설명가능성(explainability) 확보

## 12. 2차 보완: 생산(Production) 품질 체크

- Bates 번호 연속성
- 메타데이터 필드 누락 여부
- redaction 레이어 검증
- privilege clawback 시나리오 점검

디스커버리에서 “정확성 + 재현성”이 확보되어야 재판 단계에서 증거 신뢰도를 유지할 수 있습니다.
