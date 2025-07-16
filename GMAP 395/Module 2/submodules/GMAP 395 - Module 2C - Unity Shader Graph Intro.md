# Module 2C: Unity Shader Graph Introduction

> [!info] Module Overview 
> **Learning Focus:** Getting started with Unity's visual shader creation tool **
> Builds On:** Shader structure and workflow concepts from Module 2B

> [!summary] Submodule Video Overview
> <iframe src="https://1drv.ms/v/c/b08de2251f1b33a4/IQQW0TqMDw8hRZw5QBdXHF2YAczUnuUToZ2r7MuLdlxbjmM?width=2560&height=1440" width="800" height="600" frameborder="0"></iframe>

---

## 🎨 What is Unity Shader Graph?

Unity `Shader Graph` represents a fundamental shift in how we approach shader creation. Instead of writing (often) complex HLSL code, you can create sophisticated visual effects using a node-based interface (this form of *visual scripting* is something we have seen quite a bit now).

Think of Shader Graph as a visual translation layer that converts your creative ideas into the mathematical operations that GPUs understand. Most of the noes in visual scripting tools turn the visual operations into actual code and instructions in the background. When you connect nodes together, you're essentially building the same logic that would exist in written shader code (generally, with some small difference here and there), but in a way that makes the relationships between different operations much more visible and intuitive.

### 🔧 Core Requirements and Setup

Before diving into Shader Graph, you need to understand one important technical requirement (for the version of Unity we use in the course). Shader Graph operates exclusively within Unity's **Scriptable Render Pipeline (SRP)**, which means you cannot use it with the built-in render pipeline that Unity uses by default. For this course, we recommend using the **Universal Render Pipeline (URP)** because it provides excellent performance across different platforms while maintaining the flexibility you need for learning and applying your own artistic touches.

---

## 🖥️ Understanding the Shader Graph Interface

### 📋 Essential Interface Components

The **Blackboard** serves as your shader's control panel, where you define and expose parameters that other team members can adjust without opening the shader itself. When you create a property in the Blackboard, you're essentially saying "this is something that should be adjustable by designers or programmers in the editor. (assuming the property is *Exposed*)"

![[GMAP 395/Module 2/media/blackboard_shadergraph_path.png]]

The **Graph Inspector** provides contextual information about whatever node you currently have selected; it offers detailed explanations of what each node does and how its parameters affect the final result. It also provides settings for the full shader graph itself.

![[InternalInspectorBlackboardProperty.png]]

The **Main Stack** handles the core logic of your shader, separating vertex operations (which affect geometry) from fragment operations (which determine pixel colors). This separation mirrors the fundamental shader structure discussed in previous modules.

![[GMAP 395/Module 2/media/MasterStack_Populated.png]]

The **Main Preview** shows real-time updates of your shader as you work. 
> [!warning] Honestly, the preview is really not very useful and tends to stop working frequently.
When in doubt, always test your shader on actual geometry in your scene to see how it truly behaves under real lighting conditions. 


The **Toolbar** contains essential functions for saving, compiling, and debugging your shaders.

