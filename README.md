# lazynote

한국어 집필을 위한 Claude Code 플러그인 스킬셋. 서로 다른 네 가지 글쓰기 장르를 독립 스킬로 묶는다.

## 어떤 스킬을 써야 하나

| 이런 글을 쓰고 싶다면 | 스킬 | 예시 요청 |
| --- | --- | --- |
| 1차 출처로 검증한 기업 사례 분석 아티클 (조사→검증→초고→논증점검→윤문→확정본) | `lazynote-case-writing` | "이 기업 사례 조사해줘", "초고 써줘", "발행할 수 있게 정리해줘" |
| 제목·부제·소제목·목차 설계나 진단 | `lazynote-title-outline` | "제목 좀 다듬어줘", "이 책 목차 같이 잡아줘" |
| 기본 저자 본인의 경험을 담은 개인 에세이 | `lazynote-author-writing` | "이 경험으로 에세이 써줘", "이 초안 퇴고해줘" |
| 특정 개인의 페르소나로 쓰는 에세이 | `lazynote-persona-writing` | "이 인터뷰 자료로 그 사람 목소리로 글 써줘" |
| 시리즈·책을 처음 시작해서 방향이 아직 없다 | (위 스킬 어디서든 자동으로) `shared/intake.md` 기획 인터뷰 | "시리즈 어떻게 시작해야 할지 모르겠다", "책 기획 좀 도와줘" |

프로젝트의 목적·독자·용어·전체 목차가 저장소 어디에도 없으면, 위 네 스킬 중 어느 것을 트리거하든 조사·집필 전에 이 인터뷰부터 진행한다.

## 설치

이 저장소는 비공개(private)다. 설치하려는 사람을 먼저 GitHub 저장소의 collaborator로 추가해야 한다 ([Settings → Collaborators](https://github.com/lazynote-mj/lazynote/settings/access)).

터미널에서:

```bash
claude plugin marketplace add https://github.com/lazynote-mj/lazynote
claude plugin install lazynote@lazynote
```

또는 Claude Code 세션 안에서:

```
/plugin marketplace add https://github.com/lazynote-mj/lazynote
/plugin install lazynote@lazynote
```

로컬 경로로 직접 쓰는 경우(저장소를 clone해 둔 경우)는 그 경로를 대신 넣는다:

```bash
claude plugin marketplace add /path/to/lazynote
```

설치 직후엔 이미 켜져 있던 세션에서 스킬이 안 보일 수 있다 — `/reload-plugins`로 반영하거나 새 세션을 연다.

설치되면 각 스킬은 `/lazynote:lazynote-case-writing`처럼 호출하거나, 스킬 설명에 맞는 요청(예: "사례 찾아줘", "제목 좀 다듬어줘", "이 에세이 퇴고해줘")으로 자동 트리거된다.
