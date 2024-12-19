# Assignment 5: Extending the Primitive Creator Tool in Maya

## Brief 💼
You've impressed your team at Awesome Games Studio with the work you've done on creating Maya primitives. Now, they want you to take your tool to the next level! This assignment is about reinforcing your understanding of Object-Oriented Programming (OOP) while extending the tool's functionality in Maya. You'll build on the work started in the lab to create an even more powerful tool.

## Your Mission 🎯
Extend the **Primitive Creator Tool** you developed during the lab by adding one of the additional features outlined below. This assignment aims to help you apply OOP concepts practically, providing more control and flexibility to the tool and enhancing its usability.

---
## Requirements 📋

### Part 1: Extend the Primitive Creator Tool
Building on the lab work, extend your tool with the following:
1. Add **material selection** and **color picker** (completed during the lab).
2. Choose **one additional feature** from the following to implement:
   - **Set Dimensions for Primitives**: Add input fields to the UI to allow users to specify dimensions (e.g., width, height, depth) for the created primitive.
   - **Add Subdivision Controls**: Add UI controls that let users set the number of subdivisions for each primitive, making the geometry smoother.
   - **Custom Transform Options**: Allow users to set the initial position, rotation, or scale of the primitive via the UI.
3. Implement the feature following OOP principles, making use of the `PrimitiveCreatorBase`, `PrimitiveCreatorUI`, and `MayaPrimitiveCreator` classes.
4. Test your tool to ensure that all new and existing features work as expected.

### Coding Requirements
1. Follow OOP principles:
   - Use proper encapsulation where needed.
   - Implement inheritance correctly.
   - Apply abstraction where appropriate.
2. Include clear documentation throughout your code to explain new methods and functionality.
3. Test your tool in Maya to verify its functionality.

---
## Deliverables 📦
Submit a zip file named `[username]_ASN5_PrimitiveCreator.zip` containing:

1. **Python Script**:
   - `primitive_creator.py` with all implemented features.
2. **UI File**:
   - `[FILENAME].ui`.
3. **Documentation**:
   - `README.md` with:
     - Implementation details.
     - Testing results (screenshots or a video link).
     - Details about the additional feature you implemented.

> [!info] Folder Structure
> Here's how your assignment files should be organized:
> ```
> 📁 username_ASN5_PrimitiveCreator/
> ├── 📄 primitive_creator.py
> ├── 📄 main.ui
> └── 📄 README.md
> ```
> 
> - **`primitive_creator.py`**: Your main Python script with all features.
> - **`main.ui`**: The UI file for the extended tool.
> - **`README.md`**: Documentation for your implementation and testing.

---
## Grading 📊
- **Functionality**: The tool must work as expected in Maya, including the new feature, without errors.
- **OOP Design**: The implementation must follow good OOP practices, including abstraction, inheritance, and modularity.
- **UI Design**: The UI should be user-friendly and clearly present all options, including the material, color, and newly added features.
- **Code Documentation**: Your code should include clear comments, explaining each new method and its purpose.

---
## Submission Guidelines
- Submit through the course submission portal.
- Document any resources used, especially if external help or AI was used for generating code snippets.

> [!quote] Encouragement
> Extending your Primitive Creator Tool is a great opportunity to see how Object-Oriented Programming can make tools more versatile and maintainable. Applying these skills in a practical context will prepare you for future projects in both technical art and game development.
>
> Remember, learning OOP is a journey—take your time to understand each concept and see how it can help organize and structure your code more effectively. Keep experimenting, ask questions when you're stuck, and enjoy the creative process. You're building skills that will help you create amazing tools and games in the future! 🎮🔧✨

