 # Week 1 Recap: Python Basics and Project Structure Automation

## 1. Introduction to Technical Art and Scripting

Technical art bridges the gap between art and programming in game development and digital content creation. As tech artists, we use scripting to automate repetitive tasks, improve workflows, and create tools that help both artists and developers work more efficiently.

## 2. Python Fundamentals

### 2.1 Variables and Data Types
- **Variables**: Containers for storing data
- **Basic Data Types**:
  - Strings: Text (e.g., `"Hello, World!"`)
  - Integers: Whole numbers (e.g., `42`)
  - Floats: Decimal numbers (e.g., `3.14`)
  - Booleans: True/False values

Example:
```python
project_name = "SuperAwesomeGame"  # String
version_number = 1  # Integer
is_multiplayer = True  # Boolean
```

### 2.2 Lists
- Ordered collections of items
- Can contain mixed data types
- Zero-indexed (first item is at index 0)

Example:
```python
folders = ["Assets", "Scripts", "Levels", "Documentation"]
print(folders[0])  # Outputs: Assets
folders.append("Builds")  # Adds "Builds" to the end of the list
```

### 2.3 String Formatting
- F-strings: Allow embedding variables directly in strings

Example:
```python
print(f"Creating project: {project_name}")
```

## 3. Control Flow

### 3.1 For Loops
- Used to iterate over sequences (like lists)

Example:
```python
for folder in folders:
    print(f"Creating folder: {folder}")
```

## 4. Functions
- Reusable blocks of code
- Help organize and modularize your scripts

Example:
```python
def create_project_structure(name, base_path="C:/Projects"):
    # Function body here
```

## 5. Modules and Importing
- Modules are like toolkits with pre-written code
- We use the `import` keyword to use modules

Example:
```python
import os
```

## 6. File and Directory Operations
- The `os` module provides functions for interacting with the operating system
- Key functions:
  - `os.path.join()`: Creates proper file paths for any OS
  - `os.makedirs()`: Creates directories

Example:
```python
full_path = os.path.join(base_path, project_name, folder)
os.makedirs(full_path, exist_ok=True)
```

## 7. Command-Line Arguments with argparse
- Allows scripts to accept input when run from the command line
- Makes scripts more flexible and user-friendly

Example:
```python
import argparse

parser = argparse.ArgumentParser(description="Create a project folder structure.")
parser.add_argument("project_name", help="Name of the project")
args = parser.parse_args()
```

## 8. Application: Project Structure Automation

We applied these concepts to create a script that automates the creation of a project folder structure:

1. Accept a project name as input
2. Create a main project folder
3. Create subfolders (Assets, Scripts, Levels, etc.)
4. Generate a README file

This script demonstrates how programming can automate repetitive tasks in game development and digital content creation pipelines.

## 9. Best Practices
- Use descriptive variable and function names
- Comment your code to explain complex parts
- Use functions to organize and reuse code
- Handle potential errors (like existing directories)
