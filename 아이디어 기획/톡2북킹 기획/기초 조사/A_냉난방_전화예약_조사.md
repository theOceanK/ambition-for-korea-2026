# 조사 A. 미국 냉난방 소규모 사장의 전화 예약 현실

> 한 줄 결론(제 판단): 전화로 예약을 잡고 바꾸고 취소하는 AI는 Jobber(현장 서비스 관리 프로그램)가 이미 월 $29에 판다. 톡2북킹이 설 자리는 세 가지다. 출장비까지만 말하고 수리비는 지어내지 않는 금액 안내, 「한 번 울림」, 그리고 관리 프로그램 없이 일하는 직원 없는 1인 사장이다(이런 사업체가 설비 시공업의 약 3분의 2다).

조사일 2026-10-24 · 웹 검색 10회(상한) · 「놓친 전화」 숫자는 다시 찾지 않고 R1 · R2를 인용한다. 웹 페이지 인용은 WebFetch 요약을 거쳤으므로 덱에 넣기 전 원 URL을 한 번 더 눈으로 확인한다.
믿을 만한 정도: **상** = 정부 통계 · 무작위 시험 묶음 · 회사 공식 도움말 / **중** = 업체 자체 데이터이고 방법을 밝힘 / **하** = 업체 블로그 · 방법 안 밝힘.

## 기획서에 바로 쓸 숫자

| 숫자 | 무엇 | 출처 | 믿을 만한 정도 |
|---|---|---|---|
| 111,207곳, 그중 58%(64,871곳)가 직원 1~4명 | 직원 있는 배관 · 냉난방 시공 사업장(업종 코드 238220), 2023 | [1] 인구조사국 CBP 2023, 파일 직접 계산 | 상 |
| 385,453곳, 한 곳 연 매출 평균 약 $6.9만 | 직원 없는 설비 시공 사업체(전기 · 배관 · 냉난방 · 기타 합계, 코드 2382), 2024 | [2] 인구조사국 NES 2024, 파일 직접 계산 | 상(냉난방만 따로는 없음) |
| 약 65% | 설비 시공 사업체 가운데 직원 없는 곳의 비율 | [1][2]로 제 계산 | 중(연도 · 세는 단위가 다름) |
| $89(대개 $70~200) | 냉난방 출장비(service call fee) 중앙값과 흔한 범위 | [3] 업체 블로그 · [5] 검색 요약 | 하 |
| 수리를 맡기면 출장비 면제가 보통 | 냉난방 출장비 관행 | [3] 업체 블로그 | 하 |
| $1,205 | 냉난방 수리 한 건 평균 매출(2025) | R1 인용(Housecall Pro 집계) [9][26] | 중 |
| 67.8%에서 78.6%로 | 문자 예약 알림이 있을 때 약속에 오는 비율(의료 무작위 시험 7건 · 5,841명) | [10] Cochrane 2013 | 상(단, 의료 분야) |
| 12~18% | 홈서비스 노쇼 비율 | [11] 업체 블로그 | 하 |
| 월 $29(대화 30건), 넘으면 건당 $0.79 | Jobber AI 접수원. 예약 · 변경 · 취소 모두 됨 | [13][14] 공식 가격표 · 도움말 | 상 |
| 전화 +20%, 일감 +25%, 매출 +55% | 폭염 기간 하루 평균(냉난방 업체 약 800곳, 2019~2021) | [23] ServiceTitan | 중 |
| 10월 | 냉난방 출장이 가장 많은 달(7월이 아님) | [24] Samsara 출장 6,500만 건 | 중 |

## 1. 가격 안내 관행

