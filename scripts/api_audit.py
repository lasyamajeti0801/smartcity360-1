#!/usr/bin/env python3
"""
SmartCity360 - API Endpoints & Route Auditor
Inspects FastAPI route decorators across api/v1 modules to track endpoints and REST coverage.
"""

import ast
import re
from pathlib import Path
from typing import Dict, List, Any

HTTP_METHODS = {"get", "post", "put", "patch", "delete", "options", "head"}

def audit_api_endpoints(root_dir: Path) -> Dict[str, Any]:
    api_dir = root_dir / "backend" / "app" / "api"
    endpoints = []
    by_method: Dict[str, int] = {}

    if api_dir.exists():
        for py_file in api_dir.glob("**/*.py"):
            try:
                content = py_file.read_text(encoding="utf-8")
                # regex match @router.(get|post|put|delete|patch)("...")
                matches = re.findall(r'@router\.(get|post|put|patch|delete)\(\s*["\']([^"\']*)["\']', content)
                for method, path in matches:
                    method_upper = method.upper()
                    endpoints.append({
                        "method": method_upper,
                        "path": path,
                        "file": str(py_file.relative_to(root_dir))
                    })
                    by_method[method_upper] = by_method.get(method_upper, 0) + 1
            except Exception:
                pass

    return {
        "total_endpoints": len(endpoints),
        "by_method": by_method,
        "endpoints": endpoints
    }

def main():
    root = Path(__file__).resolve().parent.parent
    audit = audit_api_endpoints(root)
    print("=" * 70)
    print("SMARTCITY360 - API ARCHITECTURE AUDIT")
    print("=" * 70)
    print(f"Total API Endpoints: {audit['total_endpoints']}")
    print("-" * 70)
    print("ENDPOINTS BY METHOD:")
    for m, count in sorted(audit["by_method"].items()):
        print(f"  - {m:<8}: {count:>4}")
    print("-" * 70)
    print("SAMPLE ENDPOINTS:")
    for ep in audit["endpoints"][:10]:
        print(f"  [{ep['method']}] {ep['path']} ({ep['file']})")
    print("=" * 70)

if __name__ == "__main__":
    main()
