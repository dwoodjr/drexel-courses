---
theme: black
width: 1920
height: 1080
---

### **_Game Lighting and Workflows_**
#### GMAP 395: Advanced Game Art and Production
##### Week 3

---

### What is Game Lighting?
- **Purpose of Lighting:**
    1. Enhance mood and atmosphere.
    2. Guide the player’s attention.
    3. Improve visual clarity and realism.
    4. Communicate gameplay mechanics and objectives.
    5. Balance aesthetics with performance.

---

### Key Attributes of Lighting
- **Quality:** Determines how light interacts with surfaces.
    - Example: Realistic shadows, soft light falloffs.
- **Quantity:** The intensity and coverage of light.
    - Example: Brightness levels and area of influence.
- **Direction:** The angle and position of light.
    - Example: Backlighting for dramatic silhouettes.

<iframe width="560" height="315" src="https://www.youtube.com/embed/7MNl-j7WqTw?si=DfxcntQvlkXxpBhY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


---

### Key Concepts: Quality, Quantity, and Direction
- **Understanding Quality:**
    - High-quality lighting enhances immersion with realistic shadows and nuanced illumination.
    - Balancing quality ensures performance optimization.
- **Managing Quantity:**
    - Excessively bright or dim lighting can confuse players.
    - Adjust light intensity to fit the scene’s tone and function.
- **Using Direction Effectively:**
    - Side or top-down lighting can highlight textures or contours.
    - Directional lighting aids in visual storytelling.


<iframe width="560" height="315" src="https://www.youtube.com/embed/VXggMZvqSvM?si=_8we5-icTZw7dV3Y" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

---
### Lighting Types Overview
- **Direct Lighting:** Hits surfaces directly.
- **Indirect Lighting:** Bounces light off surfaces.
- **Ambient Lighting:** General illumination without a specific source.
- **Emissive Lighting:** Objects emit their own light.
- **Global Illumination (GI):** Simulates realistic light interactions through bounces.


