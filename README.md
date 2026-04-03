```markdown
# 📁 Directory File Analyzer

[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

> Recursively scan any directory and get instant insights: file count, total size, largest/smallest files, top file extensions – all with a clean, modular Python script.

## 🚀 Features

- **Recursive scanning** – crawls through all subdirectories
- **Human-readable sizes** – auto-converts B → KB → MB → GB
- **Instant insights** – shows largest file, smallest file, and top 3 extensions
- **Optional report export** – saves analysis to a `.txt` file
- **Zero dependencies** – uses only Python standard library
- **Modular architecture** – easy to extend or reuse components

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/lelextb/directory-analyzer.git
cd directory-analyzer

# (No pip install needed – pure Python)
```

## 🖥️ Usage

Run from the command line and enter a directory path when prompted:

```bash
python main.py
```

Or pass the directory as an argument:

```bash
python main.py /path/to/your/folder
```

### Example output

```
=== Directory File Analyzer ===

Enter directory path to analyze: ./projects/myapp

Analyzing: /home/user/projects/myapp

==================================================
ANALYSIS REPORT
==================================================

Total files: 127
Total size: 24.32 MB

Largest file: video.mp4 (12.10 MB)
Smallest file: readme.md (128 B)

Top 3 most common extensions:
1. .py (42 files)
2. .txt (31 files)
3. .csv (18 files)

==================================================

Save report to file? (y/n): y
Report saved to: report_myapp.txt
```

## 🗂️ Project Structure

```
directory_analyzer/
├── main.py               # Entry point
├── core/                 # Core logic
│   ├── scanner.py        # Recursive file scanning
│   └── analyzer.py       # Statistics computation
├── utils/                # Helpers
│   └── formatters.py     # Human-readable sizes
├── output/               # Reporting
│   └── reporter.py       # Console & file output
└── requirements.txt      # (empty – no deps)
```

## 🛠️ Extending the Tool

The modular design makes it easy to add features:

- **Add file type filtering** – modify `scanner.py` to ignore certain extensions
- **Add CSV export** – extend `reporter.py` with a `save_csv()` function
- **Add progress bar** – integrate `tqdm` (optional) in `scanner.py`

## 📄 License

MIT – free to use, modify, and distribute.

## 🤝 Contributing

Issues and pull requests are welcome! For major changes, please open an issue first.

---

**Made with ❤️ for developers who love clean data.**  
*Enjoy analyzing your directories!*
