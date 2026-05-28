from fastapi import FastAPI

app = FastAPI(title="Emprestimo-service API")

@app.get("/")
def read_root():
    return {"service": "emprestimo-service", "status": "running"}

@app.get("/health")
def health_check():
    return {"status": "ok"}
