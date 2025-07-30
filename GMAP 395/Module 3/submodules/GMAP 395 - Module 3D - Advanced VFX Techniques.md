# Module 3D: Advanced VFX Techniques

> [!info] Module Overview 
> **Learning Focus:** Mesh emission, decals, collisions, and shaders 
>  **Prerequisites:** Module 3C completed

---

## 🎯 Mesh Emission (Particles from 3D Objects)

### What is Mesh Emission?

Instead of particles coming from a simple shape (sphere, cone), they come from **any 3D model**.

**Think of it like:**

- Rain falling from cloud-shaped mesh
- Fire coming from torch handle mesh
- Magic particles following character's sword mesh

### When to Use Mesh Emission:

- Character abilities (particles follow weapon/hands)
- Environmental effects (leaves falling from tree mesh)
- Destruction effects (debris from broken object mesh)

---

## 🔥 Hands-On: Character Fire Aura

### Step 1: Setup Scene

```
1. Create/import character model
2. Create new VFX Graph: "CharacterAura"
3. Add Visual Effect component to character
```

>[!Error] On Imported Meshes
>Imported meshed must have their mesh data be set to **"Read/Write"**
>This can be done by selecting the mesh in the project window, then in the Inspector > Model Tab > Read/Write enables (tick ON)
>
![[Screenshot 2025-07-29 200313.png]]

### Step 2: Configure Mesh Emission

```
In VFX Graph:
1. Select Initialize context
2. Add "Set Position (Mesh)" block
3. Select character mesh to "Mesh" field
4. Set "Placement Mode" to "Surface"
5. Adjust the "Scale" as needed
```

### Step 3: Add Fire Properties

```
Initialize Context:
- Set Color: Orange gradient
- Set Velocity: Upward + random spread
- Set Size: Small (0.1-0.3)
- Set Lifetime: 2 seconds
```

**Result:** Fire particles now emit from character's surface!

![[Screenshot 2025-07-29 200753.png]]

---

## 🎨 Decals in VFX Graph

### What are Decals?

**Decals** = Images projected onto surfaces (like stickers on walls)

**Game Examples:**

- Bullet holes on walls
- Blood splatters on ground
- Magic circles under characters
- Scorch marks from explosions

### Decal vs Particle Difference:

|Particles|Decals|
|---|---|
|Float in space|Stick to surfaces|
|3D objects|2D projections|
|Move around|Stay in place|

---

## ⚡ Collision Detection in VFX Graph

### Why Collisions Matter:

- Particles bounce off walls realistically
- Rain drops splash when hitting ground
- Magic effects interact with environment

### Simple Collision Setup:

```
In VFX Graph Update Context:
1. Add "Collide with AABox" block
2. Enable "Bounce" for bouncing particles
3. Adjust "Bounce" value (0 = no bounce, 1 = perfect bounce)
4. Set "Lifetime Loss" for particles that fade on impact
```

### URP vs. HDRP
Some of the Collision💥 Nodes only work in HDRP (well really just one the `Collide with Depth Buffer`). There are some workarounds out there but the are not %100 and require a lot of work to get functioning.

---

## 🎭 Connecting Shaders to VFX

Yes, you can make a custom shader for achieve a certain look to your particles! This allow for a lot of control over the visual style and rendering of teh individual aprticles. But try and use *simple* shaders on particles as you may be generating millions of them.

### Why Use Shaders?

**Shaders** control how particles look when rendered:

- Glowing energy effects
- Transparent smoke
- Refractive distortions
- Animated textures

### Simple Shader Integration:

```
1. Create new Shader Graph
2. In VFX Graph Output context
3. Set "Shader Graph" to your custom shader
4. Connect VFX properties to shader inputs
```

---

## 🎯 Performance Optimization

### Key Rules:

1. **Limit active effects** - Don't run 50 VFX all  at once
2. **Use object pooling** - Reuse VFX objects instead of creating new ones when possible
3. **Control particle counts** - More particles = slower performance
4. **Clean up old effects** - Destroy or stop VFX when not needed

