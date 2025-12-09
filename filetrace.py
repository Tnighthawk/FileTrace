import os
import sys

def build_tree(root_dir):
    """
    Builds a properly formatted directory tree structure.
    """
    root_dir = os.path.abspath(root_dir)
    lines = []
    
    def add_tree_lines(directory, prefix=""):
        """Recursively builds tree lines with proper formatting."""
        try:
            entries = os.listdir(directory)
        except PermissionError:
            return
        
        # Separate and sort directories and files
        dirs = sorted([e for e in entries if os.path.isdir(os.path.join(directory, e))])
        files = sorted([e for e in entries if os.path.isfile(os.path.join(directory, e))])
        all_entries = dirs + files
        
        for i, entry in enumerate(all_entries):
            is_last = (i == len(all_entries) - 1)
            connector = "└── " if is_last else "├── "
            
            # Determine if this is a directory
            full_path = os.path.join(directory, entry)
            is_dir = os.path.isdir(full_path)
            suffix = "/" if is_dir else ""
            
            # Add the current entry
            lines.append(f"{prefix}{connector}{entry}{suffix}")
            
            # Recursively process directories
            if is_dir:
                extension = "    " if is_last else "│   "
                add_tree_lines(full_path, prefix + extension)
    
    # Start the recursive tree building
    add_tree_lines(root_dir)
    
    return lines, root_dir

def print_directory_structure(start_path):
    """
    Prints a visually structured directory tree.
    """
    if not os.path.isdir(start_path):
        print(f"Error: The provided path is not a valid directory: {start_path}")
        return
    
    tree_lines, abs_root = build_tree(start_path)
    
    print(f"\nDirectory Structure of: {abs_root}\n")
    
    # Print root directory
    root_name = os.path.basename(abs_root) or abs_root
    print(f"{root_name}/")
    
    # Print tree structure
    for line in tree_lines:
        print(line)

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