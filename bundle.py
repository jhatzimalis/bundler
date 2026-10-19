import os
import tkinter as tk
from tkinter import filedialog


def generate_directory_tree(startpath, prefix=""):
  """Recursively generates a clean ASCII tree structure of folders and files."""
  tree_lines = []
  try:
    # Get sorted items (directories first, then files)
    items = sorted(os.listdir(startpath))
  except PermissionError:
    return []

  # Filter out unwanted system/cache directories and files
  ignored = {
      ".git",
      "__pycache__",
      "node_modules",
      "venv",
      ".venv",
      "project_bundle.txt",
  }
  items = [item for item in items if item not in ignored]

  for index, item in enumerate(items):
    path = os.path.join(startpath, item)
    is_last = index == len(items) - 1

    connector = "└── " if is_last else "├── "
    tree_lines.append(f"{prefix}{connector}{item}")

    if os.path.isdir(path):
      extension = "    " if is_last else "│   "
      tree_lines.extend(generate_directory_tree(path, prefix + extension))

  return tree_lines


def bundle_project():
  root = tk.Tk()
  root.withdraw()

  print("Please select your project folder in the pop-up window...")
  project_dir = filedialog.askdirectory(title="Select Project Folder")

  if not project_dir:
    print("No folder selected. Exiting.")
    return

  output_filename = "project_bundle.txt"
  output_path = os.path.join(os.path.dirname(project_dir), output_filename)

  ignored_extensions = {
      ".png",
      ".jpg",
      ".jpeg",
      ".gif",
      ".ico",
      ".pdf",
      ".zip",
      ".tar",
      ".gz",
      ".exe",
      ".dll",
      ".pyc",
  }

  print(f"Scanning folder: {project_dir}")

  # Build the proper tree structure text
  root_name = os.path.basename(os.path.abspath(project_dir))
  tree_lines = [f"{root_name}/"] + generate_directory_tree(project_dir)
  folder_tree_str = "\n".join(tree_lines)

  # Write to output file
  with open(output_path, "w", encoding="utf-8") as outfile:
    # 1. Write the Folder Tree Section
    outfile.write("=" * 50 + "\n")
    outfile.write("PROJECT FOLDER STRUCTURE\n")
    outfile.write("=" * 50 + "\n\n")
    outfile.write(folder_tree_str)
    outfile.write("\n\n" + "=" * 50 + "\n")
    outfile.write("FILE CONTENTS\n")
    outfile.write("=" * 50 + "\n\n")

    # 2. Walk through and write file contents
    for root, dirs, files in os.walk(project_dir):
      dirs[:] = [
          d
          for d in dirs
          if d not in {".git", "__pycache__", "node_modules", "venv", ".venv"}
      ]

      for file in files:
        file_path = os.path.join(root, file)
        _, ext = os.path.splitext(file)

        if ext.lower() in ignored_extensions or file == output_filename:
          continue

        rel_path = os.path.relpath(file_path, project_dir)

        outfile.write(f"\n{'='*40}\n")
        outfile.write(f"FILE: {rel_path}\n")
        outfile.write(f"{'='*40}\n\n")

        try:
          with open(file_path, "r", encoding="utf-8", errors="ignore") as infile:
            outfile.write(infile.read())
        except Exception as e:
          outfile.write(f"[Error reading file: {e}]\n")

        outfile.write("\n\n")

  print(f"\nSuccess! Fixed bundle has been saved to:\n{output_path}")


if __name__ == "__main__":
  bundle_project()