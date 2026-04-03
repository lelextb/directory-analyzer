"""
Statistics analyzer - computes file metrics from scan results
"""
from collections import Counter
from pathlib import Path
from typing import List, Dict, Tuple

def analyze_files(files: List[Dict]) -> Dict:
    """
    Analyze list of files and return statistics dictionary.
    """
    if not files:
        return {}
    
    total_files = len(files)
    total_size = sum(f['size'] for f in files)
    
    # Find largest and smallest
    largest = max(files, key=lambda x: x['size'])
    smallest = min(files, key=lambda x: x['size'])
    
    # Count extensions
    extensions = []
    for f in files:
        ext = f['path'].suffix.lower()
        if ext:
            extensions.append(ext)
        else:
            extensions.append('[no extension]')
    
    ext_counts = Counter(extensions)
    top_extensions = ext_counts.most_common(3)
    
    return {
        'total_files': total_files,
        'total_size': total_size,
        'largest': {'path': largest['path'], 'size': largest['size']},
        'smallest': {'path': smallest['path'], 'size': smallest['size']},
        'top_extensions': top_extensions
    }