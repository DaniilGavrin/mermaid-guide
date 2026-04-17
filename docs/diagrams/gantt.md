# Диаграммы Ганта

Диаграммы Ганта для визуализации планов проектов и временных шкал.

## 📐 Базовый синтаксис

````markdown
```mermaid
gantt
    title Проект
    dateFormat  YYYY-MM-DD
    section Этап 1
    Задача 1 :a1, 2024-01-01, 7d
    Задача 2 :after a1, 5d
```
````

**Результат:**
```mermaid
gantt
    title Проект
    dateFormat  YYYY-MM-DD
    section Этап 1
    Задача 1 :a1, 2024-01-01, 7d
    Задача 2 :after a1, 5d
```

## 🔧 Директивы

| Директива | Описание |
|-----------|----------|
| `dateFormat` | Формат даты |
| `section` | Группа задач |
| `todayMarker` | Маркер текущего дня |

## 🏗 Практический пример: Разработка ПО

````markdown
```mermaid
gantt
    title План разработки
    dateFormat  YYYY-MM-DD
    axisFormat  %d.%m
    
    section Анализ
    Сбор требований       :a1, 2024-01-01, 5d
    Проектирование        :a2, after a1, 7d
    
    section Разработка
    Backend              :b1, after a2, 10d
    Frontend             :b2, after a2, 8d
    Интеграция           :b3, after b1 b2, 5d
    
    section Тестирование
    Unit тесты           :c1, after b3, 3d
    Интеграционные тесты  :c2, after c1, 5d
    
    section Релиз
    Деплой               :d1, after c2, 2d
```
````

**Результат:**
```mermaid
gantt
    title План разработки
    dateFormat  YYYY-MM-DD
    axisFormat  %d.%m
    
    section Анализ
    Сбор требований       :a1, 2024-01-01, 5d
    Проектирование        :a2, after a1, 7d
    
    section Разработка
    Backend              :b1, after a2, 10d
    Frontend             :b2, after a2, 8d
    Интеграция           :b3, after b1 b2, 5d
    
    section Тестирование
    Unit тесты           :c1, after b3, 3d
    Интеграционные тесты  :c2, after c1, 5d
    
    section Релиз
    Деплой               :d1, after c2, 2d
```

---

*Перейдите к [ментальным картам](mindmap.md) для изучения следующего типа.*