**출장비 · 점검비 금액**
- PipelineOn(마케팅 프로그램 회사, 업체 블로그, 2026-06-05): 「The 2026 median residential service call fee in the US is $89 for HVAC.」(2026년 미국 가정용 냉난방 출장비 중앙값은 $89다.) 흔한 범위 $79~129, 대부분 $69.99~89.99. 표본 · 조사 방법은 밝히지 않았다. [3]
- Housecall Pro(관리 프로그램 회사): 출장비 $70~200, 밤 · 주말 · 긴급은 더 비싸다(검색 요약, 원문 403). [5]
- PICKHVAC(가격 안내 사이트, 2026-05-23): 출장비 「$60-$120」, 출장과 진단을 합치면 평균 $150~300. [4]
- 시간 외 할증(PipelineOn 표): 토요일 낮 1.5배 $129~179 · 평일 밤 1.75배 $149~199 · 일요일 낮과 밤 10시 뒤 2배 $179~249 · 공휴일 2.5~3배 $249~399. [3]
- 면제 관행: 냉난방은 「Usually yes」(맡기면 대개 면제). 트럭에 붙이는 문구 예 「$89 service call. Waived when you approve the repair.」(출장비 $89, 수리를 맡기시면 받지 않습니다.) [3]

**전화로 어디까지 말하나**
- 출장비는 전화로 말한다. PipelineOn이 권하는 상담원 대본은 「Our service call fee is $89 and that covers our technician coming out and diagnosing the problem.」(출장비는 $89이고, 기사가 가서 고장을 진단하는 값까지 들어 있습니다.)다. [3]
- AI 회사 예시도 같다. Avoca 시연 대사 「$89 diagnostic, applied to the repair if same-day.」(진단비 $89, 당일 수리하시면 수리비에서 빼 드립니다.) [8]
- 수리비는 기사가 현장에서 정액 가격표(flat-rate price book, 일마다 값을 미리 정해 둔 표)로 먼저 알린다. ServiceTitan(2026-08-07): 「The technician quotes the price upfront, the customer approves it, and the invoice matches that number exactly.」(기사가 값을 먼저 말하고, 손님이 승인하면, 청구서가 그 숫자와 똑같다.) 상담원이 전화로 수리비를 말하는지는 글에 없다. [6]
- Sameday(AI 회사): 「Sameday can share your approved service fees and pricing ranges」(사장이 승인한 출장비와 가격 범위는 말한다), 「Repairs and replacements that need an assessment are referred to your team for a final quote.」(진단이 필요한 수리 · 교체는 사장 쪽이 최종 견적을 낸다.) [18]
- Jobber AI 접수원은 가격을 말한다는 설명이 없다. 견적이 필요한 일은 「작업 요청」으로 남기고 사장이 견적을 낸다. [15]
- 흔한 금액(PICKHVAC 평균 범위): 정기 점검 $120~180 · 작은 수리(축전기 · 릴레이 · 센서) $200~450 · 냉매 보충 $250~400 · 큰 부품 $1,200~3,500 · 기사 시간당 $75~125(긴급 $125~225). [4] 수리 한 건 평균 매출 $1,205는 R1 인용. [26]

**상담원이 묻는 것(3단계 질문 재료)**: ServiceTitan 대본(2024-02-13) = 무슨 문제인지와 언제부터인지 · 장비 나이 · 위치 · 대수 · 이름 · 주소 · 전화 · 이메일 · 집주인인지 · 주택인지 상가인지 · 누가 내는지. 날짜는 「Are mornings or afternoons better for you?」(오전이 좋으세요, 오후가 좋으세요?)로 묻는다. [7]

## 2. 변경 · 취소 · 노쇼

- **냉난방 · 현장 서비스 노쇼 실측은 못 찾았다.** 업체 블로그 숫자만 있다. SchedulingKit(예약 프로그램 회사, 2026-03-18): 홈서비스 12~18%, 원인 「Scheduled at client location」(손님 집에서 하는 약속). 출처는 「industry surveys and scheduling vendor reports rather than controlled studies」(업계 설문과 예약 업체 보고서이지 통제 연구가 아니다)라고 스스로 밝혔다. [11] Fieldproxy(업체 블로그): 현장 서비스 노쇼 10~30%, 막판 취소 10~15% 더(검색 요약, 근거 없음). [12]
- **문자 알림의 효과(믿을 만한 근거는 의료 분야뿐)**: Cochrane 체계적 문헌고찰(2013, 무작위 시험 8건 · 6,615명). 알림 없음 67.8%, 문자 알림 78.6%, 전화 알림 80.3%가 약속에 왔다. 문자와 전화의 효과는 비슷했다(RR 0.99). 약속 한 번 지키게 하는 비용은 문자가 전화보다 55~65% 쌌다(시험 2건). [10]
- **헛걸음 한 번의 비용(가정)**: 기사와 차를 합친 실비용 「$68-$98/hr」(PipelineOn). 그 글의 예시 방문(75분 일 + 30분 운전)을 넣으면 약 $119~171이다(제 계산). 손님이 집에 없으면 출장비($89)도 못 받는다고 보면 한 번에 $200~260쯤 샌다(가정 · 확인 필요). [3]
- **변경 · 취소를 전화로 받는 AI는 이미 있다**: Jobber 도움말(2026-07-09 고침) 「Online booking must be enabled for Receptionist to reschedule appointments.」(온라인 예약이 켜져 있으면 접수원이 예약을 바꾼다.) 취소도 설정을 켜면 되고, 취소한 방문은 「일정 없음」으로 남고 취소 메모가 붙는다. [14]
- 리마인더(예약 확인 문자)는 Jobber에서 Connect 요금제부터 들어 있다(1인 정가 월 $99~139). 가장 싼 Core에는 「Send automated client reminders」가 없다. [13]

