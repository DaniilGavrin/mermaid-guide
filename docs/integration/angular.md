# Интеграция с Angular

Mermaid можно легко использовать в приложениях Angular. Рассмотрим несколько подходов.

## Способ 1: Создание сервиса Mermaid

### Установка

```bash
npm install mermaid
# или
yarn add mermaid
```

### Создание сервиса

```typescript
// services/mermaid.service.ts
import { Injectable } from '@angular/core';
import mermaid from 'mermaid';

@Injectable({
  providedIn: 'root'
})
export class MermaidService {
  private initialized = false;

  constructor() {
    this.initialize();
  }

  initialize(): void {
    if (!this.initialized) {
      mermaid.initialize({
        startOnLoad: false,
        theme: 'default',
        securityLevel: 'loose',
      });
      this.initialized = true;
    }
  }

  async renderDiagram(containerId: string, diagram: string): Promise<string> {
    try {
      const { svg } = await mermaid.render(containerId, diagram);
      return svg;
    } catch (error) {
      console.error('Ошибка рендеринга Mermaid:', error);
      throw error;
    }
  }

  validateDiagram(diagram: string): boolean {
    try {
      mermaid.parse(diagram);
      return true;
    } catch {
      return false;
    }
  }
}
```

## Способ 2: Создание компонента

```typescript
// components/mermaid-diagram/mermaid-diagram.component.ts
import { Component, Input, OnInit, OnChanges, ElementRef, ViewChild } from '@angular/core';
import { MermaidService } from '../../services/mermaid.service';

@Component({
  selector: 'app-mermaid-diagram',
  template: `
    <div #container class="mermaid-container">
      <div *ngIf="error" class="error-message">
        {{ error }}
      </div>
    </div>
  `,
  styles: [`
    .mermaid-container {
      display: flex;
      justify-content: center;
      padding: 1rem;
      background: #f8f9fa;
      border-radius: 8px;
    }

    .mermaid-container :deep(svg) {
      max-width: 100%;
      height: auto;
    }

    .error-message {
      color: #dc3545;
      padding: 1rem;
      text-align: center;
    }
  `]
})
export class MermaidDiagramComponent implements OnInit, OnChanges {
  @Input() chart!: string;
  @Input() id?: string;
  
  error: string | null = null;
  
  @ViewChild('container', { static: true }) containerRef!: ElementRef;

  constructor(private mermaidService: MermaidService) {}

  ngOnInit(): void {
    this.render();
  }

  ngOnChanges(): void {
    this.render();
  }

  private async render(): Promise<void> {
    if (!this.chart) return;

    this.error = null;
    const diagramId = this.id || `mermaid-${Math.random().toString(36).substr(2, 9)}`;

    try {
      const svg = await this.mermaidService.renderDiagram(diagramId, this.chart);
      this.containerRef.nativeElement.innerHTML = svg;
    } catch (err) {
      this.error = 'Ошибка при рендеринге диаграммы. Проверьте синтаксис.';
      console.error(err);
    }
  }
}
```

### Модуль компонента

```typescript
// components/mermaid-diagram/mermaid-diagram.module.ts
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MermaidDiagramComponent } from './mermaid-diagram.component';

@NgModule({
  declarations: [MermaidDiagramComponent],
  imports: [CommonModule],
  exports: [MermaidDiagramComponent]
})
export class MermaidDiagramModule {}
```

## Способ 3: Использование в приложении

```typescript
// app.component.ts
import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  template: `
    <div class="app">
      <h1>Диаграмма последовательности</h1>
      
      <app-mermaid-diagram 
        [chart]="sequenceDiagram" 
        id="seq-1">
      </app-mermaid-diagram>
      
      <h2>Блок-схема алгоритма</h2>
      
      <app-mermaid-diagram 
        [chart]="flowchartDiagram" 
        id="flow-1">
      </app-mermaid-diagram>
    </div>
  `,
  styles: [`
    .app {
      padding: 2rem;
      max-width: 1200px;
      margin: 0 auto;
    }
    
    h1, h2 {
      color: #2c3e50;
      margin-top: 2rem;
    }
  `]
})
export class AppComponent {
  sequenceDiagram = `
