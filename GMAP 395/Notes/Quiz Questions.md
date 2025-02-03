### Quiz: Game Lighting and Workflows

1. **Multiple Choice**  
    Which of the following is _not_ a purpose of game lighting?  
    a) Enhance mood and atmosphere  
    b) Communicate gameplay mechanics and objectives  
    c) Reduce memory usage in game engines  
    d) Guide the player’s attention
    
2. **True/False**  
    Emissive lighting involves objects emitting their own light, which can contribute to both real-time and baked lighting.
    
3. **Fill in the Blank**  
    _______ is a lighting technique that simulates realistic light interactions through bounces and contributes to an immersive environment.
    
4. **Multiple Choice**  
    What is the primary role of a **spotlight** in game lighting?  
    a) Provide uniform illumination across the scene  
    b) Illuminate a specific area with a cone-shaped beam  
    c) Simulate sunlight with infinite reach  
    d) Bounce light off surfaces for indirect lighting
    
5. **True/False**  
    Static lighting is best used for dynamic, constantly changing game environments.
    
6. **Fill in the Blank**  
    _______ lighting adjusts in real-time, making it ideal for interactive or changing environments.
    
7. **Multiple Choice**  
    Light probes are used in game development to:  
    a) Simulate detailed reflections for objects  
    b) Enhance lighting for static objects only  
    c) Improve the appearance of dynamic objects by capturing surrounding light  
    d) Automatically generate lighting settings for the entire scene
    
8. **Multiple Choice**  
    Which attribute of lighting involves ensuring that brightness levels fit the scene’s tone and function?  
    a) Quality  
    b) Quantity  
    c) Direction  
    d) Dynamics
    
9. **Multiple Choice**  
    Which type of lighting is best for creating soft, general illumination without a specific light source?
    a) Directional lighting  
	b) Ambient lighting  
	c) Spot lighting  
	d) Emissive lighting
	
1. **True/False**  
    Volumetric lighting is often used to add atmospheric depth to a game scene by simulating light scattering through particles like fog or dust.
    

---

#### Answer Key

1. **c)** Reduce memory usage in game engines
2. **True**
3. **Global illumination**
4. **b)** Illuminate a specific area with a cone-shaped beam
5. **False**
6. **Dynamic**
7. **c)** Improve the appearance of dynamic objects by capturing surrounding light
8. **b)** Quantity
9. **b)** Ambient lighting
10. **True**

### Quiz: Shaders and Materials - Part I
#### GMAP 395 - Week 4 Quiz

##### **Question 1 (True/False)**

Shaders run on the **CPU** and define how objects interact with light in a scene.

##### **Question 2 (Multiple Choice)**

Which of the following is **NOT** a core shader type?  
A) Vertex Shader  
B) Fragment Shader  
C) Material Shader  
D) Compute Shader

##### **Question 3 (Fill in the Blank)**

The main purpose of a **fragment shader** is to determine the final _______ of each pixel in a rendered image.

##### **Question 4 (True/False)**

Physically Based Rendering (PBR) ensures **consistent** material appearance across different lighting conditions.

##### **Question 5 (Multiple Choice)**

Which of these effects can be achieved using shaders?  
A) Cel-shading  
B) Holograms  
C) Procedural textures  
D) All of the above

##### **Question 6 (Fill in the Blank)**

**Uniform variables** in shaders store values that remain _______ throughout the rendering of a single draw call.

##### **Question 7 (True/False)**

Procedural textures rely on images rather than mathematical functions.

##### **Question 8 (Multiple Choice)**

Which of the following is **NOT** an input to a shader?  
A) Vertex data  
B) Textures  
C) Physics simulation  
D) Uniform variables

##### **Question 9 (Fill in the Blank)**

One common **shader optimization technique** is to reduce the number of _______ calculations performed per pixel.

##### **Question 10 (True/False)**

Shaders only work with **static** objects and cannot influence dynamic elements in a scene.

#### GMAP 395 - Week 4 Quiz Answer Key

##### **Question 1 (True/False)**

**False** – Shaders run on the **GPU**, not the CPU.

##### **Question 2 (Multiple Choice)**

**C) Material Shader** – There is no "Material Shader." Shaders are typically categorized as **Vertex, Fragment (Pixel), and Compute Shaders**.

##### **Question 3 (Fill in the Blank)**

The main purpose of a **fragment shader** is to determine the final **color** of each pixel in a rendered image.

##### **Question 4 (True/False)**

**True** – PBR (Physically Based Rendering) ensures consistent material appearance across different lighting conditions.

##### **Question 5 (Multiple Choice)**

**D) All of the above** – Shaders can be used for **cel-shading (Borderlands), holograms (Halo), and procedural textures (noise-based materials).**

##### **Question 6 (Fill in the Blank)**

**Uniform variables** in shaders store values that remain **constant** throughout the rendering of a single draw call.

##### **Question 7 (True/False)**

**False** – Procedural textures **do not** rely on images but instead use **mathematical functions** to generate patterns.

##### **Question 8 (Multiple Choice)**

**C) Physics simulation** – Physics simulations are **not** a direct input to shaders. Shaders primarily take in vertex data, textures, and uniform variables.

##### **Question 9 (Fill in the Blank)**

One common **shader optimization technique** is to reduce the number of **expensive** calculations performed per pixel.

##### **Question 10 (True/False)**

**False** – Shaders can be applied to **both static and dynamic** objects, influencing animations, physics-based effects, and real-time interactions.