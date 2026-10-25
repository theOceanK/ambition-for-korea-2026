"""트라가티제 요금 개편(2026-10-24) 숫자 계산. 실행: python -X utf8 계산.py

기존 기획서(Google 문서 6절)의 원가 · 이탈률 · CAC 가정은 그대로 옮기고,
바뀐 것은 요금 단계와 클릭 요금뿐이다.
"""

PAY_FEE = 0.037        # 구독료 카드 결제 수수료(기획서: 실효 약 3.74%, 표에서는 약 3.7%)
FX = 1400              # 1달러 = 1,400원(기획서 가정)

# 단계: 기본료, 콘텐츠 원가, 전화 원가, 서버·고객지원, 포함 클릭, 넘는 클릭 단가, 월 클릭(가정), 비중, CAC
TIERS = {
    #            기본료    콘텐츠   전화    지원    포함   단가  월클릭  비중   CAC
    "베이직":   (49_000,   8_000,      0, 10_000,   300,  50,   450, 0.65, None),
    "라이트":   (199_000, 20_800, 15_000, 15_000, 1_000,  50, 1_500, 0.25, 500_000),
    "프리미엄": (399_000, 52_000, 45_000, 50_000, 3_000,  30, 6_000, 0.10, 1_000_000),
}
# 월 클릭 가정: 숏폼 1개당 월 15번(30 · 100 · 300개). 프리미엄은 매장 5곳 QR 에서 1,500번 더.
# 베이직 CAC: 기존 기획서는 2.9만 원 단계 30% = 온라인 가입 10만 원, 4.9만 원 단계 35% = 현장 영업 50만 원.
# 두 무리가 모두 새 베이직(65%)으로 오므로 그 비율을 그대로 쓴다.
CAC_BASIC = (0.30 * 100_000 + 0.35 * 500_000) / 0.65


def tier_numbers(name, clicks_on=True):
    fee, content, phone, support, incl, rate, clicks, share, cac = TIERS[name]
    click_rev = max(clicks - incl, 0) * rate if clicks_on else 0
    click_rev = min(click_rev, fee)                      # 클릭 요금 월 상한 = 기본료
    sub_gp = fee - content - phone - round(fee * PAY_FEE) - support
    click_gp = click_rev * (1 - PAY_FEE)                 # 링크 넘겨주기 원가는 거의 0원
    return dict(fee=fee, click_rev=click_rev, rev=fee + click_rev,
                sub_gp=sub_gp, gp=sub_gp + click_gp, share=share,
                cac=cac if cac else CAC_BASIC)


def blended(clicks_on=True, churn=0.04, cac_override=None, shares=None):
    rows = {n: tier_numbers(n, clicks_on) for n in TIERS}
    if shares:
        for n, s in shares.items():
            rows[n]["share"] = s
    arpu = sum(r["rev"] * r["share"] for r in rows.values())
    sub_arpu = sum(r["fee"] * r["share"] for r in rows.values())
    gp = sum(r["gp"] * r["share"] for r in rows.values())
    cac = sum((cac_override or {}).get(n, r["cac"]) * r["share"] for n, r in rows.items())
    ltv = gp / churn
    return dict(arpu=arpu, sub_arpu=sub_arpu, gp=gp, cac=cac, ltv=ltv,
                ltv_cac=ltv / cac, payback=cac / gp)


def won(x):
    return f"{x:,.0f}원"


def eok(x):
    return f"{x / 1e8:,.1f}억 원"


