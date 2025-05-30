import os
import re
import sys
from urllib.parse import quote, unquote
from PIL import Image

# GitHub Pages 이미지 base URL
GITHUB_IMAGE_BASE = "https://ye-eun-kang.github.io/documentimage/"
# 로컬에서 이미지 비율 분석에 사용할 루트 경로
LOCAL_IMAGE_ROOT = "C:/Users/ye.kang/Desktop/YE/15. web-base documentation/Github/documentimage/"

# 파일 인자 없을 시 종료
if len(sys.argv) < 2:
    print("❌ 변환할 .md 파일명을 인자로 지정해주세요.")
    sys.exit(1)

input_file = sys.argv[1]
output_file = input_file.replace(".md", ".mdx")

# Markdown의 ![]() 이미지 링크를 GitHub Pages URL로 바꿔줌
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

# <Zoom>...</Zoom> 감싸진 구버전 이미지 → <ZoomableImage />로 변환
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
            decoded = unquote(relative_path)
            encoded = quote(decoded)
            width = get_image_width_tag(decoded).replace('width=', '').replace('"', '')
            # style은 JSX 객체 문법으로 넣음 → Docusaurus에서만 인식됨
            return (
                f'  <ZoomableImage src="{GITHUB_IMAGE_BASE}{encoded}" width="{width}" />\n'
            )
        except:
            return zoom_block
    return re.sub(r'<Zoom>[\s\S]*?<img[^>]+>[\s\S]*?</Zoom>', replacer, content, flags=re.IGNORECASE)

# 이메일, URL 자동 링크 변환
def convert_email_and_url(content):
    """
    1. 중복 방지를 위해, 이미 링크 처리된 항목은 제외
    2. 순수 이메일 → mailto 링크로 변환
    3. <https://...> → [url](url) 링크로 변환
    4. 일반 도메인 → https:// 붙여 링크 변환
    """

    # 이미 링크 처리된 형식 제거
    content = re.sub(r'<(\[[^\]]+\]\([^)]+\))>', r'\1', content)

    # 이메일 변환
    content = re.sub(
        r'(?<!\[)(?<!mailto:)(?<!\]\()(?<!\]\(mailto:)(?<!mailto:)\b[\w\.-]+@[\w\.-]+\.\w{2,}\b(?!\))',
        lambda m: f"[{m.group(0)}](mailto:{m.group(0)})",
        content
    )

    # <https://url> 변환
    content = re.sub(r'<(https?://[^\s>]+)>', r'[\1](\1)', content)

    # 일반 도메인 변환 (www.example.com 등)
    domain_pattern = r'(?<![\w/])((?:https?://)?(?:www\.)?[\w.-]+\.\w{2,})(?![\w/])'
    def linkify_domain(match):
        url = match.group(1)
        if url.startswith("http"):
            return f"[{url}]({url})"
        else:
            return f"[{url}](https://{url})"
    content = re.sub(domain_pattern, linkify_domain, content)

    return content


# </table> 다음 줄바꿈 삽입
def ensure_blank_line_after_table(content):
    lines = content.splitlines()
    fixed = []
    for i, line in enumerate(lines):
        fixed.append(line)
        if line.strip().lower() == "</table>":
            if i + 1 == len(lines) or lines[i + 1].strip() != "":
                fixed.append("")
    return "\n".join(fixed)

# 이미지 너비 계산 (로컬 비율 기준으로 90% / 45% / 30% 중 하나)
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

# 일반 마크다운 이미지도 <ZoomableImage />로 변환
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
            width = get_image_width_tag(decoded).replace('width=', '').replace('"', '')
            return (
                f'  <ZoomableImage src="{GITHUB_IMAGE_BASE}{encoded}" width="{width}" />\n'
            )
        except:
            return match.group(0)

    content = re.sub(r'!\[\]\(([^)]+?\.(?:png|jpg|jpeg|svg))\)', image_replacer, content)

    for key, block in placeholders.items():
        content = content.replace(key, block)

    return content

# [!NOTE], [!WARNING] 등 → <Admonition>으로 변환
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


     # JSX 컴포넌트 자동 import 삽입 및 불필요한 import 제거
def update_imports(content):
    """
    JSX 컴포넌트가 사용된 경우:
    - 필요한 import만 삽입
    - 기존 중복 import 제거
    - 사용되지 않은 import 자동 제거
    """
    # JSX 컴포넌트와 import 경로 매핑
    component_import_map = {
        "ZoomableImage": "import ZoomableImage from '@site/src/components/ZoomableImage';",
        "Admonition": "import Admonition from '@theme/Admonition';",
        # 필요 시 여기 계속 확장 가능
    }

    # 줄 단위로 나누어 import와 body 구분
    lines = content.splitlines()
    existing_imports = []
    body_lines = []
    for line in lines:
        if line.strip().startswith("import "):
            existing_imports.append(line.strip())
        else:
            body_lines.append(line)

    body_text = "\n".join(body_lines)

    # 본문에 실제로 사용된 컴포넌트만 수집
    used_components = [
        component for component in component_import_map
        if f"<{component}" in body_text
    ]

    # 필요한 import만 재생성
    final_imports = [component_import_map[c] for c in used_components]

    # 기존 import 중에서도 중복되거나 사용되지 않은 항목 제거
    cleaned_body_lines = [
        line for line in body_lines
        if not any(imp in line for imp in component_import_map.values())
    ]

    # 최종 MDX 본문 재구성
    result = ""
    if final_imports:
        result += "\n".join(final_imports) + "\n\n"
    result += "\n".join(cleaned_body_lines).lstrip()
    return result



# 실행 메인
if os.path.exists(input_file):
    with open(input_file, "r", encoding="utf-8") as f:
        content = f.read()

    # 순서대로 변환 적용
    converted = convert_all_image_links(content)
    converted = convert_email_and_url(converted)
    converted = ensure_blank_line_after_table(converted)
    converted = replace_zoom_wrapped_images(converted)
    converted = center_resize_images_outside_tables(converted)
    converted = convert_typora_alerts_to_mdx(converted)
    converted = update_imports(converted)

    # 결과 저장
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(converted)

    print(f"✅ 변환 완료: {output_file}")
else:
    print(f"❌ 파일을 찾을 수 없습니다: {input_file}")
