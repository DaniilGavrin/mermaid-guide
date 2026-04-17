# Интеграция с Vue.js

Mermaid легко интегрируется в приложения на Vue.js. Рассмотрим несколько подходов.

## Способ 1: Компонент для Vue 3

### Установка

```bash
npm install mermaid
# или
yarn add mermaid
```

### Создание компонента

```vue
<!-- components/MermaidDiagram.vue -->
<template>
  <div ref="container" class="mermaid-container"></div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue';
import mermaid from 'mermaid';

const props = defineProps({
  chart: {
    type: String,
    required: true
  },
  id: {
    type: String,
    default: () => `mermaid-${Math.random().toString(36).substr(2, 9)}`
  }
});

const container = ref(null);

// Инициализация Mermaid
mermaid.initialize({
  startOnLoad: false,
  theme: 'default',
  securityLevel: 'loose',
});

const renderDiagram = async () => {
  if (container.value) {
    container.value.innerHTML = '';
    
    try {
      const { svg } = await mermaid.render(props.id, props.chart);
      container.value.innerHTML = svg;
    } catch (error) {
      console.error('Ошибка рендеринга Mermaid:', error);
      container.value.innerHTML = '<p style="color: red;">Ошибка при рендеринге диаграммы</p>';
    }
  }
};

onMounted(() => {
  renderDiagram();
});

watch(() => props.chart, () => {
  renderDiagram();
});
</script>

<style scoped>
.mermaid-container {
  display: flex;
  justify-content: center;
  padding: 1rem;
}

.mermaid-container :deep(svg) {
  max-width: 100%;
  height: auto;
}
</style>
```

### Использование компонента

```vue
<!-- App.vue -->
<template>
  <div class="app">
    <h1>Диаграмма последовательности</h1>
    <MermaidDiagram :chart="sequenceDiagram" id="seq-1" />
  </div>
</template>

<script setup>
import MermaidDiagram from './components/MermaidDiagram.vue';

const sequenceDiagram = `
sequenceDiagram
    participant Client
    participant Server
    participant Database
    
    Client->>Server: HTTP Request
    Server->>Database: Query
    Database-->>Server: Data
    Server-->>Client: Response
`;
</script>
```

## Способ 2: Динамические диаграммы с Composition API

```vue
<!-- DynamicDiagram.vue -->
<template>
  <div class="dynamic-diagram">
    <div class="controls">
      <button @click="addNode">Добавить узел</button>
      <button @click="removeNode">Удалить узел</button>
      <button @click="randomize">Случайная структура</button>
    </div>
    
    <MermaidDiagram :chart="generatedDiagram" id="dynamic" />
    
    <div class="code-preview">
      <pre><code>{{ generatedDiagram }}</code></pre>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';
import MermaidDiagram from './MermaidDiagram.vue';

const nodes = ref(['A', 'B', 'C', 'D']);

const generatedDiagram = computed(() => {
  let diagram = 'graph TD\n';
  
  nodes.value.forEach((node, index) => {
    diagram += `${node}[${node}]`;
    
    if (index > 0) {
      diagram += ` --> ${nodes.value[index - 1]}`;
    }
    
    diagram += '\n';
  });
  
  return diagram;
});

const addNode = () => {
  const nextChar = String.fromCharCode(65 + nodes.value.length);
  nodes.value.push(nextChar);
};

const removeNode = () => {
  if (nodes.value.length > 1) {
    nodes.value.pop();
  }
};

const randomize = () => {
  const shuffled = [...nodes.value].sort(() => Math.random() - 0.5);
  nodes.value = shuffled;
};
</script>

<style scoped>
.dynamic-diagram {
  padding: 2rem;
}

.controls {
  display: flex;
  gap: 1rem;
  margin-bottom: 2rem;
}

.controls button {
  padding: 0.5rem 1rem;
  background: #42b883;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background 0.3s;
}

.controls button:hover {
  background: #369970;
}

.code-preview {
  margin-top: 2rem;
  background: #2d2d2d;
  padding: 1rem;
  border-radius: 4px;
  overflow-x: auto;
}

.code-preview pre {
  margin: 0;
  color: #f8f8f2;
}
</style>
```

## Способ 3: Плагин для Markdown

### Установка плагина

```bash
npm install markdown-it mermaid
```

### Настройка плагина

```javascript
// plugins/mermaid.js
import mermaid from 'mermaid';

export default {
  install(app) {
    mermaid.initialize({
      startOnLoad: false,
      theme: 'default',
    });

    app.config.globalProperties.$mermaid = mermaid;
  }
};
```

### Использование в main.js

