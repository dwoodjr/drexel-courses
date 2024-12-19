# Final Exam Prep: Level Blockout Project Guide

### **Overview**

In this final exam prep, you will create, complete, and integrate tools and workflows for a Level Blockout system. This pipeline workflow will simulate a potential real-world Tech Art / Technical Direction workflow, creating assets and moving data between DCCs via scripting. This serves as an exercise in understanding scripts and scripting basics. This is also an exercise in planning and developing a dev/design process by first understanding the problem, creating an outline, then executing the tasks.

*Follow the steps below carefully to implement the provided scripts, complete the missing sections, and integrate them with Maya and Unity.*

> [!warning] Maya Version and PySide
> Depending on the version of Maya you are running you may need to adjust the code for the `level_blockout_helper.py` script to use the correct version of PySide for your Maya version.
> 	For Maya 2025+ - PySide6 and shiboken6
> 	For Maya 2023 -2024 - PySide2 and shiboken2

##
---
---
## **Part 1: Directory Creation Script**

### **Objective**

Set up a project directory structure using Python. You'll write a class-based script and complete tasks to understand **modules**, **dictionaries**, and **recursion**.

---
### **Step-by-Step Instructions**

#### Step 1: **Set Up the Script**: 
Create a new file named `directory_creator.py`.
#### Step 2: **Define the Class**: 
The `DirectoryCreator` class will handle directory creation. Below is the partially complete code:
``` python
# TASK: Import the necessary modules for this script.
# Hint: You’ll need to work with the file system and command-line arguments.

class DirectoryCreator:
    def __init__(self, base_dir):
        """
        Initialize the directory creator with the base directory.
        Args:
            base_dir (str): The base directory where the structure will be created.
        """
        self.base_dir = base_dir

        # Define the directory structure as a dictionary.
        self.structure = {
            "External Assets": {
                "Scenes": {},
                "Data": {}
            }
        }

    def create_structure(self):
        """
        Recursively create the directory structure based on the dictionary.
        """
        def create_dirs(base_path, struct):
            for folder_name, sub_struct in struct.items():
                path = os.path.join(base_path, folder_name)
                os.makedirs(path, exist_ok=True)
                create_dirs(path, sub_struct)

        create_dirs(self.base_dir, self.structure)
        print(f"Project structure created at: {self.base_dir}")

```
    
#### Step 3: **Integrate Command-Line Interface**:
Add the command-line interface to initialize and run the class.
``` python
if __name__ == "__main__":
    # TASK: Import the module for parsing command-line arguments.
    # Hint: Look at argparse.

    parser = argparse.ArgumentParser(description="Create External Assets Directory")
    parser.add_argument("base_dir", help="Base directory for the project")
    args = parser.parse_args()

    # Create an instance of DirectoryCreator and call the create_structure method.
    creator = DirectoryCreator(args.base_dir)
    creator.create_structure()

```
    
---

> [!important] Your Tasks
> 
> 1. **Import Modules**:
>     - Add the necessary `import` statements for working with the file system and command-line arguments.
>     - **Hint**: Which module is commonly used for file operations? Which one handles command-line arguments?
> 2. **Test the Script**:
>     - Save the file as `directory_creator.py`.
>     - Run the script in a terminal using:

```python
python directory_creator.py <your_base_directory>
```

