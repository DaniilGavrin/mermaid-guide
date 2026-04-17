# Стилизация и темы

Продвинутые техники кастомизации диаграмм Mermaid.

## 🎨 Темы

Mermaid поддерживает встроенные темы:

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': '#ff6b6b'}}}%%
graph TD
    A[Красная тема] --> B[Пример]
```

## 🔧 Переменные тем

| Переменная | Описание |
|------------|----------|
| `primaryColor` | Основной цвет |
| `primaryTextColor` | Цвет текста |
| `primaryBorderColor` | Цвет границы |
| `lineColor` | Цвет линий |
| `fontSize` | Размер шрифта |

## 🏗 Кастомизация блок-схемы

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 
    'primaryColor': '#4ecdc4',
    'primaryBorderColor': '#2d9c8f',
    'lineColor': '#2d9c8f'
}}}%%
graph TD
    A[Стильный узел] --> B[Другой узел]
    style A fill:#4ecdc4,stroke:#2d9c8f,color:white
    style B fill:#ffe66d,stroke:#f0c419,color:black
```

## 📊 Стили для разных типов узлов

```mermaid
graph TD
    A[Обычный] --> B{Ромб}
    B --> C((Круг))
    style A fill:#e3f2fd,stroke:#1976d2
    style B fill:#fff3e0,stroke:#f57c00
    style C fill:#e8f5e9,stroke:#388e3c
```

---

*Перейдите к [интерактивности](interactivity.md) для изучения продвинутых функций.*
