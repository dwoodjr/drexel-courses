# Live Coding Session: Control Flow and File Management

## Session Objective
Introduce control flow concepts (conditional statements and loops) and basic file I/O operations while building a script to batch rename files based on a naming convention.

## Setup (10 minutes)
- Open PyCharm or VS Code and create a new Python file named `batch_rename.py`
- Create a test folder with some sample files to rename

> [!quote] Teaching Script
> Today, we're building on our Python basics by learning about control flow and file management. We'll create a script that can batch rename files, which is a common task in development and digital content creation pipelines.

Let's break down the programming task for today's session:

1. What is the main goal of our script/program?
   Main goal: Create a script that can batch rename files in a directory based on a given prefix

2. What are the major tasks we need to accomplish to achieve this goal?
   a) Get a list of files from a specified directory
   b) Filter out files we don't want to rename
   c) Rename each valid file by adding a prefix to its name

3. Let's break down one of these major tasks into smaller steps. Choose one from above:
   Selected task: Rename each valid file by adding a prefix to its name

   Steps to accomplish this task:
   a) Create a new filename by combining the prefix and the original filename
   b) Construct the full file paths for both the old and new filenames
   c) Use a file renaming function to change the filename

4. What Python concepts or tools will we need to use?
   • Conditional statements (if/else) for filtering files
   • Loops (for loop) to iterate through the list of files
   • File I/O operations (os module) for working with directories and files
   • String manipulation for creating new filenames
   • Functions to organize our code into reusable blocks

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
> [!quote] Teaching Script
> • Conditional statements allow us to make decisions in our code
> • The `if` statement checks a condition and executes code if it's true
> • The `else` statement provides an alternative if the condition is false
> • We can use functions to encapsulate logic, like our `is_valid_filename` function

> [!question] Q for class
> What would happen if we changed the test_filename to "_hidden.txt"?

> [!answer] Answer
> If we changed the test_filename to "_hidden.txt", the output would be "_hidden.txt is not a valid filename" because our is_valid_filename function returns False for filenames starting with an underscore.

> [!example] Logical Operators: Combining Conditions
> In Python, we can use logical operators to combine multiple conditions:
> 
> 1. `and`: Both conditions must be true
> 2. `or`: At least one condition must be true
> 3. `not`: Inverts the condition
> 
> Example:
> ```python
> if (age >= 18 and has_id) or is_vip:
>     print("Welcome to the club!")
> else:
>     print("Sorry, you can't enter.")
> ```
> 
> This checks if a person is both of legal age and has ID, or if they're a VIP.

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
> [!quote] Teaching Script
> • Loops allow us to repeat actions multiple times
> • The `for` loop is used to iterate over a sequence (like a list)
> • We use `os.listdir()` to get all items in a directory
> • `os.path.isfile()` checks if an item is a file (not a directory)
> • We're building a list of files, which we'll use later for renaming

> [!question] Q for class
> How would you modify this function to include subdirectories as well?

