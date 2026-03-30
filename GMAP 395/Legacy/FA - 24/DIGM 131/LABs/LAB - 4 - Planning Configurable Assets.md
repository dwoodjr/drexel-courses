# Week 4 LAB: Code Review, Dictionaries, and JSON Configuration

##
---
## Part 1: Code Review and Critical Thinking

### Step 1: Review Your Week 3 Script

1. Open your `maya_utils.py` script from Week 3 live coding.
2. Read through the code and identify areas that could be improved or made more efficient.

> [!note] Task
> List at least three areas of your script that you think could be improved. For each area:
> - Explain why you think it needs improvement
> - Propose a solution for how you might enhance it

### Step 2: Introduction to Dictionaries

Dictionaries are powerful data structures in Python that allow us to store key-value pairs. Let's see how we can use them to improve our script.
1. create a new script titled `asset_creator.py` (**unless you already have one form ASN 3, then this is just review**)
2. Paste in the below code

> [!info] Dictionaries
> - Video: [Python Dictionaries (Corey Schafer)](https://www.youtube.com/watch?v=daefaLgNkw0)
> - Reference: [Python Dictionary (GeeksforGeeks)](https://www.geeksforgeeks.org/python-dictionary/)

```python
import maya.cmds as cmds

# Define shape types using a dictionary
SHAPE_TYPES = {
    "cube": cmds.polyCube,
    "sphere": cmds.polySphere,
    "cylinder": cmds.polyCylinder,
    "cone": cmds.polyCone
}

def create_primitive(shape_type, size, name=None):
    if shape_type not in SHAPE_TYPES:
        print(f"Unsupported shape type: {shape_type}")
        return None

    create_func = SHAPE_TYPES[shape_type]
    
    if shape_type == "cube":
        obj = create_func(width=size, height=size, depth=size)[0]
    elif shape_type == "sphere":
        obj = create_func(radius=size)[0]
    elif shape_type in ["cylinder", "cone"]:
        obj = create_func(radius=size, height=size)[0]

    if name:
        obj = cmds.rename(obj, name)
    
    return obj
```

> [!note] Task
> 1. Compare this version of `create_primitive` with your original version. What are the key differences?
> 2. Explain in your own words how using a dictionary (`SHAPE_TYPES`) makes this function more flexible and easier to extend.
> 3. How would you add a new shape type (e.g., "torus") to this system?

### Step 3: Refactoring with Dictionaries

Now, let's refactor the `create_color_material` function to use a dictionary for default colors:

```python
DEFAULT_COLORS = {
    "red": (1, 0, 0),
    "green": (0, 1, 0),
    "blue": (0, 0, 1),
    "yellow": (1, 1, 0),
    "white": (1, 1, 1)
}

def create_color_material(color, name=None):
    if isinstance(color, str):
        color = DEFAULT_COLORS.get(color.lower(), DEFAULT_COLORS["white"])
    
    material = cmds.shadingNode('lambert', asShader=True)
    cmds.setAttr(f"{material}.color", *color, type="double3")
    
    if name:
        material = cmds.rename(material, name)
    
    return material
```

> [!note] Task
> 1. Explain how this new version of `create_color_material` differs from the original.
> 2. What advantage does using `DEFAULT_COLORS` provide?
> 3. How would you use this new function? Provide an example.

##
---
## Part 2: Introduction to JSON Configuration Files

JSON (JavaScript Object Notation) is a lightweight data format that's easy for humans to read and write, and easy for machines to parse and generate. It's commonly used for configuration files.

### Step 1: Creating a JSON Configuration File

Create a new file named `asset_config.json` with the following content:

```json
{
  "shapes": {
    "cube": {
      "default_size": 1.0,
      "default_color": [1.0, 0.0, 0.0]
    },
    "sphere": {
      "default_size": 1.5,
      "default_color": [0.0, 1.0, 0.0]
    },
    "cylinder": {
      "default_size": 1.2,
      "default_color": [0.0, 0.0, 1.0]
    },
    "cone": {
      "default_size": 1.0,
      "default_color": [1.0, 1.0, 0.0]
    }
  }
}
```

> [!note] Task
> 1. Examine the structure of this JSON file. How does it relate to the Python dictionaries we've been working with?
> 2. Why might it be useful to have this configuration in a separate file?

### Step 2: Reading JSON in Python

Now, let's create a new Python script to read and use this configuration:
1. Create a script: `config_asset_creator.py`

```python
import json
import maya.cmds as cmds
import asset_creator

def read_config(config_file='asset_config.json'):
    with open(config_file, 'r') as f:
        return json.load(f)

def create_assets_from_config():
    config = read_config()
    for shape, details in config['shapes'].items():
        size = details['default_size']
        color = tuple(details['default_color'])
        name = f"{shape}_from_config"
        asset_creator.create_colored_primitive(shape, size, name, color)

def main():
    create_assets_from_config()
    asset_creator.list_assets()

if __name__ == "__main__":
    main()
```

> [!note] Task
> 1. Explain what each function in this script does.
> 2. How does this script use the configuration file to create assets?
> 3. What advantages does this approach offer compared to hardcoding values in the script?

### Step 3: Integrating Configuration with Asset Creation

Now, let's modify our `asset_creator.py` to use the configuration file:

```python
import json
import maya.cmds as cmds

def read_config(config_file='asset_config.json'):
    with open(config_file, 'r') as f:
        return json.load(f)

CONFIG = read_config()

def create_primitive(shape_type, size=None, name=None):
    if shape_type not in CONFIG['shapes']:
        print(f"Unsupported shape type: {shape_type}")
        return None

    shape_config = CONFIG['shapes'][shape_type]
    size = size or shape_config['default_size']

    create_func = getattr(cmds, f"poly{shape_type.capitalize()}")
    
    if shape_type == "cube":
        obj = create_func(width=size, height=size, depth=size)[0]
    elif shape_type == "sphere":
        obj = create_func(radius=size)[0]
    elif shape_type in ["cylinder", "cone"]:
        obj = create_func(radius=size, height=size)[0]

    if name:
        obj = cmds.rename(obj, name)
    
    return obj

def create_color_material(color=None, name=None):
    if color is None:
        color = CONFIG['shapes']['cube']['default_color']  # Default to cube's color
    
    material = cmds.shadingNode('lambert', asShader=True)
    cmds.setAttr(f"{material}.color", *color, type="double3")
    
    if name:
        material = cmds.rename(material, name)
    
    return material

# ... rest of the script remains the same
```

> [!note] Task
> 1. Compare this version of `create_primitive` and `create_color_material` with the previous versions. What are the main differences?
> 2. How does using `CONFIG` make these functions more flexible?
> 3. What would you need to do to add support for a new shape type now?

## Wrap Up

> [!quote] Reflection
> As you complete this lab, consider:
> - How do dictionaries and JSON configuration files make our script more flexible and easier to maintain?
> - What challenges might arise when using external configuration files?
> - How might these concepts apply to larger-scale game development or technical art projects?

Compile your notes and reflections from each step into a single document. Be prepared to discuss your insights in the next class session.