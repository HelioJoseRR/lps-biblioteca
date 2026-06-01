import { useState, useEffect, useCallback } from 'react'
import { enabledFeatures } from './features'

/* ===== SVG Icon Components ===== */
const Icons = {
  book: (
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
      <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/>
      <path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/>
    </svg>
  ),
  search: (
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
      <circle cx="11" cy="11" r="8"/>
      <line x1="21" y1="21" x2="16.65" y2="16.65"/>
    </svg>
  ),
  plus: (
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
      <line x1="12" y1="5" x2="12" y2="19"/>
      <line x1="5" y1="12" x2="19" y2="12"/>
    </svg>
  ),
  lock: (
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
      <rect x="3" y="11" width="18" height="11" rx="2" ry="2"/>
      <path d="M7 11V7a5 5 0 0 1 10 0v4"/>
    </svg>
  ),
  calendar: (
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
      <rect x="3" y="4" width="18" height="18" rx="2" ry="2"/>
      <line x1="16" y1="2" x2="16" y2="6"/>
      <line x1="8" y1="2" x2="8" y2="6"/>
      <line x1="3" y1="10" x2="21" y2="10"/>
    </svg>
  ),
  x: (
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
      <line x1="18" y1="6" x2="6" y2="18"/>
      <line x1="6" y1="6" x2="18" y2="18"/>
    </svg>
  ),
  check: (
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
      <polyline points="20 6 9 17 4 12"/>
    </svg>
  ),
  alertCircle: (
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
      <circle cx="12" cy="12" r="10"/>
      <line x1="12" y1="8" x2="12" y2="12"/>
      <line x1="12" y1="16" x2="12.01" y2="16"/>
    </svg>
  ),
  bookOpen: (
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
      <path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/>
      <path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/>
    </svg>
  ),
  sparkles: (
    <svg viewBox="0 0 24 24" fill="currentColor">
      <path d="M9.937 15.5A2 2 0 0 0 8.5 14.063l-6.135-1.582a.5.5 0 0 1 0-.962L8.5 9.936A2 2 0 0 0 9.937 8.5l1.582-6.135a.5.5 0 0 1 .963 0L14.063 8.5A2 2 0 0 0 15.5 9.937l6.135 1.581a.5.5 0 0 1 0 .964L15.5 14.063a2 2 0 0 0-1.437 1.437l-1.582 6.135a.5.5 0 0 1-.963 0z"/>
    </svg>
  ),
  logOut: (
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
      <path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"/>
      <polyline points="16 17 21 12 16 7"/>
      <line x1="21" y1="12" x2="9" y2="12"/>
    </svg>
  ),
  shield: (
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
      <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
    </svg>
  ),
};

/* ===== Toast Component ===== */
function Toast({ message, type, onClose }) {
  useEffect(() => {
    const timer = setTimeout(onClose, 3500);
    return () => clearTimeout(timer);
  }, [onClose]);

  return (
    <div className={`toast ${type}`}>
      {type === 'success' ? Icons.check : Icons.alertCircle}
      <span>{message}</span>
    </div>
  );
}

