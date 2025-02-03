---
theme: black
width: 1920
height: 1080
---
### GMAP 395: Advanced Game Art and Production
#### ***Shaders and Material Development - 1***
##### Week 4

> [!example] Week 4 Video Lecture
> <iframe src="https://1drv.ms/v/s!AqQzGx8l4o2wk_F31rCrj4PiIZcKAQ?embed=1" width="320" height="320" frameborder="0" scrolling="no" allowfullscreen></iframe>
> 
> [gmap395_wk4.mp4](https://1drv.ms/v/s!AqQzGx8l4o2wk_F3vSAiT9rcAKv5Jw?e=HRmiMT)


---
### What Are Shaders?
- **Definition:** Shaders are small programs that run on the GPU, defining the visual appearance of objects in a scene.
- **Purpose:** Control how materials interact with light to achieve desired visual effects.
- **Core Shader Types:**
  1. **Vertex Shaders:** Modify geometry at the vertex level.
  2. **Fragment Shaders (Pixel Shaders):** Control pixel-level color and lighting.

<iframe width="560" height="315" src="https://www.youtube.com/embed/sXbdF4KjNOc?si=T6GoU2ai30lPM2qK" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

[What are shaders? - GDQuest](https://www.youtube.com/watch?v=ax1JLQABmOw)

---
### Why Learn Shaders?
- **Customization:** Allows unique material creation.
- **Optimization:** Efficient use of GPU resources for real-time rendering.
- **Dynamic Effects:** Enables interactive and changing visuals.
- **Examples:**
  - "Stylized" water effects (*Breath of the Wild*).
  - Holograms (*Halo*).
  - Cel-shading (*Borderlands*).

---
### Shaders and Technical Art
- **Bridging Art and Code:**
  - Shaders enable technical artists to bridge visual design and programming.
- **Dynamic Visuals:**
  - Create interactive and adaptive visuals for game systems.
- **Procedural Systems:**
  - Shaders are often used in procedural workflows for generating textures, patterns, and effects.
---
### Shaders in Proceduralism and Modularity
- **Procedural Textures:**
  - Use math and logic to generate seamless textures.
- **Modular Workflows:**
  - Reusable shader modules can streamline development.
- **Examples:**
  - Procedural weathering effects.
  - Adjustable material templates for diverse assets.
---
### Shader Workflow
1. **Define Properties:** Expose parameters like color or texture to customize materials.
2. **Create SubShaders:** Specify rendering techniques for different hardware or conditions.
3. **Write Passes:** Describe rendering steps (e.g., vertex and fragment programs).
---
### Anatomy of a Shader
```csharp
Shader "Custom/ExampleShader"
{
    Properties
    {
        _Color ("Main Color", Color) = (1,1,1,1)
    }
    SubShader
    {
        Pass
        {
            CGPROGRAM
            #pragma vertex vert
            #pragma fragment frag
            // Declare the _Color property as a uniform
            fixed4 _Color;
            struct appdata
            {
                float4 vertex : POSITION; // Vertex position
            };
            struct v2f
            {
                float4 pos : SV_POSITION; // Transformed position
            };
            v2f vert (appdata v)
            {
                v2f o;
                o.pos = UnityObjectToClipPos(v.vertex);
                return o;
            }
            // Use _Color in the fragment shader
            fixed4 frag (v2f i) : SV_Target
            {
                return _Color; // Output the color
            }
            ENDCG
        }
    }
}

```
---
### Breaking Down the Shader Code
- **Shader Properties:**
  - `_Color`: Exposed parameter for material customization.
- **SubShader:**
  - Contains rendering passes for different GPU capabilities.
- **Vertex Function:**
  - Processes vertex data (positions, normals, UVs).
- **Fragment Function:**
  - Determines final pixel color using inputs from the vertex shader.
---
### Core Concepts in Shader Development
1. **Uniform Variables:**
    - **Definition:** Global variables that are constant during the rendering of a single draw call. These are set by the CPU and shared across all invocations of a shader program.
    - **Examples:**
        - Time values for animations.
2. **Attributes:**
    - **Definition:** Input data that is unique for each vertex and provided by the vertex buffer. Attributes are available only in the vertex shader.
    - **Examples:**
        - Texture coordinates (`TEXCOORD`).
3. **Varyings:**
    - **Definition:** Variables used to pass interpolated data from the vertex shader to the fragment shader.
    - **Examples:**
        - Lighting data like vertex colors or normals.
  
[The Book of Shaders](https://thebookofshaders.com/)

---
### Shader Inputs and Outputs
- **Inputs:**
  - **Vertex Data:** Positions, normals, UVs.
  - **Textures:** Color or detail maps.
  - **Uniforms:** Constants like time or transformations.
- **Outputs:**
  - Final pixel colors rendered to the screen.
---
### Shaders and 3D Geometry
#### 3D Geometry Basics
- **Vertices:** Define points in 3D space.
- **Edges:** Connect vertices to outline shapes.
- **Faces:** Form surfaces using connected edges.
- **UVs:** Map 2D textures to 3D surfaces.
- **Normals:** Vectors perpendicular to faces for lighting calculations.
#### How Geometry Connects to Shaders
- **Vertex Data:** Input for vertex shaders to transform 3D geometry.
- **Normals:** Used in lighting equations for shading effects.
- **UV Mapping:** Guides texture placement via fragment shaders.
- **Shader Outputs:** Define the final appearance of geometry on-screen.

<iframe width="560" height="315" src="https://www.youtube.com/embed/PfpE5dNTWeI?si=AbwrmazoPmn7mwzQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

---
### Shaders, Materials, and Textures
#### Shaders
- Small programs executed on the GPU.
- Control how light interacts with geometry.
- Types: Vertex, Fragment, Compute.
#### Materials
- **Definition:** A wrapper for shaders, combining textures and parameters.
- **Role:** Define the look of objects by associating shaders with visual properties.
- **Example:** A reflective material uses a custom shader for specular highlights.
#### Textures
- **Definition:** 2D images mapped to 3D geometry.
- **Purpose:** Add details like color, patterns, or surface irregularities.
- **Common Types:** Diffuse, Normal, Specular, Emissive.

<iframe width="560" height="315" src="https://www.youtube.com/embed/CBX9Esfnx5I?si=BgGV2MoG6-bE0ZcV" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

---

### PBR Workflows
#### What Is PBR?
- **Physically Based Rendering (PBR):** A method to simulate realistic lighting and material behavior.
- **Key Concepts:** Energy conservation, physically accurate shading.
- **Benefits:** Consistent results across lighting environments.
#### PBR Workflow
1. **Base Color:** Defines the albedo (color) of the surface.
2. **Metallic:** Specifies if the material is metal (affects reflection).
3. **Roughness/Smoothness:** Controls surface reflectivity.
4. **Normal Map:** Adds surface details without extra geometry.
5. **Ambient Occlusion (AO):** Simulates soft shadows in crevices.


> [!NOTE] [Material Maker](https://www.materialmaker.org/)
> Material Maker is a procedural materials authoring tool based on the Godot Engine.

---
### Mathematical Operations in Shaders
- **Vector Operations:**
  - **Dot Product:** Lighting calculations.
  - **Cross Product:** Surface normals.
- **Matrix Transformations:**
  - Object to world space conversions.
- **Color Operations:**
  - RGB blending and transitions.
- **Noise Functions:**
  - Create procedural patterns for effects.
---
### Shader Optimization Tips
- **Minimize Complexity:**
  - Use simple math operations where possible.
- **Reuse Variables:**
  - Avoid redundant calculations.
- **LOD Techniques:**
  - Reduce detail for distant objects.
---
### Real-Time Shader Examples
- **Dissolve Effects:**
  - Use noise textures to create fading effects.
- **Holographic Shaders:**
  - Add transparency and scrolling UV animations.
- **Water Shaders:**
  - Simulate refraction and wave movement.

> [!NOTE] [Real-Time VFX Website](https://realtimevfx.com/)

---

#### Introduction to Unity Shader Graph
- **What Is Shader Graph?**
  - A node-based interface for creating shaders visually.
- **Benefits:**
  - No coding required.
  - Rapid iteration and prototyping.
- **Components:**
  - Blackboard, Nodes, Master Stack, Preview, etc.
- [Shader Graph Docs](https://docs.unity3d.com/Packages/com.unity.shadergraph@14.0/manual/Getting-Started.html)

<split even gap="3">
![[blackboard_shadergraph_path.png]]
![[GraphSettings_Menu.png]]
![[MasterStack_Populated.png|320]]
</split>

---
### Lab: Shader Development in Unity
#### Objectives
1. Write a basic color shader.
2. Add texture support.
3. Implement vertex manipulation for dynamic effects.
---
### Additional Learning Resources
<iframe width="560" height="315" src="https://www.youtube.com/embed/3mfvZ-mdtZQ?si=z3o9o9HCkHIHFO2v" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

<iframe width="560" height="315" src="https://www.youtube.com/embed/kfM-yu0iQBk?si=ZtPuyhkaWPRuNbus" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

[The Unity Shader Bible](https://jettelly.com/store/the-unity-shaders-bible)

<iframe width="560" height="315" src="https://www.youtube.com/embed/u5HAYVHsasc?si=o5j2j9hQfNbCt_9P" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

[Shadertoy](https://www.shadertoy.com/)

<iframe width="560" height="315" src="https://www.youtube.com/embed/0v1l-VA6Y9E?si=ulIx6Nf7dURLOsSH" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

---
### Reflection and Discussion
- How do shaders enhance visual storytelling?
- What challenges might arise in shader development?
- Where could you apply shaders in your current projects?
---
### Final Thoughts
- Shaders are a powerful tool for creating immersive, visually striking experiences.
- Mastering shaders bridges a gap between art and technology in game development and beyond.
---
>[!info]  [[GMAP 395 - Module 2| Return to the Module Page]]