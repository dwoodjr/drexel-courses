# Assignment 3: Modular Asset Creation, Management, and Configuration

## Background
As a junior technical artist at Awesome Games Studio, you're expanding on the Maya scripting skills you've learned in class. The 3D environment team has requested a simple tool to create and color basic shapes in Maya for use as placeholder assets.

## Your Mission 🎯
Complete and extend the partially-written script to create and color basic shapes in Maya, and add a function to list all created assets. This assignment will reinforce your understanding of Maya scripting and encourage problem-solving within the framework provided.

---
## --- **Week 3** ---
### Requirements 📋
1. Complete the `asset_creator.py` script by filling in the missing code and implementing additional functionality. *You will at times need to reference the code from Week 3 live coding:* `maya_utils.py`
2. Ensure the script can:
   - Create colored primitive shapes (cube, sphere, cylinder, and cone)
   - List all assets created by the script
   - (Bonus) Randomly position created shapes
3. Use Maya's `cmds` module for all Maya operations.
4. Add comments explaining your code and your reasoning for implementations.

> [!tip] Maya Python Commands Documentation
> Throughout this assignment, you'll need to use various Maya Python commands. You can find detailed documentation here:
> [Maya Python Command Reference](https://help.autodesk.com/view/MAYAUL/2023/ENU/?guid=__CommandsPython_index_html)

### Step 1: Set up your script file

Create a new file named `asset_creator.py` and start with the following code:

```python
import maya.cmds as cmds

print("Asset Creator script loaded!")

# Define shape types
SHAPE_TYPES = {
    "cube": cmds.polyCube,
    "sphere": cmds.polySphere,
    "cylinder": cmds.polyCylinder,
    # TODO: Add the missing shape type here
}
```

> [!info] Python Dictionaries
> Dictionaries in Python are versatile data structures that store key-value pairs. They're great for mapping related pieces of information. Learn more about dictionaries here:
> [Python Dictionary Documentation](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)

> [!note] Task
> Add the missing shape type ("cone") to the `SHAPE_TYPES` dictionary. Why do you think we're using a dictionary for this? Comment your thoughts.

### Step 2: Complete the primitive creation function

Add this function to your script and fill in the blanks: 
`Hint: create_func takes the place of cmds.polyXXXX from Week 3 live coding`
`Hint: Be sure to refernce the Maya CMDs Reference above to know which "size" attributes each shape has`

```python
def create_primitive(shape_type, size, name=None):
    if shape_type not in SHAPE_TYPES:
        print(f"Unsupported shape type: {shape_type}")
        return None

    create_func = SHAPE_TYPES[shape_type]
    
    # TODO: Implement the creation logic for each shape type
    if shape_type == "cube":
        obj = create_func(width=size, height=size, depth=size)[0]
    elif shape_type == "sphere":
        obj = # Your code here
    elif shape_type in ["cylinder", "cone"]:
        obj = # Your code here

    if name:
        obj = cmds.rename(obj, name)
    
    return obj
```

> [!note] Task
> Implement the creation logic for each shape type. Consider how the `size` parameter should affect each shape differently. Add comments explaining your decisions.

> [!warning] Common Pitfall
> Remember that different shape types may use different attributes for size. For example, a sphere uses radius, while a cube uses width, height, and depth. Consult the[ Maya Python Command Reference](https://help.autodesk.com/view/MAYAUL/2024/ENU/?guid=__CommandsPython_index_html) for each shape type.

### Step 3: Implement the color material function

Add this function to your script:

```python
def create_color_material(color, name=None):
    # TODO: Create a Lambert material and set its color
    material = # Your code here
    
    if name:
        material = cmds.rename(material, name)
    
    return material
```

> [!note] Task
> Implement the `create_color_material` function. How would you ensure that the color values are valid? Add a comment discussing this.

> [!info] Maya Materials
> In Maya, materials define the look of objects. The Lambert shader is a basic material type. Learn more about materials in Maya:
> [Maya Materials Overview](https://help.autodesk.com/view/MAYAUL/2024/ENU/?guid=GUID-634CAFBE-AC48-4B73-89CA-82D64FA1BC70)

### Step 4: Implement the material assignment function

Add this function to your script:

```python
def assign_material(obj, material):
    # TODO: Assign the material to the object
    # Hint: Use cmds.select and cmds.hyperShade
```

> [!note] Task
> Complete the `assign_material` function. Why do you think we're using a separate function for this? Comment your thoughts.

> [!tip] Function Design
> Creating separate functions for distinct tasks (like material creation and assignment) is a good practice in programming. It makes your code more modular and easier to maintain. This concept is part of the "Single Responsibility Principle".

### Step 5: Create the colored primitive function

Add this function to your script:

```python
def create_colored_primitive(shape_type, size, name=None, color=(1,1,1)):
    # TODO: Create a primitive and assign a color material to it
    # Use the functions you've already created
```

> [!note] Task
> Implement the `create_colored_primitive` function using the other functions you've created. How does this function demonstrate modularity in programming? Add a comment discussing this.

> [!info] Modularity in Programming
> Modularity is a key concept in software design. It involves breaking down a program into smaller, manageable parts (modules or functions) that can work independently. Learn more:
> [Modular Programming](https://www.geeksforgeeks.org/modular-approach-in-programming/)

### Step 6: Create the asset listing function

Add this new function to your script:

```python
def list_assets():
    assets = []
    for shape_type in SHAPE_TYPES:
        assets.extend(cmds.ls(f"{shape_type}_*"))
    if assets:
        print("Assets in the scene:")
        for asset in assets:
            print(f"- {asset}")
    else:
        print("No assets found in the scene.")
```

> [!note] Task
> Implement the `list_assets` function. What strategy will you use to identify assets created by your script? Comment on your approach.

> [!tip] Naming Conventions
> Using a consistent naming convention for your created assets can make them easier to identify and manage. Consider how you might incorporate this into your `create_primitive` function.

### Step 7: Create a main function to test your script

Add this function to the end of your script:

```python
def main():
    # TODO: Create at least one of each type of colored primitive (i.e. create_colorrd_primitive(args*))
    # Then, call list_assets() to show what you've created

if __name__ == "__main__":
    main()
```

> [!note] Task
> Complete the `main` function to test all aspects of your script. Why is it important to have a testing function like this? Add a comment with your thoughts.

> [!info] The `if __name__ == "__main__":` Idiom
> This is a common Python idiom. It allows you to execute code when the script is run directly, but not when it's imported as a module. Learn more:
> [What does if __name__ == "__main__": do?](https://www.theserverside.com/tip/What-does-the-Python-if-name-equals-main-construct-do#:~:text=to%20the%20console.-,The%20if%20__name__%20%3D%3D%20%22__main__%22%3A,it%20would%20not%20execute%20automatically.)

### Bonus Challenge (OPTIONAL) 🌟
Modify the `create_colored_primitive` function to randomly position the shape within a 5x5 unit grid on the ground plane (XZ plane in Maya). 

> [!note] Task
> Implement this functionality and explain in comments how you approached this problem and why you made certain decisions.

> [!tip] Random Number Generation in Python
> You'll need to use Python's random module for this challenge. Here's a quick reference:
> [Python Random Module](https://docs.python.org/3/library/random.html)

### Running Your Script

To run your script in Maya:

1. Open Maya and go to Script Editor (Windows > General Editors > Script Editor)
2. In a new Python tab, type:
   ```python
   import asset_creator
   import importlib
   importlib.reload(asset_creator)
   asset_creator.main()
   ```
3. Click the "Execute" button or press Ctrl+Enter (Cmd+Enter on Mac)

> [!warning] Script Location
> Make sure your `asset_creator.py` file is in a location where Maya can find it (like the default scripts folder for maya under `Documents>maya>2025>scripts`. You might need to add its directory to Maya's Python path.

> [!NOTE] Using MayaCode
> You can also use the MayaCode (VS Code) workflow we covered in class to also run the script that way.

---
## --- **WEEK 4** ---

For week 4, we'll extend our asset creation tool to support external configuration, making it more flexible for artists to customize without modifying the main script.

> [!info] What is JSON?
> JSON (JavaScript Object Notation) is a lightweight data format that's easy for humans to read and write, and easy for machines to parse and generate. It's commonly used for configuration files and data exchange between different systems.

### New Requirement
Create a JSON configuration file that defines the available shape types, their default sizes, and default colors. We'll create a new script that reads this configuration and uses your existing `asset_creator.py` to create assets.

### Step 1: Create a Configuration File

Create a new file named `asset_config.json` with the following content:

```json
{
  "shapes": {
    "cube": {
      "default_size": 1.0,
      "default_color": [1.0, 0.0, 0.0]
    },
    "sphere": {
      "default_size": 1.5,
      "default_color": [0.0, 1.0, 0.0]
    },
    "cylinder": {
      "default_size": 1.2,
      "default_color": [0.0, 0.0, 1.0]
    },
    "cone": {
      "default_size": 1.0,
      "default_color": [1.0, 1.0, 0.0]
    }
  }
}
```

> [!note] Understanding JSON Syntax
> - JSON data is written as name/value pairs
> - Data is separated by commas
> - Curly braces {} hold objects
> - Square brackets [] hold arrays
> - In this example, "shapes" is an object containing multiple shape objects, each with its own properties

> [!tip] JSON Validators
> You can use online JSON validators to check if your JSON is correctly formatted. Try pasting the above JSON into [JSONLint](https://jsonlint.com/) to see how it works.

### Step 2: Create a New Script

Create a new file named `config_asset_creator.py` with the following content:

```python
import os
import json
import asset_creator

print("Config Asset Creator script loaded!")

def read_config(config_file='asset_config.json'):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(script_dir, config_file)
    with open(config_path, 'r') as f:
        return json.load(f)

def create_assets_from_config():
    config = read_config()
    for shape, details in config['shapes'].items():
        size = details['default_size']
        color = tuple(details['default_color'])
        name = f"{shape}_from_config"
        asset_creator.create_colored_primitive(shape, size, name, color)

def main():
    create_assets_from_config()
    asset_creator.list_assets()

if __name__ == "__main__":
    main()
```

> [!note] Script Overview
> 
> This script automates asset creation in Maya based on a JSON config file:
>  Importing `asset_creator` gives us access to the function defined in our first script.
> 	 - This is a good practice to have separation of function handling
> 	 - This is how you chare data between scripts
> 
> 1. **read_config()**: Loads the JSON config file.
> 
> 2. **create_assets_from_config()**:
>    - Reads the config
>    - For each shape, calls `asset_creator.create_colored_primitive()`
> 
> 3. **main()**: Orchestrates the process and lists created assets.
> 
> This structure keeps the script modular: config reading here, Maya operations in `asset_creator`.

> [!note] Working with JSON in Python
> - The `json.load()` function reads a JSON file and converts it into a Python dictionary
> - We can then access the data using standard Python dictionary syntax
> - For example, `config['shapes']` gives us the dictionary of all shapes

### Step 3: Test Your New Script

To test your new script in Maya:

1. Ensure `asset_creator.py` ,`config_asset_creator.py`, and `asset_config.json` are in Maya's Python path in the same directory.
	- _You can pass in your VS Code project directory path as a custom Maya script path by following the guide below._
2. In Maya's Script Editor, run:

```python
import sys
import importlib

# Import and reload your custom modules
import config_asset_creator
import asset_creator
importlib.reload(config_asset_creator)
importlib.reload(asset_creator)

# Run the main function
config_asset_creator.main()
```

> [!note] Adding a Custom Path to Maya's sys.path and Importing Modules
> ```python
> import sys
> import importlib
> 
> # Add the path to your custom scripts
> scripts_path = r"C:\Path\To\Your\Scripts"
> if scripts_path not in sys.path:
>     sys.path.append(scripts_path)
> 
> # Import your custom module
> import your_custom_module
> 
> # If you've already imported the module before and want to reload it
> importlib.reload(your_custom_module)
> 
> # Now you can use functions from your custom module
> your_custom_module.some_function()
> ```
> 
> This code does the following:
> 1. Imports necessary modules (`sys` and `importlib`)
> 2. Defines the path to custom scripts
> 3. Adds the path to `sys.path` if it's not already there
> 4. Imports the custom module
> 5. Optionally reloads the module if it was previously imported
> 6. Allows usage of functions from the custom module
> 
> Remember to replace `"C:\Path\To\Your\Scripts"` with your actual script path, and `your_custom_module` with your module's (python script) name.

### Step 4: Reflect on the Changes

> [!note] Task
> After implementing and testing these changes, answer the following questions in comments at the end of your `config_asset_creator.py` file:
> 1. How does using a configuration file make the asset creation process more flexible?
> 2. What are the benefits of keeping the configuration separate from the main asset creation logic?
> 3. Can you think of other aspects of asset creation that could be controlled through the configuration file?

### Bonus Challenge (OPTIONAL)
Add a new shape type to your `asset_config.json` file (for example, a torus). You don't need to implement the creation of this new shape, just add it to the configuration file and explain in a comment how you would extend the `asset_creator.py` script to support this new shape.

> [!info] Learning Resources for JSON
> Here are some resources to help you understand JSON better:
> 1. [JSON Crash Course](https://www.youtube.com/watch?v=GpOO5iKzOmY) - A quick video introduction to JSON
> 2. [W3Schools JSON Tutorial](https://www.w3schools.com/js/js_json_intro.asp) - A comprehensive text-based tutorial
> 3. [Python JSON module documentation](https://docs.python.org/3/library/json.html) - Official Python docs on working with JSON

---
## Submission 📤

Zip all deliverables into a folder titled `[username]_3-4_AssetCreationAndConfig` (replace [username] with your Drexel username) and submit via the course learning portal by the end of Week 4.

Your submission should include:
1. Your completed `asset_creator.py` file from Week 3
2. Your new `config_asset_creator.py` file from Week 4
3. Your `asset_config.json` file from Week 4

Example filename: `dkw34_3-4_AssetCreationAndConfig.zip`

> [!quote] Encouragement
> This two-part assignment challenges you to not just write code, but to think critically about tool development in a game production context. As you work through creating assets and implementing configuration systems, consider the reasons behind each decision you make. 
> 
> You're building fundamental skills in Maya scripting and modular code design, then extending those skills to create more flexible and customizable tools using JSON configuration - a technique widely used in game development and other software fields.
> 
> Remember, there's often more than one way to solve a problem in programming. Don't hesitate to experiment and ask questions if you get stuck. This assignment is building important problem-solving skills that will serve you well in your career as a technical artist or game designer or anything else really...
> 
> Don't worry if some concepts seem complex at first - with practice, you'll find that these techniques make it much easier to create powerful, flexible tools. Keep pushing yourself, stay curious, and enjoy the process. You're well on your way! 🎨🖥️🚀