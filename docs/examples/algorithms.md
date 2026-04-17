# Алгоритмы

Визуализация алгоритмов и структур данных с помощью Mermaid.

## 🔍 Бинарный поиск

```mermaid
graph TD
    A[Начало] --> B{Массив пуст?}
    B -->|Да| Z[Не найдено]
    B -->|Нет| C[Найти середину]
    C --> D{Средний = искомому?}
    D -->|Да| E[Найдено!]
    D -->|Больше| F[Искать слева]
    D -->|Меньше| G[Искать справа]
    F --> H[Обновить right]
    G --> I[Обновить left]
    H --> J{left <= right?}
    I --> J
    J -->|Да| C
    J -->|Нет| Z
```

## 📊 Сортировка пузырьком

```mermaid
sequenceDiagram
    participant Array as Массив
    participant Outer as Внешний цикл
    participant Inner as Внутренний цикл
    participant Swap as Обмен
    
    Outer->>Array: i = 0
    loop пока i < n
        Inner->>Array: j = 0
        loop пока j < n-i-1
            Array->>Array: Сравнить arr[j] и arr[j+1]
            alt arr[j] > arr[j+1]
                Swap->>Array: Поменять местами
            end
            Inner->>Inner: j++
        end
        Outer->>Outer: i++
    end
```

## 🌳 Обход дерева (BFS)

```mermaid
graph TD
    A[Корень] --> B[Левый]
    A --> C[Правый]
    B --> D[Л-Л]
    B --> E[Л-П]
    C --> F[П-Л]
    C --> G[П-П]
    
    style A fill:#f9f,stroke:#333
    style B fill:#bbf,stroke:#333
    style C fill:#bbf,stroke:#333
    style D fill:#bfb,stroke:#333
    style E fill:#bfb,stroke:#333
    style F fill:#bfb,stroke:#333
    style G fill:#bfb,stroke:#333
```

**Порядок обхода BFS:** A → B → C → D → E → F → G

---

*Перейдите к [бизнес-процессам](business-processes.md) для примеров из бизнеса.*
