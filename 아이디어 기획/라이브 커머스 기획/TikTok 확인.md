# TikTok에서 앵콜이 되는 것과 안 되는 것 (2026-10-24 14시 확인)

질문: 「쇼츠가 영원히 동작하는 라이브」의 본체(댓글에 바로 답하기, 구매 경로 붙이기)가 미국 TikTok에서 되나.
표지: [공식] = TikTok 공식 문서 원문을 열어 읽음, [제 판단] = 그 사실로 내가 내린 해석, (확인 필요) = 원문을 아직 못 연 것.
방법: TikTok 문서는 화면을 그려야 글이 나와서 헤드리스 Chrome `--dump-dom` 으로 열어 읽었다.

## 1. 한 줄 결론

- **댓글 자동 답은 된다.** 공식 API가 있다. 글(1,200자까지) 또는 그림으로 답한다.
- **영상으로 답하기는 API로 안 된다.** 답글 API는 글과 그림만 받는다.
- **TikTok 안에서는 전화번호, QR, 외부 링크를 못 쓴다.** 영상, 설명, 프로필, 콘텐츠 모두. 구매 경로는 TikTok Shop 상품 링크 하나다.
- **API는 심사를 받아야 쓴다.** 오늘 데모에서는 실제 TikTok 계정 연결 대신 흉내로 보여 준다 [제 판단].

## 2. 확인한 것

| 확인한 것 | 결과 | 근거 |
|---|---|---|
| 댓글에 자동으로 답하기 | **된다.** `/business/comment/reply/create/`(Accounts API v1.3). 「소유한 TikTok 계정의 일반 영상에 달린 댓글에 답글을 단다」. 글 1,200자까지 또는 그림 | [공식] Reply to an existing comment on an owned video. 허용 용도에 「Moderating comments」가 있음(Accounts Overview) |
| 쓰는 조건 | 2026-03-20부터 「Accounts API Access Application Form」을 내고 심사를 받아야 TikTok Accounts 권한을 준다 | [공식] Accounts Overview, Accounts FAQs |
| 스팸 주의 | 「짧은 시간에 거의 같은 내용의 댓글을 많이 달지 말라. 스팸으로 표시되면 숨겨진다」 → AI 답은 매번 다르게 써야 한다 | [공식] 답글 API 문서의 Note |
| 새 댓글을 아는 속도 | 웹훅 `comment.update` 는 댓글이 달리고 「5분 안에」 알린다 → 답은 초 단위가 아니라 몇 분 단위다. 더 빨리 하려면 댓글 목록을 자주 조회해야 하는데 호출 한도는 확인 필요 | [공식] Comment update event |
| 영상으로 답하기 | **API로 안 된다.** 답글은 글 또는 그림만. 영상 올리기 API에도 「이 댓글에 답하는 영상」 칸이 없다 → 대안: 상품 사진과 답을 넣은 그림 카드로 답한다 [제 판단]. 영상 답은 셀러가 앱에서 직접 해야 한다 | [공식] 답글 API 매개변수(text, image_uri, reply_image_url), 영상 올리기 API 매개변수 |
| 영상에 TikTok Shop 상품 링크 붙여 올리기 | Accounts API의 영상 올리기 칸에는 상품 링크 칸이 없다(글, 브랜드 콘텐츠 표시, AI 생성 표시, 댓글·듀엣·스티치 끄기, TTO 캠페인 링크뿐) → 앵콜이 올리면 상품 링크가 안 붙는다. 대안: 초안으로 보내고 셀러가 앱에서 상품 링크를 붙여 올린다(초안 기능에서 상품 링크가 되는지 확인 필요) | [공식] Publish a public video post to an owned account |
| AI 생성 표시 | 영상 올리기 API에 `is_ai_generated` 칸이 있다. 켜면 「Creator labeled as AI-generated」 표시가 붙고, 규정 위반이 없으면 배포에 영향이 없다고 적혀 있다 → 갈래 2(AI 영상)에 그대로 쓴다 | [공식] 같은 문서 |
| 전화번호, QR, 외부 링크 | **금지.** 「Prohibited actions include sharing: Links to other websites… Phone numbers, social media handles, or email addresses / QR codes」. 피해야 할 문장 예에 「If you're interested in buying these products, you can reach out to me at this number.」, 「Scan this QR code to shop our sale!」, 「Click on the link in my bio to shop for more products」가 그대로 있다. 위반하면 콘텐츠 삭제나 경고 | [공식] TikTok Shop US Content Policy, Avoid Redirecting Traffic(2026-06-22, Applies to: United States) |
| DM 자동 답 | 미국 계정은 추가로 미국 데이터 보안 심사(보통 7~10 영업일)를 통과하고 부속 계약을 맺어야 한다. 일반 개인 계정은 안 되고 사업자 계정만. TikTok Shop 구매자 메시지는 이것과 다른 시스템 | [공식] Access to Business Messaging API, US data security review |

