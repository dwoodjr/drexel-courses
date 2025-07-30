# Module 3E: VFX Style Guides and Polish

> [!info] Module Overview 
> **Learning Focus:** Creating consistent, readable VFX that enhance gameplay 
**Prerequisites:** Understanding of basic VFX creation

---

## 🎨 What is a VFX Style Guide?


### In Games:

A style guide ensures all VFX look like they belong in the **same game world** and clearly **communicate gameplay information**.

---

## 🎯 Why Style Guides Matter

### Player Clarity (Most Important!)

Players need to **instantly understand** what VFX mean:

- Red particles = Damage/danger
- Green particles = Healing/safe
- Blue particles = Magic/special abilities
- Yellow particles = Important pickup/attention

### Visual Consistency

All effects should feel like they're from the **same universe**:

- Similar color palettes
- Matching visual complexity
- Consistent particle behaviors

### Development Efficiency

Artists can work faster with **clear rules**:

- "All explosions use this fire shader"
- "Healing effects always pulse slowly"
- "Enemy abilities are red, player abilities are blue"

---
## 📋 Style Guide Checklist

Your VFX style guide should define:

- [ ] Color rules for different types of effects
- [ ] Size hierarchy based on importance
- [ ] Timing guidelines for different effect types
- [ ] Visual complexity levels
- [ ] Consistency rules across similar effects
- [ ] Readability requirements
- [ ] Performance budgets

---

## 📖 League of Legends Case Study

![[docs/gmap-395/module-3/media/vfx_styleguide_final_public_hidpjqwx7lqyx0pjj3ss.pdf|vfx_styleguide_final_public_hidpjqwx7lqyx0pjj3ss]]

### LoL's VFX Philosophy:

1. **Clarity First** - Gameplay readability over visual spectacle
2. **Consistent Language** - Similar effects use similar visuals
3. **Hierarchy** - Important effects are bigger/brighter
4. **Team Identity** - Each champion has unique VFX personality

### LoL's Color Rules:

- **Enemy abilities** = Red/Orange (danger!)
- **Friendly abilities** = Blue/Green (safe)
- **Neutral effects** = White/Gray
- **Ultimate abilities** = More intense versions of character colors

### Size and Timing Rules:

- **Basic abilities** = Small, quick effects
- **Ultimate abilities** = Large, dramatic effects with longer duration
- **Passive effects** = Subtle, continuous visuals

---

## 🎨 Creating Your Own Style Guide

### Step 1: Define Your Game's Personality

**Questions to ask:**

- Is your game realistic or stylized?
- What's the overall mood? (Dark/scary, bright/happy, serious/silly)
- What's the setting? (Fantasy, sci-fi, modern, historical)

### Step 2: Establish Color Language

```
Example Color Rules:
- Player effects: Blue (#0080FF)
- Enemy effects: Red (#FF4040)  
- Neutral/Environmental: White/Gray
- Healing: Green (#40FF40)
- Special/Rare: Purple (#8040FF)
```

### Step 3: Set Visual Complexity Levels

```
Effect Importance Hierarchy:
Level 1 (Basic): Simple, small effects
Level 2 (Important): Medium size, more particles
Level 3 (Ultimate): Large, complex, screen-filling
```

---

## ✨ VFX Polish Techniques: All about timing

Visual effects, much like great animation and sound design, need pinpoint accurate timing and event following some of the 12 principles of animation is a good way to develop some of that timing and impactful effect.

### 1. **Anticipation** (Wind-up)

Give players a **warning** before big effects:

```
Big Explosion Sequence:
1. Small sparks (0.5 seconds)
2. Medium glow buildup (1 second)  
3. BOOM! Full explosion (0.2 seconds)
4. Lingering smoke (3 seconds)
```

### 2. **Follow-through** (After-effects)

Don't just stop effects abruptly:

- Explosion → smoke and debris continue
- Magic spell → sparkles fade gradually
- Impact → dust settles slowly

### 3. **Secondary Animation**

Add **extra details** that enhance the main effect:

- Screen shake for explosions
- Camera zoom for critical hits
- UI elements that pulse with effects

### Polish Script Example:
>[!warning] This script is a theoretical example, it may not function in practice.
>The use of `Coroutines` is a great way to fire off different effects in a sequence using C#


```csharp
using UnityEngine;
using UnityEngine.VFX;

public class VFXPolish : MonoBehaviour 
{
    [Header("VFX Components")]
    public VisualEffect mainEffect;
    public VisualEffect anticipationEffect;
    public VisualEffect followThroughEffect;
    
    [Header("Camera Effects")]
    public bool useScreenShake = true;
    public float shakeIntensity = 1f;
    
    public void PlayPolishedEffect() 
    {
        StartCoroutine(PolishedSequence());
    }
    
    System.Collections.IEnumerator PolishedSequence() 
    {
        // Phase 1: Anticipation
        anticipationEffect.Play();
        yield return new WaitForSeconds(1f);
        anticipationEffect.Stop();
        
        // Phase 2: Main effect + Polish
        mainEffect.Play();
        
        if (useScreenShake) 
        {
            CameraShake.Instance.Shake(shakeIntensity);
        }
        
        yield return new WaitForSeconds(0.5f);
        
        // Phase 3: Follow-through
        followThroughEffect.Play();
        mainEffect.Stop();
        
        yield return new WaitForSeconds(2f);
        followThroughEffect.Stop();
    }
}
```

---

## 🎯 Readability Guidelines

### Visual Hierarchy Rules:

1. **Most Important** = Biggest, brightest, center screen
2. **Moderately Important** = Medium size, noticeable but not distracting
3. **Background** = Small, subtle, doesn't compete for attention

### Contrast Guidelines:

- Important effects should **stand out** from background
- Use **complementary colors** for maximum visibility
- **Avoid visual noise** - not every effect needs to be flashy

### Timing Guidelines:

- **Critical information** = Immediate visual feedback
- **Persistent states** = Gentle, continuous effects
- **Temporary effects** = Clear start and end

---

> [!tip] Pro Tip When in doubt, prioritize **gameplay clarity** over visual spectacle. Players need to understand what's happening before they can appreciate how pretty it looks!

---
---

> [!info] 🧭 Module Navigation 
> **Previous:** [[GMAP 395 - Module 3D - Advanced VFX Techniques|Module 3D]]  
> **Return to:** [[GMAP 395 - Module 3|Module Page]]