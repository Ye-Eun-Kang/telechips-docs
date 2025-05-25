import re
from urllib.parse import quote

# GitHub Pages에서 사용하는 이미지 base URL
GITHUB_IMAGE_BASE = "https://ye-eun-kang.github.io/documentimage/"

# 이미지 경로 변환 함수
def convert_all_image_links(content):
    pattern = r'!\[[^\]]*?\]\(([^)]+?\.(?:png|jpg|jpeg|svg))\)'

    def replacer(match):
        raw_path = match.group(1)
        path = raw_path.replace("\\", "/")

        if "documentimage" not in path.lower():
            return match.group(0)  # 변환 제외

        try:
            idx = path.lower().index("documentimage")
            relative_path = path[idx + len("documentimage") + 1:]
            encoded = quote(relative_path, safe="/%")  # 이중 인코딩 방지
            return f"![]({GITHUB_IMAGE_BASE}{encoded})"
        except Exception:
            return match.group(0)

    return re.sub(pattern, replacer, content, flags=re.IGNORECASE)

# </table> 이후에 빈 줄 없으면 추가
def ensure_blank_line_after_table(content):
    lines = content.splitlines()
    fixed_lines = []
    for i, line in enumerate(lines):
        fixed_lines.append(line)
        if line.strip().lower() == "</table>":
            # 다음 줄이 비어있지 않으면 빈 줄 추가
            if i + 1 < len(lines) and lines[i + 1].strip() != "":
                fixed_lines.append("")
            elif i + 1 == len(lines):
                fixed_lines.append("")
    return "\n".join(fixed_lines)

# 파일 경로 설정
input_md = "TCC803x Hardware Application Note for eMMC.md"
output_md = "TCC803x Hardware Application Note for eMMC-fixed.md"

# 처리 실행
with open(input_md, "r", encoding="utf-8") as f:
    content = f.read()

converted = convert_all_image_links(content)
converted = ensure_blank_line_after_table(converted)

with open(output_md, "w", encoding="utf-8") as f:
    f.write(converted)

print(f"변환 완료: {output_md}")
