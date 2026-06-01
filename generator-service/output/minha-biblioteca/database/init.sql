-- Schema Auto-gerado para Biblioteca LPS



CREATE TABLE IF NOT EXISTS livros (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    autor VARCHAR(255) NOT NULL,
    ano INTEGER,
    categoria VARCHAR(100)
);
INSERT INTO livros (titulo, autor, ano, categoria) VALUES 
('O Senhor dos Anéis', 'J.R.R. Tolkien', 1954, 'Fantasia'),
('1984', 'George Orwell', 1949, 'Distopia');

-- Seed de Usuário Admin padrão
INSERT INTO users (username, password_hash) 
SELECT 'admin', 'admin' 
WHERE NOT EXISTS (SELECT 1 FROM users WHERE username = 'admin');
