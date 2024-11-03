from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .core.gemini import GeminiAI
from .api.endpoints import chat

app = FastAPI(title="AI Assistant API")
ai = GeminiAI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat.router, prefix="/api/chat", tags=["chat"])

@app.get("/")
async def root():
    return {"message": "AI Assistant API is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)