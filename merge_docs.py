#!/usr/bin/env python3
"""
Скрипт для объединения всех .md файлов из папки docs в один красивый файл.
Структура как в cs-fundamentals/to-print/cs-fundamentals-full.md
"""

import os
import re
from pathlib import Path

def get_markdown_files(docs_dir):
    """Получает все .md файлы из папки docs и подпапок, сортирует по структуре."""
    md_files = []
    
    # Порядок обхода: сначала index.md, потом basics, diagrams, advanced, examples, guides, integration
    order = ['index.md', 'basics', 'diagrams', 'advanced', 'examples', 'guides', 'integration']
    
    docs_path = Path(docs_dir)
    
    # Сначала добавляем index.md если есть
    index_file = docs_path / 'index.md'
    if index_file.exists():
        md_files.append(index_file)
    
    # Затем проходим по подпапкам в нужном порядке
    for folder in order[1:]:  # пропускаем index.md
        folder_path = docs_path / folder
        if folder_path.exists() and folder_path.is_dir():
            # Сортируем файлы внутри папки
            sub_files = sorted(folder_path.rglob('*.md'))
            md_files.extend(sub_files)
    
    return md_files

def process_mermaid_blocks(content):
    """
    Обрабатывает mermaid блоки кода.
    Оставляет их как есть для рендеринга, но добавляет маркеры для красоты.
    """
    pattern = r'```mermaid\n(.*?)\n```'
    
    def replace_block(match):
        code = match.group(1)
        return f'```mermaid\n{code}\n```'
    
    return re.sub(pattern, replace_block, content, flags=re.DOTALL)

def merge_documents(docs_dir, output_file):
    """Объединяет все документы в один файл."""
    
    md_files = get_markdown_files(docs_dir)
    
    if not md_files:
        print(f"❌ Не найдено .md файлов в {docs_dir}")
        return
    
    print(f"📚 Найдено файлов: {len(md_files)}")
    
    combined_content = []
    docs_path = Path(docs_dir)
    
    for i, file_path in enumerate(md_files):
        print(f"  Обработка: {file_path.relative_to(docs_path.parent)}")
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Обрабатываем mermaid блоки
        content = process_mermaid_blocks(content)
        
        # Добавляем разделитель между файлами (кроме первого)
        if i > 0:
            combined_content.append('\n\n---\n\n')
        
        combined_content.append(content)
    
    # Записываем итоговый файл
    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(''.join(combined_content))
    
    print(f"\n✅ Создан файл: {output_file}")
    print(f"📦 Размер: {output_path.stat().st_size / 1024:.1f} KB")

if __name__ == "__main__":
    docs_dir = "/workspace/mermaid-guide/docs"
    output_file = "/workspace/mermaid-guide/to-print/mermaid-guide-complete.md"
    
    merge_documents(docs_dir, output_file)