/* ===== Main App ===== */
function App() {
  const [livros, setLivros] = useState([]);
  const [busca, setBusca] = useState('');
  const [loading, setLoading] = useState(false);
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const [view, setView] = useState('landing');
  const [selectedBook, setSelectedBook] = useState(null);
  
  // Persist login state
  const [isLoggedIn, setIsLoggedIn] = useState(() => {
    return localStorage.getItem('isLoggedIn') === 'true';
  });
  
  const [showAddModal, setShowAddModal] = useState(false);
  const [toast, setToast] = useState(null);

  const [loginUser, setLoginUser] = useState('');
  const [loginPass, setLoginPass] = useState('');
  const [newBook, setNewBook] = useState({ titulo: '', autor: '', ano: '', categoria: '', sinopse: '', tipo_edicao: '', capa: null });
  const [authorSuggestions, setAuthorSuggestions] = useState([]);
  const [showAuthorSuggestions, setShowAuthorSuggestions] = useState(false);

  const showToast = useCallback((message, type = 'success') => {
    setToast({ message, type });
  }, []);

  const fetchLivros = async (termo = '') => {
    setLoading(true);
    try {
      const url = termo
        ? `http://localhost:8080/catalogo-service/livros?busca=${termo}`
        : 'http://localhost:8080/catalogo-service/livros';
      const response = await fetch(url);
      if (response.ok) {
        const data = await response.json();
        setLivros(Array.isArray(data) ? data : []);
      }
    } catch (error) {
      console.error("Erro ao buscar livros:", error);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchLivros();
  }, []);

  useEffect(() => {
    const delayDebounceFn = setTimeout(() => {
      if (view === 'landing') fetchLivros(busca);
    }, 500);
    return () => clearTimeout(delayDebounceFn);
  }, [busca]);

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      const formData = new URLSearchParams();
      formData.append('username', loginUser);
      formData.append('password', loginPass);

      const response = await fetch('http://localhost:8080/auth-service/auth/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: formData.toString()
      });

      if (response.ok) {
        const data = await response.json();
        localStorage.setItem('token', data.access_token);
        localStorage.setItem('isLoggedIn', 'true');
        setIsLoggedIn(true);
        setView('landing');
        setLoginUser('');
        setLoginPass('');
        showToast('Autenticado com sucesso!');
      } else {
        // Fallback for when auth-service is not selected/available
        if (loginUser === 'admin' && loginPass === 'admin') {
          localStorage.setItem('isLoggedIn', 'true');
          setIsLoggedIn(true);
          setView('landing');
          setLoginUser('');
          setLoginPass('');
          showToast('Autenticado com sucesso (fallback admin)!');
        } else {
          showToast('Credenciais inválidas. Tente novamente.', 'error');
        }
      }
    } catch (err) {
      // Fallback
      if (loginUser === 'admin' && loginPass === 'admin') {
        localStorage.setItem('isLoggedIn', 'true');
        setIsLoggedIn(true);
        setView('landing');
        setLoginUser('');
        setLoginPass('');
        showToast('Autenticado com sucesso (fallback admin)!');
      } else {
        showToast('Erro de conexão ou credenciais inválidas.', 'error');
      }
    }
  };

  const handleLogout = () => {
    localStorage.removeItem('isLoggedIn');
    localStorage.removeItem('token');
    setIsLoggedIn(false);
    setIsMenuOpen(false);
    showToast('Sessão encerrada.');
  };

  const fetchAuthorSuggestions = async (query) => {
    if (query.length < 3) {
      setAuthorSuggestions([]);
      setShowAuthorSuggestions(false);
      return;
    }
    try {
      const response = await fetch(`http://localhost:8080/catalogo-service/autores?q=${encodeURIComponent(query)}`);
      if (response.ok) {
        const data = await response.json();
        setAuthorSuggestions(data);
        setShowAuthorSuggestions(data.length > 0);
      }
    } catch (err) {
      console.error("Erro ao buscar autores", err);
    }
  };

  const handleAuthorChange = (e) => {
    const val = e.target.value;
    setNewBook({ ...newBook, autor: val });
    fetchAuthorSuggestions(val);
  };

  const selectAuthor = (autor) => {
    setNewBook({ ...newBook, autor });
    setShowAuthorSuggestions(false);
  };

  const handleAddBook = async (e) => {
    e.preventDefault();
    try {
      const formData = new FormData();
      formData.append('titulo', newBook.titulo);
      formData.append('autor', newBook.autor);
      if (newBook.ano) formData.append('ano', newBook.ano);
      if (newBook.categoria) formData.append('categoria', newBook.categoria);
      if (newBook.sinopse) formData.append('sinopse', newBook.sinopse);
      if (newBook.tipo_edicao) formData.append('tipo_edicao', newBook.tipo_edicao);
      if (newBook.capa) formData.append('capa', newBook.capa);

      const response = await fetch('http://localhost:8080/catalogo-service/livros', {
        method: 'POST',
        body: formData
      });
      if (response.ok) {
        setShowAddModal(false);
        setNewBook({ titulo: '', autor: '', ano: '', categoria: '', sinopse: '', tipo_edicao: '', capa: null });
        fetchLivros();
        showToast('Livro adicionado com sucesso!');
      } else {
        showToast('Erro ao salvar livro. Verifique os dados.', 'error');
      }
    } catch (err) {
      showToast('Erro ao adicionar livro. Tente novamente.', 'error');
    }
  };

  const getCoverGradient = (title) => {
    if (!title) return 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)';
    const gradients = [
      'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
      'linear-gradient(135deg, #f093fb 0%, #f5576c 100%)',
      'linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)',
      'linear-gradient(135deg, #43e97b 0%, #38f9d7 100%)',
      'linear-gradient(135deg, #fa709a 0%, #fee140 100%)',
      'linear-gradient(135deg, #a18cd1 0%, #fbc2eb 100%)',
      'linear-gradient(135deg, #fccb90 0%, #d57eeb 100%)',
      'linear-gradient(135deg, #e0c3fc 0%, #8ec5fc 100%)',
      'linear-gradient(135deg, #f5576c 0%, #ff6a88 50%, #fccb90 100%)',
      'linear-gradient(135deg, #667eea 0%, #00d2ff 100%)',
    ];
    let hash = 0;
    for (let i = 0; i < title.length; i++) {
      hash = title.charCodeAt(i) + ((hash << 5) - hash);
    }
    return gradients[Math.abs(hash) % gradients.length];
  };

  return (
    <div className="app-container">
      {/* Toast */}
      {toast && (
        <Toast
          message={toast.message}
          type={toast.type}
          onClose={() => setToast(null)}
        />
      )}

      {/* Navbar */}
      <nav className="navbar">
        <div className="nav-content">
          <div className="nav-brand" onClick={() => setView('landing')}>
            <span className="logo-icon">
              <svg viewBox="0 0 24 24" fill="white" width="20" height="20">
                <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20" stroke="white" fill="none" strokeWidth="2" strokeLinecap="round"/>
                <path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z" stroke="white" fill="none" strokeWidth="2" strokeLinecap="round"/>
              </svg>
            </span>
            <span>LibLPS</span>
          </div>

          <div
            className={`nav-toggle ${isMenuOpen ? 'open' : ''}`}
            onClick={() => setIsMenuOpen(!isMenuOpen)}
          >
            <span></span>
            <span></span>
            <span></span>
          </div>

          <ul className={`nav-links ${isMenuOpen ? 'active' : ''}`}>
            <li
              className={view === 'landing' ? 'active' : ''}
              onClick={() => { setView('landing'); setIsMenuOpen(false); }}
            >
              Explorar
            </li>
            {!isLoggedIn ? (
              <li
                className={view === 'login' ? 'active' : ''}
                onClick={() => { setView('login'); setIsMenuOpen(false); }}
              >
                Admin
              </li>
            ) : (
              <li
                className="logout-btn"
                onClick={handleLogout}
              >
                Sair
              </li>
            )}
          </ul>
        </div>
      </nav>

      {/* ===== BOOK DETAILS VIEW ===== */}
      {view === 'book-details' && selectedBook ? (
        <main className="details-wrapper fade-in">
          <div className="details-container">
            <button className="btn-back" onClick={() => setView('landing')} aria-label="Voltar ao catálogo">
              ← Voltar ao Catálogo
            </button>
            <article className="details-layout">
              <div className="details-cover" style={{ background: selectedBook.capa_url ? `url("http://localhost:8080/catalogo-service${selectedBook.capa_url}") center/cover` : getCoverGradient(selectedBook.titulo) }}>
                {!selectedBook.capa_url && (
                  <div className="cover-design">
                    <span className="cover-title-large">{selectedBook.titulo}</span>
                  </div>
                )}
              </div>
              <div className="details-info">
                <span className="book-category">{selectedBook.categoria || 'Geral'}</span>
                <h2>{selectedBook.titulo}</h2>
                <p className="author-large">por <strong>{selectedBook.autor}</strong></p>
                <div className="details-meta">
                  <span className="meta-item">{Icons.calendar} Publicado em {selectedBook.ano || 'N/A'}</span>
                  <span className="meta-item">{Icons.book} {selectedBook.tipo_edicao || 'Edição Comum'}</span>
                </div>
                
                <div className="synopsis">
                  <h3>Sinopse</h3>
                  <p>{selectedBook.sinopse || `Um clássico indispensável que cativa leitores de todas as idades. A narrativa profunda e envolvente de ${selectedBook.autor} transporta o leitor para um universo rico em detalhes, explorando temas universais através de personagens inesquecíveis. Esta obra, categorizada como ${selectedBook.categoria || 'Geral'}, continua a ser uma referência essencial na literatura.`}</p>
                </div>

                <div className="details-actions">
                  {enabledFeatures.includes('emprestimo-service') && (
                    <button className="btn-action btn-borrow" onClick={() => showToast('Solicitação de empréstimo iniciada!')}>
                      {Icons.bookOpen} Solicitar Empréstimo
                    </button>
                  )}
                  {enabledFeatures.includes('avaliacao-service') && (
                    <button className="btn-action btn-favorite" onClick={() => showToast('Sistema de avaliação aberto!')}>
                      ★ Avaliar Obra
                    </button>
                  )}
                </div>
              </div>
            </article>
          </div>
        </main>
      ) : view === 'login' ? (
        <main className="login-wrapper fade-in">
          <div className="login-card animate-pop">
            <div className="login-header">
              <div className="icon-badge">
                {Icons.shield}
              </div>
              <h2>Painel de Controle</h2>
              <p>Autenticação do Administrador</p>
            </div>
            <form onSubmit={handleLogin} className="login-form">
              <div className="input-group">
                <label>Usuário de Acesso</label>
                <input
                  type="text"
                  placeholder="Nome de usuário"
                  value={loginUser}
                  onChange={e => setLoginUser(e.target.value)}
                  required
                />
              </div>
              <div className="input-group">
                <label>Sua Senha</label>
                <input
                  type="password"
                  placeholder="••••••••"
                  value={loginPass}
                  onChange={e => setLoginPass(e.target.value)}
                  required
                />
              </div>
              <button type="submit" className="btn-login-submit">Entrar no Sistema</button>
              <button type="button" className="btn-link" onClick={() => setView('landing')} aria-label="Voltar para a biblioteca">
                ← Voltar para a biblioteca
              </button>
            </form>
          </div>
        </main>

      ) : (
        <div className="fade-in">
          {/* ===== HERO ===== */}
          <header className="hero">
            <div className="hero-shapes">
              <div className="hero-shape"></div>
              <div className="hero-shape"></div>
              <div className="hero-shape"></div>
            </div>
            <div className="hero-content">
              <div className="hero-badge">
                {Icons.sparkles}
                <span>Catálogo Digital</span>
              </div>
              <h1>Sua biblioteca,<br />em qualquer lugar.</h1>
              <p>Explore, descubra e gerencie títulos e autores com apenas um clique.</p>
              <div className="hero-stats">
                <div className="hero-stat">
                  <div className="stat-value">{livros.length}</div>
                  <div className="stat-label">Títulos</div>
                </div>
                <div className="hero-stat">
                  <div className="stat-value">{new Set(livros.map(l => l.autor)).size}</div>
                  <div className="stat-label">Autores</div>
                </div>
                <div className="hero-stat">
                  <div className="stat-value">{new Set(livros.map(l => l.categoria).filter(Boolean)).size}</div>
                  <div className="stat-label">Categorias</div>
                </div>
              </div>
            </div>
          </header>

          {/* ===== STICKY CONTROLS ===== */}
          <nav className="sticky-controls" aria-label="Controles de pesquisa e adição">
            <div className="controls-content">
              <div className="search-pill">
                <div className="search-icon">{Icons.search}</div>
                <input
                  type="text"
                  placeholder="Pesquisar livros, autores ou categorias..."
                  value={busca}
                  onChange={(e) => setBusca(e.target.value)}
                  aria-label="Buscar livros, autores ou categorias"
                />
                {busca && (
                  <button 
                    className="btn-clear-search" 
                    onClick={() => setBusca('')}
                    aria-label="Limpar busca"
                  >
                    {Icons.x}
                  </button>
                )}
              </div>
              {isLoggedIn && (
                <button className="btn-add-mini" onClick={() => setShowAddModal(true)}>
                  {Icons.plus}
                  <span>Novo Livro</span>
                </button>
              )}
            </div>
          </nav>

          {/* ===== MAIN CONTENT ===== */}
          <main className="content">
            <section className="section-header">
              <h2>{busca ? `Resultados para "${busca}"` : 'Acervo Disponível'}</h2>
              <div className="title-underline"></div>
            </section>

            <section className="catalog-section">
              {loading ? (
                <div className="loading-state">
                  <div className="spinner"></div>
                  <p>Carregando acervo...</p>
                </div>
              ) : livros.length === 0 ? (
                <div className="empty-state">
                  <div className="empty-icon">{Icons.search}</div>
                  <h3>Nenhum livro encontrado</h3>
                  <p>Não encontramos nenhum resultado para "{busca}".</p>
                  <button className="btn-cancel" style={{marginTop: '1.5rem'}} onClick={() => setBusca('')}>
                    Limpar Busca
                  </button>
                </div>
              ) : (
                <div className="book-grid" aria-live="polite">
                  {/* Auth Ghost Card */}
                  {!isLoggedIn && (
                    <article className="book-card ghost-card" onClick={() => setView('login')} aria-label="Área do Administrador">
                      <div className="ghost-content">
                        <div className="ghost-icon">
                          {Icons.plus}
                        </div>
                        <p>Novo Título</p>
                      </div>
                    </article>
                  )}

                  {livros.map(livro => (
                    <article 
                      key={livro.id} 
                      className="book-card" 
                      role="button"
                      tabIndex="0"
                      aria-label={`Ver detalhes do livro ${livro.titulo}`}
                      onClick={() => { setSelectedBook(livro); setView('book-details'); }}
                      onKeyDown={(e) => { if(e.key === 'Enter') { setSelectedBook(livro); setView('book-details'); } }}
                    >
                      <div className="book-cover" style={{ background: livro.capa_url ? `url("http://localhost:8080/catalogo-service${livro.capa_url}") center/cover` : getCoverGradient(livro.titulo) }}>
                        {!livro.capa_url && (
                          <div className="cover-design">
                            <span className="cover-title-small">{livro.titulo}</span>
                          </div>
                        )}
                      </div>
                      <div className="book-info">
                        <span className="book-category">{livro.categoria || 'Geral'}</span>
                        <h3 className="book-title">{livro.titulo}</h3>
                        <p className="book-author">{livro.autor}</p>
                        <div className="book-meta">
                          <span className="year">
                            {Icons.calendar}
                            {livro.ano || 'N/A'}
                          </span>
                        </div>
                      </div>
                    </article>
                  ))}
                </div>
              )}
            </section>
          </main>
        </div>
      )}

      {/* ===== ADD BOOK MODAL ===== */}
      {showAddModal && (
        <div className="modal-overlay" onClick={() => setShowAddModal(false)}>
          <div className="modal-content animate-pop" onClick={e => e.stopPropagation()}>
            <div className="modal-header">
              <h3>Adicionar Registro</h3>
              <button className="btn-close" onClick={() => setShowAddModal(false)}>
                {Icons.x}
              </button>
            </div>
            <form onSubmit={handleAddBook} className="modal-form-split">
              <div className="modal-left">
                <div className="file-upload-area">
                  <input
                    type="file"
                    id="capa-upload"
                    accept="image/png, image/jpeg"
                    onChange={e => setNewBook({ ...newBook, capa: e.target.files[0] })}
                  />
                  <label htmlFor="capa-upload" className="file-upload-label">
                    {newBook.capa ? (
                      <span className="file-name">{newBook.capa.name}</span>
                    ) : (
                      <>
                        <div className="upload-icon">{Icons.plus}</div>
                        <p>Enviar Capa</p>
                        <span className="upload-hint">PNG/JPG</span>
                      </>
                    )}
                  </label>
                </div>
              </div>

              <div className="modal-right">
                <div className="input-group">
                  <label>Título da Obra</label>
                  <input
                    type="text"
                    placeholder="Ex: O Pequeno Príncipe"
                    value={newBook.titulo}
                    onChange={e => setNewBook({ ...newBook, titulo: e.target.value })}
                    maxLength="255"
                    required
                  />
                </div>
                
                <div className="input-group" style={{ position: 'relative' }}>
                  <label>Autor Principal</label>
                  <input
                    type="text"
                    placeholder="Nome do autor"
                    value={newBook.autor}
                    onChange={handleAuthorChange}
                    onBlur={() => setTimeout(() => setShowAuthorSuggestions(false), 200)}
                    onFocus={() => { if(newBook.autor.length >= 3 && authorSuggestions.length > 0) setShowAuthorSuggestions(true) }}
                    maxLength="255"
                    required
                  />
                  {showAuthorSuggestions && (
                    <ul className="autocomplete-dropdown">
                      {authorSuggestions.map((autor, idx) => (
                        <li key={idx} onClick={() => selectAuthor(autor)}>{autor}</li>
                      ))}
                    </ul>
                  )}
                </div>

                <div className="form-row-3">
                  <div className="input-group">
                    <label>Ano</label>
                    <input
                      type="number"
                      placeholder="1943"
                      value={newBook.ano}
                      onChange={e => setNewBook({ ...newBook, ano: parseInt(e.target.value) || '' })}
                      min="1000"
                      max="2100"
                    />
                  </div>
                  <div className="input-group">
                    <label>Categoria</label>
                    <select
                      value={newBook.categoria}
                      onChange={e => setNewBook({ ...newBook, categoria: e.target.value })}
                    >
                      <option value="">Selecione...</option>
                      <option value="Fantasia">Fantasia</option>
                      <option value="Ficção Científica">Ficção Científica</option>
                      <option value="Romance">Romance</option>
                      <option value="Biografia">Biografia</option>
                      <option value="Técnico/Acadêmico">Técnico / Acadêmico</option>
                      <option value="História">História</option>
                    </select>
                  </div>
                  <div className="input-group">
                    <label>Edição</label>
                    <select
                      value={newBook.tipo_edicao}
                      onChange={e => setNewBook({ ...newBook, tipo_edicao: e.target.value })}
                    >
                      <option value="">Selecione...</option>
                      <option value="Capa Comum">Comum</option>
                      <option value="Capa Dura">Dura</option>
                      <option value="Edição de Bolso">Bolso</option>
                      <option value="Edição de Luxo">Luxo</option>
                    </select>
                  </div>
                </div>

                <div className="input-group">
                  <label>Sinopse</label>
                  <textarea
                    placeholder="Resumo ou descrição do livro..."
                    value={newBook.sinopse}
                    onChange={e => setNewBook({ ...newBook, sinopse: e.target.value })}
                    rows="3"
                    maxLength="2000"
                  ></textarea>
                </div>
                
                <div className="modal-actions-right">
                  <button type="button" className="btn-cancel" onClick={() => setShowAddModal(false)}>Cancelar</button>
                  <button type="submit" className="btn-save">Confirmar Cadastro</button>
                </div>
              </div>
            </form>
          </div>
        </div>
      )}

      {/* ===== FOOTER ===== */}
      <footer className="footer">
        <div className="footer-content">
          <div className="footer-brand">
            <div className="footer-logo">
              <svg viewBox="0 0 24 24" fill="white" width="16" height="16">
                <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20" stroke="white" fill="none" strokeWidth="2.5" strokeLinecap="round"/>
                <path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z" stroke="white" fill="none" strokeWidth="2.5" strokeLinecap="round"/>
              </svg>
            </div>
            <span>LibLPS</span>
          </div>
          <p>&copy; 2026 LibLPS — Biblioteca Inteligente</p>
          <div className="footer-links">
            <a href="#">Sobre</a>
            <a href="#">Contato</a>
          </div>
        </div>
      </footer>
    </div>
  )
}

export default App
