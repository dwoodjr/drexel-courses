# Assignment 6: Maya Level Blockout Tool and Data Exporter

## Brief 💼
Your team at Awesome Games Studio is excited about the progress you've made on the **Level Blockout Tool**! Now, it's time to extend its functionality and export your blockouts into JSON data for future use. This assignment focuses on improving your tool with additional features and exporting data in a structured format.

## Your Mission 🎯
Follow along with **PLN 9** to:
1. Ensure your **Level Blockout Tool** extensions work as expected.
2. Use the **Level Blockout Exporter** to export JSON files containing blockout data.
3. Create three unique test cases to verify the functionality of your tool and exporter.

You will demonstrate these steps by submitting your Python scripts, UI file, and screenshots of your Maya scenes.

---

## Requirements 📋

### Part 1: Maya - Level Blockout Tool Extensions
Complete the extensions from **PLN 9**, ensuring:
1. You can create multiple primitives with:
   - Assigned materials and colors.
   - Grouped under a user-specified name.
   - Dimensions specified (or randomized).

### Part 2: Maya - JSON Data Exporter
1. Ensure the **Level Blockout Exporter** is functional.
   - The exporter should correctly export selected primitives into a JSON file with the following structure:
     ```json
     [
         {
             "type": "Cube",
             "position": [0, 0, 0],
             "scale": [1, 1, 1],
             "group": "BlockoutGroup"
         }
     ]
     ```
2. Test the exporter by creating three unique JSON files, each representing a different blockout.

---

### Test Cases
1. Use your **Level Blockout Tool** to create three unique blockout setups in Maya:
   - **Test Case 1**: A simple scene with a single primitive and no grouping.
   - **Test Case 2**: A scene with multiple primitives grouped under one parent.
   - **Test Case 3**: A scene with randomized dimensions and multiple groups.
2. Export each blockout into a separate JSON file using the **Level Blockout Exporter**.
3. Take a screenshot of each Maya scene before exporting.

---

## Deliverables 📦
Submit a zip file named `[username]_ASN9_MayaBlockout.zip` containing:

1. **Maya Code**:
   - `primitive_creator.py`: Your updated Level Blockout Tool with all extensions.
   - `level_blockout_exporter.py`: The Level Blockout Exporter script.
   - `main.ui`: The updated UI file.

2. **JSON Files**:
   - Three exported JSON files:
     - `blockout_test1.json`
     - `blockout_test2.json`
     - `blockout_test3.json`

3. **Screenshots**:
   - Three screenshots of your Maya scenes (one for each test case):
     - `test_case1.png`
     - `test_case2.png`
     - `test_case3.png`

> [!info] Folder Structure
> Here's how your assignment files should be organized:
> ```
> 📁 username_ASN6_MayaBlockout/
> ├── 📁 Scripts/
> │   ├── 📄 primitive_creator.py
> │   ├── 📄 level_blockout_exporter.py
> │   └── 📄 main.ui
> ├── 📁 Exports/
> │   ├── 📄 blockout_test1.json
> │   ├── 📄 blockout_test2.json
> │   └── 📄 blockout_test3.json
> ├── 📁 Screenshots/
> │   ├── 📄 test_case1.png
> │   ├── 📄 test_case2.png
> │   └── 📄 test_case3.png
> ```

---

## Grading 📊
- **Tool Functionality**:
  - JSON files are correctly exported.
  - All extended features of the Level Blockout Tool are functional.
- **JSON Structure**:
  - Data is well-organized and accurately reflects the Maya scene.
- **Code Organization and Clarity**:
  - Code is clean, well-documented, and follows good practices.
- **Screenshots**:
  - Clearly show the Maya scenes used for testing.

---

## Submission Guidelines
- Submit your assignment as a single zip file through the course portal.
- Ensure your JSON files and screenshots are correctly linked to the test cases.

> [!quote] Encouragement
> Extending your Level Blockout Tool and exporting structured data is a significant step toward building robust workflows in technical art and game development. By completing this assignment, you’re solidifying your Python skills and learning how to integrate tools for real-world use.  
>
> Take your time, follow the PLN step-by-step, and ask for help if you're stuck. You're creating tools that bridge creativity and technology—keep going! 🎮✨
