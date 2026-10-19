# 📂 Project Bundler

A lightweight, handy Python utility script that scans any project directory, generates a clean ASCII tree structure, and compiles the contents of all your source code and text files into a single consolidated text file (`project_bundle.txt`). 

It is ideal for preparing codebases to share with AI assistants (like ChatGPT or Claude), archiving small projects, or performing quick codebase code reviews.

---

## ✨ Features

- **Interactive GUI Selection:** Uses Python's built-in `tkinter` to open a native folder selection dialog.
- **ASCII Directory Tree:** Automatically generates and prepends a clean, visual folder structure map to the output file.
- **Smart Filtering:** Automatically ignores common system and dependency directories (such as `.git`, `__pycache__`, `node_modules`, `venv`, and `.venv`).
- **Binary/Media File Exclusion:** Automatically skips images, archives, executables, compiled bytecode, and other non-text formats (e.g., `.png`, `.jpg`, `.zip`, `.exe`, `.pyc`).
- **Robust Error Handling:** Safely handles file permission errors and encoding issues without crashing the script.

---

## 🚀 Requirements

- **Python 3.x**
- **Tkinter** (usually included by default with standard Python installations on Windows and macOS).

---

## 📥 Installation

1. Clone or download this repository to your local machine:
   ```bash
   git clone [https://github.com/jhatzimalis/bundler.git](https://github.com/jhatzimalis/bundler.git)
   cd your-repo-name
    ```

2. Ensure you have Python installed. You can verify your installation with:
    ```bash
    python --version
    ```

---

## 💡 Usage

Run the script from your terminal or command prompt:

```bash
python bundle_script.py

```

1. A graphical dialog window will pop up prompting you to **Select Project Folder**.
2. Choose the root directory of the project you wish to bundle.
3. The script will scan the folder, filter out ignored files/directories, and generate `project_bundle.txt` directly **outside** of the selected project directory (in its parent folder).

---

## ⚙️ Customization

You can easily customize the behavior of the script by editing the sets inside `bundle_script.py`:

* **Ignored Directories & Files:** Edit the `ignored` set in `generate_directory_tree()` and `bundle_project()` to exclude custom directories or files (e.g., build folders, log files).
* **Ignored File Extensions:** Modify the `ignored_extensions` set to skip additional binary or large data file formats.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check out the [issues page](https://www.google.com/search?q=https://github.com/jhatzimalis/bundler/issues).

---

## 📝 License

This project is open-source and available under the [MIT License](https://www.google.com/search?q=LICENSE).
