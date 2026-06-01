import { useState, useEffect } from 'react'

function App() {
  const [livros, setLivros] = useState([]);
  const [busca, setBusca] = useState('');
  const [loading, setLoading] = useState(false);
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const [view, setView] = useState('landing'); 
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [showAddModal, setShowAddModal] = useState(false);
  
  const [loginUser, setLoginUser] = useState('');
  const [loginPass, setLoginPass] = useState('');
  const [newBook, setNewBook] = useState({ titulo: '', autor: '', ano: '', categoria: '' });

  const fetchLivros = async (termo = '') => {
    setLoading(true);
    try {
      const url = termo 
        ? `http://localhost:8080/catalogo-service/livros?busca=${termo}` 
        : 'http://localhost:8080/catalogo-service/livros';
      const response = await fetch(url);
      const data = await response.json();
      setLivros(Array.isArray(data) ? data : []);
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

  const handleLogin = (e) => {
    e.preventDefault();
    if (loginUser === 'admin' && loginPass === 'admin') {
      setIsLoggedIn(true);
      setView('landing');
      setLoginUser('');
      setLoginPass('');
    } else {
      alert('Credenciais inválidas');
    }
  };

  const handleAddBook = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch('http://localhost:8080/catalogo-service/livros', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ ...newBook, id: 0 })
      });
      if (response.ok) {
        setShowAddModal(false);
        setNewBook({ titulo: '', autor: '', ano: '', categoria: '' });
        fetchLivros();
      }
    } catch (err) {
      alert('Erro ao adicionar livro');
    }
  };

  const getCoverColor = (title) => {
    const colors = ['#3b82f6', '#10b981', '#f59e0b', '#ef4444', '#8b5cf6', '#ec4899'];
    let hash = 0;
    for (let i = 0; i < title.length; i++) {
      hash = title.charCodeAt(i) + ((hash << 5) - hash);
    }
    return colors[Math.abs(hash) % colors.length];
  };

  return (
    <div className="app-container">
      <nav className="navbar">
        <div className="nav-content">
          <div className="nav-brand" onClick={() => setView('landing')}>
            <span className="logo-icon">📚</span>
            <span>LibLPS</span>
          </div>
          <div className={`nav-toggle ${isMenuOpen ? 'open' : ''}`} onClick={() => setIsMenuOpen(!isMenuOpen)}>
            <span></span>
            <span></span>
            <span></span>
          </div>
          <ul className={`nav-links ${isMenuOpen ? 'active' : ''}`}>
            <li className={view === 'landing' ? 'active' : ''} onClick={() => { setView('landing'); setIsMenuOpen(false); }}>Explorar</li>
            {!isLoggedIn ? (
              <li className={view === 'login' ? 'active' : ''} onClick={() => { setView('login'); setIsMenuOpen(false); }}>Admin</li>
            ) : (
              <li className="logout-btn" onClick={() => { setIsLoggedIn(false); setIsMenuOpen(false); }}>Sair</li>
            )}
          </ul>
        </div>
      </nav>

      {view === 'login' ? (
        <div className="login-wrapper">
          <div className="login-card animate-pop">
            <div className="login-header">
              <div className="icon-badge">🔐</div>
              <h2>Painel de Controle</h2>
              <p>Autenticação do Administrador</p>
            </div>
            <form onSubmit={handleLogin} className="login-form">
              <div className="input-group">
                <label>Usuário de Acesso</label>
                <input type="text" placeholder="Nome de usuário" value={loginUser} onChange={e => setLoginUser(e.target.value)} required />
              </div>
              <div className="input-group">
                <label>Sua Senha</label>
                <input type="password" placeholder="••••••••" value={loginPass} onChange={e => setLoginPass(e.target.value)} required />
              </div>
              <button type="submit" className="btn-login-submit">Entrar no Sistema</button>
              <button type="button" className="btn-link" onClick={() => setView('landing')}>Voltar para a biblioteca</button>
            </form>
          </div>
        </div>
      ) : (
        <>
          <header className="hero">
            <div className="hero-content">
              <h1>Sua biblioteca, <br/>em qualquer lugar.</h1>
              <p>Explore milhares de títulos e autores com apenas um clique.</p>
            </div>
          </header>

          <div className="sticky-controls">
            <div className="controls-content">
              <div className="search-pill">
                <span className="search-icon">🔍</span>
                <input 
                  type="text" 
                  placeholder="Pesquisar livros..." 
                  value={busca}
                  onChange={(e) => setBusca(e.target.value)}
                />
              </div>
              {isLoggedIn && (
                <button className="btn-add-mini" onClick={() => { console.log('Abrindo modal...'); setShowAddModal(true); }}>
                  <span>+</span> Novo Livro
                </button>
              )}
            </div>
          </div>

          <main className="content">
            <div className="section-header">
              <div className="section-title">
                <h2>{busca ? `Resultados para "${busca}"` : 'Catálogo de Obras'}</h2>
                <div className="title-underline"></div>
              </div>
            </div>

            <section className="catalog-section">
              {loading ? (
                <div className="loading-state">
                  <div className="spinner"></div>
                  <p>Filtrando...</p>
                </div>
              ) : (
                <div className="book-grid">
                  {isLoggedIn && !busca && (
                    <div className="book-card ghost-card" onClick={() => setShowAddModal(true)}>
                      <div className="ghost-content">
                        <span className="ghost-icon">➕</span>
                        <p>Novo Título</p>
                      </div>
                    </div>
                  )}
                  
                  {livros.length > 0 ? livros.map(livro => (
                    <div key={livro.id} className="book-card">
                      <div className="book-cover" style={{ backgroundColor: getCoverColor(livro.titulo) }}>
                        <div className="cover-design">
                          <span className="cover-title-small">{livro.titulo}</span>
                        </div>
                      </div>
                      <div className="book-info">
                        <span className="book-category">{livro.categoria || 'Geral'}</span>
                        <h3 title={livro.titulo}>{livro.titulo}</h3>
                        <p className="author">por <strong>{livro.autor}</strong></p>
                        <div className="book-meta">
                          <span className="year">📅 {livro.ano || 'N/A'}</span>
                        </div>
                      </div>
                    </div>
                  )) : (
                    <div className="empty-state">Nenhum livro encontrado.</div>
                  )}
                </div>
              )}
            </section>
          </main>
        </>
      )}

      {showAddModal && (
        <div className="modal-overlay" onClick={() => setShowAddModal(false)}>
          <div className="modal-content animate-pop" onClick={e => e.stopPropagation()}>
            <div className="modal-header">
              <h3>Adicionar Registro</h3>
              <button className="btn-close" onClick={() => setShowAddModal(false)}>×</button>
            </div>
            <form onSubmit={handleAddBook} className="modal-form">
              <div className="input-group">
                <label>Título da Obra</label>
                <input type="text" placeholder="Ex: O Pequeno Príncipe" value={newBook.titulo} onChange={e => setNewBook({...newBook, titulo: e.target.value})} required />
              </div>
              <div className="input-group">
                <label>Autor Principal</label>
                <input type="text" placeholder="Nome do autor" value={newBook.autor} onChange={e => setNewBook({...newBook, autor: e.target.value})} required />
              </div>
              <div className="form-row">
                <div className="input-group">
                  <label>Ano de Lançamento</label>
                  <input type="number" placeholder="Ex: 1943" value={newBook.ano} onChange={e => setNewBook({...newBook, ano: e.target.value})} />
                </div>
                <div className="input-group">
                  <label>Categoria / Gênero</label>
                  <input type="text" placeholder="Ex: Fantasia" value={newBook.categoria} onChange={e => setNewBook({...newBook, categoria: e.target.value})} />
                </div>
              </div>
              <div className="modal-actions">
                <button type="submit" className="btn-save">Confirmar Cadastro</button>
                <button type="button" className="btn-cancel" onClick={() => setShowAddModal(false)}>Cancelar</button>
              </div>
            </form>
          </div>
        </div>
      )}

      <footer className="footer">
        <div className="footer-content">
          <p><strong>LibLPS</strong> &copy; 2026 - Biblioteca Inteligente</p>
        </div>
      </footer>
    </div>
  )
}

export default App
