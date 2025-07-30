# Module 3A: VFX Basics and Game Feel

> [!info] Module Overview 
> **Learning Focus:** Understanding what VFX are and how they make games feel better 
> **Tools:** Unity

> [!summary] Submodule Video Overview
> <iframe src="https://1drv.ms/v/c/b08de2251f1b33a4/IQQXyLMuy5aoSI0I0bwR7nNYAeF-9oirzGBoH17OWu0AaBc?width=2560&height=1440" width="800" height="600" frameborder="0"></iframe>
> 
>[gmap395_md3a.mkv](https://1drv.ms/v/c/b08de2251f1b33a4/ERfIsy7LlqhIjQjRvBHuc1gB3yrx2j5yi6Cquo1ZsbYJcQ?e=qZyddr)

---

## 🎮 What Are VFX?

**VFX = Visual Effects** - basically the "special effects" you see in games that aren't just static objects.

### Here's A Real-World Analogy 🎬

Think of VFX like special effects in movies:

- **Explosions** when something blows up
- **Sparks** when metal hits metal
- **Smoke** coming from a campfire
- **Magic sparkles** around a wizard's spell

In games, these effects happen **in real-time** as you play!

### Common Game VFX Examples:

- ✨ **Particle effects** - sparks, smoke, fire
- 💥 **Explosions** - when grenades go off
- 🌟 **Magic spells** - glowing energy balls
- 💧 **Weather** - rain drops, snow flakes
- 🩸 **Hit effects** - blood splatter, damage numbers

>[!example] So You Wanna Make Games: Episode 7 - VFX
><iframe width="560" height="315" src="https://www.youtube.com/embed/3QKK2o5rWSQ?si=flP9kuJsoBLv4WLC" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

---

## 🎯 Why VFX Matter: Game Feel AKA Juiciness

**Game Feel (Game Juice!)** = How responsive and satisfying a game feels when you play it.

### The Magic Formula:

```
Player Action + Immediate Visual/Audio Response = Good Game Feel
```

### Example Breakdown:

**Okay:** Press jump button → character jumps (boring!) 
**Better:** Press jump button → character jumps + dust particles + screen shake + sound effect (exciting!)

### 🎮 Try This Mental Exercise:

Think about your favorite game. What happens when you (if these apply, maybe they don't...):

- Attack an enemy?
- Pick up an item?
- Take damage?
- Use a special ability?

You'll notice there are probably visual effects for each action!

---

## 🔥 VFX in Action: Real Examples

### Super Mario Bros 🍄

- **Coins:** Sparkle effect when collected
- **Enemies:** Puff of smoke when defeated
- **Power-ups:** Glowing aura around Mario

### Call of Duty 🎯

- **Shooting:** Muzzle flash from gun
- **Hits:** Blood spray + hit markers
- **Explosions:** Fire, smoke, debris particles

### League of Legends ⚔️

- **Abilities:** Each spell has unique VFX
- **Critical hits:** Special sparkle effects
- **Deaths:** Dramatic explosion effects

---

## 🛠️ Unity's VFX Tools: An Overview

Unity gives us **two main tools** for making VFX:

### 1. Particle System (Easier) 🎈

- **Good for:** Simple effects like fire, smoke, sparkles
- **Think of it like:** A "particle sprinkler" that shoots out lots of tiny pieces
- **Beginner-friendly:** Uses menus and sliders (no coding needed!)

### 2. VFX Graph (Advanced) 🔗

- **Good for:** Complex effects with millions of particles
- **Think of it like:** Visual programming with connected boxes
- **More powerful:** Can make movie-quality effects (also no coding, but visual scripting!)

**For now, we'll start with Particle System!**

---

## 🧪 Your First VFX: Quick Unity Demo

Let's make a simple **explosion effect** in 5 steps:

### Step 1: Create Particle System
1. Right-click in Hierarchy
2. Go to **Effects → Particle System**
3. You'll see white dots shooting upward!

### Step 2: Make it Look Like Fire
1. Select your Particle System
2. In Inspector, find **"Start Color"**
3. Change it to **orange** or **red**

### Step 3: Add Some Randomness
1. Find **"Start Speed"**
2. Change the number to make particles move faster/slower
3. Try **"Start Size"** to make particles bigger/smaller

### Step 4: Change the Shape
1. Open **"Shape"** section
2. Change **"Shape"** dropdown from "Cone" to "Sphere"
3. Watch how it changes!

### Step 5: Change the Emission
1. Find "**Looping**," turn it OFF
2. Open **"Emission"** section
3. Add **"Bursts"** by clicking the **"+"** button
4. Change **"Count"** to adjust number of particles up/down.

### Step 6: Test It
Press **Play** and watch your explosion effect!

![[Screenshot 2025-07-29 182816.png]]

---

## 💡 Key Concept: Immediate Feedback

**The Golden Rule:** When a player does something, they should **instantly** see/hear/feel a response.

### Good Examples:
- Click a button → button glows immediately
- Sword hits enemy → sparks fly right away
- Character lands → dust appears at feet

### Bad Examples:
- Click button → nothing happens visually
- Attack enemy → no visual confirmation
- Jump → no landing effect

---

## 🎨 VFX Design Principles

### 1. **Clarity** 📖
Players should understand what's happening

- Healing effects = green particles
- Damage effects = red particles
- Magic effects = blue/purple particles

### 2. **Consistency** 🎯
Similar actions should have similar effects

- All explosions use similar fire colors
- All magic spells have similar sparkle patterns

### 3. **Scale** 📏
Effects should match the importance of the action

- Small action = small effect (picking up coin)
- Big action = big effect (boss death)

---

## 🔍 Spotting Good VFX in Games

**Next time you play a game, try and notice:**

- What visual effects happen when you perform actions?
- How do they make the game feel more responsive?
- Which effects help you understand what's happening?

**Quick Exercise:** Pick a game you know well and write down 3 VFX effects you notice. What purpose does each one serve?

---

> [!tip] Remember VFX aren't just "pretty effects" - they're communication tools that tell players what's happening in your game!

---
---

> [!info] 🧭 Module Navigation 
> **Next:** [[GMAP 395 - Module 3B - Unity Particle System Hands-On|Module 3B]]  
> **Return to:** [[GMAP 395 - Module 3|Module Page]]