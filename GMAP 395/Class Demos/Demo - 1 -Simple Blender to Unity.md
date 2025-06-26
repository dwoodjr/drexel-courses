# Blender to Unity "Brickify" Demo Guide

**Duration:** 15-20 minutes  
**Goal:** Turn any object into LEGO-style bricks using procedural modeling

---

## Demo Overview: Procedural Brickify System

**What we're making:** A system that converts any 3D object into LEGO-style bricks **Why this example:** Shows point cloud generation, procedural modeling, and instancing - core technical art concepts

---

## Phase 1: Create the LEGO Brick (6-8 minutes)

### Opening Hook (1 minute)

> **"Today we're going to create a system that can turn ANY 3D object into LEGO bricks. We'll build one perfect brick, then teach Blender how to copy it thousands of times intelligently. This is how studios create massive environments from small modular pieces."**

**Key Teaching Point:** "We're not just making bricks - we're making a SYSTEM that makes bricks."

---

### Step 1: Model a Single LEGO Brick (4 minutes)

**Action:**

1. Delete default cube
2. Add Cube (Shift+A → Mesh → Cube)
3. Scale to (1, 1, 0.4) - "Standard LEGO proportions"
4. Tab into Edit Mode
5. Select top face, Inset (I) by 0.1
6. Extrude (E) up by 0.1 to create the "stud"

**Talking Points:**

- "LEGO bricks have very specific proportions - this isn't random"
- "The stud on top is what makes it recognizably LEGO"
- "Real LEGO designers follow these exact ratios"

**Question to Class:** _"Why do you think LEGO uses these exact proportions?"_ **Expected Answer:** So all pieces fit together perfectly

**Action Continue:** 7. Tab back to Object Mode 8. Add Smooth Shading (right-click → Shade Smooth) 9. Rename to "LEGO_Brick"

**Visual Check:** Should look like a recognizable LEGO brick with rounded shading

---

### Step 2: Prepare Target Object (2 minutes)

**Action:**

1. Add another object (Shift+A → Mesh → Monkey or UV Sphere)
2. Scale to about 2-3 units
3. Position away from brick (X = 4)
4. Rename to "Target_Object"

**Talking Points:**

- "This is what we're going to 'brickify'"
- "Could be any object - character, building, logo, anything"
- "The system will work on any geometry"

**Question to Class:** _"What kinds of objects do you think this would be useful for in games?"_ **Possible Answers:** Buildings, terrain, stylized characters, destructible objects

---

## Phase 2: Create the Brickify System (6-8 minutes)

### Step 3: Generate Point Cloud (3 minutes)

**Action:**

1. Select Target_Object
2. Add Modifier → Geometry Nodes
3. Click "New" in modifier panel
4. In node editor, add Points → Distribute Points on Faces
5. Connect Target_Object geometry to Distribute Points input
6. Connect Distribute Points to Group Output
7. Set Density to around 20-30

**Talking Points:**

- "Distribute Points creates a cloud of points following the surface"
- "Each point will become a place where we put a brick"
- "Higher density = more bricks, but also more geometry"

**Question to Class:** _"What happens if we make the density too high?"_ **Demonstrate:** Increase to 100, show slowdown, decrease back

**Teaching Point:** "Procedural power comes with performance responsibility"

---

### Step 4: Instance Bricks to Points (2 minutes)

**Action:**

1. Add Instances → Instance on Points
2. Connect Distribute Points → Instance on Points → Group Output
3. In Instance input, click the object picker icon
4. Select "LEGO_Brick" from the scene

**Talking Points:**

- "Instance on Points puts a copy of our brick at every point"
- "Instancing is efficient - one brick definition, thousands of copies"
- "This is how games render forests, crowds, and repeated elements"

**Visual Check:** Target object should now be covered in LEGO bricks!

**Question to Class:** _"This looks cool, but what's missing to make it look more like real LEGO?"_ **Expected Answer:** Random rotation, color variation, better spacing

---

### Step 5: Add Variation (2 minutes)

**Action:**

1. Add Utilities → Random Value (between Instance on Points and Group Output)
2. Set Data Type to Vector
3. Set Min to (0, 0, 0), Max to (0, 0, 360) - only Z rotation
4. Connect Random Value to Instance on Points "Rotation" input

**Talking Points:**

- "Random rotation makes it look more natural"
- "Real LEGO builders don't align everything perfectly"
- "Controlled randomness feels more organic"

**Action Continue:** 5. Add another Random Value node 6. Set Data Type to Vector (for color) 7. Set Min to (0.2, 0.2, 0.2), Max to (1, 1, 1) 8. Connect to Instance on Points "Instance" → could connect to a Set Material node if time allows

**Teaching Point:** "Procedural systems let us add complexity without adding work"

---

## Phase 3: Unity Integration (4-6 minutes)

### Step 6: Export Preparation (2 minutes)

**Action:**

1. Apply the Geometry Nodes modifier (down arrow → Apply)
2. Select all bricks (A to select all)
3. Join objects (Ctrl+J) if multiple objects created
4. File → Export → FBX
5. Name: "Brickified_Object_v001.fbx"
6. Export settings: Apply Modifiers ✓, Selected Objects Only ✓

