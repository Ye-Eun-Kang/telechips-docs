from PIL import Image
import os
import re
from urllib.parse import quote, unquote

# 사용자 설정
GITHUB_IMAGE_BASE = "https://ye-eun-kang.github.io/documentimage/"  # GitHub Pages에 업로드된 이미지 경로 베이스
LOCAL_IMAGE_ROOT = "C:/Users/ye.kang/Desktop/YE/15. web-base documentation/Github/documentimage/"  # 로컬 이미지 루트 경로
input_file = "TCC803x Android 12 SDK-Getting Started.mdx"  # 변환할 원본 마크다운 파일
output_file = input_file.replace(".md", ".mdx")  # 출력 파일 (.mdx로 저장)

# [1] 이미지 링크를 GitHub URL로 변환
def convert_all_image_links(content):
    # 마크다운 이미지 링크 패턴 탐색
    pattern = r'!\[[^\]]*?\]\(([^)]+?\.(?:png|jpg|jpeg|svg))\)'
    def replacer(match):
        raw_path = match.group(1).replace("\\", "/")
        if "documentimage" not in raw_path.lower():
            return match.group(0)
        try:
            # documentimage 경로 이후 상대 경로 추출
            idx = raw_path.lower().index("documentimage")
            relative_path = raw_path[idx + len("documentimage") + 1:]
            decoded = unquote(relative_path)
            encoded = quote(decoded)  # URL 인코딩
            return f"![]({GITHUB_IMAGE_BASE}{encoded})"
        except Exception:
            return match.group(0)
    return re.sub(pattern, replacer, content, flags=re.IGNORECASE)

# [2] 이메일과 URL 마크다운 형식으로 변환
def convert_email_and_url(content):
    # <[링크 텍스트](url)> → [링크 텍스트](url)
    content = re.sub(r'<(\[[^\]]+\]\([^)]+\))>', r'\1', content)
    # email 텍스트 → mailto 링크
    content = re.sub(r'(?<!\()(?<!\[)(?<!mailto:)(\b[\w\.-]+@[\w\.-]+\.\w{2,}\b)', r'[\1](mailto:\1)', content)
    # <http(s)://url> → [url](url)
    content = re.sub(r'<(https?://[^\s>]+)>', r'[\1](\1)', content)
    return content

# [3] </table> 이후에 빈 줄 삽입 (마크다운 렌더링 호환)
def ensure_blank_line_after_table(content):
    lines = content.splitlines()
    fixed = []
    for i, line in enumerate(lines):
        fixed.append(line)
        if line.strip().lower() == "</table>":
            # 다음 줄이 없거나 빈 줄이 아닌 경우, 빈 줄 추가
            if i + 1 == len(lines) or lines[i + 1].strip() != "":
                fixed.append("")
    return "\n".join(fixed)

# [4] 이미지 비율에 따라 width 퍼센트 자동 설정
def get_image_width_tag(path_from_docimage_root):
    local_path = os.path.join(LOCAL_IMAGE_ROOT, path_from_docimage_root.replace("/", os.sep))
    if not os.path.isfile(local_path):
        return 'width="45%"'  # 기본값
    try:
        with Image.open(local_path) as img:
            w, h = img.size
            ratio = w / h
            if ratio > 1.6:     # 가로형
                return 'width="90%"'
            elif ratio < 0.8:   # 세로형
                return 'width="30%"'
            else:               # 정사각형 또는 일반
                return 'width="45%"'
    except:
        return 'width="45%"'

# [5] 마크다운 이미지 → <img> 태그로 변환 + 가운데 정렬 + width 지정
def center_resize_images_outside_tables(content):
    # 테이블 블록 찾기 및 임시 치환
    table_blocks = re.findall(r"<table[\s\S]*?</table>", content, re.IGNORECASE)
    placeholders = {f"__TABLE_PLACEHOLDER_{i}__": block for i, block in enumerate(table_blocks)}
    for key, block in placeholders.items():
        content = content.replace(block, key)

    # 이미지 태그 변환 함수 정의
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
            return f'<p align="center"><img src="{GITHUB_IMAGE_BASE}{encoded}" {width} /></p>'
        except:
            return match.group(0)

    # 이미지 태그 변환 실행
    content = re.sub(r'!\[\]\(([^)]+?\.(?:png|jpg|jpeg|svg))\)', image_replacer, content)

    # 테이블 블록 복원
    for key, block in placeholders.items():
        content = content.replace(key, block)
    return content

# [6] Typora 스타일 알림(> [!NOTE] 등)을 <Admonition> MDX 컴포넌트로 변환
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
            # 이전 알림 블록 닫기
            if inside:
                converted.append(f'<Admonition type="{type_}" title="{type_.capitalize()}">')
                converted.extend(buffer)
                converted.append('</Admonition>\n')
            # 새 알림 블록 시작
            inside = True
            type_ = admonition_map.get(match.group(1).upper(), 'note')
            buffer = []
            continue

        if inside:
            if line.strip().startswith('>'):
                buffer.append(line.strip()[1:].strip())
            else:
                # 알림 블록 종료
                converted.append(f'<Admonition type="{type_}" title="{type_.capitalize()}">')
                converted.extend(buffer)
                converted.append('</Admonition>\n')
                inside = False
                converted.append(line)
        else:
            converted.append(line)

    # 파일 끝에서 열려 있던 블록 처리
    if inside:
        converted.append(f'<Admonition type="{type_}" title="{type_.capitalize()}">')
        converted.extend(buffer)
        converted.append('</Admonition>\n')

    result = "\n".join(converted)
    # import문 추가
    if '<Admonition' in result and 'import Admonition' not in result:
        result = 'import Admonition from \'@theme/Admonition\';\n\n' + result
    return result

# [7] 실행: 파일 읽기 → 변환 → 저장
if os.path.exists(input_file):
    with open(input_file, "r", encoding="utf-8") as f:
        content = f.read()

    # 변환 단계 순서대로 적용
    converted = convert_all_image_links(content)
    converted = convert_email_and_url(converted)
    converted = ensure_blank_line_after_table(converted)
    converted = center_resize_images_outside_tables(converted)
    converted = convert_typora_alerts_to_mdx(converted)

    # 결과 저장
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(converted)

    print(f"✅ 전체 변환 완료: {output_file}")
else:
    print(f"❌ 파일을 찾을 수 없습니다: {input_file}")
