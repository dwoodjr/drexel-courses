# Live Coding Session: Functions and Modular Design in Maya

## Session Objective
Introduce functions, modules, and importing while creating utility functions for common DCC tasks in Maya, focusing on creating objects and setting attributes.

## Setup (10 minutes)
- Open Maya and ensure the Script Editor is visible
- Create a new Python tab in the Script Editor
- Explain how to execute Python code in Maya's Script Editor (see `Step 0` below)

> [!quote] Teaching Script
> Today, we're diving into functions and modular design, which are crucial for creating efficient and reusable code. We'll be applying these concepts to Maya, learning how to create utility functions for common tasks like creating objects and setting attributes.

---
## Step-by-Step Guide
### 0.a. Workflow Between PyCharm and Maya (20 minutes)

> [!quote] Teaching Script
> Now that we've covered the basics of functions and modules in Maya, let's discuss how to effectively work between PyCharm and Maya. This workflow will allow you to take advantage of PyCharm's powerful editing features while still being able to execute your code in Maya.

> [!attention] Useful Tool/Plugin
> One very useful plugin for JetBrains IDEs that allows us to more seamlessly work with maya is [MayaCharm](https://plugins.jetbrains.com/plugin/8218-mayacharm/versions/stable)

> [!quote] Teaching Script
> While we've been using PyCharm, we can enhance its Maya integration using a plugin called MayaCharm. Let's set it up to streamline our Maya scripting workflow in PyCharm.

1. Install the MayaCharm Plugin:
   - Go to the provided download link above and download the latest MayaCharm zip.
   - Open PyCharm
   - Go to File > Settings (on Windows/Linux) or PyCharm > Preferences (on macOS)
   - Navigate to Plugins
   - Click the gear icon then select `Instasll Plugin from Disk...`
   - Search for and select the MayaCharm Zip

1. Set up the Command Port in Maya:
   - In Maya's Script Editor, switch to the Python tab
- Enter and execute this command in the shell:
  ```python
  import maya.cmds as cmds
if not cmds.commandPort(':4434', q=True):
   cmds.commandPort(n=':4434')
	```

4. Connect PyCharm to Maya:
   - In PyCharm, go to Tools > MayaCharm > Connect to Maya
   - You should see a message confirming the connection

5. Test the Connection:
   - Create a new Python file in PyCharm
   - Add the following code:
     ```python
     import maya.cmds as cmds
     
     cube = cmds.polyCube()[0]
     cmds.move(0, 2, 0, cube)
     ```
   - Right-click in the editor and choose "Execute in Maya" or use the keyboard shortcut (usually Ctrl+Enter or Cmd+Enter)

> [!tip] Pro Tip
> MayaCharm allows you to select specific lines of code to execute in Maya, making it easy to test and debug parts of your script.

### 0.b. Connecting Visual Studio Code with Maya using MayaCode

> [!quote] Teaching Script
> We've been using PyCharm, but Visual Studio Code (VS Code) is another popular IDE for Python development. Let's set up VS Code to work with Maya using the [MayaCode extension](https://marketplace.visualstudio.com/items?itemName=saviof.mayacode).

1. Install the MayaCode Extension:
   - Open VS Code
   - Go to the Extensions view (Ctrl+Shift+X)
   - Search for "MayaCode"
   - Click "Install" on the MayaCode extension

1. Connect to Maya:
   - Start Maya if it's not already running
      - In the maya MEL script tab run the following command:
```MEL
commandPort -name "localhost:7001" -sourceType "mel" -echoOutput;
```

   - In VS Code, use the command palette (Ctrl+Shift+P)
   - Type "MayaCode: Connect to Maya" and select it
   - VS Code should connect to Maya

4. Test the Connection:
   - Create a new file in VS Code with a `.py` extension
   - Add the following code:
     ```python
     from maya import cmds
     
     cube = cmds.polyCube()[0]
     cmds.move(0, 2, 0, cube)
     ```
   - Select the code
   - Right-click and choose "MayaCode: Execute in Maya" or use the keyboard shortcut

> [!tip] Pro Tip
> MayaCode provides code completion for Maya commands, making it easier to write Maya Python scripts in VS Code.

---
> [!attention] Maya Commands Refence: Your Best Friend
> https://help.autodesk.com/view/MAYAUL/2024/ENU/?guid=__CommandsPython_index_html
### 1. Introduction to Functions (15 minutes)

```python
import maya.cmds as cmds

def create_cube(size=1):
    cube = cmds.polyCube(w=size, h=size, d=size)[0]
    return cube

# Test the function
result = create_cube(2)
print(f"Created cube: {result}")
```

> [!quote] Teaching Script
> • Functions allow us to encapsulate reusable pieces of code
> • We define functions using the `def` keyword
> • Parameters allow us to customize function behavior
> • The `return` statement specifies what the function should output
> • We're using Maya's `cmds` module to interact with Maya's functionality

> [!question] Q for class
> How might we modify this function to create different types of primitive shapes?

> [!answer] Answer
> We could create a more general function that takes the shape type as a parameter:

```python
def create_primitive(shape_type, size=1):
    if shape_type == "cube":
        return cmds.polyCube(w=size, h=size, d=size)[0]
    elif shape_type == "sphere":
        return cmds.polySphere(r=size)[0]
    elif shape_type == "cylinder":
        return cmds.polyCylinder(r=size, h=size)[0]
    else:
        print(f"Unsupported shape type: {shape_type}")
        return None
```

### 2. Function Parameters and Default Values (20 minutes)

```python
def create_primitive(shape_type, size=1, name=None):
    if shape_type == "cube":
        obj = cmds.polyCube(w=size, h=size, d=size)[0]
    elif shape_type == "sphere":
        obj = cmds.polySphere(r=size)[0]
    elif shape_type == "cylinder":
        obj = cmds.polyCylinder(r=size, h=size)[0]
    else:
        print(f"Unsupported shape type: {shape_type}")
        return None
    
    if name:
        obj = cmds.rename(obj, name)
    
    return obj

# Test the function
cube = create_primitive("cube", 2, "my_cube")
sphere = create_primitive("sphere", 1.5)
print(f"Created cube: {cube}")
print(f"Created sphere: {sphere}")
```

> [!quote] Teaching Script
> • Function parameters make our code more flexible
> • Default parameter values allow for optional arguments
> • We can use conditional statements to handle different cases within a function
> • The `cmds.rename()` function allows us to set custom names for objects in Maya

> [!question] Q for class
> What would happen if we called the function without any arguments?

> [!answer] Answer
> If we called `create_primitive()` without any arguments, we would get an error because the `shape_type` parameter is required (it has no default value). To fix this, we could either provide a default value for `shape_type` or use exception handling to manage the error gracefully.

### 3. Modular Design and Importing (25 minutes)

> [!quote] Teaching Script
> Let's create a more Maya-accurate version of our utility functions. We'll update our code to create and assign materials with the specified colors, which is the standard way of working with colors in Maya.

1. Update the content of `maya_utils.py`:

```python
import maya.cmds as cmds

def create_primitive(shape_type, size=1, name=None):
    if shape_type == "cube":
        obj = cmds.polyCube(w=size, h=size, d=size)[0]
    elif shape_type == "sphere":
        obj = cmds.polySphere(r=size)[0]
    elif shape_type == "cylinder":
        obj = cmds.polyCylinder(r=size, h=size)[0]
    else:
        print(f"Unsupported shape type: {shape_type}")
        return None
    
    if name:
        obj = cmds.rename(obj, name)
    
    return obj

def create_color_material(color, name=None):
    material = cmds.shadingNode('lambert', asShader=True)
    cmds.setAttr(f"{material}.color", *color, type="double3")
    
    if name:
        material = cmds.rename(material, name)
    
    return material

def assign_material(obj, material):
    cmds.select(obj)
    cmds.hyperShade(assign=material)

def create_colored_primitive(shape_type, size=1, name=None, color=(1, 1, 1)):
    obj = create_primitive(shape_type, size, name)
    if obj:
        material_name = f"{obj}_material" if name else None
        material = create_color_material(color, material_name)
        assign_material(obj, material)
    return obj
```

2. Now, let's use this updated module in Maya's Script Editor:

```python
import sys
sys.path.append(r"C:/Users/YourUsername/Documents/maya/scripts")  # Adjust this path
import maya_utils

red_cube = maya_utils.create_colored_primitive("cube", 2, "red_cube", (1, 0, 0))
blue_sphere = maya_utils.create_colored_primitive("sphere", 1.5, "blue_sphere", (0, 0, 1))

print(f"Created red cube: {red_cube}")
print(f"Created blue sphere: {blue_sphere}")
```

> [!quote] Teaching Script
> • We've updated our utility functions to work with Maya's material system.
> • The `create_color_material` function creates a new Lambert material with the specified color.
> • `assign_material` function assigns the created material to our object.
> • This approach correctly sets up the relationship between objects and materials in Maya.

> [!tip] Maya Materials
> In Maya, materials (or shaders) define the visual properties of objects, including color. The Lambert shader we're using here is a basic material type, but Maya offers many other shader types for more complex visual effects.

> [!question] Q for class
> How might we extend this system to work with more complex material types in Maya, such as the standardSurface shader?

> [!answer] Answer
> To work with more complex materials like standardSurface:
> 1. We could create a new function `create_standard_surface_material()`.
> 2. This function would create a standardSurface shader and set various attributes (base color, metalness, roughness, etc.).
> 3. We might add parameters to control these additional material properties.
> 4. Our `create_colored_primitive` function could then have an optional parameter to specify the material type.
> 
> Example:
> ```python
> def create_standard_surface_material(color, metalness=0, roughness=0.5, name=None):
>     material = cmds.shadingNode('standardSurface', asShader=True)
>     cmds.setAttr(f"{material}.baseColor", *color, type="double3")
>     cmds.setAttr(f"{material}.metalness", metalness)
>     cmds.setAttr(f"{material}.specularRoughness", roughness)
>     if name:
>         material = cmds.rename(material, name)
>     return material
> ```

### 4. Best Practices for Working with Custom Modules in Maya

When working with custom modules in Maya, especially during development and testing, it's crucial to ensure you're always working with the latest version of your code. Here's the recommended approach:

1. Set Up Your Module:
   Create your module (e.g., `maya_utils.py`) in a directory that's easily accessible.

2. Create a Test Script:
   Create a separate test script (e.g., `test_script.py`) in the same directory:

   ```python
   # test_script.py
   import sys
   import os
   import importlib

   # Add your module's directory to sys.path if necessary
   script_dir = os.path.dirname(os.path.abspath(__file__))
   if script_dir not in sys.path:
       sys.path.append(script_dir)

   import maya_utils
   importlib.reload(maya_utils)

   # Your test code here
   red_cube = maya_utils.create_colored_primitive("cube", 2, "red_cube", (1, 0, 0))
   blue_sphere = maya_utils.create_colored_primitive("sphere", 1.5, "blue_sphere", (0, 0, 1))

   print(f"Created red cube: {red_cube}")
   print(f"Created blue sphere: {blue_sphere}")
   ```

3. Execute Your Test Script in Maya:
   In Maya's Script Editor, use the following code to run your test script:

   ```python
   import os
   import sys

   script_path = r"E:\DIGM131-FA24\Week 3\ModularMaya\test_script.py"

   # Ensure the script's directory is in sys.path
   script_dir = os.path.dirname(script_path)
   if script_dir not in sys.path:
       sys.path.append(script_dir)

   # Execute the script
   with open(script_path, 'r') as file:
       exec(file.read())
   ```

4. For Quick Testing:
   If you prefer to keep your test code in the Script Editor for quick iterations, you can use:

   ```python
   import sys
   import os
   import importlib

   script_dir = r"E:\DIGM131-FA24\Week 3\ModularMaya"
   if script_dir not in sys.path:
       sys.path.append(script_dir)

   import maya_utils
   importlib.reload(maya_utils)

   # Your test code here
   red_cube = maya_utils.create_colored_primitive("cube", 2, "red_cube", (1, 0, 0))
   blue_sphere = maya_utils.create_colored_primitive("sphere", 1.5, "blue_sphere", (0, 0, 1))

   print(f"Created red cube: {red_cube}")
   print(f"Created blue sphere: {blue_sphere}")
   ```

> [!note] Why Reloading is Necessary
> Python caches imported modules for efficiency. In long-running environments like Maya, this means changes to your module might not be reflected unless you explicitly reload it. Always reload during development to ensure you're testing the latest version of your code.

> [!tip] Pro Tip
> For frequently used scripts, you can create a shelf button in Maya with the execution code. This allows you to run your script with a single click.

> [!warning] Caution
> Be careful when using `exec()` with untrusted code, as it can execute any Python commands. Always ensure you trust the source of the script you're executing.

### 5. Verifying Results in Maya

When working with scripts that create or modify objects in Maya (or any DCC), it's crucial to carefully verify the results. Here are some tips to ensure you're looking at the correct objects:

1. Naming Conventions:
   Always use clear, descriptive names for your objects. For example:
   ```python
   red_cube = maya_utils.create_colored_primitive("cube", 2, "red_cube_size_2", (1, 0, 0))
   blue_sphere = maya_utils.create_colored_primitive("sphere", 1.5, "blue_sphere_size_1_5", (0, 0, 1))
   ```

2. Outliner Organization:
   Group your test objects for easy identification:
   ```python
   test_group = cmds.group(empty=True, name="test_objects")
   cmds.parent(red_cube, test_group)
   cmds.parent(blue_sphere, test_group)
   ```

3. Print Object Details:
   After creating objects, print their details to confirm:
   ```python
   def print_object_details(obj_name):
       translation = cmds.xform(obj_name, query=True, translation=True)
       scale = cmds.xform(obj_name, query=True, scale=True)
       print(f"Object: {obj_name}")
       print(f"  Position: {translation}")
       print(f"  Scale: {scale}")

   print_object_details("red_cube_size_2")
   print_object_details("blue_sphere_size_1_5")
   ```

4. Visual Checks:
   - Use Maya's focus feature (f key) on each object after creation.
   - Temporarily hide other objects in the scene to isolate your test objects.

5. Attribute Editor:
   Always double-check the Attribute Editor for precise values of transform, scale, and other properties.

> [!tip] Pro Tip
> Develop a habit of systematically verifying your script's output. This includes checking the script's print statements, Maya's Outliner, and the actual 3D viewport. Remember, what we think we're looking at isn't always what we're actually seeing!

### 6. Introduction to Dictionaries (20 minutes)

Objective: Introduce students to Python dictionaries and demonstrate their use in organizing related data, specifically in the context of Maya asset creation.

Key Points:
- Explain what dictionaries are and why they're useful
- Demonstrate how to create and use a dictionary
- Show how dictionaries can be used to map asset types to Maya commands

Live Coding:
1. Start by explaining the concept of dictionaries:
   "Dictionaries in Python are like real-world dictionaries: they have keys (words) and values (definitions). In code, we can use them to store and retrieve related information efficiently."

2. Create a dictionary of asset types and their corresponding Maya commands:
   ```python
   asset_types = {
       "building": cmds.polyCube,
       "tree": cmds.polyCone,
       "rock": cmds.polySphere
   }
   ```
   Explain: "Here, we're mapping asset types to their corresponding Maya creation functions. This allows us to easily look up the right function for each asset type."

3. Implement the `create_asset` function using the dictionary:
   ```python
   def create_asset(asset_type, size=1):
       if asset_type in asset_types:
           return asset_types[asset_type](width=size, height=size, depth=size)[0]
       else:
           print(f"Unsupported asset type: {asset_type}")
           return None
   ```
   Explain: "This function uses our dictionary to dynamically choose the right Maya command based on the asset type. It's more flexible than using if-elif statements for each type."

4. Demonstrate using the function:
   ```python
   building = create_asset("building", 2)
   tree = create_asset("tree", 1.5)
   rock = create_asset("rock", 1)

   print(f"Created building: {building}")
   print(f"Created tree: {tree}")
   print(f"Created rock: {rock}")
   ```

5. Show how easy it is to add new asset types:
   ```python
   asset_types["lamp"] = cmds.polyTorus
   lamp = create_asset("lamp", 0.5)
   print(f"Created lamp: {lamp}")
   ```

Discussion Points:
- Ask students how this approach compares to using multiple if-elif statements
- Discuss potential uses of dictionaries in other aspects of game development or 3D modeling pipelines

Quick Challenge:
Ask students to add a new asset type (e.g., "car" using `cmds.polyCylinder) to the `asset_types` dictionary and test it with the `create_asset` function.

Wrap-up:
Summarize the benefits of using dictionaries for organizing related data and how it can make our code more flexible and easier to maintain.

### 7. Wrap-up and Next Steps (10 minutes)

> [!summary] Recap
> Today we covered:
> - Creating functions for common Maya tasks
> - Modular design and importing custom modules
> - Error handling and logging in Maya scripts

> [!info] Looking Ahead
> In future lessons, we'll explore:
> - More advanced Maya operations (rigging, animation)
> - Creating custom UI elements in Maya
> - Optimizing scripts for large scenes or batch operations

> [!task] Assignment Introduction
> Your upcoming assignment will build on today's concepts:
> - You'll create a module with utility functions for Maya
> - The module will include functions for creating, modifying, and organizing objects
> - You'll implement error handling and logging
> - Bonus challenges will include creating a simple UI for your utilities
> 
> This assignment will give you hands-on experience in creating reusable, modular code for Maya.

> [!question] Final Reflection
> Consider:
> - How might these concepts apply to your current or future projects in Maya?
> - What other repetitive tasks in your Maya workflow could be automated using similar techniques?
> 
> Feel free to share your thoughts or ask any final questions.

> [!danger] BREAK (15 Minutes)
> Let's take a short break before we begin the lab portion of our class.