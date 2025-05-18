from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import json
import os

app = FastAPI()

# Allow requests from the frontend (browser)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve the chatbot.html file
@app.get("/", response_class=HTMLResponse)
async def get_home():
    return FileResponse("chatbot.html")

# Load knowledge base
with open("data/bbq_kb_delhi.json", "r", encoding="utf-8") as f:
    kb = json.load(f)

# Simple query API for the chatbot
@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    query = data.get("text", "").lower()
    for entry in kb:
        if entry["intent"] in query or entry["question"].lower() in query:
            return {"reply": entry["answer"]}
    return {"reply": "Sorry, I couldn't find an answer for that."}