- Verify that the following structure is created: 
`External Assets/    
	 Scenes/    
	 Data/
- `Data` folder is where JSON data will be exported to.
- `Scenes` folder is where the Maya Scene will be saved.

> [!info] Need Help?
> 
> - Python Modules: [os](https://docs.python.org/3/library/os.html) and [argparse](https://docs.python.org/3/library/argparse.html).
> - Watch: [How to Use Python Modules](https://www.youtube.com/watch?v=XcfxkHrHTVE).
##
---
---
## **Part 2: Working with the Maya Tool**

### **Objective**

Use the provided `Level Blockout Helper` tool to create and export a blockout in Maya. Demonstrate your understanding of the script's functionality by answering comprehension questions.

---
### **Step-by-Step Instructions**

#### **Step 1: Review the Provided Script**
You have been provided the full **`level_blockout_helper.py`** script. This script:
1. Handles primitive creation, grouping, and material assignment.
2. Connects the functionality to the UI defined in **`main.ui`**.

> ⚠️ **Note**: The script is complete, but you will need to understand its functionality to answer the provided questions.

#### **Step 2: Set Up**
1. Place the following files in a directory accessible to Maya:
    - `level_blockout_helper.py` (a renamed version of the `primitive_creator.py` script from past few weeks)
    - `load_tool.py`
    - `main.ui`
#### **Step 3: Questions for README.md**
To demonstrate your understanding of the script, answer the following questions in a section of your **README.md**:
##### **Understanding the Script**
1. How does the tool determine which primitive type to create?
    - Hint: Look at how the `primitiveComboBox` UI element is accessed.
2. What method ensures that primitives have unique names in the Maya scene?
    - Hint: Review the `get_unique_name` method in `level_blockout_helper.py`.
3. How are random dimensions applied to primitives if the randomization option is checked?
    - Hint: Look at the logic handling the `randDimsCheckBox`.
4. Explain how materials are created and assigned to primitives.
    - Hint: Focus on the use of `cmds.shadingNode` and `cmds.sets`.
5. How does the script handle grouping of created primitives?
    - Hint: Check the logic in the `create_primitives_and_group` method.

---

> [!important] Your Task
> 
> 1. Set up and test the provided `Level Blockout Helper` tool in Maya.
> 2. Answer the provided questions in your **README.md** file to demonstrate understanding of the script.

> [!info] Resources
> 
> - Python Classes and Methods: [Real Python OOP Guide](https://realpython.com/python3-object-oriented-programming/).
> - Maya Commands for Materials: [Maya Command Reference](https://help.autodesk.com/view/MAYAUL/2024/ENU/?guid=__CommandsPython_index_html).

##
---
---
## **Part 3: Testing and Exporting the Level Blockout**

### **Objective**

Test the `Level Blockout Helper` tool in Maya and complete tasks in the `Level Blockout Exporter` script to export blockout data to JSON format.

---

### **Step-by-Step Instructions**

#### **Step 1: Test the Tool in Maya**
1. Run the `load_tool.py` script in Maya to load the `Level Blockout Helper` tool.
	1. Ensure the path in `load_tool.py` is correct (before running in Maya)
```python
project_path = r"E:\DIGM131-FA24\Week 10\test" # Update this to the actual path of your python folder
```
1. Ensure the path to the `main.ui` file in `level_blockout_helper.py` is correct (before running in Maya)
```python
ui_file_path = r"E:/DIGM131-FA24/Week 10/test/main.ui"
```
2. Use the UI to:
    - Create a blockout with primitives.
    - Assign materials and group the objects.
3. Verify the scene in Maya:
    - Ensure the primitives are correctly created and grouped.
    - Check that materials are applied as expected.

#### **Step 2: Complete the Export Script**
The `Level Blockout Exporter` script is partially implemented. Your tasks focus on completing key sections.

##### **Task 1: Define the Primitive Types**
Complete the `PRIMITIVE_TYPES` dictionary in the `PrimitiveData` class. This dictionary maps Maya node types to their corresponding primitive names.
```python
class PrimitiveData:
    PRIMITIVE_TYPES = {
        # TASK: Fill in the mappings for each primitive type.
        'polyCube': 'Cube',
        'polySphere': 'Sphere',
        # Add mappings for 'polyCylinder', 'polyCone', and 'polyTorus'.
    }

```

##### **Task 2: Call Helper Methods**
In the `_add_object_data` method, use the helper methods from the `PrimitiveData` class to retrieve the primitive type and dimensions.
```python
def _add_object_data(self, obj, shape):
    history = cmds.listHistory(obj)
    primitive_type = self.primitive_data.___  # TASK: Call the method to get primitive type.
    dimensions = self.primitive_data.___  # TASK: Call the method to get dimensions.
    position = cmds.xform(obj, query=True, worldSpace=True, translation=True)
    parent = cmds.listRelatives(obj, parent=True, fullPath=True)
    group_name = parent[0] if parent else None

    self.blockout_data.append({
        "type": primitive_type,
        "position": position,
        "scale": dimensions,
        "group": group_name
    })

