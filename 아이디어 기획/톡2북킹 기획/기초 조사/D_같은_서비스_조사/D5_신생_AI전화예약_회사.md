# D5. 신생·덜 알려진 AI 전화 예약 회사 대조 (열람일 2026-10-24)

범위: 2025~2026 신생 곳, 음성 AI 플랫폼 위 템플릿·에이전시 상품. 이름이 다른 에이전트에 배정된 곳(Jobber, Housecall Pro, ServiceTitan, Workiz, Sameday, Avoca, Rosie, Probook, Netic, Smith.ai, Goodcall, My AI Front Desk, Dialzara, Upfirst, Ruby 등)은 제외.
방법: WebSearch 14회(전부 standard), WebFetch 약 20회. 목적은 반증 찾기. 「?」는 「못 찾음」이며 「없다」가 아님.
한계: 대부분 공식 페이지 한 쪽만 본 것이다. 사이트 안쪽 도움말·가격표 전체를 못 봤으므로 「?」가 많다. 검색 요약만 본 곳은 표에 「요약만」으로 적었다.

## 1. 차별점별 결론 (이 갈래 기준)

| 차별점 | 결론 | 한 줄 이유 |
|---|---|---|
| C1 가격표 안 금액만 말함 | 확인 못 함(부분적으로 가까운 곳 있음: Wakeman) | Wakeman 예시 통화에 사장이 정한 야간 출장비 $189를 말하는 장면이 있으나, 「표에 없으면 말하지 않는다」는 규칙은 어느 곳에서도 확인 못 함. Hey Telo는 「quotes 제공」이라 오히려 반대 방향. |
| C2 한 번 울림 + 실시간 넘겨받기 | 이미 부분적으로 하는 곳 있음(Wakeman, OnCrew, Phone2) | 긴급·사람 요청 시 사장 폰으로 즉시 연결(Wakeman: 통화 중 on-call 전화를 울림). 그러나 「받는 순간 한 번 울리고 AI 응대 중 알림」은 못 찾음. 통화 중 몰래 듣기·끼어들기는 콜센터용 Regal만 확인. |
| C3 사장 모국어 요약 | 살아남음(트레이드 분야 한정). 다만 가까운 곳 있음 | Phone2는 「스페인어 통화, 요약은 영어」(방향이 반대). Pinnacle Intake는 한국어 통화 지원하나 요약 언어 불명. Waboom은 한국어·영어 응대+요약이나 뉴질랜드·호주용. 「영어 통화 + 한국어 요약」은 못 찾음. |
| C4 FSM 없이 구글 캘린더 | 이미 하는 곳 있음(OnCrew, Phonely, Retell·Vapi 템플릿) | OnCrew: 「puts the appointment request on your Google Calendar when you connect it」. Phonely는 Google Calendar 예약. 신생 곳 다수는 FSM(Jobber 등)에 넣는 쪽(Cactus, Acrely, Wakeman). |
| C5 성과 요금(지켜진 예약 건수 계단) | 살아남음 | 검색 3회로 「예약당 과금·예약 0건 0원」 상품을 못 찾음. 전부 월정액($29~$799) 또는 분당·통화당 과금. 모든 곳 기준 「?」가 아니라 「이 갈래에서 못 찾음」임에 주의. |
| C6 전화로 변경·취소 | 이미 하는 곳 있음(Phonely, Waboom, Synthflow 광고) | Phonely: 다시 걸면 AI가 예약을 바꾸고 새 확인 문자. Waboom: 「Books, moves and cancels appointments」. Vapi 포럼은 취소 도구 지원 여부 엇갈림. 트레이드 전용 신생사는 대부분 언급 없음. |
| C7 대상(1인 냉난방, 한인 사장) | 살아남음 | 한인·이민자 사장 전용을 내세운 곳 못 찾음. 대부분 「홈서비스 일반」. |

「똑같은 서비스」(C1~C6 모두): 없음. 「가까운 서비스」(4개 이상 확인): 확인된 곳 없음. 단 Phonely는 C4·C6 확인(트레이드 전용 아님), Wakeman은 C1·C2 부분.
핵심 경고: C4+C6 조합은 범용 음성 AI 플랫폼으로 이미 싸게 판다(Phonely 무료 200분, Retell 분당 $0.07~$0.31). 차별점은 C4·C6 자체가 아니라 「사장이 정한 가격표 안에서만 + 사장 언어 요약 + 성과 요금」 묶음에 있다.

