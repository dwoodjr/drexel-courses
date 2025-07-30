# Module 3C: VFX Graph Introduction

> [!info] Module Overview 
> **Learning Focus:** Understanding VFX Graph and node-based VFX creation 
> **Prerequisites:** Module 3B completed

> [!summary] Submodule Video Overview
> <iframe src="https://1drv.ms/v/c/b08de2251f1b33a4/IQRuq7ZN3M47Q5wQ-VF3dIeJAVzKI5q3HXth89XQuuF7OmI?width=2560&height=1440" width="800" height="600" frameborder="0"></iframe>
> 
>[gmap395_md3c.mkv](https://1drv.ms/v/c/b08de2251f1b33a4/EW6rtk3czjtDnBD5UXd0h4kBzRlVxlOh2ifwxUKOiS1gVQ?e=AwZEgU)


---

## 🔗 What is VFX Graph?

**VFX Graph** is like building with **LEGO blocks**:

- **Each block** = A node that does one job
- **Connecting blocks** = Wires that pass information
- **Final creation** = Complex VFX effect
- **No programming** = Visual connections instead of code

### Particle System vs VFX Graph:

|Particle System|VFX Graph|
|---|---|
|🎚️ Sliders & dropdowns|🔗 Connected boxes|
|🖥️ CPU-based (slower)|⚡ GPU-based (much faster)|
|👶 Beginner-friendly|🎓 More advanced|
|1000s of particles|Millions of particles|

---

## 🎮 Why Use VFX Graph?

### Real-World Examples:

- **Explosions** with thousands of debris pieces
- **Magic spells** with complex particle interactions
- **Environmental effects** like falling leaves or rain
- **Weapon effects** like detailed muzzle flashes

### Key Benefits:

1. **Performance** - Uses GPU for massive particle counts and faster computation
2. **Flexibility** - Can create near movie-quality effects
3. **Reusability** - Save node networks as templates

---

## 🛠️ Setting Up VFX Graph

### Installation Steps:

```
1. Window → Package Manager
2. Search "Visual Effect Graph"
3. Click Install
```

### Render Pipeline Requirement:

VFX Graph **only works** with one of the Scriptable Render Pipelines (SRP):

- Universal Render Pipeline (URP)
- High Definition Render Pipeline (HDRP)

**Not compatible with Built-in Render Pipeline!**

![[Screenshot 2025-07-29 183420.png]]

---

## 🧩 Understanding Nodes (The Building Blocks)

### Node Types:

#### 1. **Context Nodes** (The Big Boxes)

- **Spawn** = Number/how particles are born
- **Initialize** = Starting particle properties
- **Update** = How particles change over time
- **Output** = How particles look when rendered

![[Screenshot 2025-07-29 184357.png]]

#### 2. **Block Nodes** (The Actions)

- **Set Position** = Where particle appears
- **Set Velocity** = How fast/direction particle moves
- **Set Color** = Particle color
- **Set Size** = Particle size
- **+ MANY MANY MORE**

![[Screenshot 2025-07-29 184430.png]]

#### 3. **Operator Nodes** (The Math)

- **Add** = Adds two numbers
- **Multiply** = Multiplies numbers
- **Random** = Creates random values
- **Time** = Gets current game time
- **+ MANY MANY MORE**

---

## 🔥 Your First VFX Graph: Simple Fire

### Step 1: Create VFX Graph

```
1. Project window (VFX folder) → Right-click
2. Create → Visual Effects → Visual Effect Graph
3. Name it "SimpleFireVFX"
```

### Step 2: Add to Scene

```
1. Drag VFX Graph to scene
2. It creates a GameObject with Visual Effect component
3. You should see default particles
```

### Step 3: Open Graph Editor

```
1. Double-click your VFX Graph asset
2. VFX Graph window opens
3. You'll see connected boxes (contexts)
```

### Step 4: Customize for Fire

```
In the Initialize context:
1. Find the "Output Particle Quad" Context
2. Change the "Set Color over Life" to a gradient from red to yellow
3. Change the "Main Texture" to Default-Particle (the white one)
4. Change "Set Size over Life" curve to go from from 1 to 0
```

![[Screenshot 2025-07-29 190811.png]]

---

## 🎯 Key Concepts: Contexts and Flow

### The VFX Graph "Pipeline":

```
SPAWN → INITIALIZE → UPDATE → OUTPUT
   ↓        ↓          ↓        ↓
Create    Set Start   Change    Draw
Particles Properties  Over Time Particles
```

### Real-World Analogy (Factory Assembly Line):

1. **Spawn** = Factory creates new toys
2. **Initialize** = Paint toys, add stickers
3. **Update** = Toys move on conveyor belt, might change
4. **Output** = Finished toys ready for display

---

## ⚡ Basic Node Operations

### Connecting Nodes:

- **Click and drag** from output port to input port
- **Lines** show data flow between nodes
- **Colors** indicate data types (float, vector, texture)

### Adding Blocks:

```
1. Right-click in Context
2. Choose "Create Block" 
3. Searh for block type
4. Block appears in Context
5. Adjust properties
```

### Common Shortcuts:

- **Spacebar** = Open node creation menu
- **Delete** = Remove selected nodes
- **Ctrl+Z** = Undo changes


---

## 🎨 Properties and Attributes

VFX Graph has a ***Blackboard*** just like Shader Graph for creating parameters! = `<x>`


![[Screenshot 2025-07-29 191305.png]]
### Properties (Global Settings):
- **Shared across all particles**
	- Example: Overall effect color, intensity
- **Exposed to Inspector** - designers/developers can adjust in *Inspector* or via **Code**

### Attributes (Per-Particle Data):
- **Individual to each particle**
	- Example: Each particle's position, velocity, age
- **Automatically managed** by VFX Graph

### Simple Property Example:

```csharp
// Expose a color property
// In VFX Graph: Create Property → Color → Name it "EffectColor"
// In Inspector: You can now change the color without opening VFX Graph
```

---

## 🔧 Connecting to Code (Basic)

### Script to Control VFX Graph:

```csharp
using UnityEngine;
using UnityEngine.VFX;

public class VFXController : MonoBehaviour 
{
    [Header("VFX Control")]
    public VisualEffect vfxGraph;
    public KeyCode playKey = KeyCode.Space;
    
    void Start()
    {
        // Stop the effect from playing on wake
        vfxGraph.Stop();
    }
    
    void Update() 
    {
        if (Input.GetKeyDown(playKey)) 
        {
            PlayVFX();
        }
    }
    
    void PlayVFX() 
    {
        // Play the effect
        vfxGraph.Play();
        
        // Or trigger a burst event
        vfxGraph.SendEvent("OnPlay");
    }
    
    void ChangeColor() 
    {
        // Change a property (if you have a Color property called "EffectColor")
        vfxGraph.SetVector4("EffectColor", Color.red);
    }
}
```

>[!warning] Notice
>Controlling VFX Graph via Scripting (Code) requires a specific "using statement" to access the class `using UnityEngine.VFX`.

---

## 🚨 Common Beginner Errors

### 1. "My VFX doesn't show up!"

- Check if using URP/HDRP (not Built-in Render Pipeline)
- Verify Visual Effect component has your VFX Graph assigned
- Make sure particles aren't transparent or too small

### 2. "Everything is connected but nothing happens!"

- Check if Spawn context is actually spawning particles
- Verify Initialize context has basic properties set
- Look for broken connections

### 3. "Performance is terrible!"

- Reduce particle count in Spawn context
- Check if you have infinite loops in Update context
- Avoid too many complex calculations

---

## 📋 Module 3C Checklist

You should understand:

- [ ] What VFX Graph is and why it's powerful
- [ ] The difference between Particle System and VFX Graph
- [ ] Basic node types (Context, Block, Operator)
- [ ] The VFX pipeline flow (Spawn → Initialize → Update → Output)
- [ ] How to create a simple fire/sparkle effect
- [ ] How to connect VFX Graph to C# scripts

---

> [!tip] Practice Tip Start simple! Master basic fire and sparkle effects before attempting complex systems.

---
---

> [!info] 🧭 Module Navigation 
> **Previous:** [[GMAP 395 - Module 3B - Unity Particle System Hands-On|Module 3B]]  
> **Next:** [[GMAP 395 - Module 3D - Advanced VFX Techniques|Module 3D]]  
> **Return to:** [[GMAP 395 - Module 3|Module Page]]