---

## 🔧 Procedural VFX (Rule-Based Effects)

### What is Procedural VFX?

Effects that **change based on rules** instead of being pre-made.

**Examples:**

- Fire gets bigger when there's more fuel
- Lightning changes path based on obstacles
- Particle color changes based on player health

### Simple Procedural Example:
>![example] To Get This Script to Work
>On your Simple Fire VFX Graph add a *float* property called `Intensity` and use by multiplying another number to control the Rate (another float).
>![[Screenshot 2025-07-29 210550.png]]
>Also add another *color* called `FireColor` and multiply the original `EffectColor` by this to set the color.
>![[Screenshot 2025-07-29 210716.png]]
>With these in place the following script should function!


```csharp
using UnityEngine;
using UnityEngine.VFX;

public class ProceduralFire : MonoBehaviour 
{
    [Header("Fire Settings")]
    public VisualEffect fireVFX;
    public float fuelAmount = 100f;
    public float burnRate = 10f;
    
    void Update() 
    {
        // Burn fuel over time
        fuelAmount -= burnRate * Time.deltaTime;
        
        // Scale fire intensity based on fuel
        float intensity = fuelAmount / 100f; // 0 to 1
        
        // Update VFX properties
        fireVFX.SetFloat("Intensity", intensity);
        fireVFX.SetVector4("FireColor", GetFireColor(intensity));
        
        // Extinguish when no fuel
        if (fuelAmount <= 0 && fireVFX.isActiveAndEnabled) 
        {
            fireVFX.Stop();
        }
    }
    
    Color GetFireColor(float intensity) 
    {
        // Blue (cold) to Red (hot) to Yellow (hottest)
        if (intensity > 0.7f) return Color.yellow;
        else if (intensity > 0.3f) return Color.red;
        else return Color.blue;
    }
    
    public void AddFuel(float amount) 
    {
        fuelAmount += amount;
        if (!fireVFX.isActiveAndEnabled) 
        {
            fireVFX.Play(); // Restart fire
        }
    }
}
```

---

## 🎮 Modular VFX Design

### What is Modular VFX?

Breaking effects into **reusable pieces** that can be mixed and matched. You are able to create Subgraphs and custom Blocks with reusable nodes or bits of code. This allows for much easier development when there are multiple effects that need to use the same base defaults or operations. Do something once, then reuse it.

### Component-Based Approach:

```
Explosion = Base Blast + Fire Particles + Smoke + Debris + Screen Shake
Magic Spell = Energy Core + Sparkles + Glow + Trail + Impact
```


---

## 🚨 Common Advanced Mistakes

### 1. "My mesh emission isn't working!"

- Check if mesh has proper vertices/faces
- Verify mesh is imported correctly and has Read/Write enabled
- Try different "Placement Mode" settings (Surface, Volume, Vertex)

### 2. "Collision detection is slow!"

- Use simplified collision meshes
- Limit collision check frequency
- Consider using trigger volumes instead of per-particle collision

### 3. "Shaders look wrong in VFX!"

- Ensure shader is compatible with VFX Graph output
- Check if shader properties are properly exposed
- Verify URP/HDRP compatibility

---

## 📋 Module 3D Checklist

You should be able to:

- [ ] Set up mesh emission from 3D objects
- [ ] Create and use decals for surface effects
- [ ] Implement collision detection for particles
- [ ] Connect custom shaders to VFX Graph
- [ ] Build modular, reusable VFX systems
- [ ] Write scripts that control VFX properties
- [ ] Optimize VFX for better performance

---
---

> [!info] 🧭 Module Navigation 
> **Previous:** [[GMAP 395 - Module 3C - VFX Graph Introduction|Module 3C]]  
> **Next:** [[GMAP 395 - Module 3E - VFX Style Guides and Polish|Module 3E]]  
> **Return to:** [[GMAP 395 - Module 3|Module Page]]