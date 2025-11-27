import pytest
from fastapi.testclient import TestClient
from main import app, get_gemini_model 

class MockGeminiResponse:
    def __init__(self, text):
        self.text = text

class MockGeminiModel:
    async def generate_content_async(self, prompt, generation_config=None):
        return MockGeminiResponse("Esta é uma resposta simulada de teste!")

client = TestClient(app)

def test_frontend_load():
    """ 
    Testa se a página HTML principal está sendo carregada corretamente.
    Substitui o antigo health check.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    assert "<title>IsCoolGPT - Seu Assistente</title>" in response.text

def test_ask_endpoint_mocked():
    app.dependency_overrides[get_gemini_model] = lambda: MockGeminiModel()
    payload = { "prompt": "Quanto é 2 + 2?", "context": "Matemática" }
    response = client.post("/ask", json=payload)
    app.dependency_overrides = {}
    
    assert response.status_code == 200
    data = response.json()
    assert data["answer"] == "Esta é uma resposta simulada de teste!"

def test_ask_endpoint_validation_error():
    payload = {} 
    response = client.post("/ask", json=payload)
    assert response.status_code == 422