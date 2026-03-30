# Live Coding Session: Python Basics + Project Structure Automation
## Session Objective
Introduce basic Python concepts (variables, data types, basic operations) while building a simple script to create a project folder structure.

> [!quote] Teaching Script
> Today, we're learning Python basics by creating a script that will help us set up the project folders for a videogame.
## Setup (10 minutes)
- Open PyCharm and create a new Python project
- Ensure your project structure looks like this:

  ``` txt
  YourProjectName/
  ├── .venv/  (or venv/)
  │   ├── Lib/
  │   ├── Scripts/
  │   ├── Include/
  │   └── .gitignore
  └── project_structure.py  (we'll create this)
  ```

- To create project_structure.py:
  1. In PyCharm, ensure you're at the root level of your project
  2. Right-click on the root folder (YourProjectName)
  3. Select "New" > "Python File"
  4. Name it "project_structure.py"

> [!note] Project Structure
> We keep our project files (like project_structure.py) separate from the virtual environment (.venv folder). The virtual environment contains Python and our project's dependencies, while our project folder contains the actual code we write. This separation is a best practice in Python development, keeping our project organized and making it easier to manage dependencies.

> [!quote] Teaching Script
> Now, let's start coding in our new project_structure.py file!
## Step-by-Step Guide

### 1. Hello, Python! (5 minutes)

```python
print("Welcome to Project Structure Automator!")
```
> [!quote] Teaching Script
> - In Python, we use the print function to output text to the console.
> - The text we want to print is enclosed in quotation marks, which tells Python it's a string - a sequence of characters.
> - Notice the parentheses after print - in Python, we always use parentheses to call `functions` (see teaching moment below).
> - This line is a simple Python statement. Each statement typically goes on its own line.

> [!example] Teaching Moment - So what is a function anyway?
> https://www.geeksforgeeks.org/functions-programming/

> [!question] Q for class
> What would happen if we forgot the quotation marks?

> [!answer] Answer
> If we forgot the quotation marks, Python would interpret the text as a variable name or a command, not as a string. This would likely result in a NameError if the text isn't a defined variable, or unexpected behavior if it happens to match an existing variable or command name.