```

##### **Task 3: Format Strings in Confirmation Messages**
Improve the confirmation dialog message by formatting the file path dynamically.
```python
def _write_to_json(self, file_path):
    try:
        with open(file_path, 'w') as json_file:
            json.dump(self.blockout_data, json_file, indent=4)
        # TASK: Format the confirmation message with the file path.
        cmds.confirmDialog(
            title="___",
            message=f"___",
            button=["OK"]
        )
    except Exception as e:
        cmds.error(f"Failed to write to {file_path}: {e}")

```

##### **Task 4: Format the Export File Path**
In the `export_level_blockout` function, ensure the JSON file is saved in the correct location. Update the `file_path` variable.
```python
if __name__ == "__main__":
    # TASK: Update this file path to point to your Data directory.
    file_name = "blockout_data.json"
    file_path = os.path.join(r"<path_to_your_project>/Data", file_name)  # Replace <path_to_your_project>.
    export_level_blockout(file_path)

```


#### **Step 3: Test the Script**
1. Select all the primitives created in Maya.
2. Run the `Level Blockout Exporter` script (via MayaCode or Copy into Script Editor):
    - Ensure the JSON file is created in the `Data` directory.
3. Inspect the JSON file:
    - Confirm it contains the correct attributes (`type`, `position`, `scale`, `group`) for each object.

---

> [!important] Your Task
> 
> 1. Complete the following tasks in the `Level Blockout Exporter` script:
>     - **Define Primitive Types**: Fill in the missing entries in the `PRIMITIVE_TYPES` dictionary.
>     - **Call Helper Methods**: Use `get_primitive_type` and `get_dimensions` to retrieve object data.
>     - **Format File Path**: Ensure the export file path is correct.
>     - **Format Strings**: Improve the confirmation message with the correct file path.
> 2. Test the script by exporting blockout data and verifying the JSON file.

> [!info] Resources
> 
> - Python Dictionaries: [Real Python Guide](https://realpython.com/python-dictionary-comprehension/).
> - String Formatting: [Python String Formatting](https://docs.python.org/3/tutorial/inputoutput.html).
> - Maya Commands: [Command Reference](https://help.autodesk.com/view/MAYAUL/2024/ENU/?guid=__CommandsPython_index_html).

##
---
---
## **Part 4: Importing Blockout Data into Unity**

### **Objective**

Use the exported JSON data to create a corresponding blockout in Unity. You’ll complete missing sections in the `blockout_importer.py` script to accomplish this.

---

### **Step-by-Step Instructions**

#### **Step 1: Setup Unity Project**
1. Open Unity and create a new project.
2. Add the `Python Scripting` package vis the Unity `Package Manager`.

#### **Step 2: Complete `level_data_importer.py`**
The provided script partially implements importing blockout data into Unity. Your task is to complete the missing sections:

##### **a. Verify JSON File Exists**
Complete the check to ensure the JSON file exists before attempting to load it.

```python
# TASK: Complete the if statement conditional check for an existing JSON file
# Hint: the os module has a check for if a file path "exists"
if not ___:
    ue.Debug.LogError(f"File not found: {self.file_path}")
    return

```

##### **b. Create GameObjects**
Complete the logic to instantiate GameObjects for each primitive type.

```python
if obj_type == "Cube":
	unity_obj = ue.GameObject.CreatePrimitive(ue.PrimitiveType.Cube)
elif obj_type == "Sphere":
	unity_obj = ue.GameObject.CreatePrimitive(ue.PrimitiveType.Sphere)
# TASK: Handle Cylinder, and unsupported types of Cone and Torus here.
# Hint: Use ue.Debug.LogWarning() to log warnings.
# Hint: What primitives are available in Unity that are similar to the ones in Maya?

```

##### **c. Set Position, Scale, and Parenting**
Ensure each object is correctly positioned, scaled, and parented under the main group object.

```python
unity_obj.transform.position = ___ # TASK: Set position, JSON data for "position"
unity_obj.transform.localScale = ___ # TASK: Set scale, JSON data for "scale"
unity_obj.transform.parent = parent.transform  # Parent under BlockoutGroup

