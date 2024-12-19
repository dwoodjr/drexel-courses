# Assignment 4: Object-Oriented Game + Tool Development
## Brief 💼
As a junior technical artist at Awesome Games Studio, you've impressed the team with your Maya scripting skills. Now, they want you to create a more robust tool system using Object-Oriented Programming principles. Additionally, the game design team has requested a simple character creation system to help prototype their upcoming RPG.

## Your Mission 🎯
Create two systems (based on the LAB work): a Maya tool that uses OOP to manage primitive creation and manipulation, and a text-based character creator that demonstrates OOP principles in a game development context. This dual approach will help you understand how OOP concepts apply across different areas of game development.

---
## Requirements 📋

### Part 1: Maya OOP Tool System
Building on the lab work, create a system that:
1. Uses a base class for all primitive shapes
2. Implements specific shape classes (cube, sphere, etc.)
3. Creates a manager class to handle all shapes

### Part 2: Character Creator System
Develop a character system that:
1. Uses a base character class
2. Implements at least `3` specific character types (Warrior, Mage, etc.)
3. Creates a manager class for character handling

### Coding Requirements
1. Follow OOP principles:
   - Use proper encapsulation when needed
   - Implement inheritance correctly
   - Apply abstraction where appropriate
2. Include clear documentation
4. Create test cases

---
## Deliverables 📦
Submit a zip file named `[username]_ASN4_OOPTools.zip` containing:

1. Maya Tool Files:
   - `maya_primitives.py`
   - `primitive_manager.py`

1. Character System Files:
   - `character_system.py`
   - `character_manager.py`
   - Plus any scripts used for the `Bonus Challenge`.

3. Documentation:
   - `README.md` with:
     - Implementation details
     - Testing results (screenshots or a video link)
     - Bonus features added

1. Test Files:
   - Test scripts

> [!info] Folder Structure
> Here's how your assignment files should be organized:
> ```
> 📁 username_ASN4_OOPTools/
> ├── 📁 maya_tools/
> │   ├── 📄 maya_primitives.py
> │   ├── 📄 primitive_manager.py
> │   └── 📁 tests/
> │       └── 📄 test_maya_tools.py
> │
> ├── 📁 character_system/
> │   ├── 📄 character_system.py
> │   ├── 📄 character_manager.py
> │   ├── 📁 characters/
> │   │   └── 📄 saved_characters.json
> │   └── 📁 tests/
> │       └── 📄 test_characters.py
> │
> └── 📄 README.md
> ```
> 
> Directory contents:
> 📁 `maya_tools/`: All Maya-related OOP implementations
> 📁 `character_system/`: Character creator system files
> 📁 `tests/`: Test scripts for each system
> 📄 `README.md`: Documentation at root level


---
## Grading 📊
- Maya OOP System
  - Base class implementation
  - Derived classes
  - Manager class

- Character System
  - Base class implementation
  - Character classes
  - Manager class

- Documentation 
  - Code documentation
  - README.md quality
  - Code style and organization
  - Submission folder structure

---
## Submission Guidelines
- Submit through the course BB Learn portal (Week 7)
- Document any resources used, especially if AI is used for generating code snippets.

---

> [!quote] Encouragement
> This assignment is your opportunity to see how Object-Oriented Programming bridges different aspects of game development. Whether you're creating tools for artists or systems for gameplay, OOP helps organize and structure your code in a way that's maintainable and extensible.
>
> The skills you're learning here are foundational to both technical art and game programming/design. You'll use these same concepts when working with Unity's C# scripts, Unreal's Blueprint system, and many other game development tools.
>
> Remember that learning OOP is a journey - it's okay if some concepts take time to click. Focus on understanding the basic principles first, then build up to more complex implementations. The goal is to start thinking about code organization and reusability in a way that will serve you throughout your game development career.
>
> Keep experimenting, stay curious, and don't hesitate to ask questions. You're developing valuable skills that will help you create better tools and games in the future! 🎮🔧✨