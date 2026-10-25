"""트라가티제 결선 10분 — Drive 템플릿 「결선 10분 B 네이비 신뢰」(PPTX 내보내기)에 내용을 채운다.

사용:
  python build_final.py <템플릿.pptx> <출력.pptx>

원천: 제출 2장(바탕화면 트라가티제_2page.pdf, 16:51) · 기획서 Google 문서 5~13절(원천_기획서.txt)
      · 요금 개편 6절 새 판(../트라가티제 요금/6절 수익 구조 새 판.html, 16시).
글 내용은 아래 TEXT · RUNS · NOTES. 「|」 = 줄바꿈.
끝나면 줄마다 글자 폭을 재서 칸 폭의 90% 를 넘는 줄을 알린다(Google Slides 는 글자가 5% 안팎 넓다).
"""
import copy
import sys

from lxml import etree
from PIL import ImageFont
from pptx import Presentation
from pptx.oxml.ns import qn
from pptx.util import Pt

FONT_PATH = r"C:\Windows\Fonts\NotoSansKR-VF.ttf"
LIMIT = 0.90

# ---- 내용 -------------------------------------------------------------------
# 쪽 번호(1부터) → {도형 id: [문단 글, ...]}  문단 수는 템플릿과 같아야 한다.
TEXT = {
    1: {
        23: ["트라가티제"],
        24: ["One product video, sales worldwide."],
        25: ["제품 영상 하나로 해외 손님의 질문에 답하고 판매처까지 안내하는 AI"],
    },
    2: {
        35: ["해외 손님이 귀국하면 끊기는 매장 매출"],
        38: ["성수"],
        39: ["스몰 브랜드 대표", "성수 매장 · 직원 2~9명"],
        40: ["“온라인으로 살 수 있나요?”|일본 기념품점 조사 1위 질문"],
        42: ["재구매 문의를 받은 일본 기념품점 직원"],
        43: ["77%"],
        45: ["콘텐츠 만들 시간과 돈이 없음"],
        46: ["대행은 월 80만~180만 원|라이브 영상은 한 번 방송하면 끝"],
        48: ["외국어 질문에 답할 사람이 없음"],
        49: ["상세페이지와 상담이 한국어뿐|사이즈와 배송을 물을 곳이 없음"],
        51: ["관심이 구매로 이어지지 않음"],
        52: ["귀국한 손님은 어디서 살지 모름|2025년 의류 역직구 -9% (통계청)"],
    },
    3: {
        61: ["성수 외국인 소비 2배, 일본 판매 길도 열림"],
        64: ["70.2만 명"],
        65: ["국내 온라인 셀러 전체|연 1조 1,930억 원"],
        68: ["14.0만 명"],
        69: ["그중 영상을 쓰는 셀러 (가정)|연 2,380억 원"],
        72: ["3천~5천 곳"],
        73: ["성수 · 명동 · 홍대 · 한남에|매장을 둔 셀러"],
        75: ["2026년 7월 틱톡 코리아-JP 크로스보더 개통, 사업자등록증만으로 일본 판매"],
        76: ["출처: 국세청 생활업종 현황(2026.8), 서울시 성수 카드 소비(2026.1~8), 틱톡 공식 블로그"
             " · 금액은 고객당 월 14.2만 원 기준(가정)"],
    },
    4: {
        85: ["영상 하나로 해외 손님 응대와 구매 안내"],
        89: ["입력"],
        90: ["상품 정보나|라이브 영상을 올림", "예: 매장에서 찍은 1분 영상"],
        95: ["AI 처리"],
        96: ["Claude가 팔리는 장면을|골라 숏폼과 4개 언어 자막", "AI 상담원 티제가|셀러 정보 안에서만 답함"],
        101: ["결과"],
        102: ["상품별 숏폼 보관함과|판매처 구매 링크", "대표에게 한국어 요약 알림"],
        104: ["라이브 데모", "tragatize.log8.kr  ·  영상 올리기, 숏폼 3개, 티제에게 전화"],
    },
    5: {
        113: ["기본료와 클릭 요금, 첫 고객은 성수 매장"],
        115: ["가격 (주력 요금제 라이트)"],
        117: ["AI 전화 포함, 대행비의 1/4|클릭 1번 50원, 판매 수수료 0|베이직 4.9만, 프리미엄 39.9만"],
        118: ["LTV/CAC 약 5.7배 (가정)|3년 1,000곳 (기본 시나리오)"],
        121: ["성수 매장 현장 영업"],
        122: ["첫 7일 성수 매장 10곳 시범, QR과 숏폼 설치"],
        125: ["무료 체험 뒤 온라인 가입"],
        126: ["베이직은 온라인으로만 판매 (영업비를 못 건짐)"],
        129: ["틱톡샵 일본 입점 셀러"],
        130: ["7월 열린 크로스보더 셀러에게 일본어 숏폼과 전화"],
    },
    6: {
        139: ["커머스 현장 감각과 AI 개발력을 갖춘 팀"],
    },
    7: {
        174: ["해외 손님이 실제로 전화하고 사러 가는지 검증"],
        178: ["성수 매장 10곳 시범 시작|매장 QR과 숏폼 설치"],
        181: ["조회, 링크 클릭, 전화 수 측정|영상과 전화 원가 실측"],
        184: ["유료 전환 3곳 (목표)|라이트 19.9만 원 첫 청구"],
    },
}

# 한 문단 안에 서식이 다른 런이 여럿인 도형 → {(쪽, 도형 id): {(문단, 런): 글}}
RUNS = {
    (5, 116): {(0, 0): "19.9만", (0, 1): " 원 / 월"},
    (6, 165): {(0, 1): "영업 현장에서 본 문제를 하루 만에 동작하는 서비스로 만듦 (커밋 100개+)"},
    (7, 186): {(0, 1): "성수 · 명동 스몰 브랜드 소개, 틱톡샵 일본 진출 셀러 연결"},
}

# 글자 크기만 바꿀 도형 → {(쪽, 도형 id): pt}
SIZE = {
    (3, 64): 30, (3, 68): 30, (3, 72): 30,
    (5, 116, 0): 40,
}

# 발표 대본(발표자 노트). 템플릿 노트의 시간 배분을 따른다(합계 9분 10초).
NOTES = {
    1: "[10초] 안녕하세요, 트라가티제입니다. 제품 영상 하나로 해외 손님에게 파는 스몰 브랜드용 AI를 만들었습니다. 바로 고객 이야기로 가겠습니다.",
    2: "[1분] 성수에 매장을 둔 직원 2~9명짜리 스몰 브랜드 대표가 우리 고객입니다.\n"
       "외국인 손님이 매장에 와서 사 갑니다. 그런데 귀국하면 끝입니다. 일본 기념품점 조사에서 직원 77%가 재구매 문의를 받았고, 가장 많은 질문이 '온라인으로 살 수 있나요?'였습니다. 한국에서도 관광 손님의 구매가 수출로 이어지지 않아, 2025년 의류 역직구는 9% 줄었습니다(통계청).\n"
       "대표는 세 가지가 막혀 있습니다. 콘텐츠를 만들 시간과 돈이 없고(대행은 월 80만~180만 원), 외국어 질문에 답할 사람이 없고, 귀국한 손님은 어디서 사야 할지 모릅니다.\n"
       "(윤정민 님 커머스 현장 사례가 있으면 여기서 한 줄)",
    3: "[1분] 숫자는 세 개입니다. 국내 온라인 셀러 70.2만 명, 그중 영상을 쓰는 셀러 14만 명, 처음 들어갈 곳은 성수 · 명동 · 홍대 · 한남에 매장을 둔 셀러 3천~5천 곳입니다.\n"
       "왜 지금이냐면, 성수 외국인 카드 소비가 올해 1~8월 103.7% 늘었고, 7월에 틱톡 코리아-JP 크로스보더가 열려 사업자등록증만 있으면 일본에서 팔 수 있게 됐습니다.\n"
       "(질문 대비) 금액은 고객당 월 14.2만 원 기준입니다. 영상 쓰는 셀러 20%는 가정이고, 보수적 하한은 연매출 1억 원 이상 셀러 4.5만 명입니다.",
    4: "[3분] 이 화면에서 바로 라이브 데모로 넘어갑니다.\n"
       "1) 매장에서 찍은 1분 영상을 올립니다. 2) Claude가 팔리는 장면을 골라 숏폼 3개와 한국어 · 영어 · 일본어 · 중국어 자막을 만듭니다. 3) 심사위원께서 티제에게 전화해 영어나 일본어로 사이즈를 물어봐 주세요. 티제는 셀러가 넣은 정보 안에서만 답하고, 셀러의 판매처 링크를 보내고, 대표에게 한국어 요약을 남깁니다.\n"
       "데모가 멈추면 녹화 영상으로 바꿉니다.",
    5: "[1분 30초] 주력 요금제 라이트는 월 19.9만 원이고 AI 전화가 들어 있습니다. 콘텐츠 대행 월 80만 원의 1/4입니다. 판매 수수료는 없고, 우리 링크로 판매처에 간 손님이 포함 클릭을 넘으면 1번에 50원을 받습니다.\n"
       "첫 고객은 성수 매장 현장 영업으로 데려옵니다. 베이직(4.9만 원)은 무료 체험 뒤 온라인 가입으로만 팝니다. 현장 영업비를 베이직으로는 못 건지기 때문입니다. 세 번째 통로는 7월에 열린 틱톡샵 일본 입점 셀러입니다.\n"
       "(질문 대비) LTV/CAC 5.7배는 가정입니다. 이탈률 4%, 클릭 매출 포함 기준입니다. 클릭 매출을 빼고 이탈률 6%여도 3.0배입니다. 약한 곳은 베이직(2.9배)이라 온라인 가입으로만 팝니다.",
    6: "[1분] 커머스 영업 현장에서 이 문제를 직접 본 사람과, AI 에이전트를 만드는 개발자가 한 팀입니다. 그래서 오늘 하루 만에 실제 동작하는 서비스를 만들었습니다(17시 현황판 기준 커밋 100개 넘음).\n"
       "(회사 내부 정보는 말하지 않습니다)",
    7: "[1분 30초] 다음 4주에 증명할 것은 하나입니다. 해외 손님이 실제로 전화하고 사러 가는지입니다.\n"
       "1주에 성수 매장 10곳에 QR과 숏폼을 설치하고, 2~3주에 조회 · 링크 클릭 · 전화 수와 원가를 재고, 4주에 유료 전환 3곳을 목표로 합니다.\n"
       "(질문 대비: 필요한 돈이 얼마냐는 질문이 반드시 옵니다. 답할 금액은 팀이 미리 정해 둡니다)\n"
       "우리가 원하는 것은 성수 · 명동 스몰 브랜드 소개와 틱톡샵 일본 진출 셀러 연결입니다. 감사합니다.",
}

