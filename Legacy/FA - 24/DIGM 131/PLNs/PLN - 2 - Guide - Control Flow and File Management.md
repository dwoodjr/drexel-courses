# Live Coding Session: Control Flow and File Management

## Session Objective
In this session, we'll build on our Python basics by learning about control flow and file management. ***We'll create a script that can batch rename files,*** which is a common task in game development and digital content creation pipelines.

## Setup (10 minutes)
- Open your preferred Python IDE and create a new Python file named `batch_rename.py`
- Create a test folder on your computer with some sample files to rename (e.g., text files, images)

> [!note] Why use an IDE?
> An Integrated Development Environment (IDE) is a software application that provides comprehensive facilities for software development. It typically includes features like code editing, debugging, and an integrated terminal, which make coding easier and more efficient.

> [!note] Important Setup Note
> Ensure you have permission to modify files in your test folder. It's best to use a dedicated test folder rather than important project files.

## Key Concepts to Watch For
- Conditional statements (if/else)
- Loops (for loops)
- File I/O operations
- Error handling

## Problem-Solving Exercise: Breaking Down Today's Task

Let's break down the programming task for today's session:

1. What is the main goal of our script/program?
   Main goal: __________________________________________________

2. What are the major tasks we need to accomplish to achieve this goal?
   a) __________________________________________________
   b) __________________________________________________
   c) __________________________________________________

3. Let's break down one of these major tasks into smaller steps. Choose one from above:
   Selected task: __________________________________________________
   Steps to accomplish this task:
   a) __________________________________________________
   b) __________________________________________________
   c) __________________________________________________

4. What Python concepts or tools will we need to use?
   • __________________________________________________
   • __________________________________________________
   • __________________________________________________

🖊️ Reflection: 
How might this task relate to real-world game development or animation workflows?
___________________________________________________________
___________________________________________________________

## Step-by-Step Guide

### 1. Introduction to Conditional Statements (15 minutes)

```python
import os

def is_valid_filename(filename):
    return not filename.startswith('.') and not filename.startswith('_')

test_filename = "example.txt"
if is_valid_filename(test_filename):
    print(f"{test_filename} is a valid filename")
else:
    print(f"{test_filename} is not a valid filename")
```

> [!info] Understanding Conditional Statements
> - `if` statements allow your code to make decisions based on conditions.
> - The condition after `if` is evaluated as True or False.
> - If True, the indented code block under `if` is executed.
> - If False, the code under `else` (if present) is executed.

> [!example] Logical Operators
> Python uses logical operators to combine or modify conditions:
> - `and`: Both conditions must be true
> - `or`: At least one condition must be true
> - `not`: Inverts the condition
>
> Example:
> ```python
> if (age >= 21 and has_id) or is_vip:
>     print("Welcome to the club!")
> else:
>     print("Sorry, you can't enter.")
> ```

🔍 Quick Challenge: Modify the `is_valid_filename` function to also exclude filenames ending with '.tmp'.

### 2. Working with Loops (20 minutes)

```python
def get_files_in_directory(directory):
    files = []
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            files.append(filename)
    return files

directory = os.getcwd()
files = get_files_in_directory(directory)
print("Files in directory:")
for file in files:
    print(file)
```

> [!info] Understanding Loops
> - Loops allow you to repeat actions multiple times.
> - `for` loops iterate over a sequence (like a list or the results of `os.listdir()`).
> - Each iteration assigns the next item in the sequence to the loop variable (e.g., `filename`).

> [!note] Important Functions
> - `os.listdir(directory)`: Returns a list of entries in the given directory.
> - `os.path.isfile(path)`: Returns True if the path is an existing regular file.
> - `os.path.join(directory, filename)`: Joins path components intelligently.

> [!tip] List Comprehension
> The `get_files_in_directory` function can be written more concisely using a list comprehension:
> ```python
> def get_files_in_directory(directory):
>     return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
> ```
> This does the same thing as the loop, but in a more compact form.

