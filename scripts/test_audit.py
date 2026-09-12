#!/usr/bin/env python3
"""
SmartCity360 - Automated Test Suite Auditor
Inspects pytest and vitest test files and counts test functions.
"""

import re
from pathlib import Path
from typing import Dict, Any

def audit_tests(root_dir: Path) -> Dict[str, Any]:
    test_files = []
    total_test_functions = 0

    # Search in backend/tests and tests/
    candidate_dirs = [root_dir / "backend" / "tests", root_dir / "tests", root_dir / "frontend" / "tests"]
    for c_dir in candidate_dirs:
        if c_dir.exists():
            for f in c_dir.glob("**/*"):
                if f.is_file() and (f.name.startswith("test_") or f.name.endswith("_test.py") or f.name.endswith(".test.ts") or f.name.endswith(".test.tsx")):
                    test_files.append(str(f.relative_to(root_dir)))
                    try:
                        content = f.read_text(encoding="utf-8")
                        # match def test_ or it(" or test("
                        py_matches = re.findall(r'def\s+test_\w+\(', content)
                        js_matches = re.findall(r'(?:it|test)\(\s*["\']', content)
                        total_test_functions += (len(py_matches) + len(js_matches))
                    except Exception:
                        pass

    return {
        "total_test_files": len(test_files),
        "total_test_functions": total_test_functions,
        "test_files": test_files
    }

def main():
    root = Path(__file__).resolve().parent.parent
    audit = audit_tests(root)
    print("=" * 70)
    print("SMARTCITY360 - TEST SUITE AUDIT")
    print("=" * 70)
    print(f"Total Test Files:     {audit['total_test_files']}")
    print(f"Total Test Functions: {audit['total_test_functions']}")
    print("-" * 70)
    for tf in audit["test_files"]:
        print(f"  - {tf}")
    print("=" * 70)

if __name__ == "__main__":
    main()
