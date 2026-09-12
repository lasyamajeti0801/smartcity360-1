"""
SmartCity360 - AI/ML Decision Support, Urban Analytics & Audit Models
Covers Machine Learning registry, inference logs, daily civic metric snapshots,
and immutable security audit logging.
"""

from datetime import datetime
from typing import Optional
from sqlalchemy import String, Text, ForeignKey, DateTime, Integer, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship
from backend.app.core.database import TimeStampedBase

class MLModelRegistry(TimeStampedBase):
    __tablename__ = "ml_models"

    model_key: Mapped[str] = mapped_column(String(64), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(128), nullable=False)
    version: Mapped[str] = mapped_column(String(32), nullable=False)
    task_type: Mapped[str] = mapped_column(String(64), nullable=False)  # CLASSIFICATION, REGRESSION, CLUSTERING
    framework: Mapped[str] = mapped_column(String(64), default="scikit-learn", nullable=False)
    accuracy_metric_name: Mapped[str] = mapped_column(String(32), default="F1-Score", nullable=False)
    accuracy_metric_value: Mapped[float] = mapped_column(Float, default=0.88, nullable=False)
    model_artifact_path: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    is_active_for_inference: Mapped[bool] = mapped_column(default=True, nullable=False)

class PredictionLog(TimeStampedBase):
    __tablename__ = "prediction_logs"

    model_id: Mapped[str] = mapped_column(String(36), ForeignKey("ml_models.id", ondelete="CASCADE"), index=True, nullable=False)
    input_payload: Mapped[str] = mapped_column(Text, nullable=False)
    prediction_output: Mapped[str] = mapped_column(Text, nullable=False)
    confidence_score: Mapped[float] = mapped_column(Float, nullable=False)
    inference_latency_ms: Mapped[float] = mapped_column(Float, nullable=False)

    model: Mapped["MLModelRegistry"] = relationship("MLModelRegistry")

class AnalyticsSnapshot(TimeStampedBase):
    __tablename__ = "analytics_snapshots"

    snapshot_date: Mapped[datetime] = mapped_column(DateTime(timezone=True), index=True, nullable=False)
    department_code: Mapped[str] = mapped_column(String(32), index=True, nullable=False)
    metric_name: Mapped[str] = mapped_column(String(64), index=True, nullable=False)  # RESOLUTION_TIME_HOURS, SLA_COMPLIANCE_PCT
    metric_value: Mapped[float] = mapped_column(Float, nullable=False)
    period_type: Mapped[str] = mapped_column(String(32), default="DAILY", nullable=False)  # DAILY, WEEKLY, MONTHLY

class AuditLog(TimeStampedBase):
    __tablename__ = "audit_logs"

    actor_id: Mapped[Optional[str]] = mapped_column(String(36), ForeignKey("users.id", ondelete="SET NULL"), index=True, nullable=True)
    action: Mapped[str] = mapped_column(String(64), index=True, nullable=False)  # USER_LOGIN, COMPLAINT_STATUS_CHANGE, DISPATCH_SENT
    resource_type: Mapped[str] = mapped_column(String(64), index=True, nullable=False)  # complaint, work_order, user, emergency
    resource_id: Mapped[str] = mapped_column(String(64), index=True, nullable=False)
    ip_address: Mapped[Optional[str]] = mapped_column(String(45), nullable=True)
    user_agent: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    details: Mapped[str] = mapped_column(Text, default="{}", nullable=False)
