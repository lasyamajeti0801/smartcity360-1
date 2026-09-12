"""
SmartCity360 - Urban Planning & Zoning Regulation Statutory Business Rules Engine
Domain: urban_planning
"""

from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass

from .models import UrbanPlanningStatus, UrbanPlanningPriority

@dataclass
class UrbanPlanningRuleResult:
    passed: bool
    rule_code: str
    severity: str
    explanation: str
    recommended_action: str
    remediation_cost_estimate: float = 0.0

def evaluate_urban_planning_statute_01(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 01 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-001'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_02(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 02 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-002'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_03(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 03 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-003'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_04(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 04 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-004'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_05(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 05 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-005'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_06(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 06 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-006'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_07(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 07 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-007'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_08(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 08 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-008'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_09(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 09 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-009'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_10(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 10 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-010'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_11(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 11 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-011'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_12(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 12 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-012'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_13(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 13 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-013'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_14(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 14 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-014'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_15(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 15 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-015'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_16(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 16 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-016'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_17(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 17 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-017'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_18(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 18 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-018'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_19(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 19 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-019'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_20(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 20 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-020'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_21(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 21 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-021'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_22(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 22 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-022'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_23(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 23 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-023'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_24(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 24 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-024'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_25(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 25 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-025'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_26(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 26 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-026'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_27(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 27 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-027'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_28(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 28 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-028'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_29(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 29 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-029'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_30(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 30 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-030'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_31(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 31 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-031'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_32(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 32 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-032'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_33(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 33 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-033'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_34(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 34 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-034'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_35(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 35 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-035'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_36(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 36 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-036'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_37(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 37 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-037'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_38(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 38 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-038'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_39(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 39 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-039'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_40(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 40 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-040'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_41(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 41 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-041'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_42(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 42 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-042'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_43(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 43 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-043'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_44(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 44 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-044'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_45(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 45 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-045'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_46(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 46 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-046'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_47(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 47 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-047'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_48(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 48 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-048'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_49(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 49 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-049'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_50(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 50 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-050'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_51(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 51 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-051'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_52(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 52 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-052'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_53(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 53 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-053'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_54(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 54 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-054'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_55(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 55 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-055'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_56(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 56 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-056'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_57(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 57 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-057'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_58(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 58 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-058'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_59(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 59 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-059'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_60(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 60 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-060'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_61(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 61 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-061'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_62(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 62 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-062'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_63(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 63 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-063'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_64(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 64 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-064'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_65(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 65 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-065'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_66(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 66 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-066'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_67(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 67 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-067'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_68(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 68 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-068'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_69(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 69 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-069'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_70(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 70 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-070'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_71(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 71 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-071'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_72(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 72 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-072'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_73(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 73 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-073'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_74(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 74 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-074'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_75(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 75 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-075'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_76(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 76 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-076'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_77(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 77 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-077'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_78(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 78 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-078'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_79(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 79 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-079'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_80(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 80 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-080'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_81(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 81 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-081'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_82(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 82 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-082'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_83(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 83 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-083'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_84(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 84 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-084'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_85(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 85 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-085'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_86(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 86 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-086'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_87(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 87 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-087'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_88(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 88 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-088'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_89(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 89 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-089'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_90(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 90 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-090'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_91(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 91 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-091'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_92(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 92 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-092'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_93(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 93 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-093'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_94(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 94 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-094'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_95(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 95 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-095'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_96(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 96 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-096'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_97(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 97 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-097'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_98(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 98 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-098'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_99(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 99 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-099'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_100(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 100 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-100'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_101(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 101 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-101'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_102(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 102 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-102'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_103(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 103 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-103'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_104(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 104 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-104'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_105(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 105 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-105'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_106(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 106 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-106'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_107(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 107 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-107'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_108(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 108 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-108'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_109(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 109 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-109'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_110(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 110 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-110'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_111(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 111 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-111'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_112(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 112 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-112'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_113(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 113 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-113'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_114(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 114 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-114'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_115(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 115 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-115'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_116(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 116 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-116'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_117(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 117 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-117'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_118(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 118 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-118'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_119(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 119 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-119'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_120(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 120 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-120'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_121(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 121 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-121'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_122(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 122 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-122'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_123(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 123 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-123'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_124(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 124 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-124'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_125(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 125 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-125'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_126(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 126 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-126'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_127(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 127 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-127'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_128(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 128 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-128'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_129(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 129 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-129'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_urban_planning_statute_130(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> UrbanPlanningRuleResult:
    """Statutory Evaluation Rule 130 for Urban Planning & Zoning Regulation."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-URBA-130'

    if metric > limit:
        return UrbanPlanningRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return UrbanPlanningRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return UrbanPlanningRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )
