# 조사 C — 해커톤 하루(개발 약 2시간 30분)에 진짜 전화 시연을 만들 수 있나 (2026-10-24)

> 한 줄 결론(제 판단): 된다. 가장 빠른 길은 「Vapi 무료 미국 번호 + Claude 두뇌 + 우리 Vercel 함수 하나에 도구 5개 + 우리 DB 장부에 먼저 쓰고 Google Calendar(서비스 계정)에 따라 쓰기」다. 심사위원 폰은 QR로 「사장 폰」이 되어 한 번 울림과 예약 카드를 받고, 손님 쪽은 노트북 웹 통화로 돌리며, 진짜 전화는 팀원 폰으로 미국 번호에 한 통 걸어 보인다. 구글이 막혀도 화면 캘린더(DB 장부)는 남으므로 시연은 죽지 않는다.

- 쓴 사람: 기초 조사 담당(Claude 서브에이전트). 공식 문서를 직접 열어 확인했다(WebFetch). RingOnce 개발 지시서(`(대회 전 준비 자료)\RingOnce_지시서\CLAUDE.md`)에서 이미 [확인]된 값은 그대로 이어받았다.
- 표지: 문서에서 확인한 것은 그대로, 「확인 필요」는 못 확인한 것, 「제 판단」은 내 판단, 「가정」은 어림이다. 시간은 모두 가정이다.

## 권장 구성

### 부품 표

| 부품 | 무엇을 | 걸리는 시간 어림(가정) | 공식 문서 |
|---|---|---|---|
| Vapi 어시스턴트 | 고정 첫 마디 · 지시문 · 영어 음성 · 받아쓰기. 두뇌는 Claude다. Vapi 의 Anthropic 목록에 `claude-haiku-4-5-20251001` · `claude-haiku-5-5` · `claude-sonnet-4-6` 등이 있고, 「use your own Anthropic account by connecting it in Integrations」라서 팀 크레딧으로 돈다 | 15분 | https://docs.vapi.ai/providers/model/anthropic |
| Vapi 무료 전화번호 | 미국 지역번호 1개 · 받는 전화만(「Free Vapi numbers are inbound only」) · 카드 없이 만들 수 있으나 「Payment method required」가 뜰 수 있음 · 활성화에 몇 분 · 통화 요금은 따로 | 5분 + 대기 | https://docs.vapi.ai/free-telephony |
| 도구 5개(우리 함수) | Vapi 가 도구를 부르면 `message.type = "tool-calls"` 와 `message.toolCallList[]`(`id` · `function.name` · `function.arguments`)를 우리 주소로 보낸다. 우리는 `{"results":[{"toolCallId":"…","result":"한 줄 문자열"}]}` 로 답한다. 「Always respond with HTTP 200」, `result` 는 「must be a flat string」 | 40분 | https://docs.vapi.ai/tools/custom-tools |
| 캘린더 층(`lib/calendar.ts`) | 한 틀 안에 둘을 둔다. ① DB 장부(Upstash Redis): 늘 먼저 쓴다 · 화면 캘린더가 이것을 그린다 ② Google Calendar: 따라 쓴다. 빈 시간 `POST https://www.googleapis.com/calendar/v3/freeBusy` · 만들기 `POST …/calendars/{calendarId}/events` · 바꾸기 `PATCH …/events/{eventId}` · 지우기 `DELETE …/events/{eventId}` · 찾기 `GET …/events?privateExtendedProperty=code=1234` | 서비스 계정 준비 20분 + 코드 30분 | https://developers.google.com/workspace/calendar/api/v3/reference/freebusy/query · …/events/insert · …/events/list |
| 가격 · 시간 계산(코드) | `shop.json` 가격표(증상 분류 → 진단비 · 흔한 수리 값의 범위)에서 코드가 금액을 고른다. 영업 칸(예: 12–2 · 2–4 · 4–6시)에서 busy 를 빼 빈 칸을 낸다. 「내일」 「금요일」 같은 말을 가게 시간대(미국 동부) 날짜로 바꾸는 일도 코드가 한다 | 20분 | (우리 코드) |
| 사장 폰 화면 `/owner?s=` | 근무 시작 · 한 번 울림(소리 · 화면 깜빡임) · 예약 카드(이름 · 연락처 · 증상 · 날짜 · 금액 칸) · [확정] [고치기] · 오늘 일정 목록 | 30분 | RingOnce 지시서 2-2 절 |
| 손님 화면 `/` | QR · 웹 통화 단추(`@vapi-ai/web` · `vapi.start(assistantId, { variableValues: { session }, metadata: { session } })`) · 받아쓰기 칸 · 영어 대사 카드 4장(잡기 · 금액 · 바꾸기 · 취소) | 30분 | RingOnce 지시서 2-1 절 |
| 진짜 울림(선택) | Twilio 로 심사위원 · 팀원 폰에 걸고, 벨이 울린다는 신호(`ringing`) 3.5초 뒤 `Status=canceled` 로 끊는다 | 20분 + 유료 전환 | https://www.twilio.com/docs/usage/tutorials/how-to-use-your-free-trial-account |
| 배포 | Vercel · Next.js. Hobby 요금제도 함수 실행 상한이 기본 300초(fluid compute 기준)라 12초 기다리는 도구도 넉넉하다 | 10분 | https://vercel.com/docs/functions/configuring-functions/duration |

