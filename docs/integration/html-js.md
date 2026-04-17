# Прямое использование в HTML/JS

Mermaid можно использовать напрямую в HTML-страницах без каких-либо фреймворков. Это самый простой способ начать работу.

## Подключение через CDN

### Базовый пример

```html
<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Mermaid Пример</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      max-width: 1200px;
      margin: 0 auto;
      padding: 2rem;
    }
    
    .diagram-container {
      background: #f8f9fa;
      padding: 2rem;
      border-radius: 8px;
      margin: 2rem 0;
      box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    pre {
      background: #2d2d2d;
      color: #f8f8f2;
      padding: 1rem;
      border-radius: 4px;
      overflow-x: auto;
    }
  </style>
</head>
<body>
  <h1>Пример использования Mermaid</h1>
  
  <div class="diagram-container">
    <h2>Блок-схема</h2>
    <div class="mermaid">
graph TD
    A[Начало] --> B{Условие}
    B -->|Да| C[Действие 1]
    B -->|Нет| D[Действие 2]
    C --> E[Конец]
    D --> E
    </div>
  </div>
  
  <div class="diagram-container">
    <h2>Диаграмма последовательности</h2>
    <div class="mermaid">
sequenceDiagram
    participant User
    participant Browser
    participant Server
    
    User->>Browser: Ввод URL
    Browser->>Server: HTTP Request
    Server-->>Browser: HTML Response
    Browser-->>User: Отображение страницы
    </div>
  </div>
  
  <h2>Исходный код</h2>
  <pre><code>&lt;div class="mermaid"&gt;
graph TD
    A[Начало] --> B{Условие}
    B -->|Да| C[Действие 1]
    B -->|Нет| D[Действие 2]
    C --> E[Конец]
    D --> E
&lt;/div&gt;</code></pre>

  <!-- Подключение Mermaid через CDN -->
  <script type="module">
    import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
    
    mermaid.initialize({
      startOnLoad: true,
      theme: 'default',
      securityLevel: 'loose',
    });
  </script>
</body>
</html>
```

## Инициализация с настройками

```html
<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <title>Mermaid с настройками</title>
</head>
<body>
  <div class="mermaid">
graph LR
    A[Node A] --> B[Node B]
    B --> C[Node C]
    C --> D[Node D]
  </div>

  <script type="module">
    import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
    
    // Расширенная конфигурация
    const config = {
      startOnLoad: false,
      theme: 'forest',
      flowchart: {
        useMaxWidth: true,
        htmlLabels: true,
        curve: 'basis'
      },
      sequence: {
        diagramMarginX: 50,
        diagramMarginY: 10,
        actorMargin: 50,
        width: 150,
        height: 65,
        boxMargin: 10
      }
    };
    
    mermaid.initialize(config);
    
    // Ручной запуск рендеринга
    await mermaid.run();
  </script>
</body>
</html>
```

## Динамическая генерация диаграмм

