# Advanced Lighting, Post-Processing, and Camera Techniques for Games

8 – Exploring Dynamics with Lighting, Post-Processing, Cameras, and Full-Screen Effects

---

## Agenda

1. Dynamic Post-Processing Control
2. Camera Stacking in URP
3. Full-Screen Effects with Shader Graph
4. Volumetric Lighting
5. Dynamic Lighting Techniques
6. Advanced Cinemachine Usage
7. Reflection Probes and Real-time GI

---

## Review: Lighting Basics in Unity

- Types of lights: Directional, Point, Spot, Area
- Light modes: Realtime, Mixed, Baked
- Global Illumination: Enhancing realism through indirect lighting

---

## Review: Light Probes and Reflection Probes

- Light Probes: Capture lighting information for dynamic objects
- Reflection Probes: Create realistic reflections in your scene
- Proper placement is key for both probe types

---

## Review: Post-Processing in URP

- Global Volume: Apply effects to the entire scene
- Post-processing effects: Bloom, Color Grading, Depth of Field, etc.
- Volume Profiles: Manage and blend between different effect settings

---

## Review: Lighting Window

- Scene: General lighting settings
- Environment: Skybox, ambient, and fog settings
- Realtime Lightmaps: Settings for real-time GI
- Baked Lightmaps: Parameters for baked lighting

---

## Review: Emissive Materials

- Creating glowing objects without light sources
- Contribution to Global Illumination (static objects only)
- Performance considerations in real-time vs. baked lighting

---

## Review: Cinemachine Basics

- Virtual Cameras: Easy setup for complex camera behaviors
- Cinemachine Brain: Manages transitions between virtual cameras
- Basic components: Body, Aim, Noise, Composition

---
## Dynamic Post-Processing Control

- Scripting post-processing effects for real-time changes
- Enhancing gameplay through dynamic visual effects
- Performance considerations

---

## Post-Processing Volume Component

```csharp
using UnityEngine;
using UnityEngine.Rendering;
using UnityEngine.Rendering.Universal;

public class BloomController : MonoBehaviour
{
    public Volume postProcessingVolume;
    private Bloom bloom;

    void Start()
    {
        postProcessingVolume.profile.TryGet(out bloom);
    }

    void Update()
    {
        if (bloom != null)
        {
            bloom.intensity.value = Mathf.Sin(Time.time) * 2f + 2f;
        }
    }
}
```

---

## Dynamic Vignette Example

```csharp
using UnityEngine;
using UnityEngine.Rendering;
using UnityEngine.Rendering.Universal;

public class VignetteController : MonoBehaviour
{
    public Volume postProcessingVolume;
    private Vignette vignette;

    void Start()
    {
        postProcessingVolume.profile.TryGet(out vignette);
    }

    public void SetVignetteIntensity(float intensity)
    {
        if (vignette != null)
        {
            vignette.intensity.value = intensity;
        }
    }
}
```

---

## Camera Stacking in URP

- Rendering multiple cameras to a single output
- Creating layered visual effects
- Use cases: UI overlays, split-screen, picture-in-picture

---

## Camera Stack Setup

1. Create multiple cameras in your scene
2. Set their Render Type:
   - Base: Main game view
   - Overlay: Additional layers (UI, effects)
3. Order cameras in the stack (lower = rendered first)

---

## Camera Stack Example

```csharp
using UnityEngine;
using UnityEngine.Rendering.Universal;

public class CameraStackController : MonoBehaviour
{
    public Camera baseCamera;
    public Camera overlayCamera;

    void Start()
    {
        var cameraData = baseCamera.GetUniversalAdditionalCameraData();
        cameraData.cameraStack.Add(overlayCamera);
    }
}
```

---

## Full-Screen Effects and Custom Render Passes in URP

- More complex than built-in post-processing effects
- Requires creation of custom render passes and renderer features
- Involves working with URP's rendering pipeline

---

## Custom Render Pass Workflow

1. Create a custom render pass script
2. Implement a custom renderer feature
3. Add the custom renderer feature to URP asset
4. Configure the render pass in your scene

---

## Example: Custom Render Pass Structure


``` c#
public class CustomRenderPass : ScriptableRenderPass
{
    public override void Execute(ScriptableRenderContext context, ref RenderingData renderingData)
    {
        // Implement your custom rendering logic here
    }
}

public class CustomRendererFeature : ScriptableRendererFeature
{
    CustomRenderPass customRenderPass;

    public override void Create()
    {
        customRenderPass = new CustomRenderPass();
    }

    public override void AddRenderPasses(ScriptableRenderer renderer, ref RenderingData renderingData)
    {
        renderer.EnqueuePass(customRenderPass);
    }
}
```

---

## Considerations for Custom Render Passes

- Performance impact on rendering pipeline
- Compatibility with different platforms
- Integration with existing URP features

---

## Custom Post-Processing Effects

- Extend URP's capabilities beyond built-in effects
- Create unique visual styles for your game
- Implement complex image processing techniques

---

