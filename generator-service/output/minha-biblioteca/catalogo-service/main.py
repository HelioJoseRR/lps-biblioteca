from fastapi import FastAPI

app = FastAPI(title="Catalogo-service API")

@app.get("/")
def read_root():
    return {"service": "catalogo-service", "status": "running"}

@app.get("/health")
def health_check():
    return {"status": "ok"}
