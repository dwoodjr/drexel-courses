# Level Blockout Tool for Maya + Unity Using Python: Part I

## Introduction

Welcome to Week 9! This week, you will be expanding on your level blockout tool in Maya by creating two new tools: a **Level Blockout Helper** and a **Level Blockout Data Exporter**. These tools will help us to connect Maya an Unity workflows, allowing for seamlessly transferring blockout data between the two platforms.

By the end of this tutorial, you’ll be able to:
1. Create Multiple grouped primitives for a level blockout in Maya.
2. Export blockout data from Maya into a JSON file.

### Learning Objectives:
- Understand how to extract data from Maya objects using Python.
- Learn to structure and write data to a JSON file.
- Begin to grasp connecting workflows between Maya and Unity, forming a pipeline for game development.

### Requirements:
- **Software**:
    - Maya 2024-2025 (or later)
    - Visual Studio Code (as the scripting IDE)
- **Python Tools**:
    - PySide Installed for Maya scripting:
        - PySide2 for Maya 2023-2024
        - PySide6 for Maya 2025+

## Overview
### Part 1
In this part, you will enhance the existing Maya Primitive Creator tool to make it more useful for level blockouts. We will:
1. Add the ability to create multiple primitives at once.
2. Implement a feature to group primitives with a user-specified name.
3. Enable setting dimensions for all primitive types, with an option for random ranges.
### Part 2
In this part, you will create a simple Python script in Maya to export your level blockout data into a **JSON file**. This file will then be imported into Unity using the `Unity Blockout Builder`.
1. Understand how to read data from selected objects in Maya.
2. Export that data (position, scale, type, and group) into a structured format (JSON).
3. Set the foundation for interoperating between Maya and Unity.

##
---
---
## Part 1: Enhancing the Primitive Tool

### Step 1: Creating Multiple Primitives

#### Create Multiple Primitives
**Objective A.** Add an input field to the UI for the number of primitives to create. 
**Objective B.** Update the `create_primitive` method to handle multiple instances.
**Objective C.** Update the creation code to connect to the new UI.

---
##### Objective A
1. Open your `main.ui` file in Qt Creator. Create a new `Layout` section for the crating the number of primitives. 
2. In this new layout add a `Spinbox`. Change its object name to "countSpinBox".
	1. It may also be a good idea to add a label and line to better organize the section
> [!tip] Break main QWidget Layout
> Remember, it may make designing the layout easier if you temporarily break the layout of the top `QWidget` object.
> `Right-click (the object) > Layout > Break Layout`

![[primNum.png]]

---
##### Objective B
Locate the `create_primitive` method in `MayaPrimitiveCreator` class:
Add a new function right above it. This Function will help create unique object names for multiple primitives.
```python
    def get_unique_name(self, base_name, index):
        """Generate a unique name by incrementing until an unused name is found"""
        while True:
            name = f"{base_name}_{index}"
            if not cmds.objExists(name):
                return name
            index += 1
```

Now, look at the `create_primitive` method in `MayaPrimitiveCreator` class:
```python
    def create_primitive(self, primitive_type):
        create_command = self.PRIMITIVE_COMMANDS.get(primitive_type)
        if create_command:
            primitive = create_command()[0]
            return primitive
        else:
            cmds.warning('Unknown primitive type')
```

Update and rename it to handle multiple creations:
```python
    def create_primitives(self, primitive_type, count=1):
        created_primitives = []
        create_command = self.PRIMITIVE_COMMANDS.get(primitive_type)
        if create_command:
            for i in range(count):
                # Create primitive with default dimensions first
                primitive = create_command()[0]
                # Get a unique name for this primitive
                unique_name = self.get_unique_name(primitive_type, i+1)
                new_name = cmds.rename(primitive, unique_name)
                created_primitives.append(new_name)
            return created_primitives
        else:
            cmds.warning('Unknown primitive type')
```

---
##### Objective C
To connect the new "Count" input field (`countSpinBox`) to the Python script:

1. **Add UI Reference for `countSpinBox`**: In the `PrimitiveCreatorUI` class, locate the `__init__` method. Add a reference to the new `countSpinBox` field from the UI:
   ```python
self.countSpinBox = self.ui.countSpinBox  # Reference the spinbox for primitive count
   ```
1. **Update the `create_primitive` Method**: Replace the existing `create_primitive` connection with a new `create_primitives_with_color` method to support creating multiple primitives:
   ```python
   self.ui.createButton.clicked.connect(self.create_primitives_with_color)
   ```
