#!/usr/bin/env python3
"""
SmartCity360 - Database Schema & Model Auditor
Inspects SQLAlchemy models, tables, columns, and relations across all civic modules.
"""

import ast
import re
from pathlib import Path
from typing import Dict, List, Any

def audit_database_models(root_dir: Path) -> Dict[str, Any]:
    models_dir = root_dir / "backend" / "app" / "models"
    tables = []
    model_classes = []

    if models_dir.exists():
        for py_file in models_dir.glob("**/*.py"):
            if py_file.name == "__init__.py":
                continue
            try:
                content = py_file.read_text(encoding="utf-8")
                # Look for __tablename__ = "..."
                found_tables = re.findall(r'__tablename__\s*=\s*["\']([^"\']+)["\']', content)
                for t in found_tables:
                    tables.append({"table": t, "file": str(py_file.relative_to(root_dir))})

                # Look for class ... (Base):
                tree = ast.parse(content)
                for node in ast.walk(tree):
                    if isinstance(node, ast.ClassDef):
                        # check if it inherits from Base or similar
                        for base in node.bases:
                            if (isinstance(base, ast.Name) and base.id in {"Base", "TimeStampedBase"}) or \
                               (isinstance(base, ast.Attribute) and base.attr in {"Base", "TimeStampedBase"}):
                                model_classes.append({
                                    "class_name": node.name,
                                    "file": str(py_file.relative_to(root_dir))
                                })
            except Exception:
                pass

    return {
        "total_tables": len(tables),
        "total_models": len(model_classes),
        "tables": tables,
        "models": model_classes
    }

def main():
    root = Path(__file__).resolve().parent.parent
    audit = audit_database_models(root)
    print("=" * 70)
    print("SMARTCITY360 - DATABASE ARCHITECTURE AUDIT")
    print("=" * 70)
    print(f"Total Database Tables Defined: {audit['total_tables']}")
    print(f"Total Model Classes:          {audit['total_models']}")
    print("-" * 70)
    print("DETECTED TABLES:")
    for t in audit["tables"]:
        print(f"  - {t['table']:<30} in {t['file']}")
    print("=" * 70)

if __name__ == "__main__":
    main()
