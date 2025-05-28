import os
import re

def convert_typora_alerts_to_mdx(content):
    # Typora alert 키워드 → Docusaurus Admonition type 매핑
    admonition_map = {
        'IMPORTANT': 'important',
        'NOTE': 'note',
        'TIP': 'tip',
        'WARNING': 'warning',
        'CAUTION': 'caution'
    }

    lines = content.splitlines()
    converted_lines = []
    inside_admonition = False
    admonition_type = ''
    buffer = []

    for line in lines:
        match = re.match(r'>\s*\[!(\w+)\]', line)
        if match:
            if inside_admonition:
                converted_lines.append(
                    f'<Admonition type="{admonition_type}" title="{admonition_type.capitalize()}">')
                converted_lines.extend(buffer)
                converted_lines.append('</Admonition>\n')
                buffer = []

            inside_admonition = True
            admonition_type = admonition_map.get(match.group(1).upper(), 'note')
            buffer = []
            continue

        if inside_admonition:
            if line.strip().startswith('>'):
                buffer.append(line.strip()[1:].strip())
            else:
                converted_lines.append(
                    f'<Admonition type="{admonition_type}" title="{admonition_type.capitalize()}">')
                converted_lines.extend(buffer)
                converted_lines.append('</Admonition>\n')
                inside_admonition = False
                converted_lines.append(line)
        else:
            converted_lines.append(line)

    if inside_admonition:
        converted_lines.append(
            f'<Admonition type="{admonition_type}" title="{admonition_type.capitalize()}">')
        converted_lines.extend(buffer)
        converted_lines.append('</Admonition>\n')

    converted = "\n".join(converted_lines)

    # JSX import 문 자동 추가
    if '<Admonition' in converted and 'import Admonition' not in converted:
        converted = 'import Admonition from \'@theme/Admonition\';\n\n' + converted

    return converted

# === 실행 대상 설정 ===
input_file = "TCC803x Android 12 SDK-Getting Started.md"   # 원본 파일명
output_file = input_file.replace(".md", ".mdx")            # 변환된 파일명

# === 변환 실행 ===
if os.path.exists(input_file):
    with open(input_file, "r", encoding="utf-8") as f:
        content = f.read()

    converted_content = convert_typora_alerts_to_mdx(content)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(converted_content)

    print(f" 변환 완료: {output_file}")
else:
    print(f"❌ 파일을 찾을 수 없습니다: {input_file}")
