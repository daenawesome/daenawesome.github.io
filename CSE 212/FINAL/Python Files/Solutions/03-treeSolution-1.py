############
# Solution #
############

"""
You are a system administrator responsible for managing a large network of servers used by your organization. 
Over time, the data stored on these servers has grown significantly, and it has become essential to optimize 
storage usage and identify potential issues. To achieve this, you decide to develop a directory analysis tool 
that provides valuable insights into the data distribution, identifies duplicate files, and calculates the total 
storage size across the network.
"""

import os

class TreeNode:
    def __init__(self, name, absolute_path, size):
        """
        Initializes a TreeNode object with a name, absolute path, and size.
        """
        self.name = name
        self.absolute_path = absolute_path
        self.size = size
        self.children = []

    def update_size(self, size):
        """
        Updates the size of the current TreeNode by adding the specified size.
        """
        self.size += size

def analyze_directory(path, visited_dirs, progress=False):
    """
    Analyzes a directory and constructs a tree structure of its contents using TreeNode objects.
    """
    if not os.path.exists(path) or not os.path.isdir(path):
        return None

    # Create the root TreeNode for the directory
    root = TreeNode(os.path.basename(path), os.path.abspath(path), 0)

    # Stack to keep track of nodes during traversal
    stack = [(root, 0)]

    # Keep track of visited directories to avoid duplicates
    visited_dirs.add(os.path.abspath(path))

    # Count the total number of files in the directory
    total_files = sum(1 for entry in os.listdir(path) if os.path.isfile(os.path.join(path, entry)))

    # Counter for the current file being processed
    current_file = 0

    while stack:
        current_node, level = stack.pop()
        current_path = current_node.absolute_path

        if os.path.isdir(current_path):
            if progress:
                current_file += 1
                print(f"Analyzing... {current_file}/{total_files} files", end="\r")

            dir_size = 0

            try:
                for entry in os.listdir(current_path):
                    child_path = os.path.join(current_path, entry)

                    # Skip special folders or files with restricted access
                    if os.path.islink(child_path):  # Skip symbolic links
                        continue
                    if entry.startswith('.'):  # Skip hidden files and directories
                        continue

                    try:
                        if os.path.isdir(child_path):
                            # Create a new TreeNode for the child directory if it hasn't been visited before
                            if child_path not in visited_dirs:
                                child_node = TreeNode(entry, child_path, 0)
                                current_node.children.append(child_node)
                                stack.append((child_node, level + 1))
                                visited_dirs.add(child_path)
                        elif os.path.isfile(child_path):
                            # Create a new TreeNode for the file and update the directory size
                            child_node = TreeNode(entry, child_path, os.path.getsize(child_path))
                            current_node.children.append(child_node)
                            dir_size += child_node.size
                    except PermissionError:
                        # Skip directories or files for which we don't have sufficient permissions
                        continue

            except PermissionError:
                # Skip directories for which we don't have sufficient permissions
                continue

            # Update the size of the current directory
            current_node.update_size(dir_size)

    if progress:
        print("Analysis Completed.        ")

    return root

def print_tree(node, indent=0):
    """
    Prints the directory tree structure starting from the given node.
    """
    if node is not None:
        print("  " * indent + f"|_ {node.name} (size: {format_size(node.size)})")
        for child in node.children:
            print_tree(child, indent + 1)

def calculate_total_size(node):
    """
    Calculates the total size of a directory and its subdirectories.
    """
    if node is None:
        return 0

    total_size = node.size
    for child in node.children:
        total_size += calculate_total_size(child)

    return total_size

def format_size(size_in_bytes):
    """
    Formats the given size in bytes into a human-readable string.
    """
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size_in_bytes < 1024.0:
            return f"{size_in_bytes:.2f} {unit}"
        size_in_bytes /= 1024.0

def count_directories_and_files(node):
    """
    Counts the number of directories and files in a directory tree.
    """
    if node is None:
        return 0, 0

    num_directories = 1
    num_files = 0
    for child in node.children:
        if os.path.isdir(child.absolute_path):
            child_directories, child_files = count_directories_and_files(child)
            num_directories += child_directories
            num_files += child_files
        elif os.path.isfile(child.absolute_path):
            num_files += 1

    return num_directories, num_files

def calculate_max_depth(node):
    """
    Calculates the maximum depth of a directory tree.
    """
    if node is None:
        return 0

    max_depth = 0
    for child in node.children:
        max_depth = max(max_depth, calculate_max_depth(child))

    return max_depth + 1

def find_duplicate_files(node):
    """
    Finds duplicate files within a directory tree.
    """
    if node is None:
        return {}

    file_dict = {}
    for child in node.children:
        if os.path.isfile(child.absolute_path):
            if child.name in file_dict:
                file_dict[child.name].append(child.absolute_path)
            else:
                file_dict[child.name] = [child.absolute_path]
        elif os.path.isdir(child.absolute_path):
            child_files = find_duplicate_files(child)
            for name, paths in child_files.items():
                if name in file_dict:
                    file_dict[name].extend(paths)
                else:
                    file_dict[name] = paths

    return {name: paths for name, paths in file_dict.items() if len(paths) > 1}

def main(directory_path=None):
    """
    Main entry point of the program.
    """
    if directory_path is None:
        script_directory = os.path.abspath(os.path.dirname(__file__))
    else:
        directory_path = os.path.abspath(directory_path)
        script_directory = directory_path

    # Set to keep track of visited directories
    visited_dirs = set()

    # Analyze the directory and obtain the root of the tree structure
    root = analyze_directory(script_directory, visited_dirs, progress=True)

    if root is not None:
        print("Directory Structure:")
        print_tree(root)

        # Calculate and print total size
        total_size = calculate_total_size(root)
        print()
        print("Total Size:", format_size(total_size))

        # Count and print number of directories and files
        num_directories, num_files = count_directories_and_files(root)
        print("Number of Directories:", num_directories)
        print("Number of Files:", num_files)

        # Calculate and print maximum depth of the directory tree
        max_depth = calculate_max_depth(root)
        print("Maximum Depth of Directory Tree:", max_depth)

        # Find and print duplicate files
        duplicate_files = find_duplicate_files(root)
        if duplicate_files:
            print("\nDuplicate Files:")
            for name, paths in duplicate_files.items():
                print(f"'{name}' found in multiple locations:")
                for path in paths:
                    print(f" - {path}")
        else:
            print("\nNo Duplicate Files Found.")

if __name__ == "__main__":
    main('') # Use & Replace main('/path/to/your/directory') with the desired directory path to analyze
