# Quick Reference: Running Python in Maya

This reference provides a quick overview of four different ways to run Python scripts in Autodesk Maya. We'll use a simple example of creating a cube with custom dimensions.

## Example Task: Create a Cube with Custom Dimensions

Here's a simple Python script to create a cube in Maya with specific dimensions:

```python
import maya.cmds as cmds

cmds.polyCube(width=2, height=3, depth=4)
```

This script creates a cube with width 2, height 3, and depth 4.

## 1. VS Code with MayaCode Plugin

> [!tip] **Requirements**
> - MayaCode plugin installed in VS Code
> - Maya running with command port open

### Opening the Correct Ports for "Send to Maya" Commands (Maya 2022 and Above)

> [!note] **Reconnect Port After Restart**
> Each time Maya is closed and reopened, the command port needs to be reconnected.

To open the correct ports in Maya, use the following code in the MEL tab of the Script Editor:

```mel
commandPort -name "localhost:7001" -sourceType "mel" -echoOutput;
```

Note: If you're using a MayaCode extension version higher than 0.9, MEL and Python code use the same port in Maya.

1. Open the script in VS Code.
2. Ensure that the MayaCode plugin is correctly configured and connected to your running instance of Maya.
3. Right-click in the editor for the script and hit `Send Python Code to Maya` to run the code in the already open Maya editor..

## 2. Copying Code to Maya Script Editor (Python)

> [!note] **Steps**
> - Maya's Script Editor can be accessed via `Windows > General Editors > Script Editor`.

1. Open Maya's Script Editor.
2. Copy the Python code into the Script Editor's Python tab.
3. Click the **Execute** button (or press **Ctrl + Enter**) to run the code.

## 3. Using MayaPy in Command Line (Bash)

> [!warning] **MayaPy Path** You need to use the path to the `mayapy` executable, which is usually located in Maya's installation directory. The default path for Maya on Windows is:
> 
> `C:\Program Files\Autodesk\Maya<version>\bin\mayapy.exe`
> 
> Replace `<version>` with the version number of Maya you have installed (e.g., `2022`).

1. Save your script to a `.py` file, e.g., `create_cube.py`.
2. Open your terminal and navigate to the directory containing your script.
3. Run the following command:

   ```bash
"C:\Program Files\Autodesk\Maya<version>\bin\mayapy.exe" create_cube.py
   ```

   Replace `<version>` with the actual version of Maya you are using.

## 4. Appending Script Directory to Maya and Importing as a Module

> [!example] **Append Path and Import**
> Useful if you want to reuse the script multiple times.

1. Save your script to a file, e.g., `create_cube.py`.
2. Open Maya's Script Editor and use the following code to append the script directory to the system path and import it:

   ```python
   import sys
   sys.path.append('/path/to/your/script_directory')
   
   import create_cube
   create_cube.create()  # Assuming your script contains a `create()` function
   ```

   Make sure to replace `'/path/to/your/script_directory'` with the actual path to the directory containing your script. DO NOT Include the script name in the directory path.

---

Feel free to use whichever method fits your workflow best. This reference should make it easy for you to experiment with Python scripting in Maya!

