# Диаграммы Зиккерта

Диаграммы Зиккерта (ZenUML) — упрощённый синтаксис для диаграмм последовательностей.

## 📐 Базовый синтаксис

```mermaid
sequenceDiagram
    participant A as Клиент
    participant B as Сервер
    
    A->>B: Запрос
    B-->>A: Ответ
```

## 🏗 Практический пример: API вызов

```mermaid
sequenceDiagram
    autonumber
    participant Client as Клиент
    participant API as API Gateway
    participant Auth as Сервис авторизации
    participant Data as Сервис данных
    
    Client->>API: POST /login
    API->>Auth: Проверка credentials
    Auth-->>API: Токен доступа
    API-->>Client: 200 OK + токен
    
    Client->>API: GET /data
    API->>Auth: Валидация токена
    Auth-->>API: Успех
    API->>Data: Запрос данных
    Data-->>API: Данные
    API-->>Client: JSON ответ
```

---

*Перейдите к [продвинутым техникам](../advanced/styling.md) для изучения стилизации.*
