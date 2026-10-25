"""앵콜 피치덱: 넘침 검사 + 쪽 그림 + PDF.

python -I -X utf8 build_deck.py          # 검사 + 그림 + PDF
python -I -X utf8 build_deck.py check    # 검사만
"""
import json
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
SRC = HERE / "앵콜 피치덱.html"
PDF = HERE / "앵콜 피치덱.pdf"
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
FOOT_TOP = 1080 - 36 - round(1728 * 200 / 3412)  # 로고 띠 윗선 = 943

CHECK_JS = r"""
<script>
window.addEventListener('load', () => setTimeout(() => {
  const out = [];
  document.querySelectorAll('section.s').forEach((s, si) => {
    const base = s.getBoundingClientRect();
    const items = [...s.querySelectorAll('[data-fit]')].map(el => {
      const r = el.getBoundingClientRect();
      return {name: el.dataset.fit, top: Math.round(r.top - base.top), bottom: Math.round(r.bottom - base.top),
              left: Math.round(r.left - base.left), right: Math.round(r.right - base.left),
              sh: el.scrollHeight, ch: el.clientHeight, sw: el.scrollWidth, cw: el.clientWidth};
    });
    out.push({slide: si + 1, items});
  });
  const pre = document.createElement('pre');
  pre.id = 'fitjson';
  pre.textContent = JSON.stringify(out);
  document.body.appendChild(pre);
}, 1500));
</script>
"""


def run_chrome(args):
    return subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                           "--force-device-scale-factor=1", *args],
                          capture_output=True, text=True, encoding="utf-8", timeout=120)


def check():
    tmp = HERE / "_check.html"
    tmp.write_text(SRC.read_text(encoding="utf-8").replace("</body>", CHECK_JS + "</body>"), encoding="utf-8")
    try:
        r = run_chrome(["--virtual-time-budget=8000", "--window-size=1920,1080", "--dump-dom", tmp.as_uri()])
    finally:
        tmp.unlink(missing_ok=True)
    m = re.search(r'<pre id="fitjson">(.*?)</pre>', r.stdout, re.S)
    if not m:
        print("검사 결과 없음", r.stderr[-500:])
        return 1
    data = json.loads(m.group(1).replace("&quot;", '"').replace("&amp;", "&"))
    bad = 0
    count = 0
    for sl in data:
        for it in sl["items"]:
            count += 1
            probs = []
            if it["sh"] > it["ch"] + 1:
                probs.append(f"세로 넘침 {it['sh'] - it['ch']}px")
            if it["sw"] > it["cw"] + 1:
                probs.append(f"가로 넘침 {it['sw'] - it['cw']}px")
            if it["bottom"] > FOOT_TOP - 4:
                probs.append(f"로고 띠 침범 (아래 {it['bottom']} > {FOOT_TOP - 4})")
            if it["right"] > 1920 - 90:
                probs.append(f"오른쪽 여백 침범 ({it['right']})")
            flag = "넘침 " + ", ".join(probs) if probs else "ok"
            bad += bool(probs)
            print(f"{sl['slide']}장 {it['name']:<10} 위 {it['top']:>4} 아래 {it['bottom']:>4}  {flag}")
        # 겹침: 같은 쪽의 data-fit 상자끼리 (포함 관계는 뺀다)
        its = sl["items"]
        for i, a in enumerate(its):
            for b in its[i + 1:]:
                inside = (a["top"] <= b["top"] and a["bottom"] >= b["bottom"] and a["left"] <= b["left"] and a["right"] >= b["right"]) or \
                         (b["top"] <= a["top"] and b["bottom"] >= a["bottom"] and b["left"] <= a["left"] and b["right"] >= a["right"])
                if inside:
                    continue
                if a["top"] < b["bottom"] and b["top"] < a["bottom"] and a["left"] < b["right"] and b["left"] < a["right"]:
                    bad += 1
                    print(f"{sl['slide']}장 겹침: {a['name']} ↔ {b['name']}")
    print(f"상자 {count}개 검사, 문제 {bad}개")
    if count < 10:  # 검사할 상자가 없어서 통과하는 일을 막는다
        print("검사한 상자가 너무 적음")
        return 1
    return 1 if bad else 0


def shots():
    for n in (1, 2):
        out = HERE / f"미리보기_{n}장.png"
        run_chrome(["--virtual-time-budget=8000", "--window-size=1920,1080", f"--screenshot={out}", SRC.as_uri() + f"#{n}"])
        print("그림", out.name, out.exists())


def pdf():
    run_chrome(["--virtual-time-budget=8000", "--no-pdf-header-footer", f"--print-to-pdf={PDF}", SRC.as_uri()])
    data = PDF.read_bytes()
    pages = len(re.findall(rb"/Type\s*/Page[^s]", data))
    print("PDF", PDF.name, len(data), "bytes", pages, "쪽")
    return 0 if pages == 2 else 1


if __name__ == "__main__":
    rc = check()
    if len(sys.argv) > 1 and sys.argv[1] == "check":
        sys.exit(rc)
    shots()
    rc |= pdf()
    sys.exit(rc)
