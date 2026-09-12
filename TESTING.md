# SmartCity360 — Testing Architecture & Quality Assurance

## 1. Testing Strategy
SmartCity360 incorporates a rigorous multi-tier testing methodology:
- **Unit Tests**: Domain logic, Pydantic schemas, password hashing, SLA calculation algorithms, and utility functions.
- **Integration Tests**: Repository data queries, database constraints, soft-delete operations, and mock payment transactions.
- **API Tests**: FastAPI endpoint tests utilizing `httpx.AsyncClient` checking HTTP status codes, headers, and RBAC authorization barriers.
- **Frontend Component Tests**: Vitest + React Testing Library checking component rendering, form validation, and user interaction.
- **Audit Verification Tests**: Verification of codebase compliance, LOC metrics, and zero-secret leaks.

---

## 2. Running Automated Tests

### Backend Test Suite (Pytest)
```bash
# Run all backend unit & API integration tests
pytest backend/tests -v

# Run with coverage report
pytest backend/tests --cov=backend/app --cov-report=term-missing
```

### Frontend Test Suite (Vitest)
```bash
cd frontend
npm test -- --run
```

### Audit Script Verification
```bash
python scripts/test_audit.py
python scripts/project_audit.py
```