## 3. 예약 관리 도구와 요금 · 업체 수

**업체 수(정부 통계, 내가 파일을 받아 직접 셈)**
- 직원 있는 배관 · 냉난방 시공 사업장(238220) 111,207곳(2023). 직원 1~4명 64,871곳(58%), 10명 미만 77%. [1] (같은 숫자는 R1에도 있다. 1~4명 비율은 이번에 새로 셈.)
- 직원 있는 설비 시공 전체(2382 = 전기 · 배관 · 냉난방 · 기타) 202,656곳(2023). [1]
- 직원 없는 설비 시공 사업체(2382) 385,453곳, 매출 합계 약 $267억, 한 곳 평균 약 $6.9만(2024). 공개 파일에는 냉난방만 따로 센 숫자가 없다(4자리 업종까지만). [2]
- 설비 시공 사업체 가운데 직원 없는 곳 약 65% = 385,453 ÷ (385,453 + 202,656)(제 계산. 연도가 하나 다르고, 직원 없는 쪽은 세금 신고 단위라 부업 · 겸업도 섞여 있을 수 있다. 확인 필요).
- 직원 없는 냉난방 · 배관만 어림하면 약 21만 곳(가정: 직원 있는 쪽에서 238220이 2382의 55%이니 직원 없는 쪽도 같다고 놓음. 385,453 × 0.55).

**도구와 한 달 요금**

| 도구 | 한 달 요금(1인 기준 정가) | 예약 · 리마인더 | 출처 |
|---|---|---|---|
| Jobber | Core $29(연 결제)~$49(월 결제) · Connect $99~139 · Grow $149~199 · Plus $399~(5명부터) | 모든 요금제에 일정 · 온라인 예약, 리마인더는 Connect부터 | [13] 공식 가격표 |
| Housecall Pro | Basic $59(연)~$79(월) · Essentials $149~189(5명) · MAX $299~329(8명) | 공식 페이지 403. 제3자 정리(2026-09-10 공식 가격표와 대조했다고 밝힘) | [16] |
| ServiceTitan | 공개 안 함. 제3자 추정 기사 한 명당 월 $245~500 + 도입비 $5,000~50,000 | 큰 업체용 | [17] 검색 요약 · 제3자 추정 |
| 종이 · 화이트보드 · 구글 캘린더 | $0 | 업체 블로그 일화만(「기사 8명이면 화이트보드가 무너진다」) | 못 찾음(비율 조사 없음) |

- 제 판단: 직원 없는 1인 사업체 평균 매출 연 $6.9만이면 월 $99~139(Jobber 리마인더 요금제)나 ServiceTitan은 무겁다. 이 층은 구글 캘린더나 종이로 버틸 가능성이 높다. 다만 비율을 잰 조사는 못 찾았다.

## 4. AI 전화 예약 경쟁사 (현장 서비스 쪽)

