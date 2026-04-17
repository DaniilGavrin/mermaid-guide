# Интеграция с GitHub и GitLab

GitHub и GitLab автоматически рендерят диаграммы Mermaid в markdown-файлах, что делает их идеальными платформами для документации.

## GitHub

### Автоматический рендеринг

GitHub поддерживает Mermaid начиная с 2022 года. Диаграммы рендерятся автоматически в:
- README.md
- Файлах документации (.md)
- Issues и Pull Requests
- Wiki

**Пример:**
```mermaid
graph LR
    A[GitHub Markdown] --> B[Автоматический рендеринг]
    B --> C[SVG изображение]
```

### Использование в README

Просто добавьте код диаграммы в markdown:

````markdown
```mermaid
sequenceDiagram
    participant Dev as Разработчик
    participant GH as GitHub
    
    Dev->>GH: Push commit с .md файлом
    GH->>GH: Обработка markdown
    GH->>Dev: Отображение диаграммы
```
````

Результат:

```mermaid
sequenceDiagram
    participant Dev as Разработчик
    participant GH as GitHub
    
    Dev->>GH: Push commit с .md файлом
    GH->>GH: Обработка markdown
    GH->>Dev: Отображение диаграммы
```

### GitHub Actions для генерации

Для создания изображений из диаграмм:

```yaml
name: Generate Mermaid Diagrams

on: [push]

jobs:
  generate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18'
      
      - name: Install mermaid-cli
        run: npm install -g @mermaid-js/mermaid-cli
      
      - name: Generate diagrams
        run: |
          mmdc -i docs/diagram.mmd -o docs/diagram.png
          
      - name: Commit generated images
        run: |
          git config user.name "GitHub Actions"
          git config user.email "actions@github.com"
          git add docs/*.png
          git commit -m "Generate diagrams" || echo "No changes"
          git push
```

### Особенности GitHub

| Функция | Поддержка |
|---------|-----------|
| Рендеринг в README | ✅ Да |
| Рендеринг в Issues | ✅ Да |
| Рендеринг в PR | ✅ Да |
| Кастомные темы | ⚠️ Ограничено |
| Интерактивность | ❌ Нет |
| Экспорт в PNG/SVG | ⚠️ Через Actions |

## GitLab

### Автоматический рендеринг

GitLab также поддерживает Mermaid в markdown:

```mermaid
graph TD
    A[GitLab] --> B[Native Support]
    B --> C[Version 13.0+]
```

### Использование в GitLab

````markdown
```mermaid
classDiagram
    class Project {
        +String name
        +Array files
        +save()
    }
    class Repository {
        +clone()
        +push()
    }
    Project --> Repository
```
````

Результат:

```mermaid
classDiagram
    class Project {
        +String name
        +Array files
        +save()
    }
    class Repository {
        +clone()
        +push()
    }
    Project --> Repository
```

### GitLab CI/CD для генерации

```yaml
generate_diagrams:
  stage: build
  image: node:18
  script:
    - npm install -g @mermaid-js/mermaid-cli
    - mkdir -p public/diagrams
    - for file in docs/*.mmd; do
        mmdc -i $file -o public/diagrams/$(basename $file .mmd).png;
      done
  artifacts:
    paths:
      - public/diagrams/
```

## Сравнение платформ

```mermaid
quadrantChart
    title "Сравнение поддержки Mermaid"
    x-axis "Меньше функций" --> "Больше функций"
    y-axis "Сложнее" --> "Проще"
    quadrant-1 "Рекомендуемые"
    quadrant-2 "Ограниченные"
    quadrant-3 "Не рекомендуются"
    quadrant-4 "Продвинутые"
    GitHub: [0.8, 0.9]
    GitLab: [0.75, 0.85]
    Notion: [0.3, 0.7]
    Custom Site: [0.95, 0.4]
```

## Лучшие практики

### 1. Версионирование диаграмм

Храните исходный код диаграмм в отдельных `.mmd` файлах:

```
docs/
├── architecture.mmd
├── flowchart.mmd
└── README.md (ссылается на .mmd файлы)
```

### 2. Документирование

Добавляйте комментарии к сложным диаграммам:

````markdown
<!-- DIAGRAM: Architecture Overview -->
<!-- UPDATED: 2024-01-15 -->
```mermaid
...
```
````

### 3. Оптимизация

- Избегайте слишком больших диаграмм (>100 элементов)
- Разбивайте сложные схемы на несколько частей
- Используйте ссылки между диаграммами

## Примеры использования

### Документация проекта

```mermaid
mindmap
  root((Проект))
    Документация
      README.md
      Архитектура
      API
    Код
      Источник
      Тесты
    CI/CD
      Сборка
      Деплой
```

### Workflow разработки

```mermaid
flowchart TD
    A[Идея] --> B[Issue]
    B --> C[Branch]
    C --> D[Код]
    D --> E[PR]
    E --> F{Code Review}
    F -->|OK| G[Merge]
    F -->|Changes| C
    G --> H[Deploy]
```

## Заключение

GitHub и GitLab предоставляют отличную поддержку Mermaid для документации. Для более сложных сценариев используйте GitHub Actions/GitLab CI для генерации изображений или создавайте собственные сайты документации.