🔍 Debugging Exercise: The following code has a bug. Can you find and fix it?
```python
def get_files_in_directory(directory):
    files = []
    for filename in os.listdir(directory):
        if os.path.isfile(filename):
            files.append(filename)
    return files
```

> [!tip] Hint for Debugging
> When working with files, it's important to consider the difference between a filename and a full file path. 
> - `filename` is just the name of the file (e.g., "document.txt")
> - A full file path includes the directory (e.g., "C:/Users/YourName/Documents/document.txt")
> 
> Which one do you think `os.path.isfile()` needs to work correctly?

### 3. File I/O Operations (25 minutes)

```python
def rename_files(directory, prefix):
    for filename in os.listdir(directory):
        if is_valid_filename(filename):
            old_file = os.path.join(directory, filename)
            new_file = os.path.join(directory, f"{prefix}_{filename}")
            os.rename(old_file, new_file)
            print(f"Renamed: {filename} -> {prefix}_{filename}")

rename_files("C:/Projects/test_files", "game_asset")
```

> [!info] File Operations
> - `os.path.join()`: Creates proper file paths for any operating system.
> - `os.rename(old, new)`: Renames a file or directory.
> - `f"{prefix}_{filename}"`: This is an f-string, allowing us to embed expressions inside string literals.

> [!warning] Error Handling
> File operations can raise errors. It's good practice to use try-except blocks:
> ```python
> try:
>     os.rename(old_file, new_file)
>     print(f"Renamed: {filename} -> {prefix}_{filename}")
> except OSError as e:
>     print(f"Error renaming {filename}: {e}")
> ```
> This prevents the script from crashing if it encounters an error with a single file.

🔍 Live Coding Pause: How might we modify this function to handle errors that could occur during file renaming?

### 4. Putting It All Together (20 minutes)

```python
import os

def is_valid_filename(filename):
    return not filename.startswith('.') and not filename.startswith('_')

def get_files_in_directory(directory):
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

def rename_files(directory, prefix):
    files = get_files_in_directory(directory)
    for filename in files:
        if is_valid_filename(filename):
            old_file = os.path.join(directory, filename)
            new_file = os.path.join(directory, f"{prefix}_{filename}")
            try:
                os.rename(old_file, new_file)
                print(f"Renamed: {filename} -> {prefix}_{filename}")
            except OSError as e:
                print(f"Error renaming {filename}: {e}")

if __name__ == "__main__":
    directory = input("Enter the directory path: ")
    prefix = input("Enter the prefix for renamed files: ")
    rename_files(directory, prefix)
```

> [!info] Script Structure
> - We've organized our code into functions, each with a specific purpose.
> - The `if __name__ == "__main__":` block is where the script starts executing when run directly.
> - We use `input()` to get user input for the directory and prefix.

🔍 Customization Opportunity: How could you modify this script to allow for different renaming patterns (e.g., adding a suffix instead of a prefix)?

## Reflection Questions
1. How might you use conditional statements and loops to automate other aspects of game development or animation workflows?
2. What are some potential issues that could arise when working with file operations, and how can we handle them?
3. How could this file renaming script be extended to support a larger asset management system in a game development project?

> [!tip] Making Your Script Flexible
> Consider how you might extend this script:
> - Add options for different renaming patterns (e.g., suffix, replace text)
> - Include a "dry run" option that shows what would be renamed without actually renaming
> - Add logging to keep track of all changes made

## Notes
[Space for your own notes, questions, and observations]

## Looking Ahead
In our next session, we'll explore:
- More complex data structures like dictionaries
- Advanced file operations and working with different file formats
- Integrating our file management skills with game development tools

> [!summary] What We've Learned
> - Conditional statements for decision-making in code
> - Loops for iterating over collections of items
> - Basic file I/O operations for managing files and directories
> - Error handling to make our scripts more robust