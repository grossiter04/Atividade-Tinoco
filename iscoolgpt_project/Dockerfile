# --- ESTÁGIO 1: BUILDER ---
# Imagem completa para instalar dependências
FROM python:3.11-slim as builder

WORKDIR /app

# Cria e ativa o venv
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Copia APENAS o requirements.txt primeiro (para usar o cache do Docker)
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copia o resto do código
COPY . .

# --- ESTÁGIO 2: FINAL (PRODUÇÃO) ---
# Imagem "slim" limpa
FROM python:3.11-slim

WORKDIR /app

# Copia o venv e o código do builder
COPY --from=builder /opt/venv /opt/venv
COPY --from=builder /app /app

# Define o PATH para usar o venv
ENV PATH="/opt/venv/bin:$PATH"

# Cria usuário não-root (boa prática de segurança)
RUN useradd --no-create-home appuser
USER appuser

EXPOSE 8000

# Comando para rodar a aplicação
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]