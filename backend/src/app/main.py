from fastapi import FastAPI

from app.api.routes import chat, documents

app = FastAPI(title="Cortex")


app.include_router(
    documents.router,
    prefix="/api/documents",
    tags=["Documents"],
)

app.include_router(
    chat.router,
    prefix="/api/chat",
    tags=["Chat"],
)


@app.get("/health")
async def health():
    return {
        "success": True,
        "message": "Cortex backend is running",
    }