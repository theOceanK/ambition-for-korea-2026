"""카드뉴스 꼴 2장 피치덱을 만든다: 카피 json → HTML → 헤드리스 Chrome PDF + 넘침 검사.

사용: python -I -X utf8 build_cards.py [번호 ...]   (번호 없으면 카피 폴더 전부)
틀은 대회 공식 발표자료 가이드(ambition-slide-kit\\GUIDE.md)를 따른다:
1920×1080 · 최대 2장 · 장마다 맨 아래 로고 띠(폭 90%) · 왼쪽 위 팀 이름 · 본문 28px 이상.
"""
import html
import json
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
COPY = HERE / "카피"
GEOM = HERE / "geom"
OUT = HERE.parent / "카드뉴스 피치덱"
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
TEAM = "김해청 · 김덕환 · 김성재 · 윤정민"

# 칸마다 글자 수 상한(띄어쓰기 포함). 카피 지시서와 같은 값이다.
LIMITS = {
    "s1.headline": 32, "s1.one": 44, "s1.market": 30, "s1.box": 34,
    "s2.headline": 30, "s2.phone": 30, "s2.num": 7, "s2.num_label": 18,
    "s2.how": 56, "s2.why": 56, "sources": 170,
}

CSS = """
@page{size:1920px 1080px;margin:0}
*{margin:0;padding:0;box-sizing:border-box;word-break:keep-all;overflow-wrap:break-word}
body{font-family:'Noto Sans KR',sans-serif;background:#555}
.s{width:1920px;height:1080px;position:relative;overflow:hidden;background:#140C09;color:#FFF4E8;page-break-after:always;margin:0 auto 40px}
@media print{body{background:none}.s{margin:0}}
.team{position:absolute;top:52px;left:96px;font-size:26px;font-weight:700;color:rgba(255,244,232,.6)}
.topic{position:absolute;top:52px;left:960px;right:96px;text-align:right;font-size:24px;font-weight:700;color:#FF6A2B}
.kick{font-size:30px;font-weight:800;color:#FF6A2B;flex-shrink:0}
.kick .ko{color:rgba(255,244,232,.55);font-weight:600;margin-left:14px}
.src{position:absolute;left:96px;right:96px;bottom:150px;height:56px;font-size:20px;line-height:1.4;color:rgba(255,244,232,.45);overflow:hidden}
.foot{position:absolute;left:5%;right:5%;bottom:32px}
.foot img{width:100%;display:block}
/* 1장 */
.p1{position:absolute;left:96px;right:96px;top:118px;bottom:224px;display:flex;flex-direction:column;overflow:hidden}
.p1>*{flex-shrink:0}
.h1{margin-top:16px;max-height:256px;font-size:100px;font-weight:900;line-height:1.2;overflow:hidden}
.one{margin-top:18px;max-height:64px;font-size:42px;font-weight:600;color:#E8C49A;overflow:hidden}
.mkt{margin-top:20px;align-self:flex-start;display:flex;align-items:center;height:60px;padding:0 28px;border-radius:30px;background:rgba(255,106,43,.16);font-size:30px;font-weight:700;color:#FFD7BF;white-space:nowrap;max-width:1728px;overflow:hidden}
.mkt b{color:#FF6A2B;margin-right:16px;font-size:24px;letter-spacing:.08em}
.row4{margin-top:auto;height:250px;display:flex;gap:28px}
.b4{flex:1;border-radius:24px;padding:22px 26px;background:rgba(255,244,232,.06);border:1px solid rgba(255,244,232,.16);overflow:hidden}
.b4 b{display:block;font-size:24px;color:#FF6A2B;letter-spacing:.06em;margin-bottom:8px}
.b4 p{font-size:33px;line-height:1.38;font-weight:600}
.b4.last{background:#FF6A2B;border-color:#FF6A2B}
.b4.last b{color:#140C09}.b4.last p{color:#140C09;font-weight:800}
/* 2장 */
.phone{position:absolute;left:96px;top:176px;width:540px;height:690px;border-radius:56px;border:3px solid rgba(255,244,232,.25);background:#21140E;padding:58px 30px 30px}
.phone .bar{font-size:24px;font-weight:700;color:rgba(255,244,232,.5);text-align:center;margin-bottom:22px}
.nt{border-radius:22px;background:#33221A;padding:18px 22px;margin-bottom:18px;height:172px;overflow:hidden}
.nt b{display:block;font-size:24px;color:#FF6A2B;margin-bottom:8px;letter-spacing:.04em}
.nt p{font-size:28px;line-height:1.4;font-weight:600}
.nt.re{background:#4A2414}
.right{position:absolute;left:700px;right:96px;top:176px;height:690px;display:flex;flex-direction:column;overflow:hidden}
.right>*{flex-shrink:0}
.h2{max-height:196px;font-size:76px;font-weight:900;line-height:1.2;overflow:hidden}
.nums{display:flex;gap:24px;margin-top:28px;height:190px}
.nm{flex:1;overflow:hidden}
.nm .bar4{height:4px;background:#FF6A2B;margin-bottom:16px}
.nm .n{font-size:84px;font-weight:900;line-height:1;color:#FFF4E8;white-space:nowrap}
.nm .l{font-size:28px;line-height:1.3;margin-top:14px;color:#E8C49A;font-weight:600}
.row2{display:flex;gap:24px;margin-top:auto;height:266px}
.b2{flex:1;border-radius:24px;padding:24px 28px;border:1px solid rgba(255,244,232,.18);overflow:hidden}
.b2 b{display:block;font-size:24px;color:#FF6A2B;letter-spacing:.06em;margin-bottom:12px}
.b2 p{font-size:30px;line-height:1.4}
"""

