## Brief

Week 2 should be focused on procedural thinking/design and procedural content generation for games as the overall major concepts/topics for the week with practical application of those concepts/ideas using Blende Geometry Nodes. 
	The blender portion should focus less on the whole "lets all make this one thing" tutorial style, but should focus more on how to think, design, and make with the tool using basic operations, procedures, and tasks common to most procedural modeling and procedural design tools
		- Nodes and Data Flow
		- Scattering / Copying
		- Splines
		- Manipulating Parameters
		- Creating Attributes and Parameters
		- Randomization/Noise
		- Boolean Operations
		- Hierarchy and Instancing
		- Deformations (Procedural)
		- Constraints (Procedural)
		- Looping and Repetition
		- Proportional Scaling

##
---

## Plan

### Theme: "Something from the Void"

#### Project Idea: Procedural Eldritch Portal
A mysterious, glowing portal emerging from a rocky void-like terrain, adorned with alien-like tendrils or organic shapes. This piece of procedural game art will integrate key concepts and topics of procedural modeling and PCG.

---

### Key Concepts with Practical Applications
1. **Nodes and Data Flow**
    - **Application:** Introduce the Geometry Nodes system and create the foundational node setup for the portal and environment.
    - **Example:** A node tree that generates the rocky base structure.
2. **Scattering / Copying**
    - **Application:** Scatter small rocks, alien spores, or glowing particles around the portal procedurally.
    - **Example:** Use a distribution system to place objects on the base geometry.
3. **Splines**
    - **Application:** Create twisting tendrils or arcane symbols around the portal.
    - **Example:** Use curves to define the tendrils' shape and geometry for their extrusion.
4. **Manipulating Parameters**
    - **Application:** Allow real-time adjustments to the portal's size, tendrils’ length, or rock density.
    - **Example:** Expose inputs for scaling and density sliders.
5. **Creating Attributes and Parameters**
    - **Application:** Use attributes to control material effects or vary the scale of scattered objects.
    - **Example:** Add vertex color or random ID attributes to assign glowing effects to specific spores.
6. **Randomization/Noise**
    - **Application:** Add variation to the placement, scale, and rotation of scattered elements.
    - **Example:** Use noise to create irregular rock formations and distort the portal’s surface.
7. **Boolean Operations**
    - **Application:** Create openings or subtractive details in the portal structure.
    - **Example:** Use Boolean nodes to carve a glowing central void in the portal.
8. **Hierarchy and Instancing**
    - **Application:** Organize components (portal, base, tendrils, spores) into reusable instances.
    - **Example:** Make the rocks modular and reusable for other projects.
9. **Deformations (Procedural)**
    - **Application:** Add organic warping or twisting effects to the portal or tendrils.
    - **Example:** Use deformation nodes to bend the tendrils dynamically.
10. **Constraints (Procedural)**
    - **Application:** Ensure objects like rocks stay aligned with the terrain or tendrils grow within specific bounds.
    - **Example:** Snap the tendrils' ends to the portal edge while keeping their base attached to the ground.
11. **Looping and Repetition**
    - **Application:** Create repeating patterns for alien symbols or portal details.
    - **Example:** Use a looping function to generate evenly spaced glowing runes around the portal.
12. **Proportional Scaling**
    - **Application:** Maintain consistent proportions for all scattered and instanced objects.
    - **Example:** Scale smaller tendrils in relation to their distance from the portal.

---

### Project/Tutorial Workflow

#### Part 1: Creating the Rocky Base
- Start with a simple plane and manipulate its shape procedurally.
- Scatter rocks and spores around the base using randomization.
##### Key Concepts:
- **Nodes and Data Flow**
    - Setting up the node system for the base geometry.
- **Randomization/Noise**
    - Adding organic variations to the rock formations.
- **Scattering / Copying**
    - Procedurally scattering rocks and spores across the base.
- **Constraints**
    - Ensuring rocks stay aligned with the surface and avoid overlapping.
##### Output: A rugged, void-like terrain with scattered rocks and spores.

#### Part 2: Designing the Portal
- Use splines to define the shape of a glowing ring or arc.
- Apply Boolean operations to carve out a central void.
##### Key Concepts:
- **Boolean Operations**
    - Carving the central void or arcane details into the portal.
- **Looping and Repetition**
    - Generating repeating patterns for glowing runes or symbols around the portal.
- **Proportional Scaling**
    - Maintaining proportionality for portal details as it scales.
##### Output: A central portal structure with a glowing void and mystical symbols.

#### Part 3: Adding Tendrils
- Use curves to create procedural tendrils twisting out of the portal.
- Apply deformation and noise for organic shapes.
##### Key Concepts:
- **Splines**
    - Creating the base shapes for twisting tendrils emerging from the portal.
- **Deformations**
    - Applying procedural bending, twisting, and warping to the tendrils for an organic look.
- **Hierarchy and Instancing**
    - Organizing tendrils as instanced components for efficient creation and reuse.
##### Output: Procedurally generated tendrils twisting and warping around the portal.

#### Part 4: Enhancing with Details
- Use randomization and constraints to place glowing spores, arcane symbols.
- Add proportional scaling to ensure all details feel cohesive.
##### Key Concepts:
- **Manipulating Parameters**
    - Exposing controls for adjusting rock density, tendril lengths, or portal size dynamically.
- **Creating Attributes and Parameters**
    - Assigning attributes for glowing effects, variation in spores, or other customizations.
##### Output: Fully procedural, adjustable game art with dynamic control over its elements.

#### Part 5: Final Touches
- Adjust parameters for artistic control and scalability.
- Discuss export options for game engines (with some more focus on Unity) 
	- e.g., baking geometry, optimizing instances, etc.

#### Part 6: Reflection
- Discuss how the procedural techniques apply to other projects.
- Encourage students to tweak and expand their creations.



##
---

## Teaching Approach
1. **Begin with Concepts:**
    - Explain the _why_ behind each step (e.g., why randomization enhances realism).
2. **Build Modularly:**
    - Construct each component (base, portal, tendrils) as separate, reusable systems.
3. **Encourage Experimentation:**
    - Allow students to tweak parameters and add their creative flair to the portal.

##
---

