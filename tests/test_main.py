import pytest
from fastapi.testclient import TestClient
from main import app, get_gemini_model # Importamos a função de dependência também

# --- MOCKS (As imitações) ---

# 1. Criamos uma classe que finge ser a resposta do Google
class MockGeminiResponse:
    def __init__(self, text):
        self.text = text

# 2. Criamos uma classe que finge ser o Modelo do Gemini
class MockGeminiModel:
    async def generate_content_async(self, prompt, generation_config=None):
        # Em vez de chamar o Google, retornamos uma frase fixa
        return MockGeminiResponse("Esta é uma resposta simulada de teste!")

# --- TESTES ---

client = TestClient(app)

def test_read_root():
    """ Testa se a API está no ar (Health Check) """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "IsCoolGPT (stateless) está operacional."}

def test_ask_endpoint_mocked():
    """ 
    Testa o endpoint /ask COM MOCK.
    Simula uma conversa sem gastar a API Key.
    """
    # A MÁGICA: Substituímos a dependência real pela falsa
    app.dependency_overrides[get_gemini_model] = lambda: MockGeminiModel()

    # Dados de teste
    payload = {
        "prompt": "Quanto é 2 + 2?",
        "context": "Matemática Básica"
    }

    response = client.post("/ask", json=payload)

    # Limpamos a substituição para não afetar outros testes
    app.dependency_overrides = {}

    # Validações
    assert response.status_code == 200
    data = response.json()
    # Verifica se a resposta é a nossa frase simulada
    assert data["answer"] == "Esta é uma resposta simulada de teste!"

def test_ask_endpoint_validation_error():
    """ 
    Testa se a API recusa dados incompletos (sem mock necessário).
    O Pydantic deve barrar isso antes mesmo de chamar o Gemini.
    """
    # Payload vazio (erro proposital)
    payload = {} 

    response = client.post("/ask", json=payload)

    # Esperamos erro 422 (Unprocessable Entity)
    assert response.status_code == 422