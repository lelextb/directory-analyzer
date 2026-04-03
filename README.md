Understood. Here's a clean, badge‑free README.md that doesn't rely on external image links – all text and emoji, fully self‑contained and copy‑ready.


# 📁 Directory File Analyzer

**Python 3.6+** | **MIT License** | **Zero Dependencies**

> Recursively scan any directory and get instant insights: file count, total size, largest/smallest files, top file extensions – all with a clean, modular Python script.

---

## 🚀 Features

- ✅ **Recursive scanning** – crawls through all subdirectories  
- ✅ **Human-readable sizes** – auto‑converts B → KB → MB → GB  
- ✅ **Instant insights** – largest file, smallest file, top 3 extensions  
- ✅ **Optional report export** – saves analysis to a `.txt` file  
- ✅ **Zero external dependencies** – uses only Python standard library  
- ✅ **Modular architecture** – easy to extend or reuse components  

---

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/lelextb/directory-analyzer.git
cd directory-analyzer

# No pip install – pure Python
```

---

## 🖥️ Usage

**Interactive mode** – you type the directory path when prompted:

```bash
python main.py
```

**Direct mode** – pass the directory as a command‑line argument:

```bash
python main.py /path/to/your/folder
```

---

## 📊 Example Output

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

---

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
└── requirements.txt      # (empty – no dependencies)
```

---

## 🛠️ Extending the Tool

The modular design makes it easy to add features:

- **Filter by file type** – modify `scanner.py` to ignore certain extensions  
- **Export to CSV** – add a `save_csv()` function in `reporter.py`  
- **Add a progress bar** – integrate `tqdm` (optional) in `scanner.py`  

---

## 📄 License

**MIT** – free to use, modify, and distribute.

---

## 🤝 Contributing

Issues and pull requests are welcome!  
For major changes, please open an issue first to discuss.

---

**Made with ❤️ for developers who love clean data.**  
*Enjoy analyzing your directories!*
