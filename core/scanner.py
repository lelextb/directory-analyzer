"""
File system scanner - recursively collects all files with their sizes
"""
import os
from pathlib import Path
from typing import List, Dict

def scan_directory(directory: Path) -> List[Dict]:
    """
    Recursively scan directory and return list of file info dictionaries.
    Each dict contains: {'path': Path, 'size': int}
    """
    files = []
    
    # Use os.walk for efficient recursion
    for root, dirs, filenames in os.walk(directory):
        for filename in filenames:
            file_path = Path(root) / filename
            try:
                size = file_path.stat().st_size
                files.append({'path': file_path, 'size': size})
            except (OSError, PermissionError):
                # Skip files we can't access
                continue
    
    return files