# Mermaid Guide

Добро пожаловать в полное руководство по **Mermaid** — инструменту для создания диаграмм и визуализаций с помощью простого текстового синтаксиса.

## 🚀 Быстрый старт

Создайте свою первую диаграмму за 30 секунд:

```mermaid
graph TD
    A[Начало] --> B{Условие?}
    B -->|Да| C[Действие 1]
    B -->|Нет| D[Действие 2]
    C --> E[Конец]
    D --> E
```

## 📚 Что вы найдете здесь

- **Основы**: Изучите синтаксис и настройте окружение
- **Типы диаграмм**: От блок-схем до диаграмм Ганта и ментальных карт
- **Продвинутые техники**: Стилизация, интерактивность и интеграция
- **Примеры**: Реальные кейсы использования в документации и архитектуре

## 🎯 Почему Mermaid?

- ✅ **Текстовый формат**: Диаграммы хранятся вместе с кодом
- ✅ **Версионность**: Легко отслеживать изменения в Git
- ✅ **Интеграция**: Работает в GitHub, GitLab, MkDocs, Obsidian и других
- ✅ **Простота**: Минимум синтаксиса для максимального результата

---

# Основы Mermaid

## Что такое Mermaid?

**Mermaid** — это JavaScript-библиотека для создания диаграмм и визуализаций с помощью простого текстового синтаксиса, похожего на Markdown.

### 🎯 Основные преимущества

| Преимущество | Описание |
|--------------|----------|
| Текстовый формат | Диаграммы хранятся в виде обычного текста |
| Версионность | Легко отслеживать изменения в Git |
| Интеграция | Работает в GitHub, GitLab, MkDocs, Obsidian |
| Простота | Минимум синтаксиса для быстрого старта |

### 🔧 Где используется

- Документация проектов
- Архитектурные схемы
- Блок-схемы алгоритмов
- Диаграммы последовательностей
- Ментальные карты

## Установка и настройка

### 📦 Установка в MkDocs

#### 1. Установка зависимостей

```bash
pip install mkdocs-material mkdocs-mermaid2-plugin
```

#### 2. Настройка `mkdocs.yml`

```yaml
markdown_extensions:
  - mermaid2

plugins:
  - search
  - mermaid2:
      version: 10.6.1
```

### 🔗 Интеграция с GitHub

GitHub автоматически рендерит Mermaid-диаграммы в Markdown-файлах.

### 🛠 Другие платформы

| Платформа | Поддержка |
|-----------|-----------|
| GitLab | ✅ Встроенная |
| Obsidian | ✅ Встроенная |
| Notion | ❌ Не поддерживается |
| Confluence | ⚠️ Через плагины |

## Базовый синтаксис

### 📐 Структура диаграммы

Любая диаграмма начинается с указания типа:

```mermaid
graph TD
    A --> B
```

### 🔤 Основные элементы

| Элемент | Синтаксис | Пример |
|---------|-----------|--------|
| Узел | `A[Текст]` | `A[Начало]` |
| Ромб (условие) | `A{Текст}` | `A{Условие?}` |
| Круг | `A((Текст))` | `A((Конец))` |
| Стрелка | `-->` | `A --> B` |
| Стрелка с текстом | `-->|Текст|` | `A -->|Да| B` |

### 🎨 Пример сложной диаграммы

```mermaid
graph TD
    Start([Начало]) --> Input[Ввод данных]
    Input --> Check{Проверка}
    Check -->|OK| Process[Обработка]
    Check -->|Error| Error[Ошибка]
    Process --> Output[Вывод]
    Error --> Input
    Output --> End([Конец])
```

### 📏 Направления

- `TD` / `TB` — сверху вниз
- `LR` — слева направо
- `RL` — справа налево
- `BT` — снизу вверх

---

# Типы диаграмм

## Блок-схемы (Flowchart)

Блок-схемы — основной тип диаграмм для визуализации процессов и алгоритмов.

### Синтаксис узлов

```mermaid
graph TD
    A[Прямоугольник] 
    B(Ромб)
    C(Круг)
    D[Ссылка](https://example.com)
    E[/Наклонный/]
    F[\Наклонный\]
    G{{Гексагон}}
    H[(Цилиндр)]
```

### Типы связей

```mermaid
graph TD
    A -- Текст --> B
    A --- B
    A -.-> B
    A ==> B
```

### Подграфы

