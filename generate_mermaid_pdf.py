#!/usr/bin/env python3
"""
Генератор PDF из Markdown для Mermaid Guide.
Адаптированная версия скрипта из cs-fundamentals.
"""

import os
import sys
import re
import subprocess
from weasyprint import HTML, CSS

def get_font_paths():
    """Возвращает пути к шрифтам в зависимости от ОС."""
    paths = {
        'regular': '/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf',
        'bold': '/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf',
        'italic': '/usr/share/fonts/truetype/liberation/LiberationSans-Italic.ttf',
        'mono': '/usr/share/fonts/truetype/liberation/LiberationMono-Regular.ttf'
    }

    for key, path in list(paths.items()):
        if not os.path.exists(path):
            alt_paths = [
                f'/usr/share/fonts/{path.split("/")[-2]}/{path.split("/")[-1]}',
                f'/usr/local/share/fonts/{path.split("/")[-1]}',
                os.path.join(os.path.dirname(__file__), os.path.basename(path))
            ]
            found = False
            for alt in alt_paths:
                if os.path.exists(alt):
                    paths[key] = alt
                    found = True
                    break
            if not found:
                print(f"⚠️ Warning: Шрифт {key} не найден по пути {path}. Будет использован системный аналог.")

    return paths

def convert_md_to_html(md_content):
    """
    Конвертирует Markdown в HTML с сохранением структуры.
    Обрабатывает заголовки, код, списки, таблицы и mermaid блоки.
    """
    lines = md_content.split('\n')
    html_parts = []
    in_code_block = False
    code_lang = None
    in_mermaid_block = False
    in_table = False
    table_rows = []

    for line in lines:
        # Обработка блоков кода ```
        if line.startswith('```'):
            if in_code_block:
                if code_lang == 'mermaid':
                    # Закрываем mermaid блок специальным классом
                    html_parts.append('</code></pre>')
                    in_mermaid_block = False
                else:
                    html_parts.append('</code></pre>')
                in_code_block = False
                code_lang = None
            else:
                lang = line[3:].strip()
                code_lang = lang
                if lang == 'mermaid':
                    html_parts.append('<pre class="mermaid"><code>')
                    in_mermaid_block = True
                else:
                    html_parts.append('<pre><code>')
                in_code_block = True
            continue

        if in_code_block:
            safe_line = line.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
            html_parts.append(safe_line)
            continue

        # Пустые строки
        if not line.strip():
            if in_table:
                # Конец таблицы
                html_parts.append(build_table(table_rows))
                table_rows = []
                in_table = False
            else:
                html_parts.append('<div class="spacer"></div>')
            continue

        # Таблицы
        if '|' in line and line.strip().startswith('|') and line.strip().endswith('|'):
            if not in_table:
                in_table = True
            cells = [cell.strip() for cell in line.split('|')[1:-1]]
            if '---' in line:
                # Это разделитель таблицы, пропускаем
                continue
            table_rows.append(cells)
            continue

        # Заголовки
        if line.startswith('# '):
            text = process_inline(line[2:])
            html_parts.append(f'<h1>{text}</h1>')
        elif line.startswith('## '):
            text = process_inline(line[3:])
            html_parts.append(f'<h2>{text}</h2>')
        elif line.startswith('### '):
            text = process_inline(line[4:])
            html_parts.append(f'<h3>{text}</h3>')
        elif line.startswith('#### '):
            text = process_inline(line[5:])
            html_parts.append(f'<h4>{text}</h4>')
        # Списки
        elif line.strip().startswith('- '):
            text = process_inline(line.strip()[2:])
            html_parts.append(f'<div class="list-item">• {text}</div>')
        # Разделители
        elif line.startswith('---'):
            html_parts.append('<hr class="section-divider"/>')
        else:
            text = process_inline(line)
            if text.strip():
                html_parts.append(f'<p>{text}</p>')

    # Если таблица не закрыта
    if in_table and table_rows:
        html_parts.append(build_table(table_rows))

    return '\n'.join(html_parts)

def build_table(rows):
    """Строит HTML таблицу."""
    if not rows:
        return ''
    
    html = '<table>'
    for i, row in enumerate(rows):
        tag = 'th' if i == 0 else 'td'
        cells = ''.join(f'<{tag}>{process_inline(cell)}</{tag}>' for cell in row)
        html += f'<tr>{cells}</tr>'
    html += '</table>'
    return html

