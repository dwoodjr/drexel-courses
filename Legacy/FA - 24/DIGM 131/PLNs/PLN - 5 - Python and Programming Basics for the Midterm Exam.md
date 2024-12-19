# Week 5 PLN: Python and Programming Basics for the Midterm Exam

## Introduction

Welcome to Week 5! This session is designed to reinforce the fundamental concepts of Python programming that are crucial for your midterm exam. We'll explore each concept in detail and see how it's applied in the context of the advanced game project setup and asset generation script you're developing. This guide will help you understand how the basic programming concepts we've learned are used in a real-world scenario of creating a tool for game development pipelines.

---
## 1. Variables and Data Types

Variables in Python are containers for storing data values. Python has several built-in data types, each serving different purposes in programming.

### 1.1 Variable Declaration and Assignment

In Python, you don't need to declare a variable's type explicitly. The type is inferred based on the value assigned.

```python
project_name = "TestProject"  # String
config_path = "config.json"   # String
verbose = True                # Boolean
```

### 1.2 Numeric Data Types

#### 1.2.1 Integers

Integers are whole numbers without a fractional component.

```python
asset_count = 5
year = 2023
```

#### 1.2.2 Floating-Point Numbers (Float)

Floating-point numbers have a decimal point or use scientific notation.

```python
scale_factor = 1.5
radius = 2.0
```

### 1.3 Strings

Strings are sequences of characters, used for text.

```python
asset_name = "LargeCube"
file_path = "C:/Projects/MyGame/Assets/"
```

### 1.4 Booleans

Booleans represent True or False values.

```python
is_valid = True
has_texture = False
```

### 1.5 Lists

Lists are ordered collections of items, which can be of mixed types.

```python
dimensions = [1, 1, 1]  # List of integers
color = [1.0, 0.0, 0.0]  # List of floats representing RGB
```

### 1.6 Using Variables in the Script

In our midterm project, we use variables throughout the script:

```python
def create_project_structure(project_name, folder_structure, verbose=False):
    project_path = os.path.join(os.getcwd(), project_name)
    os.makedirs(project_path, exist_ok=True)
    for folder in folder_structure:
        folder_path = os.path.join(project_path, folder)
        os.makedirs(folder_path, exist_ok=True)
        if verbose:
            print(f"Created folder: {folder_path}")
    return project_path
```

Here, `project_name`, `folder_structure`, and `verbose` are function parameters, `project_path` and `folder_path` are string variables created within the function, and we use string formatting to create output messages.

