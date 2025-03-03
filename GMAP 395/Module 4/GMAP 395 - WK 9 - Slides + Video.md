
# GMAP 395

### Post-Processing, Full-Screen Shader Effects, and Cameras

---


### Course Context
- We've already covered Lighting in depth.
- This presentation focuses on:
    - Post-processing
    - Full-screen shader effects
    - Camera behaviors and interactions

---


### Why Post-Processing and Cameras?
- Enhance atmosphere and mood
- Refine visual storytelling
- Create player focus through lenses, effects, and transitions
- Optimize and stylize your scenes

---


### Quick Lighting Review
- Lighting sets mood and clarity
- Guides players and reinforces theme
- Direct interaction with post-processing and camera effects

---


### Lighting + Post-Processing
- Post-processing filters amplify lighting setups
    - Bloom enhances emissive
    - Color grading adjusts overall tone
    - Vignette focuses attention

---


### Lighting + Full-Screen Effects
- Combine dynamic lighting with shaders:
    - Day/Night Cycles
    - Color Shifts
    - Fog and Atmospherics

---


# Post-Processing Pipelines

---


### What is Post-Processing?
- Visual effects applied after rendering
- Runs over the full screen, like photo filters in real-time
- Handles mood, style, and polish

<iframe width="560" height="315" src="https://www.youtube.com/embed/7YzWexOAggc?si=br182WKdVD4wNJVa" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


---


### Common Post-Processing Effects
- Bloom
- Color Grading
- Vignette
- Depth of Field
- Motion Blur
- Chromatic Aberration

<iframe width="560" height="315" src="https://www.youtube.com/embed/xxM6AUHqTMA?si=4p9RotMSOMbHHxbT" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


---


### Setting Up Post-Processing in URP
1. Create a Global Volume
2. Assign a Post-Processing Profile
3. Add overrides (Bloom, Vignette, etc.)
4. Enable post-processing on the camera

---


### Post-Processing Example
- Bloom + Emissives = Glow
- Vignette = Cinematic framing
- Color Adjustments = Visual mood shifts

![[home-before.png|720]]
![[home-after.png|720]]


---

### Best Practices
- Subtlety > Overload
- Profile performance costs
- Stack effects logically (Color Grading → Bloom → Vignette)
---
### Post-Processing Control via Scripting
1. Implement correct "using statements"
2. Reference the `Volume` and the `Override` needed for control

```c#
using UnityEngine.Rendering;  
using UnityEngine.Rendering.Universal;  
  
public class VignetteController : MonoBehaviour  
{  
    public Volume postProcessVolume;  
    private Vignette vignette;
}
```

---


# Full-Screen Shader Effects

---


### What are Full-Screen Shaders?
- Shaders that modify the entire frame
- Applied through a render pass or post-process pipeline
- Example uses:
    - Pixelation
    - Screen distortion
    - Color filters

---


### Why Use Full-Screen Shaders?
- Custom artistic control
- Real-time dynamic adjustments
- Performance-efficient stylization

---

### Common Full-Screen Shader Techniques
- UV manipulation
- Noise overlays
- Color blending
- Depth-based effects

---


### Shader Control in Gameplay
- Use DOTween or C# to change shader parameters
- Example: Expand portal effect on enemy spawn
- Sync shader animations with player actions

---


### Procedural Texture Effects
- Swirls, ripples, and patterns
- Masking and blending
- Dynamic reactions to game state

---


# Camera Systems

---

### Why Do Cameras Matter?
- Player perspective = player experience
- Cinematic movement builds immersion
- Connects gameplay to visual storytelling

<iframe width="560" height="315" src="https://www.youtube.com/embed/bHdi5Ar8GXw?si=HTUH44NnrMa9lJGu" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

---


### Cinemachine in Unity
- Follow Cameras
- Dolly Tracks
- Target Groups
- Blend Transitions

![[capsule_616x353.jpg]]

---


### Dynamic Camera Effects
- Shake on impact
- Zoom on focus
- Rotate for drama
- Depth of Field on object proximity

![[421988f6-a827-428b-86d4-9b815f15cdce.jpg|720]]

---


### Cameras + Post-Processing
- Match camera behavior with post-process states
- Example:
    - Zoom → Increase Depth of Field
    - Rotate → Add Motion Blur

---


### Cameras + Full-Screen Effects
- Trigger shaders during camera moves
- Layer transitions and fade-ins
- Match action with visual flow

<iframe width="560" height="315" src="https://www.youtube.com/embed/dH3WRx5ZPVU?si=K-WSN5XXn7v90w-v" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

---
### Camera Stacking

Layer multiple cameras together, with cameras that focus on specific layers or objects in a scene.

<iframe width="560" height="315" src="https://www.youtube.com/embed/OmCjPctKkjw?si=ywGct9TsE-OPZGtS" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


---
# Bringing It Together

---


### Complete Scene Example
- Procedural asset with dynamic shader
- Lighting supports mood
- Post-processing adds polish
- Camera movements guide focus

---


### Reflection
- How can you combine these systems?
- Where can shaders and post-processing amplify your procedural assets?
- How does the camera’s perspective shape the player’s experience?

---
---
> [!info] [[GMAP 395 - Module 4| Return to the Module Page]]