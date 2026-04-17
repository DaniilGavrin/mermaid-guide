# Диаграммы последовательностей

Диаграммы последовательностей показывают взаимодействие между объектами во времени.

## 📐 Базовый синтаксис

```mermaid
sequenceDiagram
    participant A as Клиент
    participant B as Сервер
    A->>B: Запрос
    B-->>A: Ответ
```

## 🎯 Типы стрелок

| Тип | Синтаксис | Описание |
|-----|-----------|----------|
| Сплошная | `->>` | Вызов |
| Пунктирная | `-->>` | Возврат |
| Сплошная к себе | `->>` | Самовызов |
| Создать | `->>+` | Создание участника |
| Уничтожить | `->>-` | Уничтожение |

## 🔄 Циклы и условия

```mermaid
sequenceDiagram
    participant User
    participant System
    
    User->>System: Логин
    alt Успех
        System-->>User: Токен
    else Ошибка
        System-->>User: Сообщение об ошибке
    end
    
    loop 3 раза
        User->>System: Запрос данных
        System-->>User: Данные
    end
```

## 🏗 Практический пример: HTTP запрос

```mermaid
sequenceDiagram
    autonumber
    participant Browser as Браузер
    participant Server as Сервер
    participant DB as База данных
    
    Browser->>Server: GET /api/users
    activate Server
    Server->>DB: SELECT * FROM users
    activate DB
    DB-->>Server: Данные пользователей
    deactivate DB
    Server-->>Browser: JSON ответ
    deactivate Server
```

---

*Перейдите к [диаграммам классов](class.md) для изучения следующего типа.*
