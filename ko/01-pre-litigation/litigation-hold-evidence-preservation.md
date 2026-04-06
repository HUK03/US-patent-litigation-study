# 소송보존조치(Litigation Hold) 및 증거 보전(Evidence Preservation)

> **빠른 참조(Quick Reference):** 소송보존조치(litigation hold)는 소장 수령 즉시 또는 소송이 "합리적으로 예상(reasonably anticipated)" 되는 즉시 **바로** 발령되어야 합니다. 관련 문서를 보존하지 못하면, 삭제가 일상적·비의도적이었더라도 배심원 불리추정 지시(adverse jury instruction)를 포함한 중대한 제재를 받을 수 있습니다.

---

## 1. 보존의무는 언제 발생하는가?

증거 보존의무(duty to preserve)는 소송이 **합리적으로 예상되는 시점**에 발생합니다. 이는 대부분 기업이 생각하는 시점보다 **더 이릅니다**.

| 유발 사건(Triggering Event) | 보존의무 발생 여부 |
|---|---|
| 소장 송달(Complaint served) | **예 — 즉시** |
| 특정 특허 침해를 주장하는 경고장 수령 | **예 — 즉시** (소송 합리적 예상) |
| 회사의 DJ(확인판결) 제기 내부 결정 | **예 — 즉시** |
| "침해 가능성"을 시사하는 비공식 서신 | 대체로 예 — 변호사와 평가 |
| 업계 일반 라이선스 캠페인 서한 | 변호사와 평가; 회사가 지목되면 대개 예 |
| 경쟁사가 자사 특허를 주장할 수 있다는 내부 인지 | 가능성 있음 — 변호사와 분석 문서화 |

**원칙(Rule):** 의심되면 보존조치를 발령하십시오. 과보존(over-preserving) 비용은 과소보존(under-preserving) 제재 비용보다 훨씬 낮습니다.

---

## 2. 보존 실패의 결과: 증거훼손(Spoliation)

**증거훼손(spoliation)** 은 보존의무가 존재할 때 증거를 파기·변조·미보존하는 것을 의미합니다. 연방민사소송규칙 Fed. R. Civ. P. 37(e)상 결과:

| 심각도(Severity) | 행위(Conduct) | 가능한 제재(Available Sanctions) |
|---|---|---|
| **심각(Severe)** | 소송에서 사용을 막기 위한 고의 파기 | 불리추정 배심 지시(adverse inference instruction); 사건종결적 제재(case-dispositive sanctions); 궐석판결(default judgment) |
| **중대(Significant)** | 상대방에 불이익을 초래한 과실 파기 | 상대방 증거개시 비용 부담 명령; 증거배제(preclusion); 불리지시 |
| **중간(Moderate)** | 보존의무 위반에 해당하는 일상 삭제 | 금전제재; 증거개시 연장; 시정조치(curative measures) |

특허 사건에서 불리추정 지시 한 번이면 배심 앞 신뢰가 사실상 붕괴됩니다. **고프로파일 사건에서 대형 기술기업에 대한 spoliation 제재가 반복적으로 인정되었습니다.**

---

## 3. 소송보존 통지(Litigation Hold Notice): 반드시 포함할 항목

### 누가 소송보존 통지를 받아야 하는가?

**주요 보관책임자(Primary Custodians)** (항상 포함):
- 피소 제품/기술 담당 엔지니어 및 제품매니저
- 피소 기능 담당 기술리드 및 아키텍트
- 피소 제품 매출자료를 관리하는 재무/회계 담당
- 해당 특허 또는 관련 선행기술을 검토한 IP/특허팀
- 라이선스 협의에 관여한 사업개발 담당
- 해당 특허 관련하여 상대방과 직접 접촉한 임직원

**IT 및 기록관리:**
- IT 부서(정기삭제/자동삭제 정책 중단)
- 기록관리/리걸옵스 팀
- 클라우드 스토리지 관리자

**기타 인력(필요 시):**
- 피소 제품 관련 커뮤니케이션이 있을 수 있는 영업팀
- 피소 기술/특허 관련 경영진 커뮤니케이션 담당
- 관련 데이터를 보유한 외부 벤더/계약업체

### 어떤 문서 범주를 보존해야 하는가?

