from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class ChatRequest(BaseModel):
    question: str


@router.post("/")
async def chat(request: ChatRequest):
    return {
        "success": True,
        "message": "Question received successfully",
        "question": request.question,
        "answer": "This is a dummy answer for now.",
    }