```html
<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <title>Динамические диаграммы</title>
  <style>
    .controls {
      display: flex;
      gap: 1rem;
      margin: 1rem 0;
    }
    
    button {
      padding: 0.5rem 1rem;
      background: #0d6efd;
      color: white;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }
    
    button:hover {
      background: #0b5ed7;
    }
    
    #diagram-container {
      background: #f8f9fa;
      padding: 2rem;
      border-radius: 8px;
      min-height: 200px;
    }
    
    textarea {
      width: 100%;
      height: 150px;
      font-family: monospace;
      padding: 1rem;
      border: 1px solid #ccc;
      border-radius: 4px;
    }
  </style>
</head>
<body>
  <h1>Динамическая генерация диаграмм</h1>
  
  <div class="controls">
    <button onclick="addNode()">Добавить узел</button>
    <button onclick="removeNode()">Удалить узел</button>
    <button onclick="changeLayout()">Изменить layout</button>
    <button onclick="changeTheme()">Сменить тему</button>
  </div>
  
  <textarea id="diagram-code" oninput="updateDiagram()">
graph TD
    A[Start] --> B[Process]
    B --> C[End]
  </textarea>
  
  <div id="diagram-container" class="mermaid">
graph TD
    A[Start] --> B[Process]
    B --> C[End]
  </div>

  <script type="module">
    import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
    
    let nodeCount = 3;
    let currentLayout = 'TD';
    const themes = ['default', 'forest', 'dark', 'neutral'];
    let currentThemeIndex = 0;
    
    mermaid.initialize({
      startOnLoad: false,
      theme: themes[currentThemeIndex],
      securityLevel: 'loose',
    });
    
    window.updateDiagram = async () => {
      const code = document.getElementById('diagram-code').value;
      const container = document.getElementById('diagram-container');
      
      try {
        const { svg } = await mermaid.render('dynamic-diagram', code);
        container.innerHTML = svg;
      } catch (error) {
        container.innerHTML = '<p style="color: red;">Ошибка синтаксиса: ' + error.message + '</p>';
      }
    };
    
    window.addNode = () => {
      nodeCount++;
      const newNode = String.fromCharCode(64 + nodeCount);
      const textarea = document.getElementById('diagram-code');
      const lines = textarea.value.split('\n').filter(l => l.trim());
      
      if (lines.length > 0) {
        const lastNode = lines[lines.length - 1].match(/^[A-Z]+/)[0];
        lines.push(`    ${lastNode} --> ${newNode}[${newNode}]`);
      } else {
        lines.push(`graph ${currentLayout}`);
        lines.push(`    A[A] --> ${newNode}[${newNode}]`);
      }
      
      textarea.value = lines.join('\n');
      updateDiagram();
    };
    
    window.removeNode = () => {
      if (nodeCount > 2) {
        nodeCount--;
        const textarea = document.getElementById('diagram-code');
        const lines = textarea.value.split('\n').filter(l => l.trim());
        lines.pop();
        textarea.value = lines.join('\n');
        updateDiagram();
      }
    };
    
    window.changeLayout = () => {
      const layouts = ['TD', 'LR', 'BT', 'RL'];
      const currentIndex = layouts.indexOf(currentLayout);
      currentLayout = layouts[(currentIndex + 1) % layouts.length];
      
      const textarea = document.getElementById('diagram-code');
      textarea.value = textarea.value.replace(/graph \w+/, `graph ${currentLayout}`);
      updateDiagram();
    };
    
    window.changeTheme = () => {
      currentThemeIndex = (currentThemeIndex + 1) % themes.length;
      mermaid.initialize({
        theme: themes[currentThemeIndex],
        startOnLoad: false,
      });
      updateDiagram();
    };
    
    // Первичный рендеринг
    updateDiagram();
  </script>
</body>
</html>
```

## Использование с локальным файлом

```html
<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <title>Mermaid с локальным файлом</title>
</head>
<body>
  <h1>Загрузка диаграммы из файла</h1>
  
  <input type="file" id="file-input" accept=".mmd,.txt">
  <div id="diagram-container" class="mermaid"></div>
  
  <script type="module">
    import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
    
    mermaid.initialize({
      startOnLoad: false,
      theme: 'default',
    });
    
    document.getElementById('file-input').addEventListener('change', async (event) => {
      const file = event.target.files[0];
      if (!file) return;
      
      const text = await file.text();
      const container = document.getElementById('diagram-container');
      
      try {
        const { svg } = await mermaid.render('file-diagram', text);
        container.innerHTML = svg;
      } catch (error) {
        container.innerHTML = '<p style="color: red;">Ошибка: ' + error.message + '</p>';
      }
    });
  </script>
</body>
</html>
```

## Экспорт в SVG/PNG

