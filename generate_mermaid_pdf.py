#!/usr/bin/env python3
"""
Генератор PDF из Markdown для Mermaid Guide.
Адаптированная версия скрипта из cs-fundamentals с поддержкой Mermaid диаграмм.

Особенности:
- Серый фон у блоков кода
- Шрифты Liberation Sans/Mono
- Правильные отступы и разрывы страниц
- Mermaid блоки отображаются как код с подсветкой синтаксиса
"""

import os
import sys
import re
import subprocess
from weasyprint import HTML, CSS, fonts

FontConfiguration = fonts.FontConfiguration

def get_font_paths():
    """Возвращает пути к шрифтам."""
    paths = {
        'regular': '/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf',
        'bold': '/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf',
        'italic': '/usr/share/fonts/truetype/liberation/LiberationSans-Italic.ttf',
        'mono': '/usr/share/fonts/truetype/liberation/LiberationMono-Regular.ttf'
    }
    
    for key, path in list(paths.items()):
        if not os.path.exists(path):
            print(f"⚠️ Warning: Шрифт {key} не найден по пути {path}")
    
    return paths

def convert_md_to_html(md_content):
    """
    Конвертирует Markdown в HTML с поддержкой Mermaid блоков.
    """
    lines = md_content.split('\n')
    html_parts = []
    in_code_block = False
    code_lang = None
    in_mermaid_block = False
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Обработка начала блока кода ```mermaid или ```другой_язык или ```
        if line.startswith('```'):
            if in_code_block:
                # Конец блока кода
                if in_mermaid_block:
                    html_parts.append('</code></pre></div>')
                    in_mermaid_block = False
                else:
                    html_parts.append('</code></pre>')
                in_code_block = False
                code_lang = None
            else:
                # Начало блока кода
                lang_match = re.match(r'^```(\w*)', line)
                if lang_match:
                    code_lang = lang_match.group(1)
                    if code_lang == 'mermaid':
                        in_mermaid_block = True
                        html_parts.append('<div class="mermaid-block"><pre><code class="language-mermaid">')
                    else:
                        html_parts.append('<pre><code>')
                else:
                    html_parts.append('<pre><code>')
                in_code_block = True
            i += 1
            continue
        
        if in_code_block:
            # Экранирование спецсимволов HTML внутри кода
            safe_line = line.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
            html_parts.append(safe_line)
            i += 1
            continue
        
        # Пустые строки -> отступы
        if not line.strip():
            html_parts.append('<div class="spacer"></div>')
            i += 1
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
        elif line.startswith('##### '):
            text = process_inline(line[6:])
            html_parts.append(f'<h5>{text}</h5>')
        
        # Списки (маркированные)
        elif line.strip().startswith('- '):
            text = process_inline(line.strip()[2:])
            html_parts.append(f'<div class="list-item">• {text}</div>')
        elif re.match(r'^\d+\.\s+', line.strip()):
            text = re.sub(r'^\d+\.\s+', '', line.strip())
            text = process_inline(text)
            html_parts.append(f'<div class="list-item numbered">№ {text}</div>')
        
        # Разделители секций ---
        elif line.startswith('---'):
            html_parts.append('<hr class="section-divider"/>')
        
        # Таблицы - упрощенная обработка
        elif line.strip().startswith('|') and '|' in line:
            # Пропускаем строки таблиц, они будут обработаны отдельно если нужно
            # Для простоты пока оставляем как есть
            if '|---' not in line and '|--------' not in line:
                # Это содержимое таблицы, а не разделитель
                cells = [c.strip() for c in line.split('|') if c.strip()]
                if cells:
                    row_html = ' | '.join([process_inline(cell) for cell in cells])
                    html_parts.append(f'<div class="table-row">{row_html}</div>')
        else:
            # Обычный текст
            text = process_inline(line)
            if text.strip():
                html_parts.append(f'<p>{text}</p>')
        
        i += 1
    
    return '\n'.join(html_parts)

def process_inline(text):
    """Обрабатывает inline форматирование: жирный, курсив, код."""
    # Inline код `code` -> <code>code</code>
    def replace_code(match):
        content = match.group(1)
        content = content.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        return f'<code>{content}</code>'
    
    text = re.sub(r'`([^`]+)`', replace_code, text)
    
    # Жирный **text** -> <strong>text</strong>
    text = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', text)
    
    # Курсив *text* -> <em>text</em>
    text = re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)', r'<em>\1</em>', text)
    
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
    
    # CSS стили
    css_styles = """
    @page {
        size: A4;
        margin: 2cm;
        @bottom-right {
            content: none;
        }
    }
    
    @font-face {
        font-family: "Liberation Sans";
        src: url(file:///usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf);
    }
    @font-face {
        font-family: "Liberation Sans Bold";
        src: url(file:///usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf);
    }
    @font-face {
        font-family: "Liberation Sans Italic";
        src: url(file:///usr/share/fonts/truetype/liberation/LiberationSans-Italic.ttf);
    }
    @font-face {
        font-family: "Liberation Mono";
        src: url(file:///usr/share/fonts/truetype/liberation/LiberationMono-Regular.ttf);
    }
    
    body {
        font-family: "Liberation Sans", sans-serif;
        font-size: 10pt;
        line-height: 1.3;
        color: #222;
        text-align: justify;
        widows: 2;
        orphans: 2;
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
    
    /* Блоки кода - серый фон */
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
    
    /* Mermaid блоки - специальный стиль */
    .mermaid-block {
        background-color: #f8f9fa;
        border: 1px solid #dee2e6;
        border-left: 4px solid #6f42c1;
        border-radius: 3px;
        padding: 8pt;
        margin: 6pt 0;
        page-break-inside: avoid;
    }
    
    .mermaid-block pre {
        background-color: transparent;
        border: none;
        padding: 0;
        margin: 0;
        font-size: 8pt;
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
    
    .list-item.numbered {
        padding-left: 4pt;
    }
    
    .table-row {
        font-family: "Liberation Mono", monospace;
        font-size: 8.5pt;
        background-color: #fafafa;
        padding: 2pt 4pt;
        margin: 1pt 0;
        border: 1px solid #eee;
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
    
    font_config = FontConfiguration()
    css = CSS(string=css_styles, font_config=font_config)
    
    try:
        html_doc = HTML(string=full_html)
        html_doc.write_pdf(output_path, stylesheets=[css], font_config=font_config)
        
        print(f"✅ Успешно создано: {output_path}")
        
        # Статистика
        if os.path.exists(output_path):
            size_kb = os.path.getsize(output_path) / 1024.0
            print(f"📦 Размер: {size_kb:.1f} KB")
            
            try:
                result = subprocess.run(['pdfinfo', output_path], capture_output=True, text=True, timeout=5)
                for line in result.stdout.split('\n'):
                    if 'Pages' in line:
                        print(f"📄 {line}")
            except Exception:
                pass
    
    except Exception as e:
        print(f"❌ Ошибка при генерации PDF: {e}")
        import traceback
        traceback.print_exc()
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
