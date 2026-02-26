# 🏎️ Veluxe — Premium Automotive Detailing

Veluxe is a modern, luxury-focused platform for premium automotive detailing services, inspired by the excellence of AoRaboni. It delivers a high-end digital experience for customers and a powerful management dashboard for the business owner.

## 🔗 Live Links

- **🚀 Production Site:** [veluxe-frontend-production.up.railway.app](https://veluxe-frontend-production.up.railway.app/)
- **🔐 Veluxe Manager (Dashboard):** [Login](/login) — *Contact the developer for access credentials.*

---

## ✨ Key Features

| Area | Description |
|------|-------------|
| **Landing Page** | Premium, responsive design with a high-conversion layout showcasing the value of each service. |
| **Service Catalog** | Dynamic listing of 16 real services — Ruby, Diamond & Bronze Sequences plus individual treatments. |
| **Atelier Experience** | Dedicated page highlighting the physical workspace and the care taken with every vehicle. |
| **Manager Dashboard** | Protected area for full CRUD management of services, pricing, and warranties in real time. |
| **Auth-Protected Routes** | Token-based authentication with route guards to secure the management panel. |
| **API Integration** | Vue 3 frontend seamlessly connected to a Django REST API. |

---

## 🚀 Tech Stack

### Frontend

| Technology | Purpose |
|------------|---------|
| **Vue.js 3** (Composition API) | Reactive UI framework |
| **TypeScript** | Type-safe JavaScript |
| **Vite** (Rolldown) | Lightning-fast dev server & build tool |
| **Vue Router 5** | Client-side routing with navigation guards |
| **Tailwind CSS 3.4** | Utility-first CSS framework |
| **Axios** | HTTP client for API communication |
| **PostCSS + Autoprefixer** | CSS processing pipeline |
| **Google Fonts** — Inter & Outfit | Premium typography |

### Backend

| Technology | Purpose |
|------------|---------|
| **Django 5** | Python web framework |
| **Django REST Framework** | RESTful API toolkit |
| **PostgreSQL 15** | Production-grade relational database |
| **Gunicorn** | WSGI HTTP server for production |
| **WhiteNoise** | Static file serving |
| **django-cors-headers** | Cross-origin request handling |
| **dj-database-url** | Database config via `DATABASE_URL` |
| **psycopg2** | PostgreSQL adapter for Python |

### Infrastructure & DevOps

| Technology | Purpose |
|------------|---------|
| **Docker** & **Docker Compose** | Containerized development & deployment |
| **Nginx** | Reverse proxy for the frontend container |
| **Railway** | Cloud hosting (monorepo deploy) |
| **Husky** | Git hooks automation |
| **lint-staged** | Pre-commit code quality checks |
| **Commitlint** | Enforced [Conventional Commits](https://www.conventionalcommits.org/) |

### Code Quality

| Tool | Scope |
|------|-------|
| **Biome** | Frontend linter & formatter (JS/TS/Vue/JSON) |
| **Black** | Python code formatter |
| **Flake8** | Python linter |
| **isort** | Python import sorter |

---

## 📁 Project Structure

```
veluxe/
├── backend/                # Django REST API
│   ├── core/               # Project settings & WSGI config
│   ├── services/           # Services app (models, views, serializers)
│   ├── Dockerfile          # Backend container image
│   ├── requirements.txt    # Python dependencies
│   └── manage.py
├── frontend/               # Vue 3 SPA
│   ├── src/
│   │   ├── components/     # Reusable UI components (Navbar, Hero, Services, etc.)
│   │   ├── views/          # Page-level components (Landing, Login, Space, Manager)
│   │   ├── router/         # Vue Router configuration
│   │   └── assets/         # Static assets
│   ├── Dockerfile          # Frontend container image (Nginx)
│   ├── nginx.conf          # Reverse proxy config
│   └── tailwind.config.js  # Custom theme (premium color palette)
├── docker-compose.yml      # Multi-service orchestration
├── railway.json            # Railway deployment config
├── biome.json              # Biome linter/formatter config
├── commitlint.config.js    # Commit message rules
└── package.json            # Root workspace (Husky, lint-staged)
```

---

## 🛠️ Local Development Setup

### Prerequisites

- **Node.js** v18+
- **Python** v3.12+
- **Yarn** (package manager)
- **Docker** (optional — for containerized setup)

### Option 1: Manual Setup

#### Backend (Django)

```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_real_data   # Seeds the 16 real services
python manage.py runserver
```

#### Frontend (Vue + Vite)

```bash
cd frontend
yarn install
yarn dev
```

### Option 2: Docker Compose

```bash
docker compose up --build
```

This starts all three services — **PostgreSQL**, **Backend (Gunicorn)**, and **Frontend (Nginx)** — exposing the app on `http://localhost`.

---

## 🛡️ Quality Standards

- **Automated Linting** — Pre-commit hooks via Husky + lint-staged ensure consistent code style across Python and TypeScript.
- **Conventional Commits** — All commit messages follow the [Conventional Commits](https://www.conventionalcommits.org/) specification, enforced by Commitlint.
- **Environment Isolation** — Protected environment variables and isolated database per environment.

---

## 📄 License

This project is licensed under the **ISC License** — see the [LICENSE](LICENSE) file for details.

---

**Built with a passion for automotive excellence and technical craftsmanship by Pedro Souza.**
