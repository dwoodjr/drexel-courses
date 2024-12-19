# Live Coding Session - Week 1: Python Basics + Project Structure Automation

## Session Objective
Introduce basic Python concepts while building a simple script to create a project folder structure.

## Setup (10 minutes)
- Open PyCharm and create a new Python project
- Create a new Python file named `project_structure.py`

> [!note] Project Structure
> We keep our project files separate from the virtual environment (.venv folder). This separation is a best practice in Python development.

  ``` txt
  YourProjectName/
  ├── .venv/  (or venv/)
  │   ├── Lib/
  │   ├── Scripts/
  │   ├── Include/
  │   └── .gitignore
  └── project_structure.py  (we'll create this)
  ```
## Key Concepts to Watch For
- Variables and data types
- Lists and list operations
- For loops
- String formatting (f-strings)
- Basic module usage (os module)
- Functions

## Step-by-Step Guide

### 1. Hello, Python! (5 minutes)

```python
# Your task: Print a welcome message
print("___________________")
```

> [!example] Functions in Programming
> Functions are reusable blocks of code that perform a specific task. They help organize code and make it more modular. Learn more: https://www.geeksforgeeks.org/functions-programming/

🔍 Quick Challenge: Print your name and favorite game

## Problem-Solving Exercise: Breaking Down Our Project Automation Script

> [!example] Thinking in Steps: Breaking Down Problems
> When approaching a programming task, it's helpful to break it down into smaller steps. This is an example of [Design Thinking](https://www.interaction-design.org/literature/topics/design-thinking), an iterative process for problem-solving.
> 
> We'll use these steps to break down our project automation script:
> 1. Identify the main goal of the script
> 2. List the major tasks needed to achieve that goal
> 3. Break each major task into smaller, manageable steps
> 4. Determine what concepts or tools we'll need for each step

### Breaking Down Our Project Automation Script

Let's break down our project automation script together.
Fill in the blanks:

1. What is the main goal of our project automation script?
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

4. What Python concepts or tools will we need to use in our script?
   • __________________________________________________
   • __________________________________________________
   • __________________________________________________

🔍 Quick Discussion: 
Turn to a neighbor and compare your answers. Did you identify similar tasks and steps, or did you approach the problem differently?

🖊️ Reflection: 
How do you think breaking down the problem like this will help us as we start coding our script?
___________________________________________________________
___________________________________________________________

> [!tip] Remember
> We'll refer back to this breakdown as we code our script. It will help us stay organized and focused on our goal!

### 2. Variables and Strings (10 minutes)

```python
project_name = "___________________"
print("We are setting up the project:", project_name)

# Your task: Create an f-string for the project path
project_path = f"___________________"
print("Project path:", project_path)
```

> [!example] Naming Conventions in Python
> [Python naming conventions](https://www.geeksforgeeks.org/python-naming-conventions/) help make code more readable. For example, use snake_case for variable names: `player_score = 100`

🔍 Quick Challenge: Create a variable for the game's version and include it in the project_path

### 3. Lists (15 minutes)

```python
folders = ["Assets", "Scripts", "Levels", "Documentation"]
# Your task: Add "Builds" to the folders list
___________________

# Your task: Print the first and last folder
print("First folder:", __________________)
print("Last folder:", __________________)

# Looping through a list
for folder in folders:
    print("Creating folder:", folder)
```

> [!example] Python Lists
> [Lists](https://www.geeksforgeeks.org/python-lists/) are versatile data structures in Python that can hold multiple items of different types.

🔍 Quick Challenge: Add two more relevant folders and print the updated list

### 4. Basic String Operations (10 minutes)

```python
# Your task: Create full paths for each folder using f-strings
for folder in folders:
    full_path = f"___________________"
    print("Full path:", full_path)
```

🔍 Debugging Exercise: Find and fix the bug in this code:
```python
for folder in folders
    print(Creating folder: folder)
```

### 5. Introducing the `os` Module (15 minutes)

```python
import os

# Your task: Use os.path.join to create the full path
for folder in folders:
    full_path = os.path.join("___________________")
    print("Full path:", full_path)
```

> [!example] Python Modules
> [Modules](https://www.geeksforgeeks.org/python-modules/) are like toolkits in Python, containing helpful functions we can use in our scripts.

🔍 Live Coding Pause: Let's discuss why we use os.path.join instead of string concatenation

### 6. Putting It All Together (15 minutes)

```python
# Your task: Complete the function definition
def create_project_structure(___________):
    # Add your code here
    pass

# Your task: Call the function with a project name
create_project_structure("___________________")
```

> [!example] Pseudocode in Programming
> [Pseudocode](https://www.geeksforgeeks.org/how-to-write-a-pseudo-code/) helps plan your code logic before actual coding. Try writing pseudocode for the create_project_structure function!

🔍 Customization Opportunity: Modify the function to create a folder structure for your dream game project

## Reflection Questions
1. How might you modify the `create_project_structure` function to allow for custom base paths?
2. What other folders might be useful in a game development project structure?
3. How could you use conditional statements to create different folder structures for different types of projects?

## Notes
[Use this space for your own notes, questions, and observations during the session]

## Looking Ahead
In our next session, we'll explore control flow and file management concepts.