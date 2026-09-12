# SmartCity360 — System Architecture & Design Specification

## 1. Architectural Principles

SmartCity360 follows the **Clean Architecture / Layered Architecture** paradigm combined with **Domain-Driven Design (DDD)** concepts to decouple business logic from transport and persistence layers.

### Key Architectural Tenets:
1. **Separation of Concerns**: API routes handle HTTP serialization and authentication; Services encapsulate domain business rules; Repositories handle database querying; Models represent persistent relational tables.
2. **Predictable Dependency Flow**: Inward dependency rule (`API Routes` -> `Services` -> `Repositories` -> `Models / Entities`).
3. **Auditability & Traceability**: Every sensitive state change (complaint lifecycle, work order status, user privilege escalation, emergency dispatch) produces an immutable audit event record.
4. **Zero Paid Secret Dependency**: Core civic features (maps, mock payments, machine learning) run fully self-contained using OpenStreetMap, local SQLite/PostgreSQL schemas, and local scikit-learn models.
5. **No Single Point of Failure (Resilience)**: Health checks (`/health`, `/health/live`, `/health/ready`), structured exceptions, and graceful fallback for offline clients.

---

## 2. Bounded Contexts & Domain Breakdown

SmartCity360 organizes urban management into cohesive domains:

```text
+-----------------------------------------------------------------------------------+
|                                MUNICIPAL DOMAINS                                 |
+--------------------+---------------------+--------------------+-------------------+
| 1. Identity & Auth | 2. Citizen Services | 3. Operations & WO | 4. Infrastructure |
| - Users & Staff    | - Service Catalog   | - Complaints       | - Assets          |
| - RBAC & Perms     | - Request Workflows | - Work Orders      | - Water & Waste   |
| - Citizen Profiles | - Payment Receipts  | - Field Evidence   | - Streetlights    |
+--------------------+---------------------+--------------------+-------------------+
| 5. Public Safety   | 6. Mobility & GIS   | 7. Public Comms    | 8. Intelligence   |
| - Emergencies      | - Traffic Incidents | - Announcements    | - ML Triage       |
| - Dispatch Teams   | - Transit Routes    | - Events & Calendar| - City Analytics  |
| - Facility Desk    | - Parking Sessions  | - Citizen Feedback | - SLA Prediction  |
+--------------------+---------------------+--------------------+-------------------+
```

---

## 3. Data Flow & Execution Workflows

### 3.1 Citizen Civic Complaint Lifecycle

```text
[Citizen Frontend]
       |  (POST /api/v1/complaints with GPS coords, photos, category)
       v
[FastAPI Gateway] -> Auth Guard (Citizen Role) -> Rate Limiter
       v
[Complaint Service]
       |-- 1. Validate category & SLA baseline
       |-- 2. Scikit-learn priority prediction / auto-tagging
       |-- 3. Persist Complaint (Status: NEW)
       |-- 4. Emit Audit Event ("COMPLAINT_CREATED")
       |-- 5. Dispatch in-app notification to Citizen
       v
[Department Routing Engine]
       |-- 6. Match department by category/ward
       |-- 7. Transition status: NEW -> UNDER_REVIEW -> ASSIGNED
       v
[Field Operations / Work Order Service]
       |-- 8. Generate WorkOrder linked to Complaint #
       |-- 9. Assign Field Technician
       v
[Field Technician App]
       |-- 10. Accept assignment -> IN_PROGRESS
       |-- 11. Complete tasks, upload resolution photo
       |-- 12. Submit for Supervisor Verification
       v
[Supervisor Desk]
       |-- 13. Verify evidence -> RESOLVED
       |-- 14. Close Complaint & prompt Citizen for rating
```

---

## 4. Role-Based Access Control (RBAC) Matrix

SmartCity360 enforces 8 distinct personas with fine-grained permissions:

| Persona | Permitted Capabilities | Boundary |
| :--- | :--- | :--- |
| **Citizen** | Discover services, lodge complaints, track requests, pay fees, rate resolutions | Own profile & requests only |
| **Department Staff** | View department complaints, triage requests, recommend actions | Department scope |
| **Field Staff** | View assigned work orders, update task checklists, submit field evidence | Assigned work orders only |
| **Supervisor** | Assign staff, approve/reject work order completions, monitor department SLAs | Department scope |
| **Emergency Operator**| Create emergency incidents, triage severity, dispatch response teams | City-wide emergency scope |
| **Municipal Officer** | Cross-department operational oversight, policy notices, event scheduling | Municipal authority |
| **City Administrator**| Department configuration, SLA parameter management, analytics, audit trail | City-wide operational |
| **System Administrator**| User administration, role definition, system settings, database maintenance | Platform infrastructure |

---

## 5. Geospatial & GIS Architecture

The GIS subsystem is implemented without proprietary map API keys:
- **Map Engine**: Leaflet 1.9+ integrated with OpenStreetMap tile servers.
- **Data Layers**: GeoJSON features for assets, roads, complaints, emergency zones, and public facilities.
- **Clustering & Heatmaps**: Marker clustering for dense complaints and dynamic density analysis.
- **Coordinate Standards**: WGS84 (EPSG:4326) latitude and longitude with bounding box spatial indexing.

---

## 6. Observability, Telemetry & Security Headers

Every request processed by SmartCity360 flows through mandatory middleware:
- **`X-Request-ID`**: Distributed correlation ID passed from client or generated on ingress.
- **Security Headers**:
  - `Content-Security-Policy: default-src 'self'`
  - `X-Content-Type-Options: nosniff`
  - `X-Frame-Options: DENY`
  - `Strict-Transport-Security: max-age=31536000; includeSubDomains`
- **Audit Logging**: Asynchronous recording of actor, action, resource, timestamp, and client metadata.
