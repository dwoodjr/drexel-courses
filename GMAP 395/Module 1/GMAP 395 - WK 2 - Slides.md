---
theme: black
width: 1920
height: 1080
---

### **_Game Feel and Procedural Workflows_**
#### GMAP 395: Advanced Game Art and Production
##### Week 2

---
### Game Feel
![[gamefeelcover.webp|320]]
> [!quote] Game Feel
> Real-time control of virtual objects in a simulated space, with interaction emphasized by polish.
> -- Steve Swink

<iframe width="560" height="315" src="https://www.youtube.com/embed/216_5nu4aVQ?si=N4hXCqCBg6V9xZDP" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

---

### Game Feel: The Tactile Experience of Play

- **Definition:** The visceral, tactile experience of interacting with a game, making it feel responsive and tangible.
- **Components:**
    1. **Real-Time Control:** Immediate response to player input.
    2. **Simulated Space:** Believable virtual environments with realistic or stylized physics.
    3. **Polish:** Visual, audio, and interactive feedback that enhances immersion.

**Examples:**

- _Super Mario Bros:_ Precise platforming.
- _Celeste:_ Forgiving yet challenging controls.
- _DOOM (2016):_ Weighty, impactful combat.

---

### Additional Aspects of Game Feel

- **Momentum and Inertia (Physics):**
    - Creating a sense of weight and speed in character and object movement.
    - Example: Rolling boulders in _The Legend of Zelda: Breath of the Wild_.
- **Input Responsiveness:**
    - Reducing input lag to ensure tight controls.
    - Example: Fighting games like _Street Fighter_ prioritize frame-perfect inputs.

---
### Introduction to Procedural Workflows

- **What Are Procedural Workflows?**
    - Automating content creation using algorithms and rules.
    - Efficiently producing scalable, dynamic assets and systems.
- **Why It Matters:**
    1. Reduces repetitive tasks.
    2. Enables scalability for vast game worlds.
    3. Facilitates rapid prototyping and iteration.

---

### Procedural Workflows in Action

- **Applications:**
    1. **Terrain and Landscapes:** Dynamic natural environments (_e.g.,_ _Minecraft_).
    2. **Characters and Creatures:** Diverse entities (_e.g.,_ _Spore_).
    3. **Loot Systems:** Unique equipment and items (_e.g.,_ _Borderlands_).
    4. **Buildings and Cities:** Algorithmic urban designs. (*e.g., Spiderman*)

**Efficiency:** Combines hand-crafted content with procedural systems for optimal results.

---

### Challenges in Procedural Workflows

- **Over-Generation:**
    - Excessively random content can feel disjointed.
    - Solution: Blend procedural elements with curated designs and a cehesive artistic vision.
- **Player Fatigue:**
    - Repetitive patterns may reduce engagement.
    - Solution: Introduce meaningful variability and uniqueness within procedural systems/design.

---

### Modularity in Game Design

- **What is Modularity?**
    - Reusable components for streamlined development.
- **Benefits:**
    1. **Reusability:** Assets can be used across levels/projects.
    2. **Flexibility:** Easier updates and maintenance.
    3. **Performance:** Reduces memory load by optimizing reusable assets.

**Synergy with Proceduralism:**
- Modular assets populated procedurally for diverse environments (_e.g.,_ _No Man’s Sky_).

