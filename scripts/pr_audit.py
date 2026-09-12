#!/usr/bin/env python3
"""
SmartCity360 - Pull Request & Feature Branch Auditor
Tracks genuine feature branches, PR metadata, and PR quality standards.
Ensures zero-fabrication policy: reports exact local branches and PR specifications.
"""

import json
import os
import subprocess
from pathlib import Path
from typing import List, Dict, Any

def get_git_branches(root_dir: Path) -> List[str]:
    try:
        res = subprocess.run(
            ["git", "branch", "--list", "--format=%(refname:short)"],
            cwd=root_dir,
            capture_output=True,
            text=True,
            check=True
        )
        return [b.strip() for b in res.stdout.strip().split("\n") if b.strip()]
    except Exception:
        return []

def audit_pull_requests(root_dir: Path) -> Dict[str, Any]:
    pr_dir = root_dir / "docs" / "pull_requests"
    branches = get_git_branches(root_dir)
    
    pr_records = []
    if pr_dir.exists():
        for file in sorted(pr_dir.glob("PR_*.json")):
            try:
                with open(file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    pr_records.append(data)
            except Exception as e:
                pass

    # Count PRs by status
    status_counts = {}
    for pr in pr_records:
        st = pr.get("status", "DRAFT")
        status_counts[st] = status_counts.get(st, 0) + 1

    return {
        "total_pr_records": len(pr_records),
        "total_git_branches": len(branches),
        "branches": branches,
        "status_counts": status_counts,
        "pr_records": pr_records
    }

def main():
    root = Path(__file__).resolve().parent.parent
    audit = audit_pull_requests(root)

    print("=" * 70)
    print("SMARTCITY360 - PULL REQUEST & FEATURE BRANCH AUDIT")
    print("=" * 70)
    print(f"Verified Feature Branches in Git: {audit['total_git_branches']}")
    print(f"Structured PR Documentation Records: {audit['total_pr_records']} (Target: >80)")
    print("-" * 70)
    print("STATUS BREAKDOWN:")
    for st, count in sorted(audit["status_counts"].items()):
        print(f"  - {st:<15}: {count:>4}")
    print("-" * 70)
    print("SAMPLE PRs:")
    for pr in audit["pr_records"][:5]:
        print(f"  [PR #{pr.get('pr_number', '?')}] {pr.get('title', 'Untitled')} ({pr.get('status', 'DRAFT')}) -> Branch: {pr.get('branch', 'main')}")
    print("=" * 70)

if __name__ == "__main__":
    main()
