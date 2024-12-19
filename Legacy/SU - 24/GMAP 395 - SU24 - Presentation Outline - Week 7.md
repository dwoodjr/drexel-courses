
# Game Lighting, Post-Processing, and Camera Effects in Unity

GMAP 395 – Advanced Game Design and Production

---

## Agenda

1. Introduction to Game Lighting
2. Lighting in Unity
3. Post-Processing Effects
4. Camera Effects
5. Final Project Requirements
6. Assignments Overview

---

## Introduction to Game Lighting

- Crucial for setting mood and atmosphere
- Enhances visual quality and realism
- Guides player attention and storytelling
- Impacts game performance

---

## Types of Lighting in Games

1. Direct Lighting
2. Indirect Lighting (Global Illumination)
3. Ambient Lighting
4. Emissive Lighting

---

## Direct vs Indirect Lighting

- Direct: Light that hits a surface directly from a source
- Indirect: Light that bounces off surfaces before reaching the final surface

![Direct vs Indirect Lighting Diagram]

---

## Global Illumination (GI)

- Simulates complex light interactions in a scene
- Enhances realism by calculating indirect lighting
- Can be real-time or pre-computed (baked)

---

## Lighting Strategies in Game Design

- Enhance immersion and create mood
- Provide direction and focus attention
- Communicate gameplay elements
- Support storytelling and world-building

---

## Lighting in Unity

Unity offers various tools and techniques for implementing lighting:

1. Light Types
2. Light Modes
3. Global Illumination
4. Light Probes
5. Reflection Probes

---

## Unity Light Types

1. Directional Light
2. Point Light
3. Spot Light
4. Area Light

[Visual examples of each light type]

---

## Unity Light Modes

1. Realtime: Calculated every frame
2. Mixed: Combination of realtime and baked lighting
3. Baked: Pre-calculated lighting stored in lightmaps

---

## Global Illumination in Unity

- Enlighten: Legacy GI system
- Progressive Lightmapper: Current baked GI solution
- Real-time GI: Dynamic, but performance-intensive

---

## Light Probes

- Capture lighting information for dynamic objects
- Provide efficient lighting for non-static objects
- Placed strategically in the scene

[Visual example of light probe placement]

---

## Reflection Probes

- Capture surroundings for realistic reflections
- Placed in areas where reflections are important
- Can be baked or real-time

[Visual example of reflection probe usage]

---

## Unity Lighting Window

- Access via Window > Rendering > Lighting Settings
- Control global lighting settings
- Manage baked lighting and GI settings
- Configure environment lighting

[Screenshot of Unity Lighting Window]

---

## Post-Processing in Unity

- Applies effects to the final rendered image
- Enhances visual quality and mood
- Simulates real-world camera effects
- Available through the Post-Processing package

---

## Common Post-Processing Effects

1. Bloom
2. Depth of Field
3. Color Grading
4. Ambient Occlusion
5. Motion Blur
6. Vignette

---

## Implementing Post-Processing in Unity

1. Install Post-Processing package
2. Add Post-Process Layer to the camera
3. Create Post-Process Volume
4. Configure Post-Process Profile
5. Adjust individual effect settings

---

## Post-Processing Volumes

- Define areas where effects are applied
- Can be global or local
- Blend between different profiles

[Visual example of volume blending]

---

## Camera Effects in Unity

- Enhance player experience and visual feedback
- Implemented through scripting or animation
- Common effects: shake, zoom, tilt, color adjustments

---

## Camera Shake Effect

```csharp
using UnityEngine;

public class CameraShake : MonoBehaviour
{
    public float duration = 0.5f;
    public float magnitude = 0.1f;

    public void Shake()
    {
        StartCoroutine(ShakeCoroutine());
    }

    private IEnumerator ShakeCoroutine()
    {
        Vector3 originalPosition = transform.localPosition;
        float elapsed = 0f;

        while (elapsed < duration)
        {
            float x = Random.Range(-1f, 1f) * magnitude;
            float y = Random.Range(-1f, 1f) * magnitude;

            transform.localPosition = new Vector3(x, y, originalPosition.z);
            elapsed += Time.deltaTime;
            yield return null;
        }

        transform.localPosition = originalPosition;
    }
}
```

---

## Camera Zoom Effect

```csharp
using UnityEngine;

public class CameraZoom : MonoBehaviour
{
    public float zoomSpeed = 1f;
    public float minZoom = 2f;
    public float maxZoom = 10f;

    private Camera cam;

    private void Start()
    {
        cam = GetComponent<Camera>();
    }

    private void Update()
    {
        float zoom = Input.GetAxis("Mouse ScrollWheel") * zoomSpeed;
        cam.fieldOfView = Mathf.Clamp(cam.fieldOfView - zoom, minZoom, maxZoom);
    }
}
```

---

## Optimizing Lighting and Post-Processing

- Use mixed lighting when possible
- Bake lighting for static scenes
- Limit the number of real-time lights
- Use light probes for dynamic objects
- Be mindful of post-processing effect costs
- Profile and optimize based on target platform

---

## Final Project Requirements: Lighting and Camera Effects

1. Implement at least 3 distinct lighting sources
2. Utilize 2 or more image effects or post-processing techniques
3. Demonstrate effective use of lighting for mood and visual enhancement
4. Show appropriate use of post-processing to improve overall aesthetic
5. Consider technical implementation and performance

---

## Tips for Meeting Final Project Requirements

- Experiment with different light types and setups
- Use color and intensity to create atmosphere
- Implement day/night cycles or dynamic lighting changes
- Combine multiple post-processing effects for unique looks
- Add camera effects to enhance player feedback and immersion

---

## Assignment 1: Lighting Tutorial

- Complete the Unity Learn: Creative Core – Lighting tutorial modules
- Modules to cover:
  - Get started with lighting in Unity
  - Configure the directional light and skybox
  - Add light sources to your scene
  - Configure shadows in your scene
- Optional: Baked lighting, light probes, and reflections

---

## Assignment 2: Implementing Lighting in Your Project

- Apply lighting techniques to your game project
- Focus on creating mood and emotional impact
- Use lighting to frame important areas/objects
- Implement basic post-processing effects
- Document your lighting design choices in your README

---

## Resources

- Unity Manual: Lighting
- Unity Learn: Lighting Tutorials
- Unity Post-Processing Stack Documentation
- Brackeys YouTube Channel: Lighting Tutorials
- GDC Talks on Game Lighting Techniques

---

## Questions?

Thank you for your attention!

Feel free to reach out if you have any questions about lighting, post-processing, or camera effects in Unity.

---