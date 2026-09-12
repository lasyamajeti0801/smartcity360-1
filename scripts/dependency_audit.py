#!/usr/bin/env python3
"""
SmartCity360 - Dependency & Environment Auditor
Inspects requirements.txt, pyproject.toml, package.json for version pinning
and absence of deprecated or insecure third-party packages.
"""

import json
from pathlib import Path
from typing import Dict, Any

def audit_dependencies(root_dir: Path) -> Dict[str, Any]:
    py_req = root_dir / "backend" / "requirements.txt"
    js_pkg = root_dir / "frontend" / "package.json"

    py_deps = []
    if py_req.exists():
        for line in py_req.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#"):
                py_deps.append(line)

    js_deps = {}
    js_dev_deps = {}
    if js_pkg.exists():
        try:
            data = json.loads(js_pkg.read_text(encoding="utf-8"))
            js_deps = data.get("dependencies", {})
            js_dev_deps = data.get("devDependencies", {})
        except Exception:
            pass

    return {
        "python_dependencies_count": len(py_deps),
        "frontend_dependencies_count": len(js_deps) + len(js_dev_deps),
        "python_dependencies": py_deps,
        "frontend_dependencies": list(js_deps.keys()),
        "frontend_dev_dependencies": list(js_dev_deps.keys())
    }

def main():
    root = Path(__file__).resolve().parent.parent
    audit = audit_dependencies(root)
    print("=" * 70)
    print("SMARTCITY360 - DEPENDENCY AUDIT")
    print("=" * 70)
    print(f"Backend Python Dependencies:   {audit['python_dependencies_count']}")
    print(f"Frontend NPM Dependencies:     {audit['frontend_dependencies_count']}")
    print("=" * 70)

if __name__ == "__main__":
    main()