| 회사 | 예약 | 변경 · 취소 | 금액 안내 | 연동 | 요금 | 투자 | 출처 |
|---|---|---|---|---|---|---|---|
| Jobber 접수원(Receptionist) | 됨(Jobber 일정에 바로) | 둘 다 됨(설정 필요) | 언급 없음. 견적은 사장 | Jobber 안 | 월 $29(대화 30건), 초과 $0.79, Plus 요금제는 무제한 | 이번에 확인 안 함 | [13][14][15] |
| Housecall Pro CSR AI | 확인 못 함 | 확인 못 함 | 확인 못 함 | Housecall Pro 안 | 공개 안 함(영업 견적). 제3자 추정 $100~150은 미확인 | 이번에 확인 안 함 | [16] |
| ServiceTitan 음성 AI | 확인 못 함 | 확인 못 함 | 확인 못 함 | ServiceTitan 안 | 공개 안 함, 초기 접근 단계 | 상장사 | R2 인용 [27] |
| Avoca | 됨(Simple Scheduler) | 확인 못 함 | 시연에서 진단비 말함 | ServiceTitan 인증 앱 등 | 공개 안 함 | 합계 $125M+, 기업가치 $1B | R2 인용 [27] · [8] |
| Sameday | 됨(ServiceTitan이면 기사 캘린더까지) | 「Reschedule」 기능 표시, 취소 언급 없음 | 승인한 출장비 · 가격 범위만 | ServiceTitan · Housecall Pro · Jobber · Service Fusion · FieldPulse | Launch 월 $449(500분) · Scale 월 $789(1,000분) | 프리시드 약 $500K, 출처 상충 | [18][19] · R2 인용 [27] |
| Rosie | $49는 예약 링크 문자만, $149부터 캘린더에 직접 | 언급 없음 | 언급 없음 | 캘린더 이름 안 밝힘 | $49(250분) · $149(1,000분) · $299(2,000분) | 못 찾음 | [20] |
| Goodcall | 외부 도구 연결(API · Zapier)로 | 언급 없음 | 언급 없음 | 직접 연동 이름 없음 | $79 · $129 · $299(한 달 고유 고객 수로 셈) | 못 찾음 | [21] · R2 인용 |
| Smith.ai AI 접수원 | 「AI Scheduling (Calendly & more)」 | 언급 없음 | 언급 없음 | Calendly 등 | 무료(25통) · Pro 월 $150(75통, 통당 $2) · Enterprise 월 $500 | 못 찾음 | [22] |

- 회사 주장(근거 안 밝힘): Sameday 「92% Booking rate in most channels」(대부분 통로에서 예약 성공 92%) · 「4M+ Calls answered」 [18]. Jobber 「handling over 20 calls per week on average without any intervention」(사람 손 안 대고 주당 평균 20통 넘게 처리) [15].
- Smith.ai는 R2에서 어느 탭의 가격인지 불명이었다. 이번에 연 AI 접수원 전용 가격표는 위 표와 같다(사람 상담원 연결은 따로 가능). [22]
- 제 판단: 4 · 6 · 7단계(날짜 안내 · 캘린더 등록 · 변경 · 취소)만으로는 차별점이 안 된다. Jobber가 월 $29에 한다. 다만 Jobber 접수원은 Jobber를 쓰는 사장만 쓸 수 있고, Sameday는 관리 프로그램 연동이 중심이며 월 $449부터다. 구글 캘린더만 쓰는 사장에게 바로 얹히는 곳은 Rosie($149) · Smith.ai 정도로 보인다(연동 범위는 확인 필요).

## 5. 계절 몰림

- ServiceTitan(자사 데이터, 2022-04-07): 냉난방 업체 약 800곳 · 2019~2021년 폭염 기간 하루 평균이 전화 +20% · 일감 +25% · 매출 +55%. 폭염 = 「two or more days when the temperature was unusually hot for an area, and the heat did not relent at night」(그 지역치고 유난히 더운 날이 이틀 넘게 이어지고 밤에도 안 식는 때). 폭염 때 놓친 전화 숫자는 없다. [23]
- Samsara(차량 관리 회사, 2025-08-06): 2023-09~2025-06 냉난방 출장 6,500만 건. 「October—not July—consistently marks the busiest month of the year」(가장 바쁜 달은 7월이 아니라 늘 10월). 2월이 가장 적다. 2025년 6월 폭염 때 메인주는 차 한 대당 출장이 전년보다 374% 늘었다(평소 서늘한 곳일수록 크게 늘었다). [24]
- 지역 뉴스(KCTV5, 2026-09-02): 캔자스시티 기사 한 명이 「평소 여름보다 적어도 20% 많다」고 말했다(검색 요약, 한 업체의 말). [25]
- 제 판단: 덱에는 「폭염 때 전화 20% 더」를 쓰고, 「10월이 가장 바쁘다」는 냉방 철 끝 점검과 난방 철 시작이 겹치는 때라 1년 내내 쓸 수 있다는 근거로 쓴다.

