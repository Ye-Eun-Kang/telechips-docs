import os
import re
import sys
from urllib.parse import quote, unquote
from PIL import Image

# GitHub Pages 이미지 base URL
GITHUB_IMAGE_BASE = "https://ye-eun-kang.github.io/documentimage/"
# 로컬 이미지 기준 경로
LOCAL_IMAGE_ROOT = "C:/Users/ye.kang/Desktop/YE/15. web-base documentation/Github/documentimage/"

# 파일 인자 확인
if len(sys.argv) < 2:
    print("❌ 변환할 .md 파일명을 인자로 지정해주세요.")
    sys.exit(1)

input_file = sys.argv[1]
output_file = input_file.replace(".md", ".mdx")

# 이미지 너비 자동 결정
def get_image_width_tag(path_from_docimage_root):
    local_path = os.path.join(LOCAL_IMAGE_ROOT, path_from_docimage_root.replace("/", os.sep))
    if not os.path.isfile(local_path):
        return 'width="45%"'
    try:
        with Image.open(local_path) as img:
            w, h = img.size
            ratio = w / h
            if ratio > 1.6:
                return 'width="90%"'
            elif ratio < 0.8:
                return 'width="30%"'
            else:
                return 'width="45%"'
    except:
        return 'width="45%"'

# Markdown 이미지 → ZoomableImage
def convert_markdown_images(content):
    pattern = r'!\[[^\]]*?\]\(([^)]+?(documentimage)[^)]*?\.(?:png|jpg|jpeg|svg))\)'
    def replacer(match):
        raw_path = match.group(1).replace("\\", "/")
        try:
            idx = raw_path.lower().index("documentimage/")
            relative_path = raw_path[idx + len("documentimage/"):]
            encoded = quote(unquote(relative_path))
            width = get_image_width_tag(relative_path).replace('width=', '').replace('"', '')
            return f'<ZoomableImage src="{GITHUB_IMAGE_BASE}{encoded}" width="{width}" />'
        except:
            return match.group(0)
    return re.sub(pattern, replacer, content, flags=re.IGNORECASE)

# <Zoom> → ZoomableImage
def replace_zoom_wrapped_images(content):
    def replacer(match):
        zoom_block = match.group(0)
        img_match = re.search(r'src="([^"]+)"', zoom_block)
        if not img_match:
            return zoom_block
        img_src = img_match.group(1)
        try:
            if "documentimage" not in img_src.lower():
                return zoom_block
            idx = img_src.lower().index("documentimage")
            relative_path = img_src[idx + len("documentimage") + 1:]
            encoded = quote(unquote(relative_path))
            width = get_image_width_tag(relative_path).replace('width=', '').replace('"', '')
            return f'<ZoomableImage src="{GITHUB_IMAGE_BASE}{encoded}" width="{width}" />'
        except:
            return zoom_block
    return re.sub(r'<Zoom>[\s\S]*?<img[^>]+>[\s\S]*?</Zoom>', replacer, content, flags=re.IGNORECASE)

# 이메일/URL/도메인 자동 링크 변환
def convert_email_and_url(content):
    skip_line_keywords = ["documentimage", "\\", "/", ".png", ".jpg", ".jpeg", ".svg"]
    def safe_replace(text):
        lines = text.splitlines()
        result = []
        for line in lines:
            if any(k in line for k in skip_line_keywords):
                result.append(line)
            else:
                line = re.sub(
                    r'(?<!\[)(?<!mailto:)(?<!\]\()(?!mailto:)\b[\w\.-]+@[\w\.-]+\.\w{2,}\b(?!\))',
                    lambda m: f"[{m.group(0)}](mailto:{m.group(0)})",
                    line
                )
                line = re.sub(r'<(https?://[^\s>]+)>', r'[\1](\1)', line)
                domain_pattern = r'\b((?:https?://|www\.)[\w.-]+\.\w{2,})\b'
                line = re.sub(domain_pattern, lambda m: f"[{m.group(1)}]({m.group(1)})", line)
                result.append(line)
        return "\n".join(result)
    return safe_replace(content)

# [!NOTE] → <Admonition> 변환
def convert_typora_admonitions(content):
    def repl(match):
        tag = match.group(1).strip().lower()
        body = match.group(2).strip()
        type_map = {
            "note": "note",
            "important": "important",
            "warning": "warning",
            "tip": "tip",
            "caution": "caution"
        }
        type_str = type_map.get(tag.lower(), "note")
        return f'<Admonition type="{type_str}">\n\n{body}\n\n</Admonition>'
    return re.sub(r'^\[!(NOTE|IMPORTANT|WARNING|TIP|CAUTION)\][ \t]*\n([\s\S]*?)(?=\n\s*\n|\Z)', repl, content, flags=re.MULTILINE | re.IGNORECASE)

# JSX import 자동 삽입 및 중복 제거
def update_imports(content):
    component_import_map = {
        "ZoomableImage": "import ZoomableImage from '@site/src/components/ZoomableImage';",
        "Admonition": "import Admonition from '@theme/Admonition';",
    }

    lines = content.splitlines()
    existing_imports = []
    body_lines = []
    for line in lines:
        if line.strip().startswith("import "):
            existing_imports.append(line.strip())
        else:
            body_lines.append(line)

    body_text = "\n".join(body_lines)
    used_components = [c for c in component_import_map if f"<{c}" in body_text]
    final_imports = [component_import_map[c] for c in used_components]
    final_imports = list(dict.fromkeys(final_imports))  # 중복 제거

    cleaned_body_lines = [line for line in body_lines if not any(imp in line for imp in component_import_map.values())]
    result = ""
    if final_imports:
        result += "\n".join(final_imports) + "\n\n"
    result += "\n".join(cleaned_body_lines).lstrip()
    return result

# 실행 시작
if os.path.exists(input_file):
    with open(input_file, "r", encoding="utf-8") as f:
        content = f.read()

    content = convert_markdown_images(content)
    content = replace_zoom_wrapped_images(content)
    content = convert_typora_admonitions(content)
    content = convert_email_and_url(content)
    content = update_imports(content)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"✅ 변환 완료: {output_file}")
else:
    print(f"❌ 파일을 찾을 수 없습니다: {input_file}")
