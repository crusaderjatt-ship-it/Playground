from fastapi import FastAPI

from backend.app.api.routes import router
from backend.app.core.db import init_db

app = FastAPI(title="AI Trend Radar API")
app.include_router(router)


@app.on_event("startup")
def startup() -> None:
    init_db()


@app.get("/api/health")
def health():
    return {"status": "ok"}
