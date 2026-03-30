# DIGM 131 Midterm Exam: Game Project Structure and Maya Scene Generation

## Brief 💼
As a junior technical artist at Awesome Games Studio, you've been tasked with creating a tool that will help streamline the initial setup process for new game projects. This tool will create a standardized folder structure and generate a basic Maya scene with some primitive objects.

## Your Mission 🎯
Develop a Python script (or scripts) that accomplishes the following:
1. Creates a simulated game project folder structure
2. Generates a Maya scene with at least 3 primitives of different dimensions and colors/materials

> [!note] Important Note on Saving
> You are NOT required to automate the saving of the Maya scene in your script. You can manually save the scene into the appropriate folder within the project structure after running your script.

## Requirements 📋
1. Create a Python script named `game_project_setup.py` that:
   - Uses `argparse` to accept command-line arguments for the game project name
   - Creates a folder structure with the game name as the parent directory
   - Includes subdirectories for models, textures, levels, materials, scenes, etc.
   - Uses Maya commands to create a scene with at least 3 primitive objects with different dimensions and colors/materials

1. Use appropriate comments and/or docstrings to explain your code's functionality

3. Create a README.md file that includes:
   -  Your problem-solving approach (breaking down the goals and steps)
   - Pseudocode for your script
   - Instructions on how to use your script

## Desired Directory Structure
Your script should create a directory structure similar to this:

```
📁 GameProjectName
 ┣ 📁 Models
 ┣ 📁 Textures
 ┣ 📁 Materials
 ┣ 📁 Levels
 ┣ 📁 Scenes
 ┃ ┗ 📄 GameProjectName_Scene.ma
 ┣ 📁 Scripts
 ┗ 📁 Documentation
```

## Constraints and Considerations
- Use only the Python concepts and Maya commands we've covered in class (Weeks 1-5)
	- *Extra credit / bonus challenge partially exempt*
- Consider how to make your code modular and reusable

## Deliverables 📦
1. All script(s) (`game_project_setup.py`)
2. A README.md file with your pseudocode, problem-solving approach, and usage instructions

## Submission 📤
Zip all deliverables into a folder titled `[username]_MIDTERM_GameProjectSetup` (replace [username] with your Drexel username) and submit via the course learning portal under `Midterm` section.

Your submission should include:
1. Your completed `game_project_setup.py` script
2. Your `README.md` file containing pseudocode, problem-solving approach, and usage instructions
3. Any additional files you created for the bonus challenge (if attempted)

Example filename: `dkw34_MIDTERM_GameProjectSetup.zip`

> [!important] Submission Checklist
> - Ensure your script is named correctly (`game_project_setup.py`)
> - Verify that your README.md file is complete and informative
> - Double-check that all required files are included in your zip folder
> - Make sure your zip file is named according to the specified format

Remember to submit your work well before the deadline to avoid any last-minute technical issues.

## Evaluation Criteria 🔍
- Correct implementation of project folder creation
- Proper use of Maya commands for scene generation
- Effective use of `argparse` for handling user input
- Code organization and readability
- Appropriate use of comments and/or docstrings
- Quality of pseudocode and problem-solving explanation in README.md

## Extra Credit / Bonus Challenge (1 - 2 pts) 🌟
For an additional (optional) challenge, attempt to create a single script that accomplishes all of the following:
1. Creates the project folder structure
2. Generates the Maya scene with primitives
3. Automatically saves the Maya scene into the correct folder within the project structure

This bonus task will require you to research and implement Maya file saving commands (use Maya CMDs Reference), which we haven't explicitly covered in class. If you attempt this, be sure to document your process and any new commands or techniques you use in your README.md file.

## Hints and Tips
- Start by breaking down the problem into smaller tasks (folder creation, Maya scene generation, etc.)
- Use the `os` module for file and directory operations
- Remember to import the necessary Maya modules (`import maya.cmds as cmds`)
- Consider creating separate functions for different tasks (e.g., folder creation, primitive generation, material, etc.)
- Use your previous assignments and labs as reference for similar operations, functions, and syntax

## Reminder about Pseudocode
Pseudocode is a plain language description of the steps in an algorithm or process. It's a way to plan your code before you write it, focusing on the logic rather than the syntax. Your pseudocode should outline the main steps your script will take, in a way that's easy to understand even for non-programmers.

## Reminder
- This exam is open book/notes. You may refer to your previous assignments, labs, and any course materials.
- You may use AI to generate code snippets, but all planning and writing must be your own.
- If you use AI, you must cite its use as per the course policy (do this in `README.md`).
- Focus on applying the concepts we've covered in class rather than introducing new, complex techniques.

> [!quote] Encouragement
> Remember, this exam is designed to test your understanding of the concepts we've covered so far. Don't worry if you can't implement every feature perfectly – focus on demonstrating your grasp of the core ideas. Break the problem down into smaller steps, use your resources wisely, and don't hesitate to add comments explaining your thought process. You've got this! Good luck! 🎮🖥️