## Implementing Custom Post-Processing

1. Create a custom shader for your effect
2. Implement a ScriptableRendererFeature
3. Set up a ScriptableRenderPass
4. Sample the camera color texture
5. Apply your custom shader
6. Output the result to the camera target

---

## Example: Custom Edge Detection Effect

csharp

Copy

``` c#
public class EdgeDetectionPass : ScriptableRenderPass
{
    private Material edgeDetectionMaterial;
    private RenderTargetIdentifier source;
    private RenderTargetHandle tempTexture;

    public EdgeDetectionPass(Material material)
    {
        edgeDetectionMaterial = material;
        renderPassEvent = RenderPassEvent.BeforeRenderingPostProcessing;
        tempTexture.Init("_TempTexture");
    }

    public override void Execute(ScriptableRenderContext context, ref RenderingData renderingData)
    {
        CommandBuffer cmd = CommandBufferPool.Get("Edge Detection Pass");

        RenderTextureDescriptor descriptor = renderingData.cameraData.cameraTargetDescriptor;
        cmd.GetTemporaryRT(tempTexture.id, descriptor);

        Blit(cmd, source, tempTexture.Identifier(), edgeDetectionMaterial);
        Blit(cmd, tempTexture.Identifier(), source);

        context.ExecuteCommandBuffer(cmd);
        CommandBufferPool.Release(cmd);
    }
}
```

---

## Challenges in Custom Post-Processing

- Performance optimization
- Compatibility across different hardware
- Integrating with existing post-processing stack

---

## Full-Screen Effects with Shader Graph

- Create custom shaders for full-screen effects
- Useful for complex visual effects like distortions or overlays
- Can be integrated into custom render passes

---

## Creating a Full-Screen Effect in Shader Graph

1. Create a new Shader Graph (Unlit Graph)
2. Set Surface Type to "Transparent"
3. Set Blend Mode to "Additive" or "Alpha"
4. Use Screen Position node for UV coordinates
5. Sample the scene color using a Texture2D node
6. Apply your custom effect logic
7. Output to Fragment color

---

## Integrating Shader Graph with Custom Render Pass

- Create a material using your Shader Graph shader
- Use this material in your custom render pass
- Apply the effect to the entire screen or a specific render target

---

## Performance Considerations for Full-Screen Effects

- Screen-space effects can be expensive
- Consider using lower resolution render targets
- Optimize shader complexity for mobile platforms
- Use GPU profiling tools to identify bottlenecks

---

## Dynamic Lighting Techniques

- Real-time light intensity and color changes
- Animating light properties
- Creating atmospheric effects with dynamic lighting

---

## Scripted Light Controller

```csharp
using UnityEngine;

public class DynamicLightController : MonoBehaviour
{
    public Light targetLight;
    public float intensityChangeSpeed = 1f;
    public float colorChangeSpeed = 0.5f;

    void Update()
    {
        // Pulsating intensity
        float intensity = Mathf.PingPong(Time.time * intensityChangeSpeed, 1f);
        targetLight.intensity = intensity;

        // Changing color
        float hue = Mathf.PingPong(Time.time * colorChangeSpeed, 1f);
        targetLight.color = Color.HSVToRGB(hue, 1f, 1f);
    }
}
```

---

## Advanced Cinemachine Usage

- Complex camera behaviors with Cinemachine
- Blending between multiple virtual cameras
- Creating dynamic, responsive game cameras

---

## Cinemachine State-Driven Camera

1. Create multiple CinemachineVirtualCamera objects
2. Add a CinemachineStateDrivenCamera
3. Set up an Animator Controller with camera states
4. Blend between cameras based on game states

---

## Camera Shake with Cinemachine Impulse

```csharp
using UnityEngine;
using Cinemachine;

public class CameraShakeController : MonoBehaviour
{
    public CinemachineImpulseSource impulseSource;

    public void TriggerShake(float intensity)
    {
        Vector3 shakeVector = Random.insideUnitSphere;
        impulseSource.GenerateImpulse(shakeVector * intensity);
    }
}
```

---

## Reflection Probes and Real-time GI

- Enhancing scene reflections with Reflection Probes
- Real-time Global Illumination techniques
- Balancing visual quality and performance

---

## Reflection Probe Placement

- Strategic placement for accurate reflections
- Using multiple probes for complex scenes
- Blending between probes for smooth transitions

---

## Real-time GI Setup in URP

1. Enable Real-time GI in Lighting settings
2. Mark static objects as "Contribute GI"
3. Set up Light Probes for dynamic objects
4. Configure Reflection Probes
5. Fine-tune GI settings for performance

---

## Optimizing Real-time GI

- Use mixed lighting where possible
- Limit the number of real-time lights
- Bake static lighting where appropriate
- Use Light Probes for dynamic objects

---

## Lab Preview/Demo

In the upcoming lab, we'll explore:
- Scripting post-processing effects
- Creating a dynamic third-person camera
- Implementing camera shake
- Building a day/night cycle with dynamic lighting

---