TITLE_IDS = {35, 61, 85, 113, 139}   # 자리 표시자 제목: 크기가 레이아웃에서 온다(28pt 굵게)


# ---- 도우미 -----------------------------------------------------------------
def shape_by_id(slide, sid):
    for sh in slide.shapes:
        if sh.shape_id == sid:
            return sh
    raise KeyError(sid)


def set_paras(shape, texts):
    """문단마다 첫 런의 서식을 살린 채 글만 바꾼다. 「|」 는 <a:br/> 줄바꿈."""
    paras = shape.text_frame.paragraphs
    assert len(paras) == len(texts), (shape.shape_id, len(paras), len(texts))
    for p, t in zip(paras, texts):
        runs = p.runs
        parts = t.split("|")
        runs[0].text = parts[0]
        for r in runs[1:]:
            r._r.getparent().remove(r._r)
        prev = runs[0]._r
        for part in parts[1:]:
            br = etree.Element(qn("a:br"))
            rpr = prev.find(qn("a:rPr"))
            if rpr is not None:
                br.append(copy.deepcopy(rpr))
            prev.addnext(br)
            nr = copy.deepcopy(runs[0]._r)
            nr.find(qn("a:t")).text = part
            br.addnext(nr)
            prev = nr


_fonts = {}


def font(size, bold):
    key = (size, bold)
    if key not in _fonts:
        f = ImageFont.truetype(FONT_PATH, int(size * 10))
        f.set_variation_by_axes([700 if bold else 400])
        _fonts[key] = f
    return _fonts[key]


def line_width(segments):
    """segments = [(글, 크기pt, 굵게)] → 폭(pt)."""
    return sum(font(s, b).getlength(t) / 10 for t, s, b in segments if t)


def fit_report(prs):
    bad = 0
    for si, slide in enumerate(prs.slides, 1):
        for sh in slide.shapes:
            if not sh.has_text_frame:
                continue
            bp = sh.text_frame._txBody.find(qn("a:bodyPr"))
            lins = int(bp.get("lIns", 91440)) / 12700
            rins = int(bp.get("rIns", 91440)) / 12700
            avail = sh.width / 12700 - lins - rins
            for p in sh.text_frame.paragraphs:
                line, lines = [], []
                for el in p._p:
                    if el.tag == qn("a:br"):
                        lines.append(line)
                        line = []
                    elif el.tag == qn("a:r"):
                        rpr = el.find(qn("a:rPr"))
                        sz = int(rpr.get("sz")) / 100 if rpr is not None and rpr.get("sz") else (
                            28 if sh.shape_id in TITLE_IDS else 10.5)
                        b = rpr is not None and rpr.get("b") == "1" or sh.shape_id in TITLE_IDS
                        line.append((el.find(qn("a:t")).text or "", sz, b))
                lines.append(line)
                for ln in lines:
                    w = line_width(ln)
                    txt = "".join(t for t, _, _ in ln)
                    if txt and w > LIMIT * avail:
                        bad += 1
                        print(f"  넘침 {si}쪽 id{sh.shape_id}: {w:.0f}/{avail:.0f}pt ({w / avail:.0%}) {txt}")
    print("넘치는 줄", bad)
    return bad


def main():
    tpl, out = sys.argv[1], sys.argv[2]
    prs = Presentation(tpl)
    slides = list(prs.slides)

    for si, shapes in TEXT.items():
        for sid, texts in shapes.items():
            set_paras(shape_by_id(slides[si - 1], sid), texts)
    for (si, sid), runs in RUNS.items():
        paras = shape_by_id(slides[si - 1], sid).text_frame.paragraphs
        for (pi, ri), t in runs.items():
            paras[pi].runs[ri].text = t
    for key, pt in SIZE.items():
        si, sid = key[0], key[1]
        sh = shape_by_id(slides[si - 1], sid)
        runs = sh.text_frame.paragraphs[0].runs
        targets = [runs[key[2]]] if len(key) == 3 else runs
        for r in targets:
            r.font.size = Pt(pt)
    for si, text in NOTES.items():
        slides[si - 1].notes_slide.notes_text_frame.text = text

    prs.save(out)
    print("saved", out)
    fit_report(prs)


if __name__ == "__main__":
    main()
