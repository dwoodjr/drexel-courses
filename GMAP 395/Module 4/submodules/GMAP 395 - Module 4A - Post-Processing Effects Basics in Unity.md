# Module 4A: Post-Processing Effects Basics in Unity

> [!info] Module Overview 
> **Learning Focus:** Understanding what post-processing effects are and how they enhance player experience and artistic vision 
> **Tools:** Unity URP, Visual understanding 
> **Builds On:** Game feel concepts from [[GMAP 395 - Module 1A - Game Feel and Tactile Experience]]

> [!summary] Submodule Video Overview
> <iframe src="https://1drv.ms/v/c/b08de2251f1b33a4/IQQ8d2nQ0LdDQY8yvgb-Bo5yARYDGAmCf5MoVFCqdVQj7ek?width=2560&height=1440" width="800" height="600" frameborder="0"></iframe>
> 
>[gmap395_md4a.mkv](https://1drv.ms/v/c/b08de2251f1b33a4/ETx3adDQt0NBjzK-Bv4GjnIB_TiLJ5C4CtHUJO5bxJr99Q?e=qiNBed)

---

## 🎨 What Are Post-Processing Effects?

**Post-processing effects** are visual enhancements applied to a camera's rendered image before display - think of them as **"magic glasses"** that transform how players see your game world!

### A Real-World Analogy 📷

Think of post-processing like **image filters for games**:

- **Original photo** = your 3D scene rendered normally
- **Filter applied** = post-processing effect added
- **Final result** = the stylized image players actually see

Just like how colored sunglasses change the mood of everything you look at, post-processing effects change the **entire visual feeling** of your game!

![[GMAP 395/Module 4/media/home-before.png]]
![[GMAP 395/Module 4/media/home-after.png]]

---

## ✨ Common" Game Post-Processing Effects in Unity

>[!warning] [Unity 2022.3 URP Post-Processing Documentation](https://docs.unity3d.com/2022.3/Documentation/Manual/PostProcessingOverview.html)

### 1. 🌟 Bloom "Glow"

**What it does:** Creates bright light halos around intense sources, mimicking how our eyes perceive overwhelming brightness.
**Real-world comparison:** Staring at car headlights at night creates natural bloom in your vision.
**Game applications:**

- Magical spells in fantasy games
- Energy weapons in sci-fi
- Warm sunlight streaming through windows
- Glowing collectible items

> [!tip] Bloom Common Control Parameters
> 
> - **Threshold:** Only bright pixels above this value will bloom
> - **Intensity:** Controls bloom strength; subtle is usually better
> - **Scatter:** Controls bloom spread; higher values create wider halos

### 2. 🎯 Vignette

**What it does:** Darkens screen edges, naturally guiding attention to the center.
**Camera analogy:** Looking through binoculars or an old film camera viewfinder.
**Psychological impact:**
- Creates intimacy in dialogue scenes
- Builds tension in horror games
- Simulates tunnel vision during intense moments

> [!example] Vignette in Action 
> **Horror Games:** Heavy vignette = feeling trapped and focused 
> **Adventure Games:** Light vignette = natural, comfortable framing 
> **Action Games:** Dynamic vignette that pulses with health/stamina

### 3. 🎨 Color Grading 

**What it does:** Adjusts overall color balance, contrast, and mood - equivalent to a film's color timing or Photoshop's color correction.
**Film industry parallel:**
- The orange/teal look in blockbuster movies
- The desaturated palette of apocalyptic films
- Vibrant colors in animated films

**Game examples:**
- Warm colors for cozy indoor scenes
- Cool blues for underwater levels
- High contrast for dramatic moments

### 4. 📸 Depth of Field

**What it does:** Simulates camera lens behavior by blurring objects based on distance.
**Photography equivalent:** Portrait mode on smartphones, where the background blurs while the subject stays sharp.
**Game design applications:**
- Directing attention during cutscenes
- Creating depth perception in UI elements
- Enhancing cinematic storytelling moments

>[!warning] ### Plus Many More!
> There are many more post-processing effects available by default in Unity.
> Plus it is possible to creat your own via [[GMAP 395 - Module 2A - Shader Fundamentals|Shaders!]]

---

## 🎮 Connection to Game Feel and Player Experience

### Emotional Storytelling Through Effects 💭

Post-processing serves as a **visual language** that communicates mood without words:

- **Warm, high-contrast grading** = comfort and safety
- **Desaturated colors with heavy vignetting** = unease and danger
- **Bright bloom with vibrant colors** = magical and wonderful

> [!example] Case Study: Hollow Knight 🦋 Uses subtle bloom and careful color grading to distinguish between peaceful and dangerous areas, guiding players emotionally through the world without explicit instructions.

### Procedural and Modular Workflow Integration 🔧

Modern post-processing systems support **dynamic adaptation** - effects can respond to:
- Time of day changes
- Player health status
- Different game environments
- Combat vs exploration states

**Practical example:** A single post-processing profile can shift from bright and colorful during day exploration to dark and desaturated during night combat sequences.

---

## 🎯 Post-Processing in Different Game Genres

### 🏰 Fantasy/Adventure Games
- **Heavy bloom** on magical elements
- **Warm color grading** for friendly areas
- **Cool, desaturated** tones for dungeons

### 🤖 Sci-Fi Games
- **Neon-heavy color grading** for cyberpunk aesthetics
- **Sharp contrast** and vibrant colors
- **Chromatic aberration** for tech/glitch effects

### 😱 Horror Games
- **Heavy vignette** to create claustrophobia
- **Desaturated colors** to remove comfort
- **Subtle depth of field** to hide details

### 🏃 Platformers
- **Bright, vibrant colors** for energy
- **Light bloom** on collectibles
- **Smooth color transitions** between areas

---

## 🎨 Real-World Game Examples and Analysis

> [!example] AAA Case Study: 
> Cyberpunk 2077  Uses aggressive bloom and neon-heavy color grading to establish its night-city aesthetic. 
> The heavy post-processing isn't just decoration - it reinforces the game's themes of artificial enhancement and digital overwhelm.

> [!example] Indie Case Study: 
> Ori and the Blind Forest  Demonstrates how thoughtful bloom and color grading can create an enchanted forest atmosphere on a limited budget. 
> The post-processing effects do the heavy lifting for environmental storytelling.

**Art Direction Insight:** Both games use post-processing as a **core part of their visual identity**, not as an afterthought. The effects were planned during pre-production and inform level design and asset creation.

---

## 🧠 Spotting Good Post-Processing in Games

**Next time you play a game, try to notice:**
- What visual effects make bright objects glow?
- How does the screen edge treatment affect your focus?
- Do colors feel warm and inviting or cold and threatening?
- What happens to the visuals when your character takes damage?

> [!tip] Quick Exercise 
> 📝 Pick a game you know well and write down 3 post-processing effects you notice. 
> What purpose does each one serve? How do they make you **feel** while playing?

---

## 🛠️ Hands-On Learning Activities

### Activity: Mood Board Translation 

**Goal:** Bridge traditional art skills with technical implementation
**Instructions:**
1. Create mood boards for 3 imaginary games (horror, adventure, sci-fi)
2. Identify which post-processing effects would achieve those feelings
3. Explain your choices using the concepts from this module

---

> [!tip] Remember: 
> Post-processing effects aren't just "pretty filters" - they're **communication tools** that tell players what's happening and how they should feel in your game world!

---
---

> [!info] 🧭 Module Navigation 
> **Next:** [[GMAP 395 - Module 4B - Hands-On Unity Post-Processing Implementation|Module 4B]]  
> **Return to:** [[GMAP 395 - Module 4|Module Page]]