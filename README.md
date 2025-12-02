# 🎓 IsCoolGPT - Assistente Educacional com IA

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104.0-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Render](https://img.shields.io/badge/Deploy-Render-black?style=for-the-badge&logo=render&logoColor=white)

![CI Status](https://github.com/grossiter04/Atividade-Tinoco/actions/workflows/ci-pr-validation.yml/badge.svg)
![Staging Deploy](https://github.com/grossiter04/Atividade-Tinoco/actions/workflows/cd-staging.yml/badge.svg)
![Production Deploy](https://github.com/grossiter04/Atividade-Tinoco/actions/workflows/cd-prod.yml/badge.svg)

## 📖 Sobre o Projeto

O **IsCoolGPT** é uma aplicação web Fullstack projetada para auxiliar estudantes a entenderem conceitos complexos de forma didática. Utilizando a API do **Google Gemini** (IA Generativa), o sistema recebe perguntas em linguagem natural e devolve explicações simplificadas.

Este projeto foi desenvolvido com foco em **DevOps e Engenharia de Software Moderna**, implementando uma esteira completa de CI/CD automatizada.

---

## 🚀 Arquitetura e Tecnologias

A aplicação segue uma arquitetura **Stateless** e conteinerizada, garantindo escalabilidade e consistência entre ambientes.

* **Backend:** Python 3.11 + FastAPI (Alta performance e assíncrono).
* **Frontend:** HTML5/CSS3/JS (Servido estaticamente pelo FastAPI).
* **IA Engine:** Google Gemini 2.5 Flash.
* **Containerização:** Docker (Multi-stage builds para segurança e otimização).
* **CI/CD:** GitHub Actions.
* **Infraestrutura:** Render (Hospedagem de Containers).

### 📂 Estrutura de Pastas

```text
Atividade-Tinoco/
├── .github/workflows/    # Pipelines de Automação (CI/CD)
├── static/               # Frontend (Interface do Usuário)
├── tests/                # Testes Automatizados (Pytest)
├── main.py               # Aplicação Principal (API + Rotas)
├── Dockerfile            # Receita da Imagem Docker
├── docker-compose.yml    # Orquestração para desenvolvimento local
├── requirements.txt      # Dependências do Projeto
└── README.md             # Documentação
```

---

## ⚙️ Pipeline de CI/CD

O projeto utiliza uma estratégia de versionamento baseada em 3 branches principais (`develop`, `staging`, `main`), com automação total via GitHub Actions:

1.  **Integração Contínua (CI):**
    * A cada *Push* ou *Pull Request*, o sistema roda linting (`flake8`), testes unitários (`pytest`) e verifica se o Dockerfile é válido.
2.  **Deploy em Staging (CD):**
    * Ao aprovar código na branch `staging`, o deploy é feito automaticamente no ambiente de testes.
3.  **Promoção Automática:**
    * Se o deploy em Staging for bem-sucedido, um bot realiza o *merge* automático para a branch `main`.
4.  **Deploy em Produção (CD):**
    * A atualização da `main` dispara o deploy no ambiente de produção final.

---

## 🛠️ Como Rodar Localmente

### Pré-requisitos
* Docker instalado (com Docker Compose)
* Uma chave de API do Google Gemini (`GEMINI_API_KEY`)

### Passo 1: Configuração Inicial
1.  Clone o repositório:
    ```bash
    git clone [https://github.com/grossiter04/Atividade-Tinoco.git](https://github.com/grossiter04/Atividade-Tinoco.git)
    cd Atividade-Tinoco
    ```

2.  Crie o arquivo `.env` na raiz do projeto e adicione sua chave:
    ```text
    GEMINI_API_KEY=cole_sua_chave_aqui
    ```

### Passo 2: Rodando com Docker (Recomendado)

Você tem duas opções para rodar o container:

#### 🟢 Opção A: Usando Docker Compose (Mais Fácil)
Como o projeto já possui o arquivo `docker-compose.yml`, basta um comando para subir tudo:

```bash
docker compose up --build
```
*O site estará disponível em: `http://localhost:8000`*

#### 🟠 Opção B: Usando Docker Puro
Se preferir rodar manualmente sem o compose:

1.  Construa a imagem:
    ```bash
    docker build -t iscoolgpt .
    ```
2.  Rode o container ligando a porta 8000 e passando o arquivo .env:
    ```bash
    docker run -p 8000:8000 --env-file .env iscoolgpt
    ```

### Passo 3: Rodando sem Docker (Python Puro)
Caso não queira usar Docker:

1.  Crie um ambiente virtual e instale as dependências:
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```
2.  Inicie o servidor:
    ```bash
    uvicorn main:app --reload
    ```

---

## 🧪 Rodando os Testes

Para garantir a qualidade do código, execute os testes automatizados.
**Importante:** Você deve estar com o ambiente virtual (`venv`) ativado para que o pytest encontre as dependências.

1.  **Ative o ambiente virtual** (se ainda não estiver):
    ```bash
    # Linux/Mac
    source venv/bin/activate

    # Windows
    venv\Scripts\activate
    ```

2.  **Execute os comandos:**
    ```bash
    # Roda todos os testes
    pytest
    ```

> **Nota:** Os testes de API utilizam *Mocks* para simular o Google Gemini, garantindo que você não gaste créditos da sua API durante o desenvolvimento.

---

## 🔗 Links do Projeto (Deploy)

* **Ambiente de Produção:** [Acessar IsCoolGPT (Prod)](https://atividade-tinoco.onrender.com)
* **Ambiente de Staging:** [Acessar IsCoolGPT (Staging)](https://atividade-tinoco-1.onrender.com)
* **Documentação da API (Swagger):** [Ver Docs](https://atividade-tinoco-1.onrender.com/docs)

---

## 👨‍💻 Autor

**Gabriel Rossiter**
* Projeto desenvolvido para a disciplina de Cloud Computing.