2. **Create the `create_primitives_with_color` Method**: Add the following method to handle multiple primitive creations based on the UI input:
   > [!warning] Replace `create_primitive`
> This new function is replacing the old `create_primitive` function found in the `PrimitiveCreatorUI`class.
```python
    # Function for creating multiple primitives and applying material
    def create_primitives_with_color(self):
        primitive_type = self.ui.primitiveComboBox.currentText()
        material_type = self.ui.materialComboBox.currentText().lower()
        count = self.countSpinBox.value()

        # Create the material with a unique name
        material_name = cmds.shadingNode(material_type, asShader=True, name=f"{material_type}_{primitive_type}")
        # Create a new shading group with a unique name
        shading_group = cmds.sets(name=f"{material_name}SG", empty=True, renderable=True, noSurfaceShader=True)
        # Connect shader to shading group
        cmds.connectAttr(f"{material_name}.outColor", f"{shading_group}.surfaceShader", force=True)

        # Set the color if one is selected
        color = self.ui.chooseColorButton.property("selectedColor")
        if color and color.isValid():
            red, green, blue = color.redF(), color.greenF(), color.blueF()
            if cmds.attributeQuery('color', node=material_name, exists=True):
                cmds.setAttr(f"{material_name}.color", red, green, blue, type="double3")
            if material_type in ["blinn", "phong"]:
                # Set specular color for Blinn and Phong
                cmds.setAttr(f"{material_name}.specularColor", 0.5, 0.5, 0.5, type="double3")

        # Create primitives
        maya_primitive_creator = MayaPrimitiveCreator()
        created_primitives = maya_primitive_creator.create_primitives(primitive_type, count)

        # Assign material to primitives
        if created_primitives:
            for primitive in created_primitives:
                # Ensure we're assigning to the shape node
                shapes = cmds.listRelatives(primitive, shapes=True, fullPath=True)
                if shapes:
                    cmds.sets(shapes[0], edit=True, forceElement=shading_group)

            cmds.confirmDialog(
                title="Success",
                message=f"Created {count} {primitive_type}(s) with {material_type} material.",
                button=["OK"]
            )
        else:
            cmds.warning("No primitives were created. Check the primitive type.")
```

---
#### Testing and Debugging for Step 1

1. **Verify UI Changes**:
   - Open the UI in Maya. Ensure the spinbox is visible and properly labeled.
   - Change the spinbox value and confirm it updates correctly.

2. **Primitive Creation Tests**:
   - Test creating a single primitive to confirm no regressions.
   - Test creating multiple primitives (e.g., 3 or 5 of the same type).
   - Check the naming convention: each primitive should have a unique suffix (e.g., `Sphere_1`, `Sphere_2`, ...).

3. **Error Handling**:
   - Select a type that doesn't exist (if possible) to test the `cmds.warning` message.

> [!info]
> **Debugging Tip**: Use the Maya Script Editor to check for warnings or errors during execution.

---
---
### Step 2: Adding Grouping Functionality

#### Add Grouping Feature
**Objective A.** Add an input field to the UI for the group name.  
**Objective B.** Update the `create_primitives` method to support grouping.  
**Objective C.** Connect the new group name field and update the creation logic.

---
##### Objective A
1. Open your `main.ui` file in Qt Creator.  
2. Create a new `Layout` section for grouping primitives.  
3. Add a `LineEdit` widget to allow users to specify the group name.  
   - Change the object name to `groupNameLineEdit`.
   - Add a label (e.g., "Group Name") for clarity.  

> [!tip] Break Main Layout Temporarily  
> It may make designing the layout easier if you temporarily break the layout of the top `QWidget` object.  
> `Right-click (the object) > Layout > Break Layout`.

![[grpName.png]]

---
##### Objective B
Locate the `create_primitives` method in the `MayaPrimitiveCreator` class:
```python
    def create_primitives(self, primitive_type, count=1):
        created_primitives = []
        create_command = self.PRIMITIVE_COMMANDS.get(primitive_type)
        if create_command:
            for i in range(count):
                primitive = create_command()[0]
                new_name = cmds.rename(primitive, f"{primitive_type}_{i+1}")
                created_primitives.append(new_name)
            return created_primitives
        else:
            cmds.warning('Unknown primitive type')
```

