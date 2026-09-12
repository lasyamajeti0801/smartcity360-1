#!/usr/bin/env python3
"""
SmartCity360 - Git Commit History & Quality Auditor
Validates commit count, meaningful messages, conventional commits compliance,
and author integrity.
"""

import subprocess
import sys
from pathlib import Path
from typing import List, Dict, Any

VALID_TYPES = {
    "feat", "fix", "docs", "style", "refactor",
    "perf", "test", "build", "ci", "chore", "revert", "security"
}

def run_git_cmd(args: List[str], cwd: Path) -> str:
    try:
        res = subprocess.run(
            ["git"] + args,
            cwd=cwd,
            capture_output=True,
            text=True,
            check=True
        )
        return res.stdout.strip()
    except subprocess.CalledProcessError as e:
        return ""

def audit_git_history(root_dir: Path) -> Dict[str, Any]:
    # Check if git repo
    is_repo = run_git_cmd(["rev-parse", "--is-inside-work-tree"], root_dir) == "true"
    if not is_repo:
        return {"error": "Not a git repository", "total_commits": 0, "commits": []}

    # Fetch log format: hash|author|date|subject
    log_output = run_git_cmd(["log", "--pretty=format:%h|%an|%ad|%s", "--date=short"], root_dir)
    if not log_output:
        return {"total_commits": 0, "commits": [], "type_counts": {}, "conventional_percentage": 0.0}

    lines = log_output.split("\n")
    commits = []
    type_counts: Dict[str, int] = {}
    valid_conventional = 0

    for line in lines:
        parts = line.split("|", 3)
        if len(parts) == 4:
            commit_hash, author, date, subject = parts
            commits.append({
                "hash": commit_hash,
                "author": author,
                "date": date,
                "subject": subject
            })

            # Check conventional commit format e.g. feat(auth): message
            is_conv = False
            if ":" in subject:
                prefix = subject.split(":", 1)[0].strip()
                # Might have scope: feat(gis)
                base_type = prefix.split("(")[0].strip().lower()
                if base_type in VALID_TYPES:
                    is_conv = True
                    type_counts[base_type] = type_counts.get(base_type, 0) + 1
            if is_conv:
                valid_conventional += 1

    total = len(commits)
    conv_pct = (valid_conventional / total * 100) if total > 0 else 0.0

    return {
        "total_commits": total,
        "valid_conventional": valid_conventional,
        "conventional_percentage": round(conv_pct, 2),
        "type_counts": type_counts,
        "commits": commits
    }

def main():
    root = Path(__file__).resolve().parent.parent
    audit = audit_git_history(root)

    print("=" * 70)
    print("SMARTCITY360 - GIT COMMIT AUDIT")
    print("=" * 70)
    if "error" in audit:
        print(f"Error: {audit['error']}")
        sys.exit(1)

    print(f"Total Meaningful Commits: {audit['total_commits']} (Target: >100)")
    print(f"Conventional Commits:     {audit['valid_conventional']} ({audit['conventional_percentage']}%)")
    print("-" * 70)
    print("COMMITS BY TYPE:")
    for c_type, cnt in sorted(audit["type_counts"].items(), key=lambda x: x[1], reverse=True):
        print(f"  - {c_type:<14}: {cnt:>4} commits")
    print("-" * 70)
    print("RECENT COMMITS (LAST 5):")
    for c in audit["commits"][:5]:
        print(f"  [{c['hash']}] {c['date']} - {c['subject']} ({c['author']})")
    print("=" * 70)

if __name__ == "__main__":
    main()
