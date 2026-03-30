# Assignment 7: Unity Level Blockout Importer

## Brief 💼

Your team at Awesome Games Studio is thrilled to see the progress with your Level Blockout Tool. Now it’s time to bring your blockouts into the game engine! This assignment focuses on using your **Level Blockout Data Importer** script to import JSON data and visualize your blockouts in Unity.
## Your Mission 🎯

Follow along with **PLN 10** to:
1. Import the three JSON files from Assignment 6 (or create new ones using the Maya Level Blockout Tool and JSON Exporter).
2. Use the **Level Blockout Data Importer** script to recreate the blockouts in Unity.
3. Take screenshots of the blockouts **in Unity** and submit them along with your Python script.

---
## Requirements 📋

### Part 1: JSON Data Preparation
1. Use the JSON data created in Assignment 6:
    - `blockout_test1.json`
    - `blockout_test2.json`
    - `blockout_test3.json`
2. If you didn’t complete Assignment 6, you can create three new blockouts using the **Maya Level Blockout Tool** and export them with the **JSON Data Exporter** script.
### Part 2: Unity - Level Blockout Data Importer
1. Implement the **Level Blockout Data Importer** script:
    - Parse the JSON files to extract blockout data.
    - Create corresponding GameObjects in Unity based on the data:
        - Primitive type (e.g., Cube, Sphere).
        - Position and scale.
        - Grouping (if applicable).
    - Optional: Assign colors or materials for better visualization.
2. Import all three JSON files into Unity to create the blockouts:
    - Ensure each blockout appears as a separate object or distinguishable setup in the scene.

---
## Deliverables 📦
Submit a zip file named `[username]_ASN7_UnityBlockout.zip` containing:
1. **Unity Code**:
    - `blockout_importer.py`: Your Unity script to parse JSON and recreate blockouts.
2. **Screenshots**:
    - Screenshots of the three blockouts recreated in Unity:
        - `unity_blockout1.png`
        - `unity_blockout2.png`
        - `unity_blockout3.png`
3. **JSON Files**:
    - Include the three JSON files used for importing:
        - `blockout_test1.json`
        - `blockout_test2.json`
        - `blockout_test3.json`

---
## Test Cases
1. **Test Case 1**: A single primitive with no grouping.
2. **Test Case 2**: Multiple primitives grouped under one parent.
3. **Test Case 3**: Randomized dimensions and multiple groups.

Ensure the blockouts in Unity match the data from the JSON files.

---
## Grading 📊
- **Importer Functionality**:
    - JSON data is correctly parsed and reflected in Unity.
    - All elements (e.g., position, scale, grouping) are accurate.
- **Unity Setup**:
    - Blockouts are visually clear and organized.
- **Code Organization and Clarity**:
    - Code is clean, well-documented, and follows Unity best practices.
- **Screenshots**:
    - Clearly show the Unity scenes with blockouts.

---
## Submission Guidelines
- Submit your assignment as a single zip file through the course portal.
- Include all required files and screenshots in the correct structure.

> [!info] Folder Structure Here's how your assignment files should be organized:
> 
> ```
> 📁 username_ASN7_UnityBlockout/
> ├── 📁 Scripts/
> │   └── 📄 blockout_importer.py
> ├── 📁 Screenshots/
> │   ├── 📄 unity_blockout1.png
> │   ├── 📄 unity_blockout2.png
> │   └── 📄 unity_blockout3.png
> ```

> [!quote] Encouragement By bringing your blockouts into Unity, you’re learning to integrate tools across platforms, an essential skill for game development and technical art. Celebrate your progress, and don’t hesitate to ask questions. You’re creating bridges between creativity and tech—keep it up! 🎮✨
