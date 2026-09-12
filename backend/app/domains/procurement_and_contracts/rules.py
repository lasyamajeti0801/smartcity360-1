"""
SmartCity360 - Public Procurement & Vendor Management Statutory Business Rules Engine
Domain: procurement_and_contracts
"""

from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass

from .models import ProcurementAndContractsStatus, ProcurementAndContractsPriority

@dataclass
class ProcurementAndContractsRuleResult:
    passed: bool
    rule_code: str
    severity: str
    explanation: str
    recommended_action: str
    remediation_cost_estimate: float = 0.0

def evaluate_procurement_and_contracts_statute_01(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ProcurementAndContractsRuleResult:
    """Statutory Evaluation Rule 01 for Public Procurement & Vendor Management."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-PROC-001'

    if metric > limit:
        return ProcurementAndContractsRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return ProcurementAndContractsRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return ProcurementAndContractsRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_procurement_and_contracts_statute_02(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ProcurementAndContractsRuleResult:
    """Statutory Evaluation Rule 02 for Public Procurement & Vendor Management."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-PROC-002'

    if metric > limit:
        return ProcurementAndContractsRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return ProcurementAndContractsRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return ProcurementAndContractsRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_procurement_and_contracts_statute_03(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ProcurementAndContractsRuleResult:
    """Statutory Evaluation Rule 03 for Public Procurement & Vendor Management."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-PROC-003'

    if metric > limit:
        return ProcurementAndContractsRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return ProcurementAndContractsRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return ProcurementAndContractsRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_procurement_and_contracts_statute_04(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ProcurementAndContractsRuleResult:
    """Statutory Evaluation Rule 04 for Public Procurement & Vendor Management."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-PROC-004'

    if metric > limit:
        return ProcurementAndContractsRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return ProcurementAndContractsRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return ProcurementAndContractsRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_procurement_and_contracts_statute_05(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ProcurementAndContractsRuleResult:
    """Statutory Evaluation Rule 05 for Public Procurement & Vendor Management."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-PROC-005'

    if metric > limit:
        return ProcurementAndContractsRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return ProcurementAndContractsRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return ProcurementAndContractsRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_procurement_and_contracts_statute_06(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ProcurementAndContractsRuleResult:
    """Statutory Evaluation Rule 06 for Public Procurement & Vendor Management."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-PROC-006'

    if metric > limit:
        return ProcurementAndContractsRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return ProcurementAndContractsRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return ProcurementAndContractsRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_procurement_and_contracts_statute_07(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ProcurementAndContractsRuleResult:
    """Statutory Evaluation Rule 07 for Public Procurement & Vendor Management."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-PROC-007'

    if metric > limit:
        return ProcurementAndContractsRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return ProcurementAndContractsRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return ProcurementAndContractsRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_procurement_and_contracts_statute_08(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ProcurementAndContractsRuleResult:
    """Statutory Evaluation Rule 08 for Public Procurement & Vendor Management."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-PROC-008'

    if metric > limit:
        return ProcurementAndContractsRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return ProcurementAndContractsRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return ProcurementAndContractsRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_procurement_and_contracts_statute_09(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ProcurementAndContractsRuleResult:
    """Statutory Evaluation Rule 09 for Public Procurement & Vendor Management."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-PROC-009'

    if metric > limit:
        return ProcurementAndContractsRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return ProcurementAndContractsRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return ProcurementAndContractsRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_procurement_and_contracts_statute_10(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ProcurementAndContractsRuleResult:
    """Statutory Evaluation Rule 10 for Public Procurement & Vendor Management."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-PROC-010'

    if metric > limit:
        return ProcurementAndContractsRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return ProcurementAndContractsRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return ProcurementAndContractsRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_procurement_and_contracts_statute_11(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ProcurementAndContractsRuleResult:
    """Statutory Evaluation Rule 11 for Public Procurement & Vendor Management."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-PROC-011'

    if metric > limit:
        return ProcurementAndContractsRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return ProcurementAndContractsRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return ProcurementAndContractsRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_procurement_and_contracts_statute_12(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ProcurementAndContractsRuleResult:
    """Statutory Evaluation Rule 12 for Public Procurement & Vendor Management."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-PROC-012'

    if metric > limit:
        return ProcurementAndContractsRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return ProcurementAndContractsRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return ProcurementAndContractsRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_procurement_and_contracts_statute_13(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ProcurementAndContractsRuleResult:
    """Statutory Evaluation Rule 13 for Public Procurement & Vendor Management."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-PROC-013'

    if metric > limit:
        return ProcurementAndContractsRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return ProcurementAndContractsRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return ProcurementAndContractsRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_procurement_and_contracts_statute_14(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ProcurementAndContractsRuleResult:
    """Statutory Evaluation Rule 14 for Public Procurement & Vendor Management."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-PROC-014'

    if metric > limit:
        return ProcurementAndContractsRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return ProcurementAndContractsRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return ProcurementAndContractsRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_procurement_and_contracts_statute_15(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ProcurementAndContractsRuleResult:
    """Statutory Evaluation Rule 15 for Public Procurement & Vendor Management."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-PROC-015'

    if metric > limit:
        return ProcurementAndContractsRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return ProcurementAndContractsRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return ProcurementAndContractsRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_procurement_and_contracts_statute_16(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ProcurementAndContractsRuleResult:
    """Statutory Evaluation Rule 16 for Public Procurement & Vendor Management."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-PROC-016'

    if metric > limit:
        return ProcurementAndContractsRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return ProcurementAndContractsRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return ProcurementAndContractsRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_procurement_and_contracts_statute_17(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ProcurementAndContractsRuleResult:
    """Statutory Evaluation Rule 17 for Public Procurement & Vendor Management."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-PROC-017'

    if metric > limit:
        return ProcurementAndContractsRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return ProcurementAndContractsRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return ProcurementAndContractsRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_procurement_and_contracts_statute_18(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ProcurementAndContractsRuleResult:
    """Statutory Evaluation Rule 18 for Public Procurement & Vendor Management."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-PROC-018'

    if metric > limit:
        return ProcurementAndContractsRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return ProcurementAndContractsRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return ProcurementAndContractsRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_procurement_and_contracts_statute_19(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ProcurementAndContractsRuleResult:
    """Statutory Evaluation Rule 19 for Public Procurement & Vendor Management."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-PROC-019'

    if metric > limit:
        return ProcurementAndContractsRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return ProcurementAndContractsRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return ProcurementAndContractsRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_procurement_and_contracts_statute_20(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ProcurementAndContractsRuleResult:
    """Statutory Evaluation Rule 20 for Public Procurement & Vendor Management."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-PROC-020'

    if metric > limit:
        return ProcurementAndContractsRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return ProcurementAndContractsRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return ProcurementAndContractsRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_procurement_and_contracts_statute_21(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ProcurementAndContractsRuleResult:
    """Statutory Evaluation Rule 21 for Public Procurement & Vendor Management."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-PROC-021'

    if metric > limit:
        return ProcurementAndContractsRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return ProcurementAndContractsRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return ProcurementAndContractsRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_procurement_and_contracts_statute_22(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ProcurementAndContractsRuleResult:
    """Statutory Evaluation Rule 22 for Public Procurement & Vendor Management."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-PROC-022'

    if metric > limit:
        return ProcurementAndContractsRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return ProcurementAndContractsRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return ProcurementAndContractsRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_procurement_and_contracts_statute_23(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ProcurementAndContractsRuleResult:
    """Statutory Evaluation Rule 23 for Public Procurement & Vendor Management."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-PROC-023'

    if metric > limit:
        return ProcurementAndContractsRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return ProcurementAndContractsRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return ProcurementAndContractsRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_procurement_and_contracts_statute_24(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ProcurementAndContractsRuleResult:
    """Statutory Evaluation Rule 24 for Public Procurement & Vendor Management."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-PROC-024'

    if metric > limit:
        return ProcurementAndContractsRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return ProcurementAndContractsRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return ProcurementAndContractsRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_procurement_and_contracts_statute_25(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ProcurementAndContractsRuleResult:
    """Statutory Evaluation Rule 25 for Public Procurement & Vendor Management."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-PROC-025'

    if metric > limit:
        return ProcurementAndContractsRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return ProcurementAndContractsRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return ProcurementAndContractsRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_procurement_and_contracts_statute_26(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ProcurementAndContractsRuleResult:
    """Statutory Evaluation Rule 26 for Public Procurement & Vendor Management."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-PROC-026'

    if metric > limit:
        return ProcurementAndContractsRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return ProcurementAndContractsRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return ProcurementAndContractsRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_procurement_and_contracts_statute_27(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ProcurementAndContractsRuleResult:
    """Statutory Evaluation Rule 27 for Public Procurement & Vendor Management."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-PROC-027'

    if metric > limit:
        return ProcurementAndContractsRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return ProcurementAndContractsRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return ProcurementAndContractsRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_procurement_and_contracts_statute_28(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ProcurementAndContractsRuleResult:
    """Statutory Evaluation Rule 28 for Public Procurement & Vendor Management."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-PROC-028'

    if metric > limit:
        return ProcurementAndContractsRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return ProcurementAndContractsRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return ProcurementAndContractsRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_procurement_and_contracts_statute_29(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ProcurementAndContractsRuleResult:
    """Statutory Evaluation Rule 29 for Public Procurement & Vendor Management."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-PROC-029'

    if metric > limit:
        return ProcurementAndContractsRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return ProcurementAndContractsRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return ProcurementAndContractsRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_procurement_and_contracts_statute_30(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ProcurementAndContractsRuleResult:
    """Statutory Evaluation Rule 30 for Public Procurement & Vendor Management."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-PROC-030'

    if metric > limit:
        return ProcurementAndContractsRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return ProcurementAndContractsRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return ProcurementAndContractsRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_procurement_and_contracts_statute_31(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ProcurementAndContractsRuleResult:
    """Statutory Evaluation Rule 31 for Public Procurement & Vendor Management."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-PROC-031'

    if metric > limit:
        return ProcurementAndContractsRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return ProcurementAndContractsRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return ProcurementAndContractsRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_procurement_and_contracts_statute_32(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ProcurementAndContractsRuleResult:
    """Statutory Evaluation Rule 32 for Public Procurement & Vendor Management."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-PROC-032'

    if metric > limit:
        return ProcurementAndContractsRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return ProcurementAndContractsRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return ProcurementAndContractsRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_procurement_and_contracts_statute_33(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ProcurementAndContractsRuleResult:
    """Statutory Evaluation Rule 33 for Public Procurement & Vendor Management."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-PROC-033'

    if metric > limit:
        return ProcurementAndContractsRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return ProcurementAndContractsRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return ProcurementAndContractsRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_procurement_and_contracts_statute_34(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ProcurementAndContractsRuleResult:
    """Statutory Evaluation Rule 34 for Public Procurement & Vendor Management."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-PROC-034'

    if metric > limit:
        return ProcurementAndContractsRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return ProcurementAndContractsRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return ProcurementAndContractsRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_procurement_and_contracts_statute_35(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ProcurementAndContractsRuleResult:
    """Statutory Evaluation Rule 35 for Public Procurement & Vendor Management."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-PROC-035'

    if metric > limit:
        return ProcurementAndContractsRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return ProcurementAndContractsRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return ProcurementAndContractsRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_procurement_and_contracts_statute_36(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ProcurementAndContractsRuleResult:
    """Statutory Evaluation Rule 36 for Public Procurement & Vendor Management."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-PROC-036'

    if metric > limit:
        return ProcurementAndContractsRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return ProcurementAndContractsRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return ProcurementAndContractsRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_procurement_and_contracts_statute_37(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ProcurementAndContractsRuleResult:
    """Statutory Evaluation Rule 37 for Public Procurement & Vendor Management."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-PROC-037'

    if metric > limit:
        return ProcurementAndContractsRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return ProcurementAndContractsRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return ProcurementAndContractsRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_procurement_and_contracts_statute_38(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ProcurementAndContractsRuleResult:
    """Statutory Evaluation Rule 38 for Public Procurement & Vendor Management."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-PROC-038'

    if metric > limit:
        return ProcurementAndContractsRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return ProcurementAndContractsRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return ProcurementAndContractsRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_procurement_and_contracts_statute_39(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ProcurementAndContractsRuleResult:
    """Statutory Evaluation Rule 39 for Public Procurement & Vendor Management."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-PROC-039'

    if metric > limit:
        return ProcurementAndContractsRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return ProcurementAndContractsRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return ProcurementAndContractsRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_procurement_and_contracts_statute_40(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ProcurementAndContractsRuleResult:
    """Statutory Evaluation Rule 40 for Public Procurement & Vendor Management."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-PROC-040'

    if metric > limit:
        return ProcurementAndContractsRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return ProcurementAndContractsRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return ProcurementAndContractsRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_procurement_and_contracts_statute_41(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ProcurementAndContractsRuleResult:
    """Statutory Evaluation Rule 41 for Public Procurement & Vendor Management."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-PROC-041'

    if metric > limit:
        return ProcurementAndContractsRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return ProcurementAndContractsRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return ProcurementAndContractsRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_procurement_and_contracts_statute_42(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ProcurementAndContractsRuleResult:
    """Statutory Evaluation Rule 42 for Public Procurement & Vendor Management."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-PROC-042'

    if metric > limit:
        return ProcurementAndContractsRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return ProcurementAndContractsRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return ProcurementAndContractsRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_procurement_and_contracts_statute_43(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ProcurementAndContractsRuleResult:
    """Statutory Evaluation Rule 43 for Public Procurement & Vendor Management."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-PROC-043'

    if metric > limit:
        return ProcurementAndContractsRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return ProcurementAndContractsRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return ProcurementAndContractsRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_procurement_and_contracts_statute_44(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ProcurementAndContractsRuleResult:
    """Statutory Evaluation Rule 44 for Public Procurement & Vendor Management."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-PROC-044'

    if metric > limit:
        return ProcurementAndContractsRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return ProcurementAndContractsRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return ProcurementAndContractsRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_procurement_and_contracts_statute_45(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ProcurementAndContractsRuleResult:
    """Statutory Evaluation Rule 45 for Public Procurement & Vendor Management."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-PROC-045'

    if metric > limit:
        return ProcurementAndContractsRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return ProcurementAndContractsRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return ProcurementAndContractsRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_procurement_and_contracts_statute_46(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ProcurementAndContractsRuleResult:
    """Statutory Evaluation Rule 46 for Public Procurement & Vendor Management."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-PROC-046'

    if metric > limit:
        return ProcurementAndContractsRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return ProcurementAndContractsRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return ProcurementAndContractsRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_procurement_and_contracts_statute_47(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ProcurementAndContractsRuleResult:
    """Statutory Evaluation Rule 47 for Public Procurement & Vendor Management."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-PROC-047'

    if metric > limit:
        return ProcurementAndContractsRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return ProcurementAndContractsRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return ProcurementAndContractsRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_procurement_and_contracts_statute_48(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ProcurementAndContractsRuleResult:
    """Statutory Evaluation Rule 48 for Public Procurement & Vendor Management."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-PROC-048'

    if metric > limit:
        return ProcurementAndContractsRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return ProcurementAndContractsRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return ProcurementAndContractsRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_procurement_and_contracts_statute_49(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ProcurementAndContractsRuleResult:
    """Statutory Evaluation Rule 49 for Public Procurement & Vendor Management."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-PROC-049'

    if metric > limit:
        return ProcurementAndContractsRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return ProcurementAndContractsRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return ProcurementAndContractsRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_procurement_and_contracts_statute_50(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ProcurementAndContractsRuleResult:
    """Statutory Evaluation Rule 50 for Public Procurement & Vendor Management."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-PROC-050'

    if metric > limit:
        return ProcurementAndContractsRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return ProcurementAndContractsRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return ProcurementAndContractsRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_procurement_and_contracts_statute_51(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ProcurementAndContractsRuleResult:
    """Statutory Evaluation Rule 51 for Public Procurement & Vendor Management."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-PROC-051'

    if metric > limit:
        return ProcurementAndContractsRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return ProcurementAndContractsRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return ProcurementAndContractsRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_procurement_and_contracts_statute_52(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ProcurementAndContractsRuleResult:
    """Statutory Evaluation Rule 52 for Public Procurement & Vendor Management."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-PROC-052'

    if metric > limit:
        return ProcurementAndContractsRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return ProcurementAndContractsRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return ProcurementAndContractsRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_procurement_and_contracts_statute_53(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ProcurementAndContractsRuleResult:
    """Statutory Evaluation Rule 53 for Public Procurement & Vendor Management."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-PROC-053'

    if metric > limit:
        return ProcurementAndContractsRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return ProcurementAndContractsRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return ProcurementAndContractsRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_procurement_and_contracts_statute_54(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ProcurementAndContractsRuleResult:
    """Statutory Evaluation Rule 54 for Public Procurement & Vendor Management."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-PROC-054'

    if metric > limit:
        return ProcurementAndContractsRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return ProcurementAndContractsRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return ProcurementAndContractsRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_procurement_and_contracts_statute_55(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ProcurementAndContractsRuleResult:
    """Statutory Evaluation Rule 55 for Public Procurement & Vendor Management."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-PROC-055'

    if metric > limit:
        return ProcurementAndContractsRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return ProcurementAndContractsRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return ProcurementAndContractsRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_procurement_and_contracts_statute_56(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ProcurementAndContractsRuleResult:
    """Statutory Evaluation Rule 56 for Public Procurement & Vendor Management."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-PROC-056'

    if metric > limit:
        return ProcurementAndContractsRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return ProcurementAndContractsRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return ProcurementAndContractsRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_procurement_and_contracts_statute_57(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ProcurementAndContractsRuleResult:
    """Statutory Evaluation Rule 57 for Public Procurement & Vendor Management."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-PROC-057'

    if metric > limit:
        return ProcurementAndContractsRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return ProcurementAndContractsRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return ProcurementAndContractsRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_procurement_and_contracts_statute_58(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ProcurementAndContractsRuleResult:
    """Statutory Evaluation Rule 58 for Public Procurement & Vendor Management."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-PROC-058'

    if metric > limit:
        return ProcurementAndContractsRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return ProcurementAndContractsRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return ProcurementAndContractsRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_procurement_and_contracts_statute_59(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ProcurementAndContractsRuleResult:
    """Statutory Evaluation Rule 59 for Public Procurement & Vendor Management."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-PROC-059'

    if metric > limit:
        return ProcurementAndContractsRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return ProcurementAndContractsRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return ProcurementAndContractsRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_procurement_and_contracts_statute_60(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ProcurementAndContractsRuleResult:
    """Statutory Evaluation Rule 60 for Public Procurement & Vendor Management."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-PROC-060'

    if metric > limit:
        return ProcurementAndContractsRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return ProcurementAndContractsRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return ProcurementAndContractsRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_procurement_and_contracts_statute_61(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ProcurementAndContractsRuleResult:
    """Statutory Evaluation Rule 61 for Public Procurement & Vendor Management."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-PROC-061'

    if metric > limit:
        return ProcurementAndContractsRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return ProcurementAndContractsRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return ProcurementAndContractsRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_procurement_and_contracts_statute_62(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ProcurementAndContractsRuleResult:
    """Statutory Evaluation Rule 62 for Public Procurement & Vendor Management."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-PROC-062'

    if metric > limit:
        return ProcurementAndContractsRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return ProcurementAndContractsRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return ProcurementAndContractsRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_procurement_and_contracts_statute_63(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ProcurementAndContractsRuleResult:
    """Statutory Evaluation Rule 63 for Public Procurement & Vendor Management."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-PROC-063'

    if metric > limit:
        return ProcurementAndContractsRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return ProcurementAndContractsRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return ProcurementAndContractsRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_procurement_and_contracts_statute_64(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ProcurementAndContractsRuleResult:
    """Statutory Evaluation Rule 64 for Public Procurement & Vendor Management."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-PROC-064'

    if metric > limit:
        return ProcurementAndContractsRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return ProcurementAndContractsRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return ProcurementAndContractsRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_procurement_and_contracts_statute_65(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ProcurementAndContractsRuleResult:
    """Statutory Evaluation Rule 65 for Public Procurement & Vendor Management."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-PROC-065'

    if metric > limit:
        return ProcurementAndContractsRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return ProcurementAndContractsRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return ProcurementAndContractsRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_procurement_and_contracts_statute_66(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ProcurementAndContractsRuleResult:
    """Statutory Evaluation Rule 66 for Public Procurement & Vendor Management."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-PROC-066'

    if metric > limit:
        return ProcurementAndContractsRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return ProcurementAndContractsRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return ProcurementAndContractsRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_procurement_and_contracts_statute_67(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ProcurementAndContractsRuleResult:
    """Statutory Evaluation Rule 67 for Public Procurement & Vendor Management."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-PROC-067'

    if metric > limit:
        return ProcurementAndContractsRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return ProcurementAndContractsRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return ProcurementAndContractsRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_procurement_and_contracts_statute_68(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ProcurementAndContractsRuleResult:
    """Statutory Evaluation Rule 68 for Public Procurement & Vendor Management."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-PROC-068'

    if metric > limit:
        return ProcurementAndContractsRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return ProcurementAndContractsRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return ProcurementAndContractsRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_procurement_and_contracts_statute_69(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ProcurementAndContractsRuleResult:
    """Statutory Evaluation Rule 69 for Public Procurement & Vendor Management."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-PROC-069'

    if metric > limit:
        return ProcurementAndContractsRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return ProcurementAndContractsRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return ProcurementAndContractsRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_procurement_and_contracts_statute_70(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ProcurementAndContractsRuleResult:
    """Statutory Evaluation Rule 70 for Public Procurement & Vendor Management."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-PROC-070'

    if metric > limit:
        return ProcurementAndContractsRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return ProcurementAndContractsRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return ProcurementAndContractsRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_procurement_and_contracts_statute_71(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ProcurementAndContractsRuleResult:
    """Statutory Evaluation Rule 71 for Public Procurement & Vendor Management."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-PROC-071'

    if metric > limit:
        return ProcurementAndContractsRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return ProcurementAndContractsRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return ProcurementAndContractsRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_procurement_and_contracts_statute_72(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ProcurementAndContractsRuleResult:
    """Statutory Evaluation Rule 72 for Public Procurement & Vendor Management."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-PROC-072'

    if metric > limit:
        return ProcurementAndContractsRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return ProcurementAndContractsRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return ProcurementAndContractsRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_procurement_and_contracts_statute_73(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ProcurementAndContractsRuleResult:
    """Statutory Evaluation Rule 73 for Public Procurement & Vendor Management."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-PROC-073'

    if metric > limit:
        return ProcurementAndContractsRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return ProcurementAndContractsRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return ProcurementAndContractsRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_procurement_and_contracts_statute_74(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ProcurementAndContractsRuleResult:
    """Statutory Evaluation Rule 74 for Public Procurement & Vendor Management."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-PROC-074'

    if metric > limit:
        return ProcurementAndContractsRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return ProcurementAndContractsRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return ProcurementAndContractsRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_procurement_and_contracts_statute_75(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ProcurementAndContractsRuleResult:
    """Statutory Evaluation Rule 75 for Public Procurement & Vendor Management."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-PROC-075'

    if metric > limit:
        return ProcurementAndContractsRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return ProcurementAndContractsRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return ProcurementAndContractsRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_procurement_and_contracts_statute_76(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ProcurementAndContractsRuleResult:
    """Statutory Evaluation Rule 76 for Public Procurement & Vendor Management."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-PROC-076'

    if metric > limit:
        return ProcurementAndContractsRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return ProcurementAndContractsRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return ProcurementAndContractsRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_procurement_and_contracts_statute_77(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ProcurementAndContractsRuleResult:
    """Statutory Evaluation Rule 77 for Public Procurement & Vendor Management."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-PROC-077'

    if metric > limit:
        return ProcurementAndContractsRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return ProcurementAndContractsRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return ProcurementAndContractsRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_procurement_and_contracts_statute_78(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ProcurementAndContractsRuleResult:
    """Statutory Evaluation Rule 78 for Public Procurement & Vendor Management."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-PROC-078'

    if metric > limit:
        return ProcurementAndContractsRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return ProcurementAndContractsRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return ProcurementAndContractsRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_procurement_and_contracts_statute_79(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ProcurementAndContractsRuleResult:
    """Statutory Evaluation Rule 79 for Public Procurement & Vendor Management."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-PROC-079'

    if metric > limit:
        return ProcurementAndContractsRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return ProcurementAndContractsRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return ProcurementAndContractsRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_procurement_and_contracts_statute_80(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ProcurementAndContractsRuleResult:
    """Statutory Evaluation Rule 80 for Public Procurement & Vendor Management."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-PROC-080'

    if metric > limit:
        return ProcurementAndContractsRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return ProcurementAndContractsRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return ProcurementAndContractsRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_procurement_and_contracts_statute_81(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ProcurementAndContractsRuleResult:
    """Statutory Evaluation Rule 81 for Public Procurement & Vendor Management."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-PROC-081'

    if metric > limit:
        return ProcurementAndContractsRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return ProcurementAndContractsRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return ProcurementAndContractsRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_procurement_and_contracts_statute_82(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ProcurementAndContractsRuleResult:
    """Statutory Evaluation Rule 82 for Public Procurement & Vendor Management."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-PROC-082'

    if metric > limit:
        return ProcurementAndContractsRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return ProcurementAndContractsRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return ProcurementAndContractsRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_procurement_and_contracts_statute_83(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ProcurementAndContractsRuleResult:
    """Statutory Evaluation Rule 83 for Public Procurement & Vendor Management."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-PROC-083'

    if metric > limit:
        return ProcurementAndContractsRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return ProcurementAndContractsRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return ProcurementAndContractsRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_procurement_and_contracts_statute_84(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ProcurementAndContractsRuleResult:
    """Statutory Evaluation Rule 84 for Public Procurement & Vendor Management."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-PROC-084'

    if metric > limit:
        return ProcurementAndContractsRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return ProcurementAndContractsRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return ProcurementAndContractsRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_procurement_and_contracts_statute_85(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ProcurementAndContractsRuleResult:
    """Statutory Evaluation Rule 85 for Public Procurement & Vendor Management."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-PROC-085'

    if metric > limit:
        return ProcurementAndContractsRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return ProcurementAndContractsRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return ProcurementAndContractsRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_procurement_and_contracts_statute_86(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ProcurementAndContractsRuleResult:
    """Statutory Evaluation Rule 86 for Public Procurement & Vendor Management."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-PROC-086'

    if metric > limit:
        return ProcurementAndContractsRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return ProcurementAndContractsRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return ProcurementAndContractsRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_procurement_and_contracts_statute_87(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ProcurementAndContractsRuleResult:
    """Statutory Evaluation Rule 87 for Public Procurement & Vendor Management."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-PROC-087'

    if metric > limit:
        return ProcurementAndContractsRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return ProcurementAndContractsRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return ProcurementAndContractsRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_procurement_and_contracts_statute_88(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ProcurementAndContractsRuleResult:
    """Statutory Evaluation Rule 88 for Public Procurement & Vendor Management."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-PROC-088'

    if metric > limit:
        return ProcurementAndContractsRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return ProcurementAndContractsRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return ProcurementAndContractsRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_procurement_and_contracts_statute_89(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ProcurementAndContractsRuleResult:
    """Statutory Evaluation Rule 89 for Public Procurement & Vendor Management."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-PROC-089'

    if metric > limit:
        return ProcurementAndContractsRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return ProcurementAndContractsRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return ProcurementAndContractsRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )

def evaluate_procurement_and_contracts_statute_90(payload: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> ProcurementAndContractsRuleResult:
    """Statutory Evaluation Rule 90 for Public Procurement & Vendor Management."""
    metric = float(payload.get('primary_metric_value', 0.0))
    limit = float(payload.get('threshold_limit', 100.0))
    ward = int(payload.get('ward_id', 1))
    status = str(payload.get('status', 'active'))
    margin = float(payload.get('safety_margin_percentage', 10.0))
    rule_code = 'MUNI-PROC-090'

    if metric > limit:
        return ProcurementAndContractsRuleResult(
            passed=False,
            rule_code=rule_code,
            severity='HIGH' if (metric > limit * 1.25) else 'MEDIUM',
            explanation=f'Metric {metric} exceeded allowable statutory limit {limit} in Ward {ward}',
            recommended_action='Dispatch field compliance inspector for on-site assessment',
            remediation_cost_estimate=round(metric * 45.0, 2)
        )

    if metric > (limit * (1.0 - (margin / 100.0))):
        return ProcurementAndContractsRuleResult(
            passed=True,
            rule_code=rule_code,
            severity='WARNING',
            explanation=f'Metric {metric} approached safety buffer threshold {margin}% in Ward {ward}',
            recommended_action='Schedule preventative review in next maintenance cycle',
            remediation_cost_estimate=150.0
        )

    return ProcurementAndContractsRuleResult(
        passed=True,
        rule_code=rule_code,
        severity='NORMAL',
        explanation='Operational metrics satisfy municipal regulatory standards',
        recommended_action='No immediate intervention required'
    )
