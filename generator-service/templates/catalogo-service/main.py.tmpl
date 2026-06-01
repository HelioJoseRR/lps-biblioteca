from fastapi import FastAPI, Query, HTTPException, Depends, Form, File, UploadFile
from fastapi.staticfiles import StaticFiles
from typing import List, Optional
from pydantic import BaseModel
import os
import shutil
import psycopg2
from psycopg2.extras import RealDictCursor

app = FastAPI(title="Serviço de Catálogo", description="Gerenciamento de livros com persistência em banco de dados.")

os.makedirs("uploads", exist_ok=True)
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

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
    sinopse: Optional[str] = None
    tipo_edicao: Optional[str] = None
    capa_url: Optional[str] = None

@app.get("/livros", response_model=List[Livro], tags=["Catálogo"])
async def listar_livros(
    busca: Optional[str] = Query(None, description="Busca por título ou autor")
):
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        if busca:
            query = "SELECT id, titulo, autor, ano, categoria, sinopse, tipo_edicao, capa_url FROM livros WHERE LOWER(titulo) LIKE %s OR LOWER(autor) LIKE %s"
            termo = f"%{busca.lower()}%"
            cur.execute(query, (termo, termo))
        else:
            cur.execute("SELECT id, titulo, autor, ano, categoria, sinopse, tipo_edicao, capa_url FROM livros")
        
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
        cur.execute("SELECT id, titulo, autor, ano, categoria, sinopse, tipo_edicao, capa_url FROM livros WHERE id = %s", (livro_id,))
        livro = cur.fetchone()
        if not livro:
            raise HTTPException(status_code=404, detail="Livro não encontrado")
        return livro
    finally:
        cur.close()
        conn.close()

@app.get("/autores", response_model=List[str], tags=["Catálogo"])
async def listar_autores(q: str = Query(..., min_length=3)):
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        query = "SELECT DISTINCT autor FROM livros WHERE LOWER(autor) LIKE %s LIMIT 10"
        termo = f"%{q.lower()}%"
        cur.execute(query, (termo,))
        autores = [row["autor"] for row in cur.fetchall()]
        return autores
    finally:
        cur.close()
        conn.close()

@app.post("/livros", response_model=Livro, status_code=201, tags=["Catálogo"])
async def adicionar_livro(
    titulo: str = Form(..., max_length=255),
    autor: str = Form(..., max_length=255),
    ano: Optional[int] = Form(None, ge=1000, le=2100),
    categoria: Optional[str] = Form(None, max_length=100),
    sinopse: Optional[str] = Form(None, max_length=2000),
    tipo_edicao: Optional[str] = Form(None, max_length=50),
    capa: Optional[UploadFile] = File(None)
):
    capa_url = None
    if capa and capa.filename:
        file_path = f"uploads/{capa.filename}"
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(capa.file, buffer)
        capa_url = f"/uploads/{capa.filename}"

    conn = get_db_connection()
    cur = conn.cursor()
    try:
        query = """INSERT INTO livros (titulo, autor, ano, categoria, sinopse, tipo_edicao, capa_url) 
                   VALUES (%s, %s, %s, %s, %s, %s, %s) 
                   RETURNING id, titulo, autor, ano, categoria, sinopse, tipo_edicao, capa_url"""
        cur.execute(query, (titulo, autor, ano, categoria, sinopse, tipo_edicao, capa_url))
        novo_livro = cur.fetchone()
        conn.commit()
        return novo_livro
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cur.close()
        conn.close()