def process_inline(text):
    """Обрабатывает inline форматирование."""
    # Inline код
    def replace_code(match):
        content = match.group(1)
        content = content.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        return f'<code>{content}</code>'
    text = re.sub(r'`([^`]+)`', replace_code, text)

    # Жирный
    text = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', text)

    # Курсив
    text = re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)', r'<em>\1</em>', text)

    # Ссылки [text](url)
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', text)

    return text

def generate_pdf(input_path, output_path):
    """Генерирует PDF файл."""

    if not os.path.exists(input_path):
        print(f"❌ Ошибка: Файл '{input_path}' не найден!")
        sys.exit(1)

    print(f"📖 Чтение файла: {input_path}")
    with open(input_path, 'r', encoding='utf-8') as f:
        md_content = f.read()

    html_body = convert_md_to_html(md_content)

    font_paths = get_font_paths()

    css_styles = """
    @page {
        size: A4;
        margin: 2cm;
    }

    body {
        font-family: "Liberation Sans", sans-serif;
        font-size: 10pt;
        line-height: 1.3;
        color: #222;
        text-align: justify;
    }

    h1 {
        font-family: "Liberation Sans Bold", sans-serif;
        font-size: 14pt;
        text-align: center;
        color: #000;
        margin-top: 0;
        margin-bottom: 16pt;
        page-break-after: avoid;
    }

    h2 {
        font-family: "Liberation Sans Bold", sans-serif;
        font-size: 11pt;
        text-align: center;
        color: #333;
        margin-top: 14pt;
        margin-bottom: 10pt;
        page-break-after: avoid;
    }

    h3 {
        font-family: "Liberation Sans Bold", sans-serif;
        font-size: 10pt;
        text-align: left;
        color: #444;
        margin-top: 10pt;
        margin-bottom: 6pt;
        page-break-after: avoid;
    }

    p {
        margin: 3pt 0;
        text-align: left;
    }

    .spacer {
        height: 4pt;
        font-size: 0;
        line-height: 0;
    }

    pre {
        background-color: #f4f4f4;
        border: 1px solid #e0e0e0;
        border-radius: 3px;
        padding: 6pt;
        font-family: "Liberation Mono", monospace;
        font-size: 8.5pt;
        line-height: 1.25;
        color: #333;
        margin: 4pt 0;
        white-space: pre-wrap;
        word-wrap: break-word;
        page-break-inside: avoid;
    }

    pre.mermaid {
        background-color: #f9f9f9;
        border: 1px dashed #ccc;
        text-align: center;
    }

    code {
        font-family: "Liberation Mono", monospace;
        font-size: 8.5pt;
        background-color: #f9f9f9;
        padding: 0pt 2pt;
        border-radius: 2px;
        color: #d63384;
        border: 1px solid #eee;
    }

    pre code {
        background-color: transparent;
        padding: 0;
        border: none;
        color: inherit;
    }

    .list-item {
        margin: 2pt 0;
        padding-left: 4pt;
        text-align: left;
        line-height: 1.3;
    }

    hr.section-divider {
        border: none;
        border-top: 1px solid #ccc;
        margin: 12pt 0;
    }

    strong {
        font-family: "Liberation Sans Bold", sans-serif;
        font-weight: bold;
    }

    em {
        font-family: "Liberation Sans Italic", sans-serif;
        font-style: italic;
    }

    table {
        width: 100%;
        border-collapse: collapse;
        margin: 8pt 0;
    }

    th, td {
        border: 1px solid #ddd;
        padding: 6pt;
        text-align: left;
    }

    th {
        background-color: #f4f4f4;
        font-weight: bold;
    }

    a {
        color: #0066cc;
        text-decoration: none;
    }
    """

    full_html = f"""
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <title>Mermaid Guide Complete</title>
    </head>
    <body>
        {html_body}
    </body>
    </html>
    """

    print("🎨 Генерация PDF...")

    try:
        html_doc = HTML(string=full_html)
        css = CSS(string=css_styles)
        html_doc.write_pdf(output_path, stylesheets=[css])

        print(f"✅ Успешно создано: {output_path}")

        if os.path.exists(output_path):
            size_kb = os.path.getsize(output_path) / 1024.0
            print(f"📦 Размер: {size_kb:.1f} KB")

    except Exception as e:
        print(f"❌ Ошибка при генерации PDF: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) >= 3:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
    elif len(sys.argv) == 2:
        input_file = sys.argv[1]
        output_file = "output.pdf"
    else:
        input_file = "to-print/mermaid-guide-complete.md"
        output_file = "to-print/mermaid-guide-complete.pdf"

    generate_pdf(input_file, output_file)
