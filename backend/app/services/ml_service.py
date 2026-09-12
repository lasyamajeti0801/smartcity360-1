"""
SmartCity360 - AI Decision Support & NLP Inference Service
Loads persisted scikit-learn pipeline artifacts for:
- Automatic priority classification (CRITICAL, HIGH, MEDIUM, LOW)
- Automated departmental routing (ROADS, SANITATION, ELECTRICAL, WATER)
- Model registry metrics and metadata reporting
"""

import json
import logging
from pathlib import Path
from typing import Dict, Any, Optional
import joblib

logger = logging.getLogger(__name__)

# Find ML artifacts directory relative to repository root
REPO_ROOT = Path(__file__).resolve().parent.parent.parent.parent
ARTIFACTS_DIR = REPO_ROOT / "ml" / "artifacts"

class MLDecisionService:
    _instance: Optional["MLDecisionService"] = None
    _priority_model = None
    _department_model = None
    _priority_metrics: Dict[str, Any] = {}
    _department_metrics: Dict[str, Any] = {}

    def __init__(self):
        self._load_artifacts()

    def _load_artifacts(self):
        priority_path = ARTIFACTS_DIR / "priority_classifier_v1.joblib"
        dept_path = ARTIFACTS_DIR / "department_classifier_v1.joblib"
        p_metrics_path = ARTIFACTS_DIR / "priority_metrics.json"
        d_metrics_path = ARTIFACTS_DIR / "department_metrics.json"

        if priority_path.exists():
            try:
                self._priority_model = joblib.load(priority_path)
                logger.info(f"[MLService] Priority model loaded successfully from {priority_path}")
            except Exception as e:
                logger.warning(f"[MLService] Failed to load priority model: {e}")

        if dept_path.exists():
            try:
                self._department_model = joblib.load(dept_path)
                logger.info(f"[MLService] Department model loaded successfully from {dept_path}")
            except Exception as e:
                logger.warning(f"[MLService] Failed to load department model: {e}")

        if p_metrics_path.exists():
            try:
                with open(p_metrics_path, "r", encoding="utf-8") as f:
                    self._priority_metrics = json.load(f)
            except Exception as e:
                logger.warning(f"[MLService] Failed to load priority metrics: {e}")

        if d_metrics_path.exists():
            try:
                with open(d_metrics_path, "r", encoding="utf-8") as f:
                    self._department_metrics = json.load(f)
            except Exception as e:
                logger.warning(f"[MLService] Failed to load department metrics: {e}")

    @classmethod
    def get_instance(cls) -> "MLDecisionService":
        if cls._instance is None:
            cls._instance = MLDecisionService()
        return cls._instance

    def predict_priority(self, title: str, description: str) -> Dict[str, Any]:
        """Classify complaint text into priority level with confidence scores."""
        combined_text = f"{title} {description}".strip()
        if not combined_text:
            return {"priority": "MEDIUM", "confidence": 0.5, "model_version": "fallback"}

        if self._priority_model is None:
            self._load_artifacts()

        if self._priority_model is not None:
            try:
                pred_label = self._priority_model.predict([combined_text])[0]
                proba_arr = self._priority_model.predict_proba([combined_text])[0]
                classes = list(self._priority_model.classes_)
                class_probs = {cls: round(float(prob), 4) for cls, prob in zip(classes, proba_arr)}
                confidence = round(float(max(proba_arr)), 4)

                return {
                    "priority": pred_label,
                    "confidence": confidence,
                    "probabilities": class_probs,
                    "model_version": self._priority_metrics.get("version", "1.0.0"),
                    "algorithm": self._priority_metrics.get("classifier", "LogisticRegression")
                }
            except Exception as e:
                logger.error(f"[MLService] Inference error during priority classification: {e}")

        # Rule-based fallback if model not loaded
        lower_t = combined_text.lower()
        if any(w in lower_t for w in ["fire", "lethal", "burst", "hazard", "blackout", "electrocution"]):
            return {"priority": "CRITICAL", "confidence": 0.9, "model_version": "heuristic_fallback"}
        if any(w in lower_t for w in ["flood", "pothole", "severe", "injury", "gridlock"]):
            return {"priority": "HIGH", "confidence": 0.8, "model_version": "heuristic_fallback"}
        return {"priority": "MEDIUM", "confidence": 0.7, "model_version": "heuristic_fallback"}

    def predict_department(self, title: str, description: str) -> Dict[str, Any]:
        """Classify complaint text into responsible municipal department."""
        combined_text = f"{title} {description}".strip()
        if not combined_text:
            return {"department": "ADMIN", "confidence": 0.5, "model_version": "fallback"}

        if self._department_model is None:
            self._load_artifacts()

        if self._department_model is not None:
            try:
                pred_label = self._department_model.predict([combined_text])[0]
                proba_arr = self._department_model.predict_proba([combined_text])[0]
                classes = list(self._department_model.classes_)
                class_probs = {cls: round(float(prob), 4) for cls, prob in zip(classes, proba_arr)}
                confidence = round(float(max(proba_arr)), 4)

                return {
                    "department": pred_label,
                    "confidence": confidence,
                    "probabilities": class_probs,
                    "model_version": self._department_metrics.get("version", "1.0.0"),
                    "algorithm": self._department_metrics.get("classifier", "LogisticRegression")
                }
            except Exception as e:
                logger.error(f"[MLService] Inference error during department routing: {e}")

        # Rule-based fallback
        lower_t = combined_text.lower()
        if any(w in lower_t for w in ["pothole", "road", "asphalt", "crater"]):
            return {"department": "ROADS", "confidence": 0.85, "model_version": "heuristic_fallback"}
        if any(w in lower_t for w in ["garbage", "trash", "waste", "bin"]):
            return {"department": "SANITATION", "confidence": 0.85, "model_version": "heuristic_fallback"}
        if any(w in lower_t for w in ["light", "pole", "wire", "signal", "traffic", "electric"]):
            return {"department": "ELECTRICAL", "confidence": 0.85, "model_version": "heuristic_fallback"}
        if any(w in lower_t for w in ["water", "pipe", "leak", "tap"]):
            return {"department": "WATER", "confidence": 0.85, "model_version": "heuristic_fallback"}
        return {"department": "ADMIN", "confidence": 0.5, "model_version": "heuristic_fallback"}

    def get_registry_manifest(self) -> Dict[str, Any]:
        """Returns comprehensive model registry and validation reports."""
        return {
            "registered_models": [
                {
                    "name": "complaint_priority_classifier",
                    "status": "DEPLOYED" if self._priority_model is not None else "NOT_LOADED",
                    "metrics": self._priority_metrics
                },
                {
                    "name": "department_routing_classifier",
                    "status": "DEPLOYED" if self._department_model is not None else "NOT_LOADED",
                    "metrics": self._department_metrics
                }
            ]
        }

ml_service = MLDecisionService.get_instance()