## 3. 앵콜에 뜻하는 것 [제 판단]

- 새 정의의 본체인 「댓글에 바로 답하기」는 TikTok에서 된다. 다만 「바로」는 몇 분이다. 덱에 「seconds」라고 쓰지 않는다.
- **TikTok에서의 앵콜 = 댓글 답 + TikTok Shop 상품 링크.** 전화와 QR은 TikTok 밖(인스타, 유튜브, 매장, 포장)에서만 쓴다.
- 댓글 AI 답에도 전화번호, 링크, 「DM 주세요」를 넣으면 안 된다. 답은 「영상의 상품 링크(장바구니)를 눌러 주세요」처럼 TikTok 안에서 끝낸다.
- 지난 제안의 「영상으로 답하기」는 「그림 카드로 답하기」로 바꾼다.
- 쇼츠마다 다른 전화번호나 QR로 「어느 영상이 팔았나」를 재는 방식은 TikTok에서는 못 쓴다. TikTok은 TikTok Shop 주문 데이터로 잰다(셀러 연동 API는 확인 필요).
- 오늘 데모: API 심사 때문에 실제 TikTok 계정에 답을 달 수 없다. 댓글 답은 Claude로 실제로 만들고, 다는 장면은 화면으로 보여 준다. 덱에 「TikTok API 심사 신청 단계」라고 적는다.

## 4. 아직 확인 못 한 것

- Content Posting API 초안으로 보낸 영상에 셀러가 상품 링크를 붙일 수 있나
- TikTok Shop 구매자 메시지 API(Partner API의 고객 응대 쪽): 남의 연동 도구(Zendesk 등)는 된다고 하나 원문을 못 열었다
- 댓글 목록 조회의 호출 한도(몇 분보다 빨리 답할 수 있나)
- 셀러가 TikTok Shop을 안 쓰는 일반 계정일 때의 링크 규정

## 출처

- 답글 API: https://business-api.tiktok.com/portal/docs/reply-to-an-existing-comment-on-an-owned-video/v1.3
- 댓글 관리 안내: https://business-api.tiktok.com/portal/docs/manage-comments-on-owned-tiktok-videos/v1.3
- 댓글 웹훅: https://business-api.tiktok.com/portal/docs/comment-update-event/v1.3
- Accounts API 개요(허용 용도, 2026-03-20 신청서): https://business-api.tiktok.com/portal/docs/accounts-api-overview/v1.3
- Accounts API FAQ: https://business-api.tiktok.com/portal/docs/accounts-api-faqs/v1.3
- 영상 올리기 API: https://business-api.tiktok.com/portal/docs/publish-a-public-video-post-to-an-owned-account/v1.3
- DM API 접근 조건: https://business-api.tiktok.com/portal/docs/access-to-business-messaging-api/v1.3
- 미국 데이터 보안 심사: https://business-api.tiktok.com/portal/docs/us-data-security-review/v1.3
- TikTok Shop 미국 Avoid Redirecting Traffic: https://seller-us.tiktok.com/university/essay?knowledge_id=4588077398099713&lang=en
- TikTok Shop 미국 Content Policy: https://seller-us.tiktok.com/university/essay?knowledge_id=6837891779151617
- 참고(남의 도구, 원문 아님): https://uchat.atlassian.net/wiki/spaces/UKB/pages/1248133150/Tiktok+Channel , https://docs.klink.cloud/getting-started/setup-channels/tiktok