## 기획에 주는 뜻 (제 판단)

1. 5단계 금액 안내는 「출장비 $○○, 수리를 맡기시면 받지 않습니다. 수리비는 기사가 가서 먼저 말씀드리고, 승인하시면 시작합니다」까지만 말한다. 업계 관행과 같고 RingOnce 원리 8(규칙에 없는 가격은 지어내지 않는다)과 맞는다.
2. 4 · 6 · 7단계는 Jobber가 월 $29에 이미 한다. VC 앞에서 이걸 차별점으로 내세우면 바로 반박당한다. 내세울 것은 「한 번 울림」, 사장 말(한국어) 요약, 쓰던 구글 캘린더 위에 얹기(챗2캐쉬 C2 「하던 대로 둔다」)다.
3. 첫 손님은 관리 프로그램이 무거운 직원 없는 1인 설비 사업체(38.5만 곳, 연 매출 평균 $6.9만)로 좁힌다. 「끝난 일만 센다」 요금 계단과도 맞는다.
4. 7단계에 예약 전날 확인 문자를 붙인다. 근거는 「의료 시험에서 약속 지키는 비율 67.8%가 78.6%로」이고, 덱에는 의료 분야 결과라고 밝힌다.
5. 시연 대본은 한여름 폭염 날 「에어컨에서 찬바람이 안 나와요」로 한다. 사장이 가장 바쁜 날 전화가 20% 더 온다.

## 못 찾은 것

- 냉난방만 따로 센 1인 사업체 수(NES 공개 파일은 업종 4자리 2382까지만). BLS(노동통계국) 냉난방 기사 자영업 비율은 bls.gov가 403을 돌려줘서 못 봤다.
- 작은 냉난방 업체가 무엇으로 예약을 관리하는지(종이 · 구글 캘린더 · 프로그램)를 잰 조사. 업체 블로그 일화만 있다.
- 냉난방 · 현장 서비스의 노쇼 · 「집에 없음」 실측 비율. 업체 블로그 숫자만 있다(12~18%, 10~30%).
- 전화로 수리비까지 말하는 업체의 비율, 정액 가격표를 쓰는 업체의 비율, 전화 예약 성공률 업계 평균(ServiceTitan 「95%」는 목표치다).
- Housecall Pro CSR AI의 요금 · 기능, ServiceTitan 요금(비공개), Jobber 투자 · 고객 수, Rosie · Goodcall · Smith.ai의 변경 · 취소 기능(페이지에 없음), Rosie 투자.
- Angi · HomeGuide · Housecall Pro 원문(403).
- 당일 사람이 찾을 검색어(레딧): 「reddit HVAC customer not home no show」 · 「reddit HVAC do you give prices over the phone」 · 「reddit Jobber receptionist review」.

## 출처 (모두 2026-10-24 열람)