- 합계 약 3시간 10분(가정)이다. 두 사람이 나눠 하면 2시간 30분 안에 든다. 나누는 법은 「만들 순서」에 있다.
- 돈: Vapi 는 새 계정에 「$5 free credits」를 주고, 호스팅은 분당 $0.05에 부품 값이 붙는다(https://vapi.ai/pricing). RingOnce 계산으로 심사 당일 통화 50건이면 약 $20이라 $5로는 모자란다. 미리 충전해 둔다.

### 도구 5개 — AI는 말하고, 코드가 센다

| 도구 | 받는 값 | 코드가 하는 일 · 돌려주는 한 줄 |
|---|---|---|
| `quote_price` | `issue` | 가격표에서 금액을 고른다. 표에 없으면 「Mr. Kim will quote this himself」를 돌려주고 사장 카드에 표시한다(규칙에 없는 가격을 지어내지 않는다) |
| `check_availability` | `dayHint` | 날짜 말을 날짜로 바꾸고 빈 칸을 최대 3개 낸다. 「S1 Fri Oct 24, 2–4 pm · S2 …」 |
| `book_appointment` | `slotId` · `name` · `zip` · `issue` | DB 장부와 구글에 쓴다. 코드가 만든 예약 번호 4자리를 돌려주고 AI가 읽어 준다. 사장 폰에 예약 카드 |
| `find_booking` | `code` 또는 `name` + `zip` | 전화로 걸었으면 발신 번호로 먼저 찾는다(아래). 찾은 예약 한 줄과 `bookingId` 를 돌려준다 |
| `change_booking` | `bookingId` · `action`(`reschedule` · `cancel`) · `slotId` | 바꾸기는 PATCH, 취소는 DELETE(또는 제목 앞에 「취소」를 붙여 남김). 사장 폰에 「변경 · 취소」 카드 |

- 같은 손님을 다시 찾는 열쇠: 전화로 건 통화는 Call 객체 `type` 이 `inboundPhoneCall` 이고 발신 번호가 `customer.number` 에 있다(https://docs.vapi.ai/api-reference/calls/get). 도구 요청에는 `message.call` 이 함께 온다(custom-tools 문서). 웹 통화(`webCall`)에는 발신 번호가 없다고 보고(확인 필요) 예약 번호 4자리나 이름 + 우편번호로 찾는다.
- 구글 일정에는 `extendedProperties.private` 에 `code` · `phone` 을 넣어 둔다. 찾을 때 `privateExtendedProperty=code=1234` 를 쓴다(events.list 문서: 「Extended properties constraint specified as propertyName=value. Matches only private properties.」).
- 손님을 구글 일정의 참석자로 넣지 않는다. 문서가 「Service accounts need to use domain-wide delegation of authority」라고 적어 두었다. 손님 정보는 설명 칸에 적는다.
- 「배운 규칙」 대신 「통화가 예약 기록 한 장이 된다」를 보인다(챗2캐쉬식): 통화가 끝나면(`end-of-call-report` 의 받아쓴 글) Claude 가 정해진 칸을 JSON 으로 뽑고, 사장 폰에서 [확정]을 누른다. 도구 값과 다르면 칸을 노랗게 표시한다(제 판단).

### Google Calendar 서비스 계정 — 가장 짧은 길

1. Google Cloud 콘솔에서 새 프로젝트를 만들고 Google Calendar API 를 켠다.
2. 서비스 계정을 만들고 키(JSON)를 받는다. 내용 전체를 Vercel 환경 변수 하나(`GOOGLE_SA_JSON`)에 넣는다. 저장소 · `.env` 에는 두지 않는다.
3. 사장 계정(시연용 Gmail)에 새 캘린더 「Kim's Heating 예약」을 만들고, 설정의 「특정 사용자와 공유」에 서비스 계정 메일을 넣어 「일정 변경」(Make changes to events) 권한을 준다(여러 설치 안내서가 같은 절차를 적음 · Google 공식 문서에서 이 화면은 확인 필요).
4. 캘린더 설정의 캘린더 ID(`…@group.calendar.google.com`)를 `CALENDAR_ID` 로 넣는다.
5. 코드는 범위(scope) `https://www.googleapis.com/auth/calendar` 하나로 인증한다. 이 범위는 freeBusy 와 events 만들기 둘 다 받는 목록에 들어 있다.
- 시연 노트북에서는 사장 계정으로 Google Calendar 를 열어 두면 예약이 실제 캘린더에 뜨는 장면을 0분에 보인다(제 판단).

### 「한 번 울림」과 사람에게 넘기기

- **화면 울림(기본)**: RingOnce 설계 그대로다. Vapi `status-update`(`in-progress`)와 브라우저 `call-start` 두 신호를 `/api/ring` 으로 받고, `SET ring:{session} 1 NX EX 40` 이 처음 성공할 때만 사장 폰 화면을 울린다. 사장 폰은 서버 전송(SSE)으로 받는다. 아이폰 사파리는 진동 기능이 없어 소리와 깜빡임만 준다.
- **진짜 울림**: Twilio 발신 뒤 벨 신호 3.5초에 끊는다. 체험 계정은 「You can call or message only verified recipients」 · 인증 번호 「up to 5」 · 「SMS and voice are limited to your sign-up country」라서, 심사위원 아무 폰이나 울리려면 유료 전환(RingOnce 는 $20로 봄)과 국제 발신 지역 허가(한국)가 먼저다.
- **문자 알림**: 미국 번호로 업무 문자를 보내려면 A2P 10DLC 등록이 필요하다(RingOnce 기획서 · Twilio 도움말 기준). 하루 시연에는 쓰지 않는다.
- **통화 중 사람에게 넘기기**: Vapi `transferCall` 도구가 E.164 번호로 넘긴다. 기본은 blind(말없이 연결)이고, 요약을 말해 주는 warm 방식(message · summary)은 「Twilio only」다(https://docs.vapi.ai/call-forwarding). 무료 번호는 발신이 안 되므로, 무료 번호에서 넘기기가 되는지와 한국 번호(+82)로 넘길 수 있는지는 확인 필요다. 제 판단: 시연에서는 실제 넘기기 대신 RingOnce 의 `ring_owner`(12초 기다림 → 못 받으면 다시 걸기 약속)를 쓴다.

### 심사위원 QR 시연 — 「내 폰이 사장 폰이 된다」에 필요한 것

- 역할을 하나로 정한다(제 판단): **심사위원 폰은 사장 폰이다.** QR = `/owner?s={session}`. 심사위원이 「근무 시작」을 누르면(소리 허용 · 화면 켜 두기) 노트북 웹 통화가 시작되는 순간 그 폰이 한 번 울리고, 예약 · 변경 · 취소 카드와 오늘 일정이 그 폰에 쌓인다. 두 결합 요소(한 번 울림 · 통화가 예약 기록이 됨)가 한 손 안에 다 보인다.
- 세션이 맞아야 남의 폰이 안 울린다. 웹 통화는 `metadata.session` 으로 세션을 싣는다. 진짜 전화(미국 번호로 건 통화)는 세션을 실을 수 없으므로 「무대용 고정 세션」(예: `s=stage`) 하나에 묶는다(제 판단).
- 심사위원이 자기 폰으로 직접 「거는」 장면이 꼭 필요하면 QR 페이지 안의 「웹으로 걸기」 단추(폰 브라우저 마이크 · 전화 요금 없음)로 한다. 한국 폰에서 미국 번호로 걸면 국제전화라 요금이 심사위원에게 나가므로 권하지 않는다(제 판단 · 요금은 확인 필요). 진짜 전화는 팀원 폰으로 한 통만 보인다.
- 한국 번호를 당일 받는 길은 없다고 본다(제 판단): Twilio 한국 번호는 개인에게 주지 않고, 사업자등록증과 번호 지역의 주소가 필요하다(https://www.twilio.com/en-us/guidelines/kr/regulatory). Vapi 무료 번호는 미국 지역번호뿐이다.
- 한국어: 받아쓰기 Deepgram Nova-3 은 한국어(`ko` · `ko-KR`)를 지원하지만, 여러 언어를 섞어 받는 `multi` 목록에는 한국어가 없다(https://developers.deepgram.com/docs/models-languages-overview). 그래서 한국어 손님용은 어시스턴트를 따로 둬야 한다. 첫 시장이 미국이므로 시연은 영어 어시스턴트 하나와 사장 쪽 한국어 카드로 한다.

## 막히면 대체 길

| 막힌 곳 | 언제 판단 | 대체 길 |
|---|---|---|
| Google 인증 · 공유가 안 됨 | 10:50 | DB 장부만 쓴다. 사장 폰과 노트북의 화면 캘린더가 같은 장부를 그린다. 덱에는 「구글 캘린더 연결은 다음 단계」로 적는다 |
| 잡기만 빨리 보여야 함 | 10:30 | Vapi 내장 Google Calendar 도구(`google.calendar.event.create` · `google.calendar.availability.check` · 대시보드 Integrations 에서 Google 로그인으로 연결 · 코드 0줄). 만들기와 빈 시간만 되고 바꾸기 · 지우기는 문서에 없다. 변경 · 취소는 DB 장부로 한다(https://docs.vapi.ai/tools/google-calendar) |
| 구글 대신 예약 서비스를 쓰고 싶음 | 계획 단계 | Cal.com API v2: 빈 시간 `GET /v2/slots`(`cal-api-version: 2024-09-04`) · 잡기 `POST /v2/bookings`(`2026-02-25` · 손님 `name` · `timeZone` 필수 · 이메일은 필수 아님) · 바꾸기 `POST /v2/bookings/{uid}/reschedule` · 취소 `POST /v2/bookings/{uid}/cancel`. 빈 시간 계산을 대신 해 주지만 계정 · 일정 종류 설정과 버전 헤더 둘이 더 든다. 제 판단: 구글 서비스 계정보다 느리다. 2순위 |
| Vapi 번호 활성화 · 결제에서 막힘 | 10:20 | 웹 통화만 쓴다. 진짜 전화는 결선 때 보인다 |
| 턴 지연이 2초를 넘거나 3번 연속 안 돎 | 11:15 | RingOnce 의 「통화 흉내」(녹음 재생 + 시각표로 상태를 씀)를 기본 단추로 한다. 흉내 시각표에 잡기 · 변경 · 취소 세 장면을 넣는다 |
| Twilio 진짜 울림이 막힘(국제 발신 허가 · 스팸 차단 앱) | 12:00 | 단추를 빼고 화면 울림만 쓴다 |
| Claude 칸 뽑기가 실패 · 8초 초과 | 늘 | 도구가 이미 쓴 값으로 예약 카드를 채운다(미리 쓴 문안) |

## 만들 순서

김덕환 = 화면 · Claude 호출, 김성재 = 계산 로직 · 배포(main 합치기 주인). 윤정민 = 데모 데이터(`shop.json` 가격표 · 영업 칸 · 대사 카드). 시각은 가정이다.

0. (09:40 전 · 사람 · 코드 아님) Vapi 계정 · 무료 번호 · Anthropic 계정 연결 · 크레딧 충전, Google Cloud 프로젝트 · Calendar API 켜기 · 서비스 계정 키 · 시연용 캘린더 공유, Upstash DB 1개, (선택) Twilio 유료 전환 · 한국 발신 허가 · 팀원 폰 시험 1회.
1. 10:00~10:15 김성재: 새 저장소 · Vercel 고정 주소 · 환경 변수(`GOOGLE_SA_JSON` · `CALENDAR_ID` · Vapi 키 · Upstash · Anthropic) · `lib/types.ts`(예약 칸 모양 · 도구 입출력)를 먼저 올린다.
2. 10:00~10:20 김덕환: Vapi 어시스턴트(첫 마디 · 지시문 · Claude · 영어 음성) · 도구 5개 정의(server.url 은 10:15 주소) · 대시보드 시험 통화 1회(이 녹음이 흉내 음원).
3. 10:00~10:25 윤정민: `shop.json`(가격표 8줄 안쪽 · 영업 칸 · 서비스 지역) · 영어 대사 카드 4장 · 한국어 카드 문구.
4. 10:15~10:50 김성재: `/api/vapi` 의 `tool-calls` 처리 · 가격표와 빈 칸 계산 · DB 장부(잡기 · 찾기 · 바꾸기 · 지우기) · 예약 번호 4자리.
5. 10:20~11:00 김덕환: `/owner` 사장 폰 화면(근무 시작 · 울림 · 예약 카드 · 오늘 일정) · `/` 손님 화면(QR · 웹 통화 · 받아쓰기).
6. 10:50~11:20 김성재: Google Calendar 따라 쓰기(freeBusy · insert · patch · delete · 찾기). 10:50 에 인증이 안 되면 DB 장부만으로 간다.
7. 11:00~11:15 김덕환: 이중 신호 울림(`status-update` + `call-start` → `/api/ring` · SSE).
8. 11:15 판단선: 웹 통화로 「잡기 → 바꾸기 → 취소」 3번 연속, 미국 번호로 진짜 전화 1번. 안 되면 「통화 흉내」를 기본으로.
9. 11:15~11:50 김덕환: 통화 뒤 「예약 기록 한 장」(Claude 칸 뽑기 · [확정]) · 화면 다듬기 · 「예시 · 가상 가게」 표시. 김성재: (선택) 진짜 울림 · 상한(세션당 횟수 · IP 상한 금지).
10. 11:50~12:15 김성재: 합치기 · 핫스팟으로 3번 연속 · 다른 폰 시크릿 창에서 QR 과 링크 확인.
11. 12:15 통과선 점검(로그인 없이 열림 · 3번 연속 · 덱 두 문장 · Claude 실패에도 화면 유지 · 울림 한 번만) · 12:30 제출.

## 확인 필요

- Vapi 도구의 기다림 시간 기본값: RingOnce 지시서는 `server.timeoutSeconds` 기본 20초로 적었지만, 이번에 연 custom-tools 문서에는 값이 없다.
- 웹 통화(`webCall`)에 `customer.number` 가 비어 있는지. 도구 요청의 `message.call` 안 정확한 경로(`message.call.customer.number`)도 만들면서 1분 안에 본다.
- Vapi 무료 번호에서 `transferCall` 이 되는지, 한국 번호(+82)로 넘길 수 있는지.
- Vapi 에서 고를 수 있는 한국어 음성 이름(Azure · ElevenLabs 등). 다국어 문서에는 한국어가 적혀 있지 않다.
- Vapi 크레딧 최소 충전 금액(가격 페이지에 없음).
- 개인 Gmail 캘린더를 서비스 계정에 공유하는 화면 이름과, 그 권한으로 freeBusy · 바꾸기 · 지우기가 다 되는지(공식 문서에서는 공유 절차를 못 찾음 · 설치 안내서 근거).
- Twilio 로 한국 휴대폰에 걸었다가 받기 전에 끊은 통화의 요금, 체험 계정의 안내 음성(RingOnce 노트는 「안내 음성이 먼저 나온다」고 적었고 이번 문서에는 없다).
- 한국 휴대폰에서 미국 번호로 거는 국제전화 요금과 통신사 차단 여부.
- 지시문 · 도구 응답만으로 Claude 가 날짜 · 금액을 지어내지 않는지(시험 통화 10통에서 센다).

## 출처

- Vapi: 사용자 정의 도구 https://docs.vapi.ai/tools/custom-tools · 무료 번호 https://docs.vapi.ai/free-telephony · Anthropic 모델 https://docs.vapi.ai/providers/model/anthropic · 다국어 https://docs.vapi.ai/customization/multilingual · 통화 넘기기 https://docs.vapi.ai/call-forwarding · 서버 이벤트 https://docs.vapi.ai/server-url/events · Call 객체 https://docs.vapi.ai/api-reference/calls/get · 내장 Google Calendar 도구 https://docs.vapi.ai/tools/google-calendar · 가격 https://vapi.ai/pricing (모두 2026-10-24 열람)
- Google Calendar API: freeBusy https://developers.google.com/workspace/calendar/api/v3/reference/freebusy/query · events.insert https://developers.google.com/workspace/calendar/api/v3/reference/events/insert · events.list https://developers.google.com/workspace/calendar/api/v3/reference/events/list · 서비스 계정 공유 절차(설치 안내서 · 2차) https://zappysys.com/api/integration-hub/google-calendar-connector/help/authentication/ServiceAccount · https://groups.google.com/d/msg/google-calendar-api/-/tsErJgsHh0wJ
- Cal.com API v2: 잡기 https://cal.com/docs/api-reference/v2/bookings/create-a-booking · 바꾸기 https://cal.com/docs/api-reference/v2/bookings/reschedule-a-booking · 취소 https://cal.com/docs/api-reference/v2/bookings/cancel-a-booking · 빈 시간 https://cal.com/docs/api-reference/v2/slots/get-available-time-slots-for-an-event-type
- Deepgram 언어 목록 https://developers.deepgram.com/docs/models-languages-overview
- Twilio: 체험 계정 https://www.twilio.com/docs/usage/tutorials/how-to-use-your-free-trial-account · 한국 번호 규정 https://www.twilio.com/en-us/guidelines/kr/regulatory
- Vercel 함수 실행 시간 https://vercel.com/docs/functions/configuring-functions/duration
- RingOnce 준비 자료(읽기만): `(대회 전 준비 자료)\RingOnce_지시서\CLAUDE.md` · `reports\AI 전화 응대 기획서 ver2 RingOnce.md` 3 · 4절
- 검색 횟수: WebSearch 2회(서비스 계정 공유 절차 · Twilio 한국 번호) · WebFetch 19회.