> [!note] **Official Documentation** [Shader Graph Documentation](https://docs.unity3d.com/Packages/com.unity.shadergraph@14.0/manual/Getting-Started.html) provides comprehensive technical reference for all Shader Graph features.

---

## 🔄 Connecting Shader Graph to Previous Concepts

Understanding how Shader Graph relates to the traditional shader concepts already covered will help you approach visual shader creation with a stronger foundation. When you create a node in Shader Graph, you're essentially creating a visual representation of code that would otherwise need to be written by hand.

### 🧬 Visual Representation of Shader Anatomy

Remember the shader code structure we examined in [[GMAP 395 - Module 2B - Shader Dev and 3D|Module 2B]]? Shader Graph takes those same concepts and presents them visually. When you connect a Texture Sample node to the Base Color input of your Main Stack, you're performing the same operation as writing texture sampling code in a traditional fragment shader.

Properties that you define in the Blackboard correspond directly to the Properties section of written shader code. The difference is that Shader Graph automatically handles the technical details of exposing these properties to Unity's material inspector.

### 🎯 Node-Based Logic vs. Written Code

Each node in Shader Graph represents a specific mathematical operation or data manipulation. A Multiply node performs the same function as a multiplication operation in written HLSL code.

*This visual approach becomes particularly powerful when dealing with complex operations like normal mapping or procedural texture generation.* Instead of writing mathematical formulas from scratch, you can build up these effects step by step, seeing the intermediate results at each stage of the process.

---

## 🎮 Building Your First Shader Graph

Creating your first shader in Shader Graph should feel like a guided exploration rather than a technical challenge. ***Start with simple concepts and gradually build complexity as you become more comfortable with the interface.***

### 🎨 Starting with Basic Color Control

Begin by creating a new Unlit Shader Graph and focus on understanding how data flows from inputs to outputs. Add a `Color` property to your Blackboard and connect it directly to the `Base Color` input of your *Fragment* stack. This simple connection demonstrates the fundamental concept of Shader Graph: visual nodes represent data, and connections between nodes represent the flow of that data through your shader.

When you apply this shader to a material and then to a 3D object, you're seeing the same result you would get from the basic shader code we examined earlier, but achieved through visual means rather than written code. ***This equivalence is important to understand because it reinforces that Shader Graph is not a separate technology, but instead a different way of creating the same underlying GPU programs.***

### 🔧 Understanding Data Types and Connections

As you experiment with connecting different nodes, pay attention to the colors of the connection lines. These colors represent different data types:

| Name       | Color  | Hex Value |
| ---------- | ------ | --------- |
| Artistic   | Orange | `#DB773B` |
| Channel    | Green  | `#97D13D` |
| Input      | Red    | `#CB3022` |
| Math       | Blue   | `#4B92F3` |
| Procedural | Purple | `#9C4FFF` |
| Utility    | Gray   | `#AEAEAE` |
| UV         | Teal   | `#08D78B` |

Understanding these data types helps you make appropriate connections and avoid common mistakes. For example, connecting a Vector3 color output to a float input will automatically convert the color to a single grayscale value, which might not be what you intended.

---

## 🎯 Learning Check: Interface Exploration

> [!question] 🤔 **Hands-On Exploration (5-7 minutes)**
> 
> Open Unity and create a new Shader Graph asset. Spend a few minutes exploring the interface without trying to create anything specific. Focus on understanding the relationship between different interface elements.
> 
> **Consider these questions as you explore:**
> 
> - How does adding a property to the Blackboard change what's available in the main graph area?
> - What happens when you select different nodes and observe the Graph Inspector?
> - How does the preview update when you make changes to your graph?
> 
> **Write down 2-3 observations** about how the visual interface relates to the shader concepts we've discussed in previous modules.


---

## 🚀 Next: Module 2D - Advanced Shader Graph Techniques

**Coming up:** We'll explore sophisticated Shader Graph techniques including texture manipulation, vertex displacement, and procedural pattern generation.

> [!info] 📍 Progress Tracking
> 
> - [x] Module 2A: Shader Fundamentals and Concepts ✓
> - [x] Module 2B: Shader Development Workflow and 3D Integration ✓
> - [x] Module 2C: Unity Shader Graph Introduction ✓
> - [ ] Module 2D: Advanced Shader Graph Techniques
> - [ ] Module 2E: Shader Integration and Optimization

---
----

> [!info] 🧭 Module Navigation 
> **Previous:** [[GMAP 395 - Module 2B - Shader Dev and 3D|Module 2B]]  
> **Next:** [[GMAP 395 - Module 2D - Additional Shader Graph Techniques|Module 2D]]  
> **Return to:** [[GMAP 395 - Module 2|Module Page]]