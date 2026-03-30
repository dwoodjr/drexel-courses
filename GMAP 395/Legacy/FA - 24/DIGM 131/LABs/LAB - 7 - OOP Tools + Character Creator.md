# Interactive Lab: Object-Oriented Tools in Maya & Character Creator

## 🎯 Objective
Transform our Maya primitive creation tools into an object-oriented system and create a simple character creator to reinforce OOP concepts through two different approaches.

## 📚 Pre-lab Preparation
1. Review the Week 7 materials on OOP concepts
2. Have Maya 2024/2025 open and ready
3. Create a new directory for this lab/assignment

> [!info] OOP Quick Reference
> - [Python Classes Documentation](https://docs.python.org/3/tutorial/classes.html)
> - [Maya Python Commands](https://help.autodesk.com/view/MAYAUL/2024/ENU/?guid=__CommandsPython_index_html)

##
---
---
## Part 1: Refactoring Maya Tools with OOP

### Step 1: Creating the Base Primitive Class

1. Create a new file called `maya_primitives.py`
2. ***Add the following base class structure and complete the missing code:***

```python
import maya.cmds as cmds

class MayaPrimitive:
    """Base class for Maya primitive objects."""
    
    def __init__(self, name):
        self.name = name
        self._object = None  # Internal reference to Maya object
        
    def create(self):
        """Abstract method to be implemented by subclasses."""
        raise NotImplementedError("Subclasses must implement create()")
        
    def delete(self):
        """Delete the primitive from Maya."""
		# Implement delete
     
    def move(self, x=0, y=0, z=0):
        """Move the primitive to a new position."""
		# Implement move
	
	def rotate(self, x=0, y=0, z=0):
        """Rotate the primitive."""
        # Implement rotate
	
	def scale(self, ):
		"""Scale the primitive."""
		# Implement scale
```

> [!tip] Understanding the Base Class
> - `self._object` starts with an underscore to indicate it's internal to the class
> - `create()` is an abstract method that derived classes must implement
> - Common operations like `move()` and `delete()` are defined once in the base class

### Step 2: Implementing Specific Primitive Classes

1. **Create these derived classes** that `inherit` from  `maya_primitives.py`:

```python
class CubePrimitive():
    """Class for creating and managing cubes."""

class SpherePrimitive():
    """Class for creating and managing spheres."""

class CylinderPrimitive():
    """Class for creating and managing spheres."""

class TorusPrimitive():
    """Class for creating and managing spheres."""

```

2. ***Create a script to test your implementation of ALL defined primitives:***

```python
import sys
sys.path.append("...")

import maya.cmds as cmds

"""Test code"""

# Cube
cube = CubePrimitive("test_cube", 2.0)
cube.create()
cube.move(0, 2, 0)

# Sphere
sphere = #...

# Cylinder
	# Implement

# Torus
	#Implement
```

### Step 3: Creating the Primitive Manager

1. Create a new file called `primitive_manager.py`
2. ***Finish the code to implement the manager class:***

```python
from maya_primitives import CubePrimitive, SpherePrimitive, CylinderPrimitive

class PrimitiveManager:
    """Class for managing multiple Maya primitives."""
    
    def __init__(self):
        self.primitives = {}  # Dictionary to store primitives
        
    def create_primitive(self, prim_type, name, **kwargs):
        """Create a new primitive of the specified type."""
        if prim_type.lower() == "cube":
			# missing code
        elif prim_type.lower() == "sphere":
			# missing code
        elif prim_type.lower() == "cylinder":
	        # missing code
		elif prim_type.lower() == "torus":
			# missing code
        else:
            raise ValueError(f"Unknown primitive type: {prim_type}")
            
		# missing code
        return primitive
         
    def get_primitive(self, name):
        """Get a primitive by name."""
        return self.primitives.get(name)
```

3. ***Add utility methods to the manager:***

```python
class PrimitiveManager:
    # ... previous methods ...
    
    def move_all(self, x=0, y=0, z=0):
        """Move all primitives."""
				# missing code
            
    def delete_all(self):
        """Delete all primitives."""
				# missing code
            
    def list_primitives(self):
		"""List prim info."""
				# missing code
```

4. ***Finish the code and test the manager:***

```python
# Test code
manager = PrimitiveManager()

# Create different primitives
cube = #...
sphere = #...
cylinder = #...
torus = #...

# Move all primitives up
manager.move_all(y=5)

# List all primitives
manager.list_primitives()

# Clean up
# manager.delete_all()
```

##
---
---
## Part 2: Text-Based Character Creator

### Step 1: Setting Up the Character System

1. Create a new file called `character_system.py`
2. **Implement the base character class:**

```python
class GameCharacter:
    """Base class for game characters."""
    
    def __init__(self, name, health=100, strength=10):
        self.name = name
        self.health = health
        self.strength = strength
        self.level = 1
        self.character_class = "Base"  # Will be overridden by subclasses
    
    def attack(self, target):
        """Basic attack method."""
        damage = self.strength
        target.take_damage(damage)
        return damage
        
    def take_damage(self, amount):
        """Handle receiving damage."""
        # TODO: Implement damage handling logic to reduce health and ensure it does not go below zero
	        # Use Character Health subtract some amount for damage
	        # Ensure character can't have negative health

        
    def is_alive(self):
        """Check if character is still alive."""
        # TODO: Implement alive check logic to return True if health is greater than zero

```

### Step 2: Creating Character Classes

1. ***Add specialized character classes:***
	 Be creative and have some fun coming up with class attributes

```python
# TODO: Create a class for Warrior, inheriting from GameCharacter
class Warrior(GameCharacter):
    """Warrior class with high strength and health."""
    
    def __init__(self, name):
        super().__init__(name, health=150, strength=15)
        self.character_class = "Warrior"
        self.shield_active = False  
    
    def special_ability(self):
        """Activate shield to reduce incoming damage."""
        self.shield_active = True   
    
    def take_damage(self, amount):
        """Override to implement shield."""
        if self.shield_active:
            amount = amount // 2  # Shield reduces damage by half
            self.shield_active = False
        super().take_damage(amount)
        

# TODO: Create a class for Mage, inheriting from GameCharacter
class Mage(GameCharacter):
    """Mage class with special magical abilities."""
    
    def __init__(self, name):
        # TODO: Use super() to call the base class constructor with specific health and strength values
		# Assign a "Character Class" name
		# Mage should use "Mana" for special ability
        
    
    def special_ability(self, target):
        """Cast a powerful spell."""
        # TODO: Implement special ability to cast a spell if there is enough mana
        
        
	def take_damage(self, amount):
	"""Override to implement mana reduction."""
		# TODO: Implement mana reduction logic to reduce damage taken
		# Use the parent class Take Damage method to apply damage
	

# TODO: Create a class for Rogue, inheriting from GameCharacter
class Rogue(GameCharacter):
    """Rogue class with special crit hit ability."""
    
    def __init__(self, name):
        # TODO: Use super() to call the base class constructor with specific health and strength values
		# Assign a "Character Class" name
        
    
    def special_ability(self, target):
        """Inflict critical hit on chance."""
        # TODO: Implement special ability to apply a potential critical hit using random chance
        # Dont forget to "import random"
        
	def take_damage(self, amount):
	"""Override to implement dodge chance."""
		# TODO: Implement random logic to reduce damage taken on a chance amount
		# Use the parent class Take Damage method to apply damage
		# Dont forget to "import random"
	

```

### Step 3: Character Management System

1. Create a new file called `character_manager.py`
2. **Implement the management system:**

```python
class CharacterManager:
    """System for managing game characters."""
    
    def __init__(self):
        self.characters = {}
        
    def create_character(self, char_type, name):
        """Create a new character of specified type."""
        # TODO: Implement logic to create Warrior, Mage, or Rogue based on char_type
		if char_type.lower() == "warrior":
			character = Warrior(name)
		elif # Other classes
		else:
			raise ValueError(f"Unknown character type: {char_type}")
		
		self.characters[name] = character
        return character
```

### Step 4: Testing the System

1. Create a test script called `test_characters.py`:

```python
from character_manager import CharacterManager

def main():
    # Create a manager
    manager = CharacterManager()
    
    # TODO: Create some characters using the manager and test their interactions
	warrior = manager.create_character("warrior", "Conan")
	# Create more characters...

    # Test character interactions like attacks and special abilities
	print(f"\n{warrior.name} attacks {mage.name}")
    damage = warrior.attack(mage)
    print(f"Dealt {damage} damage. {mage.name}'s health: {mage.health}")
   # Create more tests...

if __name__ == "__main__":
    main()
```


> [!tip] Testing Your Code
> Run your test script and check:
> 1. Are characters created correctly?
> 2. Do special abilities work as expected?
> 3. Are all outcomes expected?


##
---
---
## 🏆 Bonus Challenge: Creating a Battle Arena (Optional) (+2 Extra Credit)

*For students who want an extra challenge (and some extra credit), try creating a text-based battle arena where players can create characters and have them battle each other. The battle outcomes should be slightly randomized to make each battle unique.*

**Hints to Get Started:**

1. **Create a New Script**: Create a new file called `battle_arena.py`.
2. **User Input**: Use the `input()` function to allow users to create two characters. Prompt for character type (`warrior`, `mage`, `rogue`) and name.
3. **Battle Loop**: Implement a loop where the two characters take turns attacking each other until one of them is defeated.
4. **Randomized Attacks**: Use Python's `random` module to decide whether a character attacks normally or uses a special ability.

Here is a sample pseudocode outline to help you get started:

```
- Import necessary modules and classes
- Initialize character manager
- Get user input to create two characters (type and name)
- Retrieve the created characters
- Display initial battle message

- While both characters are alive:
    - Print round number
    - Randomly decide which character attacks and whether to use a special ability
    - Perform the attack or special ability
    - Print the result of the action
    - Check if the attacked character is defeated
    - If defeated, print winner message and end the loop
    - Increment round number
```

**Tips for the Battle Arena:**
- Use `random.random()` to add randomness to each character's turn.
- Use loops to keep the battle going until one character is defeated.
- Display informative messages to make the game engaging and easy to follow.
##
---
---
## Wrap-up and Assignment Submission

### Required Deliverables Checklist
✅ Maya Primitive System:
- [ ] Base `MayaPrimitive` class implementation
- [ ] At least three primitive type classes (Cube, Sphere, Cylinder)
- [ ] Working `PrimitiveManager` class
- [ ] Successful test demonstration

✅ Character System:
- [ ] Base `GameCharacter` class implementation
- [ ] At least three character classes (Warrior, Mage, Rogue)
- [ ] Working `CharacterManager` class
- [ ] Successful test demonstration


> [!attention] THIS LAB IS ALSO YOUR ASSIGNMENT
> This lab, the two exercises within, will be turned in as you assignment submission for the fourth assignment in this course. 
> See `4 - OOP` assignment on BB Learn for more specifics on the assignment submission. 
> See the assignment document for detailed submission instructions and grading criteria.

### Reflection Questions 🤔
1. How does OOP make our code more organized and maintainable?
2. What challenges did you face implementing inheritance?
3. How might you extend these systems for a larger project?
4. What advantages does the manager class pattern provide?

> [!tip] Documentation Tips
> - Comment your code thoroughly
> - Include docstrings for all classes and methods
> - Explain any complex logic or algorithms
> - Document any assumptions or limitations