```

#### Step 4. Verity Path and Test
Verify that the path to teh JSON data file in the importer script is the correct path
```python
    importer = BlockoutImporter("E:/DIGM131-FA24/Week 9/test/data/blockout_data_test.json") #Replace with your JSON file path
```

Test the script by running in in the `Python Console` within the Unity Editor

---

> [!important] Your Task
> 
> 1. Complete the missing sections of `blockout_importer.py`:
>     - Verify the JSON file exists.
>     - Create GameObjects for each primitive type.
>     - Set position, scale, and parent the objects appropriately.
> 2. Test the script by running it in Unity.

> [!info] Resources
> 
> - Unity Scripting API: [GameObject Class](https://docs.unity3d.com/Manual/class-GameObject.html).
> - Video: [Importing Data into Unity](https://www.youtube.com/watch?v=2B3D7tcWm9g).

##
---
---
## Part 5.A: **README.md Requirements**

### **Objective**

The **README.md** file is an essential part of your submission. It serves as documentation for your workflow, explanations of your scripts, and answers to comprehension questions.

---

### **Structure of README.md**

Your **README.md** file should be structured as follows:

#### **1. Project Overview**
Provide a brief summary of the project:
- What the project is about.
##### Example:

> **Project Overview**  
> This project involves creating and exporting a blockout in Maya using a custom tool, then importing the blockout into Unity. The tool includes features for creating primitives, assigning materials, grouping objects, and exporting data.


#### **2. Scripts and Workflow**
Explain the purpose of each script and how it contributes to the project:
1. **`directory_creator.py`**: Automates the creation of the project directory structure.
2. **`level_blockout_helper.py`**: Manages primitive creation, material assignment, and grouping in Maya.
3. **`level_blockout_exporter.py`**: Exports blockout data from Maya to JSON format.
4. **`blockout_importer.py`**: Imports JSON data into Unity and creates corresponding objects.


#### **3. Answer the Questions**
Answer the comprehension questions from **Part 2** in this section. Include clear, concise explanations.
##### Example Questions:
2. **What method ensures primitives have unique names?**
    - _Answer_: The `get_unique_name` method iterates through possible names and checks if they already exist using `cmds.objExists`.


#### **4. Challenges and Solutions**
Reflect on any challenges you encountered and how you solved them. Be honest but focus on what you learned.
##### Example:

> **Challenges and Solutions**  
> I struggled with understanding how to connect the UI inputs to the tool’s functionality. By carefully reviewing how the `primitiveComboBox` and `randDimsCheckBox` were accessed, I was able to trace the workflow and debug the tool effectively.


#### **5. Testing Notes**
Document your testing process:
- How you verified the Maya tool functionality.
- How you checked the JSON export file.
- How you confirmed the Unity importer worked as expected.
##### Example:
> **Testing Notes**
> - **Maya**: Created a blockout with multiple cubes and spheres. Verified correct materials and grouping.
> - **JSON**: Inspected the exported file and confirmed it matched the scene data.
> - **Unity**: Imported the JSON and confirmed correct object creation and placement.


##
---
---
## Part 5.B: Preparing for **Submission**

### **Deliverables**

Organize the following in a zipped folder titled `[YourUsername]_FinalExam`:

1. All Python scripts:
    - `directory_creator.py`
    - `level_blockout_helper.py`
    - `level_blockout_exporter.py`
    - `level_blockout_importer.py`
2. JSON file(s) created during export.
4. **README.md** file:
    - ***Includes all required sections and answers to questions.***
5. Screenshots or a screen recording showing:
    - Maya tool in use.
    - Exported JSON file.
    - Imported blockout in Unity.

---
### **Submission Prep Instructions**
1. Zip the folder:  
    Example: `YourUsername_FinalExam.zip`

> [!important] Submission Checklist
> 
> - [ ]  All scripts included.
> - [ ]  Exported JSON file.
> - [ ]  Complete README.md file with all required sections.
> - [ ]  Screenshots or recording of the workflow.

##
---
---