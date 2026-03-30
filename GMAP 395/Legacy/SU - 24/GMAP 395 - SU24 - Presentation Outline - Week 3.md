

---
# Introduction to Shader Development

---

## What Are We Covering Today?

- Review of Game Art Geometry
- Introduction to Shader Development
- Shader Breakdown
- Shader Languages in Unity
- Mathematics for Shaders
- In-Class Lab
- Final Project Review
- Preview of Next Week

Notes: This slide provides an overview of the topics we'll cover in today's session.

Speaker Script: Welcome, everyone! Today, we're diving into the fascinating world of shader development. We'll start by reviewing some key concepts in game art geometry, then move into the basics of shaders, their structure, and the languages we use to write them. We'll also cover some essential math for shaders and get our hands dirty with an in-class lab. Let's get started!

---

## Review of Game Art Geometry: Vertices

- Points in 3D space
- Fundamental building blocks of 3D models
- Defined by X, Y, Z coordinates

[Image: Diagram showing vertices on a simple 3D model]

Notes: Emphasize the importance of vertices as the foundation of 3D graphics.

Speaker Script: Let's start with the basics. Vertices are points in 3D space, defined by their X, Y, and Z coordinates. They're the fundamental building blocks of all 3D models. When we're working with shaders, we often manipulate these vertices to create various effects.

---

## Review of Game Art Geometry: Edges

- Lines connecting vertices
- Define the shape of a 3D model
- Important for silhouettes and outlines

[Image: Diagram highlighting edges on a 3D model]

Notes: Explain how edges contribute to the overall shape and appearance of a model.

Speaker Script: Edges are lines that connect vertices. They define the shape of our 3D models and are particularly important for silhouettes and outlines. In shader development, we might work with edges for effects like cel shading or edge detection.

---

## Review of Game Art Geometry: Faces

- Flat surfaces formed by three or more vertices
- Building blocks of 3D model surfaces
- Triangles are most common in real-time graphics

[Image: Diagram showing faces on a 3D model]

Notes: Highlight the prevalence of triangles in real-time graphics.

Speaker Script: Faces are the flat surfaces formed by three or more vertices. They make up the visible surface of our 3D models. In real-time graphics, we typically use triangles because they're the simplest polygon and most graphics hardware is optimized for triangle rendering.

---

## UV Coordinates

- 2D coordinate system for texturing
- U: horizontal axis, V: vertical axis
- Maps 3D model surface to 2D texture

[Image: UV unwrap of a simple 3D model]

Notes: Explain the concept of UV mapping and its importance in texturing.

Speaker Script: UV coordinates are a 2D coordinate system we use for texturing. The 'U' represents the horizontal axis, and 'V' the vertical. UV mapping allows us to wrap a 2D texture onto our 3D model's surface. This is crucial for applying textures in our shaders.

---

## Texture Mapping

- Process of applying 2D images to 3D surfaces
- Uses UV coordinates to determine placement
- Essential for adding detail to 3D models

[Image: Before and after of a textured 3D model]

Notes: Show examples of how texture mapping adds detail to models.

Speaker Script: Texture mapping is the process of applying 2D images to our 3D surfaces. It uses the UV coordinates we just discussed to determine where each part of the texture should appear on the model. This is essential for adding detail to our 3D models without increasing geometry complexity.

---

## Normals

- Vectors perpendicular to a surface
- Crucial for lighting calculations
- Determine how light interacts with a surface

[Image: Diagram showing normal vectors on a 3D model]

Notes: Emphasize the importance of normals in lighting and shading.

Speaker Script: Normals are vectors that are perpendicular to a surface. They're crucial for lighting calculations in our shaders because they determine how light interacts with a surface. The direction of the normal affects how bright or dark a surface appears under lighting.

---

## What Are Shaders?

- Programs that run on the GPU
- Determine how 3D scenes are rendered to 2D images
- Control visual appearance of objects

Notes: Introduce the concept of shaders as GPU programs.

