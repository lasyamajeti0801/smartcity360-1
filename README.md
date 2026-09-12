# SmartCity360: Integrated Urban Management & Citizen Services Platform

SmartCity360 is an enterprise-scale, production-ready municipal management platform that bridges the digital divide between citizens, city operations, public works, emergency responders, and administrative leadership.

Built on modern, decoupled architecture with **Python 3.12+ (FastAPI)** on the backend and **React 19 + TypeScript (Vite)** on the frontend, the platform integrates **26 comprehensive municipal modules** into a single cohesive, auditable system.

---

## Key Pillars & Architecture

### 1. Citizen Experience
- **Unified Civic Catalog**: Searchable repository of all municipal services, eligibility criteria, and digital application workflows.
- **Civic Issue Reporting**: 9-stage complaint lifecycle tracking with map-based GPS geolocating, evidence upload, SLA status, and citizen feedback.
- **Secure Civic Payments**: Transparent fee assessment, mock payment gateway ledger, digital receipts, and transaction history.
- **Accessible & Multilingual Architecture**: Screen-reader accessible UI (WCAG 2.1 AA compliant), responsive layouts tailored for mobile citizens.

### 2. Operational Control & Municipal Administration
- **Executive City Admin Console**: Real-time city pulse metrics, cross-department SLA compliance, budget tracking, and infrastructure health scores.
- **Department-Specific Command Desks**: Tailored operational workspaces for Roads, Sanitation, Water Supply, Electrical/Streetlights, and Transit.
- **Work-Order Dispatch & Verification**: Automatic conversion of citizen complaints into actionable field assignments with checklist verification and evidence capture.
- **Emergency Management & Real-time Triage**: Instant incident classification (Fire, Medical, Traffic, Flood), responder unit dispatch, and timeline tracking.

### 3. Open GIS & Geospatial Intelligence
- **Zero Paid API Key Dependency**: Fully powered by **Leaflet** and **OpenStreetMap** standards.
- **Multi-Layer City Map**: Infrastructure condition layers, active emergency incident clusters, complaint heatmaps, and public facility directories.

### 4. Data Science & Decision Support
- **Locally Executed Machine Learning**: Scikit-learn powered complaint category routing, SLA breach risk prediction, and infrastructure maintenance forecasting with transparent model metrics.

---

## System Architecture

```text
+-------------------------------------------------------------------------------+
|                             SMARTCITY360 CLIENTS                             |
|  [Citizen Portal]      [Staff Workdesk]      [Admin Console]    [Emergency]   |
+---------------------------------------+---------------------------------------+
                                        | HTTP/REST & WebSocket
+---------------------------------------v---------------------------------------+
|                       FASTAPI APPLICATION GATEWAY                             |
|  - Rate Limiter      - Request Correlation ID      - JWT/RBAC Auth Guard      |
|  - Security Headers  - Audit Log Middleware        - Structured Exception Hdl |
+---------------------------------------+---------------------------------------+
                                        |
  +--------------------+----------------+-------------------+----------------+
  |                    |                                    |                |
  v                    v                                    v                v
[Citizen & Auth]  [Civic Complaints]                   [Field Workorders] [Emergency]
[Services]        [Infrastructure & Utilities]         [Payments & GIS]   [Analytics]
  |                    |                                    |                |
  +--------------------+----------------+-------------------+----------------+
                                        |
+---------------------------------------v---------------------------------------+
|                          PERSISTENCE & EVENT LAYER                            |
|  PostgreSQL 16 (Relational/Spatial)  |  Redis 7 (Cache & Queue)  | Filesystem |
+-------------------------------------------------------------------------------+
```

---

## Directory Organization

```text
SmartCity360/
├── backend/                  # FastAPI Application
│   ├── app/
│   │   ├── api/v1/           # Modular REST API endpoints
│   │   ├── core/             # Configuration, database, security, logging
│   │   ├── middleware/       # Audit logging, rate limits, security headers
│   │   ├── models/           # SQLAlchemy 2.0 declarative database models
│   │   ├── repositories/     # Data access patterns
│   │   ├── schemas/          # Pydantic v2 validation models
│   │   ├── services/         # Domain business logic
│   │   └── utils/            # Shared helpers
│   └── tests/                # Pytest unit, integration, and API tests
├── frontend/                 # React 19 + TypeScript + Vite + Tailwind
│   ├── src/
│   │   ├── app/              # Routing and app entry
│   │   ├── components/       # Reusable UI, Layout, and GIS Map components
│   │   ├── features/         # Citizen, Admin, Staff, Emergency modules
│   │   ├── hooks/            # Custom React hooks
│   │   ├── services/         # API clients
│   │   ├── styles/           # Tailwind CSS styles
│   │   └── types/            # TypeScript interfaces
│   └── tests/                # Vitest & React Testing Library specs
├── ml/                       # Machine Learning models and inference engines
├── database/                 # Alembic migrations and seed datasets
├── scripts/                  # Automated verification & audit tooling
├── docs/                     # Architecture, security, API specifications
│   └── pull_requests/        # Structured PR records and branch manifests
├── docker/                   # Dockerfiles and container configurations
├── docker-compose.yml        # Multi-service local orchestrator
├── PROJECT_PROGRESS.md       # Real-time module & metric progress tracker
├── PROJECT_AUDIT.md          # Automated audit output
└── README.md                 # System overview and quickstart
```

---

## Getting Started Locally

### Prerequisites
- Python 3.12 or higher
- Node.js 20+ and npm 10+
- Git 2.40+
- Docker & Docker Compose (optional for containerized runtime)

### 1. Clone & Configure Environment
```bash
git clone <repository-url>
cd "Smart City 360"
cp .env.example .env
```

### 2. Backend Setup
```bash
cd backend
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```
- API Documentation (Swagger UI): `http://localhost:8000/docs`
- Health Checks: `http://localhost:8000/health`

### 3. Frontend Setup
```bash
cd frontend
npm install
npm run dev
```
- Access the web interface at `http://localhost:5173`

---

## Verification & Audit Tooling

SmartCity360 includes a zero-fake-metrics audit suite in `scripts/`:

```bash
# Run comprehensive quality audit and update PROJECT_AUDIT.md
python scripts/project_audit.py

# Inspect genuine production lines of code (excludes tests/cache/node_modules)
python scripts/count_loc.py

# Verify Git commit standards and conventional commit formats
python scripts/git_audit.py

# Verify pull request records and branch manifests
python scripts/pr_audit.py

# Run security checks
python scripts/security_audit.py
```

---

## License & Governance
Designed and maintained by the SmartCity360 Municipal Engineering Initiative.
Governed under Enterprise Civic Software Guidelines.
