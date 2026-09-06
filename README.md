# lazynote

한국어 집필을 위한 Claude Code 플러그인 스킬셋. 서로 다른 네 가지 글쓰기 장르를 독립 스킬로 묶는다.

## 포함된 스킬

- `lazynote-case-writing` — 1차 출처로 검증한 기업 사례를 근거로 쓰는 분석 아티클 파이프라인 (조사→검증→초고→논증점검→윤문→확정본)
- `lazynote-title-outline` — 제목·부제·소제목·목차 설계와 진단
- `lazynote-author-writing` — 기본 저자 본인의 경험을 담은 개인 에세이
- `lazynote-persona-writing` — 특정 개인의 페르소나로 쓰는 에세이

네 스킬은 시리즈·책을 처음 시작할 때 쓰는 기획 인터뷰(`shared/intake.md`)를 공유한다. 프로젝트의 목적·독자·용어·전체 목차가 비어 있으면 이 인터뷰부터 진행한다.

## 설치

터미널에서:

```bash
claude plugin marketplace add /path/to/lazynote
claude plugin install lazynote@lazynote
```

또는 Claude Code 세션 안에서:

```
/plugin marketplace add /path/to/lazynote
/plugin install lazynote@lazynote
```

설치되면 각 스킬은 `/lazynote:lazynote-case-writing`처럼 호출하거나, 스킬 설명에 맞는 요청(예: "사례 찾아줘", "제목 좀 다듬어줘", "이 에세이 퇴고해줘")으로 자동 트리거된다.
