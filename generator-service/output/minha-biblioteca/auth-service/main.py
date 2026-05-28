from fastapi import FastAPI

app = FastAPI(title="Auth-service API")

@app.get("/")
def read_root():
    return {"service": "auth-service", "status": "running"}

@app.get("/health")
def health_check():
    return {"status": "ok"}
