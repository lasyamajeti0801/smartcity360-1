# SmartCity360 — Git Workflow & Pull Request Standards

## 1. Commit Standards (Conventional Commits)
SmartCity360 strictly adheres to the **Conventional Commits 1.0.0** specification.

### Commit Format
```text
<type>(<scope>): <subject>

[optional body with rationale, affected components, and testing notes]

[optional footer with reference issue/PR: Ref: #42]
```

### Approved Types
- `feat`: New user-facing feature or municipal domain capability
- `fix`: Bug fix in backend, frontend, or data layer
- `docs`: Documentation updates (architecture, API, guides)
- `style`: Formatting, missing semicolons, stylistic tweaks (no code logic changes)
- `refactor`: Code reorganization with identical runtime behavior
- `perf`: Performance optimizations (indexes, caching, bundling)
- `test`: Adding or refactoring automated tests
- `build`: Build system, dependencies, or package updates
- `ci`: CI/CD workflow modifications
- `chore`: Maintenance tasks, repo audits, housekeeping
- `security`: Security enhancements, sanitization, dependency vulnerability fixes

### Sample Commits
```bash
feat(auth): implement citizen registration with argon2 password hashing
feat(complaints): add 9-stage complaint status transition state machine
feat(gis): integrate leaflet openstreetmap layer with marker clustering
test(work-orders): add integration tests for field technician dispatch
security(middleware): enforce strict csp and rate limiting on auth endpoints
```

---

## 2. Branching & Pull Request Lifecycle
To support rigorous team collaboration and meet the 80+ PR benchmark:
- **Base Branch**: `main` (protected production branch).
- **Feature Branches**: `feat/<domain>-<feature-name>` (e.g., `feat/auth-jwt-guard`, `feat/gis-leaflet-viewer`).
- **Fix Branches**: `fix/<domain>-<issue-name>` (e.g., `fix/complaints-sla-calc`).
- **PR Metadata Records**: Maintained in `docs/pull_requests/PR_<number>_<slug>.json` to ensure 100% auditable documentation even in disconnected/local developer environments.

### Pull Request Quality Checklist
Each PR must include:
1. Clear statement of problem & implemented solution
2. Affected files and municipal domains
3. Unit and integration test verification commands
4. Security & data privacy considerations
5. Passing audit check (`python scripts/project_audit.py`)
