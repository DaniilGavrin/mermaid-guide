# Архитектурные схемы

Визуализация архитектуры систем с помощью Mermaid.

## 🏢 Микросервисная архитектура

````markdown
```mermaid
C4Context
    title Микросервисная архитектура
    
    Person(user, "Пользователь")
    System_Boundary(b1, "Система") {
        Container(api_gw, "API Gateway", "Nginx", "Маршрутизация запросов")
        Container(auth, "Auth Service", "Node.js", "Авторизация")
        Container(users, "User Service", "Go", "Управление пользователями")
        Container(orders, "Order Service", "Java", "Обработка заказов")
    }
    
    Rel(user, api_gw, "HTTPS")
    Rel(api_gw, auth, "JWT")
    Rel(api_gw, users, "gRPC")
    Rel(api_gw, orders, "gRPC")
```
````

**Результат:**
```mermaid
C4Context
    title Микросервисная архитектура
    
    Person(user, "Пользователь")
    System_Boundary(b1, "Система") {
        Container(api_gw, "API Gateway", "Nginx", "Маршрутизация запросов")
        Container(auth, "Auth Service", "Node.js", "Авторизация")
        Container(users, "User Service", "Go", "Управление пользователями")
        Container(orders, "Order Service", "Java", "Обработка заказов")
    }
    
    Rel(user, api_gw, "HTTPS")
    Rel(api_gw, auth, "JWT")
    Rel(api_gw, users, "gRPC")
    Rel(api_gw, orders, "gRPC")
```

## 🔄 Event-Driven архитектура

````markdown
```mermaid
graph LR
    subproducers[Производители]
        A[Сервис A]
        B[Сервис B]
    end
    
    subgraphkafka[Apache Kafka]
        T1[Топик 1]
        T2[Топик 2]
    end
    
    subgraphconsumers[Потребители]
        C[Сервис C]
        D[Сервис D]
    end
    
    A --> T1
    B --> T2
    T1 --> C
    T2 --> D
```
````

**Результат:**
```mermaid
graph LR
    subproducers[Производители]
        A[Сервис A]
        B[Сервис B]
    end
    
    subgraphkafka[Apache Kafka]
        T1[Топик 1]
        T2[Топик 2]
    end
    
    subgraphconsumers[Потребители]
        C[Сервис C]
        D[Сервис D]
    end
    
    A --> T1
    B --> T2
    T1 --> C
    T2 --> D
```

## 📊 Слоёная архитектура

````markdown
```mermaid
graph TD
    subgraph Presentation[Презентационный слой]
        A[Web UI]
        B[Mobile App]
        C[API]
    end
    
    subgraph Business[Бизнес-логика]
        D[Сервисы]
        E[Правила]
    end
    
    subgraph Data[Данные]
        F[База данных]
        G[Кэш]
        H[Файлы]
    end
    
    Presentation --> Business
    Business --> Data
```
````

**Результат:**
```mermaid
graph TD
    subgraph Presentation[Презентационный слой]
        A[Web UI]
        B[Mobile App]
        C[API]
    end
    
    subgraph Business[Бизнес-логика]
        D[Сервисы]
        E[Правила]
    end
    
    subgraph Data[Данные]
        F[База данных]
        G[Кэш]
        H[Файлы]
    end
    
    Presentation --> Business
    Business --> Data
```

---

*Перейдите к [алгоритмам](algorithms.md) для визуализации алгоритмов.*