## 2. 회사별 대조

기호: ✅ 확인 / ◐ 부분 / ❌ 안 한다 확인 / ? 못 찾음. 근거는 모두 업체 공식 페이지(마케팅)이며, 한계는 위 참조.

| 회사 | 출시·투자 시기 | 대상 | C1 | C2 | C3 | C4 | C5 | C6 | 요금 | 근거 URL |
|---|---|---|---|---|---|---|---|---|---|---|
| Wakeman | ? (신생 추정, 제 판단) | 홈서비스(Jobber 사용자) | ◐ 예시 통화에 사장이 정한 야간 출장비 $189를 말함 | ◐ 긴급 시 on-call 폰을 통화 중 울림, 계속 사람을 찾으면 연결 | ? | ◐ 예약은 Jobber로(Pro 이상), 구글 캘린더 언급 없음 | ❌ 월정액 | ? | $49(100분)/$149(500분)/$399, 초과 분당 29~45센트 | wakeman.ai |
| OnCrew | ? | 트레이드(1인~다중 트럭) | ? 「학습한 가격」 언급만 | ◐ 긴급 통화를 사장 휴대폰으로 연결, 알림 선택 | ? 요약은 이메일 | ✅ 「puts the appointment request on your Google Calendar」(예약 요청 수준) | ❌ 월정액 | ? | $49(100통)/$149/$349, 초과 통화당 $0.99 | oncrew.ai |
| Phone2 (phone2.io) | ? | 계약자·홈서비스 | ? 「서비스 시간대 quote」만 | ◐ 긴급 시 on-call로 라이브 연결, 사장은 주소·증상을 먼저 봄 | ◐ 스페인어 통화, 요약은 영어 | ? 「캘린더」(종류 불명) | ❌ | ◐ 변경 링크 문자만 | $99(500통), 초과 통화당 $0.99 | phone2.io/post/ai-receptionist-for-contractors (블로그형 자사 글) |
| Phonely | ? | 범용(계약자 템플릿) | ? | ◐ 부서·상담원 연결 | ◐ 다국어·언어 감지 | ✅ Google Calendar, Calendly, Acuity | ❌ | ✅ 「callers can call back to change a booking」 | 월 200분 무료, 대량은 기업 요금 | phonely.ai/template/appointment-scheduling-for-contractors-with-voice-ai |
| Callbook | 2026년 목록 등재(출시일 불명) | 배관·냉난방·전기·지붕·청소 | ? | ? | ◐ 영어·스페인어(페이지 내 불일치) | ◐ 「calendar」(종류 불명), 자체 CRM·견적·인보이스 포함 | ❌ | ? | 문자 $19.99~, 음성 $79~ | alternativeto.net/software/callbook/about/ |
| Cactus (YC P25) | 2025 | 냉난방·배관·지붕·전기 | ? | ? | ? | ❌ FSM 직결(Housecall Pro, Jobber, FieldEdge, ServiceTitan) | ? | ? | 미공개 | ycombinator.com/companies/oncactus (요약만 + 공식 페이지) |
| Acrely (YC) | 2025 추정 | 냉난방·배관·전기 | ? | ? | ? | ◐ ServiceTitan 등 CRM 직결 | ? | ? | 미공개. 「6 customers in two weeks」 | ycombinator.com/launches/OH3-acrely-the-ai-customer-service-representative-for-home-services |
| Hey Telo (YC W25) | 2025 | 독일 수공업체(미국 아님) | ◐ 「quotes 제공」(방향 반대) | ◐ 복잡한 문의는 사람에게 넘김 | ? | ? | ? | ? | 미공개 | ycombinator.com/companies/hey-telo |
| Pinnacle Intake (ARIA) | ? | 법률·홈서비스·치과 등 일반 | ? | ? | ◐ 한국어 포함 9~10개 언어 통화, 통화 후 요약을 이메일·문자로 보냄(요약 언어 불명) | ? 캘린더 종류 불명 | ❌ | ? | $299~$799 | alternativeto.net/software/pinnacle-intake/about |
| Waboom | ? | 뉴질랜드·호주 일반 | ? | ◐ 직원 휴대폰 연결 | ◐ 한국어·영어 응대+통화 요약(요약 언어 불명) | ✅ 캘린더 연결 시 | ❌ 분당 과금 | ✅ 「Books, moves and cancels appointments」 | 분당 71~95센트(+호주 월 A$130) | waboom.ai/ai-voice-agents/multilingual/korean |
| Avidra (Product Hunt) | 2026 추정(날짜 불명) | 배관·냉난방·전기·지붕 | ? | ? 통화 후 기록·예약 확인 | ? | ? 「CRM 연동 없이 시작」, 콜백 예약 | ? | ? | 미공개 | hunted.space/dashboard/avidra |
| Ciela AI | ? | 냉난방 데모·에이전시 | ? | ? | ? | ◐ 데모는 실제 캘린더 예약 안 함 | ❌ | ? | 에이전시 월 $79 | ciela.ai/agents/ai-receptionist-for-hvac-contractors |
| Retell AI 냉난방 템플릿 | 플랫폼(2023~) | 냉난방 | ? | ◐ 못 답하면 맥락과 함께 사람에게 전환 | ? | ✅ Google Calendar 및 ServiceTitan 등 | ❌ | ? 예약만 서술 | 분당 $0.07~$0.31 | retellai.com/use-cases/hvac-virtual-receptionist |
| Vapi / Synthflow 에이전시 상품 | 플랫폼 | 프리랜서·에이전시 구축 | ? | ? | ? | ✅ Google Calendar 도구 | ❌ | ◐ Synthflow는 광고에 「rescheduling and cancellations」, Vapi는 포럼에서 취소 도구 지원이 엇갈리고 「취소했다는데 캘린더에 남음」 사례 | 월 $50~$400 추정(프리랜서 글, 미검증) | support.vapi.ai/t/28494598/rescheduling ; synthflow.ai/?p=31285 (검색 요약만) |
| Trillet | ? | 범용·화이트라벨 | ? | ◐ 생명 위급 통화는 비상선으로 | ? | ✅ Google Calendar 연동 목록에 있음 | ❌ | ? 데모에 「Can I move my appointment?」 | $49~ (가격표 별도) | trillet.ai |
| Joist AI Receptionist | ? | 소규모 계약자 | ? | ◐ 놓친 전화만 AI로 돌리거나 모든 전화 먼저 받게 선택 | ? | ? 자체 앱 일정 | ❌ | ? | 월 $49~ 추가 상품 | joist.com/features/ai-receptionist/ |
| Nexa, DialIQ, Newo.ai, RealVoice AI, VoiceCharm 등 | ? | 트레이드 | ? | Nexa는 사람 상담원 포함 | ? | ? | ? | ? | DialIQ $49~$499, RealVoice $99, VoiceCharm $299(블로그 요약) | stork.ai/blog/ai-receptionist-for-home-services-2026 (검색·블로그 요약만) |

