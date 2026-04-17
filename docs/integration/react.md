# Интеграция с React

Mermaid отлично работает в React-приложениях. Рассмотрим несколько способов подключения.

## Способ 1: Компонент mermaid-react

### Установка

```bash
npm install @mermaid-js/mermaid-react
# или
yarn add @mermaid-js/mermaid-react
```

### Использование

```jsx
import { Mermaid } from '@mermaid-js/mermaid-react';

const diagram = `
graph TD
    A[Start] --> B{Decision}
    B -->|Yes| C[Action 1]
    B -->|No| D[Action 2]
`;

function App() {
  return (
    <div className="App">
      <h1>Моя диаграмма</h1>
      <Mermaid chart={diagram} />
    </div>
  );
}

export default App;
```

## Способ 2: Ручная инициализация

### Установка

```bash
npm install mermaid
# или
yarn add mermaid
```

### Создание компонента

```jsx
// components/MermaidDiagram.jsx
import { useEffect, useRef } from 'react';
import mermaid from 'mermaid';

mermaid.initialize({
  startOnLoad: false,
  theme: 'default',
  securityLevel: 'loose',
});

const MermaidDiagram = ({ chart, id }) => {
  const containerRef = useRef(null);

  useEffect(() => {
    const renderDiagram = async () => {
      if (containerRef.current) {
        containerRef.current.innerHTML = '';
        
        try {
          const { svg } = await mermaid.render(id, chart);
          containerRef.current.innerHTML = svg;
        } catch (error) {
          console.error('Ошибка рендеринга Mermaid:', error);
          containerRef.current.innerHTML = '<p style="color: red;">Ошибка при рендеринге диаграммы</p>';
        }
      }
    };

    renderDiagram();
  }, [chart, id]);

  return <div ref={containerRef} />;
};

export default MermaidDiagram;
```

### Использование компонента

```jsx
import MermaidDiagram from './components/MermaidDiagram';

function App() {
  const sequenceDiagram = `
sequenceDiagram
    participant User
    participant API
    participant Database
    
    User->>API: Запрос данных
    API->>Database: SELECT * FROM users
    Database-->>API: Данные
    API-->>User: Ответ
  `;

  return (
    <div>
      <h1>Sequence Diagram</h1>
      <MermaidDiagram chart={sequenceDiagram} id="seq-1" />
    </div>
  );
}
```

## Способ 3: Динамические диаграммы

```jsx
import { useState } from 'react';
import MermaidDiagram from './components/MermaidDiagram';

function DynamicDiagram() {
  const [nodes, setNodes] = useState(['A', 'B', 'C']);
  
  const generateDiagram = () => {
    let diagram = 'graph LR\n';
    nodes.forEach((node, index) => {
      if (index > 0) {
        diagram += `${nodes[index - 1]} --> ${node}\n`;
      }
      diagram += `${node}[${node}]\n`;
    });
    return diagram;
  };

  return (
    <div>
      <button onClick={() => setNodes([...nodes, String.fromCharCode(65 + nodes.length)])}>
        Добавить узел
      </button>
      <MermaidDiagram chart={generateDiagram()} id="dynamic" />
    </div>
  );
}
```

## Настройка TypeScript

```typescript
// types/mermaid.d.ts
declare module '@mermaid-js/mermaid-react' {
  import { ComponentType } from 'react';
  
  interface MermaidProps {
    chart: string;
    config?: Record<string, any>;
    className?: string;
  }
  
  export const Mermaid: ComponentType<MermaidProps>;
}
```

## Оптимизация производительности

```jsx
import { useMemo } from 'react';

function OptimizedDiagram({ data }) {
  const diagram = useMemo(() => {
    // Генерируем диаграмму только при изменении data
    return generateComplexDiagram(data);
  }, [data]);

  return <MermaidDiagram chart={diagram} id="optimized" />;
}
```

## Пример: Интерактивная документация

```jsx
import { useState } from 'react';
import MermaidDiagram from './components/MermaidDiagram';

const examples = {
  flowchart: `graph TD
    Start --> Process
    Process --> Decision
    Decision -->|Yes| End
    Decision -->|No| Process`,
  
  sequence: `sequenceDiagram
    Alice->>Bob: Hello Bob
    Bob-->>Alice: Hi Alice`,
  
  class: `classDiagram
    Animal <|-- Duck
    Animal <|-- Fish
    Animal: +int age
    Animal: +String gender`,
};

function DocumentationViewer() {
  const [activeTab, setActiveTab] = useState('flowchart');

  return (
    <div className="doc-viewer">
      <div className="tabs">
        {Object.keys(examples).map(type => (
          <button
            key={type}
            className={activeTab === type ? 'active' : ''}
            onClick={() => setActiveTab(type)}
          >
            {type}
          </button>
        ))}
      </div>
      <MermaidDiagram chart={examples[activeTab]} id={activeTab} />
      <pre>
        <code>{examples[activeTab]}</code>
      </pre>
    </div>
  );
}
```

## Стилилизация

```css
/* styles/mermaid.css */
.mermaid-container {
  background: #f8f9fa;
  padding: 2rem;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.mermaid-container svg {
  max-width: 100%;
  height: auto;
}

.doc-viewer .tabs {
  display: flex;
  gap: 0.5rem;
  margin-bottom: 1rem;
}

.doc-viewer .tabs button {
  padding: 0.5rem 1rem;
  border: none;
  background: #e9ecef;
  cursor: pointer;
  border-radius: 4px;
}

.doc-viewer .tabs button.active {
  background: #0d6efd;
  color: white;
}

.doc-viewer pre {
  background: #2d2d2d;
  color: #f8f8f2;
  padding: 1rem;
  border-radius: 4px;
  overflow-x: auto;
}
```

## Полезные ссылки

- [Официальная документация Mermaid](https://mermaid.js.org/)
- [mermaid-react на GitHub](https://github.com/mermaid-js/mermaid-react)
- [Примеры React компонентов](https://github.com/mermaid-js/mermaid/tree/develop/packages/mermaid/src/docs)
