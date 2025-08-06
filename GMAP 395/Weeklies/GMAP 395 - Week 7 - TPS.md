# VFX Graph Scripting Activity

**Real-Time Parameter Control with C#**

## 🎯 What We're Doing Today

You'll learn how to control VFX Graph properties using C# scripts! This means making particle effects that respond to time, player input, and other dynamic changes.

**Activity Format:** Individual work → Partner up → Show the class  
**Time:** 50 minutes

### What You'll Learn
- How to connect C# scripts to visual effects
- Different ways to animate particle properties
- How real-time parameter changes affect visual outcomes
- Techniques for creating dynamic, responsive particle systems

---

## 📦 Getting Started

**What you need to set up:**

1. **Create a new Unity project** or use existing one
2. **Add VFX Graph package** (Window > Package Manager > search "Visual Effect Graph")
3. **Create "Simple Heads and Trails" VFX Graph** from the sample templates
4. **Add Blackboard properties** to your VFX Graph:
    - `SpawnRate` (Float) - Connect to Spawn Rate AND/OR Trigger Event Rate in your graph
    - `ParticleSize` (Float) - Connect to Set Size node
    - `EmissionColor` (Color) - Connect to Set Color node
    - `VelocityStrength` (Float) - Connect to Add Velocity node
5. **Place VFX Graph in your scene** and add the script to the same GameObject

---

## 🔍 THINK Phase (15 minutes)

**Work Individually (Together)**: Meaning in your groups each person does the following in this section.

Pick a **Control Method Card** (Below⬇) that tells you which animation technique to use.

### Your Task:

1. **Set up your VFX Graph** with Simple Sparks and Trails
2. **Add the required Blackboard properties** (SpawnRate, ParticleSize, etc.)
3. **Connect properties to appropriate nodes** in your graph
4. **Copy the script template** for your assigned method and attach to VFX GameObject
5. **Uncomment ONE property line** to see it animate
6. **Adjust the inspector values** to make it look "interesting"
7. **Try different properties** by commenting/uncommenting different lines
8. **Take screenshots** of your best results

---

## 👥 PAIR Phase (20 minutes)

**In your pairs**

### Work Together To:

1. **Share what you discovered** - Which properties looked best?
2. **Try each other's settings** - Compare different parameter values
3. **Experiment with extremes** - What happens with really high/low values?
4. **Solve problems together** - Help debug any issues
5. **Pick your best version** - Choose one to show the class

### Questions to Discuss:

- Which property made the most dramatic change?
- What parameter values created the coolest effects?
- How does your control method "feel" different from others?

---

## 🗣️ SHARE Phase (15 minutes)

**Show Your Results**

Each pair, demonstrate:

1. **Explain your control method** (sine wave, mouse input, etc.)
2. **Share your favorite parameter combination**
3. **Mention one thing that surprised you**
4. **Show your effect running** (via screenshots in your doc)

---

## 📝 Quick Reflection (5 minutes)

Write down:

- Which control method seemed most fun/interesting to use?
- What parameter change created the biggest effect?
- One technique from another control group you want to try
- Biggest challenge you figured out

---

## 🔄 Document and Turn In

>[!warning] All group members names must be on the turned in materials to receive credit! 

>[!Summary] Submission
>Submission of your groups materials, finding, and reflections should be submitted on BB Learn by END OF CLASS
>This can be simple, in the form of a word doc, pdf, or slides.

---

## 🎴 Control Method Cards

PICK ONE of these cards for your group:

> [!Note] **Group 1: Sine Wave Animation** 
> **Your Method:** Use mathematical sine waves to create smooth, rhythmic animations 
> **Focus Properties:** SpawnRate, ParticleSize 
> **Goal:** Create pulsing, breathing effects that feel organic and smooth

> [!example] **Group 2: Mouse Input Control** 
> **Your Method:** Use mouse position and movement to drive particle behavior 
> **Focus Properties:** EmissionColor, VelocityStrength 
> **Goal:** Create interactive effects that respond to user input in real-time

