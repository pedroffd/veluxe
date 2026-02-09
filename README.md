# 🏎️ Veluxe - Estética Automotiva Premium

Veluxe é uma plataforma moderna para serviços de estética automotiva, desenvolvida com **Django (Backend)** e **Vue.js 3 + Vite (Frontend)**, focada em performance, design premium e qualidade de código.

## 🚀 Tecnologias Utilizadas

### Backend
- **Framework:** Django & Django REST Framework (DRF)
- **Database:** PostgreSQL (Produção) / SQLite (Desenvolvimento Local)
- **Tools:**
  - `Black`: Formatação de código.
  - `Flake8`: Linter.
  - `Isort`: Organização de importações.
  - `dj-database-url`: Configuração de banco via URL.

### Frontend
- **Framework:** Vue.js 3 (Composition API) + TypeScript
- **Build Tool:** Vite
- **Styling:** Tailwind CSS v3.4 (+ Fonts: Inter & Outfit)
- **Tools:**
  - `Biome`: Linter e formatador de alta performance (substitui ESLint/Prettier).

### Infraestrutura & DevOps
- **Docker:** Containerização (Dockerfile e docker-compose).
- **Git Hooks:** `Husky` + `Commitlint` + `Lint-staged` para garantir commits padronizados e código limpo.

---

## 🛠️ Instalação e Execução

### Pré-requisitos
- Node.js (v18+)
- Python (v3.10+)
- Docker (Opcional, mas recomendado)

### 1. Backend (Django)

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Migrações e Seed
python manage.py migrate
python manage.py shell < seed_services.py # Popula com serviços iniciais

# Rodar Servidor
python manage.py runserver
```

O servidor rodará em `http://localhost:8000`.

### 2. Frontend (Vue + Vite)

```bash
cd frontend
yarn install  # ou npm install
yarn dev      # ou npm run dev
```

A aplicação rodará em `http://localhost:5173`.

---

## 🛡️ Padrões de Qualidade (QA)

Este projeto utiliza **Hooks do Git** para garantir qualidade.

### Scripts de Verificação
- **Backend:** `black .`, `isort .`, `flake8 .`
- **Frontend:** `npx biome check --write .`

### Commits
Utilizamos **Conventional Commits**. Mensagens fora do padrão serão rejeitadas.
- ✅ `feat: adiciona componente de contato`
- ✅ `fix: corrige erro de conexão`
- ❌ `fiz o componente` (Bloqueado pelo Commitlint)

---

## 📦 Deploy

- **Backend:** Configurado para Railway (usa `whiteNoise` e `gunicorn`).
- **Frontend:** Configurado para Vercel.

---

**Desenvolvido por Pedro Fernandes**
