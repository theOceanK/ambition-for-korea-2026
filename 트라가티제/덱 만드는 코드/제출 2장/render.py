"""PDF 쪽을 PNG 로 뽑는다: python render.py <pdf> <접두사> [배율]"""
import sys
import pypdfium2 as pdfium

pdf = pdfium.PdfDocument(sys.argv[1])
scale = float(sys.argv[3]) if len(sys.argv) > 3 else 2.0
for i in range(len(pdf)):
    img = pdf[i].render(scale=scale).to_pil()
    out = f"{sys.argv[2]}_{i + 1}.png"
    img.save(out)
    print(out, img.size)