CHECK = """
<script>
document.fonts.ready.then(function(){
  var bad=[];
  document.querySelectorAll('[data-fit]').forEach(function(el){
    var mh=parseFloat(getComputedStyle(el).maxHeight);
    var lim=isNaN(mh)?el.clientHeight:Math.max(el.clientHeight,mh);
    if(el.scrollHeight>lim+1||el.scrollWidth>el.clientWidth+1){bad.push(el.getAttribute('data-fit'));}
  });
  document.title=bad.length?('OVERFLOW:'+bad.join(',')):'OVERFLOW:none';
  // Google Slides 로 옮길 모양: 칸(배경 · 테두리) · 글(글만 든 맨 끝 요소) · 그림. 좌표는 장 기준 px.
  function rgba(s){var m=s.match(/[\\d.]+/g)||[0,0,0,0];return [+m[0],+m[1],+m[2],m.length>3?+m[3]:1];}
  function blend(c,u){var a=c[3];return [c[0]*a+u[0]*(1-a),c[1]*a+u[1]*(1-a),c[2]*a+u[2]*(1-a),1];}
  function bgOf(el){if(!el||el===document.body){return [20,12,9,1];}var c=rgba(getComputedStyle(el).backgroundColor);return c[3]>0?blend(c,bgOf(el.parentElement)):bgOf(el.parentElement);}
  function hex(c){return '#'+c.slice(0,3).map(function(v){return ('0'+Math.round(v).toString(16)).slice(-2);}).join('');}
  var out=[];
  document.querySelectorAll('section.s').forEach(function(sec,si){
    var o=sec.getBoundingClientRect();
    sec.querySelectorAll('*').forEach(function(el){
      var cs=getComputedStyle(el),r=el.getBoundingClientRect();
      if(r.width<1||r.height<1){return;}
      var box={slide:si,x:r.left-o.left,y:r.top-o.top,w:r.width,h:r.height};
      if(el.tagName==='IMG'){box.kind='img';box.src=el.getAttribute('src');out.push(box);return;}
      var bg=rgba(cs.backgroundColor),bw=parseFloat(cs.borderTopWidth)||0;
      if(bg[3]>0||bw>0){
        var b=Object.assign({},box,{kind:'shape',radius:parseFloat(cs.borderTopLeftRadius)||0});
        if(bg[3]>0){b.fill=hex(bgOf(el));}
        if(bw>0){b.line=hex(blend(rgba(cs.borderTopColor),bgOf(el)));b.lineW=bw;}
        out.push(b);
      }
      var own=Array.prototype.some.call(el.childNodes,function(n){return n.nodeType===3&&n.textContent.trim();});
      if(own&&el.children.length===0){
        var lh=cs.lineHeight==='normal'?0:parseFloat(cs.lineHeight);
        out.push(Object.assign({},box,{kind:'text',text:el.innerText,size:parseFloat(cs.fontSize),weight:+cs.fontWeight,
          color:hex(blend(rgba(cs.color),bgOf(el))),align:cs.textAlign,lh:lh}));
      }
    });
  });
  var t=document.createElement('textarea');t.id='geom';t.style.display='none';t.textContent=JSON.stringify(out);document.body.appendChild(t);
});
</script>
"""


def e(s):
    return html.escape(s, quote=False)


def check_limits(c):
    probs = []

    def lim(key, text, where):
        n = len(text)
        if n > LIMITS[key]:
            probs.append(f"{where} {n}자 > {LIMITS[key]}")

    s1, s2 = c["s1"], c["s2"]
    lim("s1.headline", s1["headline"], "1장 제목")
    lim("s1.one", s1["one"], "1장 한 줄")
    lim("s1.market", s1["market"], "1장 시장")
    for i, b in enumerate(s1["boxes"]):
        lim("s1.box", b["t"], f"1장 칸{i + 1}")
    lim("s2.headline", s2["headline"], "2장 제목")
    for i, p in enumerate(s2["phone"]):
        lim("s2.phone", p["text"], f"2장 알림{i + 1}")
    for i, m in enumerate(s2["nums"]):
        lim("s2.num", m["n"], f"2장 숫자{i + 1}")
        lim("s2.num_label", m["l"], f"2장 숫자 설명{i + 1}")
    lim("s2.how", s2["how"], "2장 작동")
    lim("s2.why", s2["why"], "2장 왜 우리")
    lim("sources", c["sources"], "출처")
    if len(s1["boxes"]) != 4 or len(s2["phone"]) != 3 or len(s2["nums"]) != 3:
        probs.append("칸 수가 틀림(1장 칸 4 · 알림 3 · 숫자 3)")
    return probs