Extend it (and rename it) to group the created primitives under a user-defined group name:
```python
    def create_primitives_and_group(self, primitive_type, count=1, group_name=None):
        created_primitives = []
        create_command = self.PRIMITIVE_COMMANDS.get(primitive_type)
        if create_command:
            for i in range(count):
                # Create primitive with default dimensions first
                primitive = create_command()[0]
                # Get a unique name for this primitive
                unique_name = self.get_unique_name(primitive_type, i+1)
                new_name = cmds.rename(primitive, unique_name)
                created_primitives.append(new_name)

            if group_name:
                # Also ensure group name is unique
                if cmds.objExists(group_name):
                    group_index = 1
                    while cmds.objExists(f"{group_name}_{group_index}"):
                        group_index += 1
                    group_name = f"{group_name}_{group_index}"
                cmds.group(created_primitives, name=group_name)
            return created_primitives
        else:
            cmds.warning('Unknown primitive type')
```

---

##### Objective C
To connect the new "Group Name" field (`groupNameLineEdit`) to the Python script:

1. **Add UI Reference for `groupNameLineEdit`**:  
   In the `PrimitiveCreatorUI` class, locate the `__init__` method. Add a reference to the new `groupNameLineEdit` field from the UI:
   ```python
   self.groupNameLineEdit = self.ui.groupNameLineEdit  # Reference the line edit for group name
   ```

3. **Modify the `create_primitives_with_color` Method**:  
   Add to this method to create and group primitives based on the user input:
   ```python
# Function for creating multiple primitives, applying material, and grouping
def create_primitives_with_color(self):
    primitive_type = self.ui.primitiveComboBox.currentText()
    material_type = self.ui.materialComboBox.currentText().lower()
    count = self.countSpinBox.value()
    group_name = self.groupNameLineEdit.text()  # Get group name from the UI

    # Create the material with a unique name
    material_name = cmds.shadingNode(material_type, asShader=True, name=f"{material_type}_{primitive_type}")
    
    # Create a new shading group with a unique name
    shading_group = cmds.sets(name=f"{material_name}SG", empty=True, renderable=True, noSurfaceShader=True)
    
    # Connect shader to shading group
    cmds.connectAttr(f"{material_name}.outColor", f"{shading_group}.surfaceShader", force=True)

    # Set the color if one is selected
    color = self.ui.chooseColorButton.property("selectedColor")
    if color and color.isValid():
        red, green, blue = color.redF(), color.greenF(), color.blueF()
        if cmds.attributeQuery('color', node=material_name, exists=True):
            cmds.setAttr(f"{material_name}.color", red, green, blue, type="double3")
        if material_type in ["blinn", "phong"]:
            # Set specular color for Blinn and Phong
            cmds.setAttr(f"{material_name}.specularColor", 0.5, 0.5, 0.5, type="double3")

    # Create primitives
    maya_primitive_creator = MayaPrimitiveCreator()
    created_primitives = maya_primitive_creator.create_primitives_and_group(primitive_type, count, group_name)

    # Assign material to primitives and group them if a group name is provided
    if created_primitives:
        for primitive in created_primitives:
            # Ensure we're assigning to the shape node
            shapes = cmds.listRelatives(primitive, shapes=True, fullPath=True)
            if shapes:
                cmds.sets(shapes[0], edit=True, forceElement=shading_group)

        # If a group name is provided, create a group and parent the primitives
        if group_name:
            cmds.group(created_primitives, name=group_name)

        # Provide feedback to the user
        message = f"Created {count} {primitive_type}(s) with {material_type} material."
        if group_name:
            message += f" All primitives are grouped under '{group_name}'."
        cmds.confirmDialog(
            title="Success",
            message=message,
            button=["OK"]
        )
    else:
        cmds.warning("No primitives were created. Check the primitive type.")

   ```

---
#### Testing and Debugging for Step 2

1. **Verify UI Changes**:
   - Open the UI in Maya. Ensure the "Group Name" field is visible and properly labeled.
   - Test entering a group name and leaving it blank.

2. **Group Creation Tests**:
   - Test creating primitives with and without a group name.
   - Verify that primitives are correctly parented to the group in the Outliner.

3. **Naming Conflicts**:
   - Test entering the same group name multiple times to check for Maya's behavior in handling conflicts.

4. **Error Handling**:
   - Leave fields blank or enter invalid inputs to ensure warnings appear in the Maya Script Editor.
