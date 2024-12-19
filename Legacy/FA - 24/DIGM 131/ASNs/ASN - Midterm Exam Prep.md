# Advanced Game Project Setup and Asset Generation - Interactive Guide

## Brief 💼
As a technical artist at Awesome Games Studio, you've been tasked with creating an advanced tool for setting up new game projects and generating initial assets. This tool will streamline the project initialization process and ensure consistency across different game projects.

## Your Mission 🎯
Develop a Python script (or scripts) that:
1. Creates a customizable game project folder structure
2. Generates various game assets using Maya
3. Records (prints statements in code for) the entire process for documentation purposes

## Requirements 📋
1. Create a main Python script named `advanced_project_setup.py` that:
   - Uses `argparse` to accept command-line arguments for the project name and configuration file path
   - Reads a JSON configuration file to determine folder structure and asset details
   - Creates the specified folder structure
   - Uses Maya commands to generate at least 5 different types of primitive assets with varying properties
   - Generates a final report summarizing the project setup and assets created

2. Create a `config.json` file that defines:
   - The folder structure for the game project
   - Details for each asset to be generated (type, dimensions, color, etc.)

3. Use appropriate comments and docstrings to explain your code's functionality

## Constraints and Considerations
- Use only Python concepts and the Maya Commands Reference covered in class (Weeks 1-4)
- Your script should be flexible enough to handle different project structures and asset configurations
- Consider how to make your code modular and reusable.


> [!attention] Companion Guide
> This assignment has a companion study guide that reviews and reinforces fundamental python and programming basics as they pertain to the midterm. It is titles `Python and Programming Basics for the Midterm Exam`. You are encouraged to complete this assignment and reference that guide as you work, and most certainly after you have completed this series of tasks in order to get a better grasp on the subject matter.

---
## Part 1: Setting Up the Configuration File

Let's start by creating our `config.json` file. Here's a basic structure:

```json
{
  "folder_structure": [
    "Assets",
    "Scenes",
    "Scripts",
    "Textures",
    "Materials"
  ],
  "assets": {
    "cube": [
      {"name": "SmallCube", "dimensions": [1, 1, 1], "color": [1, 0, 0]},
      {"name": "LargeCube", "dimensions": [2, 2, 2], "color": [0, 1, 0]}
    ],
    "sphere": [
      {"name": "SmallSphere", "radius": 0.5, "color": [0, 0, 1]},
      {"name": "LargeSphere", "radius": 1.5, "color": [1, 1, 0]}
    ]
  }
}
```

> [!important] Your Task
> 1. Add a new folder called "Documentation" to the folder_structure.
> 2. Add three new Maya primitives to the assets: a cylinder, a cone, and a torus. Each should have at least two instances with different properties.
> 3. For the new primitives, think about what properties they need (e.g., height and radius for cylinder). This a good point to look at the Maya Commands Reference

