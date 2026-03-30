# Interactive Lab: Extending Maya Utility Functions

## 🎯 Objective
Extend the `maya_utils.py` script created in the live coding session with advanced functions for grouping objects, printing detailed information, and creating multiple primitives at once.

## 📚 Pre-lab Reading
- [Maya Python API: Creating and Manipulating Objects](https://www.youtube.com/watch?v=eXFGeZZbMzQl) (12 minutes)
- [Maya Python API](https://help.autodesk.com/view/MAYAUL/2023/ENU/?guid=__CommandsPython_index_html) Reference (reference as needed)
- [Python Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions) (10 minutes)

## 🧪 Lab Steps

### Step 1: Review and Setup (10 minutes)
1. Open your `maya_utils.py` file from the live coding session.
2. Ensure it contains the basic functions for creating primitives and assigning colors.
3. Test the existing functions to make sure they're working correctly:

```python
import maya.cmds as cmds
import maya_utils
import importlib
importlib.reload(maya_utils)

# Test create_primitive function
cube = maya_utils.create_primitive("cube", 2)
sphere = maya_utils.create_primitive("sphere", 1.5)

print(f"Created cube: {cube}")
print(f"Created sphere: {sphere}")

# Test create_colored_primitive function
red_cube = maya_utils.create_colored_primitive("cube", 2, "red_cube", (1, 0, 0))
blue_sphere = maya_utils.create_colored_primitive("sphere", 1.5, "blue_sphere", (0, 0, 1))

print(f"Created red cube: {red_cube}")
print(f"Created blue sphere: {blue_sphere}")
```

Run this code in Maya's Script Editor or use your chosen Maya extension to run the code form the IDE. You should see the created objects in your scene and their names printed in the output window.

### Step 2: Implement Object Grouping Function (20 minutes)
1. Add a new function called `group_objects` to `maya_utils.py`:

```python
def group_objects(objects, group_name="new_group"):
    """
    Group the given objects under a new group in Maya.
    
    Args:
    objects (list): List of object names to group.
    group_name (str): Name for the new group.
    
    Returns:
    str: Name of the created group.
    """
    group = cmds.group(empty=True, name=group_name)
    for obj in objects:
        cmds.parent(obj, group)
    return group
```

2. Test this function by creating a few objects and grouping them:

```python
import maya_utils
importlib.reload(maya_utils)

# Create some objects
cube1 = maya_utils.create_primitive("cube", 1)
cube2 = maya_utils.create_primitive("cube", 2)
sphere = maya_utils.create_primitive("sphere", 1.5)

# Group the objects
group_name = maya_utils.group_objects([cube1, cube2, sphere], "my_group")
print(f"Created group: {group_name}")

# Verify in Maya's Outliner that the objects are now under the new group
```

### Step 3: Implement Primitive Info Printing Function (25 minutes)
1. Add a new function called `print_primitive_info` to `maya_utils.py`:

```python
def print_primitive_info(obj_name):
    """
    Print detailed information about a primitive object in Maya.
    
    Args:
    obj_name (str): Name of the object to inspect.
    """
    shape = cmds.listRelatives(obj_name, shapes=True)[0]
    object_type = cmds.objectType(shape)
    
    print(f"Object: {obj_name} (Type: {object_type})")
    
    if object_type == 'polyCube':
        width = cmds.getAttr(f"{shape}.width")
        height = cmds.getAttr(f"{shape}.height")
        depth = cmds.getAttr(f"{shape}.depth")
        print(f"  Size: Width={width}, Height={height}, Depth={depth}")
    
    elif object_type == 'polySphere':
        radius = cmds.getAttr(f"{shape}.radius")
        print(f"  Radius: {radius}")
    
    elif object_type == 'polyCylinder':
        radius = cmds.getAttr(f"{shape}.radius")
        height = cmds.getAttr(f"{shape}.height")
        print(f"  Size: Radius={radius}, Height={height}")
    
    else:
        print("  Unknown primitive type")
```

2. Test this function with different types of primitives:

```python
import maya_utils
importlib.reload(maya_utils)

# Create different primitives
cube = maya_utils.create_primitive("cube", 2)
sphere = maya_utils.create_primitive("sphere", 1.5)
cylinder = maya_utils.create_primitive("cylinder", 1)

# Print info for each primitive
maya_utils.print_primitive_info(cube)
maya_utils.print_primitive_info(sphere)
maya_utils.print_primitive_info(cylinder)
```

### Step 4: Implement Multi-Primitive Creation and Grouping Function (30 minutes)
1. Add a new function called `create_and_group_primitives` to `maya_utils.py`:

```python
def create_and_group_primitives(primitives_data):
    """
    Create multiple primitives, group them, and print their info.
    
    Args:
    primitives_data (list): List of dictionaries, each containing data for a primitive.
                            Each dict should have keys: 'type', 'size', 'name', 'color'
    
    Returns:
    str: Name of the group containing all created primitives.
    """
    created_objects = []
    for data in primitives_data:
        obj = create_colored_primitive(data['type'], data['size'], data['name'], data['color'])
        created_objects.append(obj)
        print_primitive_info(obj)
    
    group_name = group_objects(created_objects, "primitives_group")
    print(f"All objects grouped under: {group_name}")
    return group_name
```

2. Test this function with a list of primitive data:

```python
import maya_utils
importlib.reload(maya_utils)

primitives_data = [
    {"type": "cube", "size": 1, "name": "small_cube", "color": (1, 1, 0)},
    {"type": "sphere", "size": 0.5, "name": "small_sphere", "color": (0, 1, 1)},
    {"type": "cylinder", "size": 0.75, "name": "small_cylinder", "color": (1, 0, 1)}
]

group = maya_utils.create_and_group_primitives(primitives_data)
print(f"Created group: {group}")

# Verify in Maya's Outliner that the objects are created and grouped correctly
```

📝 Reflection Question: How might these new functions be useful in a larger Maya project or pipeline?

### Step 5: Create a Comprehensive Test Script (25 minutes)
1. Create a new Python file named `test_maya_utils.py` in the same directory as your `maya_utils.py`.
2. Add the following content to `test_maya_utils.py`:

```python
import maya.cmds as cmds
import maya_utils
import importlib
importlib.reload(maya_utils)

def test_maya_utils():
    # Clear existing scene
    cmds.file(new=True, force=True)

    # Test individual primitive creation
    cube = maya_utils.create_colored_primitive("cube", 2, "test_cube", (1, 0, 0))
    sphere = maya_utils.create_colored_primitive("sphere", 1.5, "test_sphere", (0, 1, 0))
    cylinder = maya_utils.create_colored_primitive("cylinder", 1, "test_cylinder", (0, 0, 1))

    print("Individual primitives created:")
    maya_utils.print_primitive_info(cube)
    maya_utils.print_primitive_info(sphere)
    maya_utils.print_primitive_info(cylinder)

    # Test grouping
    group_name = maya_utils.group_objects([cube, sphere, cylinder], "test_group")
    print(f"\nGroup created: {group_name}")
    
    # Test multi-primitive creation and grouping
    primitives_data = [
        {"type": "cube", "size": 1, "name": "small_cube", "color": (1, 1, 0)},
        {"type": "sphere", "size": 0.5, "name": "small_sphere", "color": (0, 1, 1)},
        {"type": "cylinder", "size": 0.75, "name": "small_cylinder", "color": (1, 0, 1)}
    ]
    
    multi_group = maya_utils.create_and_group_primitives(primitives_data)
    print(f"\nMulti-primitive group created: {multi_group}")

    # Verify scene contents
    all_objects = cmds.ls(type="transform")
    print("\nAll objects in scene:")
    for obj in all_objects:
        print(obj)

if __name__ == "__main__":
    test_maya_utils()
```

3. Run the test script in Maya's Script Editor:

```python
import test_maya_utils
importlib.reload(test_maya_utils)
test_maya_utils.test_maya_utils()
```

4. Verify that all functions work as expected and that the output in the Script Editor matches what you intended.

---
### Step 6: Reflection and Documentation (15 minutes)
1. Review the output of your test script. Does it demonstrate all the new functionality you've added?
2. Add comments to your `maya_utils.py` file explaining how each function works and how they can be used together.
3. Update the docstrings of your functions if needed, ensuring they accurately describe the function's purpose, parameters, and return values.

📝 Reflection Question: How does creating a comprehensive test script help in developing and maintaining utility functions? What other scenarios might you want to test in a real production environment?

## 🧠 Knowledge Check Quiz
1. What is the purpose of the `group_objects` function?
2. Why is it useful to have a function that prints information about primitives?
3. How does the `create_and_group_primitives` function combine the functionality of other functions?
4. Why is it important to clear the existing scene at the beginning of the test script?
5. How does the test script demonstrate the integration of all the new functions you've created?

## 🏆 Bonus Challenge
Modify the `print_primitive_info` function to include information about the object's material (color). How would you access and print this information?