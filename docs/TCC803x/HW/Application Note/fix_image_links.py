import re
from urllib.parse import quote

GITHUB_IMAGE_BASE = "https://ye-eun-kang.github.io/documentimage/"

def convert_all_image_links(content):
    # 패턴: ![텍스트](C:\... 또는 ../... .png|.jpg 등)
    pattern = r'!\[[^\]]*?\]\(([^)]+?\.(?:png|jpg|jpeg|svg))\)'

    def replacer(match):
        raw_path = match.group(1)

        # 윈도우 경로 → 슬래시로
        path = raw_path.replace("\\", "/")

        if "documentimage" not in path.lower():
            return match.group(0)  # 변환 안 함

        try:
            idx = path.lower().index("documentimage")
            relative_path = path[idx + len("documentimage") + 1:]
            encoded = quote(relative_path)
            return f"![]({GITHUB_IMAGE_BASE}{encoded})"
        except Exception:
            return match.group(0)

    return re.sub(pattern, replacer, content, flags=re.IGNORECASE)

# 파일명 설정
input_md = "TCC803x Hardware Application Note for eMMC.md"
output_md = "TCC803x Hardware Application Note for eMMC-fixed.md"

# 실행
with open(input_md, "r", encoding="utf-8") as f:
    content = f.read()

converted = convert_all_image_links(content)

with open(output_md, "w", encoding="utf-8") as f:
    f.write(converted)

print(f"✅ 변환 완료: {output_md}")
