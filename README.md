# 🏎️ Veluxe - Estética Automotiva Premium

Veluxe é uma plataforma moderna e luxuosa para serviços de estética automotiva de alto padrão, inspirada na excelência da AoRaboni. O projeto oferece uma experiência digital premium para clientes e uma ferramenta robusta de gestão para o proprietário.

## 🔗 Links de Acesso

- **🚀 Site Live (Produção):** [https://veluxe-frontend-production.up.railway.app/](https://veluxe-frontend-production.up.railway.app/)
- **🔐 Veluxe Manager (Dashboard):** [Acesse aqui](/login)
  - *Consulte o desenvolvedor para credenciais de acesso.*

---

## ✨ Funcionalidades Principais

- **Landing Page Premium:** Design responsivo, moderno e de alta conversão, focado em mostrar o valor dos serviços.
- **Catálogo Detalhado:** Exibição dinâmica de 16 serviços reais (Sequências Rubi, Diamante, Bronze e tratamentos individuais).
- **Atelier Experience:** Página dedicada para mostrar o ambiente físico e o cuidado com os veículos.
- **Dashboard do Gestor:** Área restrita para cadastro, edição e exclusão de serviços, preços e garantias em tempo real.
- **Integração API:** Frontend Vue 3 conectado a um Backend Django REST com autenticação segura.

---

## 🚀 Tecnologias Utilizadas

### Backend
- **Framework:** Django & Django REST Framework (DRF)
- **Database:** PostgreSQL (Railway)
- **Tools:** `Black`, `Flake8`, `Isort` (estilização e qualidade).

### Frontend
- **Framework:** Vue.js 3 (Composition API) + TypeScript
- **Styling:** Tailwind CSS v3.4 (+ Fonts: Inter & Outfit)
- **Tools:** `Biome` (Linter & Formatter).

### Infraestrutura & DevOps
- **Deploy:** Railway (Monorepo com Docker).
- **Padrões:** Conventional Commits + Husky + Commitlint.

---

## 🛠️ Configuração Local (Desenvolvimento)

### Pré-requisitos
- Node.js (v18+)
- Python (v3.12+)
- Docker (Opcional)

### 1. Backend (Django)
```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_real_data # Popula com os 16 serviços reais
python manage.py runserver
```

### 2. Frontend (Vue + Vite)
```bash
cd frontend
yarn install
yarn dev
```

---

## 🛡️ Padrões de Qualidade

Este projeto segue rigorosos padrões de qualidade:
- **Linting:** Automatizado via hooks para garantir código limpo.
- **Commits:** Padronizados seguindo `Conventional Commits`.
- **Produção:** Variáveis de ambiente protegidas e banco de dados isolado.

---

**Desenvolvido com foco em excelência estética e técnica por Pedro Fernandes.**
