# Диаграммы сущность-связь (ER)

ER-диаграммы для моделирования данных и связей между сущностями.

## 📐 Базовый синтаксис

````markdown
```mermaid
erDiagram
    CUSTOMER ||--o{ ORDER : places
    ORDER ||--|{ LINE_ITEM : contains
```
````

**Результат:**
```mermaid
erDiagram
    CUSTOMER ||--o{ ORDER : places
    ORDER ||--|{ LINE_ITEM : contains
```

## 🔗 Типы связей

| Связь | Синтаксис | Описание |
|-------|-----------|----------|
| Один к одному | `\|\|--\|\|` | 1:1 |
| Один ко многим | `\|\|--o{` | 1:N |
| Многие ко многим | `}o--o{` | N:M |
| Необязательная | `o{` | 0..N |

## 🏗 Практический пример: Интернет-магазин

````markdown
```mermaid
erDiagram
    CUSTOMER {
        int id PK
        string name
        string email
    }
    ORDER {
        int id PK
        int customer_id FK
        date order_date
        float total
    }
    PRODUCT {
        int id PK
        string name
        float price
    }
    ORDER_ITEM {
        int id PK
        int order_id FK
        int product_id FK
        int quantity
    }
    
    CUSTOMER ||--o{ ORDER : places
    ORDER ||--|{ ORDER_ITEM : contains
    PRODUCT ||--o{ ORDER_ITEM : "included in"
```
````

**Результат:**
```mermaid
erDiagram
    CUSTOMER {
        int id PK
        string name
        string email
    }
    ORDER {
        int id PK
        int customer_id FK
        date order_date
        float total
    }
    PRODUCT {
        int id PK
        string name
        float price
    }
    ORDER_ITEM {
        int id PK
        int order_id FK
        int product_id FK
        int quantity
    }
    
    CUSTOMER ||--o{ ORDER : places
    ORDER ||--|{ ORDER_ITEM : contains
    PRODUCT ||--o{ ORDER_ITEM : "included in"
```

---

*Перейдите к [диаграммам Ганта](gantt.md) для изучения следующего типа.*
