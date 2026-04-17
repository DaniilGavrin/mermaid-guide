# Работа с Obsidian

Obsidian — мощный инструмент для работы с заметками, который имеет отличную встроенную поддержку Mermaid.

## Базовое использование

### Создание диаграммы

1. Откройте или создайте заметку в Obsidian
2. Используйте стандартный синтаксис Mermaid:

````markdown
```mermaid
graph TD
    A[Идея] --> B[Исследование]
    B --> C[Планирование]
    C --> D[Реализация]
    D --> E[Тестирование]
    E --> F[Публикация]
```
````

## Типы диаграмм в Obsidian

### Flowchart (Блок-схемы)

````markdown
```mermaid
graph LR
    Start --> Input[/Ввод данных/]
    Input --> Process[Обработка]
    Process --> Decision{Условие?}
    Decision -->|Да| Output[/Вывод/]
    Decision -->|Нет| Process
    Output --> End
```
````

### Sequence Diagram (Диаграммы последовательностей)

````markdown
```mermaid
sequenceDiagram
    participant U as Пользователь
    participant O as Obsidian
    participant M as Mermaid
    
    U->>O: Создать заметку
    O->>M: Инициализировать рендерер
    M-->>O: Готово
    O-->>U: Показать диаграмму
```
````

### Class Diagram (Диаграммы классов)

````markdown
```mermaid
classDiagram
    class Заметка {
        +String title
        +String content
        +Date created
        +Date modified
        +addTag(String)
        +removeTag(String)
        +search(String) List~Заметка~
    }
    
    class Тег {
        +String name
        +List~Заметка~ notes
    }
    
    Заметка "1" -- "*" Тег : has
```
````

### Gantt Chart (Диаграммы Ганта)

````markdown
```mermaid
gantt
    title Проект написания книги
    dateFormat  YYYY-MM-DD
    section Подготовка
    Исследование       :a1, 2024-01-01, 30d
    План глав          :after a1, 15d
    section Написание
    Глава 1            :2024-02-15, 20d
    Глава 2            :after Chapter 1, 20d
    Глава 3            :after Chapter 2, 20d
    section Редактура
    Первое чтение      :2024-04-15, 15d
    Финальная правка   :after First pass, 10d
```
````

### Mindmap (Ментальные карты)

````markdown
```mermaid
mindmap
  root((Проект))
    Планирование
      Цели
      Ресурсы
      Сроки
    Разработка
      Дизайн
      Код
      Тесты
    Запуск
      Маркетинг
      Поддержка
```
````

### ER Diagram (Диаграммы сущность-связь)

````markdown
```mermaid
erDiagram
    ПОЛЬЗОВАТЕЛЬ ||--o{ ЗАМЕТКА : создает
    ПОЛЬЗОВАТЕЛЬ {
        int id
        string имя
        string email
    }
    ЗАМЕТКА ||--|{ ТЕГ : содержит
    ЗАМЕТКА {
        int id
        string заголовок
        text содержимое
        date дата_создания
    }
    ТЕГ {
        int id
        string название
    }
```
````

## Настройка тем

### Выбор темы

1. Откройте **Settings** (Настройки)
2. Перейдите в **Appearance** (Внешний вид)
3. Найдите секцию **Mermaid theme**
4. Выберите одну из тем:
   - `default` — светлая тема по умолчанию
   - `forest` — зеленая тема
   - `dark` — темная тема
   - `neutral` — нейтральная серая тема

### Автоматическое переключение тем

Obsidian может автоматически переключать тему Mermaid вместе с темой приложения:

```javascript
// В сниппете или плагине
app.on('css-change', () => {
  const isDark = document.body.classList.contains('theme-dark');
  // Логика переключения темы Mermaid
});
```

## Продвинутые техники

### Связь между заметками

Используйте Mermaid для визуализации связей между заметками:

````markdown
```mermaid
graph TD
    A[[Главная]] --> B[Проекты]
    A --> C[Идеи]
    A --> D[Ресурсы]
    B --> E[Проект 1]
    B --> F[Проект 2]
    C --> G[Идея 1]
    D --> H[Статья]
    D --> I[Видео]
    
    style A fill:#f9f,stroke:#333
    style B fill:#bbf,stroke:#333
    style C fill:#bfb,stroke:#333
    style D fill:#fbb,stroke:#333
```
````

### Интерактивные элементы

Хотя Obsidian не поддерживает полную интерактивность, можно использовать кликабельные ссылки:

