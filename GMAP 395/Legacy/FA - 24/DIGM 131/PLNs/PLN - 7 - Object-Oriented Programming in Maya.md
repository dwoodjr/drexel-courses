# Code Review Session: Object-Oriented Programming in Maya

## Introduction

***Welcome to Week 7!*** This week marks an important transition in our Python journey as we explore Object-Oriented Programming (OOP) and how it can make our tools more powerful and maintainable. We'll also start the journey to learning how to create professional-looking user interfaces for our tools using `Qt Creator` (but more on that next week).

Building on our previous work with Python 3 and Maya primitives and project automation, we'll see how OOP can help us organize our code better and create more sophisticated tools. By the end of this session, you'll understand how to structure your code using classes and objects, and how we will begin to apply these to create intuitive user interfaces for your tools.

> [!info] Understanding OOP Concepts
> - Video: [Python OOP Tutorial (Corey Schafer)](https://www.youtube.com/watch?v=ZDa-Z5JzLYM)
> - Reference: [Python Classes Documentation](https://docs.python.org/3/tutorial/classes.html)
> - Reference: [W3Schoold - Python Classes + Objects](https://www.w3schools.com/python/python_classes.asp)
> - Video: [OOP in Python Explained](https://www.youtube.com/watch?v=JeznW_7DlB0)


> [!example] Object-oriented Programming in 7 minutes | Mosh
> Let's watch this video, that does an excellent job at breaking down the core concepts: https://www.youtube.com/watch?v=pTB0EiLXUC8


### Session Planning

#### Main Goals for Today
1. Understand OOP concepts and their benefits for tool development
2. Transform our previous Maya utility functions into well-organized classes
3. Learn how classes can prepare us for UI development
4. Begin to think about tool design from a user perspective

#### Breaking Down Our Tasks
1. *What problems are we trying to solve?*
   - Code organization and reusability
   - Making our tools more maintainable
   - Preparing our code for future UI integration

1. What concepts do we need?
   **Main goal**: Transform our Maya tools into organized, reusable classes
   Steps to accomplish this:
	   1. Identify what parts of our tools should be classes
	   2. Design class hierarchies for our tools
	   3. Implement the classes with proper methods
	   4. Test and refine our implementation

1. *How does this build on previous work?*
   - We'll reorganize our primitive creation code into classes
   - We'll structure our code to be UI-ready
   - We'll make our tools more flexible using inheritance

> [!example] Think Like a Developer
> When creating tools for Maya (or any DCC or Game Engine), consider:
> - How will you or other artists use this tool?
> - What functionality needs to be easily accessible?
> - How can we make the tool intuitive?
> - What might need to change in the future?

##
---
---

## Part 1: Understanding Classes with Maya + Python

### From Functions to Classes

Let's start by seeing how we can transform our previous Maya tools into classes. We'll begin with a simple example:

```python
# Our previous approach (Week 3)
def create_cube(size=1, name="cube1"):
    return cmds.polyCube(w=size, h=size, d=size, n=name)[0]

def move_object(obj_name, x=0, y=0, z=0):
    cmds.move(x, y, z, obj_name)

# Using functions
my_cube = create_cube(2, "test_cube")
move_object(my_cube, 0, 3, 0)
```

> [!example] Why This Needs Improvement
> Our current approach has some limitations:
> - Each function operates independently
> - No easy way to track object properties
> - Difficult to maintain related functionality
> - Hard to extend with new features

### Introducing Classes

Let's rewrite this as a class:

```python
import maya.cmds as cmds

class MayaCube:
    """A class to create and manage cube primitives in Maya."""
    
    def __init__(self, name="cube1", size=1.0):
        """Initialize a new cube with name and size."""
        self.name = name
        self.size = size
        self._object = None  # Stores the Maya object name
    
    def create(self):
        """Create the cube in Maya."""
        if self._object is None:  # Only create if it doesn't exist
            self._object = cmds.polyCube(
                n=self.name,
                w=self.size,
                h=self.size,
                d=self.size
            )[0]
            return self._object
    
    def move(self, x=0, y=0, z=0):
        """Move the cube to a new position."""
        if self._object:
            cmds.move(x, y, z, self._object)
    
    def delete(self):
        """Delete the cube from Maya."""
        if self._object and cmds.objExists(self._object):
            cmds.delete(self._object)
            self._object = None

# Using our class
my_cube = MayaCube("test_cube", 2)
my_cube.create()
my_cube.move(0, 3, 0)
```

> [!info] Understanding Classes
> - Video: [Python Classes and Objects](https://www.youtube.com/watch?v=apACNr7DC_s)
> - Reference: [Object-Oriented Programming (OOP) in Python](https://realpython.com/python3-object-oriented-programming/)

### Key Benefits of Using Classes

1. **Organization**
```python
# Without classes (messy, scattered data and functions)
cube1_size = 1
cube1_pos = [0, 0, 0]

def move_cube(cube_name, x, y, z):
    cmds.move(x, y, z, cube_name)

def scale_cube(cube_name, size):
    cmds.scale(size, size, size, cube_name)

# Using these is confusing and error-prone
my_cube = cmds.polyCube()[0]
move_cube(my_cube, 0, 5, 0)
scale_cube(my_cube, 2)

# With classes (everything organized in one place)
class Cube:
    def __init__(self, name, size=1):
        self.name = name
        self.size = size
        self.position = [0, 0, 0]
        self.create()
    
    def create(self):
        self.object = cmds.polyCube(n=self.name, w=self.size, 
                                   h=self.size, d=self.size)[0]
    
    def move(self, x, y, z):
        cmds.move(x, y, z, self.object)
        self.position = [x, y, z]

# Clear and organized usage
my_cube = Cube("cube1", 2)
my_cube.move(0, 5, 0)
```

2. **Reusability**
```python
# Without classes (repetitive code)
cube1 = cmds.polyCube(n="cube1", w=2, h=2, d=2)[0]
cmds.move(0, 2, 0, cube1)

cube2 = cmds.polyCube(n="cube2", w=1, h=1, d=1)[0]
cmds.move(3, 0, 0, cube2)

# With classes (easy to create multiple objects)
class Cube:
    def __init__(self, name, size=1):
        self.name = name
        self.size = size
        self.create()
    
    def create(self):
        self.object = cmds.polyCube(n=self.name, w=self.size, 
                                   h=self.size, d=self.size)[0]
    
    def move(self, x, y, z):
        cmds.move(x, y, z, self.object)

# Create as many cubes as you need easily
cube1 = Cube("cube1", 2)
cube2 = Cube("cube2", 1)
cube1.move(0, 2, 0)
cube2.move(3, 0, 0)
```

3. **Better Structure**
```python
# Without classes (hard to add new features)
def create_cube(name, size):
    return cmds.polyCube(n=name, w=size, h=size, d=size)[0]

def move_cube(cube, x, y, z):
    cmds.move(x, y, z, cube)

# Adding new features means adding more disconnected functions
def color_cube(cube, color):
    # Complex material creation code...
    pass

# With classes (easy to extend)
class Cube:
    def __init__(self, name, size=1):
        self.name = name
        self.size = size
        self.color = None
        self.create()
    
    def create(self):
        self.object = cmds.polyCube(n=self.name, w=self.size, 
                                   h=self.size, d=self.size)[0]
    
    def move(self, x, y, z):
        cmds.move(x, y, z, self.object)
    
    def set_color(self, color):
        self.color = color
        material = cmds.shadingNode('lambert', asShader=True)
        cmds.setAttr(f"{material}.color", *color)
        cmds.select(self.object)
        cmds.hyperShade(assign=material)

# Easy to use all features
my_cube = Cube("colorCube", 2)
my_cube.move(0, 2, 0)
my_cube.set_color([1, 0, 0])  # Red cube
```

> [!tip] Understanding the Benefits
> Notice how using classes:
> - Keeps related code together
> - Makes creating multiple objects simpler
> - Makes adding new features cleaner and easier

> [!tip] Best Practices for Maya Classes
> 1. Always track the Maya object name internally
> 2. Include cleanup methods (like delete())
> 3. Check if objects exist before operating on them
> 4. ***Use meaningful variable names***
> 5. Add clear documentation using docstrings

### Understanding Encapsulation and Abstraction in Python

These two core principles of OOP help us organize our code and hide unnecessary complexity.

> [!info] OOP Principles Resources
> - Video: [OOP Principles Explained](https://www.youtube.com/watch?v=pTB0EiLXUC8)
> - Reference: [Python OOP Concepts](https://www.geeksforgeeks.org/python-oops-concepts/)
> - Guide: [Understanding Abstraction](https://realpython.com/python-interface/)

#### Example with Both Concepts

```python
class MayaShape:
    """Abstract base class for Maya shapes."""
    def __init__(self, name):
        self.name = name          # Public attribute
        self._size = 1.0          # Protected attribute (encapsulation)
        self._object = None       # Protected attribute
        
    def create(self):
        """Abstract method - each shape creates differently."""
        pass  # To be implemented by specific shapes
        
    def delete(self):
        """Common method for all shapes."""
        if self._object:
            cmds.delete(self._object)
            self._object = None

class MayaCube(MayaShape):
    """Concrete cube class."""
    def create(self):
        """Specific implementation for cube."""
        self._object = cmds.polyCube(n=self.name, w=self._size, 
                                    h=self._size, d=self._size)[0]
        
    def set_size(self, value):
        """Safe way to change size (encapsulation)."""
        if value > 0:
            self._size = value
            self._update_transform()
        else:
            print("Error: Size must be positive")
            
    def _update_transform(self):
        """Internal method (encapsulation)."""
        if self._object:
            cmds.scale(self._size, self._size, self._size, self._object)
```

#### Understanding the Concepts

1. **Encapsulation** (Hiding Data)
   - `self.name` - Public (open to everyone)
   - `self._size` - Protected (should stay internal)
   - `self._update_transform()` - Internal method

2. **Abstraction** (Hiding Complexity)
   - `MayaShape` defines what ALL shapes can do
   - `create()` method hides HOW each shape is made
   - Users don't need to know the details

> [!example] Using These Concepts
> ```python
> # Creating shapes without worrying about details
> cube = MayaCube("cube1")
> cube.create()         # Don't need to know HOW it's created
> cube.set_size(2)      # Safe way to change size
> cube.delete()         # Common to all shapes
> 
> # These would be bad practice:
> cube._size = -5       # Bad: breaking encapsulation
> cube._update_transform()  # Bad: using internal method
> ```

> [!tip] Remember
> - Encapsulation: Protect data with _ prefix
> - Abstraction: Hide complex details in base classes
> - Use clear, simple interfaces for users
> - Don't worry about implementation details

### Exercise: Creating Your First Maya Class

Let's modify our `MayaCube` class to add some useful features:

```python
class MayaCube:
    def __init__(self, name="cube1", size=1.0):
        self.name = name
        self.size = size
        self._object = None
        self.position = [0, 0, 0]  # Track position
    
    def create(self):
        if self._object is None:
            self._object = cmds.polyCube(n=self.name, w=self.size, 
                                       h=self.size, d=self.size)[0]
            return self._object
            
    def move(self, x=0, y=0, z=0):
        if self._object:
            cmds.move(x, y, z, self._object)
            self.position = [x, y, z]  # Update position
    
    def get_info(self):
        """Print information about this cube."""
        print(f"Cube: {self.name}")
        print(f"Size: {self.size}")
        print(f"Position: {self.position}")
```

> [!question] Think About It
> 1. What other properties might be useful to track?
> 2. What additional methods would make this class more useful?

##
---
---

## Part 2: Inheritance with Maya Primitives

Now that we understand basic classes, let's see how inheritance can help us create a more flexible system for managing different types of primitives.

### Why Use Inheritance?

> [!example] Real-World Example
> Think about different types of Maya primitives:
> - All primitives can be moved, scaled, and rotated
> - Each primitive has unique creation parameters
> - Some operations are specific to certain primitive types
> 
> Inheritance lets us share common functionality while allowing for specialized behavior.

> [!info] Understanding Inheritance
> - Video: [Python Inheritance Tutorial](https://www.youtube.com/watch?v=RSl87lqOXDE)
> - Reference: [Inheritance in Python](https://realpython.com/inheritance-composition-python/)

### Creating a Base Primitive Class

```python
class MayaPrimitive:
    """Base class for all Maya primitives."""
    
    def __init__(self, name):
        self.name = name
        self._object = None
        self.position = [0, 0, 0]
        self.rotation = [0, 0, 0]
        self.scale = [1, 1, 1]
    
    def create(self):
        """Abstract method to be implemented by child classes."""
        raise NotImplementedError("Subclasses must implement create()")
    
    def move(self, x=0, y=0, z=0):
        """Move the primitive to a new position."""
        if self._object:
            cmds.move(x, y, z, self._object)
            self.position = [x, y, z]
    
    def rotate(self, x=0, y=0, z=0):
        """Rotate the primitive."""
        if self._object:
            cmds.rotate(x, y, z, self._object)
            self.rotation = [x, y, z]
    
    def delete(self):
        """Delete the primitive from Maya."""
        if self._object and cmds.objExists(self._object):
            cmds.delete(self._object)
            self._object = None
```

### Creating Specialized Primitive Classes

```python
class MayaCube(MayaPrimitive):
    """Class for creating and managing cubes."""
    
    def __init__(self, name="cube1", size=1.0):
        super().__init__(name)  # Initialize parent class
        self.size = size
    
    def create(self):
        """Create a cube in Maya."""
        if self._object is None:
            self._object = cmds.polyCube(n=self.name, w=self.size, 
                                       h=self.size, d=self.size)[0]
            return self._object

class MayaSphere(MayaPrimitive):
    """Class for creating and managing spheres."""
    
    def __init__(self, name="sphere1", radius=1.0):
        super().__init__(name)
        self.radius = radius
    
    def create(self):
        """Create a sphere in Maya."""
        if self._object is None:
            self._object = cmds.polySphere(n=self.name, r=self.radius)[0]
            return self._object
```

> [!tip] Understanding super()
> The `super().__init__()` call is crucial - it ensures the parent class is properly initialized. Think of it as setting up the foundation before adding specialized features.

### Using Our Inherited Classes

```python
import sys
sys.path.append("path/to/scripts...")

import maya.cmds as cmds
# Create different primitives
cube = MayaCube("my_cube", 2)
sphere = MayaSphere("my_sphere", 1.5)

# Create them in Maya
cube.create()
sphere.create()

# Move them to different positions
cube.move(0, 2, 0)
sphere.move(3, 0, 0)

# Both classes inherit the rotate method
cube.rotate(0, 45, 0)
sphere.rotate(45, 0, 0)
```

> [!question] Exercise
> Create a new class `MayaCylinder` that inherits from `MayaPrimitive`:
> 1. What parameters would it need?
> 2. How would you implement its `create()` method?
> 3. What unique methods might a cylinder need?

### Benefits of Inheritance

1. **Code Reuse**
   - Common operations (move, rotate, delete) are defined once
   - Each primitive only needs to implement its unique features

2. **Consistency**
   - All primitives share the same basic interface
   - New primitives will automatically have standard functionality

3. **Maintainability**
   - Changes to common functionality can be made in one place
   - Easy to add new features to all primitives

##
---
---
## Part 3: Polymorphism with Maya Tool Functions

Polymorphism allows us to write code that works with different types of objects in a consistent way. In tool development, this is particularly useful when we want to create flexible systems that can handle different types of objects or operations (like in Maya different types of primitives).

> [!info] Understanding Polymorphism
> - Video: [Python Polymorphism Explained](https://www.youtube.com/watch?v=tHN8I_4FIt8)
> - Reference: [Polymorphism in Python](https://www.geeksforgeeks.org/polymorphism-in-python/)

### Basic Polymorphism Example

```python
def create_primitive(prim_object):
    """Create any primitive object."""
    prim_object.create()
    print(f"Created: {prim_object.name}")

# Works with any primitive class
cube = MayaCube("poly_cube")
sphere = MayaSphere("poly_sphere")

create_primitive(cube)     # Works with cubes
create_primitive(sphere)   # Works with spheres
```

### Creating a Primitive Manager

Let's create a class that can manage different types of primitives:

```python
class PrimitiveManager:
    """Class for managing multiple Maya primitives."""
    
    def __init__(self):
        self.primitives = {}  # Store all created primitives
    
    def create_primitive(self, prim_type, name, **kwargs):
        """Create a new primitive of the specified type."""
        if prim_type.lower() == "cube":
            size = kwargs.get("size", 1.0)
            primitive = MayaCube(name, size)
        elif prim_type.lower() == "sphere":
            radius = kwargs.get("radius", 1.0)
            primitive = MayaSphere(name, radius)
        else:
            raise ValueError(f"Unknown primitive type: {prim_type}")
        
        primitive.create()
        self.primitives[name] = primitive
        return primitive
    
    def move_all(self, x=0, y=0, z=0):
        """Move all primitives."""
        for primitive in self.primitives.values():
            primitive.move(x, y, z)
    
    def delete_all(self):
        """Delete all primitives."""
        for primitive in self.primitives.values():
            primitive.delete()
        self.primitives.clear()

    def get_info(self):
        """Print information about all primitives."""
        for name, primitive in self.primitives.items():
            print(f"\nPrimitive: {name}")
            print(f"Type: {type(primitive).__name__}")
            print(f"Position: {primitive.position}")
```

### Using the Primitive Manager

```python
# Create a manager
manager = PrimitiveManager()

# Create different primitives
cube1 = manager.create_primitive("cube", "cube1", size=2)
sphere1 = manager.create_primitive("sphere", "sphere1", radius=1.5)

# Move all primitives up
manager.move_all(y=5)

# Get info about all primitives
manager.get_info()

# Clean up
manager.delete_all()
```

> [!tip] Real-World Application
> This pattern is common in professional tools where you need to:
> - Handle multiple types of objects
> - Apply operations to groups of objects
> - Maintain consistent interfaces
> - Track object state and relationships

> [!question] Exercise: Extending the System
> How would you:
> 1. Add support for a new primitive type?
> 2. Add a new operation that only some primitives support?
> 3. Create a way to group primitives together?

##
---
---

## Part 4: Preview of UI Development with Qt Creator

Now, we'll look at how our OOP-based tools can be integrated with user interfaces. While we won't be building UIs today, understanding how our class structure supports UI development is crucial.

> [!note] UI Development Preview
> This is a preview of what we'll be doing in more detail next week. Today we're focusing on how our OOP design decisions support UI integration.

### Why Qt Creator?

> [!info] Qt and Maya
> - Qt is the framework used by Maya itself for its interface.
> - Provides professional-looking, consistent UI elements.
> - Well-documented and widely used in the industry.
> - Integrates seamlessly with Maya's Python environment.

### Demo: Basic Tool Interface Design

Let's look at how our `PrimitiveManager` class could be used with a UI:

```python
from PySide2 import QtWidgets
from PySide2.QtWidgets import QVBoxLayout, QLabel, QLineEdit, QComboBox, QPushButton, QListWidget

class PrimitiveManager:
    """A class to manage creation and deletion of primitives."""
    
    def create_primitive(self, prim_type, name, size=1.0):
        # Example method to create a primitive
        if prim_type.lower() not in ["cube", "sphere", "cylinder"]:
            raise ValueError(f"Unsupported primitive type: {prim_type}")
        print(f"Creating {prim_type} named {name} with size {size}")
        # Logic to create the primitive (placeholder for actual Maya cmds)
        return f"{prim_type}: {name}"

class PrimitiveCreatorWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.manager = PrimitiveManager()
        self.setup_ui()
    
    def setup_ui(self):
        """Sets up the basic UI layout for primitive creation."""
        self.setWindowTitle("Primitive Creator")
        central_widget = QtWidgets.QWidget()
        layout = QVBoxLayout()

        # Create UI elements
        self.type_label = QLabel("Type:")
        self.type_combo = QComboBox()
        self.type_combo.addItems(["Cube", "Sphere", "Cylinder"])
        
        self.name_label = QLabel("Name:")
        self.name_input = QLineEdit()

        self.size_label = QLabel("Size:")
        self.size_input = QLineEdit("1.0")
        
        self.create_button = QPushButton("Create Primitive")
        self.create_button.clicked.connect(self.create_primitive_clicked)

        self.output_list = QListWidget()

        # Add widgets to the layout
        layout.addWidget(self.type_label)
        layout.addWidget(self.type_combo)
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)
        layout.addWidget(self.size_label)
        layout.addWidget(self.size_input)
        layout.addWidget(self.create_button)
        layout.addWidget(QLabel("Created Objects:"))
        layout.addWidget(self.output_list)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
    
    def create_primitive_clicked(self):
        """Callback for when the create button is clicked."""
        prim_type = self.type_combo.currentText()
        name = self.name_input.text()
        try:
            size = float(self.size_input.text())
        except ValueError:
            QtWidgets.QMessageBox.warning(self, "Input Error", "Size must be a number.")
            return
        
        try:
            new_prim = self.manager.create_primitive(prim_type, name, size=size)
            self.output_list.addItem(new_prim)
        except ValueError as e:
            QtWidgets.QMessageBox.critical(self, "Creation Error", str(e))
```

> [!example] UI Integration Benefits
> Notice how our OOP design makes UI integration simpler:
> - Clean separation between tool logic and UI.
> - Easy to add new features without changing core functionality.
> - Error handling is centralized.
> - State management is handled by our classes.

### Next Week Preview: Qt Creator Interface

Here's a glimpse of what we'll be building next week:

```python
class PrimitiveCreatorWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.manager = PrimitiveManager()
        self.setup_ui()
    
    def setup_ui(self):
        """Preview of UI setup."""
        # We'll learn how to create these UI elements next week.
        self.setWindowTitle("Primitive Creator")
```

> [!tip] Preparing for UI Development
> When designing your classes, consider:
> - What properties need to be accessible from the UI?
> - What operations should be triggered by UI elements?
> - How will you handle errors and user feedback?
> - What state needs to be maintained?

#### Example UI Wireframe
```
+------------------------+
|    Primitive Creator   |
+------------------------+
| Type:   [Cube    ▾]    |
| Name:   [          ]   |
| Size:   [1.0      ]    |
|                        |
| [Create Primitive]     |
|                        |
| Created Objects:       |
| [List View         ]   |
|                        |
| [Delete Selected]      |
+------------------------+
```


> [!info] Qt Resources for Next Week
> - Reference: [Qt for Python Documentation](https://doc.qt.io/qtforpython/)
> - Tutorial: [Getting Started with Qt](https://www.youtube.com/watch?v=i9T0AudMS4U)
> - Video: [Qt Designer Basics](https://www.youtube.com/watch?v=FVpho_UiDAY)
> - Maya Docs: [Working with Qt](https://help.autodesk.com/view/MAYADEV/2025/ENU/?guid=Maya_DEVHELP_Working_with_Qt_html)
##
---
---
## Wrap-Up and Character Creator Preview

### Today's Key Takeaways
1. **OOP Benefits for Maya Tools**
   - Better organization through classes
   - Code reuse through inheritance
   - Flexibility through polymorphism
   - Easier UI integration preparation

2. **Class Structure Review**
   ```python
   # Basic structure we learned
   class MayaPrimitive:        # Base class
       def __init__(self):
           # Basic properties
   
   class MayaCube(MayaPrimitive):  # Inherited class
       def create(self):
           # Specific implementation
   
   class PrimitiveManager:     # Management class
       def create_primitive(self):
           # Handle different types
```

> [!example] Code Evolution
> See how our code evolved from simple functions to organized classes:
> ```python
> # Week 3:
> def create_cube(size): pass
> def move_cube(cube, x, y, z): pass
> 
> # Week 7:
> cube = MayaCube("cube1", 2)
> cube.move(1, 2, 3)
> ```

### Preview: Text-Based Character Creator

In the LAB, you'll apply these OOP concepts to a game design exercise: creating a text-based character system.

```python
# Preview of character system
class GameCharacter:
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength
    
    def attack(self, target):
        """Basic attack method."""
        pass

class Warrior(GameCharacter):
    def special_ability(self):
        """Warrior-specific ability."""
        pass
```

> [!note] Why a Character Creator?
> This exercise will help reinforce OOP concepts in a different context:
> - Classes represent different character types
> - Inheritance creates specialized characters
> - Polymorphism handles different abilities
### Looking Ahead to Week 8

Next week we'll:
1. Build a complete UI for our Maya Primitives tool
2. Learn Qt Creator
3. Connect our classes to UI elements

> [!tip] Preparation for Next Week
> To get the most out of next week:
> 1. Practice with the classes we built today
> 2. Review the Qt resources provided
> 3. Think about what features you'd want in your tool's UI

### Final Thoughts

> [!quote] Remember
> OOP is a powerful way to organize code, but it's not about complexity - it's about making our code more manageable and maintainable. Start simple and build up as needed.

### Lab Preview
For this week's lab, you'll:
1. Complete the Maya primitive system
2. Create a simple character system

> [!info] Additional Resources
> - [Maya Python Command Reference](https://help.autodesk.com/view/MAYAUL/2024/ENU/?guid=__CommandsPython_index_html)
> - [Object-Oriented Programming Concepts](https://realpython.com/python3-object-oriented-programming/)

> [!question] Reflection Questions
> 1. How does OOP improve our Maya tools compared to our previous approach?
> 2. What aspects of OOP seem most useful for your own tools?
> 3. How might you use these concepts in your future projects?

##
---
---
## Connection to Game Development: Unity Character Controller Example

> [!note] Why This Matters
> As future game developers, you'll very likely encounter Unity and C#. The OOP concepts we're learning with Python and Maya directly translate to game development. Let's see how below...

Here's a basic Unity character controller written in C#:

```csharp
using UnityEngine;

public class PlayerController : MonoBehaviour
{
    // Properties (similar to our Python class attributes)
    public float moveSpeed = 5f;
    public float jumpForce = 5f;
    private bool isGrounded = true;
    private Rigidbody rb;  // Reference to physics component

    // Start is like our __init__ method in Python
    void Start()
    {
        // Get and store reference to the Rigidbody component
        rb = GetComponent<Rigidbody>();
    }

    // Update runs every frame (like a loop)
    void Update()
    {
        // Get input (similar to our Maya tool user inputs)
        float horizontalInput = Input.GetAxis("Horizontal");
        float verticalInput = Input.GetAxis("Vertical");

        // Create movement vector (similar to our Maya transform operations)
        Vector3 movement = new Vector3(horizontalInput, 0, verticalInput);
        
        // Apply movement
        rb.MovePosition(transform.position + movement * moveSpeed * Time.deltaTime);

        // Handle jumping (similar to our special abilities in character system)
        if (Input.GetButtonDown("Jump") && isGrounded)
        {
            rb.AddForce(Vector3.up * jumpForce, ForceMode.Impulse);
            isGrounded = false;
        }
    }

    // Collision detection (similar to our combat system)
    void OnCollisionEnter(Collision collision)
    {
        if (collision.gameObject.CompareTag("Ground"))
        {
            isGrounded = true;
        }
    }
}
```

### Breaking Down the Concepts We've Covered

1. **Classes and Objects** (Week 7)
   ```csharp
   public class PlayerController : MonoBehaviour
   ```
   - Just like our `MayaPrimitive` 
   - Creates a template for player behavior
   - Can be reused for multiple players

2. **Properties/Attributes** (Weeks 1-7)
   ```csharp
   public float moveSpeed = 5f;
   private bool isGrounded = true;
   ```
   - Similar to our Python attributes (`self.name`, `self.size`)
   - Stores state and data
   - Public/Private is like our Python underscore convention

3. **Methods** (Weeks 1-7)
   ```csharp
   void Update()
   {
       // Method body
   }
   ```
   - Like our Python methods (`create()`, `move()`)
   - Encapsulates functionality
   - Organized within the class

4. **Control Flow** (Weeks 2-3)
   ```csharp
   if (Input.GetButtonDown("Jump") && isGrounded)
   {
       // Jump code
   }
   ```
   - Same if/else logic we used in Python
   - Conditional execution of code

5. **Variables and Data Types** (Week 1)
   ```csharp
   float moveSpeed = 5f;
   bool isGrounded = true;
   Vector3 movement;
   ```
   - Similar to Python's variables
   - Different syntax, same concept

6. **Inheritance** (Week 7)
   ```csharp
   public class PlayerController : MonoBehaviour
   ```
   - Like our Python inheritance, in Unity and C# most scripts `inherit` from a parent class: MonoBehaviour
   - Inherits functionality from parent class

7. **State Management** (Weeks 3-7)
   ```csharp
   private bool isGrounded = true;
   // ... later in code ...
   isGrounded = false;
   ```
   - Tracking object state (like our Maya primitive positions)
   - Maintaining and updating data

> [!tip] Python vs C# Comparison
> ```python
> # Python (Our Maya Class)
> class MayaCube:
>     def __init__(self):
>         self.position = [0, 0, 0]
>     
>     def move(self, x, y, z):
>         self.position = [x, y, z]
>         cmds.move(x, y, z, self.object)
> ```
> ```csharp
> // C# (Unity)
> public class PlayerController : MonoBehaviour
> {
>     private Vector3 position;
>     
>     void Move(float x, float y, float z)
>     {
>         position = new Vector3(x, y, z);
>         transform.position = position;
>     }
> }
> ```

> [!note] Key Takeaway
> Whether you're scripting in Maya with Python or making games in Unity with C#, the fundamental programming concepts remain the same! The skills you're learning now will directly transfer to game development.

##
---
---
## Connection to Game Development: Unity Game Manager Example

Here's a simple game manager that handles different types of characters (similar to the character system in the LAB):

```csharp
using UnityEngine;
using System.Collections.Generic;

// Base character class (similar to our GameCharacter)
public abstract class GameCharacter : MonoBehaviour
{
    public string characterName;
    public float health;
    
    // Abstract method (like our Python 'pass' methods)
    public abstract void SpecialAbility();
    
    // Virtual method (can be overridden)
    public virtual void TakeDamage(float damage)
    {
        health -= damage;
        if (health <= 0)
        {
            Debug.Log($"{characterName} has been defeated!");
        }
    }
}

// Derived classes (like our Warrior, Mage, etc.)
public class WarriorCharacter : GameCharacter
{
    public override void SpecialAbility()
    {
        Debug.Log($"{characterName} uses Shield Block!");
        // Shield implementation
    }
}

public class MageCharacter : GameCharacter
{
    public override void SpecialAbility()
    {
        Debug.Log($"{characterName} casts Fireball!");
        // Spell implementation
    }
}

// Game Manager (similar to our PrimitiveManager/CharacterManager)
public class GameManager : MonoBehaviour
{
    // Singleton pattern (common in Unity)
    public static GameManager Instance { get; private set; }
    
    // List of all characters (like our manager dictionaries)
    private List<GameCharacter> characters = new List<GameCharacter>();
    
    void Awake()
    {
        if (Instance == null)
        {
            Instance = this;
            DontDestroyOnLoad(gameObject);
        }
        else
        {
            Destroy(gameObject);
        }
    }
    
    // Add character to management (like our create_primitive method)
    public void RegisterCharacter(GameCharacter character)
    {
        characters.Add(character);
        Debug.Log($"Registered: {character.characterName}");
    }
    
    // Remove character from management (like our delete method)
    public void UnregisterCharacter(GameCharacter character)
    {
        characters.Remove(character);
        Debug.Log($"Unregistered: {character.characterName}");
    }
    
    // Example of polymorphism: Activate all characters' abilities
    public void ActivateAllSpecialAbilities()
    {
        foreach (GameCharacter character in characters)
        {
            character.SpecialAbility();  // Each type handles this differently
        }
    }
    
    // Damage all characters (similar to our move_all)
    public void DamageAll(float damage)
    {
        foreach (GameCharacter character in characters)
        {
            character.TakeDamage(damage);
        }
    }
}
```

### Comparing Management Systems

> [!example] Python vs C# Management
> ```python
> # Our Python Manager
> class CharacterManager:
>     def __init__(self):
>         self.characters = {}
>     
>     def create_character(self, char_type, name):
>         if char_type == "warrior":
>             character = Warrior(name)
>         elif char_type == "mage":
>             character = Mage(name)
>         self.characters[name] = character
> ```
```csharp
// Unity Manager
public class GameManager : MonoBehaviour
{
    private List<GameCharacter> characters;
    public void RegisterCharacter(GameCharacter character)
    {
        characters.Add(character);
    }
}
```

### Key Polymorphism Concepts Illustrated

1. **Abstract Methods**
   - Python: We used `raise NotImplementedError`
   - C#: Uses `abstract` keyword
   - Both enforce implementation in derived classes

2. **Method Overriding**
   - Python: Redefining methods in child classes
   - C#: Using `override` keyword
   - Both allow specialized behavior

3. **Common Interface**
   - Python: Our manager treated all primitives/characters similarly
   - C#: GameManager treats all GameCharacters similarly
   - Both demonstrate "programming to an interface"

> [!tip] Understanding Polymorphism
> Whether in Python or C#, polymorphism allows us to:
> - Treat different objects through a common interface
> - Write code that works with future object types
> - Maintain clean, organized management systems

> [!note] Real-World Application
> This pattern is exactly how many games handle:
> - Different types of enemies
> - Various power-ups
> - Multiple weapon types
> 
> The principles you're learning apply directly to real game development!

##
---
---