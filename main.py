import os
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
import google.generativeai as genai
from typing import Annotated
from dotenv import load_dotenv 

# Carrega o arquivo .env
load_dotenv() 

# Pega a chave do ambiente
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

#print("Chave aqui")
#print(GEMINI_API_KEY)

if not GEMINI_API_KEY:
    raise RuntimeError("GEMINI_API_KEY não definida no .env!")

genai.configure(api_key=GEMINI_API_KEY)

# --- Modelos de Dados (Pydantic) ---
class StudyQuery(BaseModel):
    prompt: str
    context: str | None = None

class AIResponse(BaseModel):
    answer: str

# --- Inicialização do App ---
app = FastAPI(title="IsCoolGPT API")

# --- Lógica de Negócio (Stateless) ---
def get_gemini_model():
    model = genai.GenerativeModel('gemini-2.5-flash')
    return model

async def fetch_gemini_response(model: genai.GenerativeModel, query: StudyQuery):
    try:
        system_instruction = (
            "Você é o 'IsCoolGPT', um assistente educacional. "
            "Sua missão é explicar conceitos complexos de forma simples e didática."
        )
        full_prompt = f"Contexto: {query.context}\n\nPergunta: {query.prompt}"
        
        response = await model.generate_content_async(full_prompt)
        return response.text
    except Exception as e:
        print(f"Erro na API do Gemini: {e}")
        raise HTTPException(status_code=502, detail="Erro ao contatar o modelo de IA.")

# --- Endpoints da API ---
@app.get("/")
def read_root():
    return {"status": "IsCoolGPT (stateless) está operacional."}

@app.post("/ask", response_model=AIResponse)
async def handle_study_query(
    query: StudyQuery, 
    model: Annotated[genai.GenerativeModel, Depends(get_gemini_model)]
):
    answer = await fetch_gemini_response(model, query)
    return AIResponse(answer=answer)