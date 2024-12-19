# Week 2 Recap: Control Flow and File Management

## 1. Introduction to Control Flow and File Management
Control flow structures allow us to make decisions and repeat actions in our code. File management is crucial for organizing and manipulating data in game development and digital content creation pipelines. These concepts enable us to create more dynamic and powerful scripts.

## 2. Control Flow Structures

### 2.1 Conditional Statements
- **if, elif, else**: Used for decision-making in code
Example:
```python
def is_valid_filename(filename):
    return not filename.startswith('.') and not filename.startswith('_')

if is_valid_filename("example.txt"):
    print("Valid filename")
else:
    print("Invalid filename")
```

### 2.2 Loops
- **for loops**: Used to iterate over sequences (like lists or file names)
Example:
```python
for filename in os.listdir(directory):
    if os.path.isfile(os.path.join(directory, filename)):
        print(f"Found file: {filename}")
```

## 3. File and Directory Operations

### 3.1 Working with Paths
- **os.path.join()**: Creates proper file paths for any operating system
Example:
```python
full_path = os.path.join(directory, filename)
```

### 3.2 File Operations
- **os.rename()**: Renames files
- **os.listdir()**: Lists contents of a directory
Example:
```python
os.rename(old_file, new_file)
files = os.listdir(directory)
```

### 3.3 Directory Operations
- **os.makedirs()**: Creates directories (including nested ones)
Example:
```python
os.makedirs(full_path, exist_ok=True)
```

## 4. Error Handling
- **try-except blocks**: Used to handle potential errors gracefully
Example:
```python
try:
    os.rename(old_file, new_file)
except OSError as e:
    print(f"Error renaming file: {e}")
```

## 5. Functions for File Management
- Encapsulate file operations in reusable functions
Example:
```python
def rename_files(directory, prefix):
    for filename in os.listdir(directory):
        if is_valid_filename(filename):
            old_file = os.path.join(directory, filename)
            new_file = os.path.join(directory, f"{prefix}_{filename}")
            try:
                os.rename(old_file, new_file)
                print(f"Renamed: {filename} -> {prefix}_{filename}")
            except OSError as e:
                print(f"Error renaming {filename}: {e}")
```

## 6. Application: File Sorting and Organization
We applied these concepts to create scripts that:
1. Batch rename files based on a naming convention
2. Sort files into subdirectories based on their types
3. Organize project files into a structured hierarchy

These scripts demonstrate how we can use Python to automate file management tasks in game development and digital content creation pipelines.

## 7. Best Practices
- Use descriptive function and variable names
- Handle potential errors with try-except blocks
- Create modular, reusable functions for common operations
- Use comments to explain complex logic or important decisions in your code
