"""Slides 요청 묶음 하나를 꺼내 출력한다. 사용: python -I -X utf8 print_chunk.py <파일 이름> <묶음 번호> <기본 슬라이드 ID>

첫 줄 = 묶음 수, 둘째 줄 = 그 묶음의 JSON 배열(update_presentation 의 requests 로 그대로 보낸다).
"""
import json
import sys
from pathlib import Path

name, idx, default_id = sys.argv[1], int(sys.argv[2]), sys.argv[3]
path = Path(__file__).resolve().parent / "slides" / name
chunks = json.loads(path.read_text(encoding="utf8"))
print(f"묶음 수 {len(chunks)}")
print(json.dumps(chunks[idx], ensure_ascii=False, separators=(",", ":")).replace("__DEFAULT__", default_id))
