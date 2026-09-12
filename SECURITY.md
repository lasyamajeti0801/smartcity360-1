# SmartCity360 — Security Policy & Controls

## 1. Authentication & Session Management
- **Password Security**: Passwords are cryptographically hashed using **Argon2id** or **Bcrypt** with a work factor of 12. Plaintext passwords never touch database persistence or logs.
- **JWT Authentication**: Asymmetric/HMAC-SHA256 signed JSON Web Tokens with short expiration (15–60 minutes) and cryptographically random refresh tokens stored in HTTP-only, SameSite cookies.
- **Brute Force Protection**: Account lockout policies and IP-based rate limiting on sensitive endpoints (`/api/v1/auth/login`, `/api/v1/auth/register`, `/api/v1/auth/reset-password`).

---

## 2. Authorization & Granular RBAC
- **Principle of Least Privilege**: Access to municipal endpoints is guarded by declarative role and permission dependencies.
- **Tenant & Object Isolation**: Citizens can only access complaints, requests, and payment receipts associated with their verified account (`user_id == current_user.id`).
- **Staff Boundary Enforcement**: Department staff are restricted to assets, work orders, and complaints originating within their assigned municipal department.

---

## 3. Data Protection & File Upload Safeguards
- **File Validation**:
  - Whitelisted MIME types (`image/jpeg`, `image/png`, `image/webp`, `application/pdf`).
  - Magic byte verification preventing spoofed file extensions.
  - Maximum upload size capped at 25MB per file.
  - Random UUID-based filename generation to prevent directory traversal (`../../etc/passwd`).
  - Stored outside web execution roots.
- **Data Sanitization**: Pydantic v2 and Zod schema validation on ingress; parameterized SQLAlchemy queries to eliminate SQL Injection (SQLi).
- **Zero Third-Party Secret Dependency**: No hardcoded API keys for external services.

---

## 4. Security Incident Response
To report a security vulnerability in SmartCity360, email `security@smartcity360.local`. Critical patches are deployed via automated CI/CD security pipelines.