Speaker Script: Now that we've reviewed the basics of 3D geometry, let's dive into shaders. Shaders are programs that run on the GPU, or Graphics Processing Unit. They determine how our 3D scenes are rendered into the 2D images we see on screen, controlling the visual appearance of objects in our game.

---

## The Role of Shaders in the Rendering Pipeline

1. Vertex Processing
2. Primitive Assembly
3. Rasterization
4. Fragment Processing
5. Output Merging

[Image: Diagram of rendering pipeline]

Notes: Briefly explain each stage of the pipeline.

Speaker Script: Shaders play a crucial role in the rendering pipeline. This process takes our 3D scene data and transforms it into a 2D image. Shaders are primarily involved in the vertex processing stage, where we can manipulate the position and attributes of vertices, and the fragment processing stage, where we determine the final color of each pixel.

---

## Connection to Technical Art and Proceduralism

- Bridge between art and programming
- Enable creation of dynamic, responsive visuals
- Allow for procedural generation of textures and effects

Notes: Highlight how shaders connect art and programming.

Speaker Script: Shaders are a key tool in technical art, bridging the gap between traditional art and programming. They enable us to create dynamic, responsive visuals that can change based on game conditions. Shaders also allow for procedural generation of textures and effects, opening up endless possibilities for unique and efficient visual designs.

---

## Real-World Examples of Shader Usage in Games

- Water effects in "The Legend of Zelda: Breath of the Wild"
- Hologram effects in "Halo"
- Cel-shading in "Borderlands"

[Images: Screenshots of mentioned effects]

Notes: Show visual examples of each effect if possible.

Speaker Script: Shaders are used extensively in modern games. For example, the beautiful water effects in "Breath of the Wild" are created using shaders. The iconic hologram effects in the "Halo" series are also shader-based. And the distinctive cel-shaded look of the "Borderlands" series? You guessed it - shaders!

---

## Anatomy of a Basic Shader

```glsl
Shader "Custom/BasicShader"
{
    Properties
    {
        _Color ("Color", Color) = (1,1,1,1)
    }
    SubShader
    {
        Pass
        {
            CGPROGRAM
            #pragma vertex vert
            #pragma fragment frag
            
            // Shader code here
            
            ENDCG
        }
    }
}
```

Notes: Explain each section of the shader code.

Speaker Script: Let's break down a basic shader. We start with the shader name, then define properties that can be set in the Unity Inspector. The SubShader block contains one or more Pass blocks, which define how the object is rendered. Inside the Pass, we have our actual shader code, starting with CGPROGRAM and ending with ENDCG.

---

## Vertex Shaders

- First programmable stage in the rendering pipeline
- Processes each vertex individually
- Can modify vertex positions, normals, UVs, etc.
- Outputs to fragment shader

Notes: Emphasize the per-vertex nature of vertex shaders.

Speaker Script: Vertex shaders are the first programmable stage in the rendering pipeline. They process each vertex of our 3D models individually. In a vertex shader, we can modify the position, normal, UV coordinates, and other attributes of each vertex. The output of the vertex shader is then passed to the fragment shader.

---

## Fragment Shaders

- Also known as pixel shaders
- Runs for each pixel covered by a triangle
- Determines final color of each pixel
- Can perform texture sampling, lighting calculations, etc.

Notes: Highlight the per-pixel nature of fragment shaders.

Speaker Script: Fragment shaders, also known as pixel shaders, run for each pixel that's covered by a triangle in our 3D model. The main job of a fragment shader is to determine the final color of each pixel. This is where we perform operations like texture sampling, lighting calculations, and any other per-pixel effects.

---

## Shader Inputs and Outputs

Inputs:
- Vertex data (position, normal, UV, etc.)
- Textures
- Uniform variables

Outputs:
- Vertex shader: Modified vertex data
- Fragment shader: Final pixel color

Notes: Explain the flow of data through the shader stages.

