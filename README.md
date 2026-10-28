# File-searching-tool

# CLI File Searcher 🔍

A lightweight, bulletproof Command Line Interface (CLI) file search engine written in Python. It recursively scans the file system from the root directory (`/`) to find specific files by their exact names.

## 🚀 Features

- **Recursive Deep Search:** Scans the entire directory tree starting from the root.
- **Fail-Safe & Bulletproof:** Safely handles restricted system folders (`PermissionError`) and virtual filesystems like Linux `/sys/` or `/proc` without crashing.
- **Symlink Protection:** Prevents infinite loops by ignoring symbolic links during recursive directory traversal.
- **Infinite Loop CLI:** Keeps running in the terminal, allowing you to perform multiple searches in a row.

## 🛠️ How It Works

The script utilizes Python's built-in `os.scandir()`, which provides significantly faster directory traversal compared to traditional `os.walk()`. 

It uses an optimized exception-handling pattern to bypass:
1. `OSError: [Errno 40] Too many levels of symbolic links`
2. `OSError: [Errno 5] Input/output error` (commonly found in Linux dynamic driver folders)

## 📋 Requirements

- **Python 3.x** (No external dependencies required!)
- Works on **Linux**, **macOS**, and **Windows**.

## 💻 Usage

1. Clone this repository:
   ```bash
   git clone https://github.com
   cd file-searcher
   ```

2. Run the script:
   ```bash
   python main.py
   ```

3. Enter the exact filename you are looking for

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).
