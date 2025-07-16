# Module 2B: Shader Development Workflow and 3D Integration

> [!info] Module Overview 
> **Learning Focus:** Understanding shader structure, 3D geometry integration, and material workflows 
> **Builds On:** Shader fundamentals from Module 2A

> [!summary] Submodule Video Overview
> <iframe src="https://1drv.ms/v/c/b08de2251f1b33a4/IQRCKI_0ztslSpw8qrJulgG1AROFcqyPG0IVHSETwz-iA48?width=2560&height=1440" width="800" height="600" frameborder="0"></iframe>
> 
> [gmap395_md2b.mkv](https://1drv.ms/v/c/b08de2251f1b33a4/EUIoj_TO2yVKnDyqsm6WAbUBH3c8nX5N8INVCquAZ7eKyQ?e=D9LR6S)

---

## 🏗️ Shader Workflow and Anatomy

Understanding how shaders are structured helps you approach them systematically rather than feeling overwhelmed by the code.

### 📋 Essential Workflow Steps

> [!success] **Standard Shader Development Process**
> 
> 1. **🎛️ Define Properties:** Expose parameters like color or texture for customization
> 2. **🔧 Create SubShaders:** Specify rendering techniques for different hardware
> 3. **⚡ Write Passes:** Describe rendering steps (vertex and fragment programs)

### 🧬 Anatomy of a Basic Shader

```HLSL
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

> [!tip] **Code Breakdown**
> 
> - **Properties:** `_Color` exposed parameter for material customization
> - **SubShader:** Contains rendering passes for different GPU capabilities
> - **Vertex Function:** Processes vertex data (positions, normals, UVs)
> - **Fragment Function:** Determines final pixel color using vertex shader inputs

---

## 🔧 Core Shader Development Concepts

### 📊 Essential Variable Types

> [!note] **Three Critical Variable Categories**
> 
> **🌐 Uniform Variables:**
> 
> - Global variables constant during rendering of a single draw call
> - Set by CPU and shared across all shader invocations
> - _Examples:_ Time values for animations, transformation matrices
> 
> **📍 Attributes:**
> 
> - Input data unique for each vertex from the vertex buffer
> - Available only in vertex shader
> - _Examples:_ Vertex positions, texture coordinates (`TEXCOORD`)
> 
> **🔀 Varyings:**
> 
> - Variables passing interpolated data from vertex to fragment shader
> - _Examples:_ Lighting data, vertex colors, processed normals

> [!tip] **Further Learning** [The Book of Shaders](https://thebookofshaders.com/) - Excellent resource for deeper shader mathematics

---

## 🎯 Shaders and 3D Geometry Integration

Understanding how shaders connect to 3D geometry is crucial for creating believable materials and effects.

### 📐 3D Geometry Fundamentals

> [!info] **Essential Geometry Components**
> 
> - **🔹 Vertices:** Define points in 3D space
> - **📏 Edges:** Connect vertices to outline shapes
> - **🔺 Faces:** Form surfaces using connected edges
> - **🗺️ UVs:** Map 2D textures to 3D surfaces
> - **➡️ Normals:** Vectors perpendicular to faces for lighting calculations

<iframe width="560" height="315" src="https://www.youtube.com/embed/PfpE5dNTWeI?si=AbwrmazoPmn7mwzQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

### 🔗 How Geometry Connects to Shaders

The relationship between geometry and shaders creates the foundation for all visual effects in games.

> [!example] **Geometry-Shader Connections**
> 
> - **📍 Vertex Data:** Input for vertex shaders to transform 3D geometry
> - **💡 Normals:** Used in lighting equations for realistic shading effects
> - **🗺️ UV Mapping:** Guides texture placement via fragment shaders
> - **🎨 Shader Outputs:** Define the final appearance of geometry on-screen

---

## 🎨 Materials, Textures, and Shader Relationships

Understanding the relationship between these three elements helps you build more sophisticated visual systems.

### 🧩 The Three-Part System

> [!success] **Understanding the Hierarchy**
> 
> **🔧 Shaders:** Small programs executed on the GPU that control light interaction
> 
> **📦 Materials:** Wrappers for shaders that combine textures and parameters
> 
> - Define the look of objects by associating shaders with visual properties
> - _Example:_ A reflective material uses a custom shader for specular highlights
> 
> **🖼️ Textures:** 2D images mapped to 3D geometry
> 
> - Add details like color, patterns, or surface irregularities
> - _Common Types:_ Diffuse, Normal, Specular, Emissive

<iframe width="560" height="315" src="https://www.youtube.com/embed/CBX9Esfnx5I?si=BgGV2MoG6-bE0ZcV" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

---

## ⚡ PBR Workflows in Modern Game Development

**Physically Based Rendering (PBR)** represents the current industry standard for creating realistic materials that respond consistently to lighting.

### 🌟 What Makes PBR Special?

> [!info] **PBR Fundamentals**
> 
> - **Method:** Simulates realistic lighting and material behavior
> - **Key Concepts:** Energy conservation, physically accurate shading
> - **Benefits:** Consistent results across different lighting environments

### 🔧 Standard PBR Workflow Components

> [!success] **Essential PBR Maps**
> 
> 1. **🎨 Base Color:** Defines the albedo (color) of the surface
> 2. **⚙️ Metallic:** Specifies if the material is metal (affects reflection behavior)
> 3. **🔘 Roughness/Smoothness:** Controls surface reflectivity and micro-detail
> 4. **📐 Normal Map:** Adds surface details without additional geometry
> 5. **🌑 Ambient Occlusion (AO):** Simulates soft shadows in surface crevices

> [!tip] **Procedural Material Tool** [Material Maker](https://www.materialmaker.org/) - Free procedural materials authoring tool based on Godot Engine

---

## 🧮 Mathematical Operations in Shader Development

Shaders rely heavily on mathematical operations to create visual effects. Understanding these basics helps you approach shader development more confidently.

### 🔢 Essential Math Concepts

> [!note] **Core Mathematical Operations**
> 
> **📐 Vector Operations:**
> 
> - _Dot Product:_ Essential for lighting calculations
> - _Cross Product:_ Used for calculating surface normals
> 
> **🔄 Matrix Transformations:**
> 
> - Object to world space conversions
> - Camera projection calculations
> 
> **🌈 Color Operations:**
> 
> - RGB blending and color transitions
> - Color space conversions
> 
> **🌊 Noise Functions:**
> 
> - Create procedural patterns for natural effects
> - Generate randomness for organic textures

---

## 📈 Shader Optimization Fundamentals

Writing efficient shaders ensures your game maintains smooth performance across different hardware configurations.

### ⚡ Essential Optimization Strategies

> [!warning] **Performance Best Practices**
> 
> - **🔧 Minimize Complexity:** Use simple math operations where possible
> - **♻️ Reuse Variables:** Avoid redundant calculations within shader code
> - **📊 LOD Techniques:** Reduce detail for distant objects automatically
> - **🎯 Platform Awareness:** Consider target hardware limitations early

---

## 🎮 Real-Time Shader Examples in Games

Understanding common shader applications helps you recognize opportunities in your own projects.

### 🌟 Popular Real-Time Effects

> [!example] **Common Game Shader Applications**
> 
> **💨 Dissolve Effects:** Use noise textures to create object fading effects
> 
> **👻 Holographic Shaders:** Combine transparency with scrolling UV animations
> 
> **🌊 Water Shaders:** Simulate refraction and wave movement for realistic water

> [!tip] **Professional VFX Community** [Real-Time VFX Website](https://realtimevfx.com/) - Industry forum for real-time visual effects

---

## 🚀 Next: Module 2C - Unity Shader Graph Introduction

**Coming up:** We'll explore Unity's visual shader creation tool and learn how to build shaders without writing code.

> [!info] 📍 Progress Tracking
> 
> - [x] Module 2A: Shader Fundamentals and Concepts ✓
> - [x] Module 2B: Shader Development Workflow and 3D Integration ✓
> - [ ] Module 2C: Unity Shader Graph Introduction
> - [ ] Module 2D: Advanced Shader Graph Techniques
> - [ ] Module 2E: Shader Integration and Optimization

---

> [!info] 🧭 Module Navigation 
> **Previous:** [[GMAP 395 - Module 2A - Shader Fundamentals|Module 2A]]  
> **Next:** [[GMAP 395 - Module 2C - Unity Shader Graph Intro|Module 2C]]  
> **Return to:** [[GMAP 395 - Module 2|Module Page]]