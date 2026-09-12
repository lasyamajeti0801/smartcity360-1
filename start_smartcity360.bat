@echo off
title SmartCity360 - Unified Municipal Platform Launcher
echo ======================================================================
echo SMARTCITY360 - INTEGRATED URBAN MANAGEMENT ^& CITIZEN SERVICES PLATFORM
echo ======================================================================
echo.
echo [1/3] Starting FastAPI Backend on http://127.0.0.1:8000 ...
start "SmartCity360 Backend (FastAPI)" cmd /k "cd /d %~dp0 && .\.venv\Scripts\python -m uvicorn backend.app.main:app --host 127.0.0.1 --port 8000"

echo [2/3] Starting React + Vite + Leaflet GIS Frontend on http://127.0.0.1:5173 ...
start "SmartCity360 Frontend (React + Vite)" cmd /k "cd /d %~dp0\frontend && npm.cmd run dev"

echo [3/3] Waiting 4 seconds for server initialization...
timeout /t 4 /nobreak >nul

echo.
echo Opening SmartCity360 in your browser...
start http://127.0.0.1:5173
start http://127.0.0.1:8000/docs

echo ======================================================================
echo SMARTCITY360 IS RUNNING!
echo.
echo Frontend Portal:  http://127.0.0.1:5173
echo Backend API Docs: http://127.0.0.1:8000/docs
echo.
echo DEMO ACCOUNTS:
echo - City Admin:       admin@smartcity360.local       / AdminSecurePass2026!
echo - Citizen Portal:   citizen@smartcity360.local     / CitizenSecurePass2026!
echo - Field Staff:      staff.roads@smartcity360.local / StaffSecurePass2026!
echo - 911 Dispatcher:   emergency@smartcity360.local   / EmergencySecurePass2026!
echo ======================================================================
echo Keep this window open or close it when finished.
pause