---
---
### Step 3: Adding Custom Dimensions with Randomization

#### Add Custom Dimension Fields
**Objective A.** Add input fields to the UI for custom dimensions and randomization options.  
**Objective B.** Update the `create_primitives_with_color` method to handle dimensions.  

---
##### Objective A
1. Open your `main.ui` file in Qt Creator.
2. Create a new `Layout` section for custom dimensions. Add the following elements:
   - Three `DoubleSpinBox` widgets (one each for X, Y, and Z dimensions). Name them:
     - `dimXSpinBox`
     - `dimYSpinBox`
     - `dimZSpinBox`
   - A `CheckBox` for enabling randomization. Name it `randDimsCheckBox`.
   - Three additional `SpinBox` pairs (Min/Max) for random dimensions:
     - `minDimXSpinBox` and `maxDimXSpinBox`
     - `minDimYSpinBox` and `maxDimYSpinBox`
     - `minDimZSpinBox` and `maxDimZSpinBox`

> [!tip] UI Layout Organization  
> Add labels for clarity (e.g., "Dimension X", "Random Min X", "Random Max X") and arrange the widgets in rows for better readability.

![[dims.png]]

---
##### Objective B
Update the **`create_primitives_with_color`** method to include dimension handling:

> [!warning] Import Random
> It is important to note that you must import the `random` module at the top of the script (above the other module imports).
> ```python
> import random
> ```

```python
    # Function for creating multiple primitives, applying material, grouping, and setting dimensions
    def create_primitives_with_color(self):
        primitive_type = self.ui.primitiveComboBox.currentText()
        material_type = self.ui.materialComboBox.currentText().lower()
        count = self.countSpinBox.value()
        group_name = self.groupNameLineEdit.text()  # Get group name from the UI
        randomize = self.ui.randDimsCheckBox.isChecked()  # Check if randomization is enabled

        # Create the material with a unique name
        material_name = cmds.shadingNode(material_type, asShader=True, name=f"{material_type}_{primitive_type}")
        shading_group = cmds.sets(name=f"{material_name}SG", empty=True, renderable=True, noSurfaceShader=True)
        cmds.connectAttr(f"{material_name}.outColor", f"{shading_group}.surfaceShader", force=True)

        # Set the color if one is selected
        color = self.ui.chooseColorButton.property("selectedColor")
        if color and color.isValid():
            red, green, blue = color.redF(), color.greenF(), color.blueF()
            if cmds.attributeQuery('color', node=material_name, exists=True):
                cmds.setAttr(f"{material_name}.color", red, green, blue, type="double3")
            if material_type in ["blinn", "phong"]:
                cmds.setAttr(f"{material_name}.specularColor", 0.5, 0.5, 0.5, type="double3")

        # Determine dimensions
        if randomize:
            dimX = (self.ui.minDimXSpinBox.value(), self.ui.maxDimXSpinBox.value())
            dimY = (self.ui.minDimYSpinBox.value(), self.ui.maxDimYSpinBox.value())
            dimZ = (self.ui.minDimZSpinBox.value(), self.ui.maxDimZSpinBox.value())
        else:
            dimX = self.ui.dimXSpinBox.value()  # Just get the single value
            dimY = self.ui.dimYSpinBox.value()
            dimZ = self.ui.dimZSpinBox.value()

        # Create primitives
        maya_primitive_creator = MayaPrimitiveCreator()
        created_primitives = maya_primitive_creator.create_primitives_and_group(primitive_type, count, group_name)

        # Assign material and dimensions to primitive
        if created_primitives:
            for primitive in created_primitives:
                # Assign material
                shapes = cmds.listRelatives(primitive, shapes=True, fullPath=True)
                if shapes:
                    cmds.sets(shapes[0], edit=True, forceElement=shading_group)

                # Apply dimensions based on primitive type
                if randomize:
                    x_val = random.uniform(*dimX)
                    y_val = random.uniform(*dimY)
                    z_val = random.uniform(*dimZ)
                else:
                    x_val = dimX  # Use the single value directly
                    y_val = dimY
                    z_val = dimZ

                # Get the construction history node
                history = cmds.listHistory(primitive)
                construction_node = next((node for node in history if cmds.nodeType(node).startswith('poly')), None)

                if construction_node:
                    if primitive_type == 'Cube':
                        cmds.setAttr(f"{construction_node}.width", x_val)
                        cmds.setAttr(f"{construction_node}.height", y_val)
                        cmds.setAttr(f"{construction_node}.depth", z_val)
                    elif primitive_type == 'Sphere':
                        radius = x_val / 2
                        cmds.setAttr(f"{construction_node}.radius", radius)
                    elif primitive_type == 'Cylinder':
                        cmds.setAttr(f"{construction_node}.radius", x_val / 2)
                        cmds.setAttr(f"{construction_node}.height", y_val)
                    elif primitive_type == 'Cone':
                        cmds.setAttr(f"{construction_node}.radius", x_val / 2)
                        cmds.setAttr(f"{construction_node}.height", y_val)
                    elif primitive_type == 'Torus':
                        cmds.setAttr(f"{construction_node}.radius", x_val / 2)
                        cmds.setAttr(f"{construction_node}.sectionRadius", y_val / 4)

            # Group primitives if a group name is provided
            if group_name:
                cmds.group(created_primitives, name=group_name)

            # Provide feedback to the user
            message = f"Will create {count} {primitive_type}(s) with {material_type} material."
            if group_name:
                message += f" All primitives will be grouped under '{group_name}'."
            cmds.confirmDialog(
                title="Confirm Creation",
                message=message,
                button=["OK"]
            )
        else:
            cmds.warning("No primitives were created. Check the primitive type.")
```

