# SmartCity360 — Database Architecture & Schema Specification

## 1. Persistence Framework
SmartCity360 uses **PostgreSQL 16** with **SQLAlchemy 2.0 (Async)** as the primary Object-Relational Mapper (ORM) and **Alembic** for schema migrations.

### Standard Entity Fields (Audit Mixin)
Every primary table inherits standard audit and lifecycle fields:
- `id` (UUID / Integer Primary Key)
- `created_at` (TIMESTAMP WITH TIME ZONE, Default: UTC NOW)
- `updated_at` (TIMESTAMP WITH TIME ZONE, Auto-update on modification)
- `is_deleted` (BOOLEAN, Default: FALSE for soft-delete support)

---

## 2. Relational Schema Architecture (26 Municipal Domains)

```text
+---------------------------------------------------------------------------------+
|                                 CORE ERD OVERVIEW                               |
+---------------------------------------------------------------------------------+
|                                                                                 |
|   +---------------+ 1:N +-------------------+ 1:N +-------------------------+   |
|   |     Users     |---->|  CitizenProfiles  |     |   NotificationRecords   |   |
|   +---------------+     +-------------------+     +-------------------------+   |
|           | 1:N                                                                 |
|           +------------>+-------------------+ 1:N +-------------------------+   |
|                         |  DepartmentStaff  |---->|   WorkOrderAssignments  |   |
|                         +-------------------+     +-------------------------+   |
|                                                                                 |
|   +---------------+ 1:N +-------------------+ 1:N +-------------------------+   |
|   |  Departments  |---->| MunicipalServices |---->|     ServiceRequests     |   |
|   +---------------+     +-------------------+     +-------------------------+   |
|           | 1:N                                                |                |
|           +------------>+-------------------+                  |                |
|                         |    Complaints     |                  v                |
|                         +-------------------+ 1:1 +-------------------------+   |
|                                  |--------------->|       WorkOrders        |   |
|                                                   +-------------------------+   |
|                                                                | 1:N            |
|                                                   +-------------------------+   |
|                                                   |     WorkOrderTasks      |   |
|                                                   +-------------------------+   |
|                                                                                 |
|   +-------------------+ 1:N +-------------------+ 1:N +---------------------+   |
|   | Infrastructure    |---->| AssetInspections  |     |   AssetMaintenance  |   |
|   | Assets            |     +-------------------+     +---------------------+   |
|   +-------------------+                                                         |
|                                                                                 |
|   +-------------------+ 1:N +-------------------+ 1:N +---------------------+   |
|   | EmergencyIncidents|---->| EmergencyDispatch |<----|EmergencyResponseTeam|   |
|   +-------------------+     +-------------------+     +---------------------+   |
|                                                                                 |
+---------------------------------------------------------------------------------+
```

---

## 3. Entity Definitions by Functional Domain

### 3.1 Identity, RBAC & Audit
- `users`: Core authentication identity, email, hashed password, active status, phone.
- `roles`: Role definitions (Citizen, Staff, Supervisor, Admin, Emergency, etc.).
- `permissions`: Granular permission flags (`complaints:create`, `work_orders:assign`, etc.).
- `user_roles`: Many-to-many junction between users and roles.
- `citizen_profiles`: Citizen metadata, address line, ward ID, national ID token, emergency contact.
- `department_staff`: Association between staff user and municipal department, badge number, title.
- `audit_logs`: Immutable audit events tracking actor, action, resource, IP address, timestamp, delta payload.

### 3.2 Municipal Services & Citizen Requests
- `departments`: Municipal departments (Roads, Water, Sanitation, Electrical, Health, Safety).
- `service_categories`: High-level service classification (Permits, Utilities, Civic Complaints).
- `municipal_services`: Catalog items with processing timelines, fee amounts, and document requirements.
- `service_requests`: Submitted applications with state machine (`SUBMITTED` -> `UNDER_REVIEW` -> `APPROVED`).
- `service_documents`: Uploaded citizen verification documents with MIME validation.

### 3.3 Civic Complaints & Work Orders
- `complaint_categories`: Potholes, streetlights, garbage overflow, water leak, drainage, etc.
- `complaints`: Public civic complaints with GPS lat/lon, description, urgency, SLA deadlines, 9 statuses.
- `complaint_comments`: Department notes and citizen communication history.
- `complaint_status_history`: Auditable timestamped transitions across complaint lifecycle.
- `work_orders`: Municipal work tickets generated from complaints or scheduled maintenance.
- `work_order_tasks`: Granular action checklist for field technicians.
- `work_order_evidence`: Uploaded photo/document evidence confirming work completion.

### 3.4 Infrastructure, Utilities & Mobility
- `infrastructure_assets`: Bridges, roads, pipelines, buildings, traffic signals with condition status.
- `asset_inspections`: Scheduled structural condition assessments.
- `asset_maintenance`: Historical and upcoming repair work records.
- `streetlight_assets`: Geo-tagged streetlights, bulb type, wattage, operational status.
- `water_assets`: Distribution mains, valves, storage tanks, and flow monitoring.
- `waste_zones`: Municipal collection sectors, collection frequencies, depot locations.
- `waste_collection_requests`: Citizen bulk waste or missed collection tickets.
- `traffic_incidents`: Congestion alerts, signal failures, road detours.
- `transport_routes`: City bus routes, transit line IDs, operating frequencies.
- `transport_stops`: Geo-located bus stops and stations.
- `parking_locations`: Municipal parking lots, capacity, pricing models.
- `parking_sessions`: Active parking transactions and meter sessions.

### 3.5 Emergency, Facilities, Payments & Announcements
- `emergency_incidents`: High-priority 911/112 municipal emergency reports.
- `emergency_response_teams`: Police, Fire, Ambulance, Search & Rescue squads.
- `emergency_dispatches`: Active dispatches linking response teams to emergency incidents.
- `facilities`: Geo-referenced municipal facilities (hospitals, schools, fire houses, civic centers).
- `payment_transactions`: Financial ledger records, payment references, mock gateway responses.
- `payment_receipts`: Structured receipts with tax breakdown and digital verification hashes.
- `announcements`: Public bulletins with validity windows and priority badges.
- `city_events`: Community meetings, town halls, cultural festivals with attendance limits.
- `feedback_records`: Citizen satisfaction scores and service review notes.
- `notification_records`: Push/In-app/Email notifications sent to citizens or staff.

---

## 4. Indexing & Query Optimization
1. **Foreign Key Indexes**: B-tree indexes on all foreign key references (`user_id`, `department_id`, `complaint_id`).
2. **Compound Filtering Indexes**:
   - `idx_complaints_dept_status_sla` ON `complaints (department_id, status, sla_due_at)`
   - `idx_workorders_staff_status` ON `work_orders (assigned_staff_id, status)`
   - `idx_emergencies_severity_status` ON `emergency_incidents (severity, status)`
3. **Geospatial Indexes**:
   - Spatial indexing on `(latitude, longitude)` for fast bounding-box queries within citizen viewports.
