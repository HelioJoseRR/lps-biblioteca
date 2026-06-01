from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

app = FastAPI(title="API Gateway", description="Ponto central de acesso aos microsserviços.", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.api_route("/catalogo-service/{path:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def proxy_catalogo_service(path: str):
    import httpx
    async with httpx.AsyncClient() as client:
        # Simplificacao: roteia para o container via docker network
        url = f"http://catalogo-service:8000/{path}"
        # No mundo real, repassariamos params e headers
        return {"gateway": "Proxy to catalogo-service", "url": url}


@app.get("/")
def root():
    return {"status": "Gateway Operacional", "servicos_disponiveis": ["catalogo-service"]}
