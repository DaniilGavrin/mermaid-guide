# Диаграммы требований

Диаграммы требований для документирования функциональных и нефункциональных требований.

## 📐 Базовый синтаксис

````markdown
```mermaid
requirementDiagram
    requirement "Авторизация" {
        id: 1
        text: Пользователь должен иметь возможность войти
        risk: high
        verifymethod: test
    }
```
````

**Результат:**
```mermaid
requirementDiagram
    requirement "Авторизация" {
        id: 1
        text: Пользователь должен иметь возможность войти
        risk: high
        verifymethod: test
    }
```

## 🏗 Практический пример: Система заказов

````markdown
```mermaid
requirementDiagram
    requirement "Создание заказа" {
        id: 1
        text: Пользователь может создать заказ
        risk: high
        verifymethod: test
    }
    
    requirement "Оплата заказа" {
        id: 2
        text: Пользователь может оплатить заказ
        risk: high
        verifymethod: test
    }
    
    functionalRequirement "Email уведомление" {
        id: 3
        text: Система отправляет email после оплаты
        risk: medium
        verifymethod: inspection
    }
    
    "Создание заказа" - satisfies -> "Оплата заказа"
    "Оплата заказа" - traces -> "Email уведомление"
```
````

**Результат:**
```mermaid
requirementDiagram
    requirement "Создание заказа" {
        id: 1
        text: Пользователь может создать заказ
        risk: high
        verifymethod: test
    }
    
    requirement "Оплата заказа" {
        id: 2
        text: Пользователь может оплатить заказ
        risk: high
        verifymethod: test
    }
    
    functionalRequirement "Email уведомление" {
        id: 3
        text: Система отправляет email после оплаты
        risk: medium
        verifymethod: inspection
    }
    
    "Создание заказа" - satisfies -> "Оплата заказа"
    "Оплата заказа" - traces -> "Email уведомление"
```

---

*Перейдите к [продвинутым техникам](../advanced/styling.md) для изучения стилизации.*
