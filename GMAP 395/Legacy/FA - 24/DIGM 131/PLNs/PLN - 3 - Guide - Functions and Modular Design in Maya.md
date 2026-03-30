# Live Coding Session: Functions and Modular Design in Maya

## Session Objective
Learn how to create reusable functions for common Maya tasks and organize them into a modular structure. This will help you automate repetitive processes and build more efficient workflows in Maya.

## Setup
- Open Maya and ensure the Script Editor is visible
- Create a new Python tab in the Script Editor
- Open your preferred code editor (PyCharm or Visual Studio Code)

> [!note] Important Setup Note
> Make sure you have Python and Maya installed on your system. We'll be using Python 3.x and Maya 2023 or later.

## Key Concepts to Watch For
- Functions in Python
- Modular design principles
- Maya Python commands (cmds module)
- Importing and using custom modules in Maya

## Problem-Solving Exercise: Breaking Down Today's Task

Let's break down the programming task for today's session:

1. What is the main goal of our script/program?
   Main goal: ___

2. What are the major tasks we need to accomplish to achieve this goal?
- ___

3. Let's break down one of these major tasks into smaller steps. 
   Selected task: ___
   Steps to accomplish this task:
	- ___

1. What Python concepts or tools will we need to use?
	- ___

🖊️ Reflection: 
How might this task relate to real-world game development or animation workflows?

---
## Step-by-Step Guide

### 1.a. Setting Up the Development Environment

#### Option A: Setting up PyCharm with MayaCharm

1. Install the MayaCharm Plugin:
   - Go to File > Settings (on Windows/Linux) or PyCharm > Preferences (on macOS)
   - Navigate to Plugins
   - Search for "MayaCharm" and install it
   - Restart PyCharm

2. Set up the Command Port in Maya:
   - In Maya's Script Editor, switch to the Python tab
   - Enter and execute this command:
     ```python
     import maya.cmds as cmds
     if not cmds.commandPort(':4434', q=True):
        cmds.commandPort(n=':4434')
     ```

3. Connect PyCharm to Maya:
   - In PyCharm, go to Tools > MayaCharm > Connect to Maya
   - You should see a message confirming the connection

#### Option B: Setting up Visual Studio Code with MayaCode

1. Install the MayaCode Extension:
   - Open VS Code
   - Go to the Extensions view (Ctrl+Shift+X)
   - Search for "MayaCode"
   - Click "Install" on the MayaCode extension

2. Connect to Maya:
   - Start Maya if it's not already running
   - In Maya's Script Editor, in the MEL tab, run:
     ```mel
     commandPort -name "localhost:7001" -sourceType "mel" -echoOutput;
     ```
   - Execute this code in the Maya Script editor to open the connection.

🔍 Quick Challenge: Create a new Python file in your chosen editor, write a simple Python print statement, and execute it in Maya using your newly set up environment.

> [!attention] Maya Commands Refence: Your Best Friend
> https://help.autodesk.com/view/MAYAUL/2024/ENU/?guid=__CommandsPython_index_html
### 1.b. Introduction to Functions

```python
import maya.____ as ____

def create_cube(____=1):
    cube = cmds.______(w=____, h=____, d=____)[0]
    return ____

# Test the function
result = ______(2)
print(f"Created cube: {____}")
```
### 2. Creating Our First Maya Utility Function

```python
import maya.cmds as cmds

def create_primitive(shape_type, size=1):
    if shape_type == "cube":
        return cmds.polyCube(w=____, h=____, d=____)[0]
    elif shape_type == "sphere":
        return cmds.polySphere(r=____)[0]
    elif shape_type == "cylinder":
        return cmds.polyCylinder(r=____, h=____)[0]
    else:
        print(f"Unsupported shape type: ____")
        return ____
```

> [!example] Function Parameters
> In Python, we can define functions with parameters to make them more flexible. Here, `shape_type` and `size` are parameters that allow us to customize the primitive we're creating.

🔍 Quick Challenge: Add another shape type (e.g., "cone") to the `create_primitive` function.

### 3. Implementing Color Assignment

```python
def create_color_material(color, name=None):
    material = cmds.shadingNode(____, asShader=True)
    cmds.setAttr(f"{material}.color", ____, type="double3")
    
    if name:
        material = cmds.____(material, name)
    
    return ____

def assign_material(obj, material):
    cmds._____(obj)
    cmds.hyperShade(____=material)

def create_colored_primitive(shape_type, size=1, name=None, color=(1, 1, 1)):
    obj = ______(shape_type, size)
    if obj:
        material_name = f"{obj}_material" if name else None
        material = ______(color, material_name)
        ______(obj, material)
    return ____
```

### 4. Organizing into a Module

Create a new file named `maya_utils.py` and move all our functions into it.

```python
# maya_utils.py
# maya_utils.py
import maya.cmds as cmds

# [Include all the functions we've created so far]

if ____ == "____":
    # Test code
    cube = create_colored_primitive(____, ____, ____, ____)
    sphere = create_colored_primitive(____, ____, ____, ____)
    print(f"Created red cube: {____}")
    print(f"Created blue sphere: {____}")
```

🔍 Customization Opportunity: Add your own test code to create a scene with multiple colored primitives.

### 5. Importing and Using Our Module

In Maya's Script Editor:

```python
import ____
____.path.append(r"C:/Path/To/Your/Script/Directory")  # Adjust this path
import ______
import importlib
importlib.______(maya_utils)

# Use the functions from our module
red_cube = maya_utils.______(_____, _____, _____, _____)
blue_sphere = maya_utils.______(_____, _____, _____, _____)

print(f"Created red cube: {____}")
print(f"Created blue sphere: {____}")
```

### 6. Introduction to Dictionaries

```python
# Define a dictionary of asset types and their corresponding Maya commands
asset_types = {
    "building": cmds.________,
    "tree": cmds.________,
    "rock": cmds.________
}

def create_asset(asset_type, ____=1):
    if asset_type ____ asset_types:
        # Use the dictionary to call the appropriate Maya command
        return asset_types[________](width=____, height=____, depth=____)[0]
    else:
        print(f"Unsupported asset type: {________}")
        return ________

# Test the function
building = create_asset("________", 2)
tree = create_asset("________", 1.5)
rock = create_asset("________", 1)

print(f"Created building: {________}")
print(f"Created tree: {________}")
print(f"Created rock: {________}")
```

> [!example] Dictionaries in Python
> Dictionaries are versatile data structures that store key-value pairs. They're useful for mapping between related pieces of information. In this case, we're using a dictionary to map asset types to their corresponding Maya creation functions.

🔍 Quick Challenge: Add a new asset type (e.g., "lamp" using `cmds.polyTorus`) to the `asset_types` dictionary and test it with the `create_asset` function.

## Reflection Questions
1. How can modular design improve our Maya scripting workflow?
2. What other common Maya tasks could we turn into reusable functions?
3. How might we extend this system to work with more complex shapes or materials?

## Notes
[Use this space to write your own notes, questions, and observations]

## Looking Ahead
In our next session, we'll explore:
- Creating more advanced Maya operations (e.g. animation)  and refining our scripts 
- Developing custom UI elements for our Maya tools
- Optimizing our scripts
