# Диаграммы классов

Диаграммы классов UML для отображения структуры системы.

## 📐 Базовый синтаксис

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

## 🔗 Типы отношений

| Отношение | Синтаксис | Описание |
|-----------|-----------|----------|
| Наследование | `<|--` | "Является" |
| Реализация | `<|..` | Интерфейс |
| Ассоциация | `-->` | Связь |
| Агрегация | `o--` | "Часть целого" |
| Композиция | `*--` | Сильная связь |

## 🏗 Практический пример

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

---

*Перейдите к [диаграммам состояний](state.md) для изучения следующего типа.*
