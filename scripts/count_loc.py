#!/usr/bin/env python3
"""
SmartCity360 - LOC (Lines of Code) Counter and Source Metrics Auditor
Strict Zero-Fake-Metrics Policy: Distinguishes genuine production code from
tests, docs, configs, and third-party dependencies/caches.
"""

import os
import sys
from pathlib import Path
from typing import Dict, List, Tuple, Any

EXCLUDED_DIRS = {
    "node_modules",
    ".venv",
    "venv",
    "env",
    "dist",
    "build",
    ".git",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
    "coverage",
    "htmlcov",
    ".idea",
    ".vscode",
    "dist-ssr",
    ".system_generated"
}

PRODUCTION_EXTENSIONS = {
    ".py": "Python",
    ".ts": "TypeScript",
    ".tsx": "TypeScript (React)",
    ".js": "JavaScript",
    ".jsx": "JavaScript (React)",
    ".sql": "SQL / DDL",
    ".css": "CSS / Styles",
    ".sh": "Shell Script",
    ".ps1": "PowerShell",
}

DOCS_EXTENSIONS = {
    ".md": "Markdown",
    ".rst": "ReStructuredText",
    ".txt": "Text Docs",
}

CONFIG_EXTENSIONS = {
    ".json": "JSON Config",
    ".yaml": "YAML Config",
    ".yml": "YAML Config",
    ".toml": "TOML Config",
    ".ini": "INI Config",
    ".env.example": "Env Template",
}

def is_test_file(path: Path) -> bool:
    name = path.name.lower()
    parts = [p.lower() for p in path.parts]
    return (
        "test" in parts
        or "tests" in parts
        or name.startswith("test_")
        or name.endswith("_test.py")
        or name.endswith(".test.ts")
        or name.endswith(".test.tsx")
        or name.endswith(".spec.ts")
        or name.endswith(".spec.tsx")
    )

def count_file_lines(path: Path) -> Tuple[int, int, int]:
    """
    Returns (total_lines, code_lines, blank_lines)
    """
    total = 0
    blank = 0
    code = 0
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                total += 1
                stripped = line.strip()
                if not stripped:
                    blank += 1
                elif stripped.startswith("#") or stripped.startswith("//") or stripped.startswith("/*") or stripped.startswith("*"):
                    # Comment line
                    pass
                else:
                    code += 1
    except Exception:
        return 0, 0, 0
    return total, code, blank

def scan_directory(root_dir: Path) -> Dict[str, Any]:
    stats = {
        "production": {
            "total_lines": 0,
            "code_lines": 0,
            "blank_lines": 0,
            "files": 0,
            "by_language": {},
            "file_list": []
        },
        "tests": {
            "total_lines": 0,
            "code_lines": 0,
            "blank_lines": 0,
            "files": 0,
            "file_list": []
        },
        "docs": {
            "total_lines": 0,
            "files": 0,
            "file_list": []
        },
        "config": {
            "total_lines": 0,
            "files": 0,
            "file_list": []
        }
    }

    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Prune excluded dirs in-place
        dirnames[:] = [d for d in dirnames if d not in EXCLUDED_DIRS]
        
        for fname in filenames:
            fpath = Path(dirpath) / fname
            rel_path = fpath.relative_to(root_dir)
            ext = fpath.suffix.lower()

            if is_test_file(fpath):
                t, c, b = count_file_lines(fpath)
                stats["tests"]["total_lines"] += t
                stats["tests"]["code_lines"] += c
                stats["tests"]["blank_lines"] += b
                stats["tests"]["files"] += 1
                stats["tests"]["file_list"].append((str(rel_path), t, c))
            elif ext in PRODUCTION_EXTENSIONS:
                t, c, b = count_file_lines(fpath)
                lang = PRODUCTION_EXTENSIONS[ext]
                stats["production"]["total_lines"] += t
                stats["production"]["code_lines"] += c
                stats["production"]["blank_lines"] += b
                stats["production"]["files"] += 1
                stats["production"]["file_list"].append((str(rel_path), t, c))

                if lang not in stats["production"]["by_language"]:
                    stats["production"]["by_language"][lang] = {"files": 0, "lines": 0, "code_lines": 0}
                stats["production"]["by_language"][lang]["files"] += 1
                stats["production"]["by_language"][lang]["lines"] += t
                stats["production"]["by_language"][lang]["code_lines"] += c
            elif ext in DOCS_EXTENSIONS:
                t, _, _ = count_file_lines(fpath)
                stats["docs"]["total_lines"] += t
                stats["docs"]["files"] += 1
                stats["docs"]["file_list"].append((str(rel_path), t))
            elif ext in CONFIG_EXTENSIONS or fname in [".gitignore", "Dockerfile", "docker-compose.yml"]:
                t, _, _ = count_file_lines(fpath)
                stats["config"]["total_lines"] += t
                stats["config"]["files"] += 1
                stats["config"]["file_list"].append((str(rel_path), t))

    return stats

def main():
    root = Path(__file__).resolve().parent.parent
    stats = scan_directory(root)

    print("=" * 70)
    print("SMARTCITY360 - VERIFIED SOURCE METRICS & LOC AUDIT")
    print("=" * 70)
    print(f"Production Source Code:  {stats['production']['total_lines']:,} lines ({stats['production']['code_lines']:,} code lines) in {stats['production']['files']} files")
    print(f"Test Code:               {stats['tests']['total_lines']:,} lines ({stats['tests']['code_lines']:,} code lines) in {stats['tests']['files']} files")
    print(f"Documentation:           {stats['docs']['total_lines']:,} lines in {stats['docs']['files']} files")
    print(f"Configuration & Ops:     {stats['config']['total_lines']:,} lines in {stats['config']['files']} files")
    print("-" * 70)
    print("PRODUCTION BREAKDOWN BY LANGUAGE:")
    for lang, data in sorted(stats["production"]["by_language"].items(), key=lambda x: x[1]["lines"], reverse=True):
        print(f"  - {lang:<22}: {data['lines']:>8,} lines ({data['code_lines']:>8,} code) across {data['files']:>4} files")
    print("=" * 70)

if __name__ == "__main__":
    main()