**기술 문서(가장 중요):**
- [ ] 피소 제품/기능의 설계명세, 아키텍처 문서, 기술 백서
- [ ] 소스코드 버전 이력(특허 우선일 이전부터 모든 버전)
- [ ] 소프트웨어 빌드 기록, 변경로그, 커밋 이력(Git/SVN logs)
- [ ] CAD 파일, 회로도(schematics), 하드웨어 사양
- [ ] 제품 로드맵 및 기능 기획 문서
- [ ] 피소 기능 관련 시험계획, 테스트 결과, 버그리포트
- [ ] 제조공정 문서(공정특허의 경우)

**커뮤니케이션:**
- [ ] 이메일(업무용 전체 계정 — 업무에 사용된 개인계정 포함)
- [ ] 메신저: Slack, Microsoft Teams, KakaoTalk(업무), WeChat 등
- [ ] 피소 기술 관련 문자메시지
- [ ] 피소 제품/기능을 논의한 회의록 및 발표자료
- [ ] 특허 또는 잠재 침해 이슈 관련 내부 메모

**사업·재무 기록:**
- [ ] 피소 제품의 매출/판매/가격 데이터(최근 6년+)
- [ ] 피소 제품 원가·회계 기록
- [ ] 피소 제품 마케팅 자료 및 제품 소개물

**선행기술 및 IP 기록:**
- [ ] 특허 우선일 이전 회사 공개물/논문/발표자료
- [ ] 해당 기술 관련 내부 식별 선행기술
- [ ] 동일 기술영역의 자사 특허출원
- [ ] 관련 선행기술 검색 결과 또는 FTO 분석

**제3자 및 계약 문서:**
- [ ] 주장 특허 관련 과거 라이선스 협상/계약
- [ ] 피소 구성요소 관련 공급업체/벤더 계약
- [ ] 기술영역 표준단체 제출자료(SEP 관련 시)

---

## 4. IT 연계 체크리스트

IT는 소송보존 지시 수령 후 **48시간 내** 다음 조치를 해야 합니다.

**이메일 시스템:**
- [ ] 대상 보관책임자에 대한 자동삭제/보관삭제/보존정책 중단
- [ ] 식별된 보관책임자 계정에 legal hold 설정(Exchange/Google Workspace/Office 365)
- [ ] [제품 출시일/특허 우선일]부터 현재까지 이메일 보존
- [ ] hold 구현 일시와 방법 문서화

**협업·메신저 플랫폼:**
- [ ] Slack, Microsoft Teams 또는 동등 시스템의 삭제 중단
- [ ] 피소 제품/기능 관련 채널 및 DM 전체 보존
- [ ] 🌏 **KakaoTalk Business / Kakao Work:** 한국 임직원 업무 메신저 캡처 보장; 업무기기의 개인 KakaoTalk도 hold 대상이 될 수 있음
- [ ] 관련 회의 영상/음성 기록(Zoom, Teams recordings) 보존

**코드 저장소(Code Repositories):**
- [ ] 관련 저장소의 purge/cleanup 스크립트 중단
- [ ] 모든 브랜치/태그/커밋 이력 및 메타데이터 보존
- [ ] 저장소를 소송 아카이브로 백업

**파일 저장소(File Storage):**
- [ ] 관련 공유드라이브(Google Drive, SharePoint, OneDrive, NAS) 삭제정책 중단
- [ ] 문서관리시스템(Confluence, SharePoint 등) 전체 보존
- [ ] 제품 데이터가 있는 클라우드 스토리지(AWS S3, Azure Blob 등) 캡처·보존

**백업 및 재해복구(Backup and Disaster Recovery):**
- [ ] 관련 기간의 백업 테이프/이미지 보존
- [ ] hold 해제 전 정기 백업을 덮어쓰지 말 것

**퇴사자(Departing Employees):**
- [ ] 소송 중 퇴사하는 보관책임자(custodian)를 IT가 플래그
- [ ] 계정 비활성화 전 퇴사자 데이터 보존
- [ ] HR로부터 퇴사자 데이터 보존 완료 서면 확인 확보

---

## 5. 🌏 해외기업(한국) 특수 고려사항

한국 기업은 미국식 소송보존을 이행할 때 고유한 과제를 겪습니다.

### 지리적 범위(Geographic Scope)
소송보존은 **전 세계에 적용**됩니다. 포함 대상:
- 한국 본사(서울/수원/인천 운영 포함)
- 한국 자회사 및 계열사
- 피소 제품에 관여한 모든 해외 임직원

