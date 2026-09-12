"""
SmartCity360 - Municipal Taxation & Revenue Audit Statutory Business Rules Engine
Domain: tax_and_revenue
"""

from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass

from .models import TaxAndRevenueStatus, TaxAndRevenuePriority

@dataclass
class TaxAndRevenueRuleResult:
    passed: bool
    rule_code: str
    severity: str
    explanation: str
    recommended_action: str
    remediation_cost_estimate: float = 0.0

def evaluate_tax_and_revenue_statute_01(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> TaxAndRevenueRuleResult:
    """Statutory Evaluation Rule 01 for Municipal Taxation & Revenue Audit."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-TAX_-001'

    if metric > limit:
        return TaxAndRevenueRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return TaxAndRevenueRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return TaxAndRevenueRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_tax_and_revenue_statute_02(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> TaxAndRevenueRuleResult:
    """Statutory Evaluation Rule 02 for Municipal Taxation & Revenue Audit."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-TAX_-002'

    if metric > limit:
        return TaxAndRevenueRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return TaxAndRevenueRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return TaxAndRevenueRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_tax_and_revenue_statute_03(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> TaxAndRevenueRuleResult:
    """Statutory Evaluation Rule 03 for Municipal Taxation & Revenue Audit."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-TAX_-003'

    if metric > limit:
        return TaxAndRevenueRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return TaxAndRevenueRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return TaxAndRevenueRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_tax_and_revenue_statute_04(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> TaxAndRevenueRuleResult:
    """Statutory Evaluation Rule 04 for Municipal Taxation & Revenue Audit."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-TAX_-004'

    if metric > limit:
        return TaxAndRevenueRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return TaxAndRevenueRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return TaxAndRevenueRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_tax_and_revenue_statute_05(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> TaxAndRevenueRuleResult:
    """Statutory Evaluation Rule 05 for Municipal Taxation & Revenue Audit."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-TAX_-005'

    if metric > limit:
        return TaxAndRevenueRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return TaxAndRevenueRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return TaxAndRevenueRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_tax_and_revenue_statute_06(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> TaxAndRevenueRuleResult:
    """Statutory Evaluation Rule 06 for Municipal Taxation & Revenue Audit."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-TAX_-006'

    if metric > limit:
        return TaxAndRevenueRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return TaxAndRevenueRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return TaxAndRevenueRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_tax_and_revenue_statute_07(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> TaxAndRevenueRuleResult:
    """Statutory Evaluation Rule 07 for Municipal Taxation & Revenue Audit."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-TAX_-007'

    if metric > limit:
        return TaxAndRevenueRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return TaxAndRevenueRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return TaxAndRevenueRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_tax_and_revenue_statute_08(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> TaxAndRevenueRuleResult:
    """Statutory Evaluation Rule 08 for Municipal Taxation & Revenue Audit."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-TAX_-008'

    if metric > limit:
        return TaxAndRevenueRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return TaxAndRevenueRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return TaxAndRevenueRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_tax_and_revenue_statute_09(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> TaxAndRevenueRuleResult:
    """Statutory Evaluation Rule 09 for Municipal Taxation & Revenue Audit."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-TAX_-009'

    if metric > limit:
        return TaxAndRevenueRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return TaxAndRevenueRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return TaxAndRevenueRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_tax_and_revenue_statute_10(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> TaxAndRevenueRuleResult:
    """Statutory Evaluation Rule 10 for Municipal Taxation & Revenue Audit."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-TAX_-010'

    if metric > limit:
        return TaxAndRevenueRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return TaxAndRevenueRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return TaxAndRevenueRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_tax_and_revenue_statute_11(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> TaxAndRevenueRuleResult:
    """Statutory Evaluation Rule 11 for Municipal Taxation & Revenue Audit."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-TAX_-011'

    if metric > limit:
        return TaxAndRevenueRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return TaxAndRevenueRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return TaxAndRevenueRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_tax_and_revenue_statute_12(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> TaxAndRevenueRuleResult:
    """Statutory Evaluation Rule 12 for Municipal Taxation & Revenue Audit."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-TAX_-012'

    if metric > limit:
        return TaxAndRevenueRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return TaxAndRevenueRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return TaxAndRevenueRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_tax_and_revenue_statute_13(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> TaxAndRevenueRuleResult:
    """Statutory Evaluation Rule 13 for Municipal Taxation & Revenue Audit."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-TAX_-013'

    if metric > limit:
        return TaxAndRevenueRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return TaxAndRevenueRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return TaxAndRevenueRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_tax_and_revenue_statute_14(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> TaxAndRevenueRuleResult:
    """Statutory Evaluation Rule 14 for Municipal Taxation & Revenue Audit."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-TAX_-014'

    if metric > limit:
        return TaxAndRevenueRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return TaxAndRevenueRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return TaxAndRevenueRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_tax_and_revenue_statute_15(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> TaxAndRevenueRuleResult:
    """Statutory Evaluation Rule 15 for Municipal Taxation & Revenue Audit."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-TAX_-015'

    if metric > limit:
        return TaxAndRevenueRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return TaxAndRevenueRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return TaxAndRevenueRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_tax_and_revenue_statute_16(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> TaxAndRevenueRuleResult:
    """Statutory Evaluation Rule 16 for Municipal Taxation & Revenue Audit."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-TAX_-016'

    if metric > limit:
        return TaxAndRevenueRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return TaxAndRevenueRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return TaxAndRevenueRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_tax_and_revenue_statute_17(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> TaxAndRevenueRuleResult:
    """Statutory Evaluation Rule 17 for Municipal Taxation & Revenue Audit."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-TAX_-017'

    if metric > limit:
        return TaxAndRevenueRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return TaxAndRevenueRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return TaxAndRevenueRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_tax_and_revenue_statute_18(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> TaxAndRevenueRuleResult:
    """Statutory Evaluation Rule 18 for Municipal Taxation & Revenue Audit."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-TAX_-018'

    if metric > limit:
        return TaxAndRevenueRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return TaxAndRevenueRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return TaxAndRevenueRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_tax_and_revenue_statute_19(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> TaxAndRevenueRuleResult:
    """Statutory Evaluation Rule 19 for Municipal Taxation & Revenue Audit."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-TAX_-019'

    if metric > limit:
        return TaxAndRevenueRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return TaxAndRevenueRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return TaxAndRevenueRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_tax_and_revenue_statute_20(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> TaxAndRevenueRuleResult:
    """Statutory Evaluation Rule 20 for Municipal Taxation & Revenue Audit."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-TAX_-020'

    if metric > limit:
        return TaxAndRevenueRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return TaxAndRevenueRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return TaxAndRevenueRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_tax_and_revenue_statute_21(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> TaxAndRevenueRuleResult:
    """Statutory Evaluation Rule 21 for Municipal Taxation & Revenue Audit."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-TAX_-021'

    if metric > limit:
        return TaxAndRevenueRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return TaxAndRevenueRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return TaxAndRevenueRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_tax_and_revenue_statute_22(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> TaxAndRevenueRuleResult:
    """Statutory Evaluation Rule 22 for Municipal Taxation & Revenue Audit."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-TAX_-022'

    if metric > limit:
        return TaxAndRevenueRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return TaxAndRevenueRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return TaxAndRevenueRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_tax_and_revenue_statute_23(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> TaxAndRevenueRuleResult:
    """Statutory Evaluation Rule 23 for Municipal Taxation & Revenue Audit."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-TAX_-023'

    if metric > limit:
        return TaxAndRevenueRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return TaxAndRevenueRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return TaxAndRevenueRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_tax_and_revenue_statute_24(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> TaxAndRevenueRuleResult:
    """Statutory Evaluation Rule 24 for Municipal Taxation & Revenue Audit."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-TAX_-024'

    if metric > limit:
        return TaxAndRevenueRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return TaxAndRevenueRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return TaxAndRevenueRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_tax_and_revenue_statute_25(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> TaxAndRevenueRuleResult:
    """Statutory Evaluation Rule 25 for Municipal Taxation & Revenue Audit."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-TAX_-025'

    if metric > limit:
        return TaxAndRevenueRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return TaxAndRevenueRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return TaxAndRevenueRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_tax_and_revenue_statute_26(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> TaxAndRevenueRuleResult:
    """Statutory Evaluation Rule 26 for Municipal Taxation & Revenue Audit."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-TAX_-026'

    if metric > limit:
        return TaxAndRevenueRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return TaxAndRevenueRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return TaxAndRevenueRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_tax_and_revenue_statute_27(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> TaxAndRevenueRuleResult:
    """Statutory Evaluation Rule 27 for Municipal Taxation & Revenue Audit."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-TAX_-027'

    if metric > limit:
        return TaxAndRevenueRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return TaxAndRevenueRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return TaxAndRevenueRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_tax_and_revenue_statute_28(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> TaxAndRevenueRuleResult:
    """Statutory Evaluation Rule 28 for Municipal Taxation & Revenue Audit."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-TAX_-028'

    if metric > limit:
        return TaxAndRevenueRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return TaxAndRevenueRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return TaxAndRevenueRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_tax_and_revenue_statute_29(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> TaxAndRevenueRuleResult:
    """Statutory Evaluation Rule 29 for Municipal Taxation & Revenue Audit."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-TAX_-029'

    if metric > limit:
        return TaxAndRevenueRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return TaxAndRevenueRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return TaxAndRevenueRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_tax_and_revenue_statute_30(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> TaxAndRevenueRuleResult:
    """Statutory Evaluation Rule 30 for Municipal Taxation & Revenue Audit."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-TAX_-030'

    if metric > limit:
        return TaxAndRevenueRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return TaxAndRevenueRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return TaxAndRevenueRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_tax_and_revenue_statute_31(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> TaxAndRevenueRuleResult:
    """Statutory Evaluation Rule 31 for Municipal Taxation & Revenue Audit."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-TAX_-031'

    if metric > limit:
        return TaxAndRevenueRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return TaxAndRevenueRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return TaxAndRevenueRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_tax_and_revenue_statute_32(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> TaxAndRevenueRuleResult:
    """Statutory Evaluation Rule 32 for Municipal Taxation & Revenue Audit."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-TAX_-032'

    if metric > limit:
        return TaxAndRevenueRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return TaxAndRevenueRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return TaxAndRevenueRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_tax_and_revenue_statute_33(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> TaxAndRevenueRuleResult:
    """Statutory Evaluation Rule 33 for Municipal Taxation & Revenue Audit."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-TAX_-033'

    if metric > limit:
        return TaxAndRevenueRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return TaxAndRevenueRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return TaxAndRevenueRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_tax_and_revenue_statute_34(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> TaxAndRevenueRuleResult:
    """Statutory Evaluation Rule 34 for Municipal Taxation & Revenue Audit."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-TAX_-034'

    if metric > limit:
        return TaxAndRevenueRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return TaxAndRevenueRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return TaxAndRevenueRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_tax_and_revenue_statute_35(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> TaxAndRevenueRuleResult:
    """Statutory Evaluation Rule 35 for Municipal Taxation & Revenue Audit."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-TAX_-035'

    if metric > limit:
        return TaxAndRevenueRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return TaxAndRevenueRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return TaxAndRevenueRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_tax_and_revenue_statute_36(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> TaxAndRevenueRuleResult:
    """Statutory Evaluation Rule 36 for Municipal Taxation & Revenue Audit."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-TAX_-036'

    if metric > limit:
        return TaxAndRevenueRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return TaxAndRevenueRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return TaxAndRevenueRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_tax_and_revenue_statute_37(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> TaxAndRevenueRuleResult:
    """Statutory Evaluation Rule 37 for Municipal Taxation & Revenue Audit."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-TAX_-037'

    if metric > limit:
        return TaxAndRevenueRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return TaxAndRevenueRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return TaxAndRevenueRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_tax_and_revenue_statute_38(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> TaxAndRevenueRuleResult:
    """Statutory Evaluation Rule 38 for Municipal Taxation & Revenue Audit."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-TAX_-038'

    if metric > limit:
        return TaxAndRevenueRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return TaxAndRevenueRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return TaxAndRevenueRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_tax_and_revenue_statute_39(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> TaxAndRevenueRuleResult:
    """Statutory Evaluation Rule 39 for Municipal Taxation & Revenue Audit."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-TAX_-039'

    if metric > limit:
        return TaxAndRevenueRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return TaxAndRevenueRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return TaxAndRevenueRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_tax_and_revenue_statute_40(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> TaxAndRevenueRuleResult:
    """Statutory Evaluation Rule 40 for Municipal Taxation & Revenue Audit."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-TAX_-040'

    if metric > limit:
        return TaxAndRevenueRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return TaxAndRevenueRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return TaxAndRevenueRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_tax_and_revenue_statute_41(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> TaxAndRevenueRuleResult:
    """Statutory Evaluation Rule 41 for Municipal Taxation & Revenue Audit."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-TAX_-041'

    if metric > limit:
        return TaxAndRevenueRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return TaxAndRevenueRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return TaxAndRevenueRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_tax_and_revenue_statute_42(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> TaxAndRevenueRuleResult:
    """Statutory Evaluation Rule 42 for Municipal Taxation & Revenue Audit."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-TAX_-042'

    if metric > limit:
        return TaxAndRevenueRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return TaxAndRevenueRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return TaxAndRevenueRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_tax_and_revenue_statute_43(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> TaxAndRevenueRuleResult:
    """Statutory Evaluation Rule 43 for Municipal Taxation & Revenue Audit."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-TAX_-043'

    if metric > limit:
        return TaxAndRevenueRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return TaxAndRevenueRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return TaxAndRevenueRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_tax_and_revenue_statute_44(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> TaxAndRevenueRuleResult:
    """Statutory Evaluation Rule 44 for Municipal Taxation & Revenue Audit."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-TAX_-044'

    if metric > limit:
        return TaxAndRevenueRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return TaxAndRevenueRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return TaxAndRevenueRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_tax_and_revenue_statute_45(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> TaxAndRevenueRuleResult:
    """Statutory Evaluation Rule 45 for Municipal Taxation & Revenue Audit."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-TAX_-045'

    if metric > limit:
        return TaxAndRevenueRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return TaxAndRevenueRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return TaxAndRevenueRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_tax_and_revenue_statute_46(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> TaxAndRevenueRuleResult:
    """Statutory Evaluation Rule 46 for Municipal Taxation & Revenue Audit."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-TAX_-046'

    if metric > limit:
        return TaxAndRevenueRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return TaxAndRevenueRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return TaxAndRevenueRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_tax_and_revenue_statute_47(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> TaxAndRevenueRuleResult:
    """Statutory Evaluation Rule 47 for Municipal Taxation & Revenue Audit."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-TAX_-047'

    if metric > limit:
        return TaxAndRevenueRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return TaxAndRevenueRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return TaxAndRevenueRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_tax_and_revenue_statute_48(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> TaxAndRevenueRuleResult:
    """Statutory Evaluation Rule 48 for Municipal Taxation & Revenue Audit."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-TAX_-048'

    if metric > limit:
        return TaxAndRevenueRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return TaxAndRevenueRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return TaxAndRevenueRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_tax_and_revenue_statute_49(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> TaxAndRevenueRuleResult:
    """Statutory Evaluation Rule 49 for Municipal Taxation & Revenue Audit."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-TAX_-049'

    if metric > limit:
        return TaxAndRevenueRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return TaxAndRevenueRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return TaxAndRevenueRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_tax_and_revenue_statute_50(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> TaxAndRevenueRuleResult:
    """Statutory Evaluation Rule 50 for Municipal Taxation & Revenue Audit."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-TAX_-050'

    if metric > limit:
        return TaxAndRevenueRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return TaxAndRevenueRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return TaxAndRevenueRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_tax_and_revenue_statute_51(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> TaxAndRevenueRuleResult:
    """Statutory Evaluation Rule 51 for Municipal Taxation & Revenue Audit."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-TAX_-051'

    if metric > limit:
        return TaxAndRevenueRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return TaxAndRevenueRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return TaxAndRevenueRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_tax_and_revenue_statute_52(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> TaxAndRevenueRuleResult:
    """Statutory Evaluation Rule 52 for Municipal Taxation & Revenue Audit."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-TAX_-052'

    if metric > limit:
        return TaxAndRevenueRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return TaxAndRevenueRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return TaxAndRevenueRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_tax_and_revenue_statute_53(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> TaxAndRevenueRuleResult:
    """Statutory Evaluation Rule 53 for Municipal Taxation & Revenue Audit."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-TAX_-053'

    if metric > limit:
        return TaxAndRevenueRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return TaxAndRevenueRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return TaxAndRevenueRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_tax_and_revenue_statute_54(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> TaxAndRevenueRuleResult:
    """Statutory Evaluation Rule 54 for Municipal Taxation & Revenue Audit."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-TAX_-054'

    if metric > limit:
        return TaxAndRevenueRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return TaxAndRevenueRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return TaxAndRevenueRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_tax_and_revenue_statute_55(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> TaxAndRevenueRuleResult:
    """Statutory Evaluation Rule 55 for Municipal Taxation & Revenue Audit."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-TAX_-055'

    if metric > limit:
        return TaxAndRevenueRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return TaxAndRevenueRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return TaxAndRevenueRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_tax_and_revenue_statute_56(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> TaxAndRevenueRuleResult:
    """Statutory Evaluation Rule 56 for Municipal Taxation & Revenue Audit."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-TAX_-056'

    if metric > limit:
        return TaxAndRevenueRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return TaxAndRevenueRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return TaxAndRevenueRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_tax_and_revenue_statute_57(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> TaxAndRevenueRuleResult:
    """Statutory Evaluation Rule 57 for Municipal Taxation & Revenue Audit."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-TAX_-057'

    if metric > limit:
        return TaxAndRevenueRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return TaxAndRevenueRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return TaxAndRevenueRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_tax_and_revenue_statute_58(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> TaxAndRevenueRuleResult:
    """Statutory Evaluation Rule 58 for Municipal Taxation & Revenue Audit."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-TAX_-058'

    if metric > limit:
        return TaxAndRevenueRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return TaxAndRevenueRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return TaxAndRevenueRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_tax_and_revenue_statute_59(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> TaxAndRevenueRuleResult:
    """Statutory Evaluation Rule 59 for Municipal Taxation & Revenue Audit."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-TAX_-059'

    if metric > limit:
        return TaxAndRevenueRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return TaxAndRevenueRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return TaxAndRevenueRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_tax_and_revenue_statute_60(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> TaxAndRevenueRuleResult:
    """Statutory Evaluation Rule 60 for Municipal Taxation & Revenue Audit."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-TAX_-060'

    if metric > limit:
        return TaxAndRevenueRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return TaxAndRevenueRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return TaxAndRevenueRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_tax_and_revenue_statute_61(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> TaxAndRevenueRuleResult:
    """Statutory Evaluation Rule 61 for Municipal Taxation & Revenue Audit."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-TAX_-061'

    if metric > limit:
        return TaxAndRevenueRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return TaxAndRevenueRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return TaxAndRevenueRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_tax_and_revenue_statute_62(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> TaxAndRevenueRuleResult:
    """Statutory Evaluation Rule 62 for Municipal Taxation & Revenue Audit."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-TAX_-062'

    if metric > limit:
        return TaxAndRevenueRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return TaxAndRevenueRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return TaxAndRevenueRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_tax_and_revenue_statute_63(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> TaxAndRevenueRuleResult:
    """Statutory Evaluation Rule 63 for Municipal Taxation & Revenue Audit."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-TAX_-063'

    if metric > limit:
        return TaxAndRevenueRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return TaxAndRevenueRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return TaxAndRevenueRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_tax_and_revenue_statute_64(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> TaxAndRevenueRuleResult:
    """Statutory Evaluation Rule 64 for Municipal Taxation & Revenue Audit."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-TAX_-064'

    if metric > limit:
        return TaxAndRevenueRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return TaxAndRevenueRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return TaxAndRevenueRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_tax_and_revenue_statute_65(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> TaxAndRevenueRuleResult:
    """Statutory Evaluation Rule 65 for Municipal Taxation & Revenue Audit."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-TAX_-065'

    if metric > limit:
        return TaxAndRevenueRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return TaxAndRevenueRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return TaxAndRevenueRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_tax_and_revenue_statute_66(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> TaxAndRevenueRuleResult:
    """Statutory Evaluation Rule 66 for Municipal Taxation & Revenue Audit."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-TAX_-066'

    if metric > limit:
        return TaxAndRevenueRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return TaxAndRevenueRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return TaxAndRevenueRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_tax_and_revenue_statute_67(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> TaxAndRevenueRuleResult:
    """Statutory Evaluation Rule 67 for Municipal Taxation & Revenue Audit."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-TAX_-067'

    if metric > limit:
        return TaxAndRevenueRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return TaxAndRevenueRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return TaxAndRevenueRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_tax_and_revenue_statute_68(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> TaxAndRevenueRuleResult:
    """Statutory Evaluation Rule 68 for Municipal Taxation & Revenue Audit."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-TAX_-068'

    if metric > limit:
        return TaxAndRevenueRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return TaxAndRevenueRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return TaxAndRevenueRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_tax_and_revenue_statute_69(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> TaxAndRevenueRuleResult:
    """Statutory Evaluation Rule 69 for Municipal Taxation & Revenue Audit."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-TAX_-069'

    if metric > limit:
        return TaxAndRevenueRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return TaxAndRevenueRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return TaxAndRevenueRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_tax_and_revenue_statute_70(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> TaxAndRevenueRuleResult:
    """Statutory Evaluation Rule 70 for Municipal Taxation & Revenue Audit."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-TAX_-070'

    if metric > limit:
        return TaxAndRevenueRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return TaxAndRevenueRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return TaxAndRevenueRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_tax_and_revenue_statute_71(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> TaxAndRevenueRuleResult:
    """Statutory Evaluation Rule 71 for Municipal Taxation & Revenue Audit."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-TAX_-071'

    if metric > limit:
        return TaxAndRevenueRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return TaxAndRevenueRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return TaxAndRevenueRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_tax_and_revenue_statute_72(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> TaxAndRevenueRuleResult:
    """Statutory Evaluation Rule 72 for Municipal Taxation & Revenue Audit."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-TAX_-072'

    if metric > limit:
        return TaxAndRevenueRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return TaxAndRevenueRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return TaxAndRevenueRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_tax_and_revenue_statute_73(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> TaxAndRevenueRuleResult:
    """Statutory Evaluation Rule 73 for Municipal Taxation & Revenue Audit."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-TAX_-073'

    if metric > limit:
        return TaxAndRevenueRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return TaxAndRevenueRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return TaxAndRevenueRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_tax_and_revenue_statute_74(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> TaxAndRevenueRuleResult:
    """Statutory Evaluation Rule 74 for Municipal Taxation & Revenue Audit."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-TAX_-074'

    if metric > limit:
        return TaxAndRevenueRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return TaxAndRevenueRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return TaxAndRevenueRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_tax_and_revenue_statute_75(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> TaxAndRevenueRuleResult:
    """Statutory Evaluation Rule 75 for Municipal Taxation & Revenue Audit."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-TAX_-075'

    if metric > limit:
        return TaxAndRevenueRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return TaxAndRevenueRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return TaxAndRevenueRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_tax_and_revenue_statute_76(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> TaxAndRevenueRuleResult:
    """Statutory Evaluation Rule 76 for Municipal Taxation & Revenue Audit."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-TAX_-076'

    if metric > limit:
        return TaxAndRevenueRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return TaxAndRevenueRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return TaxAndRevenueRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_tax_and_revenue_statute_77(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> TaxAndRevenueRuleResult:
    """Statutory Evaluation Rule 77 for Municipal Taxation & Revenue Audit."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-TAX_-077'

    if metric > limit:
        return TaxAndRevenueRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return TaxAndRevenueRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return TaxAndRevenueRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_tax_and_revenue_statute_78(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> TaxAndRevenueRuleResult:
    """Statutory Evaluation Rule 78 for Municipal Taxation & Revenue Audit."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-TAX_-078'

    if metric > limit:
        return TaxAndRevenueRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return TaxAndRevenueRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return TaxAndRevenueRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_tax_and_revenue_statute_79(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> TaxAndRevenueRuleResult:
    """Statutory Evaluation Rule 79 for Municipal Taxation & Revenue Audit."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-TAX_-079'

    if metric > limit:
        return TaxAndRevenueRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return TaxAndRevenueRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return TaxAndRevenueRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_tax_and_revenue_statute_80(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> TaxAndRevenueRuleResult:
    """Statutory Evaluation Rule 80 for Municipal Taxation & Revenue Audit."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-TAX_-080'

    if metric > limit:
        return TaxAndRevenueRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return TaxAndRevenueRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return TaxAndRevenueRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_tax_and_revenue_statute_81(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> TaxAndRevenueRuleResult:
    """Statutory Evaluation Rule 81 for Municipal Taxation & Revenue Audit."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-TAX_-081'

    if metric > limit:
        return TaxAndRevenueRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return TaxAndRevenueRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return TaxAndRevenueRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_tax_and_revenue_statute_82(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> TaxAndRevenueRuleResult:
    """Statutory Evaluation Rule 82 for Municipal Taxation & Revenue Audit."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-TAX_-082'

    if metric > limit:
        return TaxAndRevenueRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return TaxAndRevenueRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return TaxAndRevenueRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_tax_and_revenue_statute_83(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> TaxAndRevenueRuleResult:
    """Statutory Evaluation Rule 83 for Municipal Taxation & Revenue Audit."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-TAX_-083'

    if metric > limit:
        return TaxAndRevenueRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return TaxAndRevenueRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return TaxAndRevenueRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_tax_and_revenue_statute_84(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> TaxAndRevenueRuleResult:
    """Statutory Evaluation Rule 84 for Municipal Taxation & Revenue Audit."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-TAX_-084'

    if metric > limit:
        return TaxAndRevenueRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return TaxAndRevenueRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return TaxAndRevenueRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_tax_and_revenue_statute_85(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> TaxAndRevenueRuleResult:
    """Statutory Evaluation Rule 85 for Municipal Taxation & Revenue Audit."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-TAX_-085'

    if metric > limit:
        return TaxAndRevenueRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return TaxAndRevenueRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return TaxAndRevenueRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_tax_and_revenue_statute_86(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> TaxAndRevenueRuleResult:
    """Statutory Evaluation Rule 86 for Municipal Taxation & Revenue Audit."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-TAX_-086'

    if metric > limit:
        return TaxAndRevenueRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return TaxAndRevenueRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return TaxAndRevenueRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_tax_and_revenue_statute_87(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> TaxAndRevenueRuleResult:
    """Statutory Evaluation Rule 87 for Municipal Taxation & Revenue Audit."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-TAX_-087'

    if metric > limit:
        return TaxAndRevenueRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return TaxAndRevenueRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return TaxAndRevenueRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_tax_and_revenue_statute_88(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> TaxAndRevenueRuleResult:
    """Statutory Evaluation Rule 88 for Municipal Taxation & Revenue Audit."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-TAX_-088'

    if metric > limit:
        return TaxAndRevenueRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return TaxAndRevenueRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return TaxAndRevenueRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_tax_and_revenue_statute_89(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> TaxAndRevenueRuleResult:
    """Statutory Evaluation Rule 89 for Municipal Taxation & Revenue Audit."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-TAX_-089'

    if metric > limit:
        return TaxAndRevenueRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return TaxAndRevenueRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return TaxAndRevenueRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_tax_and_revenue_statute_90(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> TaxAndRevenueRuleResult:
    """Statutory Evaluation Rule 90 for Municipal Taxation & Revenue Audit."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-TAX_-090'

    if metric > limit:
        return TaxAndRevenueRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return TaxAndRevenueRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return TaxAndRevenueRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )
