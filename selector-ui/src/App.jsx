import { useState, useMemo } from 'react';
import { features } from './features';
import './App.css';

/* ===== SVG Icons ===== */
const CheckIcon = () => (
  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="3" strokeLinecap="round" strokeLinejoin="round">
    <polyline points="20 6 9 17 4 12"/>
  </svg>
);

const LinkIcon = () => (
  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
    <path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/>
    <path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/>
  </svg>
);

/* ===== Category Icons ===== */
const categoryIcons = {
  'Core': '🧩',
  'Segurança': '🔐',
  'Operacional': '📋',
  'Financeiro': '💰',
  'Comunicação': '📨',
  'Exploração': '🔍',
  'Social': '💬',
  'Todas': '📦',
};

function App() {
  const [selectedFeatures, setSelectedFeatures] = useState(
    features.filter(f => f.mandatory).map(f => f.id)
  );
  const [projectName, setProjectName] = useState('minha-biblioteca');
  const [activeCategory, setActiveCategory] = useState('Todas');
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState(null);

  const categories = useMemo(() =>
    ['Todas', ...new Set(features.map(f => f.category))],
  []);

  const toggleFeature = (id) => {
    const feature = features.find(f => f.id === id);
    if (feature.mandatory) return;

    setSelectedFeatures(prev => {
      if (prev.includes(id)) {
        // Unselecting: also unselect anything that depends on this
        const toRemove = [id];
        let changed = true;
        while (changed) {
          changed = false;
          features.forEach(f => {
            if (prev.includes(f.id) && !toRemove.includes(f.id)) {
              if (f.dependencies.some(dep => toRemove.includes(dep))) {
                toRemove.push(f.id);
                changed = true;
              }
            }
          });
        }
        return prev.filter(fid => !toRemove.includes(fid));
      } else {
        // Selecting: also select all dependencies
        const toAdd = [id];
        let changed = true;
        while (changed) {
          changed = false;
          const currentAdding = [...toAdd];
          currentAdding.forEach(fid => {
            const f = features.find(feat => feat.id === fid);
            f.dependencies.forEach(depId => {
              if (!toAdd.includes(depId) && !prev.includes(depId)) {
                toAdd.push(depId);
                changed = true;
              }
            });
          });
        }

        // Handle exclusions: if we select this, deselect conflicting ones
        const conflicting = features.filter(f =>
          toAdd.includes(f.id) && f.excludes.some(excl => prev.includes(excl))
        ).flatMap(f => f.excludes);

        const newSelection = [...new Set([...prev, ...toAdd])].filter(fid => !conflicting.includes(fid));
        return newSelection;
      }
    });
  };

  const filteredFeatures = useMemo(() =>
    activeCategory === 'Todas' ? features : features.filter(f => f.category === activeCategory)
  , [activeCategory]);

  const selectedList = useMemo(() =>
    features.filter(f => selectedFeatures.includes(f.id))
  , [selectedFeatures]);

  const progressPercent = Math.round((selectedFeatures.length / features.length) * 100);

  const handleGenerate = async () => {
    if (projectName.trim() === '' || loading) return;
    setLoading(true);
    setMessage(null);

    try {
      const response = await fetch('http://localhost:5000/generate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          projectName,
          features: selectedFeatures
        })
      });

      const data = await response.json();
      if (response.ok) {
        setMessage({ type: 'success', text: `✓ Sucesso! Aplicação gerada em output/${projectName}/` });
      } else {
        setMessage({ type: 'error', text: data.error || 'Erro ao gerar.' });
      }
    } catch (err) {
      setMessage({ type: 'error', text: 'Erro de conexão com o servidor.' });
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="layout">
      {/* Navbar */}
      <header className="navbar">
        <div className="navbar-brand">
          <h1>⚡ Biblioteca LPS</h1>
          <span className="progress-badge">{selectedFeatures.length} de {features.length} features</span>
        </div>
        <div className="project-config">
          <input
            type="text"
            value={projectName}
            onChange={(e) => setProjectName(e.target.value)}
            placeholder="Nome da aplicação"
          />
        </div>
      </header>

      <div className="container">
        {/* Sidebar - Categories */}
        <aside className="sidebar">
          <h3>Categorias</h3>
          <ul>
            {categories.map(cat => (
              <li
                key={cat}
                className={activeCategory === cat ? 'active' : ''}
                onClick={() => setActiveCategory(cat)}
              >
                <span>{categoryIcons[cat] || '📁'} {cat}</span>
                <span className="count">
                  {features.filter(f => (cat === 'Todas' || f.category === cat) && selectedFeatures.includes(f.id)).length}
                </span>
              </li>
            ))}
          </ul>
        </aside>

        {/* Main Content - Feature Cards */}
        <main className="main-content">
          <div className="features-grid">
            {filteredFeatures.map(feature => (
              <div
                key={feature.id}
                className={`card ${selectedFeatures.includes(feature.id) ? 'selected' : ''} ${feature.mandatory ? 'mandatory' : ''}`}
                onClick={() => toggleFeature(feature.id)}
              >
                <div className="card-top">
                  <div className="checkbox">
                    <CheckIcon />
                  </div>
                  <div className="card-info">
                    <h4>{feature.name}</h4>
                    <span className="category-tag">{feature.category}</span>
                  </div>
                </div>
                <p className="description">{feature.description}</p>
                <div className="card-footer">
                  {feature.mandatory ? (
                    <span className="badge mandatory">Obrigatória</span>
                  ) : (
                    <span className="badge optional">Opcional</span>
                  )}
                  {feature.dependencies.length > 0 && (
                    <span className="dep-link" title={`Requer: ${feature.dependencies.join(', ')}`}>
                      <LinkIcon />
                      {feature.dependencies.length} dep{feature.dependencies.length > 1 ? 's' : '.'}
                    </span>
                  )}
                </div>
              </div>
            ))}
          </div>
        </main>

        {/* Summary Panel */}
        <aside className="summary-panel">
          <h3>Resumo</h3>

          {/* Progress Bar */}
          <div className="progress-bar-container">
            <div className="progress-bar-info">
              <span>Progresso</span>
              <span className="progress-percent">{progressPercent}%</span>
            </div>
            <div className="progress-bar-track">
              <div
                className="progress-bar-fill"
                style={{ width: `${progressPercent}%` }}
              ></div>
            </div>
          </div>

          <div className="summary-content">
            <div className="summary-group">
              <label>Selecionadas ({selectedFeatures.length})</label>
              <ul>
                {selectedList.map(f => (
                  <li key={f.id}>{f.name}</li>
                ))}
              </ul>
            </div>
          </div>
          <div className="actions">
            {message && <div className={`message ${message.type}`}>{message.text}</div>}
            <button
              className="btn-primary"
              disabled={!projectName.trim() || loading}
              onClick={handleGenerate}
            >
              {loading ? '⏳ Gerando...' : '🚀 Gerar Aplicação'}
            </button>
            <button className="btn-secondary" onClick={() => setSelectedFeatures(features.filter(f => f.mandatory).map(f => f.id))}>
              Resetar Seleção
            </button>
          </div>
        </aside>
      </div>
    </div>
  );
}

export default App;