```html
<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <title>Экспорт диаграмм</title>
  <style>
    .actions {
      margin: 1rem 0;
      display: flex;
      gap: 1rem;
    }
    
    button {
      padding: 0.5rem 1rem;
      background: #28a745;
      color: white;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }
    
    #diagram-container {
      border: 1px solid #ddd;
      padding: 2rem;
      background: white;
    }
  </style>
</head>
<body>
  <h1>Экспорт диаграммы</h1>
  
  <div class="mermaid">
graph TD
    A[Start] --> B[Process]
    B --> C{Decision}
    C -->|Yes| D[Action 1]
    C -->|No| E[Action 2]
    D --> F[End]
    E --> F
  </div>
  
  <div class="actions">
    <button onclick="exportSVG()">Экспорт SVG</button>
    <button onclick="exportPNG()">Экспорт PNG</button>
  </div>

  <script type="module">
    import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
    
    mermaid.initialize({
      startOnLoad: true,
      theme: 'default',
    });
    
    window.exportSVG = () => {
      const svg = document.querySelector('.mermaid svg');
      if (!svg) return;
      
      const svgData = new XMLSerializer().serializeToString(svg);
      const blob = new Blob([svgData], { type: 'image/svg+xml' });
      const url = URL.createObjectURL(blob);
      
      const link = document.createElement('a');
      link.href = url;
      link.download = 'diagram.svg';
      link.click();
      
      URL.revokeObjectURL(url);
    };
    
    window.exportPNG = async () => {
      const svg = document.querySelector('.mermaid svg');
      if (!svg) return;
      
      const canvas = document.createElement('canvas');
      const ctx = canvas.getContext('2d');
      const svgData = new XMLSerializer().serializeToString(svg);
      
      const img = new Image();
      const svgBlob = new Blob([svgData], { type: 'image/svg+xml;charset=utf-8' });
      const url = URL.createObjectURL(svgBlob);
      
      img.onload = () => {
        canvas.width = img.width;
        canvas.height = img.height;
        ctx.drawImage(img, 0, 0);
        
        canvas.toBlob((blob) => {
          const pngUrl = URL.createObjectURL(blob);
          const link = document.createElement('a');
          link.href = pngUrl;
          link.download = 'diagram.png';
          link.click();
          URL.revokeObjectURL(pngUrl);
        }, 'image/png');
        
        URL.revokeObjectURL(url);
      };
      
      img.src = url;
    };
  </script>
</body>
</html>
```

## Интеграция с Markdown

```html
<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <title>Mermaid + Markdown</title>
  <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
  <style>
    body {
      max-width: 900px;
      margin: 0 auto;
      padding: 2rem;
      font-family: Georgia, serif;
    }
    
    pre {
      background: #f6f8fa;
      padding: 1rem;
      border-radius: 4px;
      overflow-x: auto;
    }
    
    .mermaid {
      background: #fff;
      padding: 1rem;
      border: 1px solid #e1e4e8;
      border-radius: 4px;
      margin: 1rem 0;
    }
  </style>
</head>
<body>
  <div id="content"></div>

  <script type="module">
    import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
    
    mermaid.initialize({
      startOnLoad: false,
      theme: 'default',
    });
    
    const markdownText = `
# Документация проекта

## Архитектура

\`\`\`mermaid
graph TD
    Client[Клиент] --> LoadBalancer[Балансировщик]
    LoadBalancer --> Server1[Сервер 1]
    LoadBalancer --> Server2[Сервер 2]
    LoadBalancer --> Server3[Сервер 3]
    Server1 --> Database[(База данных)]
    Server2 --> Database
    Server3 --> Database
\`\`\`

## Процесс разработки

\`\`\`mermaid
gantt
    title Процесс разработки
    dateFormat  YYYY-MM-DD
    section Планирование
    Анализ требований :a1, 2024-01-01, 7d
    Проектирование :after a1, 5d
    section Разработка
    Фронтенд :2024-01-15, 14d
    Бэкенд :2024-01-15, 14d
    section Тестирование
    Интеграционное тестирование :2024-02-01, 7d
\`\`\`
    `;
    
    // Парсинг Markdown
    const html = marked.parse(markdownText);
    document.getElementById('content').innerHTML = html;
    
    // Рендеринг Mermaid диаграмм
    await mermaid.run();
  </script>
</body>
</html>
```

## Полезные ссылки

- [Официальная документация Mermaid](https://mermaid.js.org/)
- [CDN jsDelivr](https://www.jsdelivr.com/package/npm/mermaid)
- [Marked.js для Markdown](https://marked.js.org/)
