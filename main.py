#!/usr/bin/env python3
"""
Directory File Analyzer - Main Entry Point
"""
import sys
from pathlib import Path
from core.scanner import scan_directory
from core.analyzer import analyze_files
from output.reporter import print_report, save_report

def main():
    print("=== Directory File Analyzer ===\n")
    
    # Get directory path from user
    if len(sys.argv) > 1:
        dir_path = sys.argv[1]
    else:
        dir_path = input("Enter directory path to analyze: ").strip()
    
    # Validate path
    path = Path(dir_path)
    if not path.exists():
        print(f"Error: Path '{dir_path}' does not exist.")
        return
    if not path.is_dir():
        print(f"Error: '{dir_path}' is not a directory.")
        return
    
    print(f"\nAnalyzing: {path.absolute()}\n")
    
    # Step 1: Scan all files
    files = scan_directory(path)
    if not files:
        print("No files found in the directory.")
        return
    
    # Step 2: Analyze statistics
    stats = analyze_files(files)
    
    # Step 3: Display report
    print_report(stats)
    
    # Optional: Save to file
    save = input("\nSave report to file? (y/n): ").strip().lower()
    if save == 'y':
        save_report(stats, path.name)

if __name__ == "__main__":
    main()