[A guide to global illumination - ADOBE ](https://www.adobe.com/products/substance3d/discover/what-is-global-illumination.html#:~:text=Global%20illumination%20is%20a%20feature,doesn't%20look%20very%20realistic.)

<iframe width="560" height="315" src="https://www.youtube.com/embed/04YUZ3bWAyg?si=FYbntATZXyYFmGlt" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

---

### Technical Considerations Across Platforms
- **General Principles:**
    - All game engines rely on similar principles for rendering lighting.
    - Systems like lightmaps, probes, and dynamic adjustments are ubiquitous.
- **Implementation Tips:**
    - Always profile lighting performance.
    - Utilize modular workflows for scalability when needed/possible.


---

### Common Types of Light Emitting Objects
1. **Directional Light:** Simulates sunlight, infinite reach.
2. **Point Light:** Emits light uniformly in all directions.
3. **Spot Light:** Creates a cone-shaped beam.
4. **Area Light:** Illuminates a specific area (baked only).

[The Level Design Book - Lighting](https://book.leveldesignbook.com/process/lighting)

---

### Light Modes and Applications
- **Dynamic Lighting:** Updates continuously, ideal for interactive or changing environments.
- **Static Lighting:** Pre-calculated for non-interactive elements to reduce processing.
- **Hybrid Systems:** Combine dynamic and static methods for optimized results.

[Unity Documentation on "Light Modes"](https://docs.unity3d.com/6000.0/Documentation/Manual/LightModes-introduction.html)

---

### Optimizing Lighting for Performance
1. **Limit Realtime Lights:** Use baked lighting wherever possible.
2. **Leverage Mixed Lighting:** Combine dynamic and static lighting.
3. **Light Probes:** Optimize lighting for dynamic objects.
4. **Reflection Probes:** Simulate realistic reflections.
5. **Profile Lighting Costs:** Regularly monitor performance impact.

[Difference Between Realtime, Mixed, And Baked Lighting in Unity](https://vintay.medium.com/difference-between-realtime-mixed-and-baked-lighting-in-unity-6bda1f24bfb)

> [!NOTE] See again ([Global Illumination in Tom Clancy's The Division](https://www.youtube.com/watch?v=04YUZ3bWAyg))


---

### Tools for Technical Lighting
- **Baking Systems:** Pre-render static lights for better performance.
- **Volumetric Effects:** Add atmospheric depth with fog and light scattering.
- **Custom Shaders:** Fine-tune light interactions for specific materials.
- **Node-Based Workflows and Code:** Use visual tools for procedural lighting systems.

---

### Dynamic Lighting Techniques
1. **Day/Night Cycles:** Transition lighting over time to match environmental storytelling.
2. **Interactive Lighting:** Lights that respond to player actions or environmental triggers.
3. **Color and Intensity Shifts:** Create mood transitions or dramatic effects.

---

### Lighting as a Gameplay Mechanic
- **Guidance:** Direct player attention to objectives.
    - Example: Highlight interactable objects or paths.
- **Atmosphere:** Build tension or mood.
    - Example: Dim, flickering lights in a horror game.
- **Puzzle Elements:** Use light as an integral component of gameplay challenges.
    - Example: Reflective surfaces or light-activated mechanisms.

<iframe width="560" height="315" src="https://www.youtube.com/embed/wjMlHY3-sWI?si=5Y-cKS6g87Q0Oq9t" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

---

### Advanced Lighting Design Strategies
- **Layered Lighting:** Combine ambient, direct, and dynamic sources for depth.
- **Color Theory in Lighting:** Use color to evoke emotions or set the scene’s tone.
- **Light-Based Storytelling:** Subtle shifts in lighting to hint at narrative progression.

---

### Balancing Performance and Visuals
- **LOD Systems:** Adjust lighting details based on distance.
- **Render Pipelines (Graphics Pipeline):** Use advanced pipelines for better control.
- **Post-Processing:** Enhance visuals without additional light sources.

[OpenGL Rendering Pipeline | An Overview](https://www.geeksforgeeks.org/opengl-rendering-pipeline-overview/)
[Graphics Pipelines](https://en.wikipedia.org/wiki/Graphics_pipeline)
<iframe width="560" height="315" src="https://www.youtube.com/embed/oLiJTcdBCkM?si=sPORx7YosYtV_EFk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

---

### Understanding Color in Game Lighting
#### Why Color Matters:
- **Emotion and Atmosphere:**
    - Colors evoke specific emotions and set the tone of a scene.
    - Example: Warm colors like orange and red convey energy or danger, while cool colors like blue and green suggest calm or mystery.
- **Player Guidance:**
    - Bright or contrasting colors naturally draw attention to key gameplay elements.
    - Example: A glowing blue portal in a dimly lit room.

---

### Core Concepts of Color Theory
1. **Hue, Saturation, and Value (HSV):**
    - **Hue:** The color itself (e.g., red, blue, yellow).
    - **Saturation:** The intensity or purity of the color.
    - **Value:** The brightness or darkness of the color.
2. **Color Harmony:**
    - **Complementary Colors:** Opposite on the color wheel (e.g., blue and orange) create contrast.
    - **Analogous Colors:** Side-by-side on the wheel (e.g., red, orange, yellow) create harmony.
    - **Triadic Colors:** Equally spaced around the wheel for balance (e.g., red, yellow, blue).
3. **Color Temperature:**
    - **Warm Colors:** Reds, yellows, and oranges evoke energy and warmth.
    - **Cool Colors:** Blues and greens create calm or distance.

<iframe width="560" height="315" src="https://www.youtube.com/embed/zl2B6SCqA1s?si=sCEeLNxe_vBOuYck" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

---

### Color Scripts: Using Color to Tell Stories

#### What is a Color Script?
- A previsualization tool that maps out the emotional journey of a game using color.
- Often used in animated films and games to ensure consistency and coherence in visual storytelling.

#### Example Process:
1. Break down the game or level into key moments or scenes.
2. Assign a dominant color palette to each moment based on its mood or theme.
    - Example: Use red hues for high-intensity battles and softer blues for reflective or quiet moments.
3. Create thumbnail sketches or storyboards with approximate lighting and color.

[How to Make a Color Script](https://photography.tutsplus.com/tutorials/how-to-colourscripts-animation--cms-38391)
[Color Scripting - Khan Academy](https://www.khanacademy.org/computing/pixar/art-of-lighting/introduction-to-virtual-lighting/a/exercise-5-color-scripts)

<iframe width="560" height="315" src="https://www.youtube.com/embed/BWEWOBJKWpA?si=fkQ1myM-CWSLCPpf" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


---

### Techniques for Integrating Color and Light
1. **Color Temperature in Lighting:**
    - Use warm light for natural, inviting environments (e.g., sunlight or firelight).
    - Use cool light for sterile or eerie settings (e.g., moonlight or fluorescent light).
2. **Color Grading in Post-Processing:**
    - Adjust the overall tone of a scene to emphasize mood.
    - Example: Desaturate colors for a bleak, dystopian setting or enhance vibrancy for fantastical worlds.
3. **Dynamic Color Shifts:**
    - Change lighting color dynamically to reflect gameplay events or mood shifts.
    - Example: A room flooding with red light during an alarm.

<iframe width="560" height="315" src="https://www.youtube.com/embed/DXcYSbH5Ukw?si=9LnX1dwr3HRZw4GG" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

---

### Case Study: Dynamic Lighting Example: "[Control](https://www.remedygames.com/games/control)" by Remedy Entertainment
- **Platform:** High-spec PC and consoles (PS4/PS5, Xbox One/Series).
- **Lighting Techniques Used:**
    - **Dynamic Lighting:** Utilizes real-time ray tracing for accurate reflections, shadows, and indirect lighting. Light changes dynamically as the player interacts with the environment or moves through different spaces.
    - **Global Illumination:** Achieved through ray tracing to simulate realistic light bounces, enhancing immersion in its moody, supernatural world.
    - **Volumetric Lighting:** Used extensively to create atmospheric effects like light beams filtering through dust or fog, amplifying the game's eerie tone.
- **Optimization Techniques:**
    - Ray tracing is scaled back on lower-end systems by using approximations or turning off certain effects while maintaining the overall mood.
    - Selective use of baked lighting for static geometry.


| ![[6492c4abf65d6e4dfffbb89e_CONTROL_WorldTrailer_quarry_sky-p-500.avif]] | ![[6492c4ab6751d8f29f5e4826_LAUNCH_Screenshot_101-p-500.webp]] |
| ------------------------------------------------------------------------ | -------------------------------------------------------------- |
|                                                                          |                                                                |


---

### Case Study: Optimized Lighting Example: "[Monument Valley](https://www.monumentvalleygame.com/mv3)" by ustwo games
- **Platform:** Mobile devices.
- **Lighting Techniques Used:**
    - **Baked Lighting:** Pre-calculated lightmaps are used for all scenes, ensuring the game runs smoothly on low-power devices while maintaining visual appeal.
    - **Ambient Occlusion:** Baked into textures to give depth and definition to the minimalist geometric environments.
    - **Color as Light:** Simple, vibrant color palettes imply lighting and shadow, reducing computational overhead while creating an artistic, dreamlike aesthetic.
- **Optimization Techniques:**
    - Fixed camera angles and static environments allow for efficient pre-rendering.
    - Minimal reliance on dynamic lights, focusing instead on artistic use of gradients and shading.



|                          |                          |
| ------------------------ | ------------------------ |
| ![[iPad_02-600x800.png]] | ![[iPad_01-600x800.png]] |

---

### Case Study: Compare and Contrast:

|**Aspect**|**Control**|**Monument Valley**|
|---|---|---|
|**Platform Target**|High-spec PCs and consoles|Mobile devices|
|**Lighting Approach**|Real-time dynamic lighting and ray tracing|Fully baked lighting with artistic shading|
|**Performance Strategy**|Scalable settings, reduced ray tracing for lower-end|Pre-baked lightmaps for static environments|
|**Visual Focus**|Hyper-realistic, atmospheric environments|Minimalist, stylized geometric worlds|
|**Key Techniques**|Ray tracing, global illumination, volumetrics|Baked lighting, ambient occlusion, vibrant colors|
#### Some Questions
- How does each game leverage its lighting strategy to create a distinct mood and enhance the player experience?
- What challenges might developers face when scaling the lighting approach for different platforms or performance tiers?
- How do the artistic and technical choices in each game reflect the limitations or opportunities of their respective platforms?


---

### Practical Application
#### Optimizing a Scene
1. Use **baked lighting** for static elements.
2. Add **light probes** for dynamic objects.
3. Profile scene with Unity’s Profiler.

#### Enhancing Player Experience
1. Add **spotlights** to key areas.
2. Use **color grading** for mood.
3. Implement **dynamic light triggers** for interactivity.


---

### Summary
- **Lighting Attributes:** Quality, quantity, direction.
- **Optimization Tools:** Lightmaps, probes, and profiling.
- **Dynamic Techniques:** Time-of-day, animated lights, interactive systems.
- **Gameplay Integration:** Light as a mechanic for guidance and immersion.

<iframe width="560" height="315" src="https://www.youtube.com/embed/MkWIHLL5pyQ?si=rEcFB3zqTH6k5P63" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

---

### Final Thoughts
- **Lighting Principles Are Universal:** The same concepts apply across all major engines and tools.
- **Always Iterate:** Refine lighting to balance performance and aesthetics.
- **Stay Curious:** Explore how other games use light to innovate.

---
### Questions for Reflection
1. How does lighting influence player decision-making?
2. What challenges arise when balancing performance with high-quality lighting?
3. How can you apply these concepts across different game engines or tools?

---

>[!info]  [[GMAP 395 - Module 1| Return to the Module Page]]