````markdown
```mermaid
graph LR
    A[Начало] --> B[[Документация]]
    B --> C[[API Reference]]
    C --> D[[Примеры]]
    
    click B href "https://publish.obsidian.md/your-vault/Documentation" "Открыть документацию"
    click C href "https://publish.obsidian.md/your-vault/API" "Открыть API"
    click D href "https://publish.obsidian.md/your-vault/Examples" "Открыть примеры"
```
````

### Использование с плагинами

#### Excalidraw + Mermaid

Плагин Excalidraw позволяет комбинировать Mermaid с ручными рисунками:

1. Установите плагин **Excalidraw**
2. Создайте новый Excalidraw файл
3. Вставьте Mermaid код через меню

#### Dataview + Mermaid

Автоматическая генерация диаграмм из данных:

````markdown
```dataview
TABLE without id file.link as "Заметка", tags as "Теги"
FROM #проект
SORT file.name
```

```mermaid
%% Генерируется вручную на основе данных выше
graph TD
    A[Проект Alpha] --> B[Задача 1]
    A --> C[Задача 2]
    A --> D[Задача 3]
```
````

## Шаблоны для частого использования

### Шаблон: Процесс разработки

Создайте файл `Templates/Development Process.md`:

````markdown
## Процесс разработки

```mermaid
graph LR
    A[Идея] --> B[Требования]
    B --> C[Дизайн]
    C --> D[Разработка]
    D --> E[Тестирование]
    E --> F{Баги?}
    F -->|Да| D
    F -->|Нет| G[Релиз]
```

**Статус:** %% Не начато %%
**Дата начала:** %% {{date}} %%
````

### Шаблон: Архитектура системы

````markdown
## Архитектура

```mermaid
graph TB
    subgraph Client
        A[Browser]
        B[Mobile App]
    end
    
    subgraph Server
        C[Load Balancer]
        D[API Server]
        E[Database]
    end
    
    A --> C
    B --> C
    C --> D
    D --> E
```

**Версия:** 1.0
**Последнее обновление:** {{date}}
````

## Советы и лучшие практики

1. **Используйте комментарии** для документации сложных диаграмм:
   ```mermaid
   graph TD
       %% Основной поток
       A --> B
       %% Обработка ошибок
       B --> C
   ```

2. **Группируйте связанные элементы** с помощью `subgraph`:
   ```mermaid
   graph TB
       subgraph Frontend
           A[React]
           B[Vue]
       end
       
       subgraph Backend
           C[Node.js]
           D[Python]
       end
   ```

3. **Сохраняйте простоту** — сложные диаграммы трудно читать

4. **Используйте цвета осмысленно**:
   ```mermaid
   graph LR
       A[Критично] --> B[Важно]
       B --> C[Нормально]
       
       style A fill:#ff6b6b
       style B fill:#ffd93d
       style C fill:#6bcb77
   ```

5. **Версионируйте диаграммы** вместе с заметками через Git

## Экспорт и публикация

### Экспорт в PNG/SVG

1. Откройте заметку с диаграммой
2. Нажмите правой кнопкой на диаграмму
3. Выберите **Save as image**
4. Выберите формат (PNG или SVG)

### Публикация через Obsidian Publish

Диаграммы Mermaid автоматически рендерятся в опубликованных заметках.

### Экспорт в PDF

1. Установите плагин **Export to PDF**
2. Экспортируйте заметку
3. Диаграммы будут включены как изображения

## Решение проблем

### Диаграмма не отображается

1. Проверьте синтаксис в [Mermaid Live Editor](https://mermaid.live/)
2. Убедитесь, что отступы правильные (пробелы, не табы)
3. Перезагрузите Obsidian

### Медленный рендеринг

1. Упростите диаграмму
2. Разбейте на несколько меньших диаграмм
3. Отключите предпросмотр для больших заметок

### Конфликты с плагинами

Если диаграммы не работают после установки плагина:
1. Отключите недавно установленные плагины
2. Проверьте консоль разработчика (`Ctrl+Shift+I`)
3. Обновите Obsidian до последней версии

## Полезные ресурсы

- [Официальная документация Obsidian](https://help.obsidian.md/How+to/Create+diagrams+with+Mermaid)
- [Mermaid JS Documentation](https://mermaid.js.org/)
- [Obsidian Forum - Mermaid Tag](https://forum.obsidian.md/tag/mermaid)
- [Awesome Obsidian](https://github.com/kmaasrud/awesome-obsidian)
