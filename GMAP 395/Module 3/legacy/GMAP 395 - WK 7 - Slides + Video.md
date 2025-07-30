---
theme: black
width: 1920
height: 1080
---


## _GMAP 395: Advanced Game Art and Production_
### Real-Time VFX in Games: Advanced Techniques
##### Week 7
---

### 1. Introduction to Real-Time VFX (Review)
- What are real-time VFX?
- Why are they crucial for game development?
- How do they integrate into modern game engines?
- Where do shaders fit in?

<iframe width="560" height="315" src="https://www.youtube.com/embed/gQMeyedKmh0?si=G0JB-D2Sbez0l42a" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

---

### 2. The Role of VFX in Game Design (Review)
- Enhancing Game Feel: Player immersion through visual impact
- Providing Visual Feedback: Representing gameplay mechanics
- Creating Atmosphere: Setting the mood and tone of a game world
- Guiding Player Attention: Directing the eye using motion and color

<iframe width="560" height="315" src="https://www.youtube.com/embed/NQ5Dllbxbz4?si=T6V8jase2GvmHK4P" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

---

### 3. VFX Graph: A Node-Based System (Review)
- What is VFX Graph?
    - A GPU-powered, node-based tool for creating real-time VFX
- Why use VFX Graph instead of a traditional particle system?
    - Performance: Uses GPU acceleration
    - Flexibility: Can handle complex simulations
    - Scalability: Works with procedural effects

