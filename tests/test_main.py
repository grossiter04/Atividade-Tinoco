from fastapi.testclient import TestClient
from main import app  # Importa sua aplicação FastAPI

# Cria um cliente de teste
client = TestClient(app)

def test_read_root():
    """ Testa se o endpoint de health check '/' está OK """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "IsCoolGPT (stateless) está operacional."}