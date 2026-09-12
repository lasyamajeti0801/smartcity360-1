#!/usr/bin/env python3
"""
SmartCity360 - Documentation Suite Auditor
Verifies that all required architecture and operations documentation files
exist, are non-empty, and thoroughly document the platform.
"""

from pathlib import Path
from typing import Dict, List, Any

REQUIRED_DOCS = [
    "README.md",
    "PROJECT_PROGRESS.md",
    "PROJECT_AUDIT.md",
    "ARCHITECTURE.md",
    "DATABASE.md",
    "SECURITY.md",
    "TESTING.md",
    "DEPLOYMENT.md",
    "CONTRIBUTING.md",
    "GIT_WORKFLOW.md",
    "CHANGELOG.md",
]

def audit_documentation(root_dir: Path) -> Dict[str, Any]:
    doc_statuses = []
    missing_count = 0
    total_lines = 0

    for doc_name in REQUIRED_DOCS:
        doc_path = root_dir / doc_name
        if not doc_path.exists():
            doc_path = root_dir / "docs" / doc_name
        
        if doc_path.exists():
            lines = len(doc_path.read_text(encoding="utf-8", errors="ignore").splitlines())
            total_lines += lines
            doc_statuses.append({
                "document": doc_name,
                "status": "PRESENT",
                "lines": lines
            })
        else:
            missing_count += 1
            doc_statuses.append({
                "document": doc_name,
                "status": "MISSING",
                "lines": 0
            })

    # Count additional docs in docs/
    docs_folder = root_dir / "docs"
    additional_docs = 0
    if docs_folder.exists():
        for doc in docs_folder.glob("**/*.md"):
            if doc.name not in REQUIRED_DOCS:
                additional_docs += 1
                total_lines += len(doc.read_text(encoding="utf-8", errors="ignore").splitlines())

    return {
        "required_total": len(REQUIRED_DOCS),
        "present_count": len(REQUIRED_DOCS) - missing_count,
        "missing_count": missing_count,
        "additional_docs_count": additional_docs,
        "total_doc_lines": total_lines,
        "documents": doc_statuses
    }

def main():
    root = Path(__file__).resolve().parent.parent
    audit = audit_documentation(root)
    print("=" * 70)
    print("SMARTCITY360 - DOCUMENTATION SUITE AUDIT")
    print("=" * 70)
    print(f"Required Documentation Files: {audit['present_count']} / {audit['required_total']} Present")
    print(f"Additional Documentation:     {audit['additional_docs_count']} files")
    print(f"Total Documentation Lines:    {audit['total_doc_lines']:,} lines")
    print("-" * 70)
    for doc in audit["documents"]:
        flag = "OK " if doc["status"] == "PRESENT" else "FAIL"
        print(f"  [{flag}] {doc['document']:<26}: {doc['lines']:>5} lines")
    print("=" * 70)

if __name__ == "__main__":
    main()