접근 막힘: quadshot.com 데모 페이지(403), callin.io 냉난방 페이지(410), housecallpro.com 블로그(403) — 검색 요약만 봤으므로 표에서 뺐다.

## 3. 가장 가까운 3곳

### ① Wakeman (wakeman.ai)
- 같은 점: 사장 이름으로 전화 받음, 사장이 정한 출장비를 말하는 예시, 긴급 시 사장 폰을 통화 중 울림, 계속 사람을 찾는 손님은 연결, 홈서비스 1인~소규모 대상, 스팸 미과금.
- 다른 점: 예약은 Jobber로 들어감(구글 캘린더 아님), 성과 요금 아님(월 $49~$399), 언어·변경·취소 언급 없음, 「표에 없는 금액은 말하지 않는다」 규칙은 확인 못 함.
- 말할 수 있는 문장: 「Wakeman은 Jobber 사용자에게 문자로 일감을 알려 주지만, 톡2북킹은 Jobber 없이 구글 캘린더에 바로 넣고 사장 모국어 카드로 주며 지켜진 예약 건수만큼만 받는다.」(제 해석)

### ② Phonely 계약자 템플릿 (phonely.ai)
- 같은 점: Google Calendar 예약, 다시 걸면 변경(C6), 다국어, 다시 확인 문자.
- 다른 점: 범용 플랫폼이라 가격표 제한·사장 폰 알림·사장 언어 요약 언급 없음. 무료 200분 후 사용량 과금. 트레이드 전용 아님.
- 말할 수 있는 문장: 「Phonely는 예약 변경까지 되는 범용 도구지만, 톡2북킹은 냉난방 사장의 가격표·긴급 판단·모국어 요약을 처음부터 맞춰 둔 완제품이다.」(제 해석)

