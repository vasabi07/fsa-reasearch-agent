from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from agent import builder
from pydantic import BaseModel
from langchain_core.messages import HumanMessage, SystemMessage, BaseMessage
from websearch_agent import graph
app = FastAPI()

# ✅ Add CORS Middleware (Important for preflight requests)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (Change this in production)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, OPTIONS, etc.)
    allow_headers=["*"],  # Allow all headers
)

class ChatRequest(BaseModel):
    message: str

# ✅ Handle OPTIONS preflight requests explicitly
# @app.options("/chat/threads")
# async def options_chat_threads():
#     return {}

@app.post("/chat")
async def chat(request: ChatRequest):
    print(request)
    response = graph.invoke({"question":request.message})
    print(response["answer"])
    return {"message": response["answer"].content}  # Return conversation history

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8000)