sequenceDiagram
    participant User
    participant Frontend
    participant Backend
    participant Database
    
    User->>Frontend: Ввод данных
    Frontend->>Backend: POST /api/data
    Backend->>Database: INSERT
    Database-->>Backend: Success
    Backend-->>Frontend: 201 Created
    Frontend-->>User: Подтверждение
  `;

  flowchartDiagram = `
graph TD
    A[Начало] --> B{Валидация}
    B -->|Успех| C[Обработка]
    B -->|Ошибка| D[Логирование]
    C --> E[Сохранение]
    D --> F[Возврат ошибки]
    E --> G[Конец]
    F --> G
  `;
}
```

### Подключение модуля

```typescript
// app.module.ts
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppComponent } from './app.component';
import { MermaidDiagramModule } from './components/mermaid-diagram/mermaid-diagram.module';

@NgModule({
  declarations: [AppComponent],
  imports: [
    BrowserModule,
    MermaidDiagramModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule {}
```

## Динамические диаграммы

```typescript
// components/dynamic-diagram/dynamic-diagram.component.ts
import { Component } from '@angular/core';

@Component({
  selector: 'app-dynamic-diagram',
  template: `
    <div class="dynamic-diagram">
      <div class="controls">
        <button (click)="addNode()">Добавить узел</button>
        <button (click)="removeNode()">Удалить узел</button>
        <button (click)="randomize()">Случайная структура</button>
      </div>
      
      <app-mermaid-diagram [chart]="generatedDiagram" id="dynamic"></app-mermaid-diagram>
      
      <div class="code-preview">
        <h3>Исходный код диаграммы:</h3>
        <pre><code>{{ generatedDiagram }}</code></pre>
      </div>
    </div>
  `,
  styles: [`
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
      background: #0d6efd;
      color: white;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }
    
    .controls button:hover {
      background: #0b5ed7;
    }
    
    .code-preview {
      margin-top: 2rem;
      background: #2d2d2d;
      padding: 1rem;
      border-radius: 4px;
      color: #f8f8f2;
    }
    
    .code-preview h3 {
      color: #fff;
      margin-top: 0;
    }
  `]
})
export class DynamicDiagramComponent {
  nodes: string[] = ['A', 'B', 'C', 'D'];

  get generatedDiagram(): string {
    let diagram = 'graph TD\n';
    
    this.nodes.forEach((node, index) => {
      diagram += `${node}[${node}]`;
      
      if (index > 0) {
        diagram += ` --> ${this.nodes[index - 1]}`;
      }
      
      diagram += '\n';
    });
    
    return diagram;
  }

  addNode(): void {
    const nextChar = String.fromCharCode(65 + this.nodes.length);
    this.nodes.push(nextChar);
  }

  removeNode(): void {
    if (this.nodes.length > 1) {
      this.nodes.pop();
    }
  }

  randomize(): void {
    this.nodes = [...this.nodes].sort(() => Math.random() - 0.5);
  }
}
```

## Интеграция с формами

