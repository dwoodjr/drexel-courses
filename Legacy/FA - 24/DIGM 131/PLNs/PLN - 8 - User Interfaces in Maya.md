# PLN Week 8: Building a PyQt UI for "Primitive Creator" in Maya 2024-2025

##
---
---
## Introduction

Welcome to Week 8! This week, you will be building a user interface for creating Maya polygon primitives using PyQt and Qt Creator. We'll expand on the concepts you've learned so far, incorporating what you've already experienced with Python, PyQt, and integrating UIs into Maya.

By the end of this tutorial, you'll have built a fully functional "Primitive Creator" tool that can add different polygon primitives like cubes, spheres, cylinders, and more into Maya directly from your PyQt-based UI.

### Learning Objectives:
- Understand how to design a UI using Qt Creator.
- Learn to connect UI components to functionality in Maya using PyQt and Python.
- Apply Object-Oriented Programming (OOP) concepts to make your code more extensible, flexible, and maintainable.

### Requirements:
- Maya 2024-2025
- Qt Creator (for creating the UI)
- PySide Installed
	- PySide2 for Maya 2023 - 2024
	- PySide6 for Maya 2025 +

##
---
## Step-by-Step Tutorial: Creating the Primitive Creator UI

### Step 1: Setting Up the Environment
1. **Install Qt Creator**: You will need Qt Creator to create the `.ui` file for the UI design. Make sure you have Qt Creator installed and ready to go.
	1. Install Link: [Qt Creator Offline Installer](https://www.qt.io/offline-installers)

   > [!TIP]
   > Qt Creator is an IDE that allows you to visually design UIs. It's a very user-friendly tool that will help you design the interface without writing all the code manually.

### Step 2: Design the UI in Qt Creator
1. **Launch Qt Creator**: Start Qt Creator and create a new form. Select `File > New File...`
	1. Select `Qt`
	2. Select `Qt Widgets Designer Form`. Then click `Choose...` at the bottom
	3. In the next window, select `Widget` (leave everything else default). Click `Next >`
	4. In the next window, give your .ui file a name (no spaces!) and save it a directory you can access.
	   Click `Next >`
	5. On the next window, do NOT select a project (leave everything default). Click `Finish`

   > [!TIP]
   > The `Widget` template provides a full-featured window that is a blank canvas. This is perfect for building any custom UIs.

1. **Setup the UI Widget Layout**
	- Select your blank canvas, in the `Widget Box` to the right select a Layout (Vertical or Grid are good options). 
	  Drag it onto your canvas.
	- For this layout to take we need to "assign it" to the canvas. In the top item bar, with the icons, select the layout you chose from the side (match the icons).

![[layout.png]]

1. **Add Widgets**:
   - **Add a `QComboBox`**:
     - In the widget panel on the left, find the `QComboBox` widget and drag it onto the main window.
       *Make sure to place widgets inside the layout!*
     - The `QComboBox` will allow users to select which type of primitive they want to create (e.g., Cube, Sphere, Cylinder, etc.).
     - Once added, rename the `QComboBox` to `primitiveComboBox` in the properties panel on the right. *This will make it easier to reference in your code*.
       - Objects can be renamed by either double-clicking the name in the `Object Inspector` (on the right) OR by changing the "objectName" in the `Property Editor`(on the right).
   
> [!NOTE]
> A `QComboBox` is a dropdown menu that allows the user to choose one option from a list. We use it here so that users can easily select which type of primitive they want to create.

> [!error] Resizing in Qt Creator
> The application will try and force the best sizing when using a layout, this can be very frustrating and limiting at times. One way to get around this is to use multiple layouts for each section of your UI. For instance, have a single `Vertical Layout` box for the "title" area with a `Label` and some `Horizontal Lines`. Then, have another `Vertical Layout` for the "primitive selection" area (with the QComboBox) from above. For this to work you will need to break the top QWidget layout: Right-click the `QWidget` and go to `Layout > Break Layout`
> ![[multipleLayout.png]]


   - **Add a `QPushButton`**:
     - Find the `QPushButton` widget and drag it below the `QComboBox`.
     - Rename the button to `createPrimitiveButton` and change its text to "Create Primitive".
     - This button will be used to trigger the creation of the selected primitive in Maya.

> [!TIP]
> A `QPushButton` is a clickable button. We use it here to let the user tell Maya to create the selected primitive when they click it.

   - **Add Labels for Clarity**:
     - Add a `QLabel` above the `QComboBox` with the text "Select Primitive Type:".
     - This will make your UI more intuitive for the user.

3. **Save the UI File**: Save your `.ui` file.

   > [!IMPORTANT]
   > Make sure to save your `.ui` file in the same directory as your Python script, so it's easy to load later.

   > [!TIP]
   > The `.ui` file is an XML representation of the UI you just created. This file will be loaded by Python to generate the UI in Maya.


> [!attention] Restore the main QWidet Layout
> Once you are happy with the layout opf your UI  sections. It is a good idea to restore a layout for the parent/main QWidget object. 
> Right-click the `QWidget` and go to `Layout > <Choose a suitable option...>` (like Vertical or Grid)

### Step 3: Writing the Python Script to Load the UI in Maya
1. **Set Up the Python Script**:
   - Create a new Python file named `primitive_creator_ui.py`.
   - Import the necessary modules:
 ```python
import maya.cmds as cmds
import maya.OpenMayaUI as omui
from PySide6 import QtCore, QtWidgets
from PySide6.QtUiTools import QUiLoader
from shiboken6 import wrapInstance
 ```

> [!CONTEXT]
> - `QtWidgets` is part of PyQt and provides the widgets we need.
> - `cmds` is Maya's command module, which we use to create primitives.
> - `wrapInstance` and `omui` are used to embed our PyQt UI into Maya's interface.

2. **Applying Object-Oriented Programming Concepts**
   - To make our code more extensible, flexible, and maintainable, we will organize our script using classes, inheritance, and polymorphism.

   - Define a base class `PrimitiveCreatorBase` which serves as the abstract layer:
 ```python
class PrimitiveCreatorBase:
    def create_primitive(self, primitive_type):
       raise NotImplementedError("This method should be implemented by subclasses")
 ```

> [!NOTE]
> The `PrimitiveCreatorBase` class is abstract. It defines a method `create_primitive()` that must be implemented by any subclass. This helps enforce consistency in how primitives are created.

> [!error] Install PySide 6
> Python, when installed, may not install PySide when it is downloaded. To ensure that it is installed on your machine. Open a Terminal/CMD window and run the command `pip install pyside6`. Wait for it to complete the installation process, then close the window. This should ensure that the correct version of pyside is installed for this exercise.
> ![[pipInstallPyside.png]]


> [!attention] Pyside Version
> Please note, any individuals using `Maya 2024` *or older* will need to use Pyside2 and Shiboken2. So, install the correct version for the version of Maya you are running. `pip install pyside2`.
 ```python
import maya.cmds as cmds
import maya.OpenMayaUI as omui
from PySide2 import QtCore, QtWidgets
from PySide2.QtUiTools import QUiLoader
from shiboken2 import wrapInstance
 ```


   - Define a subclass `MayaPrimitiveCreator` that inherits from `PrimitiveCreatorBase`:
 ```python
class MayaPrimitiveCreator(PrimitiveCreatorBase):
	PRIMITIVE_COMMANDS = {
		'Cube': cmds.polyCube,
		'Sphere': cmds.polySphere,
		'Cylinder': cmds.polyCylinder,
		'Cone': cmds.polyCone,
		'Torus': cmds.polyTorus
	}

	def create_primitive(self, primitive_type):
		create_command = self.PRIMITIVE_COMMANDS.get(primitive_type)
		if create_command:
			create_command()
		else:
			cmds.warning('Unknown primitive type')
 ```

> [!TIP]
> This class provides a concrete implementation of the `create_primitive()` method, allowing us to handle each primitive type in Maya.

3. **Define the UI Class**:
   - Define the `PrimitiveCreatorUI` class to load the UI and integrate the primitive creation functionality:
 ```python
class PrimitiveCreatorUI(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(PrimitiveCreatorUI, self).__init__(parent)

        # Specify the absolute path to the UI file
        ui_file_path = r"PATH TO UI FILE"  # Update this to the actual path of your main.ui file. INCLUDE THE FILE NAME IN PATH

        # Load the UI file
        ui_file = QtCore.QFile(ui_file_path)
        if not ui_file.exists():
            cmds.error(f"UI file not found: {ui_file_path}")
            return

        ui_file.open(QtCore.QFile.ReadOnly)
        loader = QUiLoader()
        self.ui = loader.load(ui_file, self)
        ui_file.close()

        self.ui.setParent(self)
        self.primitive_creator = MayaPrimitiveCreator() # Create an instance of MayaPrimitiveCreator

        #Signal to connect the button to the create_primitive method
        self.ui.createPrimitiveButton.clicked.connect(self.create_primitive)

    def create_primitive(self):
        #Signal to get the current text from the combobox and pass it to the create_primitive method
        primitive_type = self.ui.primitiveComboBox.currentText()
        self.primitive_creator.create_primitive(primitive_type)
 ```

> [!NOTE]
> - The `__init__` method initializes the UI and creates an instance of `MayaPrimitiveCreator` to handle primitive creation.
> - This structure uses composition by including a `MayaPrimitiveCreator` instance within `PrimitiveCreatorUI`.

### Step 4: Launch the UI in Maya
1. **Instantiate and Show the UI**:
   - At the end of `primitive_creator_ui.py`, add the following code to launch the UI in Maya:
 ```python
def show_primitive_creator():
    global primitive_creator_ui

    # Close any existing UI instance if it exists
    try:
        primitive_creator_ui.close()
        primitive_creator_ui.deleteLater()
    except:
        pass

    # Create and show the UI
    primitive_creator_ui = PrimitiveCreatorUI()
    primitive_creator_ui.show()
 
 if __name__ == '__main__':
    show_primitive_creator()
 ```

   > [!TIP]
   > This block of code ensures that only one instance of the UI is open at any time. If the UI is already open, it closes it before opening a new instance.

### Step 5: Adding Primitive Options to UI

1. **Add Primitive Types to the QComboBox**:
    - Go back to Qt Creator and add items to the `QComboBox` list by right-clicking on the `primitiveComboBox` and selecting `Edit Items...`.
    - Add all of the primitives we defined in our script by name (e.g., "Cube", "Sphere", "Cylinder", "Cone", "Torus").
> [!TIP] By adding these items, you ensure that users have all the options available that match the primitives handled in the script. This also makes the UI more user-friendly and consistent.

![[addItems.png]]
### Step 6: Creating a Loading Script for Maya

1. **Create a Script to Load the Tool in Maya**:
    - To run our script in Maya (and make a custom shelf tool button), we will need a script to load and run the files we just created (`primitive_creator_ui.py` and the `.ui`).
    - Create a new Python file named `load_tool.py`.
    - Add the following code to load the script as a module in Maya and execute it:
``` python
import sys
project_path = r"PATH TO SCRIPT DIRECTORY"  # Update this to the actual path of your script directory
if project_path not in sys.path:
	sys.path.append(project_path)

import importlib
import primitive_creator_ui
importlib.reload(primitive_creator_ui)
primitive_creator_ui.show_primitive_creator()
```
> [!NOTE] This script sets up the environment to load the primitive creator as a Maya tool. Update `PATH TO SCRIPT DIRECTORY` to the location where you saved your files. Once this script is created, you can use it to add a custom button to Maya's shelf to quickly access your tool.

> [!warning] File Name for Module
> It is important to note that the module being imported by `import` and the`importlib` statements needs to match the file name of the python file hosting the code for maya commands. So in this case it should be `primitive_creator_ui`. But check you file name!

### Step 7: Testing and Creating a Custom Shelf Tool in Maya

#### Step 7.1: Testing and Final Touches
- **Test Your UI**: Load the `load_tool.py` script code into a *Python Tab* in Maya's script editor and run it.
  - Make sure that selecting each primitive type from the combo box and clicking "Create Primitive" creates the correct type of polygon primitive in Maya.

  > [!TIP]
  > Testing is crucial to make sure that everything works as expected. If something doesn't work, use `print()` statements to debug the issue.

  > [!question] 
  > Think about adding more features, such as the ability to set the number or dimensions for each primitive. This will make your tool more versatile and useful.

#### Step 7.2: Creating a Custom Shelf Tool in Maya
1. **Add a Shelf Button for Your Tool**:
   - Once you've successfully tested the script, you can create a custom shelf button in Maya to easily access your tool.
   - Open Maya's Script Editor and go to the *Python Tab*.
   - Copy and paste the following code into the editor:
 ```python
project_path = r"PATH TO SCRIPT DIRECTORY"  # Update this to the actual path of your script directory
if project_path not in sys.path:
	sys.path.append(project_path)

import importlib
import primitive_creator_ui
importlib.reload(primitive_creator_ui)
primitive_creator_ui.show_primitive_creator()
 ```
   - Highlight all of the code and middle-mouse drag it to your desired shelf.

   > [!TIP]
   > You can also add an icon to your shelf button by right-clicking on it and selecting "Edit...". Adding an icon helps make your tools easily recognizable.

![[shelfEditor.png]]

2. **Test the Shelf Tool**:
   - Click on your new shelf button to verify that it loads the "Primitive Creator" UI as expected.
   - If there are any issues, return to the Script Editor and check for errors. Debug as needed to ensure the tool runs smoothly.

   > [!NOTE]
   > Adding your tool as a shelf button allows you to access it quickly without having to run the script from the Script Editor every time. It also makes your workflow more efficient and user-friendly.

### Tips:
- Refer to the example files (`assignment2.py` and `main.ui`) for guidance.
- Make sure your UI is intuitive and easy for the user to navigate.
##
---
## Wrap-Up and Tool Extension LAB Preview

### Today's Key Takeaways
- We learned how to create a custom UI in Qt Creator and integrate it with Maya using PyQt.
- We applied Object-Oriented Programming concepts to make our tool more maintainable and scalable.
- We successfully created a shelf button in Maya to quickly access our Primitive Creator tool.

### Preview: Extending the Primitive Creator Tool
As we've seen today, there's much more that can be done using Maya commands for primitives. For example, you could add functionality to set dimensions or even create custom materials for each primitive.

In the **Lab Session**, you'll be working on extending the tool we just made to add some additional features, like setting primitive dimensions or applying colored materials. This is an opportunity to make your tool even more powerful and user-friendly.
#### Example UI Wireframe for Extended Primitive Creator Tool
Take a look at this example wireframe for the extended tool UI:

```
+------------------------+
|    Primitive Creator   |
+------------------------+
| Type:   [Cube    ▾]    |
| Name:   [         ]    |
| Size:   [1.0      ]    |
|                        |
| [Create Primitive]     |
|                        |
| Select Material:       |
| [Lambert        ▾]     |
|                        |
| [Choose Color]         |
+------------------------+
| [Create Primitives]    |
+------------------------+
```

> [!EXTRA]
> Think about how adding features like material selection or size input could make your tool more versatile. Consider how these options might also help a user build an entire scene more efficiently.