---
#### Testing and Debugging for Step 3

1. **Fixed Dimensions**:
   - Enter specific values for X, Y, Z dimensions and ensure primitives are scaled accordingly.

2. **Random Dimensions**:
   - Enable randomization, set min/max ranges, and confirm that generated primitives have varied scales within the range.

3. **Combination Tests**:
   - Test fixed dimensions with grouping.
   - Test random dimensions with material assignment.

4. **Error Handling**:
   - Leave fields blank or input invalid values to check for proper warnings.

**Here is what the full UI in Qt Creator might look like:**
![[fullUI.png]]

##
---
---
## Part 2: Level Blockout Exporter Tool

### Step 1: Setup

#### 1. Create the Python Script

1. In Vs Code, create a new Python script called `level_blockout_exporter.py

First, we must define a function to get the dimension values of our primitives and assign them as "Scale" values. 
1. Add the following code to the script
   ```python
import maya.cmds as cmds
import json
import os

def get_primitive_dimensions(obj, shape_node):
    """Get the actual dimensions of the primitive from its construction history"""
    history = cmds.listHistory(obj)
    construction_node = next((node for node in history if cmds.nodeType(node).startswith('poly')), None)
    
    if not construction_node:
        return [1.0, 1.0, 1.0]  # Default scale if no construction history
        
    node_type = cmds.nodeType(construction_node)
    
    if node_type == 'polyCube':
        width = cmds.getAttr(f"{construction_node}.width")
        height = cmds.getAttr(f"{construction_node}.height")
        depth = cmds.getAttr(f"{construction_node}.depth")
        return [width, height, depth]
    elif node_type == 'polySphere':
        radius = cmds.getAttr(f"{construction_node}.radius")
        return [radius * 2, radius * 2, radius * 2]
    elif node_type in ['polyCylinder', 'polyCone']:
        radius = cmds.getAttr(f"{construction_node}.radius")
        height = cmds.getAttr(f"{construction_node}.height")
        return [radius * 2, height, radius * 2]
    elif node_type == 'polyTorus':
        radius = cmds.getAttr(f"{construction_node}.radius")
        section_radius = cmds.getAttr(f"{construction_node}.sectionRadius")
        return [radius * 2, section_radius * 2, radius * 2]
        
    return [1.0, 1.0, 1.0]  # Default scale if type not recognized
   ```

> [!hint] Looking Ahead
> This is an important step as it relates to the functionality of the `Unity Blockout Importer` script we will build next week.

Next, we will need to actually write the data gathered from each primitive into JSON format.
2. Add the following function to the script
```python
def export_level_blockout(file_path=None):
    selected_objects = cmds.ls(selection=True, long=True) # This gets the selected objects
    if not selected_objects: # This checks if no objects are selected
        cmds.warning("No objects selected! Please select the primitives to export.") # This is a warning that will be shown if no objects are selected
        return # This returns if no objects are selected

    blockout_data = [] # This initializes an empty list to store the blockout data

    for obj in selected_objects:
        shape = cmds.listRelatives(obj, shapes=True, fullPath=True) # This gets the shape of the object
        if not shape: # This checks if the shape exists
            cmds.warning(f"Skipping {obj}, no shape found.") # This is a warning that will be shown if the shape does not exist
            continue


        # Get the construction history to determine primitive type
        history = cmds.listHistory(obj) # This gets the history of the object
        construction_node = next((node for node in history if cmds.nodeType(node).startswith('poly')), None) # This gets the construction node of the object
        if construction_node:
            node_type = cmds.nodeType(construction_node)
            primitive_type = {
                'polyCube': 'Cube',
                'polySphere': 'Sphere',
                'polyCylinder': 'Cylinder',
                'polyCone': 'Cone',
                'polyTorus': 'Torus'
            }.get(node_type, 'Unknown')
        else:
            primitive_type = 'Unknown'


        # Get object attributes
        position = cmds.xform(obj, query=True, worldSpace=True, translation=True) # This gets the position of the object
        
        # Get dimensions instead of scale
        dimensions = get_primitive_dimensions(obj, shape[0]) # This gets the dimensions of the object
        parent = cmds.listRelatives(obj, parent=True, fullPath=True) # This gets the parent of the object
        group_name = parent[0] if parent else None # This gets the name of the group

        # Append object data (structure of the data)
        blockout_data.append({
            "type": primitive_type,
            "position": position,
            "scale": dimensions,  # Using dimensions instead of transform scale
            "group": group_name
        })

    # Write to JSON
    try:
        with open(file_path, 'w') as json_file: # This opens the JSON file for writing
            json.dump(blockout_data, json_file, indent=4) # This writes the blockout data to the JSON file
        cmds.confirmDialog( # This confirms the export was successful
            title="Export Successful",
            message=f"Level blockout exported to {file_path}",
            button=["OK"]
        )
    except Exception as e:
        cmds.error(f"Failed to write to {file_path}: {e}") # This is an error that will be shown if the export fails
