import re
from urllib.parse import quote, unquote

GITHUB_IMAGE_BASE = "https://ye-eun-kang.github.io/documentimage/"

def convert_all_image_links(content):
    pattern = r'!\[[^\]]*?\]\(([^)]+?\.(?:png|jpg|jpeg|svg))\)'
    
    def replacer(match):
        raw_path = match.group(1)
        path = raw_path.replace("\\", "/")

        if "documentimage" not in path.lower():
            return match.group(0)

        try:
            idx = path.lower().index("documentimage")
            relative_path = path[idx + len("documentimage") + 1:]

            # 이미 인코딩된 %20, %23 등을 다시 인코딩하지 않도록 처리
            decoded = unquote(relative_path)
            encoded = quote(decoded)
            return f"![]({GITHUB_IMAGE_BASE}{encoded})"
        except Exception:
            return match.group(0)

    return re.sub(pattern, replacer, content, flags=re.IGNORECASE)

def convert_email_and_url(content):
    # 이메일 변환: plain → [email](mailto:email)
    content = re.sub(
        r'(?<!\()(?<!\[)(?<!mailto:)(\b[\w\.-]+@[\w\.-]+\.\w{2,}\b)',
        r'[\1](mailto:\1)',
        content
    )

    # <https://...> → [https://...](https://...)
    content = re.sub(
        r'<(https?://[^\s>]+)>',
        r'[\1](\1)',
        content
    )
    return content

def ensure_blank_line_after_table(content):
    lines = content.splitlines()
    fixed_lines = []
    for i, line in enumerate(lines):
        fixed_lines.append(line)
        if line.strip().lower() == "</table>":
            if i + 1 < len(lines) and lines[i + 1].strip() != "":
                fixed_lines.append("")
            elif i + 1 == len(lines):
                fixed_lines.append("")
    return "\n".join(fixed_lines)

# 파일명 설정
input_file = "TCC803x Hardware Application Note for eMMC.md"
output_file = "TCC803x Hardware Application Note for eMMC-fixed.md"

# 실행
with open(input_file, "r", encoding="utf-8") as f:
    content = f.read()

converted = convert_all_image_links(content)
converted = convert_email_and_url(converted)
converted = ensure_blank_line_after_table(converted)

with open(output_file, "w", encoding="utf-8") as f:
    f.write(converted)

print(f" 변환 완료: {output_file}")
