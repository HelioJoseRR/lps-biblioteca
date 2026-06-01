from fastapi import FastAPI, Query, HTTPException, Depends
from typing import List, Optional
from pydantic import BaseModel
import os
import psycopg2
from psycopg2.extras import RealDictCursor

app = FastAPI(title="Serviço de Catálogo", description="Gerenciamento de livros com persistência em banco de dados.")

# Configurações do Banco de Dados vindas do ambiente
DB_HOST = os.getenv("DB_HOST", "db")
DB_NAME = os.getenv("DB_NAME", "library_db")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASS = os.getenv("DB_PASS", "postgres")

def get_db_connection():
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        cursor_factory=RealDictCursor
    )
    return conn

class Livro(BaseModel):
    id: int
    titulo: str
    autor: str
    ano: Optional[int]
    categoria: Optional[str]

@app.get("/livros", response_model=List[Livro], tags=["Catálogo"])
async def listar_livros(
    busca: Optional[str] = Query(None, description="Busca por título ou autor")
):
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        if busca:
            query = "SELECT id, titulo, autor, ano, categoria FROM livros WHERE LOWER(titulo) LIKE %s OR LOWER(autor) LIKE %s"
            termo = f"%{busca.lower()}%"
            cur.execute(query, (termo, termo))
        else:
            cur.execute("SELECT id, titulo, autor, ano, categoria FROM livros")
        
        livros = cur.fetchall()
        return livros
    finally:
        cur.close()
        conn.close()

@app.get("/livros/{livro_id}", response_model=Livro, tags=["Catálogo"])
async def obter_livro(livro_id: int):
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute("SELECT id, titulo, autor, ano, categoria FROM livros WHERE id = %s", (livro_id,))
        livro = cur.fetchone()
        if not livro:
            raise HTTPException(status_code=404, detail="Livro não encontrado")
        return livro
    finally:
        cur.close()
        conn.close()

@app.post("/livros", response_model=Livro, status_code=201, tags=["Catálogo"])
async def adicionar_livro(livro: Livro):
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        query = "INSERT INTO livros (titulo, autor, ano, categoria) VALUES (%s, %s, %s, %s) RETURNING id, titulo, autor, ano, categoria"
        cur.execute(query, (livro.titulo, livro.autor, livro.ano, livro.categoria))
        novo_livro = cur.fetchone()
        conn.commit()
        return novo_livro
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cur.close()
        conn.close()
