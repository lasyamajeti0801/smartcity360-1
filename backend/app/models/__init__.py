"""
SmartCity360 - Unified Relational Models Package
Exports all SQLAlchemy models across the 26 civic modules.
"""

from backend.app.core.database import Base, TimeStampedBase

# 1. Identity & RBAC
from backend.app.models.user import (
    User,
    Role,
    Permission,
    UserRole,
    RolePermission,
    CitizenProfile,
    DepartmentStaff
)

# 2. Municipal Departments & Service Catalog
from backend.app.models.department import (
    Department,
    ServiceCategory,
    MunicipalService
)

# 3. Citizen Service Requests
from backend.app.models.service_request import (
    ServiceRequest,
    ServiceDocument,
    ServiceRequestHistory,
    STATUS_DRAFT,
    STATUS_SUBMITTED,
    STATUS_UNDER_REVIEW,
    STATUS_APPROVED,
    STATUS_REJECTED,
    STATUS_IN_PROGRESS,
    STATUS_COMPLETED
)

# 4. Civic Complaints
from backend.app.models.complaint import (
    ComplaintCategory,
    Complaint,
    ComplaintComment,
    ComplaintStatusHistory,
    STATUS_NEW,
    STATUS_UNDER_REVIEW,
    STATUS_ASSIGNED,
    STATUS_IN_PROGRESS,
    STATUS_ON_HOLD,
    STATUS_RESOLVED,
    STATUS_CLOSED,
    STATUS_REOPENED,
    STATUS_REJECTED
)

# 5. Work Orders
from backend.app.models.work_order import (
    WorkOrder,
    WorkOrderTask,
    WorkOrderEvidence,
    WO_STATUS_CREATED,
    WO_STATUS_ASSIGNED,
    WO_STATUS_ACCEPTED,
    WO_STATUS_IN_PROGRESS,
    WO_STATUS_BLOCKED,
    WO_STATUS_SUBMITTED,
    WO_STATUS_VERIFICATION,
    WO_STATUS_COMPLETED,
    WO_STATUS_CANCELLED
)

# 6. Infrastructure, Utilities & Sanitation
from backend.app.models.infrastructure import (
    InfrastructureAsset,
    AssetInspection,
    AssetMaintenance,
    StreetlightAsset,
    WaterAsset,
    WasteZone,
    WasteCollectionRequest
)

# 7. Mobility, Transit & Parking
from backend.app.models.mobility import (
    TrafficIncident,
    TransportRoute,
    TransportStop,
    ParkingLocation,
    ParkingSession
)

# 8. Emergency, Dispatch & Facilities
from backend.app.models.emergency import (
    EmergencyIncident,
    EmergencyResponseTeam,
    EmergencyDispatch,
    Facility
)

# 9. Civic Engagement, Payments & Notifications
from backend.app.models.engagement import (
    PaymentTransaction,
    PaymentReceipt,
    NotificationRecord,
    Announcement,
    CityEvent,
    FeedbackRecord
)

# 10. AI/ML, Analytics & Audit
from backend.app.models.analytics import (
    MLModelRegistry,
    PredictionLog,
    AnalyticsSnapshot,
    AuditLog
)

__all__ = [
    "Base",
    "TimeStampedBase",
    "User",
    "Role",
    "Permission",
    "UserRole",
    "RolePermission",
    "CitizenProfile",
    "DepartmentStaff",
    "Department",
    "ServiceCategory",
    "MunicipalService",
    "ServiceRequest",
    "ServiceDocument",
    "ServiceRequestHistory",
    "ComplaintCategory",
    "Complaint",
    "ComplaintComment",
    "ComplaintStatusHistory",
    "WorkOrder",
    "WorkOrderTask",
    "WorkOrderEvidence",
    "InfrastructureAsset",
    "AssetInspection",
    "AssetMaintenance",
    "StreetlightAsset",
    "WaterAsset",
    "WasteZone",
    "WasteCollectionRequest",
    "TrafficIncident",
    "TransportRoute",
    "TransportStop",
    "ParkingLocation",
    "ParkingSession",
    "EmergencyIncident",
    "EmergencyResponseTeam",
    "EmergencyDispatch",
    "Facility",
    "PaymentTransaction",
    "PaymentReceipt",
    "NotificationRecord",
    "Announcement",
    "CityEvent",
    "FeedbackRecord",
    "MLModelRegistry",
    "PredictionLog",
    "AnalyticsSnapshot",
    "AuditLog"
]
