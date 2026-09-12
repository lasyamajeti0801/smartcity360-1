# SmartCity360 — Deployment & Infrastructure Guide

## 1. Containerized Architecture
SmartCity360 provides container specifications for container orchestration via **Docker** and **Docker Compose**.

### Services:
- `backend`: FastAPI async application container running with Uvicorn workers.
- `frontend`: React + TypeScript production bundle served via high-performance Nginx.
- `postgres`: PostgreSQL 16 database with PostGIS extensions.
- `redis`: Redis 7 in-memory cache and background job broker.

---

## 2. Docker Compose Deployment

```bash
# Start all platform services in the background
docker-compose up -d --build

# Inspect running service status
docker-compose ps

# View backend logs
docker-compose logs -f backend

# Run database migrations
docker-compose exec backend alembic upgrade head
```

---

## 3. Health & Readiness Monitoring
- Liveness Probe: `GET /health/live` (Checks process execution)
- Readiness Probe: `GET /health/ready` (Verifies database and redis connections)
- System Metrics: `GET /health`
