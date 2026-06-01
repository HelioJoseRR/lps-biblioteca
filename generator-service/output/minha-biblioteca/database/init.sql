-- Schema Auto-gerado para Biblioteca LPS



CREATE TABLE IF NOT EXISTS livros (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    autor VARCHAR(255) NOT NULL,
    ano INTEGER,
    categoria VARCHAR(100),
    sinopse TEXT,
    tipo_edicao VARCHAR(50),
    capa_url VARCHAR(255)
);
INSERT INTO livros (titulo, autor, ano, categoria, sinopse, tipo_edicao) VALUES 
('O Senhor dos Anéis', 'J.R.R. Tolkien', 1954, 'Fantasia', 'A grande jornada para destruir o Um Anel.', 'Capa Dura'),
('1984', 'George Orwell', 1949, 'Ficção Científica', 'Uma distopia onde o Grande Irmão tudo vê.', 'Bolso');