> [!example] Thinking in Steps: Breaking Down Problems
> When approaching a programming task, it's helpful to break it down into smaller steps: https://codedamn.com/news/programming/how-to-solve-coding-problems-guide
> This is an example of [Design Thinking](https://www.interaction-design.org/literature/topics/design-thinking#:~:text=Design%20thinking%20is%20a%20non,%2C%20Ideate%2C%20Prototype%20and%20Test.) `An iterative process for problem-solving`
> 
> 1. Identify the main goal of your script
> 2. List the major tasks needed to achieve that goal
> 3. Break each major task into smaller, manageable steps
> 4. Determine what concepts or tools you'll need for each step
> 
> For example, in our project structure script:
> 1. Main goal: Create a project folder structure
> 2. Major tasks: Set project name, define folders, create directories
> 3. Smaller steps: Store project name in variable, create list of folders, use a loop to create each folder
> 4. Concepts needed: Variables, lists, loops, os module functions
> 
> Practice this approach with your next programming task!

### 2. Variables and Strings (10 minutes)

```python
project_name = "SuperAwesomeGame"
print("We are setting up the project:", project_name)

# String concatenation
project_path = "C:/Games/" + project_name
print("Project path:", project_path)

# F-strings (formatted string literals)
project_path = f"C:/Games/{project_name}"
print("Project path:", project_path)
```
> [!quote] Teaching Script
> - [Variables](https://www.geeksforgeeks.org/variables-programming/) are like containers that store [data types](https://www.geeksforgeeks.org/python-data-types/). Here, we're storing the project name in a variable as a `String` type.
> - We use the equal sign to assign a value to a variable.
> - Strings can be joined together using the plus sign - this is called concatenation.
> - F-strings are a powerful way to embed variables directly in strings. Notice the 'f' before the quotation marks.
> - Inside an f-string, we put variables or expressions inside curly braces {}.
> - F-strings often make our code more readable and easier to understand.

> [!example] Naming Conventions in Python
> Using clear, consistent names in your code makes it easier to read and understand. Here are some [Python naming conventions](https://www.geeksforgeeks.org/python-naming-conventions/):
> 
> 1. Variables and functions: Use lowercase with underscores between words (snake_case)
>    Example: `project_name`, `create_folder`
> 
> 2. Constants: Use all uppercase with underscores
>    Example: `MAX_FILE_SIZE`, `DEFAULT_PATH`
> 
> 3. Classes: Use CamelCase (capitalize each word, no spaces)
>    Example: `GameProject`, `FileManager`
> 
> 4. Modules: Use short, all-lowercase names
>    Example: `os`, `sys`, `math`
> 
> 5. Be descriptive but concise. `player_score` is better than `s` or `the_score_of_the_player`
> 
> Following these conventions will make your code more professional and easier for others (and future you) to read!

> [!question] Q for class
> Come up with three more variables that might be useful for describing a game project.

> [!answer] Answer
> Some possible answers include:
> - game_genre = "RPG"
> - player_count = 4
> - release_date = "2024-12-25"
> - is_multiplayer = True

> [!activity] Think-Pair-Share (~5 minutes)
> Come up with three more variables that might be useful for describing a game project. Discuss with your partner why these `variables` would be helpful and what `data types` they might use.
> 
> After discussion, be prepared to share your ideas with the class.

### 3. Lists (15 minutes)
```python
folders = ["Assets", "Scripts", "Levels", "Documentation"]
print("We will create these folders:", folders)

# List operations
folders.append("Builds")
print("Updated folders:", folders)

print("First folder:", folders[0])
print("Last folder:", folders[-1])

# Looping through a list
for folder in folders:
    print("Creating folder:", folder)
```
> [!quote] Teaching Script
> - [Lists](https://www.geeksforgeeks.org/python-lists/) in Python are collections of items, enclosed in square brackets and separated by commas.
> - We can add items to a list using the append method. Methods are functions that belong to an object.
> - Python uses zero-based indexing, so the first item is at index 0, the second at index 1, and so on.
> - We can use negative indices to count from the end of the list. -1 refers to the last item.
> - A [for loop](https://www.geeksforgeeks.org/for-loop-syntax/) lets us iterate over each item in the list. The 'for' keyword is followed by a variable name that will represent each item, then 'in', then the list name.
> - The indented block after the for statement is executed once for each item in the list.

> [!question] Q for class
> How would you remove the "Documentation" folder from the list?

> [!answer] Answer
> You can remove "Documentation" from the list using the remove() method:
> folders.remove("Documentation")
> Alternatively, you could use:
> folders = [folder for folder in folders if folder != "Documentation"]

> [!activity] Think-Pair-Share (~7 minutes)
> With your partner, brainstorm a list of at least 5 specific asset folders that might be useful in a game project (e.g., "Characters", "Environments"). Then, write a short Python code snippet that creates this list and prints out each folder name.
> 
> Be ready to share your list and code with the class.

### 4. Basic String Operations (10 minutes)
```python
for folder in folders:
    full_path = f"{project_name}/{folder}"
    print("Full path:", full_path)
```
> [!quote] Teaching Script
> - Here we're combining f-strings with our for loop to create full paths for each folder.
> - The f-string allows us to embed our variables directly in the string.
> - This approach is very readable and makes it clear what the final string will look like.
> - As we loop through each folder, the 'folder' variable takes on each value in the list.

> [!question] Q for class
> How could we modify this to include the "C:/Games/" part in every path?

> [!answer] Answer
> We could modify the f-string to include the base path:
> full_path = f"C:/Games/{project_name}/{folder}"
> Alternatively, we could create a base_path variable and use it in our f-string:
> base_path = "C:/Games"
> full_path = f"{base_path}/{project_name}/{folder}"

> [!activity] Think-Pair-Share "6 minutes"
> Discuss with your partner how you could modify our current code to include a version number in each folder path. For example, instead of "ProjectName/Assets", it would be "ProjectName_v1.0/Assets".
> 
> Write out the modified line of code and be prepared to explain your solution to the class.

### 5. Introducing the `os` Module (15 minutes)
```python
import os

for folder in folders:
    full_path = os.path.join("C:/Games", project_name, folder)
    print("Full path:", full_path)
    # os.makedirs(full_path, exist_ok=True)  # We'll uncomment this later!
```
> [!quote] Teaching Script
> - [Modules](https://www.geeksforgeeks.org/python-modules/) in Python are like toolkits - they contain helpful functions we can use in our scripts.
> - We use the 'import' keyword to bring in a module. Here, we're importing the 'os' module, which helps with operating system related tasks.
> - `os.path.join` is a function that combines path components intelligently, regardless of the operating system.
> - It automatically uses the correct separator (slash or backslash) for the current operating system.
> - The `os.makedirs` function (when uncommented) will actually create these directories on your computer.
> - We're using 'exist_ok=True' to prevent errors if the directory already exists.
> - Python documentation has a[ list of all supported python modules](https://docs.python.org/3/py-modindex.html)

> [!question] Q for class
> Why might `os.path.join` be better than manual string concatenation for file paths?

> [!answer] Answer
> os.path.join is better because:
> 1. It automatically uses the correct path separator for the current operating system (/ for Unix/Mac, \ for Windows).
> 2. It handles cases where there are already separators at the end of path components, preventing double separators.
> 3. It's more readable and less error-prone, especially for complex paths.
> 4. It's more maintainable if you need to port your code to a different operating system.

> [!example] Debugging: Reading Error Messages
> [Error messages](https://www.geeksforgeeks.org/runtime-errors/) can be intimidating, but they're incredibly helpful. Here's how to read them:
> 
> 1. Look at the last line of the error message first - it often tells you what type of error occurred
> 2. Find the line number where the error occurred
> 3. Read the error description - it often gives clues about what went wrong
> 
> Common errors for beginners:
> - SyntaxError: You might have a typo or forgotten a colon (:)
> - NameError: You're using a variable that hasn't been defined
> - IndentationError: Your code isn't indented correctly
> 
> Remember, errors are normal in programming. They're not failures, they're opportunities to learn and improve your code!

> [!activity] Think-Pair-Share "8 minutes"
> With your partner, explore the Python documentation for the `os` module. Find two other functions in the `os` module that might be useful for managing project files or directories. Discuss how you might use these functions in our project structure script.
> 
> Be ready to share your findings and ideas with the class.

### 6. Putting It All Together (15 minutes)
```python
import os

def create_project_structure(name, base_path="C:/Games"):
    project_path = os.path.join(base_path, name)
    folders = ["Assets", "Scripts", "Levels", "Documentation", "Builds"]
    
    print(f"Creating project structure for: {name}")
    for folder in folders:
        full_path = os.path.join(project_path, folder)
        print(f"Creating folder: {full_path}")
        # os.makedirs(full_path, exist_ok=True)  # We'll uncomment this later!

create_project_structure("MyAwesomeGame")
```
> [!quote] Teaching Script
> - We define a function using the 'def' keyword, followed by the function name and parentheses.
> - Name here is a[ function parameter](https://www.geeksforgeeks.org/deep-dive-into-parameters-and-arguments-in-python/)
> - Inside the parentheses, we specify the parameters our function accepts.
> - We can provide default values for parameters, like we're doing with base_path here.
> - Inside our function, we're bringing together all the concepts we've learned: variables, f-strings, lists, for loops, and the os module.
> - This function encapsulates our project creation logic, making it reusable and easier to understand.
> - We call our function by using its name followed by parentheses containing the arguments.

> [!question] Q for class
> How might you expand this script to be more useful for your game development workflow?

> [!answer] Answer
> - Some possible expansions could include:
> - Adding more specific folders for different asset types (e.g., "Models", "Textures", "Audio")
> - Creating default files in each folder (e.g., a README.md in each directory)
> - Integrating with version control (e.g., initializing a git repository)
> - Adding command-line arguments to customize the project name and structure
> - Creating a configuration file to define different project structures for different types of games

> [!example] Using Pseudocode to Plan Your Script
> [Pseudocode](https://www.geeksforgeeks.org/how-to-write-a-pseudo-code/) is a great way to plan your script before diving into actual coding. It helps you focus on logic without worrying about syntax. Here's how to use it:
> 
> 1. Write out the steps of your program in plain English
> 2. Use indentation to show structure (like loops or conditional statements)
> 3. Be specific about what each step does, but don't worry about Python syntax
> 
> Example pseudocode for our project structure script:
> ``` txt
> Set the project name
> Create a list of folder names
> For each folder name:
>     Combine project name and folder name to create full path
>     If the full path doesn't exist:
>         Create the directory
>     Print a message saying the directory was created
> Print a message that the project structure is complete
> ```
> 
> Try writing pseudocode for your next programming task before you start coding!

> [!activity] Think-Pair-Share "10 minutes"
> With your partner, sketch out a plan for a more advanced version of our `project_structure` function. Consider adding features like:
> - Allowing customization of the folder structure
> - Creating default files in certain folders
> - Handling errors (e.g., if a folder already exists)
> 
> Outline your enhanced function and be prepared to discuss your design decisions with the class.

### 7. Wrap-up and Next Steps (10 minutes)

> [!summary] Recap
> Today we covered several key Python concepts:
> - Variables and data types (strings, integers)
> - Lists and list operations
> - For loops for iteration
> - String formatting with f-strings
> - Basic module usage (importing and using the `os` module)
> - Creating functions to encapsulate our code

> [!info] Looking Ahead
> In future lessons, we'll expand on these concepts by:
> - Exploring more complex data structures (dictionaries, sets)
> - Diving deeper into functions and introducing lambda functions
> - Learning about file I/O operations
> - Introducing error handling with try/except blocks
> - Exploring more modules useful for game development and pipeline automation

> [!task] Assignment Introduction
> Your upcoming assignment will build directly on what we've learned today:
> - You'll create a more advanced version of our project structure script
> - The script will allow for customizable folder structures
> - You'll implement error handling to make the script more robust
> - Bonus challenges will include creating default files and integrating with version control
> 
> This assignment will give you hands-on experience applying these Python basics to a real-world tech art scenario.

> [!question] Final Reflection
> Take a moment to consider:
> - Which concept from today's lesson do you think will be most useful in your work?
> - What questions do you still have about Python or project structure automation?
> 
> Feel free to share your thoughts or ask questions before we wrap up.

> [!danger] BREAK (~15 Minutes)
> Let's have a break before be begin the lab portion of our class.






