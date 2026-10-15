import os
import sys
import zipfile
import shutil
from pathlib import Path

def create_trainplex_zip():
    repo_root = Path(__file__).resolve().parent.parent
    downloads_dir = repo_root.parent
    
    # Destination zip paths
    destinations = [
        repo_root / "SmartCity360_Project.zip",
        downloads_dir / "SmartCity360_Project.zip",
        downloads_dir / "repo (2).zip",
        downloads_dir / "repo.zip",
    ]
    
    primary_zip = destinations[0]
    print(f"Packaging TrainPlex compliant archive from: {repo_root}")

    # Exclusions - NOTE: .git is explicitly INCLUDED for TrainPlex git verification!
    excluded_dirs = {
        'node_modules',
        '.venv',
        'venv',
        'dist',
        '__pycache__',
        '.pytest_cache',
        '.system_generated'
    }
    
    excluded_extensions = {'.zip', '.pyc', '.pyo'}
    excluded_filenames = {'.DS_Store', 'Thumbs.db'}

    file_count = 0
    git_file_count = 0
    total_uncompressed_bytes = 0

    with zipfile.ZipFile(primary_zip, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=6) as zf:
        for root, dirs, files in os.walk(repo_root):
            # Prune excluded directories in-place so os.walk does not traverse them
            dirs[:] = [d for d in dirs if d not in excluded_dirs]

            rel_root = os.path.relpath(root, repo_root)
            if rel_root == '.':
                rel_root = ''

            for file in files:
                if file in excluded_filenames:
                    continue
                ext = os.path.splitext(file)[1].lower()
                if ext in excluded_extensions:
                    continue

                full_path = Path(root) / file
                
                # Never include the output zip in itself
                if full_path.name.endswith('.zip'):
                    continue

                # Root-level arcname (so .git is at .git/ and main.py is at main.py)
                arcname = (Path(rel_root) / file).as_posix() if rel_root else file

                try:
                    zf.write(full_path, arcname=arcname)
                    file_count += 1
                    if arcname.startswith('.git/'):
                        git_file_count += 1
                    total_uncompressed_bytes += full_path.stat().st_size
                except Exception as e:
                    print(f"Warning: could not add {arcname}: {e}")

    zip_size_mb = primary_zip.stat().st_size / (1024 * 1024)
    print(f"\nSuccessfully created primary archive: {primary_zip.name}")
    print(f"  Total Files Packaged: {file_count:,}")
    print(f"  .git History Files:   {git_file_count:,} (Guarantees TrainPlex Git PASS)")
    print(f"  Uncompressed Size:    {total_uncompressed_bytes / (1024 * 1024):.2f} MB")
    print(f"  Compressed ZIP Size:  {zip_size_mb:.2f} MB")

    # Mirror to all target paths
    print("\nCopying to mirror destinations:")
    for dest in destinations[1:]:
        try:
            shutil.copy2(primary_zip, dest)
            print(f"  [OK] Copied to: {dest}")
        except Exception as e:
            print(f"  [Notice] Could not copy to {dest}: {e}")

    print("\nTrainPlex Archive Packaging Complete!")

if __name__ == '__main__':
    create_trainplex_zip()