```javascript
// main.js
import { createApp } from 'vue';
import App from './App.vue';
import mermaidPlugin from './plugins/mermaid';

const app = createApp(App);
app.use(mermaidPlugin);
app.mount('#app');
```

## Интеграция с Nuxt.js

### Установка

```bash
npm install mermaid
```

### Создание плагина

```javascript
// plugins/mermaid.client.js
import mermaid from 'mermaid';

export default defineNuxtPlugin(() => {
  mermaid.initialize({
    startOnLoad: false,
    theme: 'default',
  });

  return {
    provide: {
      mermaid
    }
  };
});
```

### Компонент для Nuxt

```vue
<!-- components/MermaidChart.vue -->
<template>
  <div ref="container" class="mermaid-chart"></div>
</template>

<script setup>
const props = defineProps({
  chart: String,
  id: String
});

const container = ref(null);
const { $mermaid } = useNuxtApp();

onMounted(async () => {
  if (container.value && props.chart) {
    try {
      const { svg } = await $mermaid.render(props.id || 'mermaid', props.chart);
      container.value.innerHTML = svg;
    } catch (error) {
      console.error(error);
    }
  }
});
</script>
```

## Пример: Документация API

```vue
<!-- APIDocumentation.vue -->
<template>
  <div class="api-docs">
    <nav class="sidebar">
      <button 
        v-for="endpoint in endpoints" 
        :key="endpoint.name"
        :class="{ active: activeEndpoint === endpoint.name }"
        @click="activeEndpoint = endpoint.name"
      >
        {{ endpoint.name }}
      </button>
    </nav>
    
    <main class="content">
      <h2>{{ currentEndpoint.name }}</h2>
      <p>{{ currentEndpoint.description }}</p>
      
      <h3>Sequence Diagram</h3>
      <MermaidDiagram :chart="currentEndpoint.diagram" :id="currentEndpoint.name" />
      
      <h3>Code Example</h3>
      <pre><code>{{ currentEndpoint.code }}</code></pre>
    </main>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';
import MermaidDiagram from './MermaidDiagram.vue';

const endpoints = [
  {
    name: 'GET /users',
    description: 'Получение списка пользователей',
    diagram: `
sequenceDiagram
    participant Client
    participant API
    participant DB
    
    Client->>API: GET /users
    API->>DB: SELECT * FROM users
    DB-->>API: Users data
    API-->>Client: JSON response
    `,
    code: `fetch('/api/users')
  .then(res => res.json())
  .then(data => console.log(data));`
  },
  {
    name: 'POST /users',
    description: 'Создание нового пользователя',
    diagram: `
sequenceDiagram
    participant Client
    participant API
    participant DB
    participant Validator
    
    Client->>API: POST /users {data}
    API->>Validator: Validate data
    Validator-->>API: Valid
    API->>DB: INSERT user
    DB-->>API: Created
    API-->>Client: 201 Created
    `,
    code: `fetch('/api/users', {
  method: 'POST',
  body: JSON.stringify({ name: 'John' })
});`
  }
];

const activeEndpoint = ref(endpoints[0].name);

const currentEndpoint = computed(() => {
  return endpoints.find(e => e.name === activeEndpoint.value);
});
</script>

<style scoped>
.api-docs {
  display: flex;
  gap: 2rem;
  padding: 2rem;
}

.sidebar {
  width: 250px;
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.sidebar button {
  padding: 0.75rem;
  text-align: left;
  background: none;
  border: 1px solid #e0e0e0;
  border-radius: 4px;
  cursor: pointer;
}

.sidebar button.active {
  background: #42b883;
  color: white;
  border-color: #42b883;
}

.content {
  flex: 1;
}

.content h2, .content h3 {
  color: #2c3e50;
}
</style>
```

## TypeScript поддержка

```typescript
// types/mermaid.d.ts
declare module 'mermaid' {
  interface MermaidConfig {
    theme?: 'default' | 'forest' | 'dark' | 'neutral';
    startOnLoad?: boolean;
    securityLevel?: 'strict' | 'loose';
  }

  interface RenderResult {
    svg: string;
  }

  export function initialize(config: MermaidConfig): void;
  export function render(id: string, text: string): Promise<RenderResult>;
}
```

## Оптимизация

```vue
<script setup>
import { shallowRef, triggerRef } from 'vue';
import mermaid from 'mermaid';

// Используем shallowRef для больших диаграмм
const diagramData = shallowRef(initialDiagram);

const updateDiagram = (newData) => {
  diagramData.value = newData;
  triggerRef(diagramData); // Принудительное обновление
};
</script>
```

## Полезные ссылки

- [Vue.js официальная документация](https://vuejs.org/)
- [Nuxt.js документация](https://nuxt.com/)
- [Mermaid JS](https://mermaid.js.org/)
