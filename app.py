#!/usr/bin/env python3
"""
SmartCity360 - Application Factory Export
Exposes FastAPI application instance at project root.
"""

import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent
BACKEND_DIR = ROOT_DIR / "backend"
sys.path.insert(0, str(BACKEND_DIR))

from app.main import app

__all__ = ["app"]
