"""
Report generation and output handling
"""
from pathlib import Path
from utils.formatters import human_readable_size

def print_report(stats: dict):
    """Print formatted report to console"""
    print("\n" + "="*50)
    print("ANALYSIS REPORT")
    print("="*50)
    
    print(f"\nTotal files: {stats['total_files']}")
    print(f"Total size: {human_readable_size(stats['total_size'])}")
    
    print(f"\nLargest file: {stats['largest']['path'].name} "
          f"({human_readable_size(stats['largest']['size'])})")
    
    print(f"Smallest file: {stats['smallest']['path'].name} "
          f"({human_readable_size(stats['smallest']['size'])})")
    
    print("\nTop 3 most common extensions:")
    for i, (ext, count) in enumerate(stats['top_extensions'], 1):
        print(f"{i}. {ext} ({count} files)")
    
    print("\n" + "="*50)

def save_report(stats: dict, dir_name: str):
    """Save report to a text file"""
    output_file = Path(f"report_{dir_name}.txt")
    
    with open(output_file, 'w') as f:
        f.write("DIRECTORY FILE ANALYZER REPORT\n")
        f.write("="*50 + "\n\n")
        f.write(f"Total files: {stats['total_files']}\n")
        f.write(f"Total size: {human_readable_size(stats['total_size'])}\n\n")
        
        f.write(f"Largest file: {stats['largest']['path']} "
                f"({human_readable_size(stats['largest']['size'])})\n")
        f.write(f"Smallest file: {stats['smallest']['path']} "
                f"({human_readable_size(stats['smallest']['size'])})\n\n")
        
        f.write("Top 3 most common extensions:\n")
        for i, (ext, count) in enumerate(stats['top_extensions'], 1):
            f.write(f"{i}. {ext} ({count} files)\n")
    
    print(f"Report saved to: {output_file}")