Speaker Script: Shaders work with various inputs and outputs. Inputs can include vertex data like position and normal, textures, and uniform variables that we set from our game code. The vertex shader outputs modified vertex data, which becomes input for the fragment shader. The fragment shader's final output is the color of each pixel.

---

## Uniforms, Attributes, and Varying Variables

- Uniforms: Global variables set from CPU
- Attributes: Per-vertex input data
- Varying: Data passed from vertex to fragment shader

Notes: Explain the differences and uses of each variable type.

Speaker Script: In shaders, we work with different types of variables. Uniforms are global variables that we can set from our CPU-side code. Attributes are per-vertex input data, like position or normal. Varying variables are used to pass data from the vertex shader to the fragment shader, like interpolated colors or UVs.

---

## Overview of HLSL

- High-Level Shading Language
- Used in DirectX and Unity
- C-like syntax
- Designed specifically for graphics programming

Notes: Introduce HLSL as the primary shader language in Unity.

Speaker Script: In Unity, we primarily use HLSL, which stands for High-Level Shading Language. It's the shader language used in DirectX and has a C-like syntax. HLSL is designed specifically for graphics programming, providing features and optimizations that are particularly useful for shader development.

---

## Comparison with Other Shader Languages

- GLSL (OpenGL Shading Language)
- CG (C for Graphics)

Similarities:
- C-like syntax
- Designed for graphics

Differences:
- Platform support
- Some syntax variations

Notes: Briefly compare HLSL with GLSL and CG.

Speaker Script: While we focus on HLSL in Unity, it's worth knowing about other shader languages. GLSL is used with OpenGL, and CG is a language developed by NVIDIA. They all have C-like syntax and are designed for graphics, but there are differences in platform support and some syntax variations.

---

## Basic Syntax and Structure of Unity Shaders

```glsl
Shader "Custom/MyShader"
{
    Properties { /* ... */ }
    SubShader
    {
        Tags { /* ... */ }
        CGPROGRAM
        #pragma vertex vert
        #pragma fragment frag
        
        struct appdata { /* ... */ }
        struct v2f { /* ... */ }
        
        v2f vert (appdata v) { /* ... */ }
        fixed4 frag (v2f i) : SV_Target { /* ... */ }
        ENDCG
    }
}
```

Notes: Walk through the basic structure of a Unity shader.

Speaker Script: This slide shows the basic structure of a Unity shader. We have our shader name, properties, and a SubShader block. Inside the SubShader, we define our vertex and fragment functions, along with any necessary structs for passing data between them. The actual shader code goes between CGPROGRAM and ENDCG.

---

## Vector Operations in Shaders

- Vector addition and subtraction
- Scalar multiplication
- Dot product
- Cross product

Example:
```glsl
float3 a = float3(1, 2, 3);
float3 b = float3(4, 5, 6);
float3 c = a + b; // (5, 7, 9)
float d = dot(a, b); // 32
```

$$ \begin{align*} \text{Addition:} & \quad \vec{a} + \vec{b} = (a_1 + b_1, a_2 + b_2, a_3 + b_3) \[10pt] \text{Scalar Multiplication:} & \quad k\vec{a} = (ka_1, ka_2, ka_3) \[10pt] \text{Dot Product:} & \quad \vec{a} \cdot \vec{b} = a_1b_1 + a_2b_2 + a_3b_3 \[10pt] \text{Cross Product:} & \quad \vec{a} \times \vec{b} = (a_2b_3 - a_3b_2, a_3b_1 - a_1b_3, a_1b_2 - a_2b_1) \end{align*} $$
Notes: Demonstrate basic vector operations used in shaders.

Speaker Script: Vector math is crucial in shader development. We frequently use operations like addition, subtraction, scalar multiplication, dot product, and cross product. These operations allow us to manipulate positions, directions, and colors in our shaders.

---

## Matrix Operations in Shaders

- Matrix multiplication
- Transformation matrices (translation, rotation, scaling)

Example:
```glsl
float4x4 worldMatrix;
float4 localPos = float4(vertex.xyz, 1);
float4 worldPos = mul(worldMatrix, localPos);
```

