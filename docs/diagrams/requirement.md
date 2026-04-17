# Диаграммы требований (Requirement Diagram)

Позволяют визуализировать требования и их связи с элементами системы.

## Пример 1: Базовое требование

### Исходный код:

```text
requirementDiagram

    requirement "Безопасность данных" {
        id: REQ-001
        text: "Все данные должны быть зашифрованы"
        risk: High
        verifymethod: Test
    }

    element "База данных" {
        type: Database
    }

    "База данных" - satisfies -> "Безопасность данных"
```

### Результат:

```mermaid
requirementDiagram

    requirement "Безопасность данных" {
        id: REQ-001
        text: "Все данные должны быть зашифрованы"
        risk: High
        verifymethod: Test
    }

    element "База данных" {
        type: Database
    }

    "База данных" - satisfies -> "Безопасность данных"
```

## Пример 2: Сложная система требований

### Исходный код:

```text
requirementDiagram

    requirement "Высокая доступность" {
        id: REQ-002
        text: "Система должна работать 99.9% времени"
        risk: Medium
        verifymethod: Analysis
    }

    element "Балансировщик" {
        type: Service
    }

    element "Кластер БД" {
        type: Database
    }

    "Балансировщик" - satisfies -> "Высокая доступность"
    "Кластер БД" - satisfies -> "Высокая доступность"
```

### Результат:

```mermaid
requirementDiagram

    requirement "Высокая доступность" {
        id: REQ-002
        text: "Система должна работать 99.9% времени"
        risk: Medium
        verifymethod: Analysis
    }

    element "Балансировщик" {
        type: Service
    }

    element "Кластер БД" {
        type: Database
    }

    "Балансировщик" - satisfies -> "Высокая доступность"
    "Кластер БД" - satisfies -> "Высокая доступность"
```
