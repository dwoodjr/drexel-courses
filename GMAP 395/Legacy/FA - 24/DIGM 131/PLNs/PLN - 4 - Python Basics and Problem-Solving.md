# Week 4 PLN: Python Basics Review and Problem-Solving Strategies

## Introduction

***Welcome to Week 4!*** We're all taking a step back to review and reinforce the fundamental concepts of Python programming we have seen so far (plus a couple of new ones). This session is designed to ensure everyone has a solid foundation before we move forward in the course. We'll also introduce some problem-solving strategies that will help you approach programming tasks more effectively.

> [!attention] Test the Provided Code
>You are ***strongly*** encouraged to open up an IDE (like VS Code) and test each section of code in this review document to see how it functions when run.

## Part 1: Python Basics Review

### 1. Variables and Data Types

Variables are containers for storing data values. In Python, you don't need to declare a variable's type explicitly.

```python
# Integers
age = 25
year = 2023

# Floating-point numbers
height = 1.75
weight = 68.5

# Strings
name = "Alice"
greeting = 'Hello, World!'

# Booleans
is_student = True
has_car = False

# Printing variables
print(f"Name: {name}, Age: {age}, Height: {height}m")
```
> [!info] Variables and Data Types
> - Video: [Python Variables (Programming with Mosh)](https://www.youtube.com/watch?v=cQT33yu9pY8)
> - Reference: [Python Variables (GeeksforGeeks)](https://www.geeksforgeeks.org/python-variables/)
> - Reference: [Python Data Types (GeeksforGeeks)](https://www.geeksforgeeks.org/python-data-types/)

> [!info] Formatted String Literals (f-strings)
> Video: [Python Quick Tip: F-Strings (Corey Schafer)](https://www.youtube.com/watch?v=nghuHvKLhJA)
> Reference: [f-strings in Python](https://www.geeksforgeeks.org/formatted-string-literals-f-strings-python/)
### 2. Basic Operations

Python supports various operations on different data types.

```python
# Arithmetic operations
a = 10
b = 3

print(f"Addition: {a + b}")
print(f"Subtraction: {a - b}")
print(f"Multiplication: {a * b}")
print(f"Division: {a / b}")
print(f"Integer Division: {a // b}")
print(f"Modulus: {a % b}")
print(f"Exponentiation: {a ** b}")

# String operations
first_name = "John"
last_name = "Doe"

full_name = first_name + " " + last_name
print(f"Full name: {full_name}")

# String repetition
print("Ha" * 3)  # Prints HaHaHa
```
> [!info] Basic Operations
> - Video: [Math in Python in Easy](https://www.youtube.com/watch?v=jc7TBgMS_kw)
> - Reference: [Python Operators (GeeksforGeeks)](https://www.geeksforgeeks.org/python-operators/)
### 3. Conditional Statements

Conditional statements allow you to execute different code based on certain conditions.

```python
age = 18

if age >= 18:
    print("You are an adult")
elif age >= 13:
    print("You are a teenager")
else:
    print("You are a child")

# Nested conditions
has_license = True

if age >= 18:
    if has_license:
        print("You can drive")
    else:
        print("You need to get a license to drive")
else:
    print("You are too young to drive")
```
> [!info] Conditional Statements
> - Video: [Python If Else (Programming with Mosh)](https://www.youtube.com/watch?v=Zp5MuPOtsSY&list=PLTjRvDozrdlxj5wgH4qkvwSOdHLOCx10f&index=9)
> - Reference: [Python if, if...else, if...elif...else (GeeksforGeeks)](https://www.geeksforgeeks.org/python-if-else/)
### 4. Loops

Loops allow you to repeat a block of code multiple times.

```python
# For loop
for i in range(5):
    print(f"Iteration {i + 1}")

# While loop
count = 0
while count < 5:
    print(f"Count is {count}")
    count += 1

# Looping through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}")
```
> [!info] Loops
> - Video: [Python for Loops (Programming with Mosh)](https://www.youtube.com/watch?v=94UHCEmprCY&list=PLTjRvDozrdlxj5wgH4qkvwSOdHLOCx10f&index=7)
> - Reference: [Python Loops (GeeksforGeeks)](https://www.geeksforgeeks.org/loops-in-python/)
### 5. Functions

Functions are reusable blocks of code that perform a specific task.

```python
def greet(name):
    return f"Hello, {name}!"

message = greet("Alice")
print(message)

def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)
print(f"5 + 3 = {result}")

# Function with default parameter
def power(base, exponent=2):
    return base ** exponent

print(power(3))    # Prints 9
print(power(3, 3)) # Prints 27
```
> [!info] Functions
> - Video: [Python Functions (Programming with Mosh)](https://www.youtube.com/watch?v=u-OmVr_fT4s&list=PLTjRvDozrdlxj5wgH4qkvwSOdHLOCx10f&index=8&t=1s)
> - Reference: [Python Functions (GeeksforGeeks)](https://www.geeksforgeeks.org/python-functions/)
##
---
## Part 2: Connecting the Basics to Previous Work

Now that we've reviewed these fundamental concepts, let's look back at what we've accomplished in the first three weeks and see how these basics form the foundation of more complex scripts we have worked on.

### Week 1: Project Structure Automation

In our first week, we created a script to automate project folder creation. Let's break down how the basic concepts we've reviewed today were used:

1. **Variables and Strings**: 
   We used variables to store the project name and path:
   ```python
   project_name = "SuperAwesomeGame"
   project_path = f"C:/Games/{project_name}"
   ```

2. **Lists**:
   We used a list to store folder names:
   ```python
   folders = ["Assets", "Scripts", "Levels", "Documentation"]
   ```
> [!info] Lists
> - Video: [Python Lists (Programming with Mosh)](https://www.youtube.com/watch?v=9OeznAkyQz4&list=PLTjRvDozrdlxj5wgH4qkvwSOdHLOCx10f&index=10)
> - Reference: [Python Lists (GeeksforGeeks)](https://www.geeksforgeeks.org/python-list/)

1. **Loops**:
   We used a for loop to iterate through the folder list:
   ```python
   for folder in folders:
       full_path = os.path.join(project_path, folder)
       # Create folder
   ```

4. **Functions**:
   We encapsulated our logic in a function:
   ```python
   def create_project_structure(name, base_path="C:/Games"):
       # Function body
   ```

5. **Modules**:
   We imported and used the `os` module for file operations:
   ```python
   import os
   ```
> [!info] Modules and Importing
> - Video: [Python Modules (Bro Code)](https://www.youtube.com/watch?v=XcfxkHrHTVE)
> - Reference: [Python Modules (GeeksforGeeks)](https://www.geeksforgeeks.org/python-modules/)

> [!note] REMEMBER DOCUMENTATION (Your Best Friend)
> You are never going to be expected to commit to memory everything a module, package, or plugin does/can do. That is just not rally possible. You will. however, be expected to know how/when to reference documentation. So for any tool, software, or coding framework you use one of the first things you should do is find its documentation. Python is great in that is has EXTENSIVE documentation on almost all of its default `modules` and `syntax`. So get comfortable with searching the internet for them and reading them to get a better handle of how each part of it works. You can even find videos or ask a LLM for more context.
> Link to the [Python Module Index](https://docs.python.org/3/py-modindex.html)
### Week 2: File Management and Batch Renaming

In Week 2, we expanded on these concepts from Week 1 to create a more complex file management script:
> [!info] File I/O
> - Video: [Python File Handling (Corey Schafer)](https://www.youtube.com/watch?v=Uh2ebFW8OYM)
> - Reference: [Python File I/O (GeeksforGeeks)](https://www.geeksforgeeks.org/file-handling-python/)

1. **Conditional Statements**:
   We used if statements (control flow) to filter files:
   ```python
   if is_valid_filename(filename):
       # Rename file
   ```

2. **Error Handling**:
   We introduced try-except blocks for robust file operations:
   ```python
   try:
       os.rename(old_file, new_file)
   except OSError as e:
       print(f"Error renaming {filename}: {e}")
   ```
> [!info] Error Handling
> - Video: [Python Try Except (Corey Schafer)](https://www.youtube.com/watch?v=NIWwJbo-9_8)
> - Reference: [Python Exception Handling (GeeksforGeeks)](https://www.geeksforgeeks.org/python-exception-handling/)


1. **Function Parameters**:
   We made our functions more flexible with parameters:
   ```python
   def rename_files(directory, prefix):
       # Function body
   ```

### Week 3: Modular Design in Maya

In Week 3, we applied these concepts to Maya scripting and introduced more advanced ideas:

1. **Dictionaries**:
   We used dictionaries to map asset types to creation functions (in truth we didn't quite get to this, but it is covered in the Week 4 video (first thing)):
   ```python
   asset_types = {
       "cube": cmds.polyCube,
       "cone": cmds.polyCone,
       "sphere": cmds.polySphere
   }
   ```
> [!info] Dictionaries
> - Video: [Python Dictionaries (Corey Schafer)](https://www.youtube.com/watch?v=daefaLgNkw0)
> - Reference: [Python Dictionary (GeeksforGeeks)](https://www.geeksforgeeks.org/python-dictionary/)


1. **Modular Design**:
   We created separate functions for different tasks and combined them:
   ```python
   def create_primitive(shape_type, size=1, name=None):
       # Function body

   def create_color_material(color, name=None):
       # Function body

   def create_colored_primitive(shape_type, size=1, name=None, color=(1, 1, 1)):
       obj = create_primitive(shape_type, size, name)
       material = create_color_material(color)
       # Assign material to object
   ```

### Critical Thinking Exercise

Now, let's apply some critical thinking to our previous work:

1. How might we modify our Week 1 project structure script to be more flexible for different types of game projects?
2. In our Week 2 file management script, how could we extend it to handle different file types differently?
3. For our Week 3 Maya utilities, how could we make them more efficient for creating multiple objects at once?

Take a few minutes to think about these questions and write down your ideas. Remember, there's no single correct answer (in fact, there is almost always going to be *more than one way* to accomplish something) – the goal is to think creatively about how to apply and extend what you've learned.

##
---
## Part 3: Problem-Solving Strategies

### 1. Understand the Problem

*Before writing any code*, make sure you fully understand what the problem is asking. **Break it down into smaller, manageable parts.** If you are finding you don't know everything you need to about a specific problem *research it* (look it up); if that doesn't provide results, ask questions for clarification (peers, professors, online forums, etc.).

Example: Create a function that calculates the area of a rectangle.

- What inputs do we need? (length and width)
- What output should we produce? (area)
- What formula do we use? (area = length * width)

### 2. Plan Your Approach

Outline the steps you'll take to solve the problem. This can be in pseudocode or simple English.

Example plan for calculating rectangle area:
1. Define a function that takes two parameters: length and width
2. Multiply length by width
3. Return the result


> [!attention] Critical Thinking and Problem Solving Guide
> I have uploaded a revised version of a critical thinking and problem solving guide I have been developing for some of my other game design courses. It is stripped down and easier to digest, I believe; and be aware it is "non-extensive." There is a bunch that goes into developing and studying these crucial skills (decades of research, in fact) but what it has in there are some of the fundamental steps you can take to working on this approach. So please, read it over (multiple times), save it, and use it as a reference as you work.
> 
> Guide Title: `Critical Thinking and Problem-Solving - A Guide to Learning Better, Faster`

### 3. Write the Code

Translate your plan into actual Python code.

```python
def calculate_rectangle_area(length, width):
    area = length * width
    return area

# Test the function
result = calculate_rectangle_area(5, 3)
print(f"The area of the rectangle is: {result}")
```

### 4. Test and Debug

Always test your code with different inputs to ensure it works correctly. If there are errors, debug step by step.

```python
# Additional tests
print(calculate_rectangle_area(10, 20))  # Should print 200
print(calculate_rectangle_area(7.5, 2.5))  # Should print 18.75
print(calculate_rectangle_area(0, 5))  # Should print 0
```

### 5. Refine and Optimize

Once your code works, consider if there are ways to improve it. Can you make it more efficient or easier to read?

```python
def calculate_rectangle_area(length, width):
    if length < 0 or width < 0:
        return "Error: Length and width must be non-negative"
    return length * width

# Test the improved function
print(calculate_rectangle_area(5, 3))    # Works as before
print(calculate_rectangle_area(-1, 5))   # Handles negative input
```

##
---
## The Essence of Programming in Game Design + Technical Art

As we conclude our review of Python basics, let's consider how these fundamental programming concepts apply to technical art, specifically in the context of working with Maya.

At its core, programming for technical art and in game design involves:

1. Determining what data is needed
2. Assigning that data to variables
3. Getting correct references to objects
4. Manipulating objects using data and variables
5. Using functions, operations, and algorithms
6. Arriving at the desired outcome (and refine)

Let's break this down further using our Maya work as an example:

### 1. Determining what data is needed

This is often the first step in solving any problem with programming. You need to identify what information you need to represent and manipulate to achieve your goal.

> [!example] Example
> For creating primitive shapes in Maya, this might be shape types, dimensions, positions, or colors.

### 2. Assigning data to variables

Once you know what data you need, you store it in variables. This allows you to reference and manipulate the data throughout your code.

> [!example] Example
> ```python
> cube_size = 2
> sphere_radius = 1.5
> cylinder_color = (1, 0, 0)  # Red in RGB
> ```

### 3. Getting correct references to Maya objects

In scripting, you're often working with objects that exist outside the script. You need to be able to correctly identify and reference these objects in your code.

> [!example] Example
> ```python
> cube = cmds.polyCube(width=cube_size, height=cube_size, depth=cube_size)[0]
> sphere = cmds.polySphere(radius=sphere_radius)[0]
> ```

### 4. Manipulating Maya objects using data and variables

This is where you use your programming logic to change the state of your scene/tool/game based on the data you have.

> [!example] Example
> ```python
> cmds.move(0, cube_size/2, 0, cube)  # Move cube to sit on the ground plane
> cmds.scale(2, 2, 2, sphere)  # Scale the sphere
> ```

### 5. Using functions, operations, and algorithms

These are the tools you use to process your data and achieve your desired outcomes. Functions encapsulate reusable pieces of logic, operations perform specific tasks, and algorithms provide step-by-step procedures for solving problems.

> [!example] Example
> ```python
> def create_colored_primitive(shape_type, size, color):
>     if shape_type == "cube":
>         obj = cmds.polyCube(width=size, height=size, depth=size)[0]
>     elif shape_type == "sphere":
>         obj = cmds.polySphere(radius=size)[0]
>     
>     material = cmds.shadingNode("lambert", asShader=True)
>     cmds.setAttr(f"{material}.color", *color)
>     cmds.select(obj)
>     cmds.hyperShade(assign=material)
>     
>     return obj
> ```

### 6. Arriving at the desired outcome

This is your goal - the change you want to see in your scene/tool/game. It's what happens when you correctly apply your logic to your data.

> [!example] Example
> Creating a scene with multiple colored primitive shapes:
> ```python
> red_cube = create_colored_primitive("cube", 2, (1, 0, 0))
> blue_sphere = create_colored_primitive("sphere", 1.5, (0, 0, 1))
> green_cylinder = create_colored_primitive("cylinder", 1, (0, 1, 0))
> ```

> [!note] Key Takeaway
> In essence, programming for technical art in is about:
> 1. Representing the scene elements as data
> 2. Storing that data in variables
> 3. Writing functions to manipulate objects
> 4. Applying that logic to achieve desired changes or outcome

This process forms the core of what you do when scripting, whether you're creating simple primitives, automating complex modeling tasks, or setting up data-driven animations.

> [!tip] Problem-Solving Approach
> When faced with a new scripting challenge, try breaking it down into these components:
> 1. What scene elements and properties do I need to work with?
> 2. How will I store and reference this data?
> 3. What commands or programming tasks do I need to use?
> 4. What manipulations do I need to perform?
> 5. What functions will help me organize my code?
> 6. What's the final state I want my outcome to be in?

By approaching problems this way, you can start to see patterns and similarities across different scripting tasks, making it easier to apply your skills to new situations.

> [!question] Reflection
> Think about the Maya scripts you've written so far in this course. Can you identify these elements in your code? How have you represented data, manipulated Maya objects, and used functions to achieve your goals?

Understanding this fundamental approach can help you tackle new scripting challenges and see how the individual concepts you're learning fit into the larger process of programming for technical art and game design.

##
---
## Conclusion

By revisiting our previous work through the lens of these fundamental concepts, we can see how basic building blocks combine to create more complex and powerful scripts. As we move forward, keep thinking about how you can apply these basics in new and creative ways to solve increasingly complex problems in game development and digital content creation.

Remember, becoming proficient in programming takes time and practice. Don't be discouraged if you don't understand everything immediately. Keep practicing, experimenting, and asking questions.
##
---










