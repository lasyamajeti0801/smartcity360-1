#!/usr/bin/env python3
"""
SmartCity360 - Backend Layer Architecture Auditor
Audits services, repositories, schemas, models, and core configuration.
"""

from pathlib import Path
from typing import Dict, Any

def audit_backend_layers(root_dir: Path) -> Dict[str, Any]:
    backend_dir = root_dir / "backend" / "app"
    layers = {
        "models": 0,
        "schemas": 0,
        "repositories": 0,
        "services": 0,
        "api": 0,
        "core": 0,
        "middleware": 0
    }
    file_count = 0

    if backend_dir.exists():
        for py_file in backend_dir.glob("**/*.py"):
            file_count += 1
            rel_parts = py_file.relative_to(backend_dir).parts
            if len(rel_parts) > 1:
                layer = rel_parts[0]
                if layer in layers:
                    layers[layer] += 1

    return {
        "total_backend_files": file_count,
        "layer_counts": layers
    }

def main():
    root = Path(__file__).resolve().parent.parent
    audit = audit_backend_layers(root)
    print("=" * 70)
    print("SMARTCITY360 - BACKEND STRUCTURE AUDIT")
    print("=" * 70)
    print(f"Total Backend Files: {audit['total_backend_files']}")
    print("-" * 70)
    for layer, cnt in sorted(audit["layer_counts"].items()):
        print(f"  - {layer:<15}: {cnt:>4} files")
    print("=" * 70)

if __name__ == "__main__":
    main()
