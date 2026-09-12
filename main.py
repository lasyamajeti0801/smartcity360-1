#!/usr/bin/env python3
"""
SmartCity360 - Integrated Urban Management & Citizen Services Platform
Primary Application Entry Point
"""

import os
import sys
import uvicorn
from pathlib import Path

# Ensure backend directory is in python path
ROOT_DIR = Path(__file__).resolve().parent
BACKEND_DIR = ROOT_DIR / "backend"
sys.path.insert(0, str(BACKEND_DIR))

from app.main import app

def run_server():
    """Start uvicorn server for SmartCity360 API."""
    port = int(os.getenv("PORT", 8000))
    host = os.getenv("HOST", "0.0.0.0")
    print(f"Starting SmartCity360 Unified Urban Platform on {host}:{port}")
    uvicorn.run(app, host=host, port=port, log_level="info")

if __name__ == "__main__":
    run_server()