```typescript
// components/diagram-editor/diagram-editor.component.ts
import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-diagram-editor',
  template: `
    <div class="editor">
      <form [formGroup]="form">
        <div class="form-group">
          <label for="diagramType">Тип диаграммы:</label>
          <select id="diagramType" formControlName="type">
            <option value="flowchart">Flowchart</option>
            <option value="sequence">Sequence</option>
            <option value="class">Class</option>
            <option value="state">State</option>
          </select>
        </div>
        
        <div class="form-group">
          <label for="diagramCode">Код диаграммы:</label>
          <textarea 
            id="diagramCode" 
            formControlName="code" 
            rows="10"
            (input)="onCodeChange()">
          </textarea>
        </div>
        
        <div class="form-actions">
          <button type="button" (click)="loadTemplate()">Загрузить шаблон</button>
          <button type="button" (click)="validate()">Проверить</button>
        </div>
      </form>
      
      <div class="preview">
        <h3>Предпросмотр:</h3>
        <app-mermaid-diagram [chart]="form.get('code')?.value" id="preview"></app-mermaid-diagram>
      </div>
      
      <div *ngIf="validationResult" class="validation-result">
        {{ validationResult }}
      </div>
    </div>
  `,
  styles: [`
    .editor {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 2rem;
      padding: 2rem;
    }
    
    .form-group {
      margin-bottom: 1rem;
    }
    
    label {
      display: block;
      margin-bottom: 0.5rem;
      font-weight: bold;
    }
    
    select, textarea {
      width: 100%;
      padding: 0.5rem;
      border: 1px solid #ccc;
      border-radius: 4px;
    }
    
    .form-actions {
      display: flex;
      gap: 1rem;
      margin-top: 1rem;
    }
    
    .form-actions button {
      padding: 0.5rem 1rem;
      background: #0d6efd;
      color: white;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }
    
    .preview {
      background: #f8f9fa;
      padding: 1rem;
      border-radius: 8px;
    }
    
    .validation-result {
      grid-column: 1 / -1;
      padding: 1rem;
      border-radius: 4px;
      text-align: center;
    }
    
    .validation-result.success {
      background: #d4edda;
      color: #155724;
    }
    
    .validation-result.error {
      background: #f8d7da;
      color: #721c24;
    }
  `]
})
export class DiagramEditorComponent {
  form: FormGroup;
  validationResult: string | null = null;

  private templates: Record<string, string> = {
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
    
    state: `stateDiagram-v2
    [*] --> Still
    Still --> [*]
    Still --> Moving
    Moving --> Still`
  };

  constructor(private fb: FormBuilder) {
    this.form = this.fb.group({
      type: ['flowchart', Validators.required],
      code: [this.templates['flowchart'], Validators.required]
    });
  }

  onCodeChange(): void {
    this.validationResult = null;
  }

  loadTemplate(): void {
    const type = this.form.get('type')?.value;
    if (type && this.templates[type]) {
      this.form.patchValue({ code: this.templates[type] });
    }
  }

  validate(): void {
    const code = this.form.get('code')?.value;
    // Простая валидация
    if (code && code.trim().length > 0) {
      this.validationResult = '✓ Диаграмма валидна';
      this.validationResult += ' success';
    } else {
      this.validationResult = '✗ Ошибка: пустой код';
      this.validationResult += ' error';
    }
  }
}
```

## Работа с темизацией

```typescript
// services/theme.service.ts
import { Injectable } from '@angular/core';
import mermaid from 'mermaid';

export type MermaidTheme = 'default' | 'forest' | 'dark' | 'neutral';

@Injectable({
  providedIn: 'root'
})
export class ThemeService {
  private currentTheme: MermaidTheme = 'default';

  setTheme(theme: MermaidTheme): void {
    this.currentTheme = theme;
    mermaid.initialize({
      theme: theme,
      startOnLoad: false,
    });
    
    // Сохраняем тему в localStorage
    localStorage.setItem('mermaid-theme', theme);
  }

  getTheme(): MermaidTheme {
    const saved = localStorage.getItem('mermaid-theme') as MermaidTheme;
    return saved || 'default';
  }

  toggleTheme(): void {
    const themes: MermaidTheme[] = ['default', 'forest', 'dark', 'neutral'];
    const currentIndex = themes.indexOf(this.currentTheme);
    const nextIndex = (currentIndex + 1) % themes.length;
    this.setTheme(themes[nextIndex]);
  }
}
```

## Полезные ссылки

- [Angular официальная документация](https://angular.io/)
- [Mermaid JS](https://mermaid.js.org/)
- [ Reactive Forms в Angular](https://angular.io/guide/reactive-forms)
