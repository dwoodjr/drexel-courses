---
theme: black
width: 1920
height: 1080
---
---
### GMAP 395: Advanced Game Art and Production

#### Week 5 - Shader Graph & Visual Shader Development

[gmap395_wk5.mp4](https://1drv.ms/v/s!AqQzGx8l4o2wk_IPty_ck4XywUX00A?e=r8xsqz)
<iframe src="https://1drv.ms/v/s!AqQzGx8l4o2wk_IPaLmdAExeJXl5JA?embed=1" width="320" height="320" frameborder="0" scrolling="no" allowfullscreen></iframe>

---

### Recap of Week 4 - Shader Fundamentals
- Shader Structure
    - Properties, Subshaders, Passes
    - Vertex Shaders 
    - Fragment Shaders

---
### What is Shader Graph?
- Visual Shader Creation Tool in Unity
- Node-Based Interface
    - No need for manual HLSL coding
    - Drag-and-drop workflow
- Requires Scriptable Render Pipeline (SRP)
    - URP (Universal Render Pipeline) is recommended for this course

---

### Shader Graph Interface Breakdown

- **Blackboard**: Define and expose parameters
- **Graph Inspector**: Contextual information about nodes
- **Main Stack**: Handles Vertex and Fragment logic
- **Main Preview**: Real-time shader preview (can be unreliable)
- **Toolbar**: Save, compile, and debug shaders


---
### Texture Mapping & Blending in Shader Graph

- Base Color Texturing
    - Sample a Texture2D and apply UV coordinates
- Using Lerp for Blending
    - Combine two textures using a Mask Texture
- Adding Detail Textures
    - Multiply noise maps for realistic effects

<iframe width="560" height="315" src="https://www.youtube.com/embed/zt21itB0ESw?si=hzZWxC0AvGoHWa-I" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

---

### Normal Mapping & Advanced Surface Detail

- Normal Maps Enhance Perceived Depth
    - Adds lighting-based details without extra geometry
- Implementation:
    - Use a Sample Texture 2D Node
    - Convert RGB values to Normal Data
    - Blend Normal Maps for extra detail

[This is Normal - ArtStation](https://www.artstation.com/blogs/typhen/GMyG/this-is-normal-1-what-normal-maps-are-and-how-they-work)
[What is Normal Mapping? - Adobe](https://www.adobe.com/products/substance3d/discover/normal-mapping.html)

---

### Common Shader Graph Operations

4. Color Adjustments
    - Adjust color values dynamically
5. UV Manipulation
    - Tiling, Offset, and Rotation
6. Vertex Displacement
    - Animate geometry movement
7. Time-Based Animations
    - Scroll textures, pulse effects

<iframe width="560" height="315" src="https://www.youtube.com/embed/gJMeSkolnw4?si=m7Dfpt4bsLcaQ3Ax" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

<iframe width="560" height="315" src="https://www.youtube.com/embed/MbD6ZTupmws?si=bHRxwZlEQpZAsHzb" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

---

### Vertex Displacement with Sine Waves

- Use the Position Node
- Apply Sine Waves for Oscillating Movement
- Combine Noise for Organic Deformations
- Practical Use: Water ripples, grass swaying, liquid surfaces

<iframe width="560" height="315" src="https://www.youtube.com/embed/IjfBlUtJF_0?si=X16DgtXyt6zvYTqa" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

---

### Using Noise for Procedural Patterns

- Types of Noise
    - Perlin Noise: Soft organic patterns
    - Voronoi Noise: Cellular structure
    - Gradient Noise: Blending & soft transitions
    - Many more...
- Blending Techniques
    - Combine noise with Lerp & Multiply Nodes
    - Adjust intensity via Remap Node


<iframe width="560" height="315" src="https://www.youtube.com/embed/jAOqmx764dA?si=8v9vrI1ifCuHEORZ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

---

### Custom Lighting in Shader Graph

- Lighting Models
    - PBR-based or Custom Light Calculations
- Creating Custom Rim Lighting
    - Multiply View Direction and Normal
    - Apply an Fresnel Node for edge glow

<iframe width="560" height="315" src="https://www.youtube.com/embed/ldtY-qwrm00?si=TPtMoWE9L7DnxDSS" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

---

## The Role of Shaders in the Rendering Pipeline

### 1. Vertex Processing
- Handles transformations of vertex positions and attributes.
- Adjusts geometry before rasterization.
- Key Operations:
    - Model-View-Projection transformations.
    - Vertex displacement (e.g., vertex animation for waves or procedural terrain).

### 2. Primitive Assembly
- Groups vertices into triangles or other primitives.
- Prepares geometry for rasterization.
- Affects edge visibility and culling.

---
## The Role of Shaders in the Rendering Pipeline (CONT.)
### 3. Rasterization
- Converts primitives (triangles) into pixel fragments.
- Determines which pixels will be rendered on the screen.

### 4. Fragment Processing
- Calculates the final color of each pixel.
- Executes texture mapping, lighting calculations, and shading effects.

### 5. Output Merging
- Combines rendered pixels into a final image.
- Handles blending, depth testing, and post-processing effects.

https://www.khronos.org/opengl/wiki/Rendering_Pipeline_Overview

---
![[renderPipeline.jpg|640]]


<iframe width="560" height="315" src="https://www.youtube.com/embed/oLiJTcdBCkM?si=lUZch6a5srRFLjEu" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

<iframe width="560" height="315" src="https://www.youtube.com/embed/C8YtdC8mxTU?si=npBTMSnBA2V1UmWN" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

---
### Integration with VFX Graph (Module 3 Preview)

- VFX Meshes
    - Assign shaders to particle systems
- Custom VFX Shaders
    - Modify shaders dynamically in real-time
- Particle Systems
	- Practical Use: Fire, smoke, dissolving effects


---

### Bridging Shader Graph & C# for Real-Time Material Manipulation

- Manipulating Shader Properties via C#
    - Expose shader parameters in Shader Graph (e.g., _Color, _Emission, _DistortionAmount)
    - Use C# scripts to modify material properties dynamically
- Responding to Game Events
    - Change material colors when taking damage
    - Adjust transparency when cloaking
    - Animate distortion or displacement over time
- Example: Modifying Shader Properties in C#
    
    ```csharp
    using UnityEngine;
    
    public class MaterialController : MonoBehaviour
    {
        public Material dynamicMaterial;
        public float pulseSpeed = 2f;
    
        void Update()
        {
            // Animate Emission Intensity Over Time
            float emission = Mathf.PingPong(Time.time * pulseSpeed, 1f);
            dynamicMaterial.SetFloat("_EmissionIntensity", emission);
        }
    
        public void SetDamageEffect()
        {
            // Flash red when hit
            dynamicMaterial.SetColor("_BaseColor", Color.red);
        }
    }
    ```
    
- Real-World Uses
    - Player Interaction: Change material properties based on proximity
    - UI Feedback: Highlight objects when hovered over
    - Environmental Effects: Shift colors based on time of day or weather conditions

---

### Tweening in Shaders for Procedural Animation

- What is Tweening?
    - Smooth interpolation of values over time
- Linking Animations to Shader Properties
    - Change Emission Intensity, Transparency, Displacement
- Tweening Libraries in Unity
    - DOTween, LeanTween
- Example: Glow pulse shader using a tweened float variable

```csharp
using DG.Tweening;
Material mat;
void Start() {
    mat = GetComponent<Renderer>().material;
    mat.DOColor(Color.blue, "_EmissionColor", 2f).SetLoops(-1, LoopType.Yoyo);
}
```

---

### Case Study: Shader-Driven Effects in Games

1. Cel Shading in *Borderlands*
    - Uses custom ramp shading
    - Simplified shadows for comic book style
2. Hologram Effects in *Halo*
    - Vertex displacement for distortion
    - Transparency with additive blending
3. Water Simulation in *Sea of Thieves*
    - Vertex waves via sine displacement
    - Reflection and refraction shaders

---

### Connection Between Procedural Modeling & Shaders
- Procedural Modeling generates game assets dynamically—Shaders can complement this by adding:
    - Procedural Textures: Generate surface detail without needing high-resolution textures
    - Dynamic Surface Effects: Adapt material appearance based on model parameters
    - Example: A procedural rock model can have a procedural shader that controls:
        - Color variation based on world position
        - Edge wear effects using curvature maps
        - Moss or dirt accumulation in crevices
- Key Concept: Both Procedural Modeling & Shaders use node-based workflows (*Houdini*, *Blender Geometry Nodes*, *Unity Shader Graph*)

---

### Game Lighting & Shaders – How They Work Together
- Lighting in Games defines how objects appear based on:
    - Direct Lighting (sunlight, spotlights)
    - Indirect Lighting (bounced light, reflections)
    - Ambient Lighting (general scene illumination)
- Shaders Enhance Lighting by:
    - Controlling how materials respond to light (diffuse, metallic, specular)
    - Using custom lighting models to override Unity’s default lighting
    - Adding real-time effects, like rim lighting, emissive glow, and reflections
- Example: A lava shader that uses emissive properties to glow in dark environments
    

---

### Shader Graph vs. Handwritten Shader Code
- Shader Graph
    - Visual scripting for shaders
    - No need for HLSL coding
    - Best for rapid prototyping
    - Limited in customization (but extendable with code)
- HLSL / Custom Shader Code
    - More control over rendering logic
    - Better for performance optimizations
    - Required for advanced effects (custom lighting, procedural vertex animations)
- When to Use Each?
    - Shader Graph: Prototyping, procedural textures, stylized effects
    - Handwritten Code: Performance-critical shaders, advanced lighting, VFX shaders

---

### Common Shader Debugging & Optimization Tips
- Performance Considerations
    - Reduce Overdraw: Use Alpha Clipping instead of transparent materials when possible
    - Shader Complexity: Limit the number of shader passes (each pass is an extra rendering step)
    - Optimize Textures: Avoid high-res textures where procedural patterns can be used
- Debugging Shader Graph
    - Use Frame Debugger (`Window > Analysis > Frame Debugger`) to see rendering steps
    - Use Material Debugging Mode (`Scene View > Debug Shading Modes`) to isolate issues
    - Always test shaders under different lighting conditions

---

### Real-World Use Cases of Shaders in Game Development
- Stylized Games
    - Example: _Hollow Knight_ uses hand-painted textures + simple shaders for a 2D lighting effect
- Realistic Games
    - Example: _The Last of Us 2_ uses physically-based shaders for materials like leather and metal
- Procedural Effects
    - Example: _No Man’s Sky_ procedural planets use Shader Graph for terrain blending
- Interactive Environments
    - Example: _Control_ by Remedy uses dynamic shaders for real-time environment shifts
- Takeaway: Shaders are a core part of how modern games achieve immersion and responsiveness!

---
---
>[!info]  [[GMAP 395 - Module 2| Return to the Module Page]]