> [!info] Variables and Data Types
> - Video: [Python Variables (Programming with Mosh)](https://www.youtube.com/watch?v=cQT33yu9pY8)
> - Reference: [Python Variables (GeeksforGeeks)](https://www.geeksforgeeks.org/python-variables/)
> - Reference: [Python Data Types (GeeksforGeeks)](https://www.geeksforgeeks.org/python-data-types/)
> - Advanced Topic: [Type Hinting in Python](https://docs.python.org/3/library/typing.html)


---
## 2. Lists and Dictionaries

Lists and dictionaries are two fundamental data structures in Python that allow you to organize and manipulate collections of data efficiently.

### 2.1 Lists

Lists are ordered, mutable sequences of elements. They can contain items of different types, including other lists.

#### 2.1.1 Creating Lists

```python
# From config.json
folder_structure = ["Assets", "Scenes", "Scripts", "Textures", "Materials", "Documentation"]

# Another example from the script
dimensions = [1, 1, 1]  # List of integers representing width, height, and depth
```

#### 2.1.2 List Indexing

Lists use zero-based indexing (starts counting from 0). You can access individual elements using their index.

```python
first_folder = folder_structure[0]  # "Assets"
last_folder = folder_structure[-1]  # "Documentation"

width = dimensions[0]  # 1
height = dimensions[1]  # 1
depth = dimensions[2]  # 1
```

In the `generate_maya_assets` function, we use indexing to access individual dimensions:

```python
obj = cmds.polyCube(w=asset['dimensions'][0], h=asset['dimensions'][1], d=asset['dimensions'][2], n=asset['name'])[0]
```

#### 2.1.3 List Slicing

You can extract a portion of a list using slicing.

```python
middle_folders = folder_structure[1:4]  # ["Scenes", "Scripts", "Textures"]
```

#### 2.1.4 List Methods

Lists have built-in methods for manipulation:

```python
folder_structure.append("Plugins")  # Adds "Plugins" to the end of the list
folder_structure.remove("Textures")  # Removes "Textures" from the list
```

### 2.2 Dictionaries

Dictionaries are unordered collections of key-value pairs. They provide fast lookups and are highly useful for structured data.

#### 2.2.1 Creating Dictionaries

```python
# Simplified version of the asset configuration
asset_config = {
    "cube": [{"name": "SmallCube", "dimensions": [1, 1, 1], "color": [1, 0, 0]}],
    "sphere": [{"name": "LargeSphere", "radius": 1.5, "color": [0, 1, 0]}]
}
```

#### 2.2.2 Accessing Dictionary Values

You can access values using their keys:

```python
cube_config = asset_config["cube"]
sphere_color = asset_config["sphere"][0]["color"]
```

In the `generate_maya_assets` function, we iterate over the dictionary:

```python
for asset_type, assets in asset_config.items():
    for asset in assets:
        # Use asset properties
```

#### 2.2.3 Dictionary Methods

Dictionaries have useful methods:

```python
asset_types = asset_config.keys()  # Returns a view of all keys
cube_assets = asset_config.get("cube", [])  # Safe way to get a value, returns [] if key doesn't exist
```

### 2.3 Using Lists and Dictionaries Together

In our script, we often use lists within dictionaries to represent multiple assets of the same type:

```python
asset_config = {
    "cube": [
        {"name": "SmallCube", "dimensions": [1, 1, 1], "color": [1, 0, 0]},
        {"name": "LargeCube", "dimensions": [2, 2, 2], "color": [0, 1, 0]}
    ],
    "sphere": [
        {"name": "SmallSphere", "radius": 0.5, "color": [0, 0, 1]},
        {"name": "LargeSphere", "radius": 1.5, "color": [1, 1, 0]}
    ]
}
```

This structure allows us to easily iterate over all assets and create them in Maya:

```python
for asset_type, assets in asset_config.items():
    for asset in assets:
        if asset_type == "cube":
            cmds.polyCube(w=asset['dimensions'][0], h=asset['dimensions'][1], d=asset['dimensions'][2], n=asset['name'])
        elif asset_type == "sphere":
            cmds.polySphere(r=asset['radius'], n=asset['name'])
```

> [!info] Lists and Dictionaries
> - Video: [Python Lists (Programming with Mosh)](https://www.youtube.com/watch?v=9OeznAkyQz4)
> - Reference: [Python Lists (GeeksforGeeks)](https://www.geeksforgeeks.org/python-list/)
> - Video: [Python Dictionaries (Corey Schafer)](https://www.youtube.com/watch?v=daefaLgNkw0)
> - Reference: [Python Dictionary (GeeksforGeeks)](https://www.geeksforgeeks.org/python-dictionary/)
> - Advanced Topic: [List Comprehensions](https://www.w3schools.com/python/python_lists_comprehension.asp)
> - Advanced Topic: [Dictionary Comprehensions](https://www.geeksforgeeks.org/dictionary-comprehension-in-python/)


---
## 3. Functions

Functions are reusable blocks of code that perform a specific task. They help in organizing code, improving readability, and reducing repetition.

### 3.1 Defining Functions

Functions are defined using the `def` keyword, followed by the function name and parameters in parentheses.

```python
def create_material(name, color):
    """Create a Lambert material with the specified color."""
    material = cmds.shadingNode('lambert', asShader=True, name=f"{name}_material")
    cmds.setAttr(f"{material}.color", *color, type="double3")
    return material
```

### 3.2 Function Parameters

Parameters are variables that are passed to a function when it is called.

#### 3.2.1 Required Parameters

```python
def create_primitive(shape_type, size):
    # Function body
```

#### 3.2.2 Optional Parameters with Default Values

```python
def create_project_structure(project_name, folder_structure, verbose=False):
    # Function body
```

### 3.3 Return Values

Functions can return values using the `return` statement.

```python
def load_configuration(config_path):
    try:
        with open(config_path, 'r') as config_file:
            return json.load(config_file)
    except FileNotFoundError:
        print(f"Error: Configuration file not found at {config_path}")
        return None
```

### 3.4 Function Docstrings

Docstrings provide a description of what the function does, its parameters, and return value.

```python
def assign_material(obj, material):
    """
    Assign a material to an object.
    
    Args:
        obj (str): The name of the Maya object.
        material (str): The name of the material to assign.
    """
    shading_group = cmds.sets(renderable=True, noSurfaceShader=True, empty=True, name=f"{material}_SG")
    cmds.connectAttr(f"{material}.outColor", f"{shading_group}.surfaceShader", force=True)
    cmds.sets(obj, edit=True, forceElement=shading_group)
```

### 3.5 Using Functions in the Script

In our midterm project, we use functions to organize our code into logical, reusable units:

```python
def main():
    args = parse_arguments()
    config = load_configuration(args.config_path)
    if config is None:
        return
    
    project_path = create_project_structure(args.project_name, config['folder_structure'], args.verbose)
    
    generate_maya_assets(config['assets'], args.verbose)
    
    save_maya_scene(project_path, args.project_name)
    
    # Print summary
```

This `main` function calls several other functions, each responsible for a specific part of the script's functionality.

> [!info] Functions
> - Video: [Python Functions (Programming with Mosh)](https://www.youtube.com/watch?v=u-OmVr_fT4s)
> - Reference: [Python Functions (GeeksforGeeks)](https://www.geeksforgeeks.org/python-functions/)
> - Advanced Topic: [Lambda Functions](https://www.w3schools.com/python/python_lambda.asp)
> - Advanced Topic: [Decorators](https://realpython.com/primer-on-python-decorators/)


---
## 4. Control Flow (if statements, loops)

Control flow statements direct the order in which a program's code executes. The most common control flow statements are if statements (for decision making) and loops (for repeated execution).

### 4.1 If Statements

If statements allow the program to execute different code based on certain conditions.

#### 4.1.1 Basic If Statement

```python
if verbose:
    print(f"Created folder: {folder_path}")
```

#### 4.1.2 If-Else Statement

```python
if config is None:
    return
else:
    # process configuration
```

#### 4.1.3 If-Elif-Else Statement

```python
if asset_type == "cube":
    obj = cmds.polyCube(w=asset['dimensions'][0], h=asset['dimensions'][1], d=asset['dimensions'][2], n=asset['name'])[0]
elif asset_type == "sphere":
    obj = cmds.polySphere(r=asset['radius'], n=asset['name'])[0]
else:
    print(f"Unsupported asset type: {asset_type}")
    continue
```

### 4.2 Loops

Loops allow you to execute a block of code repeatedly.

#### 4.2.1 For Loops

For loops iterate over a sequence (like a list or dictionary).

```python
for folder in folder_structure:
    folder_path = os.path.join(project_path, folder)
    os.makedirs(folder_path, exist_ok=True)
```

#### 4.2.2 Nested Loops

You can have loops within loops, which is useful for iterating over nested structures.

```python
for asset_type, assets in asset_config.items():
    for asset in assets:
        # Create asset
```

#### 4.2.3 While Loops

While loops continue executing as long as a condition is true.

```python
while True:
    try:
        # attempt some operation
        break
    except SomeError:
        # handle error
        continue
```

### 4.3 Using Control Flow in the Script

In our midterm project, we use control flow extensively to handle different scenarios:

```python
def generate_maya_assets(asset_config, verbose=False):
    created_assets = []
    for asset_type, assets in asset_config.items():
        for asset in assets:
            try:
                if asset_type == "cube":
                    obj = cmds.polyCube(w=asset['dimensions'][0], h=asset['dimensions'][1], d=asset['dimensions'][2], n=asset['name'])[0]
                elif asset_type == "sphere":
                    obj = cmds.polySphere(r=asset['radius'], n=asset['name'])[0]
                elif asset_type == "cylinder":
                    obj = cmds.polyCylinder(r=asset['radius'], h=asset['height'], n=asset['name'])[0]
                else:
                    print(f"Unsupported asset type: {asset_type}")
                    continue
                
                # Create and assign material
                material = create_material(asset['name'], asset['color'])
                assign_material(obj, material)
                
                created_assets.append(obj)
                if verbose:
                    print(f"Created {asset_type}: {asset['name']}")
            except Exception as e:
                print(f"Error creating {asset_type} '{asset['name']}': {str(e)}")
    
    return created_assets
```

This function uses nested loops to iterate over the asset configuration, if-elif statements to handle different asset types, and try-except for error handling.

> [!info] Control Flow
> - Video: [Python If Else (Programming with Mosh)](https://www.youtube.com/watch?v=Zp5MuPOtsSY)
> - Reference: [Python if, if...else, if...elif...else (GeeksforGeeks)](https://www.geeksforgeeks.org/python-if-else/)
> - Video: [Python for Loops (Programming with Mosh)](https://www.youtube.com/watch?v=94UHCEmprCY)
> - Reference: [Python Loops (GeeksforGeeks)](https://www.geeksforgeeks.org/loops-in-python/)
> - Advanced Topic: [List Comprehensions](https://www.w3schools.


---