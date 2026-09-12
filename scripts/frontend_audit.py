#!/usr/bin/env python3
"""
SmartCity360 - Frontend Component & Architecture Auditor
Audits components, features, hooks, pages, types, and styles.
"""

from pathlib import Path
from typing import Dict, Any

def audit_frontend(root_dir: Path) -> Dict[str, Any]:
    src_dir = root_dir / "frontend" / "src"
    categories = {
        "components": 0,
        "features": 0,
        "pages": 0,
        "hooks": 0,
        "services": 0,
        "types": 0,
        "styles": 0
    }
    file_count = 0

    if src_dir.exists():
        for f in src_dir.glob("**/*"):
            if f.is_file() and f.suffix in {".ts", ".tsx", ".js", ".jsx", ".css"}:
                file_count += 1
                rel_parts = f.relative_to(src_dir).parts
                if len(rel_parts) > 1:
                    cat = rel_parts[0]
                    if cat in categories:
                        categories[cat] += 1

    return {
        "total_frontend_files": file_count,
        "category_counts": categories
    }

def main():
    root = Path(__file__).resolve().parent.parent
    audit = audit_frontend(root)
    print("=" * 70)
    print("SMARTCITY360 - FRONTEND ARCHITECTURE AUDIT")
    print("=" * 70)
    print(f"Total Frontend Source Files: {audit['total_frontend_files']}")
    print("-" * 70)
    for cat, cnt in sorted(audit["category_counts"].items()):
        print(f"  - {cat:<15}: {cnt:>4} files")
    print("=" * 70)

if __name__ == "__main__":
    main()
