"""
Formatting utilities for human-readable output
"""
import math

def human_readable_size(size_bytes: int) -> str:
    """Convert bytes to human readable format (KB, MB, GB)"""
    if size_bytes == 0:
        return "0 B"
    
    units = ['B', 'KB', 'MB', 'GB', 'TB']
    unit_index = int(math.floor(math.log(size_bytes, 1024)))
    unit_index = min(unit_index, len(units) - 1)
    
    size = size_bytes / (1024 ** unit_index)
    return f"{size:.2f} {units[unit_index]}"