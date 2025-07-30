# Module 3B: Unity Particle System Hands-On

> [!info] Module Overview 
> **Learning Focus:** Creating your first VFX with Unity's Particle System 
> **Tools:** Unity, basic shapes

> [!summary] Submodule Video Overview
> <iframe src="https://1drv.ms/v/c/b08de2251f1b33a4/IQQ5ZAqSom-4SK9-384Cg_fsAV0_553uFCHvIb05uZvwU7k?width=2560&height=1440" width="800" height="600" frameborder="0"></iframe>
> 
>[gmap395_md3b.mkv](https://1drv.ms/v/c/b08de2251f1b33a4/ETlkCpKib7hIr37fzgKD9-wBIn7515LcprbP4pqvNtocGw?e=wfqjJj)


---

## 🎈 Understanding Particles

Think of a **Particle System** like a **bubble machine**:

- **The machine** = Particle System component
- **Each bubble** = Individual particle
- **Bubble "properties"** = Size, color, speed, lifetime (how long before they pop!)
- **Machine settings** = How many bubbles per second, which direction

**Key Insight:** You control the "machine," and it creates thousands of individual "bubbles" (particles) automatically.

---

## 🔧 Particle System Components

### Main Settings*:

1. **Start Lifetime** = How long each particle lives (like bubble lifespan)
2. **Start Speed** = How fast particles shoot out
3. **Start Color** = What color the particles are

>[!summary] There are actually way more settings, but to keep it simple start with these

### Shape Settings:

- **Cone** = Particles spray like a garden hose
- **Sphere** = Particles explode outward like fireworks
- **Box** = Particles come from a rectangular area

---

## 🔥 Hands-On: Create a Campfire Effect

Let's build a campfire step-by-step:

### Step 1: Basic Setup

```
1. Create new scene
2. Add Particle System (Effects → Particle System)
3. Name it "Campfire"
4. Position it at (0, 0, 0)
```

### Step 2: Make It Look Like Fire

```
Main Module:
- Start Lifetime: 2
- Start Speed: 3
- Start Color: Orange (#FF4500)
- Start Size: 0.5
```
![[Screenshot 2025-07-29 180313.png]]

### Step 3: Fire Shape

```
Shape Module:
- Shape: Cone
- Angle: 15 (narrow cone)
- Radius: 0.1
```
![[Screenshot 2025-07-29 180237.png]]

### Step 4: Fire Movement

```
Velocity over Lifetime Module:
- Enable this module
- Linear Y: 2 (makes fire go upward)
```
![[particle_3b-4_velocityLifetime 1.png]]

### Step 5: Size Changes (Fire Gets Smaller)

```
Size over Lifetime Module:
- Enable this module
- Size: Create curve that starts at 3 and ends at 0
```
![[particle_3b-5_sizeCurve.png]]


**Test it!** Press Play and you should see orange particles flowing upward like fire!

---

## 💨 Quick Exercise: Make Smoke

Duplicate the Campfire and modify your to create smoke:

```
Changes to make:
- Lifetime: 5 (longer)
- Start Color: Gray (#808080)
- Start Speed: 1 (slower)
- Start Size: 1 (bigger)
- Size over Lifetime: Start at 0.5, end at 2 (grows bigger)
- Position behind the Campfire
```

---

## ⚡ Adding Randomness (Making It Natural)

Real effects aren't perfectly uniform. Add randomness: 
*To change the default type of a parameter hit the down arrow (dropdown menu) to the far right of the value.*
### Random Colors:

Instead of solid orange, use **gradient**:

```
Start Color:
- Set to "Random Between Two Colors"
- Color A: Orange (#FF4500)  
- Color B: Red (#FF0000)
```

### Random Sizes:

```
Start Size:
- Set to "Random Between Two Constants"  
- Min: 0.3
- Max: 0.8
```

### Random Speed:

```
Start Speed:
- Set to "Random Between Two Constants"
- Min: 1.5
- Max: 5  
```
![[Screenshot 2025-07-29 181541.png]]


---

## 🎮 Making VFX Interactive with Code

Let's make particles respond to player input with simple C# script:

### Script: Simple VFX Trigger

```csharp
using UnityEngine;

public class VFXTrigger : MonoBehaviour 
{
    [Header("VFX Settings")]
    public ParticleSystem myEffect;
    public KeyCode triggerKey = KeyCode.Space;
    
    void Update() 
    {
        // When player presses space, play effect
        if (Input.GetKeyDown(triggerKey)) 
        {
            PlayEffect();
        }
    }
    
    void PlayEffect() 
    {
        if (myEffect != null) 
        {
            myEffect.Play();
            Debug.Log("VFX Played!");
        }
    }
}
```

>[!warning] In order for this t work, you need to disable (tick OFF) **"Play on Wake"** in the main module.

### How to Use This Script:

1. Create empty GameObject
2. Add this script to it
3. Drag your Particle System into "My Effect" slot
4. Press Play, then press Spacebar!

![[Screenshot 2025-07-29 182920.png]]

---

## 🎯 Performance Tips (Keep Your Game Running Smooth)

### The Golden Rules:

1. **Limit particle count** - Don't go crazy with numbers
2. **Short lifetimes** - Particles shouldn't live forever
3. **Simple materials** - Fancy textures slow things down
4. **Turn off when not needed** - Use `Stop()` in scripts

### Good Practice Example:

```csharp
public class EfficientVFX : MonoBehaviour 
{
    public ParticleSystem effect;
    
    void Start() 
    {
        // Automatically stop after 5 seconds
        Invoke("StopEffect", 5f);
    }
    
    void StopEffect() 
    {
        effect.Stop();
    }
}
```

---

## 🏃‍♂️ Quick Challenge: Make Hit Effect

**Goal:** Create a "hit effect" that plays when something gets damaged.

**Requirements:**

- Red particles
- Burst emission (not continuous)
- Short lifetime (quick flash)
- Spreads outward from impact point

**Hint:** Look for "Emission" module and change from "Rate over Time" to "Bursts"!

---

## 🔍 Troubleshooting Common Issues

### "I don't see any particles!"

- Check if Particle System is selected
- Make sure Start Color isn't transparent (Alpha value)
- Verify Start Size isn't 0

### "Particles are too fast/slow!"

- Adjust Start Speed
- Check Velocity over Lifetime module

### "Effect looks weird!"

- Reset modules you're not using
- Check Shape settings
- Verify Main module settings

---

## 📋 Module 3B Checklist

By the end of this module, you should be able to:

- [ ] Create a basic Particle System
- [ ] Adjust main settings (lifetime, speed, color, size)
- [ ] Use different emission shapes
- [ ] Add randomness to make effects natural
- [ ] Trigger effects with simple C# scripts
- [ ] Create fire, smoke, and explosion effects

---

> [!tip] Practice Tip Try recreating VFX you see in games you play. Start simple - even basic sparkles or smoke can teach you a lot!

---
---

> [!info] 🧭 Module Navigation 
> **Previous:** [[GMAP 395 - Module 3A - VFX Basics and Game Feel|Module 3A]]  
> **Next:** [[GMAP 395 - Module 3C - VFX Graph Introduction|Module 3C]]  
> **Return to:** [[GMAP 395 - Module 3|Module Page]]