from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional

router = APIRouter()

class ChatMessage(BaseModel):
    message: str
    context: Optional[str] = None
    user_id: Optional[str] = None

@router.post("/send")
async def send_message(chat_msg: ChatMessage):
    try:
        # Yapay zeka yanıtını al
        response = await ai.get_response(chat_msg.message)
        return {
            "status": "success",
            "response": response,
            "user_id": chat_msg.user_id
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))