> [!warning] **Group 3: Smooth Transitions (DOTween)** 
> **Your Method:** Use DOTween library to create polished, eased animations 
> **Focus Properties:** SpawnRate, ParticleSize 
> **Goal:** Create professional-feeling transitions with smooth curves and loops

> [!error] **Group 4: Random Bursts** 
> **Your Method:** Use random values and timers to create unpredictable effects 
> **Focus Properties:** All properties with random variations 
> **Goal:** Create organic, natural-feeling bursts and variations


## 🛠️ Script Templates
### Group 1: Sine Wave Animation

```csharp
using UnityEngine;
using UnityEngine.VFX;

public class VFXController : MonoBehaviour
{
    private VisualEffect vfx;
    [SerializeField] private float frequency = 1f;
    [SerializeField] private float amplitude = 0.5f;
    [SerializeField] private float baseValue = 50f;
    
    void Start()
    {
        vfx = GetComponent<VisualEffect>();
    }
    
    void Update()
    {
        // Ready-made sine wave method - choose your property!
        float sineValue = Mathf.Sin(Time.time * frequency);
        float animatedValue = baseValue + (sineValue * amplitude * baseValue);
        
        // TODO: Pick ONE property to animate (uncomment one line):
        // vfx.SetFloat("SpawnRate", animatedValue);
        // vfx.SetFloat("ParticleSize", Mathf.Max(0.1f, animatedValue * 0.01f));
    }
}
```

### Group 2: Mouse Input Control

```csharp
using UnityEngine;
using UnityEngine.VFX;

public class VFXController : MonoBehaviour
{
    private VisualEffect vfx;
    [SerializeField] private float maxValue = 10f;
    
    void Start()
    {
        vfx = GetComponent<VisualEffect>();
    }
    
    void Update()
    {
        // Ready-made mouse input method - choose your property!
        Vector3 mousePos = Input.mousePosition;
        float normalizedX = mousePos.x / Screen.width;
        float inputValue = normalizedX * maxValue;
        
        // TODO: Pick ONE property to control (uncomment one):
        // vfx.SetFloat("VelocityStrength", inputValue);
        // Color inputColor = new Color(normalizedX, 1f - normalizedX, 0.5f, 1f);
        // vfx.SetVector4("EmissionColor", inputColor);
    }
}
```

### Group 3: Smooth Transitions (DOTween)

```csharp
using UnityEngine;
using UnityEngine.VFX;
using DG.Tweening;

public class VFXController : MonoBehaviour
{
    private VisualEffect vfx;
    [SerializeField] private float duration = 3f;
    [SerializeField] private float minValue = 20f;
    [SerializeField] private float maxValue = 100f;
    
    void Start()
    {
        vfx = GetComponent<VisualEffect>();
        StartTweenAnimation();
    }
    
    void StartTweenAnimation()
    {
        // Ready-made DOTween method - choose your property!
        DOVirtual.Float(minValue, maxValue, duration, (value) => {
            // TODO: Pick ONE property to animate (uncomment one):
            // vfx.SetFloat("SpawnRate", value);
            // vfx.SetFloat("ParticleSize", value * 0.01f);
        })
        .SetLoops(-1, LoopType.Yoyo)
        .SetEase(Ease.InOutSine);
    }
}
```

### Group 4: Random Bursts

```csharp
using UnityEngine;
using UnityEngine.VFX;

public class VFXController : MonoBehaviour
{
    private VisualEffect vfx;
    [SerializeField] private float interval = 2f;
    [SerializeField] private float baseValue = 50f;
    private float timer;
    
    void Start()
    {
        vfx = GetComponent<VisualEffect>();
        timer = interval;
    }
    
    void Update()
    {
        timer -= Time.deltaTime;
        
        if (timer <= 0f)
        {
            // Ready-made random burst method - choose your property!
            float randomValue = Random.Range(baseValue * 0.5f, baseValue * 2f);
            
            // TODO: Pick ONE property to randomize (uncomment one):
            // vfx.SetFloat("SpawnRate", randomValue);
            // Color randomColor = new Color(Random.value, Random.value, Random.value, 1f);
            // vfx.SetVector4("EmissionColor", randomColor);
            
            timer = interval;
        }
    }
}
```

---
---