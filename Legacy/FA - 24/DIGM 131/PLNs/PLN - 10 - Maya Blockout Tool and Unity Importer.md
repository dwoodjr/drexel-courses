# Level Blockout Tool for Maya + Unity Using Python: Part II

## Introduction

Welcome to Week 10! This week, you will be connecting your Maya level blockout tool JSON data export to Unity via a new script, the ***Blockout Data Importer***. This tools will help us to connect Maya an Unity workflows and complete our tooling pipeline, allowing for seamlessly transferring blockout data between the two platforms.

By the end of this tutorial, you’ll be able to:
1. Import multiple level blockouts into a default Unity 3D scene.
### Learning Objectives:
- Learn to convert data from a JSON file.
- Learn how to use Unity's Python Scripting Package
- Learn of to transfer valuable game level construction data between software. 
-  See how to connect workflows between Maya and Unity, forming a complete pipeline for game development.

### Requirements:
- **Software**:
    - Maya 2024-2025 (or later)
    - Visual Studio Code (as the scripting IDE)
    - Unity 2022.3.XXf1 LTS
- **Python Tools**:
    - JSON Module:
    - Unity Python Scripting Package

## Overview

### Part 1
In this step, you will build a **Unity Blockout Importer** tool using Python. This tool will:
1. Read the JSON file exported from Maya (via the Level Blockout Exporter).
2. Use the data to dynamically create placeholder objects (cubes, spheres, etc.) in Unity.
3. Organize the imported objects under a parent GameObject.

##
---
---
## Part 1: Unity Blockout Importer Tool

### Step 1: Setting Up Python in Unity

#### 1. Create a Unity Project (Unity Version 2022.3.X)
Install the Unity Hub and create a new Unity project:
1. Create the project using the which version of 2022.3.Xf1 is available.
2. To create a new project, open the Unity Hub and hit `New Project`.
3. Use the default 3D settings and save the project.
#### 2. Enable Python in Unity
Ensure Unity’s Python for Unity package is installed:
1. Open Unity and go to **Window > Package Manager**.
2. In the Package Manager switch to `Packages: Unity Registry` (Top left of the window)
3. Search for **Python Scripting** in the Package Manager and install it.
#### 3. Create a Folder for the Tool
1. In Unity, create a folder in the **Assets** directory called `Scripts`.
2. Inside `Scripts`, create a new Python script file named `blockout_importer.py`.

---

### Step 2: Writing the Unity Importer Script

Open `blockout_importer.py` in your Python editor (e.g., VS Code). Paste the following script:

```python
import UnityEngine as ue
import json
import os

class BlockoutImporter:
    def __init__(self, file_path):
        self.file_path = file_path

    def import_blockout(self):
    
        # Verify the file exists
        if not os.path.exists(self.file_path):
            ue.Debug.LogError(f"File not found: {self.file_path}")
            return

        # Read the JSON file
        with open(self.file_path, 'r') as file:
            blockout_data = json.load(file)

        # Create the parent GameObject for imported data
        parent = ue.GameObject("BlockoutGroup")

        # Iterate through the blockout data and create the primitives
        for obj in blockout_data:
            obj_type = obj.get("type", "Cube") # get type, if not found, default to cube
            position = ue.Vector3(*obj["position"]) # Extract the object position from JSON
            scale = ue.Vector3(*obj["scale"]) # Extract the object scale from JSON

            # Create Unity GameObjects for the primitives
            if obj_type == "Cube":
                unity_obj = ue.GameObject.CreatePrimitive(ue.PrimitiveType.Cube)
            elif obj_type == "Sphere":
                unity_obj = ue.GameObject.CreatePrimitive(ue.PrimitiveType.Sphere)
            elif obj_type == "Cylinder":
                unity_obj = ue.GameObject.CreatePrimitive(ue.PrimitiveType.Cylinder)
            elif obj_type == "Cone":
                ue.Debug.LogWarning("Cone type not supported, defaulting to Cylinder")
                unity_obj = ue.GameObject.CreatePrimitive(ue.PrimitiveType.Cylinder)
            elif obj_type == "Torus":
                ue.Debug.LogWarning("Torus type not supported, defaulting to Sphere")
                unity_obj = ue.GameObject.CreatePrimitive(ue.PrimitiveType.Sphere)

            # Set Position of the GameObject
            unity_obj.transform.position = position

            # Set Scale of the GameObject
            scale_values = [float(s) for s in obj["scale"]]
            unity_obj.transform.localScale = ue.Vector3(scale_values[0], scale_values[1], scale_values[2])

            # Set Parent of the GameObject
            unity_obj.transform.parent = parent.transform
        ue.Debug.Log(f"Imported {len(blockout_data)} objects successfully!")

if __name__ == "__main__":
    importer = BlockoutImporter("E:/DIGM131-FA24/Week 9/test/data/blockout_data.json") #Replace with your JSON file path
    importer.import_blockout()
```

---

### Step 3: Running the Unity Importer

#### 1. Preparing the JSON File
Export the level blockout from Maya using the `export_level_blockout` tool. Place the JSON file in your Unity project’s `Assets` folder (e.g., `Assets/blockout_data.json`).

#### 2. Running the Script
1. Open the Python console in Unity (**Window > General >Python Console**).
2. Load the blockout_importer.py file into the Unity python Script Editor
3. Execute the importer script:
	1. Ensure the bottom the the script has a main function and you have correctly replaced the JSON data file path
	   ```python
if __name__ == "__main__": 
	importer = BlockoutImporter("path/to/your/blockout_data.json") # Replace with the path to your JSON file
	importer.import_blockout()
   ```
4. Unity will execute the script, and you should see the imported objects in your scene, organized under a parent GameObject named `BlockoutGroup`.


> [!warning] Object Scale
> Maya and Unity have different default working Units for scale. Unity used *Meters*, Maya uses *Centimeters*. If you blockout is very small be sure to change the default working units in Maya to meters.
> - Refer back to `PLN 9` on how to do this
> - Or just research it (Google), it is easy info to find.


---

### Step 4: Testing and Debugging

#### 1. Verify Imported Objects
- Check the Unity Hierarchy to ensure the objects are grouped under `BlockoutGroup`.
- Verify object types (e.g., Cube, Sphere), positions, and scales.

#### 2. Handle Common Errors
- **File Not Found**: Ensure the JSON file exists in the specified path.
- **Incorrect JSON Structure**: Verify that the exported JSON matches the expected format:
  ```json
  [
      {
          "type": "Cube",
          "position": [0, 0, 0],
          "scale": [1, 1, 1],
          "group": "BlockoutGroup"
      }
  ]
  ```

##
---
---
## What’s Next?

This Unity importer completes the workflow from Maya to Unity! *(for our classes purposes at least)* 
You can now:
1. Export level blockouts from Maya using the Level Blockout Exporter.
2. Import and visualize the blockouts in Unity.
3. Extend the Unity importer to support additional features, such as:
   - Rotational Data (requires updating the both the Primitive Creator and JSON Exporter Scripts to handle rotation data)
   - Assigning materials.
   - Use Unity's `ProBuilder` Package to further blockout and refine level design.

> [!tip]
> Experiment with different blockout setups in Maya and observe how they translate into Unity.