> [!answer] Answer
> [To include subdirectories](https://docs.python.org/3/library/os.html), we could use `os.walk()` instead of `os.listdir()`. Here's a modified version:
> ```python
> def get_files_in_directory(directory):
>     files = []
>     for root, dirs, filenames in os.walk(directory):
>         for filename in filenames:
>             files.append(os.path.join(root, filename))
>     return files
> ```
> This will recursively search through all subdirectories and return the full paths of all files.

>[!quote] Teaching Script 
>- The `os.walk()` function is used to traverse the directory tree 
>- It yields a 3-tuple: (dirpath, dirnames, filenames) for each directory it visits 
>- We use a nested loop to iterate over all filenames in each directory
>- `os.path.join()` is used to create the full path for each file 
>- This function will return all files in the given directory and its subdirectories

> [!question] Q for class 
> How would you modify this function to exclude certain file types, like temporary files ending with '.tmp'?

> [!answer] Answer To exclude certain file types, we can add a condition in the inner loop. Here's an example:
> 
> ``` python
> 	def get_files_in_directory(directory, exclude_extensions=['.tmp']):
> 		files = [] 
> 		for root, dirs, filenames in os.walk(directory):
> 			for filename in filenames: 
> 					if not any(filename.endswith(ext) for ext in exclude_extensions):
> 						files.append(os.path.join(root, filename))
> 		return files
> ```
> This modified function takes an optional parameter `exclude_extensions` which is a list of file extensions to exclude. It uses a list comprehension with the `any()` function to check if the filename ends with any of the excluded extensions.

> [!activity] Think-Pair-Share (7 minutes)
> With your partner, discuss how you might use a loop to rename all the files in a directory to have a consistent naming convention. For example, adding a prefix to all files or changing their extension. Write a pseudocode outline of how you would approach this task.
> 
> Be prepared to share your ideas with the class.

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
> [!quote] Teaching Script
> • The `os.path.join()` function creates proper file paths for any operating system
> • `os.rename()` is used to rename files
> • We're using our `is_valid_filename` function to skip files we don't want to rename
> • This function demonstrates combining loops, conditionals, and file operations

> [!question] Q for class
> What potential issues might arise if a file with the new name already exists?

> [!answer] Answer
> If a file with the new name already exists, `os.rename()` will raise an OSError. To handle this, we could:
> 1. Use a try-except block to catch the error and skip the file
> 2. Check if the new filename exists before renaming and modify it (e.g., add a number)
> 3. Use `os.replace()` instead, which will overwrite existing files (use with caution!)

> [!example] Error Handling with try-except
> Error handling is crucial when working with files. Here's how we can use try-except:
> 
> ```python
> def rename_files(directory, prefix):
>     for filename in os.listdir(directory):
>         if is_valid_filename(filename):
>             old_file = os.path.join(directory, filename)
>             new_file = os.path.join(directory, f"{prefix}_{filename}")
>             try:
>                 os.rename(old_file, new_file)
>                 print(f"Renamed: {filename} -> {prefix}_{filename}")
>             except OSError as e:
>                 print(f"Error renaming {filename}: {e}")
> ```
> 
> This way, if an error occurs during renaming, the script will continue with the next file instead of crashing.

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
> [!quote] Teaching Script
> • We've combined all our functions into a complete script
> • The script now takes user input for the directory and prefix
> • We're using the `if __name__ == "__main__":` idiom to make our script both importable and executable
> • This script demonstrates control flow, file I/O, and error handling in a real-world scenario

> [!question] Q for class
> How might we extend this script to handle different renaming patterns, not just adding a prefix?

> [!answer] Answer
> To handle different renaming patterns, we could:
> 1. Create a function that generates new filenames based on various patterns
> 2. Use command-line arguments to specify the renaming pattern
> 3. Implement different renaming strategies (e.g., prefix, suffix, replace, regex) and let the user choose

> [!activity] Think-Pair-Share (10 minutes)
> With your partner, brainstorm how you could modify this script to work with a specific development workflow. For example, how might you use it to organize textures or 3D models? What naming conventions would be useful?
> 
> Be prepared to share your ideas and explain how you would implement them using the concepts we've learned today.

### 5. Wrap-up and Next Steps (10 minutes)

> [!summary] Recap
> Today we covered several key concepts:
> - Conditional statements for decision-making in code
> - Loops for iterating over collections of items
> - Basic file I/O operations for managing files and directories
> - Error handling to make our scripts more robust

> [!info] Looking Ahead
> In future lessons, we'll expand on these concepts by:
> - Exploring more complex data structures like dictionaries
> - Learning about list comprehensions for more concise code
> - Introducing regular expressions for advanced pattern matching
> - Diving deeper into file operations and working with different file formats

> [!task] Assignment Introduction
> Your upcoming assignment will build directly on what we've learned today:
> - You'll create a more advanced version of our file management script
> - The script will organize files in a game project directory based on file types
> - You'll implement error handling and logging to make the script production-ready
> - Bonus challenges will include handling nested directories and custom naming conventions
> 
> This assignment will give you hands-on experience applying control flow and file management concepts to a real-world game development scenario.

> [!question] Final Reflection
> Take a moment to consider:
> - How might these file management scripts be useful in your game development projects?
> - What other repetitive tasks in your workflow could be automated using similar scripts?
> 
> Feel free to share your thoughts or ask any final questions before we wrap up.

> [!danger] BREAK (15 Minutes)
> Let's take a short break before we begin the lab portion of our class.