1. U.S. Census Bureau · County Business Patterns 2023 · 미국 전체 파일 · https://www2.census.gov/programs-surveys/cbp/datasets/2023/cbp23us.zip (내려받아 238220 · 2382 행을 직접 셈)
2. U.S. Census Bureau · Nonemployer Statistics 2024 · 미국 파일(서버 수정일 2026-09-29) · https://www2.census.gov/programs-surveys/nonemployer-statistics/datasets/2024/historical-datasets/nonemp24us.zip (2382 행을 직접 셈)
3. PipelineOn · 「Service Call Fee: What to Charge in 2026」 · 2026-06-05 · 업체 블로그 · https://pipelineon.com/blog/service-call-fee/
4. PICKHVAC · 「HVAC Service, Tune-Up and Inspection Cost 2026」 · 2026-05-23 · 가격 안내 사이트 · https://www.pickhvac.com/?p=46346
5. Housecall Pro · 「How to price HVAC services」 · 날짜 미확인 · 업체 블로그 · 검색 요약만(403) · https://www.housecallpro.com/resources/how-to-price-hvac-services/
6. ServiceTitan · 「HVAC Flat-Rate Pricing」 · 2026-08-07 · 업체 블로그 · https://www.servicetitan.com/blog/hvac-flat-rate-pricing
7. ServiceTitan · 「HVAC Call Scripts」 · 2024-02-13 · 업체 블로그 · https://www.servicetitan.com/blog/hvac-call-scripts
8. Avoca · AI Coach for HVAC · 날짜 미표기 · 업체 페이지 · https://www.avoca.ai/coach/hvac
9. Housecall Pro · 「HVAC industry trends」(수리 한 건 평균 $1,205) · R1이 검색 요약으로 인용 · https://www.housecallpro.com/resources/hvac-industry-trends/
10. Gurol-Urganci I. 외 · 「Mobile phone messaging reminders for attendance at healthcare appointments」 · Cochrane Database of Systematic Reviews · 2013 · doi 10.1002/14651858.CD007458.pub3 (Europe PMC 초록으로 열람)
11. SchedulingKit · 「Average no-show rates by industry」 · 2026-03-18 · 업체 블로그 · https://schedulingkit.com/blog/average-no-show-rates-by-industry
12. Fieldproxy · 현장 서비스 노쇼 글 · 업체 블로그 · 검색 요약만 · https://www.fieldproxy.ai/articles/field-service-customer-no-show-management
13. Jobber · 가격표 · https://www.getjobber.com/pricing/
14. Jobber Help Center · 「Receptionist powered by Jobber AI」 · 처음 2024-07-31, 고침 2026-07-09 · https://help.getjobber.com/en/articles/receptionistpowered-by-jobber-ai/
15. Jobber · AI Receptionist 기능 페이지 · https://www.getjobber.com/features/ai-receptionist/
16. ContractorToolStack · Housecall Pro pricing · 2026-09-10(공식 가격표와 대조했다고 밝힘) · 제3자 정리 · https://contractortoolstack.com/software/housecall-pro/pricing/
17. ServiceTitan 요금 제3자 추정 · 검색 요약 · https://www.getonecrew.com/post/servicetitan-pricing · https://projul.com/blog/servicetitan-pricing-analysis-2026 · https://trustradius.com/products/servicetitan/pricing
18. Sameday · 가격표 https://sameday.ai/pricing · HVAC 페이지 https://sameday.ai/industries/hvac
19. Sameday 투자 · 회사 목록 사이트(검색 요약, 프리시드 $500K 또는 합계 $750K로 상충) · https://www.extruct.ai/hub/gosameday-com-funding · https://www.cbinsights.com/company/sameday
20. Rosie · 가격표 · https://heyrosie.com/pricing
21. Goodcall · 가격표 · https://www.goodcall.com/pricing
22. Smith.ai · AI Receptionist 가격표 · https://smith.ai/pricing/ai-receptionist
23. ServiceTitan · 「HVAC revenue during heat waves」 · 2022-04-07 · 자사 데이터 · https://www.servicetitan.com/blog/hvac-revenue-heat-waves
24. Samsara · 「Peak season for HVAC」 · 2025-08-06 · 자사 데이터 · https://www.samsara.com/blog/peak-season-for-hvac
25. KCTV5 · 「Heat wave pushes metro AC units, HVAC crews to the limit」 · 2026-09-02 · 검색 요약만 · https://www.kctv5.com/2026/09/02/heat-wave-pushes-metro-ac-units-hvac-crews-limit/
26. 팀 조사 R1 · `(대회 전 준비 자료)\research_notes\AI 전화 응대\R1_시장_못받는전화.md`(놓친 전화 숫자 · 수리 평균 $1,205 · 238220 사업장 수)
27. 팀 조사 R2 · `(대회 전 준비 자료)\research_notes\AI 전화 응대\R2_경쟁사_투자.md`(Avoca · ServiceTitan · Sameday 투자 · Goodcall 요금)