```mermaid
graph TD
    subgraph Один
        A --> B
    end
    subgraph Два
        C --> D
    end
    Один --> Два
```

## Диаграммы последовательностей (Sequence)

Диаграммы последовательностей показывают взаимодействие между объектами во времени.

### Базовый синтаксис

```mermaid
sequenceDiagram
    participant A as Клиент
    participant B as Сервер
    A->>B: Запрос
    B-->>A: Ответ
```

### Типы сообщений

| Тип | Синтаксис | Описание |
|-----|-----------|----------|
| Сплошная стрелка | `->>` | Синхронное сообщение |
| Пунктирная стрелка | `-->>` | Возврат ответа |
| Сплошная к себе | `->>` | Сообщение самому себе |
| Активация | `activate` / `deactivate` | Показывает активность |

### Практический пример

```mermaid
sequenceDiagram
    autonumber
    participant User as Пользователь
    participant API as API
    participant DB as База данных
    
    User->>API: POST /login
    activate API
    API->>DB: Проверка credentials
    activate DB
    DB-->>API: Данные пользователя
    deactivate DB
    API-->>User: Токен доступа
    deactivate API
```

## Диаграммы классов (Class Diagram)

Диаграммы классов UML для отображения структуры системы.

### Базовый синтаксис

```mermaid
classDiagram
    class Animal {
        +String name
        +int age
        +makeSound()
    }
    class Dog {
        +breed
        +bark()
    }
    Animal <|-- Dog
```

### Типы отношений

| Отношение | Синтаксис | Описание |
|-----------|-----------|----------|
| Наследование | `<|--` | "Является" |
| Реализация | `<|..` | Интерфейс |
| Ассоциация | `-->` | Связь |
| Агрегация | `o--` | "Часть целого" |
| Композиция | `*--` | Сильная связь |

### Практический пример

```mermaid
classDiagram
    class User {
        +id: int
        +name: string
        +email: string
        +login()
        +logout()
    }
    class Order {
        +id: int
        +items: List~Item~
        +total: float
        +calculateTotal()
    }
    class Item {
        +name: string
        +price: float
        +quantity: int
    }

    User "1" --> "0..*" Order : places
    Order "1" *-- "1..*" Item : contains
```

## Диаграммы состояний (State Diagram)

Показывают переходы между состояниями объекта.

### Базовый синтаксис

```mermaid
stateDiagram-v2
    [*] --> Still
    Still --> Moving
    Moving --> Still
    Moving --> Crash
    Crash --> [*]
```

### Сложный пример

```mermaid
stateDiagram-v2
    state Выбор {
        [*] --> Ожидание
        Ожидание --> Обработка: Получено
        Обработка --> Ожидание: Ошибка
        Обработка --> [*]: Успех
    }
```

## Диаграммы Ганта (Gantt)

Диаграммы Ганта для планирования проектов.

### Пример

```mermaid
gantt
    title План разработки
    dateFormat  YYYY-MM-DD
    section Бэкенд
    Проектирование       :a1, 2024-01-01, 7d
    Разработка API       :after a1, 14d
    Тестирование         :10d
    section Фронтенд
    Дизайн UI           :2024-01-05, 5d
    Вёрстка             :10d
    Интеграция          :7d
```

## Ментальные карты (Mindmap)

Иерархические структуры для мозгового штурма.

### Пример

```mermaid
mindmap
  root((Mermaid))
    Основы
      Синтаксис
      Установка
    Диаграммы
      Flowchart
      Sequence
      Class
    Интеграции
      GitHub
      MkDocs
      Obsidian
```

## ER-диаграммы (Entity Relationship)

ER-диаграммы для моделирования данных.

### Базовый синтаксис

```mermaid
erDiagram
    CUSTOMER ||--o{ ORDER : places
    ORDER ||--|{ LINE_ITEM : contains
    CUSTOMER {
        string name
        string email
    }
    ORDER {
        int id
        date created
    }
```

## Диаграммы требований (Requirement)

Для спецификации требований.

```mermaid
requirementDiagram
    requirement R1 {
        id: "REQ-001"
        text: "Система должна поддерживать авторизацию"
        risk: High
        verifymethod: Test
    }
    element AuthModule {
        type: "Component"
    }
    AuthModule - satisfies -> R1
```

## Диаграммы пользовательских путей (User Journey)

Показывают путь пользователя через сервис.