한국어 문서(한국어 이메일, KakaoTalk 메시지, 한국어 내부 메모 포함)는 **미국 증거개시 대상**이며 반드시 보존되어야 합니다. 제출 시 번역이 필요할 수 있습니다.

### 한국 개인정보보호법(PIPA)과의 긴장
한국 PIPA는 임직원 개인정보를 보호합니다. 미국 법원은 이러한 긴장을 인지하지만 **PIPA를 미국 문서제출의 전면적 항변으로 일반적으로 인정하지 않습니다.** *Aérospatiale* comity 5요소 분석을 적용하십시오.
1. 미국 소송에서 해당 문서의 중요성
2. 요청의 특정성(specificity)
3. 정보의 미국 기원 여부
4. 대체 수단으로 정보 획득 가능성
5. 미준수가 미국의 중대한 이익을 훼손하는 정도

**실무 접근:** 즉시 hold를 발령해 모든 데이터를 보존하고, 실제 제출요청이 들어오면 외부대리인과 PIPA 관련 제출 범위를 협의하십시오. **보존(preservation)과 제출(production)은 별개 문제**입니다 — 일단 전부 보존하고, 제출 범위는 이후 다투십시오.

### KakaoTalk 및 한국 메신저 앱
미국 법원은 한국 당사자 사건에서 KakaoTalk 메시지 제출을 명한 바 있습니다. 법무팀은 다음을 수행해야 합니다.
- 보관책임자가 사용하는 업무 관련 KakaoTalk 채널 식별
- 한국어 원문(native content) 형태로 보존
- 검토 전까지 채널/메시지 이력 삭제 금지

### 번역 비용 — 지금 예산 반영
대형 특허사건에서 한국어 문서 번역비는 **수백만 달러**에 달한 사례가 있습니다. 초기 예산 편성이 필수입니다.
- 보관책임자 수·기간을 기준으로 한국어 문서량 추정
- USPTO 경험이 있는 기술/법률 번역 벤더 사전 선정
- 한국어 지원 TAR(Technology Assisted Review) 도구 검토

---

## 6. 소송 중 보관책임자(Custodian) 관리

### 초기 보관책임자 인터뷰
소송보존 발령 후 30일 내(가급적 외부대리인 주관) 인터뷰를 실시하여 다음을 확인하십시오.
- hold 통지 수령 및 이해 확인
- 초기 목록에 없던 추가 보관책임자 식별
- 비표준 데이터 소스 확인(업무용 개인기기, 자택 PC, 개인 이메일)
- 이미 삭제된 문서 존재 여부 및 경위 기록

### 지속적 보관책임자 관리
- **재통지(re-notify):** 사건 범위가 확대되면(신규 특허/신규 피소제품 추가) 보관책임자 재통지
- **신규입사자:** 관련 지식/문서 보유 시 hold 대상 추가
- **퇴사자:** 오프보딩 전 데이터 보존, 보존 사실 서면 기록
- **연간 리마인더:** 장기소송의 경우 최소 연 1회 전체 보관책임자에 재안내

### 보관책임자 확인서(Acknowledgment Form)
모든 보관책임자는 hold 수령·이해 확인서에 서명해야 합니다. 다음 로그를 유지하십시오.
- hold 통지 발송일
- 확인서 회수일
- 후속조치/재통지 일자
- 예외사항 및 보고된 문제

---

## 7. 소송보존 해제 프로토콜

보존의무는 합의 또는 판결 선고로 **자동 종료되지 않습니다**. 해제 전에 아래를 확인하십시오.

- [ ] 최종판결 확정 + 항소기간 만료(항소통지 30일)
- [ ] 항소 시: Federal Circuit 판결 및 certiorari 기간 만료
- [ ] 모든 재판 후 모션 해결
- [ ] 동일 특허 관련 사건 전부 종결
- [ ] 주관 소송변호사로부터 해제 서면 승인 획득

**해제 시 조치:**
- IT에 대상 보관책임자 정상 보존/삭제 정책 재개 지시
- 보관책임자에게 hold 해제 사실 서면 통지
- hold 자체 문서(통지서, 보관책임자 목록, 확인서)는 해제 후 최소 3년 보관

---

## 8. 소송보존 통지 템플릿(샘플)

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
