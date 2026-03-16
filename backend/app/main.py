from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.cadastros_base import router as cadastros_router
from app.routes.registro_vacinacao import router as registro_router

app = FastAPI(title="API Comprovante de Vacinacao", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health", tags=["Health"])
def health_check() -> dict[str, str]:
    return {"status": "ok"}


app.include_router(registro_router, prefix="/api/v1")
app.include_router(cadastros_router, prefix="/api/v1")
