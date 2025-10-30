from fastapi import FastAPI
from server.agent import llm
from server.models.schemas import ChatRequest, ChatResponse

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    messages = [m.dict() for m in req.messages]
    reply = llm.chat(messages)
    return ChatResponse(text=reply)