**Talking Points:**

- "Apply modifier 'bakes' our procedural system into real geometry"
- "Version numbers help track iterations"
- "Unity needs regular mesh data, not procedural instructions"

**Question to Class:** _"Why can't Unity read Geometry Nodes directly?"_ **Answer:** Different software, different languages - need common format (FBX)

---

### Step 7: Unity Scene Setup (2 minutes)

**Action:**

1. Open Unity 2022 (new 3D project)
2. Import FBX to Assets folder
3. Drag model into scene
4. Position at origin (0,0,0)

**Talking Points:**

- "Pipeline complete - Blender creates, Unity displays"
- "Same asset can be used in levels, as props, in cutscenes"

**Visual Check:** Brickified object should appear in Unity scene

---

### Step 8: Quick Lighting Setup (2 minutes)

**Action:**

1. Rotate Main Camera to get good angle
2. Create Directional Light (right-click → Light → Directional Light)
3. Angle light from side (Rotation: 45, -30, 0)
4. Set Intensity to 2
5. Add Point Light above object (Position: 0, 5, 0)
6. Set Point Light color to warm orange/yellow

**Talking Points:**

- "Lighting sells the 'toy' aesthetic"
- "Directional light = sunlight, Point light = room lighting"
- "Two-point lighting is classic studio setup"

**Question to Class:** _"How does the lighting make this feel more like toys?"_ **Answer:** Bright, clean lighting like a toy commercial or display

---

## Phase 4: Procedural Thinking Demo (2-3 minutes)

### Step 9: Show the Power of Iteration (2 minutes)

**Go back to Blender:**

1. Undo back to before applying modifier
2. Change point density from 30 to 50
3. Re-export as "v002"
4. Import to Unity and compare

**Talking Points:**

- "This is procedural power - change one number, get completely different result"
- "Same workflow scales from 100 bricks to 100,000 bricks"
- "Artist controls density based on performance needs and visual goals"

**Question to Class:** _"In a real game, when might you want fewer vs. more bricks?"_ **Answers:** Fewer for distant objects, more for hero pieces, performance considerations

---

### Step 10: Concept Expansion (1 minute)

**Quick Brainstorm:** _"How could we expand this system?"_

- Different brick sizes (1x1, 2x1, 2x2)
- Color coding by height or surface angle
- Hollow interiors vs. solid bricks
- Animation of building/breaking apart
- Different materials for different brick types

**Teaching Point:** "This 15-minute demo is the foundation for complex procedural systems used in AAA games"

---

## Key Concepts Review

### Ask Class to Identify:

1. **"What was procedural about this demo?"**
    
    - Point distribution algorithm, instancing rules, random variation
2. **"What made this modular?"**
    
    - One brick design used everywhere, system works on any input object
3. **"What was our pipeline?"**
    
    - Blender (procedural system) → FBX export → Unity (lighting and presentation)
4. **"How is this like real game development?"**
    
    - Modular assets, performance considerations, artist-friendly parameters

---

## Professional Context Connections

**Real-World Applications:**

- **Environment Art**: Modular building systems, terrain details
- **VFX**: Debris systems, crowd duplication
- **Technical Art**: Asset optimization, automated content generation
- **Game Design**: Destructible environments, construction mechanics

**Industry Example:** "Games like Minecraft, LEGO games, and even Fortnite's building system use these exact concepts at scale."

---

## Troubleshooting Notes

### Common Issues:

1. **Too many bricks/slow performance:** Lower density or use LOD systems
2. **Bricks not appearing:** Check object picker connection in Instance node
3. **Export problems:** Ensure modifier is applied before export
4. **Unity import issues:** Verify FBX settings include geometry

### Time Management:

- **Running long:** Skip color variation, focus on core concept
- **Running short:** Show different input objects (cube, sphere, text)
- **Technical issues:** Have backup FBX file ready

---

## Student Takeaways

**Core Concepts Demonstrated:**

- **Point cloud generation** from any geometry
- **Instancing** for efficient duplication
- **Procedural variation** through controlled randomness
- **Pipeline workflow** from creation to implementation
- **Scalable systems** that work at any complexity level

**Most Important Insight:** "Professional game development is about building systems, not individual assets."

---

## Extension Ideas (If Time Allows)

### Quick Iterations:

1. **Different input objects:** Text, logos, complex models
2. **Brick variations:** Different scales, shapes
3. **Smart placement:** Align bricks to surface normals

### Next Week Preview:

_"Next week we'll expand procedural modeling to create complete modular environments and explore advanced lighting workflows."_

---

## Demo Success Markers

**Students should leave understanding:**

- Procedural modeling creates systems, not just objects
- Instancing is key to performance in game development
- Pipeline workflows connect creative tools to game engines
- Simple rules can generate complex, appealing results
- Technical art bridges creativity and technical implementation

**Energy Goal:** Students excited to experiment with their own objects and see what they can "brickify"!