### ③ OnCrew (oncrew.ai)
- 같은 점: Google Calendar 연결, 긴급 시 사장 휴대폰으로 연결, 사장이 알림 받을 통화를 고름, 트레이드 전용, 월 $49 시작.
- 다른 점: 캘린더에는 「예약 요청」을 올림(확정 예약인지 불명), 변경·취소·언어·가격표 제한 언급 없음, 통화당 과금 구조, 통화 중 합류 설명 없음.
- 말할 수 있는 문장: 「OnCrew는 예약 요청을 캘린더에 올려 주지만, 톡2북킹은 통화 중에 확정 예약을 넣고 같은 손님이 다시 걸면 바꾸거나 취소한다.」(제 해석, OnCrew 쪽 변경·취소는 못 찾았을 뿐 안 한다고 확인된 것은 아님)

## 4. 정리 (제 판단)
- 반증 결과: 이 갈래에서 C1~C6 전부를 하는 곳은 못 찾음. C4·C6는 이미 하는 곳이 있어 차별점으로 내세우면 약함.
- 가장 안전한 차별점: C5(성과 요금)와 C3(영어 통화 + 사장 모국어 요약), C1의 「표에 없으면 말하지 않음」 규칙, C7(한인 사장).
- 약한 차별점: C4, C6, C2의 긴급 연결 부분(Wakeman·OnCrew·Phone2 있음). C2는 「받는 순간 한 번 울림 + AI 응대 중 알림」 묶음일 때만 구별됨.
- 확인 필요: Wakeman·OnCrew·Phonely·Pinnacle Intake는 가격표 전체·도움말·무료 체험으로 C1·C3·C6를 직접 시험해 볼 것(사람 몫).
- 이 갈래는 신생 곳 위주라 정보가 얇다. 「?」가 많은 것은 「없다」가 아니다.

## 5. 출처 목록 (열람 2026-10-24)
- https://www.ycombinator.com/launches/OH3-acrely-the-ai-customer-service-representative-for-home-services (공식)
- https://www.ycombinator.com/companies/oncactus (공식, YC 기업 페이지)
- https://www.ycombinator.com/companies/hey-telo (공식, YC 기업 페이지)
- https://www.wakeman.ai (공식)
- https://oncrew.ai (공식)
- https://www.trillet.ai (공식)
- https://www.phonely.ai/template/appointment-scheduling-for-contractors-with-voice-ai (공식)
- https://www.retellai.com/use-cases/hvac-virtual-receptionist (공식)
- https://ciela.ai/agents/ai-receptionist-for-hvac-contractors (공식)
- https://www.joist.com/features/ai-receptionist/ (공식)
- https://www.waboom.ai/ai-voice-agents/multilingual/korean (공식)
- https://www.phone2.io/post/ai-receptionist-for-contractors (업체 블로그)
- https://alternativeto.net/software/callbook/about/ (제3자 목록)
- https://alternativeto.net/software/pinnacle-intake/about (제3자 목록)
- https://www.hunted.space/dashboard/avidra (Product Hunt 미러)
- https://www.stork.ai/blog/ai-receptionist-for-home-services-2026 (제3자 블로그, 제휴성 가능)
- https://support.vapi.ai/t/28494598/rescheduling ; https://support.vapi.ai/t/18774075/calendar-integrations (Vapi 지원 포럼, 검색 요약만)
- https://synthflow.ai/?p=31285 (Synthflow 마케팅, 검색 요약만)
- https://lunacal.ai/blogs/ai-receptionist-for-hvac (블로그, 가격 요약만)
- https://support.regal.ai/hc/en-us/articles/48626814195355-How-to-Take-Over-an-AI-Agent-s-Call (콜센터 도구, C2 비교용)
- 접근 막힘: quadshot.com/ai-receptionist-demo/ (403), callin.io/hvac-virtual-receptionist-ai (410), housecallpro.com/resources/best-ai-answering-services-contractors/ (403)
