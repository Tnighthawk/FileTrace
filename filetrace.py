import os
import sys

def build_tree(root_dir):
    """
    Walks the directory and builds a list of (path, is_last) entries.
    """
    tree = []
    root_dir = os.path.abspath(root_dir)
    
    for current_root, dirs, files in os.walk(root_dir):
        # Sort for consistent output
        dirs.sort()
        files.sort()
        
        depth = current_root.replace(root_dir, '').count(os.sep)
        indent = ""
        if depth > 0:
            indent = "    " * (depth - 1) + "│   "
        
        dir_name = os.path.basename(current_root) or os.path.basename(root_dir)
        tree.append((indent, dir_name, True))  # Directory entry (is_last = True for now)
        
        # Add files and subdirs
        entries = dirs + files
        for i, entry in enumerate(entries):
            is_last = (i == len(entries) - 1)
            connector = "└── " if is_last else "├── "
            prefix = indent + ("    " if depth == 0 else "│   ") if not is_last else indent + "    "
            tree.append((prefix + connector, entry, is_last))
    
    return tree, root_dir

def print_directory_structure(start_path):
    """
    Prints a visually structured directory tree.
    """
    if not os.path.isdir(start_path):
        print(f"Error: The provided path is not a valid directory: {start_path}")
        return
    
    tree, abs_root = build_tree(start_path)
    
    print(f"\nDirectory Structure of: {abs_root}\n")
    
    for i, (prefix, name, is_last) in enumerate(tree):
        if i == 0:
            # Root directory
            print(f"{name}/")
            continue
        
        # Determine symbol based on type
        if name in [d for d in os.listdir(abs_root) if os.path.isdir(os.path.join(abs_root, name))]:
            suffix = "/"
        else:
            suffix = ""
        
        print(f"{prefix}{name}{suffix}")

def resolve_input_path(user_input):
    """
    Resolves user input to a valid absolute directory path.
    Handles quotes, relative paths, and sibling directories.
    """
    path = user_input.strip().strip('"\'')
    
    if not path:
        return None
    
    # Case 1: Absolute path
    if os.path.isabs(path):
        return path if os.path.isdir(path) else None
    
    # Case 2: Relative to current directory
    candidate1 = os.path.abspath(path)
    if os.path.isdir(candidate1):
        return candidate1
    
    # Case 3: Relative to parent (sibling project)
    candidate2 = os.path.abspath(os.path.join('..', path))
    if os.path.isdir(candidate2):
        return candidate2
    
    return None

def main():
    print("Directory Tree Visualizer\n")
    raw_input = input("Please enter the starting directory path: ").strip()
    
    resolved = resolve_input_path(raw_input)
    
    if not resolved:
        print("Error: Could not resolve a valid directory from the input.")
        print("   Try using absolute path or relative path like '../my_super_cool_project'")
        sys.exit(1)
    
    if resolved != os.path.abspath(raw_input.strip('"\'')):
        print(f"Resolved path: {resolved}")
    
    print_directory_structure(resolved)

if __name__ == "__main__":
    main()