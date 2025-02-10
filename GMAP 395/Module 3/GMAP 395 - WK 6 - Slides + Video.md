---
theme: black
width: 1920
height: 1080
---

### GMAP 395: Advanced Game Art and Production

#### _Real-Time VFX in Games_

##### Week 6

---

### What Are Real-Time VFX?
- Definition: Visual effects (VFX) generated and rendered in real-time during gameplay.
- Examples:
    - Explosions
    - Magic spells
    - Environmental effects (rain, fog)
    - UI enhancements (damage indicators, hit effects)

<iframe width="560" height="315" src="https://www.youtube.com/embed/3QKK2o5rWSQ?si=a1hFPyhMXHAwqc97" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

[VFX in Video Games | From History to Future](https://polydin.com/vfx-in-video-games/)
[The Ultimate Guide to VFX for Gaming: From Explosions to Environments](https://magicmedia.studio/news-insights/guide-to-vfx-for-gaming/#:~:text=VFX%20in%20games%20are%20the%20computer%2Dgenerated%20effects,realism%2C%20impact%2C%20and%20excitement%20in%20the%20game.)

---

### Importance of VFX in Games
1. Enhance Visual Feedback
    - Instant response to player actions.
2. Reinforce Game Mechanics
    - Visual cues for interaction and gameplay.
3. Create Atmosphere and Mood
    - Set tone and immersion.
4. Guide Player Attention
    - Highlight important elements dynamically.

![[vfxingamestypes.webp|720]]

---

### Game Feel and VFX
- Player Control: VFX enhance the feeling of control.
- Actions and Events: VFX reinforce gameplay actions visually.
- User Feedback: Immediate, clear responses to inputs.

![[gamefeelcover.webp]]

---

### The 7 "Steps" of Game Feel

1. **Input**: Player action (button press, movement).
2. **Response**: Immediate visual feedback.
3. **Context**: Game state, environment.
4. **Polish**: Added visual elements for clarity.
5. **Metaphor**: Visual representation of actions.
6. **Rules**: Logic governing interactions.
7. **Juiciness**: Visually satisfying effects.

---

### Proceduralism in VFX
- Definition: Algorithm-driven (rules-driven) VFX.
- Benefits:
    - Efficient content creation.
    - Runtime variety.
    - Adaptability to dynamic scenarios.

---

### Modularity in VFX Design
- Definition: Using reusable, interchangeable VFX components ("layering meaningful stuff").
- Advantages:
    - Consistency across effects.
    - Easier iteration and updates.
    - Performance optimization.

<iframe width="560" height="315" src="https://www.youtube.com/embed/4_0hiAWzzoM?si=U11WlBEFLg5fW16a" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

---

### Case Study: LoL Volibear Reveal VFX
- Breakdown of stylized VFX in _League of Legends_.
- Use of lighting, particles, and shaders to enhance character identity.
- Blog: [A Storm is Brewing](https://leagueoflegends.com/en-us/news/dev/dev-a-storm-is-brewing/)

![[volibear.jpg|720]]

---

---

### Unity Particle System Overview

- Built-in VFX tool with CPU-based simulation.
- Efficient for many effects, but has limitations for complex scenes.
- Trusted by developers, used for particles like:
    - Smoke
    - Fire
    - Sparks

[Unity ParticleSystem Doc](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html)

---

### Key Components of the Particle System

- Emitter: Spawns particles in the scene.
- Particles: Individual units of the effect.
- Modules: Control particle behavior over time.
    - Emission: When and how particles are generated.
    - Shape: The emission area (sphere, cone, box, mesh).
    - Over Lifetime: Changes in particle size, speed, color, etc.

![[unityParticleSystsem.png|320]]

---

### Particle System: Key Modules

#### Emission Module
- Controls emission rate (particles per second).
- Emission Type:
    - Continuous
    - Burst (one-time)
    - Periodic

#### Shape Module
- Sphere: Emission from a spherical area.
- Cone: Directional emission.
- Box: Emission within a rectangular volume.
- Mesh: Emission from a custom mesh.

---

### Particle System: Color Over Lifetime
- Color Changes: Transitions particle colors over time.
    - Example: Fire transitions from red → yellow → orange.
- Gradient Use: Defines smooth color changes.


---

### Introduction to VFX Graph

- Node-Based Tool: Visual effect creation without scripting.
- GPU-Accelerated: Handles millions of particles efficiently.
- SRP Required: Requires Scriptable Render Pipeline for optimal performance.

![[vfxg1.png]]

---

### VFX Graph: Key Concepts

- **Nodes and Blocks**: Define particle behavior.
- **Contexts**: Stages of effect processing (spawn, initialize, update, output).
- **Properties**: Global values affecting multiple nodes.
- **Attributes**: Per-particle data like position, velocity, color.
- **Operators**: Perform calculations and logic in the effect.
- **Events**: Control effect timing and triggering.
- **Systems**: Grouped VFX elements working together.

---

### VFX Graph vs. Particle System

|Feature|Unity Particle System|VFX Graph|
|---|---|---|
|Ease of Use|Easier, UI-driven|Requires node-based logic|
|Performance|CPU-based, limited scalability|GPU-based, high performance|
|Complexity|Good for simple effects|Ideal for advanced VFX|

---

### VFX Graph: Procedural Techniques
- Animation Curves: Define smooth transformations.
- Noise-Based Movement: Create natural, organic motion.
- GPU Events: React to game logic dynamically.


---

### Performance Considerations
1. Particle Count: Higher counts impact FPS.
2. Texture Size: Large textures increase memory load.
3. Overdraw: Too many overlapping transparent particles = wasted draw calls.
4. CPU vs. GPU Load: Minimize CPU dependency for smoother performance.

---

### Art Direction in VFX
- Color Palettes: Match game aesthetics.
- Particle Shapes: Custom visuals for a unique look.
- Style Guide: Ensures consistent VFX appearance across the game.

---
### VFX & Game Art Style Guides
#### What is a Style Guide?
- A **documented set of rules** that defines the visual and design principles of a game’s VFX, materials, and assets.
- Helps artists, designers, and developers create **consistent and cohesive** effects across the game.
- Ensures **readability and player experience** remain clear, even in complex gameplay.

 _Ensuring Visual Consistency & Player Readability in Games_

---
### VFX & Game Art Style Guides: Why They Matter

✅ **Consistency** – All effects maintain a unified artistic vision.  
✅ **Readability** – Ensures visual effects clearly communicate gameplay mechanics.  
✅ **Efficiency** – Streamlines asset production and iteration.  
✅ **Performance** – Prevents excessive visual clutter and optimizes resources.


---
### Case Study: LoL VFX Style Guide

- How _League of Legends_ creates clear, readable, and stylized VFX.
- Read more: [League’s VFX Style Guide](https://nexus.leagueoflegends.com/en-us/2017/10/dev-leagues-vfx-style-guide/)

> _Example:_ League of Legends' VFX style guide ensures every champion’s effects are instantly recognizable across different skins and themes.

https://realtimevfx.com/t/official-league-of-legends-vfx-style-guide/3392

![[VFX_Styleguide_final_public_hidpjqwx7lqyx0pjj3ss.pdf]]



---

### Breakdown of a Complex VFX
1. Charge-Up: Initial build-up of energy.
2. Release: Effect execution (e.g., spell cast, explosion).
3. Impact: The moment of interaction.
4. Lingering Effects: Residual visuals post-action.

<iframe width="560" height="315" src="https://www.youtube.com/embed/IHAEL6g7ZnI?si=gUSSzrYsfKzNsExQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

---

### VFX Development Workflow
5. Design Effect: Sketch and concept.
6. Emitter System: Implement using Particle System.
7. Enhance with VFX Graph: Add procedural details.
8. Game Integration: Attach effects to game objects.

---

### Integrating VFX with Gameplay
- Tied to Player Actions
    - Example: Sword swings → Motion trails
    - Example: Magic casting → Particle buildup
- Feedback and Clarity
    - Example: Enemy damage hit sparks
    - Example: Low-health warning effects

---

### Resources for Further Learning
- Unity VFX Documentation: [Unity Docs](https://docs.unity3d.com/)
- VFX Artist Communities: [Real-Time VFX](https://realtimevfx.com/)
- Tutorials & Guides: on YouTube, Etc.


---

### Lab Exercise
- Create a VFX sequence for a simple game mechanic using:
    - Unity’s Particle System
    - VFX Graph
    - Game Feel principles

---

### Final Thoughts
- Real-Time VFX improves game feedback, immersion, and polish.
- Unity’s Particle System and VFX Graph both serve different needs.
- Balance performance and aesthetics to optimize gameplay experience.

---

### Lab Time
- Implement a basic real-time VFX system in Unity.
- Focus on timing, response, and feedback.

---
---
>[!info]  [[GMAP 395 - Module 3| Return to the Module Page]]