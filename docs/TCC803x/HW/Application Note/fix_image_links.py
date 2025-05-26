import re

def convert_email_and_url(content):
    # 이메일 패턴
    content = re.sub(
        r'(?<!\()(?<!\[)(?<!mailto:)(\b[\w\.-]+@[\w\.-]+\.\w{2,}\b)',
        r'[\1](mailto:\1)',
        content
    )

    # URL (꺾쇠 괄호 내) 패턴
    content = re.sub(
        r'<(https?://[^\s>]+)>',
        r'[\1](\1)',
        content
    )

    return content

# 파일명 설정
input_file = "TCC803x Hardware Application Note for eMMC.md"
output_file = "TCC803x Hardware Application Note for eMMC-fixed.md"

# 변환 실행
with open(input_file, "r", encoding="utf-8") as f:
    content = f.read()

converted = convert_email_and_url(content)

with open(output_file, "w", encoding="utf-8") as f:
    f.write(converted)

print(f"\이메일과 링크 변환 완료: {output_file}")
