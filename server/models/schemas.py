from pydantic import BaseModel
from typing import List, Optional

class ChatMessage(BaseModel):
    role: str   # user
    content: str

class ChatRequest(BaseModel):
    messages: List[ChatMessage]

class ChatResponse(BaseModel):
    text: str