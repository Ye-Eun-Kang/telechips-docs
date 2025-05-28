import os
import re
import sys
from urllib.parse import quote, unquote
from PIL import Image

# GitHub Pages 이미지 기본 주소
GITHUB_IMAGE_BASE = "https://ye-eun-kang.github.io/documentimage/"

# 로컬 이미지 경로 (비율 분석용)
LOCAL_IMAGE_ROOT = "C:/Users/ye.kang/Desktop/YE/15. web-base documentation/Github/documentimage/"

# 변환할 입력 파일 지정
if len(sys.argv) < 2:
    print("❌ 변환할 .md 파일명을 인자로 지정해주세요.")
    print("예: python convert_to_mdx.py '파일명.md'")
    sys.exit(1)

input_file = sys.argv[1]
output_file = input_file.replace(".md", ".mdx")

# 1. Markdown 이미지 경로 → GitHub 링크로
def convert_all_image_links(content):
    pattern = r'!\[[^\]]*?\]\(([^)]+?\.(?:png|jpg|jpeg|svg))\)'
    def replacer(match):
        raw_path = match.group(1).replace("\\", "/")
        if "documentimage" not in raw_path.lower():
            return match.group(0)
        try:
            idx = raw_path.lower().index("documentimage")
            relative_path = raw_path[idx + len("documentimage") + 1:]
            decoded = unquote(relative_path)
            encoded = quote(decoded)
            return f"![]({GITHUB_IMAGE_BASE}{encoded})"
        except:
            return match.group(0)
    return re.sub(pattern, replacer, content, flags=re.IGNORECASE)

# 2. 이메일 및 URL 자동 링크화
def convert_email_and_url(content):
    content = re.sub(r'<(\[[^\]]+\]\([^)]+\))>', r'\1', content)
    content = re.sub(r'(?<!\()(?<!\[)(?<!mailto:)(\b[\w\.-]+@[\w\.-]+\.\w{2,}\b)', r'[\1](mailto:\1)', content)
    content = re.sub(r'<(https?://[^\s>]+)>', r'[\1](\1)', content)
    return content

# 3. </table> 뒤에 공백 삽입
def ensure_blank_line_after_table(content):
    lines = content.splitlines()
    fixed = []
    for i, line in enumerate(lines):
        fixed.append(line)
        if line.strip().lower() == "</table>":
            if i + 1 == len(lines) or lines[i + 1].strip() != "":
                fixed.append("")
    return "\n".join(fixed)

# 4. 이미지 비율 기반 width 조정
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

# 5. 마크다운 이미지 → Zoom + 가운데 정렬 + width 자동
def center_resize_images_outside_tables(content):
    table_blocks = re.findall(r"<table[\s\S]*?</table>", content, re.IGNORECASE)
    placeholders = {f"__TABLE_PLACEHOLDER_{i}__": block for i, block in enumerate(table_blocks)}
    for key, block in placeholders.items():
        content = content.replace(block, key)

    def image_replacer(match):
        raw_url = match.group(1).replace("\\", "/")
        if "documentimage" not in raw_url.lower():
            return match.group(0)
        try:
            idx = raw_url.lower().index("documentimage")
            relative_path = raw_url[idx + len("documentimage") + 1:]
            decoded = unquote(relative_path)
            encoded = quote(decoded)
            width = get_image_width_tag(decoded)
            return (
                f'<div align="center">\n'
                f'  <Zoom>\n'
                f'    <img src="{GITHUB_IMAGE_BASE}{encoded}" {width} alt="" />\n'
                f'  </Zoom>\n'
                f'</div>'
            )
        except:
            return match.group(0)

    content = re.sub(r'!\[\]\(([^)]+?\.(?:png|jpg|jpeg|svg))\)', image_replacer, content)

    for key, block in placeholders.items():
        content = content.replace(key, block)

    return content

# 6. > [!NOTE] 스타일 → <Admonition> 변환
def convert_typora_alerts_to_mdx(content):
    admonition_map = {
        'IMPORTANT': 'important',
        'NOTE': 'note',
        'TIP': 'tip',
        'WARNING': 'warning',
        'CAUTION': 'caution'
    }
    lines = content.splitlines()
    converted, buffer = [], []
    inside = False
    type_ = ''

    for line in lines:
        match = re.match(r'>\s*\[!(\w+)\]', line)
        if match:
            if inside:
                converted.append(f'<Admonition type="{type_}" title="{type_.capitalize()}">')
                converted.extend(buffer)
                converted.append('</Admonition>\n')
            inside = True
            type_ = admonition_map.get(match.group(1).upper(), 'note')
            buffer = []
            continue
        if inside:
            if line.strip().startswith('>'):
                buffer.append(line.strip()[1:].strip())
            else:
                converted.append(f'<Admonition type="{type_}" title="{type_.capitalize()}">')
                converted.extend(buffer)
                converted.append('</Admonition>\n')
                inside = False
                converted.append(line)
        else:
            converted.append(line)

    if inside:
        converted.append(f'<Admonition type="{type_}" title="{type_.capitalize()}">')
        converted.extend(buffer)
        converted.append('</Admonition>\n')

    return "\n".join(converted)

# ================= 실행 =================
if os.path.exists(input_file):
    with open(input_file, "r", encoding="utf-8") as f:
        content = f.read()

    converted = convert_all_image_links(content)
    converted = convert_email_and_url(converted)
    converted = ensure_blank_line_after_table(converted)
    converted = center_resize_images_outside_tables(converted)
    converted = convert_typora_alerts_to_mdx(converted)

    # Zoom import 자동 삽입
    if '<Zoom>' in converted and "import Zoom from 'react-medium-image-zoom';" not in converted:
        converted = (
            "import Zoom from 'react-medium-image-zoom';\n"
            "import 'react-medium-image-zoom/dist/styles.css';\n\n"
        ) + converted

    # Admonition import 자동 삽입
    if '<Admonition' in converted and "import Admonition from '@theme/Admonition';" not in converted:
        converted = "import Admonition from '@theme/Admonition';\n\n" + converted

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(converted)

    print(f"✅ 변환 완료: {output_file}")
else:
    print(f"❌ 파일을 찾을 수 없습니다: {input_file}")
