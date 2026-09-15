---
name: ask-lazynote
description: 어느 lazynote 스킬로 시작해야 할지 안내하는 라우터. 저자의 준비 상태에 따라 갈 곳을 알려준다.
disable-model-invocation: true
---

# Ask Lazynote

여섯 개 스킬 중 뭘 써야 할지 모르겠으면 여기서 고른다. 자동으로 트리거되지 않으니 `/lazynote:ask-lazynote`로 직접 부른다.

## 먼저 확인 — 이미 있는 원고나 이미지를 다루는가

**이미 쓴 글을 교정·윤문만 하고 싶다** → `lazynote-korean-editing`. 시리즈 기획과 무관하게 바로 시작한다.

**이미 있는 원고에 도표나 표지·썸네일 이미지가 필요하다** → `lazynote-article-images`. 마찬가지로 기획 인터뷰 없이 바로 시작한다.

둘 다 아니라면 — 새로 쓰거나 구조를 잡아야 한다면 — 아래에서 자기 상태를 고른다.

## 지금 어디에 있는가

**목차나 개요가 이미 있다** → 그 상태를 존중한다. 바로 쓰고 싶은 스킬로 간다 — 기업 사례면 `lazynote-case-writing`, 개인 에세이면 `lazynote-author-writing`, 다른 사람 목소리면 `lazynote-persona-writing`. 목차 자체를 다시 점검하고 싶으면 `lazynote-title-outline`.

**주제는 설명할 수 있는데 구조가 없다** → 쓰려는 스킬(`lazynote-case-writing`/`lazynote-author-writing`/`lazynote-persona-writing`)을 그대로 부른다. 목적·독자·전체 목차가 비어 있으면 스킬이 알아서 `shared/intake.md` 기획 인터뷰로 넘어간다. 질문마다 추천 답이 붙어서 나오니 승인·수정만 하면 된다.

**아직 뭘 쓰고 싶은지도 명확하지 않다** → 시리즈 전체를 기획하려 들지 않는다. **한 편만 먼저 써 본다.** 원하는 스킬을 그대로 불러서 시작한다 — 처음이라 기획 인터뷰가 뜨더라도 전체 시리즈를 다 정하라는 게 아니다. 완료 조건은 목적·독자, 그리고 이번 편이 답할 질문 정도면 된다(핵심 개념은 0개여도 된다). 나머지는 미정으로 남겨두고 일단 한 편을 써 본다. 시리즈 전체 목차는 두세 편 쌓인 뒤 다시 잡아도 된다.

## 스킬 요약

| 스킬 | 쓰는 때 |
| --- | --- |
| `lazynote-case-writing` | 1차 출처로 검증한 기업 사례 분석 아티클 |
| `lazynote-author-writing` | 기본 저자 본인의 경험을 담은 개인 에세이 |
| `lazynote-persona-writing` | 다른 사람의 목소리로 쓰는 글 |
| `lazynote-title-outline` | **이미 있는** 원고·아이디어의 제목·목차를 설계하거나 점검. 재료 자체가 없으면 위 세 스킬 중 하나로 먼저 간다 |
| `lazynote-korean-editing` | 이미 쓴 아티클·에세이·보고서·이메일·안내문의 맞춤법·교정·윤문 |
| `lazynote-article-images` | 이미 있는 원고에 맞는 도표·차트·표지·썸네일 이미지 |
