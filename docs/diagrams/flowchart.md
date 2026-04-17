# Блок-схемы (Flowchart)

Блок-схемы — самый популярный тип диаграмм в Mermaid.

## 📊 Типы узлов

**Пример кода:**
````markdown
````markdown
```mermaid
graph TD
    A[Прямоугольник] --> B{Ромб}
    B --> C(Круг)
    B --> D([Скошенный])
    B --> E[(Цилиндр)]
    B --> F((Двойной круг))
```
````

**Результат:**
```mermaid
graph TD
    A[Прямоугольник] --> B{Ромб}
    B --> C(Круг)
    B --> D([Скошенный])
    B --> E[(Цилиндр)]
    B --> F((Двойной круг))
```
````

**Результат:**
````markdown
```mermaid
graph TD
    A[Прямоугольник] --> B{Ромб}
    B --> C(Круг)
    B --> D([Скошенный])
    B --> E[(Цилиндр)]
    B --> F((Двойной круг))
```
````

**Результат:**
```mermaid
graph TD
    A[Прямоугольник] --> B{Ромб}
    B --> C(Круг)
    B --> D([Скошенный])
    B --> E[(Цилиндр)]
    B --> F((Двойной круг))
```

## 🔗 Типы связей

| Тип | Синтаксис | Вид |
|-----|-----------|-----|
| Сплошная | `-->` | → |
| Пунктирная | `-.->` | ⇢ |
| Жирная | `==>` | ⇒ |
| Тонкая | `---` | — |

## 🏷 Подписи на связях

**Пример кода:**
````markdown
````markdown
```mermaid
graph LR
    Start -->|Шаг 1| Process
    Process -->|Шаг 2| Check{Проверка}
    Check -->|Да| End
    Check -->|Нет| Process
```
````

**Результат:**
```mermaid
graph LR
    Start -->|Шаг 1| Process
    Process -->|Шаг 2| Check{Проверка}
    Check -->|Да| End
    Check -->|Нет| Process
```
````

**Результат:**
````markdown
```mermaid
graph LR
    Start -->|Шаг 1| Process
    Process -->|Шаг 2| Check{Проверка}
    Check -->|Да| End
    Check -->|Нет| Process
```
````

**Результат:**
```mermaid
graph LR
    Start -->|Шаг 1| Process
    Process -->|Шаг 2| Check{Проверка}
    Check -->|Да| End
    Check -->|Нет| Process
```

## 🎯 Практический пример: Алгоритм сортировки

**Пример кода:**
````markdown
````markdown
```mermaid
graph TD
    Start([Начало]) --> Init[Инициализация]
    Init --> Loop{Есть элементы?}
    Loop -->|Да| Compare[Сравнение]
    Compare --> Swap{Нужно менять?}
    Swap -->|Да| Exchange[Обмен]
    Swap -->|Нет| Next[Следующий элемент]
    Exchange --> Next
    Next --> Loop
    Loop -->|Нет| Finish([Конец])
```
````

**Результат:**
```mermaid
graph TD
    Start([Начало]) --> Init[Инициализация]
    Init --> Loop{Есть элементы?}
    Loop -->|Да| Compare[Сравнение]
    Compare --> Swap{Нужно менять?}
    Swap -->|Да| Exchange[Обмен]
    Swap -->|Нет| Next[Следующий элемент]
    Exchange --> Next
    Next --> Loop
    Loop -->|Нет| Finish([Конец])
```
````

**Результат:**
````markdown
```mermaid
graph TD
    Start([Начало]) --> Init[Инициализация]
    Init --> Loop{Есть элементы?}
    Loop -->|Да| Compare[Сравнение]
    Compare --> Swap{Нужно менять?}
    Swap -->|Да| Exchange[Обмен]
    Swap -->|Нет| Next[Следующий элемент]
    Exchange --> Next
    Next --> Loop
    Loop -->|Нет| Finish([Конец])
```
````

**Результат:**
```mermaid
graph TD
    Start([Начало]) --> Init[Инициализация]
    Init --> Loop{Есть элементы?}
    Loop -->|Да| Compare[Сравнение]
    Compare --> Swap{Нужно менять?}
    Swap -->|Да| Exchange[Обмен]
    Swap -->|Нет| Next[Следующий элемент]
    Exchange --> Next
    Next --> Loop
    Loop -->|Нет| Finish([Конец])
```

---

*Перейдите к [диаграммам последовательностей](sequence.md) для изучения следующего типа.*