> [!info] JSON in Python
> JSON (JavaScript Object Notation) is a lightweight data interchange format that is easy for humans to read and write and easy for machines to parse and generate. In Python, we can use the `json` module to work with JSON data.
> 
> - Video: [Working with JSON in Python](https://www.youtube.com/watch?v=9N6a-VLBa2I)
> - Reference: [Python JSON](https://docs.python.org/3/library/json.html)

---
## Part 2: Implementing the Main Script

Now, let's implement our `advanced_project_setup.py` script. We'll go through each function step by step.

### Importing Required Modules

```python
import argparse
import json
import maya.cmds as cmds
import maya.standalone
maya.standalone.initialize(name='python')
```

> [!important] Your Task
> We're missing an important module that we need for file and directory operations. Add the correct import statement for this module. Explain in a comment why this module is necessary for our script.

> [!info] Python Modules
> Modules in Python are files containing Python definitions and statements. They allow you to organize your code into reusable pieces.
> 
> - Video: [Python Modules](https://www.youtube.com/watch?v=uoVUOTPL9Rw)
> - Reference: [Python Modules](https://docs.python.org/3/tutorial/modules.html)


### Parsing Command-Line **Arguments**

```python
def parse_arguments():
    """
    Parse command-line arguments.
    
    Returns:
        argparse.Namespace: Parsed arguments
    """
    parser = argparse.ArgumentParser(description="Game Project Setup and Asset Generation")
    parser.add_argument("project_name", help="Name of the game project")
    parser.add_argument("config_path", help="Path to the configuration JSON file")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output")
    return parser.parse_args()
```

> [!important] Your Task
> 1. Explain in your own words (in a comment or docstring) what the 'verbose' option does in this script.
> 2. Explain what `action="store_true"` does in the `add_argument` method for the verbose option.
> 3. (*Optional: Requires completion of all steps*) Find all the places in the script where the `verbose` parameter is used. What kind of extra information does it provide?

> [!info] Understanding the 'verbose' Option
> The 'verbose' option is a common feature in scripts that allows for more detailed output. In this script:
> 
> 1. We add a command-line argument `-v` or `--verbose` using `argparse`.
> 2. When this option is used, `args.verbose` becomes `True`.
> 3. We pass this boolean value to functions that can provide extra output.
> 4. These functions use if statements to check if verbose is True before printing extra information.
> 
> This is an advanced feature that you might see in professional scripts. For now, you can think of it as a switch that turns on or off extra print statements in our code.

> [!info] Additional Resources on Command-Line Arguments and Verbose Output
> - [Python argparse Tutorial](https://docs.python.org/3/howto/argparse.html)
> - [Argparse Basics](https://www.youtube.com/watch?v=FbEJN8FsJ9U&t=90s)
> - [Real Python: Command-Line Arguments](https://realpython.com/python-command-line-arguments/)
> - [What is Verbose Mode](https://www.geeksforgeeks.org/what-is-verbose-mode/)

### Loading Configuration

```python
def load_configuration(config_path):
    """
    Load configuration from JSON file.
    
    Args:
        config_path (str): Path to the configuration file
    
    Returns:
        dict: Loaded configuration
    """
    try:
        # The 'with' statement ensures that the file is properly closed after we're done with it,
        # even if an exception occurs.
        with open(config_path, 'r') as config_file:
            # 'json.load()' reads the JSON data from the file and converts it into a Python dictionary
            return json.load(config_file)
    except FileNotFoundError:
        print(f"Error: Configuration file not found at {config_path}")
        return None
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in configuration file {config_path}")
        return None

# Note: The 'with' statement is a context manager in Python. It's used to ensure that a resource is
# properly managed (in this case, that the file is closed after we're done reading from it).
# This is good practice as it prevents resource leaks and makes your code more robust.
```

> [!important] Your Task
> 1. Add a comment explaining why we use `'r'` as the mode when opening the file.
> 2. Implement error handling for a potential `PermissionError` that might occur if the script doesn't have permission to read the file.

> [!info] Understanding PermissionError and Exception Handling
> A `PermissionError` is raised when an operation is not permitted due to a lack of file system permissions. In the context of opening files, this could happen if you try to read a file that you don't have permission to access.
>
> To handle this error, you'll need to add another `except` block to catch `PermissionError`. Here are some resources to help you understand and implement this:
>
> 1. Python Exception Handling Tutorial: [Real Python - Exception Handling](https://realpython.com/python-exceptions/)
> 2. Python PermissionError Documentation: [Python Docs - PermissionError](https://docs.python.org/3/library/exceptions.html#PermissionError)
> 3. Video Tutorial on Python Exceptions: [Python Exception Handling](https://www.youtube.com/watch?v=NIWwJbo-9_8)
>
> Remember, the structure for adding a new exception is:
> ```python
> except PermissionError:
>     # Your error handling code here
> ```
> Think about what message would be helpful for a user to see if this error occurs, and what the function should return in this case.

### Creating Project Structure

```python
def create_project_structure(project_name, folder_structure, verbose=False):
    """
    Create the project folder structure.
    
    Args:
        project_name (str): Name of the project
        folder_structure (list): List of folders to create
        verbose (bool): Whether to print detailed information
    
    Returns:
        str: Path to the created project folder
    """
    project_path = os.path.join(os.getcwd(), project_name)
    os.makedirs(project_path, exist_ok=True)
    for folder in folder_structure:
        folder_path = os.path.join(project_path, folder)
        os.makedirs(folder_path, exist_ok=True)
        if verbose:
            print(f"Created folder: {folder_path}")
    return project_path
```

> [!important] Your Task
> Modify this function to return a list of created folders along with the project path. Here's a step-by-step guide to help you:
> 
> 1. Create an empty list at the beginning of the function to store the paths of created folders.
> 2. Inside the for loop, after creating each folder, add its path to this list.
> 3. At the end of the function, return both the project path and the list of folder paths.
> 4. Update the function's docstring to reflect that it now returns two values.
> 
> Hint: You can return multiple values in Python using a tuple, like this:
> ```python
> return project_path, folder_list
> ```
> 
> Don't forget to update any part of the main script that calls this function to handle the new return value!

> [!info] File and Directory Operations in Python
> The `os` module provides a way of using operating system dependent functionality like creating directories.
> 
> - Video: [Python OS Module](https://www.youtube.com/watch?v=tJxcKyFMTGo)
> - Reference: [OS Module](https://docs.python.org/3/library/os.html)

### Material Creation Function

```python
def create_material(name, color):
    """Create a Lambert material with the specified color."""
    material = cmds.shadingNode('lambert', asShader=True, name=f"{name}_material")
    cmds.setAttr(f"{material}.color", *color, type="double3")
    return material
```

> [!important] Your Task
> Add comments to this function explaining:
> 1. What a Lambert material is and why we're using it.
> 2. What the asterisk (*) does when used with the color parameter in `cmds.setAttr()`.

> [!NOTE] Unpacking Python Arguments
> Reference: [Unpacking Python Arguments](https://docs.python.org/3/tutorial/controlflow.html#unpacking-argument-lists)

> [!info] Lambert Materials
> Lambert materials are a type of basic, matte shader in 3D graphics. They're often used for their simplicity and efficiency in rendering. Understanding different shader types is crucial for technical and material artists working on game assets.

### Material Assignment Function

```python
def assign_material(obj, material):
    """Assign a material to an object."""
    shading_group = cmds.sets(renderable=True, noSurfaceShader=True, empty=True, name=f"{material}_SG")
    cmds.connectAttr(f"{material}.outColor", f"{shading_group}.surfaceShader", force=True)
    cmds.sets(obj, edit=True, forceElement=shading_group)
```

> [!important] Your Task
> Add comments to this function explaining:
> 1. What a shading group is and why it's necessary.
> 2. The purpose of the `cmds.connectAttr()` function in this context.

> [!info] Shading Groups in Maya
> Shading groups in Maya are sets that associate shaders with geometry. They play an important role in how materials are applied to objects in the scene. Understanding this connection is important for creating and managing materials in complex scenes.

### Generating Maya Assets

```python
def generate_maya_assets(asset_config, verbose=False):
    """
    Generate Maya assets based on the configuration.
    
    Args:
        asset_config (dict): Asset configuration dictionary
        verbose (bool): Whether to print detailed information
    """
    created_assets = []
    for asset_type, assets in asset_config.items():
        for asset in assets:
		    try:
	            if asset_type == "cube":
	                obj = cmds.polyCube(w=asset['dimensions'][0], h=asset['dimensions'][1], d=asset['dimensions'][2], n=asset['name'])[0]
	            elif asset_type == "sphere":
	                obj = cmds.polySphere(r=asset['radius'], n=asset['name'])[0]
	            # Add conditions for cylinder, cone, and torus here
	            else:
	                print(f"Unsupported asset type: {asset_type}")
	                continue
			
				# Create and assign material
				material = create_material(asset['name'], asset['color'])
				assign_material(obj, material)
			
			    created_assets.append(obj)
	            if verbose:
		            print(f"Created {asset_type}: {asset['name']} with color: {asset['color']}")
                
		except Exception as e: print(f"Error creating {asset_type} '{asset['name']}': {str(e)}")
	return created_assets	
```

> [!important] Your Task
> Implement the creation of cylinder, cone, and torus assets. Remember to set their properties based on the configuration.

> [!info] Maya Python Commands
> The `maya.cmds` module provides a Python wrapper for Maya's command engine, allowing you to create and manipulate 3D objects programmatically.
> 
> - Video: [Maya Python API Introduction](https://www.youtube.com/watch?v=eXFGeZZbMzQ)
> - Reference: [Maya Python API](https://help.autodesk.com/view/MAYAUL/2024/ENU/?guid=__CommandsPython_index_html)

### Saving the Maya File

```python
def save_maya_scene(project_path, project_name):
    """
    Save the current Maya scene.

    Args:
        project_path (str): Path to the project directory
        project_name (str): Name of the project
    """
    scenes_dir = os.path.join(project_path, "Scenes")
    scene_file = os.path.join(scenes_dir, f"{project_name}.ma")
    cmds.file(rename=scene_file)
    cmds.file(save=True, type="mayaAscii")
    print(f"Saved Maya scene: {scene_file}")
```

>[!info] Why Save the Scene? 
>Saving the Maya scene allows you to open and view the generated assets directly in Maya. This is crucial for verifying the results of your script and for further work on the assets.

### Main Function

```python
def main():
    """
    Main function to run the script.
    """
    args = parse_arguments()
    config = load_configuration(args.config_path)
    if config is None:
        return
    
    project_path = create_project_structure(args.project_name, config['folder_structure'], args.verbose)
    
    generate_maya_assets(config['assets'], args.verbose) # Generate Assets
    
	save_maya_scene(project_path, args.project_name) # Save the Maya Scene to Scenes sub-directory
    
    # Add summary here
    
    if args.verbose:
        print("Project setup completed successfully")
	    
	maya.standalone.uninitialize()
	
if __name__ == "__main__":
    main()
```

> [!important] Your Task
> Add a summary at the end of the `main` function that records how many folders and assets were created. This summary should be printed to the console.

---
## Part 3: Testing and Refinement

> [!attention] Running Maya Scripts in Production
> The method we're about to use represents a more typical approach to running Maya scripts in a production environment. Unlike using the MayaCode extension or saving scripts to Maya's script path, this method allows for:
> 1. Proper use of command-line arguments
> 2. Saving Maya scenes programmatically
> 3. Running Maya in "headless" or batch mode
> 
> This approach is crucial for pipeline integration and automation tasks where Maya's GUI isn't needed or available. It's the standard way to run Maya scripts in many professional settings.
>
> Further reading:
> - [Autodesk: Using Maya in Batch Mode](https://help.autodesk.com/view/MAYAUL/2024/ENU/?guid=GUID-2E5D1D43-DC3D-4CB2-9A35-757598220F22)
> - [Mayapy: The Maya Python Standalone Interpreter](https://help.autodesk.com/view/MAYAUL/2024/ENU/?guid=GUID-D64ACA64-2566-42B3-BE0F-BCE843A1702F)
> - [Running Python Scripts with Mayapy](https://help.autodesk.com/view/MAYAUL/2024/ENU/?guid=Maya_SDK_Maya_Python_API_PythonOutsideMayaSession_html)

To test your script:

1. Open a command prompt (CMD) or terminal.

2. Navigate to the directory containing your script:
   ```
   cd path/to/your/script/directory
   ```

3. Run the script using `mayapy` with the necessary arguments:
   ```
   "C:\Program Files\Autodesk\Maya2025\bin\mayapy.exe" advanced_project_setup.py TestProject config.json -v
   ```
   Replace the path to mayapy.exe with the correct path for your Maya installation, if it's different.

> [!info] Understanding mayapy
> `mayapy` is a standalone Python interpreter that comes with Maya. It includes all of Maya's Python modules and allows you to run Maya Python scripts without opening the Maya GUI. This is useful for automating tasks and running scripts in batch mode.

> [!info] Why Use Command-Line Arguments?
> Command-line arguments allow your script to be flexible and reusable. You can easily change the project name, configuration file, and verbosity without modifying the script itself. This is a common practice in professional pipeline tools.

> [!important] Your Task
> Create test cases with at least 3 different project names and configurations. For different configurations, copy the original config file, rename it and open/edit the values inside. Don't forget to save any changes.
> 
> Document your test results in a README.md file, including:
> 1. The folder structure created for each project
> 2. The Maya assets generated for each configuration
> 3. Any output printed to the console, especially when using the `--verbose` option
> 4. Verify that the Maya scene file is saved in the correct location and can be opened in Maya
> 
> Example test cases:
> ```
> mayapy advanced_project_setup.py ProjectAlpha config.json -v
> mayapy advanced_project_setup.py BetaGame config_beta.json
> mayapy advanced_project_setup.py GammaWorld config_gamma.json -v
> ```

> [!info] Viewing Maya Scenes
> To view the generated Maya scenes:
> 1. Open Maya
> 2. Go to File > Open Scene
> 3. Navigate to your project's Scenes folder
> 4. Open the .ma file created by your script
> 
> Check that all assets are present, correctly positioned, and have the right materials applied.

---
## Reflection

As you complete this assignment, consider the following questions:

1. How does this project incorporate the fundamental programming concepts we've learned?
2. What was the most challenging part of this assignment, and how did you overcome it?
3. How might you extend or improve this script for use in a real game development pipeline?

*Feel free and open to placing the answers to your reflections in your README.md file*

Remember, this assignment is designed to challenge you and prepare you for the midterm exam and real-world development scenarios. Take your time, refer to your notes and resources, and don't hesitate to ask for clarification if needed. Good luck!

---
## Submission 📤

Zip all deliverables into a folder titled `[username]_midtermPrep` (replace [username] with your Drexel username) and submit via the course learning portal under ***Week 5***.

Your submission should include:
1. Your completed `advanced_project_setup.py` file
2. Your new `config.json` file
3. Your `README.md` file

Example filename: `dkw34_midtermPrep.zip`