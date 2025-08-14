# Module 4B: Hands-On Unity Post-processing Implementation

> [!info] Module Overview 
> **Learning Focus:** Practical Unity post-processing setup and scripting control 
> **Tools:** Unity URP, C# scripting, Volume system 
> **Builds On:** Post-processing concepts from [[GMAP 395 - Module 4A - Post-Processing Effects Basics in Unity]]

> [!summary] Submodule Video Overview
> <iframe src="https://1drv.ms/v/c/b08de2251f1b33a4/IQTtEOhJvAkbQ7FOT-JODkSEAag2SsRq0jEiXozwq7tIyZc?width=2560&height=1440" width="800" height="600" frameborder="0"></iframe>
> 
>[gmap395_md4b.mkv](https://1drv.ms/v/c/b08de2251f1b33a4/Ee0Q6Em8CRtDsU5P4k4ORIQBT6nTeL0RRNEC0TvMSPzGIQ?e=9HpL40)

---

## 🚀 Unity URP Setup and Current Best Practices
### Getting Started: Essential Setup ⚙️

**Step 1: Verify Your Render Pipeline**

1. Go to **Edit → Project Settings → Graphics**
2. Make sure **Scriptable Render Pipeline Settings** shows a URP asset
3. If not, create one: **Assets → Create → Rendering → URP Asset**

**Step 2: Enable Post-Processing on Camera**

1. Select your **Main Camera**
2. In the **Camera** component, find **Rendering** section
3. ✅ Check **"Post Processing"**

> [!error] Common Mistake! The #1 reason post-processing "doesn't work" is forgetting Step 2. Always verify post-processing is enabled on your camera first!

---

## 🛠️ Step-by-Step Implementation Guide

### Foundation Setup Process 📋

#### Step 1: Create Your Post-Processing Volume

1. **Right-click in Hierarchy**
2. **Volume → Global Volume**
3. **Name it:** "PostProcess_Global"

#### Step 2: Create Your Profile

1. **Select your Global Volume**
2. In the **Volume component**, click **"New"** next to Profile
3. **Save it** in your project (good organization!)

#### Step 3: Add Your First Effects

1. Click **"Add Override"**
2. **Post-processing → Bloom** (let's start with something fun!)
3. Click **"Add Override"** again
4. **Post-processing → Vignette**

### Your First Effect: Making Things Glow! ✨

Let's make a glowing object that actually glows:

1. **Create a Cube** in your scene
2. **Create a Material** for it
3. Set the material's **Emission** to a bright color (like cyan)
4. Set **Emission** intensity to **2 or higher**
5. **Apply the material** to your cube

Now configure Bloom:

1. **Select your Global Volume**
2. **Enable Bloom** by checking the box next to it
3. **Enable Threshold** and set it to **0.9**
4. **Enable Intensity** and set it to **1**

**Press Play** - your cube should now have a beautiful glow!

---

## 💻 Scripting Post-Processing: Your First Controller

### Basic Post-Processing Controller Script

```csharp
using UnityEngine;
using UnityEngine.Rendering;
using UnityEngine.Rendering.Universal;

// Simple controller that art students can understand and modify
public class PostProcessingController : MonoBehaviour
{
    [Header("Post-Processing Components")]
    [SerializeField] private Volume postProcessVolume;
    
    // These will appear in Inspector for easy tweaking
    [Header("Effect Intensity Controls")]
    [Range(0f, 2f)] public float bloomIntensity = 1f;
    [Range(0f, 1f)] public float vignetteIntensity = 0.3f;
    [Range(-100f, 100f)] public float colorSaturation = 0f;
    
    // Component references - cached for performance
    private Bloom bloom;
    private Vignette vignette;
    private ColorAdjustments colorAdjustments;
    
    void Start()
    {
        // Get references to post-processing components
        // TryGet is safer than direct access - won't crash if component missing
        if (postProcessVolume.profile.TryGet<Bloom>(out bloom))
        {
            Debug.Log("Bloom component ready");
        }
        
        if (postProcessVolume.profile.TryGet<Vignette>(out vignette))
        {
            Debug.Log("Vignette component ready");  
        }
        
        if (postProcessVolume.profile.TryGet<ColorAdjustments>(out colorAdjustments))
        {
            Debug.Log("Color Adjustments component ready");
        }
    }
    
    void Update()
    {
        // Allow real-time adjustment for experimentation
        if (bloom != null)
            bloom.intensity.Override(bloomIntensity);
            
        if (vignette != null)
            vignette.intensity.Override(vignetteIntensity);
            
        if (colorAdjustments != null)
            colorAdjustments.saturation.Override(colorSaturation);
    }
    
    // Public methods for game events
    public void TriggerHealthDamageEffect()
    {
        // Flash red screen and increase vignette when player takes damage
        StartCoroutine(HealthDamageVisualFeedback());
    }
    
    private System.Collections.IEnumerator HealthDamageVisualFeedback()
    {
        // Store original values
        float originalVignetteIntensity = vignetteIntensity;
        float originalSaturation = colorSaturation;
        
        // Apply damage effect
        vignetteIntensity = 0.8f;
        colorSaturation = -50f;
        
        // Hold effect for short duration
        yield return new WaitForSeconds(0.2f);
        
        // Gradually return to normal
        float timer = 0f;
        float duration = 1f;
        
        while (timer < duration)
        {
            timer += Time.deltaTime;
            float progress = timer / duration;
            
            vignetteIntensity = Mathf.Lerp(0.8f, originalVignetteIntensity, progress);
            colorSaturation = Mathf.Lerp(-50f, originalSaturation, progress);
            
            yield return null;
        }
    }
}
```

### How to Use This Script 📝

1. **Create an empty GameObject** and name it "PostProcessingController"
2. **Add the script** to this GameObject
3. **Drag your Global Volume** into the "Post Process Volume" slot
4. **Press Play** and adjust the sliders in the Inspector!


---

## 🎨 Common URP Effects and Implementation

### Bloom Configuration for Beginners 🌟

> [!example] Bloom Settings Explained
> 
> - **Threshold (0.9 recommended):** Only bright pixels above this value will bloom
> - **Intensity (0.5-1.5 range):** Controls bloom strength; subtle is usually better
> - **Scatter (0.7 default):** Controls bloom spread; higher values create wider halos
> - **Tint:** Slight warm tint (pale yellow) feels natural for most scenes

**Quick Setup:**

1. Add **Bloom** override to your Volume
2. **Threshold:** 0.9
3. **Intensity:** 1.0
4. **Scatter:** 0.7

### Vignette Best Practices 🎯

> [!tip] Vignette Modes
> 
> - **Classic Mode:** Simple, performance-friendly darkening
> - **Masked Mode:** Uses textures for creative shapes and effects

**Recommended Settings:**

- **Intensity Range:** 0.2-0.4 for subtle atmosphere, 0.5+ for dramatic effect
- **Smoothness:** Higher values create softer transitions
- **Color:** Usually black, but try dark blue for night scenes!

### Color Grading Essentials 🎨

> [!example] Color Grading Controls
> 
> - **Post-exposure:** Global brightness adjustment (±0.5 typical range)
> - **Contrast:** Enhances visual pop (±20 typical range)
> - **Hue Shift:** Creative color transformations (use sparingly)
> - **Saturation:** Boost for stylized looks, reduce for realistic feel

---


## 🏋️ Useful Exercises

### Exercise 1: Mood Lighting Lab 🧪

**Goal:** Understand how post-processing affects emotional response

**Instructions:**

1. **Create a simple scene** (a few basic objects)
2. **Create 3 mood presets:**
    - ☀️ **Cheerful Morning:** Bright, warm, high contrast
    - 🌅 **Dramatic Sunset:** Orange tint, medium bloom
    - 🌙 **Eerie Night:** Desaturated, heavy vignette
3. **Switch between them** and notice how the same scene feels completely different!

### Exercise 2: Health Feedback System ❤️

**Goal:** Connect game logic to visual systems

**Instructions:**

1. **Use the PostProcessingController script** from above
2. **Create a simple health system** with a slider UI
3. **Connect health changes** to the `TriggerHealthDamageEffect()` method
4. **Test taking damage** and watch the visual feedback!


---

## 🔧 Troubleshooting Common Issues

> [!warning] Problem: "My post-processing isn't working!" **Solution:** Check these in order:
> 
> 1. ✅ Is post-processing enabled on your camera?
> 2. ✅ Do you have a Global Volume in your scene?
> 3. ✅ Does your Volume have a Profile assigned?
> 4. ✅ Are your effects enabled (checkboxes checked)?

> [!tip] Performance Tip 
> Post-processing can be expensive! 
> For mobile/web builds, use effects sparingly and test on target devices.

> [!tip] Remember: The key to good post-processing is **subtlety**! Start with small values and build up gradually. Less is often more!

---
---

> [!info] 🧭 Module Navigation 
> **Previous:** [[GMAP 395 - Module 4A - Post-Processing Effects Basics in Unity|Module 4A]]  
> **Next:** [[GMAP 395 - Module 4C - Cinemachine and Camera Systems Fundamentals|Module 4C]]  
> **Return to:** [[GMAP 395 - Module 4|Module Page]]