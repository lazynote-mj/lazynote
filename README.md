# lazynote

한국어 집필을 위한 Claude Code 플러그인 스킬셋. 글쓰기·제목과 목차·한국어 교정과 윤문·아티클 이미지 제작을 여섯 개의 독립 스킬로 묶는다.

## 어떤 스킬을 써야 하나

| 이런 글을 쓰고 싶다면 | 스킬 | 예시 요청 |
| --- | --- | --- |
| 1차 출처로 검증한 기업 사례 분석 아티클 (조사→검증→초고→논증점검→윤문→확정본) | `lazynote-case-writing` | "이 기업 사례 조사해줘", "초고 써줘", "발행할 수 있게 정리해줘" |
| 제목·부제·소제목·목차 설계나 진단 | `lazynote-title-outline` | "제목 좀 다듬어줘", "이 책 목차 같이 잡아줘" |
| 기본 저자 본인의 경험을 담은 개인 에세이 | `lazynote-author-writing` | "이 경험으로 에세이 써줘", "이 초안 퇴고해줘" |
| 특정 개인의 페르소나로 쓰는 에세이 | `lazynote-persona-writing` | "이 인터뷰 자료로 그 사람 목소리로 글 써줘" |
| 한국어 맞춤법·띄어쓰기·호응 교정과 자연스러운 윤문 | `lazynote-korean-editing` | "맞춤법만 고쳐줘", "말투는 살리고 자연스럽게 다듬어줘" |
| 아티클의 논지를 설명하는 도표 또는 표지·썸네일 이미지 | `lazynote-article-images` | "이 글에 맞는 이미지 만들어줘", "이 도표를 최신 원고에 맞춰줘" |
| 시리즈·책을 처음 시작해서 방향이 아직 없다 | (네 글쓰기 스킬에서 새 기획 시) `shared/intake.md` 기획 인터뷰 | "시리즈 어떻게 시작해야 할지 모르겠다", "책 기획 좀 도와줘" |

새 시리즈·책을 기획하며 목적·독자·용어·전체 목차가 저장소에 없으면 네 글쓰기 스킬에서 기획 인터뷰부터 진행한다. 이미 있는 원고의 한국어 교정·윤문에는 이 인터뷰가 필요하지 않다.

## 설치

이 저장소는 공개(public)다. 누구나 링크만으로 설치할 수 있다.

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

## 이미지 제작

`lazynote-article-images`는 원고와 삽입 위치를 읽고 도표·차트와 표지·썸네일의 제작 경로를 고른다. 도표는 직접 제작한 원본과 업로드용 이미지를 관리하고, AI 일러스트는 현재 환경에 연결된 이미지 생성 도구를 사용한다. 플러그인 자체에 이미지 생성 서비스나 API 키는 포함되지 않는다. 생성 도구가 없으면 프롬프트와 제작 사양을 제공한다.

## 한국어 교정·윤문

`lazynote-korean-editing`은 장르에 공통으로 쓰는 교정·윤문 기준이다. 기존 글쓰기 스킬에서 이 기준을 참조하고, `lazynote-case-writing/references/voice.md`는 분석 아티클의 문체 기준을 추가한다. 맞춤법만 요청하면 표현과 구조는 유지하며, 윤문에서도 사실·조건·유보의 강도와 필자의 말투를 보존한다. 외부 맞춤법 검사기 없이도 사용할 수 있다.