>[!example] [Balancing modularity and uniqueness in Environment Art](https://www.beyondextent.com/articles/balancing-modularity-and-uniqueness-in-environment-art)

![[modualassetpack.png|640]]

---

### Modular Workflows: Best Practices

- **Asset Organization:**
    - Maintain a clean structure for quick access and scalability.
- **Consistent Metrics:**
    - Standardize dimensions and pivot points.
- **Interoperability:**
    - Ensure modular assets work seamlessly in various configurations.

---
### PCG in  Games
Book: 
> [!link]  [Procedural Content Generation in Games](https://www.pcgbook.com/)

<iframe width="560" height="315" src="https://www.youtube.com/embed/B11RlHZsmGE?si=jLx4mpb84y8DKfAp" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

---

### Taxonomy of Procedural Content Generation (PCG)

![[pcgTaxonomy.png]]

- **Game Bits:** Assets (textures, sounds, models).
- **Game Space:** Levels, terrains, maps.
- **Game Systems:** Rules and mechanics (_e.g.,_ weather systems).
- **Game Scenarios:** Events, narratives, quests.

**Examples:**
- _Roguelikes:_ Procedurally generated levels (_e.g.,_ _Hades_).
- _Survival Games:_ Dynamic environments (_e.g.,_ _Subnautica_).

> [!link] [Procedural content generation for games: A survey](https://dl.acm.org/doi/10.1145/2422956.2422957)

---

### Expanding PCG Taxonomy

- **Hybrid Approaches:**
    - Combining procedural and hand-crafted elements.
    - Example: _Shadow of Mordor’s_ Nemesis system mixes procedural generation with predefined rules.
        
- **Adaptive PCG:**
    - Systems that adjust content based on player behavior.
    - Example: Dynamic difficulty adjustment in _Left 4 Dead_.

---
### Node-Based Workflows

- **Definition:** Visual scripting using nodes to represent operations and data flow.
- **Advantages:**
    1. Artist-friendly and intuitive.
    2. Clear visual representation of processes.
    3. Supports modularity and reusability.

**Tools:**
- *Blender Geometry Nodes:* Procedural modeling nodes.
- _Houdini:_ Procedural modeling and VFX.
- _Unreal Engine Blueprint:_ Gameplay logic.
- _Unity Shader Graph:_ Material creation.

---

### Beyond Basics: Node Systems

- **Dynamic Dependencies:**
    - Create relationships between nodes for real-time updates.
    - Example: Automatically updating materials when assets change.
- **Optimizations:**
    - Collapse redundant nodes for streamlined performance.
    - Example: Combining noise and displacement nodes in terrain shaders.

---

### 3D Geometry Basics and Procedural Math

- **[Geometry Fundamentals](https://www.youtube.com/watch?v=Wmwe1fmR1SM):**
    - **Vertices:** Points in 3D space.
    - **Edges:** Lines connecting vertices.
    - **Faces:** Surfaces defined by edges.
    - **Normals:** Perpendicular vectors to surfaces.
- **Math Concepts:**
    - **[Vectors](https://www.khanacademy.org/math/algebra-home/alg-vectors/alg-vector-basics/v/introduction-to-vectors-and-scalars):** Direction and magnitude.
    - **[Matrices](https://www.khanacademy.org/math/precalculus/x9e81a4f98389efdf:matrices/x9e81a4f98389efdf:mat-intro/v/introduction-to-the-matrix):** Transformations in space.
    - **[Quaternions](https://www.youtube.com/watch?v=zjMuIxRvygQ):** Representing rotations.

**Applications:**
- Procedural transformations (_e.g.,_ proportional scaling).

![[3D-Shapes-01-01.png|320]]

---

### Common Procedural Operations

- **Nodes and Data Flow:** Organizing procedural steps.
- **Scattering/Copying:** Distributing objects procedurally (_e.g.,_ foliage).
- **Splines:** Creating paths and smooth curves.
- **Parameter Manipulation:** Dynamically adjusting properties.
- **Attributes:** Defining object-specific data.
- **Randomization/Noise:** Adding variation and realism.
- **Boolean Operations:** Combining or subtracting shapes.
- **Instancing:** Efficiently reusing objects.
- **Deformations:** Transforming shapes procedurally (_e.g.,_ terrain sculpting).
- **Constraints:** Guiding procedural behaviors.
- **Looping:** Repeating processes for consistency.

---

### Expanded Operations and Techniques

- **Noise Patterns:** [The Art of Procedural Noise](https://www.youtube.com/watch?v=erI7k3lt4UY)
    - Procedural textures for organic designs.
    - Example: Voronoi patterns used for terrain generation or cellular structures.
- **Fractals:** [Explaining Fractals in 5 Levels](https://www.wired.com/video/watch/5-levels-computer-scientist-explains-fractals-in-5-levels-of-difficulty)
    - Recursive geometries for complex visuals.
    - Example: Mandelbrot sets for landscapes or branching systems like lightning.
- **Flow Fields:** [The Beauty of Code: Flow Fields](https://www.youtube.com/watch?v=na7LuZsW2UM)
    - Directing particle systems dynamically.
    - Example: Simulating wind patterns or flocking behaviors in particle systems.
- **L-Systems:** [L-Systems Fundamentals](https://www.youtube.com/watch?v=egxBK_EGauM)
    - Rule-based systems for generating fractal-like structures.
    - Example: Procedurally creating realistic trees, plants, or coral.
- **Shape Grammars:** [Procedural Building: Shape Grammars](https://www.youtube.com/watch?v=zCeqBV0Amm0)
    - Rule-based approach for generating architectural or structured designs.
    - Example: Creating procedurally generated buildings or city layouts.

---

![[fractals.png|320]]
![[noise.jpg]]


---

### Integration of Techniques

1. **Nodes:** Visual representation of workflows.
2. **Attributes:** Define unique object behaviors.
3. **Randomization:** Add variation for realism.
4. **Scalability:** Efficiently create vast, dynamic environments.

**Practical Example:**
- Generate a forest:
    1. Use splines for paths.
    2. Scatter trees procedurally.
    3. Add random noise for variation.

---

### Case Study: _No Man’s Sky_

- **Overview:**
    - Infinite universe generated procedurally.
- **Key Techniques:**
    1. **Procedural Terrain:** Dynamic landscapes with varied biomes.
    2. **Modular Assets:** Ships, flora, and fauna built from reusable parts.
    3. **Node-Based Workflows:** Data-driven algorithms for content generation.

**Impact:** Demonstrates the synergy of proceduralism and modularity for immersive exploration.

> [!NOTE] [The algorithms of No Man’s Sky](https://www.rambus.com/blogs/the-algorithms-of-no-mans-sky-2/)

<iframe width="560" height="315" src="https://www.youtube.com/embed/C9RyEiEzMiU?si=_b7kaNPVxXKIxqMM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

---

### Final Thoughts

- **Procedural Workflows:** Automate and enhance creativity.
- **Modularity:** Reuse and optimize assets.
- **Game Feel:** Ensure tactile and immersive experiences.
- **Tools and Techniques:** Build scalable, dynamic, and engaging game worlds.

**Reflection Questions:** 
- How will you apply procedural and modular techniques in your projects?
- How do node-based workflows enhance creativity and efficiency in game design?
- What are the advantages and challenges of combining proceduralism and modularity in a game project?
- Can you identify a game you’ve played that effectively uses procedural techniques? How did it enhance (or detract from) the gameplay experience?

---

