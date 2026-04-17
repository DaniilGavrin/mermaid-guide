// React компонент для отображения Mermaid диаграмм
import { useEffect, useRef, useState } from 'react';
import mermaid from 'mermaid';

// Инициализация Mermaid
mermaid.initialize({
  startOnLoad: false,
  theme: 'default',
  securityLevel: 'loose',
  fontFamily: 'sans-serif',
});

interface MermaidDiagramProps {
  chart: string;
  id: string;
  className?: string;
  config?: Record<string, any>;
}

/**
 * Компонент для рендеринга Mermaid диаграмм в React
 * 
 * @example
 * ```jsx
 * <MermaidDiagram 
 *   chart={`graph TD\nA --> B`} 
 *   id="diagram-1" 
 * />
 * ```
 */
const MermaidDiagram: React.FC<MermaidDiagramProps> = ({ 
  chart, 
  id, 
  className = '', 
  config = {} 
}) => {
  const containerRef = useRef<HTMLDivElement>(null);
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const renderDiagram = async () => {
      if (!containerRef.current) return;

      setLoading(true);
      setError(null);
      containerRef.current.innerHTML = '';

      try {
        // Применяем кастомные настройки если есть
        if (Object.keys(config).length > 0) {
          mermaid.initialize({ ...mermaid.getConfig(), ...config });
        }

        const { svg } = await mermaid.render(id, chart);
        containerRef.current.innerHTML = svg;
        
        // Добавляем классы для стилизации
        const svgElement = containerRef.current.querySelector('svg');
        if (svgElement) {
          svgElement.classList.add('mermaid-svg');
          svgElement.setAttribute('role', 'img');
          svgElement.setAttribute('aria-label', 'Mermaid diagram');
        }
      } catch (err) {
        const errorMessage = err instanceof Error ? err.message : 'Неизвестная ошибка';
        setError(`Ошибка рендеринга: ${errorMessage}`);
        console.error('Mermaid rendering error:', err);
      } finally {
        setLoading(false);
      }
    };

    // Debounce для предотвращения частых перерисовок
    const timeoutId = setTimeout(renderDiagram, 100);
    
    return () => clearTimeout(timeoutId);
  }, [chart, id, config]);

  if (loading) {
    return (
      <div className={`mermaid-loading ${className}`} role="status">
        <span className="sr-only">Загрузка диаграммы...</span>
        <div className="spinner"></div>
      </div>
    );
  }

  if (error) {
    return (
      <div className={`mermaid-error ${className}`} role="alert">
        <p>{error}</p>
        <pre className="error-code">{chart}</pre>
      </div>
    );
  }

  return (
    <div 
      ref={containerRef} 
      className={`mermaid-container ${className}`}
      role="figure"
    />
  );
};

export default MermaidDiagram;