Notes: Explain the importance of matrices for transformations.

Speaker Script: Matrices are essential for transforming our 3D models. We use matrix multiplication to apply transformations like translation, rotation, and scaling. In shaders, we often use matrices to convert between different coordinate spaces, like from object space to world space.

---

## Color Spaces and Operations

- RGB vs HSV
- Color blending
- Gamma correction

Example:
```glsl
fixed4 color1 = fixed4(1, 0, 0, 1); // Red
fixed4 color2 = fixed4(0, 1, 0, 1); // Green
fixed4 blended = lerp(color1, color2, 0.5); // Yellow
```

Notes: Discuss different color spaces and common color operations.

Speaker Script: Understanding color spaces and operations is crucial for shader development. We typically work in RGB space, but sometimes HSV can be useful. Color blending, using functions like lerp, allows us to create smooth transitions between colors. We also need to be aware of gamma correction to ensure our colors appear correctly on different displays.

---

## Common Mathematical Functions in Shaders

- Trigonometric functions (sin, cos, tan)
- Interpolation functions (lerp, smoothstep)
- Clamping and remapping functions

Example:
```glsl
float wave = sin(_Time.y * frequency) * amplitude;
float t = saturate((value - min) / (max - min));
```

Notes: Highlight frequently used math functions in shader development.

Speaker Script: Shaders make use of a variety of mathematical functions. Trigonometric functions like sine and cosine are great for creating wave-like movements. Interpolation functions like lerp and smoothstep allow for smooth transitions. We also frequently use clamping and remapping functions to keep values within desired ranges.

---

## In-Class Lab: Introduction to Shader Language

- Writing a simple color shader
- Adding texture support
- Basic vertex manipulation

Notes: Briefly introduce the lab exercise.

Speaker Script: Now it's time to put what we've learned into practice! In this lab, we'll write a simple color shader, then add texture support, and finally implement some basic vertex manipulation. This hands-on experience will help solidify the concepts we've covered today.

---

## Final Project: Shader Requirements

- Implement at least 2 custom shaders
- Demonstrate understanding of vertex and fragment shaders
- Incorporate texturing and vertex manipulation
- Consider performance and optimization

Notes: Outline the shader-related requirements for the final project.

Speaker Script: For your final project, you'll need to implement at least two custom shaders. These should demonstrate your understanding of both vertex and fragment shaders. You should incorporate texturing and some form of vertex manipulation. Remember to consider performance and optimization in your shader design.

---

## Q&A Session

- Any questions about shaders?
- Clarifications on the final project requirements?
- Additional resources or support needed?

Notes: Encourage students to ask questions about the material covered or the final project.

Speaker Script: Before we wrap up, let's take some time for questions. Does anyone need clarification on any of the shader concepts we've covered today? Or perhaps you have questions about the shader requirements for the final project? This is a great time to ask!

---

## Preview: Introduction to Shader Graph

- Visual shader creation tool in Unity
- Node-based interface
- Allows for rapid prototyping and iteration

[Image: Screenshot of Unity Shader Graph interface]

Notes: Give a brief preview of what will be covered in the next session.

Speaker Script: In our next session, we'll be diving into Unity's Shader Graph. This is a powerful visual tool for creating shaders, using a node-based interface. It allows for rapid prototyping and iteration, making it easier to experiment with different shader effects. We'll explore how Shader Graph can streamline our shader development process.

---

## Importance of Visual Shader Development

- Accessibility for artists and non-programmers
- Faster iteration and prototyping
- Visualization of data flow in shaders
- Bridge between technical requirements and artistic vision

Notes: Highlight the benefits of visual shader development tools.

Speaker Script: Visual shader development tools like Shader Graph are becoming increasingly important in game development. They make shader creation more accessible to artists and non-programmers, allow for faster iteration and prototyping, and provide a clear visualization of how data flows through our shaders. These tools serve as a bridge between technical requirements and artistic vision