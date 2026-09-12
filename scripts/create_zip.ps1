# SmartCity360 - Complete Testing Package Generator (LOC & Commit Verification)
# Packages the entire repository INCLUDING the full .git repository for commit & LOC audit testing.

$ErrorActionPreference = "Stop"

$ProjectRoot = "C:\Users\pedha\OneDrive\Desktop\Smart City 360"
$ExportFolder = "C:\Users\pedha\OneDrive\Desktop\SmartCity360"
$ZipTargetDesktop = "C:\Users\pedha\OneDrive\Desktop\SmartCity360_Testing_Package.zip"
$ZipTargetWorkspace = "C:\Users\pedha\OneDrive\Desktop\Smart City 360\SmartCity360_Testing_Package.zip"
$ZipStandardDesktop = "C:\Users\pedha\OneDrive\Desktop\SmartCity360_Project.zip"

Write-Host "Creating clean testing export directory..." -ForegroundColor Cyan
if (Test-Path $ExportFolder) {
    Remove-Item -Recurse -Force $ExportFolder
}
New-Item -ItemType Directory -Path $ExportFolder | Out-Null

# 1. Copy .git folder for commit count & git history testing
Write-Host "Copying .git repository history (for commit verification)..." -ForegroundColor Green
$SrcGit = Join-Path $ProjectRoot ".git"
$DstGit = Join-Path $ExportFolder ".git"
robocopy $SrcGit $DstGit /E /NFL /NDL | Out-Null

# 2. Directories to copy
$Directories = @("backend", "database", "data", "ml", "scripts", "docs", "docker", "frontend")

foreach ($Dir in $Directories) {
    $SrcDir = Join-Path $ProjectRoot $Dir
    $DstDir = Join-Path $ExportFolder $Dir
    if (Test-Path $SrcDir) {
        Write-Host "Copying $Dir (excluding transient node_modules/.venv)..." -ForegroundColor Gray
        robocopy $SrcDir $DstDir /E /XD node_modules dist __pycache__ .pytest_cache .venv /XF *.pyc *.tsbuildinfo /NFL /NDL | Out-Null
    }
}

# 3. Copy root project files
Write-Host "Copying root files and configs..." -ForegroundColor Gray
Get-ChildItem -Path $ProjectRoot -File | Where-Object { $_.Name -notmatch '\.zip$' } | ForEach-Object {
    Copy-Item $_.FullName -Destination $ExportFolder
}

# 4. Compress package with Windows tar.exe
Write-Host "Compressing complete testing archive..." -ForegroundColor Cyan
if (Test-Path $ZipTargetDesktop) {
    Remove-Item -Force $ZipTargetDesktop
}

tar.exe -a -c -f $ZipTargetDesktop -C "C:\Users\pedha\OneDrive\Desktop" SmartCity360

Copy-Item $ZipTargetDesktop -Destination $ZipTargetWorkspace -Force
Copy-Item $ZipTargetDesktop -Destination $ZipStandardDesktop -Force
Copy-Item $ZipTargetDesktop -Destination "C:\Users\pedha\Downloads\SmartCity360_Project.zip" -Force


# Clean staging folder
Remove-Item -Recurse -Force $ExportFolder

$FileSize = (Get-Item $ZipTargetDesktop).Length / 1MB
Write-Host ""
Write-Host "======================================================================" -ForegroundColor Green
Write-Host "TESTING PACKAGE (WITH FULL GIT & COMMIT HISTORY) CREATED!" -ForegroundColor Green
Write-Host ("Desktop Archive:   {0} ({1:N2} MB)" -f $ZipTargetDesktop, $FileSize) -ForegroundColor White
Write-Host ("Workspace Archive: {0} ({1:N2} MB)" -f $ZipTargetWorkspace, $FileSize) -ForegroundColor White
Write-Host "======================================================================" -ForegroundColor Green
