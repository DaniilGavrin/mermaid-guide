# Интерактивность

Интерактивные элементы в диаграммах Mermaid.

## 🔗 Кликабельные ссылки

```mermaid
graph TD
    A[GitHub] --> B[Документация]
    click A "https://github.com" "Открыть GitHub"
    click B "https://mermaid.js.org" "Открыть документацию"
```

## 📝 Tooltip (подсказки)

```mermaid
graph TD
    A[Наведите на меня] 
    B[И на меня тоже]
    
    click A callback "Это всплывающая подсказка"
    click B href "https://example.com" "Перейти на сайт"
```

## 🎯 JavaScript колбэки

```mermaid
graph TD
    A[Кликни меня] --> B[Результат]
    
    click A call testCallback("Привет!")
```

```javascript
window.testCallback = function(message) {
    alert(message);
};
```

## 💡 Практическое использование

- Ссылки на внешнюю документацию
- Переходы между разделами сайта
- Вызов модальных окон
- Трекинг аналитики

---

*Перейдите к [интеграции](integration.md) для изучения подключения к другим инструментам.*
