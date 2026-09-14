import os
import sys
import zipfile
import shutil
from pathlib import Path

def create_root_archive():
    project_root = Path(r"C:\Users\pedha\OneDrive\Desktop\Smart City 360")
    desktop = Path(r"C:\Users\pedha\OneDrive\Desktop")
    downloads = Path(r"C:\Users\pedha\Downloads")

    target_zip = desktop / "repo.zip"
    alt_zip_1 = desktop / "SmartCity360_Project.zip"
    alt_zip_2 = desktop / "SmartCity360_Testing_Package.zip"
    workspace_zip = project_root / "SmartCity360_Project.zip"
    downloads_zip = downloads / "SmartCity360_Project.zip"

    print(f"Creating root-level ZIP package: {target_zip}")

    # Exclusions
    excluded_dirs = {
        'node_modules',
        '.venv',
        'dist',
        '__pycache__',
        '.pytest_cache',
        '.system_generated'
    }
    excluded_extensions = {'.zip', '.pyc', '.tsbuildinfo'}

    file_count = 0
    total_uncompressed_bytes = 0

    with zipfile.ZipFile(target_zip, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=6) as zf:
        for root, dirs, files in os.walk(project_root):
            # Prune excluded directories in-place
            dirs[:] = [d for d in dirs if d not in excluded_dirs]

            rel_root = os.path.relpath(root, project_root)
            if rel_root == '.':
                rel_root = ''

            for file in files:
                ext = os.path.splitext(file)[1].lower()
                if ext in excluded_extensions:
                    continue

                full_path = Path(root) / file
                arcname = (Path(rel_root) / file).as_posix() if rel_root else file

                try:
                    zf.write(full_path, arcname=arcname)
                    file_count += 1
                    total_uncompressed_bytes += full_path.stat().st_size
                except Exception as e:
                    print(f"Warning: could not add {arcname}: {e}")

    zip_size_mb = target_zip.stat().st_size / (1024 * 1024)
    print(f"Successfully created {target_zip.name}:")
    print(f"  Files Added: {file_count:,}")
    print(f"  Uncompressed Size: {total_uncompressed_bytes / (1024 * 1024):.2f} MB")
    print(f"  ZIP Archive Size: {zip_size_mb:.2f} MB")

    # Copy to mirror destinations
    print("Copying to mirror locations...")
    shutil.copy2(target_zip, alt_zip_1)
    shutil.copy2(target_zip, alt_zip_2)
    shutil.copy2(target_zip, workspace_zip)
    try:
        downloads.mkdir(parents=True, exist_ok=True)
        shutil.copy2(target_zip, downloads_zip)
        print(f"  Copied to: {downloads_zip}")
    except Exception as e:
        print(f"  Note on downloads copy: {e}")

    print(f"  Copied to: {alt_zip_1}")
    print(f"  Copied to: {alt_zip_2}")
    print(f"  Copied to: {workspace_zip}")

    # Verify root structure
    print("Verifying archive integrity & root entries:")
    with zipfile.ZipFile(target_zip, 'r') as zf:
        namelist = set(zf.namelist())
        checks = [
            'main.py',
            'package.json',
            'README.md',
            '.git/HEAD',
            'backend/app/main.py',
            'frontend/src/app/App.tsx',
            'frontend/src/features/citizen/CitizenDashboard.tsx',
            'frontend/src/features/admin/AdminDashboard.tsx'
        ]
        all_passed = True
        for item in checks:
            if item in namelist:
                print(f"  [PASS] Found at archive root: {item}")
            else:
                print(f"  [FAIL] Missing: {item}")
                all_passed = False

        if all_passed:
            print("\nALL ARCHIVE ROOT INTEGRITY CHECKS PASSED!")
        else:
            print("\nSome archive root checks failed.")

if __name__ == '__main__':
    create_root_archive()