```mermaid
journey
    title Путь покупки
    section Поиск
      Найти товар: 5: User
      Просмотреть отзывы: 4: User
    section Покупка
      Добавить в корзину: 5: User
      Оформить заказ: 3: User
    section Доставка
      Получить товар: 5: User
```

## Timeline диаграммы

Хронология событий.

```mermaid
timeline
    title История Mermaid
    2014 : Создан проект
    2016 : Добавлены sequence диаграммы
    2019 : Интеграция с GitHub
    2023 : Версия 10.0
```

## Квадрантные диаграммы (Quadrant Chart)

Матрицы для анализа.

```mermaid
quadrantChart
    title Анализ технологий
    x-axis "Сложность" --> "Простота"
    y-axis "Мощность" --> "Простота"
    quadrant-1 "Сложно но мощно"
    quadrant-2 "Просто и мощно"
    quadrant-3 "Просто но слабо"
    quadrant-4 "Сложно и слабо"
    Mermaid: [0.8, 0.7]
    Graphviz: [0.3, 0.9]
```

## C4 диаграммы

Модель архитектуры ПО.

```mermaid
C4Context
    Person(user, "Пользователь")
    System(system, "Система", "Описание")
    Rel(user, system, "Использует")
```

---

# Продвинутые техники

## Стилизация

### Темы

```mermaid
%%{init: {'theme': 'dark'}}%%
graph TD
    A[Тёмная тема] --> B[Красиво]
```

### Кастомные стили

```mermaid
graph TD
    A[Красный узел]:::red
    B[Синий узел]:::blue
    classDef red fill:#f96,stroke:#333;
    classDef blue fill:#69f,stroke:#333;
    A --> B
```

## Интерактивность

Добавление кликабельных элементов:

```mermaid
graph TD
    A[Кликни меня]
    click A "https://example.com" "Перейти"
```

## Интеграция с фреймворками

### React

```jsx
import Mermaid from 'react-mermaid2';

<Mermaid chart={`
  graph TD
    A[React] --> B[Mermaid]
`}/>
```

### Vue

```vue
<template>
  <mermaid :chart="chartData"/>
</template>
```

---

# Практические примеры

## Архитектура микросервисов

```mermaid
graph TB
    subgraph Frontend
        Web[Web App]
        Mobile[Mobile App]
    end
    subgraph API Gateway
        Gateway[API Gateway]
    end
    subgraph Services
        Auth[Auth Service]
        Users[User Service]
        Orders[Order Service]
    end
    subgraph Data
        DB[(Database)]
        Cache[(Cache)]
    end
    
    Web --> Gateway
    Mobile --> Gateway
    Gateway --> Auth
    Gateway --> Users
    Gateway --> Orders
    Auth --> DB
    Users --> DB
    Users --> Cache
    Orders --> DB
```

## Бизнес-процессы

```mermaid
flowchart LR
    Start([Начало]) --> Review{Требуется<br/>согласование?}
    Review -->|Да| Manager[Согласование<br/>менеджером]
    Review -->|Нет| Process[Выполнение]
    Manager --> Approved{Одобрено?}
    Approved -->|Да| Process
    Approved -->|Нет| Reject([Отклонено])
    Process --> End([Конец])
```

## Алгоритмы

```mermaid
flowchart TD
    Start([Начало]) --> Init[i = 0, sum = 0]
    Init --> Check{i < n?}
    Check -->|Да| Add[sum += arr[i]]
    Add --> Inc[i++]
    Inc --> Check
    Check -->|Нет| Result[return sum]
    Result --> End([Конец])
```

## Документация

```mermaid
flowchart TB
    Docs[Документация]
    subgraph Разделы
        Intro[Введение]
        Install[Установка]
        Usage[Использование]
        API[API Reference]
    end
    Docs --> Intro
    Docs --> Install
    Docs --> Usage
    Docs --> API
```

---

# Заключение

Mermaid — мощный инструмент для создания диаграмм прямо в Markdown. Используйте его для:

- 📋 Технической документации
- 🏗 Архитектурных схем
- 📊 Визуализации данных
- 🔄 Описания процессов

**Ресурсы:**
- [Официальная документация](https://mermaid.js.org/)
- [Редактор Mermaid Live](https://mermaid.live/)
- [GitHub Repository](https://github.com/mermaid-js/mermaid)

---

*Руководство создано [DaniilGavrin](https://github.com/DaniilGavrin)*
