# 상대경로 링크 수동 점검 체크리스트

점검일: 2026-04-05 (UTC)
점검 범위: `ko/` 내 문서 네비게이션 링크

## 체크 항목

- [x] 각 문서 상단에 `[상위 목차(ko/README.md)]` 링크가 존재한다.
- [x] 각 문서 하단에 `이전 문서` / `다음 문서` 링크가 존재한다.
- [x] 링크 텍스트가 한국어로 통일되어 있다.
- [x] `README.md` 포함 전체 23개 `.md` 파일에 동일 포맷이 적용되었다.
- [x] 폴더 순서(00-overview → … → appendices)에 맞게 이전/다음 연결이 구성되었다.
- [x] 상대경로 링크를 열었을 때 파일이 실제로 존재한다.
- [x] 첫 문서의 `이전 문서`는 `없음`, 마지막 문서의 `다음 문서`는 `없음`으로 표기되었다.

## 점검 방법(수동/보조)

1. 문서 상단에서 `상위 목차` 링크 클릭 시 `ko/README.md`로 이동되는지 확인.
2. 문서 하단의 `이전 문서` 링크 클릭 시 직전 순서 문서로 이동되는지 확인.
3. 문서 하단의 `다음 문서` 링크 클릭 시 다음 순서 문서로 이동되는지 확인.
4. 아래 보조 검증 스크립트로 깨진 상대경로 링크가 없는지 확인:

```bash
python - <<'PY'
from pathlib import Path
import re
root=Path('.')
files=sorted(Path('ko').rglob('*.md'))
broken=[]
for f in files:
    text=f.read_text(encoding='utf-8')
    for m in re.finditer(r'\[[^\]]+\]\(([^)]+)\)',text):
        link=m.group(1).split('#')[0].strip()
        if not link or link.startswith('http') or link.startswith('mailto:'):
            continue
        if not (f.parent / link).resolve().exists():
            broken.append((str(f), link))
print('BROKEN' if broken else 'OK', broken)
PY
```