```

Lastly, we need to execute the functions and save the JSON file to a directory we can access.
3. Add this last bit of code to the end of the script
```python
if __name__ == "__main__":
    # Replace with your desired file path (make sure to include the file and extension)
    file_path = r"path_to_export\blockout_data.json"
    export_level_blockout(file_path)
```
> [!info] File Path
> Replace `"C:/path_to_export/blockout_data.json"` with a valid file path on your system.


---

### Step 2: Testing the Exporter

#### 1. Setup Your Scene
1. Use the Level Blockout Tool from Part 1 to create and group some primitives.
2. Move the primitives around Maya to create a simple test "blockout".
3. Select the primitives you want to export.
#### 2. Run the Exporter
1. Back in VS Code us the MayaCode extension to execute the script.
	1. Or use any of the other methods we have covered in the class. Including copying the script into Maya Script Editor.
3. Run the script

> [!note] Understanding the Code
> **Selection**: The script reads all selected objects in Maya.
> **Attributes**: For each object, it collects:
> 	`type`: Whether it's a Cube, Sphere, etc.
> 	`position`: The object's position in world space.
> 	`scale`: The object's dimensions.
> 	`group`: The name of its parent (if it has one).
> **JSON Writing**: The script saves the data to a file in JSON format.
---

### Step 3: Verifying the Exported Data

1. Open the exported file (`blockout_data.json`) in a text editor like **Notepad++** or in **Visual Studio Code**.
2. Verify the structure. It should look similar to this:
   ```json
   [
       {
           "type": "Cube",
           "position": [0, 0, 0],
           "scale": [2, 1, 1],
           "group": "BlockoutGroup"
       },
       {
           "type": "Sphere",
           "position": [5, 0, 0],
           "scale": [1, 1, 1],
           "group": "BlockoutGroup"
       }
   ]
   ```

> [!error] Debugging and Common Errors
> 1. **No Objects Selected**:
> 	1. Ensure you've selected the objects in Maya before running the script.
> 2. **Incorrect File Path**:
> 	1. Check the file path in the `export_level_blockout` call.
> 	2. Use double backslashes (`\\`) for Windows paths.
> 3. **Empty or Incorrect JSON**:
> 	1. Verify the scene contains valid primitives (e.g., Cube, Sphere).
> 	2. Check Maya's **Script Editor** for warnings or errors.

> [!tip]
> Save and organize your Maya scenes and JSON files for future reference. We will need them next week.

##
---
---
