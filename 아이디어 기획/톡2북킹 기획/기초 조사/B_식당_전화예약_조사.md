# 조사 B. 미국 식당의 전화 예약 현실

> 한 줄 결론(제 판단): 식당에서 돈이 새는 큰 구멍은 노쇼(예약하고 안 오는 손님)보다 **늦은 취소와 바쁜 시간에 못 받는 전화**다. 그런데 식당 AI 전화 시장은 이미 투자를 많이 받은 경쟁사가 붐빈다. 그래서 톡2북킹은 식당 일반이 아니라 **예약 장부 없이 사장이 직접 전화를 받는 작은 식당**으로 좁혀야 한다.

- 쓴 사람: 기초 조사 담당(Claude 서브에이전트) · 2026-10-24. 웹 검색 8회(상한 8) · WebFetch 약 25회. 레딧은 시도하지 않았다.
- 표지: 「업체 블로그」 = 전화 AI · 예약 시스템을 파는 회사가 자기 고객 자료로 낸 숫자. 「검색 요약」 = 원문을 못 열고 검색 결과 요약만 본 것. 「팀 조사」 = `(대회 전 준비 자료)\research_notes\AI 전화 응대\` 의 RingOnce 조사 파일을 다시 옮긴 것. 「제 판단」 = 내 해석. 「제 계산」 = 원천 숫자로 내가 계산한 것.

## 기획서에 바로 쓸 숫자

| 숫자 | 무엇 | 출처 | 믿을 만한 정도 |
|---|---|---|---|
| 33% | 바쁜 시간에 식당이 못 받는 전화 | Maple 2025-12-07 · 통화 120만+ · 업체 블로그 | 낮음~중간(못 받은 전화 수는 가게가 스스로 보고) |
| 9% · 40% | 안 받힌 전화: 풀서비스 식당 · 퀵서비스(패스트푸드형) 식당 | Revmo 2026 · 통화 녹음 12,091건 · 업체 보고서 · 팀 조사 R1 | 중간(녹음 기반 · 식당 수 미공개) |
| 34% | 식당 전화 중 영업시간 밖에 오는 전화 | Slang 자체 통화 자료 · implicator.ai 기사(2026-02-24) 재인용 | 낮음(업체 자료 2차) |
| 38% | 식당 전화 중 예약 전화 | Maple 2025-12-07 · 업체 블로그 | 낮음~중간 |
| 72% | 예약해 본 사람 가운데 「보통 전화로 예약한다」 | AYTM 설문 2016-12 · 1,000명 | 중간(오래됨 · 지금은 확인 필요) |
| 3.17% | 미국 식당 노쇼 비율 | resOS 노쇼 지수 2026 · 미국 예약 309,604건 · 식당 316곳 | 중간(예약 시스템 회사 자기 자료지만 표본 · 정의 공개) |
| 15% · 56% | 예약 중 취소된 비율(제 계산) · 그 취소 중 24시간 안에 들어온 비율 | resOS 2026 · 전체 예약 3,768,761건 중 취소 566,049건 | 중간 |
| 3배 이상 | 늦은 취소가 노쇼보다 많다 | resOS 2026 | 중간 |
| 16% 낮음 | 문자 알림을 받은 예약의 노쇼(같은 식당 비교 · 원인 아닌 연관) | resOS 2026 | 중간 |
| $399 · $599 | 식당 AI 전화 대표 업체 Slang 의 매장 1곳 월 요금(부터) | Slang 공식 요금 페이지 | 높음 |
| $36M(누적 $68M) · 2,000곳+ | Slang 2026-02 투자 · 쓰는 식당 매장 수 | Pulse 2.0 보도자료 기사 2026-02-24 | 중간~높음 |
| $250 · $720 | 사람이 받는 응대 대행 Ruby 월 요금(50분 · 200분) | Ruby 공식 요금 페이지 | 높음 |
| 192,465곳 | 미국 한인 소유 사업체(2007 · 직원 있는 곳 71,423) | 미국 인구조사국 SBO 2007 | 높음(단 19년 전) |

## 1. 식당이 놓치는 전화

- **바쁜 시간 33%** — 「Restaurants miss 33% of incoming calls during peak service hours」(식당은 바쁜 시간에 들어오는 전화의 33%를 놓친다). 「68% of all calls occur during lunch (11am to 2pm) and dinner (5pm to 9pm) rushes」(전화의 68%가 점심 · 저녁 바쁜 시간에 온다). 표본은 「over 1.2 million calls across 1,000+ restaurant and local business locations from December 2023 to November 2025」. 업체 스스로 못 받은 전화 수는 가게 자기 보고이고 「may not be representative of all U.S. restaurants」(미국 식당 전체를 대표하지 않을 수 있다)라고 적었다. 출처: Maple · 업체 블로그 · 2025-12-07.
- **식당 종류마다 크게 다르다** — Revmo 「State of Calls Report 2026」(통화 녹음 12,091건): 퀵서비스 40% 안 받힘(원문 열람) · 풀서비스 9% · 패스트캐주얼 25% · 피자 7%(팀 조사 R1 · 검색 요약). 「more than one in 10 calls go unanswered」(열 통 중 한 통 넘게 안 받힌다). 출처: Revmo · 업체 보고서.
- 다른 업체 숫자: Hostie 는 「roughly 30% of restaurant calls go unanswered during peak hours」라고 썼지만 출처를 「Industry data」로만 적었다(업체 블로그 · 2026-05-07 · 근거 불명).
- **전화 내용** — Maple 표: 예약 38%(업체 블로그). 팀 조사 R5 의 Maple 다른 자료: 예약 중심 식당은 예약 28.3% · 「사람 바꿔 달라」 14.2%. Slang 은 예약 57%(검색 요약). 업체마다 크게 다르다. Slang 자료: 식당 전화의 71%가 매출과 바로 이어지고, 34%는 영업시간 밖에 온다(implicator.ai 2026-02-24 기사 재인용 · 업체 자료).
- **전화 예약 비중(오래된 자료뿐)** — AYTM 2016-12 설문 1,000명: 「72% said they usually make their reservations over the phone」 · 「25% regularly make online reservations」. 응답자 나라는 적혀 있지 않다. 코넬대 호텔경영 연구소(Kimes · Kies 2012 · 미국 소비자 474명): 「the telephone remains by far the most common way to make a restaurant reservation」(전화가 여전히 가장 흔한 예약 방법이다). 같은 연구의 「71.7%가 전화」는 검색 요약에서만 봤고 원문 대조는 못 했다.
- **놓친 전화의 돈** — Maple: 「The average unanswered call represents $85 in potential lost revenue」(안 받힌 전화 한 통 = 평균 $85 매출 기회 · 업체 블로그 · 계산법 미공개). Revmo: 매장 50곳 퀵서비스 체인이 놓친 전화로 한 해 $3.65M 손실(업체 보고서). Hostie 의 「한 해 $150K~250K」는 「하루 15통 × 예약 20% × $150」 가정에서 나온 숫자라 쓰지 않는다.
- 손님 반응: CallRail 2025-09 미국 소비자 1,000명 중 82%가 「안 받으면 다른 곳에 건다」(모든 업종 · 팀 조사 R1). Popmenu 「음성 사서함에 두 번 닿으면 83%가 그 식당을 포기」(implicator.ai 재인용 · 2차).

## 2. 노쇼와 예약 변경 · 취소

- **노쇼 비율** — resOS(유럽 예약 시스템 회사) 「No-Show Index 2026」: 「the average recorded restaurant no-show rate is 2.33%」, 표본 「3,768,761 reservations across 2,417 restaurants」, 기간 「between August 2025 and July 2026」. **미국은 3.17%**(309,604건 · 316곳). 저녁 2.63% · 점심 1.84%. 노쇼는 직원 · 연동이 기록한 경우만 센다(「never an automatic timeout」). 게시 2026-08-19.
- 다른 숫자: 「OpenTable 망 노쇼 10~20%」 · 「예약금 · 카드 보증이면 절반 이하, 5~7%」 · 「당일 알림이면 20~50% 감소」는 업체 블로그(ainora.lt)가 OpenTable 을 인용했다며 적었지만 원문 링크가 없다(확인 필요). resOS 3.17% 와 크게 다르다. 재는 법(무엇을 노쇼로 치나)이 숫자를 가른다.
- **취소가 노쇼보다 크다** — resOS: 취소 566,049건(전체 예약의 약 15.0% · 제 계산 566,049 ÷ 3,768,761). 「56% of them arrived within 24 hours of the booking, or after it had already started」(취소의 56%가 예약 24시간 안에, 또는 시작한 뒤에 왔다). 시작 뒤 취소 7.1% · 0~2시간 전 17.4% · 2~6시간 전 15.0% · 6~24시간 전 16.6%. 늦은 취소가 「outnumbered recorded no-shows more than three to one」(기록된 노쇼보다 3배 넘게 많다).
- **문자 알림** — resOS: 「Reservations with a delivered SMS reminder showed a 16% lower recorded no-show rate than reservations at the same restaurants without one.」 원인이 아니라 연관이라고 밝혔다. The Access Group 의 「24시간 전 문자로 최대 30% 감소」는 업체 블로그 · 원출처 없음.
- **예약금 · 카드 보증** — resOS: 노쇼 보호를 건 예약은 노쇼 0.80%(238,539건 중 1,907) · 안 건 예약 2.47%(3,461,164건 중 85,589). 좋은 손님만 보호를 받아들였을 수 있어 효과와 선택을 가르지 못한다고 적었다.
- **식당이 잃는 돈** — 공식 달러 숫자는 못 찾았다. 어림(가정): 하루 예약 손님 100명 · 1인 $40 이면 노쇼 3.17% 는 하루 약 $127, 30일 약 $3,800 의 매출 기회다(100 × 0.0317 × $40 × 30). 1인 $40 과 하루 100명은 내가 둔 가정이다.
- 예약 「변경」 비율: 못 찾음.

## 3. 지금 쓰는 대안과 비용

- **OpenTable**(예약 장부 · 손님 망): 공식 요금 페이지는 두 번 다 시간 초과로 못 열었다. 경쟁 업체 블로그(Eat App)는 Basic $149 · Core $299 · Pro $499/월 + 망에서 온 손님 1명당 $1.50(Basic) · $1.00(Core · Pro), 12개월 자동 갱신이라 적었다. Capterra 목록은 $39 · $249 · $449/월로 다르다. 2026년 초부터 예약금 · 노쇼 벌금 같은 결제에 2% 수수료를 붙였다고 한다(Eat App · 확인 필요).
- **Resy**: Eat App 기준 $249 · $399 · $899/월, 손님당 수수료 없음(출처 하나 · 공식 페이지는 내용이 안 읽힘 · 확인 필요).
- **사람 응대 대행 Ruby**(공식 요금): 50분 $250 · 100분 $395 · 200분 $720 · 500분 $1,725/월. 「optional AI enhancements are available in all our plans, at no extra cost」. 초과 분당 요금은 안 적혀 있다.
- **Yelp Host** $149/월(Yelp 손님 관리 고객 $99) · **Yelp Receptionist** $99/월(팀 조사 R2 · 검색 요약).
- **직원이 받기**: 식당 안내 직원(호스트) 시급은 노동통계국(BLS) 페이지가 다른 화면으로 넘어가 못 찾았다.
- 제 판단: 예약 장부(OpenTable · Resy)는 한 달 $150~900 에 손님당 수수료까지 내야 한다. 작은 식당은 장부 없이 종이 · 전화로 받는 곳이 많을 것이다(가정 · 숫자 못 찾음). 톡2북킹이 「캘린더 한 건」으로 장부를 대신하면 이 비용이 비교선이 된다.

## 4. AI 전화 예약 경쟁사 (식당 쪽)

| 업체 | 하는 일 | 요금 | 투자 · 규모 | 출처 |
|---|---|---|---|---|
| Slang AI | 24시간 전화 응대 · 예약 · 단체석 · 출장 요리 문의 · 단골 알아봄 · 중요한 손님은 직원에게 넘김. OpenTable · SevenRooms · Yelp · Resy 연동. 설정 30분 미만. Core 에 스페인어, Premium 은 97개 언어 | Core $399 · Premium $599/매장/월(부터) · 기사는 $450~600 | 2026-02 Series B $36M(USVP 주도 · 지분 $28M + 빚 $8M) · 누적 $68M · 매장 2,000곳+ · 통화 2,500만+ | 공식 요금 페이지 · Pulse 2.0(2026-02-24) · implicator.ai |
| Hostie | 전화 · 문자 · 예약 · 포장 주문 · 단체 행사 문의. Premium 은 「Book and modify reservations」(예약 잡기 · 바꾸기) · 20개 언어 | 페이지에 값 없음 · 「$199/월부터」(기사 · 2차) | 2026-07 Series A $12M(Obvious Ventures 주도) · 누적 $16M · 미국 식당 「hundreds」 · 손님 대화 200만+ · 예약 손님 40만+ | Pulse 2.0(2026-07-09) · 공식 요금 페이지 |
| Loman | 피자 · 포장 많은 식당. 주문 · 전화 예약 · 전화 결제 · 주문 판매 시스템(POS) 연동(Toast · Square · Clover 등) · OpenTable · Resy 연동 | 값 비공개(「Request Pricing」) · 「분당 요금 없음」 | 2025-08 시드 $3.5M(Next Coast Ventures 주도) | 공식 요금 페이지 · BusinessWire(검색 요약 · 원문 403) · 팀 조사 R2 |
| Maitre-D | 전화 · 문자 · 이메일 · 예약 · 주문 · 20개 언어 · 주문 판매 · 예약 시스템 연동 | 못 찾음 | 못 찾음 | 자기 소개 페이지(검색 요약) |
| SoundHound | 전화 주문 · 드라이브스루 · 키오스크 음성 주문 · 주문 판매 시스템 연동. 예약은 페이지에 없음 | 공개 안 함 | 상장사 | 공식 식당 페이지 |
| Yelp Host · Receptionist | 식당 · 서비스업 전화 응대 · 통화 요약 | $99~149/월 | 상장사 | 팀 조사 R2 |
| OpenTable · Resy · SevenRooms | OpenTable 은 자체 전화 AI 없이 「integrates with industry-leading voice AI solutions」(제휴)라는 검색 요약만 있다. Resy · SevenRooms 자체 전화 AI 는 못 찾음 | — | — | 검색 요약 · 확인 필요 |

- 그 밖에 이름만 나온 곳: Vox · Revmo · Certus AI · RestoHost($299 · $499 · 업체 블로그) · Kea($10M Series A · 날짜 미확인 · 팀 조사 R2) · ConverseNow.
- implicator.ai 기사는 이 시장을 「around $10 billion today」(지금 약 100억 달러), 2029년 490억 달러로 적었다. 원출처는 안 밝혔다(쓰지 않는 편이 낫다 · 제 판단).
- 제 판단: 경쟁사는 모두 **OpenTable · Resy 같은 예약 장부와 주문 판매 시스템 연동**을 앞세운다. 즉 이미 장부를 쓰는 중간 이상 식당을 노린다. 「사장 폰 한 번 울림」 「사장 말(한국어)로 요약」 「장부 없는 가게의 캘린더」를 내세운 곳은 못 찾았다(없다고 단정은 못 함).

## 5. 미국 한인 식당 · 한인 사업체 수

- 미국 인구조사국 사업주 조사(SBO) 2007: 「Koreans owned 192,465 firms (12.4 percent), with receipts of $78.6 billion (15.5 percent)」 · 「In 2007, there were 71,423 Korean-owned employer firms」. 2002 년은 약 15만 8천 곳(검색 요약). 지금 조사(연간 사업 조사 ABS)의 한인 숫자와 한인 식당 수는 못 찾았다.
- 비교용(팀 조사 R1 · 인구조사국 CBP 2023): 직원 있는 미국 식당 사업장 528,714곳(풀서비스 258,626 + 퀵서비스 270,088) · 그중 65%가 직원 20명 미만.

## 기획에 주는 뜻 (제 판단)

1. 사용자 흐름 7단계 「전화로 취소 · 변경」은 덤이 아니라 돈이 되는 기능이다. 늦은 취소가 노쇼의 3배가 넘으니, 취소 전화를 바로 받아 빈자리를 다시 여는 것이 식당에서 가장 셀 수 있는 효과다.
2. 예약 식당(풀서비스)은 못 받는 전화가 9%로 낮다. 「바쁜 시간 33%」 「영업시간 밖 34%」로 시간을 좁혀 말해야 숫자가 산다.
3. 식당 AI 전화는 Slang($68M) · Hostie($16M) · Loman · Yelp 가 이미 있다. 식당만으로 정면 승부하면 약하다. 첫 고객은 사용자 예시대로 서비스업(에어컨 수리)에 두고, 식당은 「장부 없는 작은 한인 식당」 둘째 칸으로 둔다.
4. 가격 비교선: Slang $399~599 · Hostie $199~ · Yelp $99~149 · Ruby $250~ · OpenTable $149~499 + 손님당 수수료. RingOnce 계단($0 · $49 · $149 · $299)은 그 아래에 선다.
5. 알림 문자(노쇼 16% 낮음)는 만들기 쉽고 효과 숫자가 있다. 예약 확정 문자에 「바꾸려면 이 번호로 전화」를 넣으면 7단계와 바로 이어진다.

## 못 찾은 것

- 미국 식당이 노쇼 · 늦은 취소로 잃는 돈의 공식 달러 숫자 · 예약 변경 비율.
- 2020년 이후 미국 전화 예약 비중의 독립 설문(있는 것은 2016 · 2012 자료뿐).
- 식당 안내 직원(호스트) 시급(BLS 페이지가 안 열림) · OpenTable · Resy 공식 요금(페이지 안 열림).
- OpenTable · Resy · SevenRooms 자체 전화 AI 여부(OpenTable 제휴는 검색 요약뿐) · Maitre-D 요금 · 투자 · SoundHound 식당 예약 기능 · Loman 공식 요금.
- 최신 한인 사업체 수(ABS) · 한인 식당 수.
- 당일 사람이 찾을 검색어(레딧): `site:reddit.com/r/restaurantowners missed calls reservations` · `site:reddit.com/r/restaurantowners Slang AI` · `site:reddit.com/r/KitchenConfidential no shows phone` · `site:reddit.com/r/smallbusiness AI receptionist restaurant`.

## 출처

- Maple, The State of Restaurant Phone Communication: Insights from 1 Million+ Calls (2025-12-07) https://maple.inc/blog/the-state-of-restaurant-phone-communication-insights-from-1-million-calls
- Revmo, State of Calls Report 2026 https://revmo.ai/guides/state-of-calls-report · PDF(팀 조사 R1) https://wp.revmo.ai/wp-content/uploads/2026/04/REVMO_STATE-OF-CALLS-REPORT-2026-SS.pdf
- Hostie, Why 30% of Restaurant Calls Go Unanswered (2026-05-07) https://hostie.ai/articles/restaurant-calls-unanswered-statistics
- implicator.ai, Slang AI proved restaurants need voice AI… (2026-02-24) https://www.implicator.ai/slang-ai-proved-restaurants-need-voice-ai-now-it-needs-to-prove-they-need-slang/
- AYTM, Online Reservations Survey (2016-12-19) https://aytm.com/post/online-reservations-survey
- Kimes · Kies, The Role of Multi-Restaurant Reservation Sites in Restaurant Distribution Management (Cornell, 2012) https://ecommons.cornell.edu/entities/publication/80e251d5-bde1-4d84-8fbd-262efacc6fef
- resOS, Restaurant No-Show Index 2026 (2026-08-19) https://resos.com/restaurant-no-show-rate/
- ainora.lt, Restaurant No-Show Statistics 2026 https://ainora.lt/blog/restaurant-no-show-statistics-2026 · The Access Group https://www.theaccessgroup.com/en-gb/blog/hos-8-ways-to-reduce-no-shows-in-your-restaurant/
- Eat App, OpenTable pricing https://restaurant.eatapp.co/blog/opentable-pricing · Capterra https://www.capterra.ie/software/17313/opentable-for-restaurants
- Ruby 요금 https://www.ruby.com/pricing/
- Slang 요금 https://www.slang.ai/pricing · Pulse 2.0, Slang AI $36 Million Series B (2026-02-24) https://pulse2.com/slang-ai-36-million-series-b/amp/
- Pulse 2.0, Hostie Raises $12 Million Series A (2026-07-09) https://pulse2.com/hostie-raises-12-million-series-a-to-expand-ai-powered-restaurant-concierge-platform/ · Hostie 요금 https://hostie.ai/pricing
- Loman 요금 https://www.loman.ai/pricing · BusinessWire (2025-08-26) https://www.businesswire.com/news/home/20250826992233/en/Loman-AI-Raises-$3.5-Million-to-Transform-Restaurant-Operations-with-Voice-AI
- Maitre-D 소개 https://www.videosdk.live/ai-apps/maitre-d · SoundHound 식당 https://www.soundhound.com/restaurants/usa
- OpenTable 음성 AI 제휴(검색 요약) https://www.opentable.ca/restaurant-solutions/en/?p=81272
- U.S. Census Bureau, Survey of Business Owners: Asian-Owned Firms 2007 https://www.census.gov/library/publications/2007/econ/2007-sbo-asian.html
- 팀 조사 `(대회 전 준비 자료)\research_notes\AI 전화 응대\` R1_시장_못받는전화.md(Revmo · CallRail · CBP 2023) · R2_경쟁사_투자.md(Yelp · Loman · Kea) · R5_고통_학습가치.md(Maple 전화 의도)
