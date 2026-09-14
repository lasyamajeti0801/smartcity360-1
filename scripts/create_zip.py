import os
import zipfile
import shutil

EXCLUDE_DIRS = {
    'node_modules',
    '.venv',
    'venv',
    '.git',
    'dist',
    '__pycache__',
    '.pytest_cache',
    '.idea',
    '.vscode',
    'brain',
    '.system_generated'
}

EXCLUDE_EXTS = {
    '.pyc',
    '.pyo',
    '.zip'
}

EXCLUDE_FILES = {
    '.DS_Store',
    'Thumbs.db'
}

def create_project_zip():
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    output_zip_in_repo = os.path.join(repo_root, 'SmartCity360_Project.zip')
    downloads_dir = os.path.abspath(os.path.join(repo_root, '..'))
    output_zip_in_downloads = os.path.join(downloads_dir, 'SmartCity360_Project.zip')

    print(f"Packaging repository from: {repo_root}")
    
    file_count = 0
    total_uncompressed_bytes = 0

    with zipfile.ZipFile(output_zip_in_repo, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(repo_root):
            # Filter directories in-place
            dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS and not d.startswith('.git')]
            
            for file in files:
                if file in EXCLUDE_FILES:
                    continue
                ext = os.path.splitext(file)[1].lower()
                if ext in EXCLUDE_EXTS:
                    continue
                
                full_path = os.path.join(root, file)
                if os.path.abspath(full_path) in (os.path.abspath(output_zip_in_repo), os.path.abspath(output_zip_in_downloads)):
                    continue
                
                rel_path = os.path.relpath(full_path, repo_root)
                archive_name = os.path.join('SmartCity360', rel_path)
                
                try:
                    file_size = os.path.getsize(full_path)
                    zipf.write(full_path, archive_name)
                    file_count += 1
                    total_uncompressed_bytes += file_size
                except Exception as e:
                    print(f"Skipping {rel_path}: {e}")

    zip_size_bytes = os.path.getsize(output_zip_in_repo)
    zip_size_mb = zip_size_bytes / (1024 * 1024)
    uncompressed_mb = total_uncompressed_bytes / (1024 * 1024)

    try:
        shutil.copy2(output_zip_in_repo, output_zip_in_downloads)
        print(f"Copied zip to Downloads folder: {output_zip_in_downloads}")
    except Exception as e:
        print(f"Note on copy: {e}")

    print(f"\nSuccessfully created clean SmartCity360 project zip archive!")
    print(f"- Total files packaged: {file_count}")
    print(f"- Uncompressed size: {uncompressed_mb:.2f} MB")
    print(f"- Compressed zip size: {zip_size_mb:.2f} MB")
    print(f"- Primary path: {output_zip_in_repo}")
    if os.path.exists(output_zip_in_downloads):
        print(f"- Downloads folder path: {output_zip_in_downloads}")

if __name__ == '__main__':
    create_project_zip()
