# Assignment 1: Basic Project Structure Automation 🚀

### Background
As a new tech artist at Awesome Games Studio, you're creating a simple Python script to set up folders for new game projects. This will help the team start new projects more quickly and consistently.

### Your Mission 🎯
Create a Python script that makes folders for a new game project and writes a simple README file inside the project folder.

### Requirements 📋
1. Create a Python script named `create_game_project.py`.
2. Use `argparse` to handle the project name as a command-line argument.
3. Create four folders: "Assets", "Scripts", "Levels", and "Documentation".
4. Create a simple README.md file in the project root.
5. Print messages to show what the script is doing.

### Step-by-Step Guide 📝

1. Open PyCharm and create a new Python file named `create_game_project.py`.

2. Copy this code structure into your file:

```python
import os
import argparse

def create_project_structure(project_name):
    # We'll add code here to create folders and the README file

# We'll add code here to set up argument parsing

# We'll add code here to call the create_project_structure function
```

3. In the `create_project_structure` function, add this code to create the project folder and subfolders:

```python
def create_project_structure(project_name):
    # Create the main project directory
    os.makedirs(project_name, exist_ok=True)
    print(f"Created project folder: {project_name}")

    # List of folders to create
    folders = ["Assets", "Scripts", "Levels", "Documentation"]
    
    # Create each subfolder
    for folder in folders:
        folder_path = os.path.join(project_name, folder)
        os.makedirs(folder_path, exist_ok=True)
        print(f"Created folder: {folder_path}")
    
    # We'll add code here to create the README file
```

4. Still in the `create_project_structure` function, add this code to create the README file:

```python
    # Create README.md
    readme_path = os.path.join(project_name, "README.md")
    readme_content = f"# {project_name}\n\nThis is a game project created by Awesome Games Studio."
    
    with open(readme_path, 'w') as file:
        file.write(readme_content)
    print(f"Created README file: {readme_path}")
```

5. After the function, add this code to set up argument parsing:

```python
parser = argparse.ArgumentParser(description="Create a game project structure.")
parser.add_argument("project_name", help="Name of the game project")
args = parser.parse_args()
```

6. Finally, at the end of the file, add this code to call the function:

```python
create_project_structure(args.project_name)
```

### Your Tasks 🛠️

1. Combine all the code snippets above into your `create_game_project.py` file.
2. Add comments to your code explaining what each part does. For example:

```python
# Import required modules
import os
import argparse

# Function to create project structure
def create_project_structure(project_name):
    # Create the main project directory
    os.makedirs(project_name, exist_ok=True)
    print(f"Created project folder: {project_name}")

    # List of folders to create
    folders = ["Assets", "Scripts", "Levels", "Documentation"]
    
    # Create each subfolder
    for folder in folders:
        # ... (rest of the function)

# ... (rest of the script)
```

### Testing Your Script 🧪

To test your script:

1. Open the Terminal in PyCharm (usually at the bottom of the window).
2. Run your script with a project name:

```
python create_game_project.py MyAwesomeGame
```

3. Check your file explorer to see if the folders and README file were created.

> [!note] 
> The project folder and files will be created in the same directory as your Python script.

### Deliverables 📦
Your Python script (`create_game_project.py`) with comments explaining the code.

### Evaluation Criteria 🔍
- Correct use of argparse for handling the project name input
- Successful creation of the main project folder, subfolders, and README.md file
- Clear print statements showing the script's actions
- Code readability with comments explaining your code

> [!tip] Reminder
> Remember to use `os.path.join()` when creating file paths. This ensures your script works on different operating systems.

### Submission 📤
Submit your `create_game_project.py` file via the course learning portal.

> [!quote] Encouragement
> This is your first step in creating useful tools with Python! Don't worry if you don't understand every detail yet - focus on getting the script to run and create the folders. If you get stuck, review the lab materials and don't hesitate to ask for help. You're learning valuable skills that will make your work as a tech artist easier and more efficient. Keep going, you've got this! 💻✨