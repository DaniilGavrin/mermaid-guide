#!/bin/bash
set -e

OUTPUT_DIR="to-print"
COMBINED_MD="$OUTPUT_DIR/mermaid-guide-complete.md"
TEMP_HTML="$OUTPUT_DIR/temp.html"
PDF_FILE="$OUTPUT_DIR/mermaid-guide-complete.pdf"

mkdir -p "$OUTPUT_DIR"

# Создаем заголовок YAML для Pandoc/MkDocs
cat > "$COMBINED_MD" << 'EOF'
---
title: "Полное руководство по Mermaid.js"
author: "DaniilGavrin"
date: "`date +%Y-%m-%d`"
lang: ru
toc: true
toc-depth: 3
geometry: margin=2cm
header-includes: |
    <script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
    <script>mermaid.initialize({ startOnLoad: true });</script>
    <style>
        body { font-family: 'DejaVu Sans', sans-serif; }
        pre { background: #f4f4f4; padding: 10px; border-radius: 5px; }
        .mermaid { text-align: center; margin: 20px 0; }
        img { max-width: 100%; height: auto; }
    </style>
---

# Полное руководство по Mermaid.js

*Автоматически сгенерированная документация*

---

EOF

# Функция для добавления файлов с заголовками
add_section() {
    local title=$1
    echo "" >> "$COMBINED_MD"
    echo "# $title" >> "$COMBINED_MD"
    echo "" >> "$COMBINED_MD"
}

# Добавляем основные разделы
echo "📝 Сборка документации..."

# Basics
for f in docs/basics/*.md; do
    [ -f "$f" ] || continue
    echo "Adding $f"
    cat "$f" >> "$COMBINED_MD"
    echo "" >> "$COMBINED_MD"
    echo "---" >> "$COMBINED_MD"
done

# Diagrams
add_section "Типы диаграмм"
for f in docs/diagrams/*.md; do
    [ -f "$f" ] || continue
    echo "Adding $f"
    cat "$f" >> "$COMBINED_MD"
    echo "" >> "$COMBINED_MD"
    echo "---" >> "$COMBINED_MD"
done

# Advanced
add_section "Продвинутые техники"
for f in docs/advanced/*.md; do
    [ -f "$f" ] || continue
    echo "Adding $f"
    cat "$f" >> "$COMBINED_MD"
    echo "" >> "$COMBINED_MD"
    echo "---" >> "$COMBINED_MD"
done

# Examples
add_section "Примеры использования"
for f in docs/examples/*.md; do
    [ -f "$f" ] || continue
    echo "Adding $f"
    cat "$f" >> "$COMBINED_MD"
    echo "" >> "$COMBINED_MD"
    echo "---" >> "$COMBINED_MD"
done

# Integration
add_section "Интеграция"
for f in docs/integration/*.md; do
    [ -f "$f" ] || continue
    echo "Adding $f"
    cat "$f" >> "$COMBINED_MD"
    echo "" >> "$COMBINED_MD"
    echo "---" >> "$COMBINED_MD"
done

# Guides
add_section "Гайды по платформам"
for f in docs/guides/*.md; do
    [ -f "$f" ] || continue
    echo "Adding $f"
    cat "$f" >> "$COMBINED_MD"
    echo "" >> "$COMBINED_MD"
    echo "---" >> "$COMBINED_MD"
done

echo "✅ Markdown файл собран: $COMBINED_MD"

# Генерация HTML через mkdocs (чтобы отрендерить мермайды)
echo "🔄 Генерация HTML для рендеринга диаграмм..."
mkdocs build --clean --site-dir "$OUTPUT_DIR/site_html"

# Конвертация HTML в PDF через wkhtmltopdf
echo "🖨️ Генерация PDF..."
wkhtmltopdf --enable-local-file-access \
            --encoding utf-8 \
            --margin-top 20mm \
            --margin-bottom 20mm \
            --margin-left 15mm \
            --margin-right 15mm \
            --footer-center "[page] из [toPage]" \
            "$OUTPUT_DIR/site_html/index.html" \
            "$PDF_FILE"

echo "✅ PDF создан: $PDF_FILE"
echo "🎉 Готово!"
