from fastapi import APIRouter, Query
from typing import Optional
import json
import os

kb_router = APIRouter()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, '../data')

def load_kb(city):
    path = os.path.join(DATA_DIR, f"bbq_kb_{city.lower()}.json")
    with open(path, "r") as f:
        return json.load(f)

@kb_router.get("/api/knowledgebase")
def get_kb_response(city: str, intent: str, query: str):
    kb = load_kb(city)
    for item in kb:
        if intent == item['intent'] and query.lower() in item['question'].lower():
            return {"answer": item['answer']}
    return {"answer": "Sorry, I couldn’t find relevant information."}
