# Документация проектов

Использование Mermaid для документации программного обеспечения.

## 📚 README файлы

````markdown
```mermaid
graph LR
    A[README.md] --> B[Описание проекта]
    A --> C[Установка]
    A --> D[Использование]
    A --> E[Архитектура]
```
````

**Результат:**
```mermaid
graph LR
    A[README.md] --> B[Описание проекта]
    A --> C[Установка]
    A --> D[Использование]
    A --> E[Архитектура]
```

## 🏗 Архитектурная документация

````markdown
```mermaid
C4Context
    title Архитектура веб-приложения
    
    Person(user, "Пользователь")
    System(frontend, "Frontend", "React приложение")
    System(backend, "Backend", "Node.js API")
    SystemDb(db, "База данных", "PostgreSQL")
    
    Rel(user, frontend, "Использует")
    Rel(frontend, backend, "Вызывает API")
    Rel(backend, db, "Хранит данные")
```
````

**Результат:**
```mermaid
C4Context
    title Архитектура веб-приложения
    
    Person(user, "Пользователь")
    System(frontend, "Frontend", "React приложение")
    System(backend, "Backend", "Node.js API")
    SystemDb(db, "База данных", "PostgreSQL")
    
    Rel(user, frontend, "Использует")
    Rel(frontend, backend, "Вызывает API")
    Rel(backend, db, "Хранит данные")
```

## 📋 Техническая спецификация

````markdown
```mermaid
sequenceDiagram
    participant Client
    participant API
    participant DB
    
    Client->>API: GET /users
    API->>DB: SELECT * FROM users
    DB-->>API: Данные
    API-->>Client: JSON ответ
```
````

**Результат:**
```mermaid
sequenceDiagram
    participant Client
    participant API
    participant DB
    
    Client->>API: GET /users
    API->>DB: SELECT * FROM users
    DB-->>API: Данные
    API-->>Client: JSON ответ
```

## ✅ Best Practices

- Храните диаграммы рядом с кодом
- Используйте версионирование
- Обновляйте при изменении архитектуры
- Добавляйте описания к сложным диаграммам

---

*Перейдите к [архитектурным схемам](architecture.md) для более детального изучения.*