[VFX Graph](https://unity.com/features/visual-effect-graph)

![[vfxgSplash.png|720]]

---

### 4. Core VFX Graph Concepts (Review)
- Initialize, Update, and Output Stages
    - Each stage controls different aspects of an effect
- Using Contexts to Structure Effects
    - Emit, spawn, evolve, and output visual data
- Key Properties and Attributes
    - Controlling speed, lifespan, and rendering of particles

![[VFXGraph_3-5_ComplexNetwork.png|720]]

---

### 5. Modular VFX Design for Games (Review)
- Definition: Designing reusable, interchangeable VFX components
- Why Modular?
    - Consistency: Keeps effects visually unified
    - Efficiency: Reduces redundant work
    - Flexibility: Enables rapid iteration and customization

---

### 6. Implementing Modular VFX Graphs
- Sub-graphs: Reusable VFX components
- Prefab Systems: Assigning VFX to game assets dynamically
- Scriptable Objects: Storing reusable effect parameters

[Proceduralism as a catalyst for creativity feat. Julie Lottering from SideFX](https://www.youtube.com/watch?v=DRi2bRDB-x0)
[Proceduralism for Games? Short answer is YES. | Christos Stavridis | GDC HIVE 2023](https://www.youtube.com/watch?v=lb4yVPeWuwY)

---

### 7. Procedural VFX for Games (Review)
- Definition: Using algorithms to generate VFX dynamically
- Applications in Games:
    - Particle behavior (e.g., wind-driven dust, randomized explosions)
    - Procedural shape generation (e.g., smoke, fire)
    - Color schemes that evolve over time

[Procedural generation: Creating infinite algorithmic realities](https://www.autodesk.com/solutions/procedural-generation)

<iframe width="560" height="315" src="https://www.youtube.com/embed/9NgxCGkzsvg?si=IYMCmiFGD1OIIamr" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

---

### 8. Controlling VFX with Noise-Based Systems
- Noise in Motion:
    - Integrating Perlin noise for fluid, organic movement
- Shaping Effects with Noise:
    - Creating naturalistic smoke, fire, and energy patterns

[Understanding Perlin Noise](https://adrianb.io/2014/08/09/perlinnoise.html)
[Perlin Noise: A Procedural Generation Algorithm](# Perlin Noise: A Procedural Generation Algorithm)

![[perlin-noise-terrain-mesh1.png|720]]

---

### 9. Mesh Emission in VFX
- What is Mesh Emission?
    - Using 3D models as particle emitters instead of simple point sources
- Why Use Meshes?
    - Enables complex particle behaviors
    - Aligns particles with character movements
    - Creates detailed environmental effects

---

### 10. Implementing Mesh Emission in VFX Graph
1. Import a mesh asset
2. Set it as the emitter in the VFX Graph
3. Control particle emission based on mesh attributes
4. Adjust parameters for density and speed

<iframe width="560" height="315" src="https://www.youtube.com/embed/yW1uXjnq14Q?si=11H2-KQXJyPgr6AQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

---

### 11. Decals in VFX Graph
- What are Decals?
    - 2D images projected onto 3D surfaces
- Use Cases:
    - Blood splatters, bullet holes, footprints
    - Magic circles, surface-based energy effects
- Performance Benefits:
    - Add detail without modifying geometry
    - Can be animated dynamically in VFX Graph

<iframe width="560" height="315" src="https://www.youtube.com/embed/a1mDf2dj6JU?si=UDKza80CIj9DHf_N" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
[URP Decals in Unity](https://www.youtube.com/watch?v=zSMjTK8d7GQ)

---

### 12. Advanced Decal Techniques in VFX
- Animating Decals: Simulating movement on surfaces
- Reactive Decals: Creating effects like scorch marks that fade over time
- Optimizing Performance: Using GPU-friendly decal projection

---

### 13. Collision and Interaction in VFX
- Why Interaction Matters in VFX
    - Makes environments feel alive and reactive
    - Enhances player feedback in gameplay
- Examples of Interactive VFX
    - Splashes in water when a character lands
    - Dust kicking up as a player runs
    - Particles colliding with objects (rain hitting surfaces)

![[Block-CollideWithDepthBufferMain.png]]

---

### 14. Setting Up Collision in VFX Graph
1. Activate collision detection in VFX Graph
2. Define collision surfaces (plane, sphere, or mesh)
3. Apply force or change particle behavior upon impact

---

### 15. Connecting Shaders to VFX Graph
- Why Use Shaders in VFX?
    - Shaders modify particle visuals dynamically
    - Add advanced effects like refraction, emissive glow, and distortion
- How It Works:
    - Use Shader Graph as an output material in VFX Graph
    - Modify shader parameters in real-time based on particle properties

---

### 16. Shader-Based Particle Rendering
- Examples of Shader-Controlled VFX
    - Heat distortions for explosions
    - Energy-based auras that pulse dynamically
    - Water ripples that react to collisions
- Using Shader Graph to Adjust Particle Appearance
    - Connect VFX Graph outputs to shader inputs
    - Modify properties like opacity, glow, and texture movement

---

### 17. Combining VFX Graph and Shaders for Dynamic Effects
- Example Workflow:
    1. Create a VFX Graph system for an explosion
    2. Apply Shader Graph to control particle visuals
    3. Use real-time parameters (e.g., intensity, color) to adjust shader properties
- Benefit: More integrated, seamless visual effects

---

### 18. Real-Time Shader Control in VFX
- Modifying Shader Properties via Gameplay
    - Connecting game events to VFX shader parameters
    - Examples:
        - Fire effect that intensifies when a player is near
        - Magic aura that fades when a spell ends

---

### 19. Implementing Real-Time Shader Control
1. Expose shader parameters to Unity’s inspector
2. Modify them in real-time using scripts
3. Link parameters to gameplay events
4. Optimize for performance

https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VFX.VisualEffect.html

---

### 20. Performance Considerations for VFX
- Balancing visual fidelity and frame rate
    - Avoiding overdraw in transparent particle effects
    - Reducing unnecessary GPU calculations
    - Using GPU instancing for efficient rendering

---

### 21. Optimization Strategies
- Limit Simultaneous effects: Fewer complex effect splaying at one time
- Reduce Particle Lifetime: Shorter effects reduce CPU/GPU load
- Use "LODs" for Effects: Lower detail for distance effects

---

### 22. Case Study: Optimized VFX in a AAA Game
- Example:
    - How _Control_ (Remedy Entertainment) handles interactive lighting & destruction effects
    - How *Destiny 2* (Bungie) uses shader-driven energy effects to create responsive player abilities

---

### 23. Future Trends in Real-Time VFX
- AI-Assisted VFX Creation
- Ray-Traced Particle Systems for ultra-realistic lighting
- Procedural VFX Workflows for generative effects in games
- VFX in XR (VR/AR/MR) for immersive real-time experiences

---

### 24. Key Takeaways
- Modular and procedural workflows enable flexible VFX
- Shaders + VFX Graph create advanced, real-time visual effects
- Performance optimization is crucial for real-time rendering
- Interactive VFX enhances immersion and gameplay feedback

---

### 25. Final Thoughts & Discussion
- How do shaders enhance VFX in gameplay?
- What are some real-world examples of modular VFX?
- Where do you see VFX heading in the next five years?

---
---
>[!info]  [[GMAP 395 - Module 3| Return to the Module Page]]