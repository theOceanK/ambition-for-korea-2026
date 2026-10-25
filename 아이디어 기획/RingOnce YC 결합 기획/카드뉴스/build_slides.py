"""카드뉴스 HTML 에서 잰 모양(geom/*.json)을 Google Slides batchUpdate 요청으로 바꾼다.

사용: python -I -X utf8 build_slides.py [번호 ...]
출력: slides/기획_NN_*.json = 요청 묶음 목록(묶음 하나 = update_presentation 한 번).
요청 안의 "__DEFAULT__" 는 새 프레젠테이션의 기본 슬라이드 id 로 바꿔 넣는다.
글꼴은 HTML 과 같은 Noto Sans KR 이라 줄바꿈이 거의 같다. 로고 띠는 Drive 의 footer-for-dark-slides.png 를 쓴다.
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
GEOM = HERE / "geom"
OUT = HERE / "slides"
EMU = 9144000 / 1920  # px 하나 = 4762.5 EMU (16:9 기본 판 720pt × 405pt)
PT = 720 / 1920  # px 하나 = 0.375pt
INSET_X, INSET_Y = 91440, 45720  # Slides 글상자 기본 안쪽 여백(0.1in · 0.05in)
FOOTER = "<대회 바닥글 그림 주소>"
NOTO_LINE = 1.448  # Noto Sans KR 기본 줄 높이(em)
CHUNK = 70


def rgb(h):
    h = h.lstrip("#")
    return {"red": round(int(h[0:2], 16) / 255, 3), "green": round(int(h[2:4], 16) / 255, 3),
            "blue": round(int(h[4:6], 16) / 255, 3)}


def props(page, x, y, w, h):
    return {"pageObjectId": page,
            "size": {"width": {"magnitude": round(w), "unit": "EMU"}, "height": {"magnitude": round(h), "unit": "EMU"}},
            "transform": {"scaleX": 1, "scaleY": 1, "translateX": round(x), "translateY": round(y), "unit": "EMU"}}


def requests_for(geom):
    reqs = [{"createSlide": {"objectId": f"slide{i + 1}", "slideLayoutReference": {"predefinedLayout": "BLANK"}}} for i in range(2)]
    reqs.append({"deleteObject": {"objectId": "__DEFAULT__"}})
    for i in range(2):
        reqs.append({"updatePageProperties": {"objectId": f"slide{i + 1}", "pageProperties": {
            "pageBackgroundFill": {"solidFill": {"color": {"rgbColor": rgb("#140c09")}}}}, "fields": "pageBackgroundFill"}})
    for n, g in enumerate(geom):
        page, oid = f"slide{g['slide'] + 1}", f"s{g['slide'] + 1}e{n:03d}"
        x, y, w, h = g["x"] * EMU, g["y"] * EMU, g["w"] * EMU, g["h"] * EMU
        if g["kind"] == "img":
            reqs.append({"createImage": {"objectId": oid, "url": FOOTER, "elementProperties": props(page, x, y, w, h)}})
        elif g["kind"] == "shape":
            reqs.append({"createShape": {"objectId": oid, "shapeType": "ROUND_RECTANGLE" if g["radius"] > 0 else "RECTANGLE",
                                         "elementProperties": props(page, x, y, w, h)}})
            sp = {"shapeBackgroundFill": {"solidFill": {"color": {"rgbColor": rgb(g["fill"])}}} if "fill" in g
                  else {"propertyState": "NOT_RENDERED"}}
            sp["outline"] = ({"outlineFill": {"solidFill": {"color": {"rgbColor": rgb(g["line"])}}},
                              "weight": {"magnitude": round(g["lineW"] * PT, 2), "unit": "PT"}} if "line" in g
                             else {"propertyState": "NOT_RENDERED"})
            reqs.append({"updateShapeProperties": {"objectId": oid, "shapeProperties": sp,
                                                   "fields": "shapeBackgroundFill,outline"}})
        else:
            one_line = g["h"] < g["size"] * 1.9
            grow = g["w"] * 0.15 * EMU if one_line else 0  # 한 줄짜리는 폭을 넉넉히(글꼴 차이로 줄이 꺾이지 않게)
            align = {"right": "END", "end": "END", "center": "CENTER"}.get(g["align"], "START")
            bx = x - INSET_X - (grow if align == "END" else grow / 2 if align == "CENTER" else 0)
            reqs.append({"createShape": {"objectId": oid, "shapeType": "TEXT_BOX",
                                         "elementProperties": props(page, bx, y - INSET_Y, w + 2 * INSET_X + grow, h + 2 * INSET_Y)}})
            reqs.append({"insertText": {"objectId": oid, "text": g["text"]}})
            reqs.append({"updateTextStyle": {"objectId": oid, "style": {
                "fontSize": {"magnitude": round(g["size"] * PT, 2), "unit": "PT"},
                "weightedFontFamily": {"fontFamily": "Noto Sans KR", "weight": {600: 700, 800: 900}.get(g["weight"], g["weight"])},  # Slides 는 600 · 800 을 한 단계 가늘게 그린다(시험판 실측)
                "foregroundColor": {"opaqueColor": {"rgbColor": rgb(g["color"])}}},
                "fields": "fontSize,weightedFontFamily,foregroundColor"}})
            ps = {"alignment": align}
            if g["lh"]:
                ps["lineSpacing"] = round(g["lh"] / (g["size"] * NOTO_LINE) * 100, 1)
            reqs.append({"updateParagraphStyle": {"objectId": oid, "style": ps,
                                                  "fields": ",".join(ps)}})
    return reqs


def main(argv):
    OUT.mkdir(exist_ok=True)
    files = sorted(GEOM.glob("기획_*.json"))
    if argv:
        files = [f for f in files if any(f.name.startswith(f"기획_{n.zfill(2)}") for n in argv)]
    for f in files:
        reqs = requests_for(json.loads(f.read_text(encoding="utf8")))
        chunks = [reqs[i:i + CHUNK] for i in range(0, len(reqs), CHUNK)]
        dst = OUT / f.name.replace("_카드뉴스", "")
        dst.write_text(json.dumps(chunks, ensure_ascii=False, separators=(",", ":")), encoding="utf8")
        print(f"{dst.name}: 요청 {len(reqs)}개 · 묶음 {len(chunks)} · {dst.stat().st_size:,} 바이트")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
