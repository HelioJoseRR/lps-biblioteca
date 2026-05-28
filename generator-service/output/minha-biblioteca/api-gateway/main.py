from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

app = FastAPI(title="API Gateway", description="Central routing for microservices. Interactive documentation available.", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/catalogo-service/{path:path}")
async def proxy_catalogo_service(path: str):
    # Simulates proxy routing to the microservice
    return {"gateway": "proxying to catalogo-service", "path": path}


@app.get("/emprestimo-service/{path:path}")
async def proxy_emprestimo_service(path: str):
    # Simulates proxy routing to the microservice
    return {"gateway": "proxying to emprestimo-service", "path": path}


@app.get("/auth-service/{path:path}")
async def proxy_auth_service(path: str):
    # Simulates proxy routing to the microservice
    return {"gateway": "proxying to auth-service", "path": path}


@app.get("/")
def root():
    return {"status": "Gateway Operational", "services": ["catalogo-service", "emprestimo-service", "auth-service"]}

@app.get("/docs-redirect")
def redirect_docs():
    return RedirectResponse(url="/docs")
