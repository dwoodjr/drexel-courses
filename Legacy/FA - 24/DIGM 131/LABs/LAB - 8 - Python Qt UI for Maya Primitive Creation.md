# Interactive Lab: Maya Primitive Creator Tool Extension

##
---
---

## 🎯 Objective
Transform our Maya primitive creation tools into an object-oriented system and extend the "Primitive Creator" tool by adding new features such as material selection and a color picker.

## 📚 Pre-lab Preparation
1. Review the Week 8 materials on UI creation.
2. Have Maya 2024/2025 open and ready.
3. Create a new directory for this lab/assignment.

> [!info] OOP Quick Reference
> - [Python Classes Documentation](https://docs.python.org/3/tutorial/classes.html)
> - [Maya Python Commands](https://help.autodesk.com/view/MAYAUL/2024/ENU/?guid=__CommandsPython_index_html)

##
---

## Part 1: Adding Material and Color Picker

### Step 1: Update the UI in Qt Creator

**Add Widgets for Material Selection**:
   - Open your existing `.ui` file in Qt Creator.
   - **Add a `QLabel`** below the "Create Primitive" button with the text "Select Material:".
   - **Add a `QComboBox`** below the label and rename it to `materialComboBox`. This combo box will allow users to select different materials (e.g., Lambert, Phong).

   > [!TIP]
   > Materials define how an object reacts to light. The most common materials in Maya are **Lambert**, **Blinn**, and **Phong**. We'll use these as options in the dropdown.

**Add Widgets for Color Picker**:
   - Add another `QPushButton` below the material combo box. Set the text to "Choose Color" and rename it to `chooseColorButton`. This button will allow the user to open a color picker dialog.

   > [!NOTE]
   > A color picker dialog is a convenient way for users to select a color. This button will trigger the color picker.

3. **Save the Updated UI**: Save the updated `.ui` file.

### Step 2: Modify the Python Script

**Add Material Selection Logic**:
   - In your `PrimitiveCreatorUI` class, add logic to populate the `materialComboBox` with materials.
   - In the `__init__` method, add the following lines:
```python
self.ui.materialComboBox.addItems(["Lambert", "Blinn", "Phong"])
```

   > [!TIP]
   > This adds the material options to the combo box so users can select one before creating the primitive. This version of the implementation is also sets the combo box option in code, instead of in the Qt editor.

**Apply Material and Color to the Created Primitive**:
   - Update the `PrimitiveCreatorUI()` class to apply the selected material and color with their own functions:
```python
class PrimitiveCreatorUI(QtWidgets.QMainWindow):
	# [Previous code as before...]
    
    # Function for creating the primitive and applying material
    def create_primitive(self):
        primitive_type = self.ui.primitiveComboBox.currentText()
        material_type = self.ui.materialComboBox.currentText().lower()

        # Create the primitive
        maya_primitive_creator = MayaPrimitiveCreator()
        primitive = maya_primitive_creator.create_primitive(primitive_type)

        if primitive:
            # Create the material and assign it to the primitive
            material = cmds.shadingNode(material_type, asShader=True)
            cmds.select(primitive)
            cmds.hyperShade(assign=material)
            
            # Get color from UI button property and apply it to the material
            color = self.ui.chooseColorButton.property("selectedColor")
            if color and color.isValid():
                # Set the color of the material using RGB values in the correct range
                cmds.setAttr(f"{material}.color", color.redF(), color.greenF(), color.blueF(), type="double3")

	# [Color selection function code here... (see below)]
```

   > [!TIP]
   > The `shadingNode` command creates a new shader node, and `sets` command creates a shading group to link the shader to the primitive. We then use `setAttr` to apply the RGB color values.


**Add Color Picker Functionality**:
   - Connect the `chooseColorButton` to a new method called `choose_color`:
```python
self.ui.chooseColorButton.clicked.connect(self.choose_color)
```
   - Define the `select_color` method to open a color dialog and store the selected color (This function is a part of the `PrimitiveCreatorUI` class):
```python
    # Function for selecting the color/opening the color picker
	def select_color(self):
		color = QtWidgets.QColorDialog.getColor()
		if color.isValid():
				# Set the button's background to reflect the selected color
				self.ui.chooseColorButton.setStyleSheet(f"background-color: {color.name()}; border: none;")
				# Store the selected color as a property for later use
				self.ui.chooseColorButton.setProperty("selectedColor", color)
```

   > [!NOTE]
   > The `QColorDialog.getColor()` method opens a color picker dialog.

### Step 3: Test the Extended Tool

- **Load the Updated Script**: Load and run the updated `primitive_creator.py` script in Maya using your shelf tool. 
	  *Since we utilized the `load_tool.py` code to make the shelf button, there should be no need to update the shelf tool code, just run it again by clicking on it.*
- **Test Material and Color Selection**: Ensure that selecting a material and color results in a primitive with the correct material and color applied.

   > [!TIP]
   > If something doesn't work, use `print()` statements to debug the values of `material_type` and `selected_color`.

##
---
## Part 2: Assignment - Add One Additional Feature

*Now that you've added material and color options, it's time to extend your tool even further.* Choose **one** of the following features to implement as part of your assignment:

### Additional Features (***Choose One***):
#### Option 1: **Set Dimensions for Primitives**
   - Add input fields (e.g., `QDoubleSpinBox`) to allow users to specify dimensions (e.g., width, height, depth) for the created primitive.
   > [!HINT]
> Reference the Maya commands documentation for `polyCube`, `polySphere`, etc., to see what parameters you can adjust.

#### Option 2: **Add Subdivision Controls**
   - Allow the user to specify the number of subdivisions for each primitive to create smoother geometry.
   > [!HINT]
     > Use `QSpinBox` to let the user set subdivision levels. Check the Maya commands reference for how to apply subdivisions to each primitive type.

#### Option 3:**Custom Transform Options**
   - Add controls to let the user set the initial position, rotation, and scale of the primitive when it's created.
   > [!HINT]
     > You can use `cmds.setAttr()` to set the translation, rotation, or scale attributes of the created primitive. Add fields to the UI for these attributes.

