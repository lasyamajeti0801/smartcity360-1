# SmartCity360 - PowerShell Quick Launcher
Write-Host "======================================================================" -ForegroundColor Cyan
Write-Host "SMARTCITY360 - INTEGRATED URBAN MANAGEMENT & CITIZEN SERVICES PLATFORM" -ForegroundColor Cyan
Write-Host "======================================================================" -ForegroundColor Cyan

$Root = Split-Path -Parent $MyInvocation.MyCommand.Path

Write-Host "`n[1/3] Launching FastAPI Backend on http://127.0.0.1:8000..." -ForegroundColor Green
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$Root'; .\.venv\Scripts\python -m uvicorn backend.app.main:app --host 127.0.0.1 --port 8000"

Write-Host "[2/3] Launching React Vite GIS Frontend on http://127.0.0.1:5173..." -ForegroundColor Green
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$Root\frontend'; npm.cmd run dev"

Start-Sleep -Seconds 3

Write-Host "`n[3/3] Opening browser tabs..." -ForegroundColor Green
Start-Process "http://127.0.0.1:5173"
Start-Process "http://127.0.0.1:8000/docs"

Write-Host "`n======================================================================" -ForegroundColor Yellow
Write-Host "SMARTCITY360 IS RUNNING!" -ForegroundColor Yellow
Write-Host "Frontend Portal:  http://127.0.0.1:5173" -ForegroundColor White
Write-Host "Backend API Docs: http://127.0.0.1:8000/docs" -ForegroundColor White
Write-Host "`nDEMO CREDENTIALS:" -ForegroundColor Yellow
Write-Host "  Admin:       admin@smartcity360.local       / AdminSecurePass2026!" -ForegroundColor White
Write-Host "  Citizen:     citizen@smartcity360.local     / CitizenSecurePass2026!" -ForegroundColor White
Write-Host "  Field Staff: staff.roads@smartcity360.local / StaffSecurePass2026!" -ForegroundColor White
Write-Host "  Emergency:   emergency@smartcity360.local   / EmergencySecurePass2026!" -ForegroundColor White
Write-Host "======================================================================`n" -ForegroundColor Yellow