if __name__ == "__main__":
    print("== 단계별 (클릭 가정 포함)")
    for n in TIERS:
        r = tier_numbers(n)
        print(f"{n}: 기본료 {won(r['fee'])} 클릭 {won(r['click_rev'])} 합 {won(r['rev'])} | "
              f"구독 이익 {won(r['sub_gp'])}({r['sub_gp'] / r['fee']:.0%}) "
              f"이익 합 {won(r['gp'])} | CAC {won(r['cac'])} | "
              f"LTV/CAC(4%) {r['gp'] / 0.04 / r['cac']:.1f}배")

    print("\n== 가중 평균 (65:25:10)")
    base = blended()
    print(f"고객당 월 매출 {won(base['arpu'])} (구독 {won(base['sub_arpu'])} + 클릭 "
          f"{won(base['arpu'] - base['sub_arpu'])})")
    print(f"고객당 월 이익 {won(base['gp'])} ({base['gp'] / base['arpu']:.1%})  CAC {won(base['cac'])}")
    for churn in (0.04, 0.06):
        for clicks_on in (True, False):
            b = blended(clicks_on, churn)
            print(f"이탈 {churn:.0%} 클릭 {'포함' if clicks_on else '0'}: LTV {won(b['ltv'])} "
                  f"LTV/CAC {b['ltv_cac']:.1f}배 회수 {b['payback']:.1f}개월")
    for churn in (0.04, 0.06):
        b = blended(True, churn, cac_override={n: 2 * tier_numbers(n)["cac"] for n in TIERS})
        print(f"CAC 2배, 이탈 {churn:.0%}, 클릭 포함: LTV/CAC {b['ltv_cac']:.1f}배")
    print(f"기존 판처럼 이익률을 65%로 깎으면(이탈 4%): "
          f"{base['arpu'] * 0.65 / 0.04 / base['cac']:.1f}배")
    print("클릭이 아주 많은 셀러(월 6,000번): "
          f"라이트 {won(199_000 + min((6_000 - 1_000) * 50, 199_000))} "
          f"vs 프리미엄 {won(399_000 + min((6_000 - 3_000) * 30, 399_000))}")
    b = blended(False, 0.06, cac_override={"베이직": 500_000})
    print(f"가장 나쁘게(이탈 6%, 클릭 0, 베이직도 전부 현장 영업): LTV/CAC {b['ltv_cac']:.1f}배")
    b = blended(True, 0.04, shares={"베이직": 0.87, "라이트": 0.10, "프리미엄": 0.03})
    print(f"라이트 10% · 프리미엄 3%로 떨어지면(이탈 4%, 클릭 포함): 고객당 월 매출 {won(b['arpu'])} "
          f"LTV/CAC {b['ltv_cac']:.1f}배")

    print("\n== 프리미엄 근거: 라이트에 추가 요금을 붙여 같은 양을 쓰면")
    extra = 6 * 3_000 + 12 * 5_000 + 200 * 500 + 2_000 * 50
    print(f"영상 6시간 18,000 + 템플릿 롱폼 12편 60,000 + 전화 200통 100,000 + 클릭 2,000번 100,000 "
          f"= {won(extra)} → 합 {won(199_000 + extra)}")

    print("\n== 기존(2.9만 · 4.9만 · 19.9만, 30:35:35) 비교")
    old_arpu = 0.30 * 29_000 + 0.35 * 49_000 + 0.35 * 199_000
    print(f"기존 고객당 월 매출 {won(old_arpu)}")

    print("\n== 3년 매출 · 시장 규모 (고객당 월 매출 × 12)")
    a_all, a_sub = base["arpu"] * 12, base["sub_arpu"] * 12
    for label, n in (("보수", 350), ("기본", 1_000), ("낙관", 2_400)):
        print(f"3년차 {label} {n:,}곳: ARR {eok(n * a_all)} (구독만 {eok(n * a_sub)})")
    print(f"TAM 70.2만 명: {eok(702_000 * a_all)} (구독만 {eok(702_000 * a_sub)})")
    print(f"SAM 14.0만 명: {eok(140_000 * a_all)}  SOM 1,000곳 = SAM의 {1_000 / 140_000:.1%}")
    usd = base["arpu"] / FX
    print(f"미국 계산 기준: 월 ${usd:,.0f}")
    print(f"미국 TAM 88만: ${880_000 * usd * 12 / 1e8:,.2f}억 달러 ({eok(880_000 * usd * 12 * FX)})")
    print(f"미국 SAM 21.5만: ${215_000 * usd * 12 / 1e8:,.2f}억 달러 ({eok(215_000 * usd * 12 * FX)})")
    print(f"미국 SOM 2,150곳: ${2_150 * usd * 12 / 1e4:,.0f}만 달러 ({eok(2_150 * usd * 12 * FX)})")