def render(c):
    s1, s2 = c["s1"], c["s2"]
    head = (f'<div class="team">{e(TEAM)}</div>'
            f'<div class="topic">{e(c["topic"])}</div>')
    foot = ('<div class="src" data-fit="출처">' + e(c["sources"]) + '</div>'
            '<div class="foot"><img src="../../ambition-slide-kit/footer-for-dark-slides.png" alt=""></div>')
    boxes = "".join(
        f'<div class="b4{" last" if i == 3 else ""}" data-fit="1장 칸{i + 1}"><b>{e(b["k"])}</b><p>{e(b["t"])}</p></div>'
        for i, b in enumerate(s1["boxes"]))
    page1 = (f'<section class="s">{head}'
             f'<div class="p1" data-fit="1장 전체"><div class="kick"><span>기획 {e(c["no"])} · {e(c["name"])}</span><span class="ko">{e(c["name_ko"])}</span></div>'
             f'<div class="h1" data-fit="1장 제목">{e(s1["headline"])}</div>'
             f'<div class="one" data-fit="1장 한 줄">{e(s1["one"])}</div>'
             f'<div class="mkt" data-fit="1장 시장"><b>TARGET</b><span>{e(s1["market"])}</span></div>'
             f'<div class="row4">{boxes}</div></div>{foot}</section>')
    notes = "".join(
        f'<div class="nt{" re" if i == 2 else ""}" data-fit="2장 알림{i + 1}"><b>{e(p["tag"])}</b><p>{e(p["text"])}</p></div>'
        for i, p in enumerate(s2["phone"]))
    nums = "".join(
        f'<div class="nm" data-fit="2장 숫자{i + 1}"><div class="bar4"></div><div class="n">{e(m["n"])}</div><div class="l">{e(m["l"])}</div></div>'
        for i, m in enumerate(s2["nums"]))
    page2 = (f'<section class="s">{head}'
             f'<div class="phone"><div class="bar">{e(s2.get("phone_bar", "시연 화면 · 예시"))}</div>{notes}</div>'
             f'<div class="right" data-fit="2장 오른쪽"><div class="h2" data-fit="2장 제목">{e(s2["headline"])}</div>'
             f'<div class="nums">{nums}</div>'
             f'<div class="row2"><div class="b2" data-fit="2장 작동"><b>HOW IT WORKS</b><p>{e(s2["how"])}</p></div>'
             f'<div class="b2" data-fit="2장 왜 우리"><b>WHY US · NEXT 7 DAYS</b><p>{e(s2["why"])}</p></div></div></div>'
             f'{foot}</section>')
    title = f'기획 {c["no"]} {c["name"]} 카드뉴스'
    return (f'<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>{e(title)}</title>'
            '<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable-dynamic-subset.min.css">'
            f'<style>{CSS}</style></head><body>{page1}{page2}{CHECK}</body></html>')


def chrome(*args):
    return subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-sandbox",
                           "--virtual-time-budget=15000", *args],
                          capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=180)


def build(path):
    c = json.loads(path.read_text(encoding="utf8"))
    probs = check_limits(c)
    stem = f'기획_{c["no"]}_{c["name"]}_카드뉴스'
    page = OUT / f"{stem}.html"
    page.write_text(render(c), encoding="utf8")
    dom = chrome("--dump-dom", page.as_uri()).stdout
    m = re.search(r"<title>(OVERFLOW:[^<]*)</title>", dom)
    overflow = m.group(1) if m else "OVERFLOW:unknown(검사 실패)"
    g = re.search(r'<textarea id="geom"[^>]*>(.*?)</textarea>', dom, re.S)
    GEOM.mkdir(exist_ok=True)
    if g:
        (GEOM / f"{stem}.json").write_text(html.unescape(g.group(1)), encoding="utf8")
    pdf = OUT / f"{stem}.pdf"
    chrome("--no-pdf-header-footer", f"--print-to-pdf={pdf}", page.as_uri())
    pages = len(re.findall(rb"/Type\s*/Page[^s]", pdf.read_bytes())) if pdf.exists() else 0
    ok = overflow == "OVERFLOW:none" and pages == 2 and not probs
    print(f'[{"통과" if ok else "확인"}] {stem} | {overflow} | PDF {pages}쪽'
          + (" | 글자 수: " + "; ".join(probs) if probs else ""))
    return ok


def main(argv):
    OUT.mkdir(parents=True, exist_ok=True)
    files = sorted(COPY.glob("기획_*.json"))
    if argv:
        files = [f for f in files if any(f.name.startswith(f"기획_{n.zfill(2)}") for n in argv)]
    if not files:
        print("카피 json 없음")
        return 1
    results = [build(f) for f in files]
    print(f"{len(results)}개 중 통과 {sum(results)}")
    return 0 if all(results) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
