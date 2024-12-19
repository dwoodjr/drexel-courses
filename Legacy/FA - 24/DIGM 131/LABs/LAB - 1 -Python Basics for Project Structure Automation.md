# Interactive Lab: Extending Project Structure Automation

## 🎯 Objective
Build upon the basic project structure automation script by adding command-line argument parsing, making the tool more flexible and user-friendly.

## 📚 Pre-lab Reading
- [Argparse Tutorial](https://docs.python.org/3/howto/argparse.html) (15 minutes)
- [Video Tutorial - Argparse](https://www.youtube.com/watch?v=aGy7U5ItLRk) (19 minutes)

> [!note] For Beginners
> Don't worry if you don't understand everything in the pre-lab reading. We'll go through the concepts step-by-step in this lab.

## Starting Point: Live Coding Session Script

Here's the complete script from the live coding session. Copy this into a new file named `project_structure.py` in your PyCharm project:

```python
import os

# Be sure to change the base_path value to something that makes more sense for your project,
# like the python project root directory
def create_project_structure(project_name, base_path="C:/Projects"):
    project_path = os.path.join(base_path, project_name)
    folders = ["Assets", "Scripts", "Levels", "Documentation", "Builds"]
    
    print(f"Creating project structure for: {project_name}")
    for folder in folders:
        full_path = os.path.join(project_path, folder)
        print(f"Creating folder: {full_path}")
        os.makedirs(full_path, exist_ok=True)

# Example usage
create_project_structure("MyAwesomeGame")
```

> [!tip] Copying Code
> You can copy and paste this code directly into your PyCharm editor. Make sure to save the file after pasting. This goes for any code in this document as you work through it.

## 🧪 Lab Steps

### Step 1: Review and Setup (10 minutes)

1. Open PyCharm and create a new Python file named `project_structure.py`.
2. Copy the starting point script into this file.
3. Read through each line of the code and try to understand what it does.
4. Run the script by clicking the green "Run" arrow in PyCharm or by right-clicking in the editor and selecting "Run 'project_structure'".

> [!note] Understanding the Code
> The `create_project_structure` function creates folders for a game project. It uses `os.path.join` to create proper file paths and `os.makedirs` to create the folders.

### Step 2: Introduction to argparse (20 minutes)

Now, let's modify our script to accept command-line arguments using `argparse`.

1. At the top of your script, add the import for argparse:

```python
import os
import argparse
```

2. After the `create_project_structure` function, add the following code:

```python
parser = argparse.ArgumentParser(description="Create a project folder structure.")
parser.add_argument("project_name", help="Name of the project")
parser.add_argument("--base-path", default="C:/Projects", help="Base path for the project")

args = parser.parse_args()

create_project_structure(args.project_name, args.base_path)
```

3. Remove the example usage line `create_project_structure("MyAwesomeGame")`.

> [!note] What's happening here?
> - We're creating an `ArgumentParser` object to handle command-line arguments.
> - We add two arguments: `project_name` (required) and `--base-path` (optional).
> - `parser.parse_args()` processes the command-line arguments.
> - We call our function with the parsed arguments.

Your complete script should now look like this:

```python
import os
import argparse

def create_project_structure(project_name, base_path="C:/Projects"):
    project_path = os.path.join(base_path, project_name)
    folders = ["Assets", "Scripts", "Levels", "Documentation", "Builds"]
    
    print(f"Creating project structure for: {project_name}")
    for folder in folders:
        full_path = os.path.join(project_path, folder)
        print(f"Creating folder: {full_path}")
        os.makedirs(full_path, exist_ok=True)

parser = argparse.ArgumentParser(description="Create a project folder structure.")
parser.add_argument("project_name", help="Name of the project")
parser.add_argument("--base-path", default="C:/Projects", help="Base path for the project")

args = parser.parse_args()

create_project_structure(args.project_name, args.base_path)
```

### Step 3: Testing Your Script (15 minutes)

Now that we've added command-line argument support, we need to test our script differently.

1. In PyCharm, locate the `Terminal` tab at the bottom of the window.
   - If you don't see it, go to View > Tool Windows > Terminal.

2. In the terminal, navigate to your project directory if you're not already there.

3. Run your script with different arguments:

```
python project_structure.py MyGame
python project_structure.py "Awesome Adventure" --base-path C:\GameProjects
```

4. Check your file system to see if the folders were created as expected.

> [!note] Understanding the Commands
> - `python project_structure.py MyGame` creates a project named "MyGame" in the default location.
> - `python project_structure.py "Awesome Adventure" --base-path C:\GameProjects` creates a project with spaces in its name in a custom location.

### Step 4: Adding Flexibility (20 minutes)

Let's add an option to specify custom folders.

1. Add a new argument for folders:

```python
parser.add_argument("--folders", nargs="*", default=["Assets", "Scripts", "Levels", "Documentation", "Builds"], 
                    help="List of folders to create")
```

2. Update the `create_project_structure` function to use this argument:

```python
def create_project_structure(project_name, base_path, folders):
    project_path = os.path.join(base_path, project_name)
    
    print(f"Creating project structure for: {project_name}")
    for folder in folders:
        full_path = os.path.join(project_path, folder)
        print(f"Creating folder: {full_path}")
        os.makedirs(full_path, exist_ok=True)
```

3. Update the function call:

```python
create_project_structure(args.project_name, args.base_path, args.folders)
```

Your final script should look like this:

```python
import os
import argparse

def create_project_structure(project_name, base_path, folders):
    project_path = os.path.join(base_path, project_name)
    
    print(f"Creating project structure for: {project_name}")
    for folder in folders:
        full_path = os.path.join(project_path, folder)
        print(f"Creating folder: {full_path}")
        os.makedirs(full_path, exist_ok=True)

parser = argparse.ArgumentParser(description="Create a project folder structure.")
parser.add_argument("project_name", help="Name of the project")
parser.add_argument("--base-path", default="C:/Projects", help="Base path for the project")
parser.add_argument("--folders", nargs="*", default=["Assets", "Scripts", "Levels", "Documentation", "Builds"], 
                    help="List of folders to create")

args = parser.parse_args()

create_project_structure(args.project_name, args.base_path, args.folders)
```

Test your script with custom folders:

```
python project_structure.py RPGQuest --folders Characters Items Quests
```

> [!note] What's new?
> - `nargs="*"` in the argument definition allows the user to specify any number of folders.
> - The script now creates only the folders specified by the user, or the default ones if not specified.

## 🧠 Knowledge Check Quiz
1. What is the purpose of the `argparse` module?
2. How do you add a required argument in argparse?
3. What's the difference between a positional argument and an optional argument in argparse?

## 🤔 Final Reflection
Think about how you could use command-line arguments in other scripts you might create for game development or digital content creation. What kind of options would be useful?