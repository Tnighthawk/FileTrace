# FileTrace

A lightweight, user-friendly Python tool that generates a **clean, visually structured directory tree** using ASCII art. Perfect for project documentation, debugging, or sharing file structures in terminals.

---

## Features

- **Visual tree output** with `├──`, `└──`, and `│` connectors  
- **Smart path resolution**:  
  - Strips surrounding quotes  
  - Resolves relative paths (current or parent directory)  
  - Handles sibling project folders (e.g., `../my_super_cool_project`)  
- **Sorted directories and files** for consistent output  
- **Copy-paste-ready** terminal output  
- **No external dependencies**

---

## Quick Start

1. **Save the script** as `super_cool_tool.py`
2. **Run in terminal**:
   ```bash
   python super_cool_tool.py
