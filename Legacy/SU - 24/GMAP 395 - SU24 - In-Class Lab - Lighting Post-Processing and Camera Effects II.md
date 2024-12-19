# Lab: Dynamic Day-Night Cycle with Camera Shake and Reflections

## Objective
Create a small, open environment with a dynamic day-night cycle that affects gameplay and mood, incorporating advanced lighting, post-processing, and camera techniques.

## Prerequisites
- Unity 2022.3 LTS or later with URP
- Basic familiarity with C# scripting in Unity
## Part 1: Setting Up the Scene

1. Create a new URP 3D project in Unity.

2. OPTIONAL: Import a simple low-poly environment asset pack. Or simply use Unity primitives if you'd like. 
   > [!tip] Asset Selection
   > Choose an asset pack with a variety of elements like trees, rocks, and simple structures. The Unity Asset Store has several free options. 

4. Place objects from your asset pack around the scene to create a small diorama.

## Part 2: Implementing the Day-Night Cycle

1. Create a new empty GameObject and name it "DayNightController".

2. Add a new script to this object, also named "DayNightController".

3. Open the script and add the following code:

```csharp
using UnityEngine;

public class DayNightController : MonoBehaviour
{
    public Light sunLight;
    public float dayDuration = 60f; // One day every 60 seconds
    
    public float timeOfDay = 0.25f; // Start at 6:00 AM

    void Update()
    {
        timeOfDay += Time.deltaTime / dayDuration;
        if (timeOfDay >= 1f) timeOfDay -= 1f;

        float sunRotation = timeOfDay * 360f;
        sunLight.transform.rotation = Quaternion.Euler(sunRotation, 230f, 0);
    }
}
```

1. Create a Directional Light for the sun (*only if one does not already exist*) and assign it to the `sunLight` variable in the DayNightController component.

![[sunLight.png]]

> [!note] Sun Position
> The sun's starting rotation of (90, 230, 0) positions it in the east at the start of the day.

## Part 3: Dynamic Lighting + Colors

1. Modify the DayNightController script to change the sun's color based on the time of day:

```csharp
public class DayNightController : MonoBehaviour
{
    // ... previous code ...

    public Gradient sunColor;

    void Update()
    {
        // ... previous update code ...

        sunLight.color = sunColor.Evaluate(timeOfDay);
    }
}
```

1. In the Inspector, set up the color gradient for the sun:
   - Morning: Soft orange
   - Midday: Bright white
   - Evening: Deep orange
   - Night: Dark blue

![[sunColor.png]]

> [!tip] Color Selection
> Use warm colors for sunrise/sunset and cool colors for night to create a more realistic atmosphere.

3. Extend the DayNightController script to modify the sun's intensity:

```csharp
public class DayNightController : MonoBehaviour
{
    // ... previous code ...
    public AnimationCurve lightIntensityCurve;

    void Update()
    {
        // ... previous update code ...
        
        // Update sun intensity
        float intensityMultiplier = lightIntensityCurve.Evaluate(timeOfDay);
        sunLight.intensity = intensityMultiplier * 1.5f; // Base intensity of 1.5
    }
}
```

1. In the Inspector, set up the Light Intensity Curve:
   - Create an AnimationCurve with the following key points:
     - Time 0.0 (Midnight): Value 0.1
     - Time 0.25 (Sunrise): Value 0.8
     - Time 0.5 (Noon): Value 1.0
     - Time 0.75 (Sunset): Value 0.8
     - Time 1.0 (Midnight): Value 0.1

![[sunIntensity.png]]

> [!note] Light Intensity
> The intensity curve allows for smooth transitions between day and night, with peak brightness at noon and minimum at midnight.

5. Adjust the base intensity (1.5f in the example) to fit your scene's lighting needs.

> [!tip] Fine-tuning
> Experiment with different intensity values and curve shapes to achieve the desired lighting effect for your specific environment.

## Part 4: Implementing Dynamic Post-Processing

1. Create a Global Volume in your scene (*if one does not already exist*) `GameObject > Volume > Global Volume`.
2. Create a new Volume Profile for this Global Volume.
3. Add the following effects to the Volume Profile:
   - Bloom
   - Color Adjustments
   - Vignette
4. Create a new script called "PostProcessingController" and attach it to the Global Volume.
5. Implement the script to adjust post-processing based on time of day:

```csharp
using UnityEngine;  
using UnityEngine.Rendering;  
using UnityEngine.Rendering.Universal;  
  
public class PostProcessingController : MonoBehaviour  
{  
    public DayNightController dayNightController;  
    private Volume volume;  
  
    private Bloom bloom;  
    private ColorAdjustments colorAdjustments;  
    private Vignette vignette;  
  
    void Start()  
    {        volume = GetComponent<Volume>();  
        volume.profile.TryGet(out bloom);  
        volume.profile.TryGet(out colorAdjustments);  
        volume.profile.TryGet(out vignette);  
    }  
    void Update()  
    {        float timeOfDay = dayNightController.timeOfDay;  
  
        // Adjust bloom intensity  
        if (bloom != null)  
            bloom.intensity.value = Mathf.Lerp(0.2f, 1f, Mathf.PingPong(timeOfDay * 2, 1));  
  
        // Adjust color filter and other color adjustments  
        if (colorAdjustments != null)  
        {            colorAdjustments.colorFilter.value = dayNightController.sunColor.Evaluate(timeOfDay);  
            colorAdjustments.saturation.value = Mathf.Lerp(-20f, 20f, Mathf.PingPong(timeOfDay * 2, 1));  
            colorAdjustments.postExposure.value = Mathf.Lerp(-1f, 1f, Mathf.PingPong(timeOfDay * 2, 1));  
            colorAdjustments.contrast.value = Mathf.Lerp(0f, 20f, Mathf.PingPong(timeOfDay * 2, 1));  
        }  
        // Adjust vignette intensity  
        if (vignette != null)  
            vignette.intensity.value = Mathf.Lerp(0.2f, 0.4f, 1 - Mathf.PingPong(timeOfDay * 2, 1));  
    }}
```

6. Ensure that the `DayNightController` script has public `timeOfDay` and `sunColor` variables:

```csharp
public class DayNightController : MonoBehaviour
{
    public float timeOfDay = 0.25f; // Start at 6:00 AM
    public Gradient sunColor;

    // ... rest of the DayNightController code ...
}
```

1. Assign the `DayNightController` to its corresponding spot on the `PostProcessingController` script in the Inspector window.

![[ppController.png]]

> [!note] Post-Processing Effects
> These settings create a dynamic atmosphere that changes throughout the day-night cycle. The color filter adapts to the sun's color, while saturation, exposure, and contrast adjust to enhance the mood at different times of day.

> [!tip] Fine-tuning
> Experiment with the ranges/values for each effect to achieve the desired look for your specific scene. You may need to adjust these values based on your lighting setup and artistic vision.

## Part 5: Implementing Cinemachine for Dynamic Camera

1. Install Cinemachine via the Package Manager. If you are use the bellow Starter Asset, it will import automatically.

1. Install the `Starter Assets - ThirdPerson | Updates in new CharacterController package`:
   - This must be obtained from the [Asset Store](https://assetstore.unity.com/packages/essentials/starter-assets-thirdperson-updates-in-new-charactercontroller-pa-196526)
   - Add a character controller prefab to your scene. These can be found under `StarterAssets > ThirdPersonController > Prefabs` one of the `NestedParent_XXX` prefabs.

> [!NOTE]
> The free Unity `Starter Assets - ThirdPerson | Updated` is more than enough for this tutorial and can be downloaded for free from the Asset Store: https://assetstore.unity.com/packages/essentials/starter-assets-thirdperson-updates-in-new-charactercontroller-pa-196526

> [!attention] 
> Depending on the environment assets you choose to use. You may need to ensure that the colliders are set properly and have appropriate dimensions for the character controller to be able to traverse the scene.

1. Set up Cinemachine:
   - Create a Cinemachine Virtual Camera
   - A Cinemachine Brain will be added on the Main Camera
   - Set up the Virtual Camera to follow and look at the player

> [!NOTE]
> The aforementioned `Unity Starter Assets - ThirdPerson` already has the Cinemachine system setup for character follow. No need to change anything unless desired.

1. Implement a basic camera shake effect:
   1. Create a `CameraShake.cs` script and replace the code with the following:

```csharp
using UnityEngine;  
using Cinemachine;  
using DG.Tweening;  
  
public class CameraShake : MonoBehaviour  
{  
    public CinemachineVirtualCamera virtualCamera;  
    private CinemachineImpulseSource impulseSource;  
    private CinemachineTransposer transposer;  
    private Vector3 originalFollowOffset;  
  
    void Start()  
    {        //Check if there is a virtual camera  
        if (virtualCamera == null)  
        {            Debug.LogError("CameraShake: Virtual Camera is not assigned!");  
            return;  
        }  
        // Get the CinemachineTransposer component  
        transposer = virtualCamera.GetCinemachineComponent<CinemachineTransposer>();  
        if (transposer != null)  
        {            originalFollowOffset = transposer.m_FollowOffset;  
        }        else  
        {  
            Debug.LogWarning("CameraShake: CinemachineTransposer not found on the virtual camera.");  
        }  
        // Add CinemachineImpulseSource if it doesn't exist  
        impulseSource = GetComponent<CinemachineImpulseSource>();  
        if (impulseSource == null)  
        {            impulseSource = gameObject.AddComponent<CinemachineImpulseSource>();  
            Debug.Log("CameraShake: Added CinemachineImpulseSource component");  
        }  
        // Configure the impulse source for the shake effect  
        impulseSource.m_ImpulseDefinition.m_ImpulseType = CinemachineImpulseDefinition.ImpulseTypes.Uniform;  
        impulseSource.m_ImpulseDefinition.m_ImpulseDuration = 0.5f; // Adjust as needed  
  
	            //There are two ways to assign the Impulse Source Shape: 1. via built-in shapes or 2. custom animation curve.            //Comment out the one you do not wish to use.            // 1.Built-in        //impulseSource.m_ImpulseDefinition.m_ImpulseShape = CinemachineImpulseDefinition.ImpulseShapes.Explosion;            //2. Custom Animation Curve
	impulseSource.m_ImpulseDefinition.m_CustomImpulseShape = CreateSawShakeShape();  
  
        impulseSource.m_ImpulseDefinition.m_DissipationRate = 0.25f; // Adjust for faster or slower falloff  
  
        Debug.Log("CameraShake: Initialization complete with saw-like shake configuration");  
    }  
    private AnimationCurve CreateSawShakeShape()  
    {        AnimationCurve curve = new AnimationCurve();  
  
        // Create a saw-like pattern  
        for (int i = 0; i < 10; i++)  
        {            float time = i / 10f;  
            float value = (i % 2 == 0) ? 1f : -1f;  
            curve.AddKey(new Keyframe(time, value, float.PositiveInfinity, float.PositiveInfinity));  
        }  
        // Ensure it ends at 0  
        curve.AddKey(new Keyframe(1f, 0f, float.NegativeInfinity, 0f));  
  
        return curve;  
    }  
    public void Shake(float intensity)  
    {        Debug.Log($"CameraShake: Saw-like shake called with intensity {intensity}");  
  
        // Generate impulse  
        Vector3 shakeVector = Random.insideUnitSphere;  
        impulseSource.GenerateImpulse(shakeVector * intensity);  
  
        // Schedule a reset after the impulse duration  
        float resetDelay = impulseSource.m_ImpulseDefinition.m_ImpulseDuration;  
        DOVirtual.DelayedCall(resetDelay, () =>  
        {  
            ResetCameraPosition();  
            Debug.Log("CameraShake: Saw-like shake completed and camera reset");  
        });    }  
    private void ResetCameraPosition()  
    {        if (transposer != null)  
        {            transposer.m_FollowOffset = originalFollowOffset;  
        }    }  
    private void OnDisable()  
    {        ResetCameraPosition();  
    }}
```

2. Attach the new Camera Shake script component to the character controller's `PlayerFollowCamera` or your character's Main Camera.

3. Assign the Virtual Camera to the corresponding spot on the component.
   ![[cameraShake.png]]

4. Ensure that your CinemachineVirtualCamera has a CinemachineImpulseListener component. If it doesn't, add one `Add Component > Cinemachine > Cinemachine Impulse Listener`.

> [!note] Customization
> You can adjust the shake behavior by modifying the `ConfigureImpulseSource()` method. The `m_ImpulseDuration` controls the length of the shake, and `m_DissipationRate` affects how quickly the shake effect fades out.

5. Create a new script called `ShakeTrigger.cs` and add the following code:

```csharp
using UnityEngine;
using System.Collections;

public class ShakeTrigger : MonoBehaviour
{
    public CameraShake cameraShake;
    public float shakeDelay = 1f;
    public float shakeIntensity = 0.5f;

    void Start()
    {
        if (cameraShake == null)
        {
            Debug.LogError("ShakeTrigger: CameraShake component is not assigned!");
        }
    }

    void Update()
    {
        if (Input.GetKeyDown(KeyCode.Space))
        {
            Debug.Log("ShakeTrigger: Space key pressed, starting delayed shake");
            StartCoroutine(DelayedShake());
        }
    }

    private IEnumerator DelayedShake()
    {
        Debug.Log($"ShakeTrigger: Waiting for {shakeDelay} seconds before shaking");
        yield return new WaitForSeconds(shakeDelay);

        if (cameraShake != null)
        {
            Debug.Log($"ShakeTrigger: Calling Shake with intensity {shakeIntensity}");
            cameraShake.Shake(shakeIntensity);
        }
        else
        {
            Debug.LogError("ShakeTrigger: Cannot shake, CameraShake component is null");
        }
    }
}
```

6. Attach the ShakeTrigger script to an empty GameObject in your scene or to your player character.

7. In the Inspector, assign the CameraShake component to the `cameraShake` field of the ShakeTrigger script.

8. Adjust the `shakeDelay` and `shakeIntensity` values in the Inspector as needed.

> [!tip] Camera Shake Usage
> With this setup, pressing the Space key will trigger the camera shake after the specified delay. You can modify the `Update` method in the ShakeTrigger script to trigger the shake based on different game events or player actions.

## Part 6: Implementing Camera Stacking

1. Create a new camera for a UI overlay:
   - Create a new Camera object in the hierarchy
   - Set its `Render Mode` to Overlay
   - Set only the `Clear Depth` check
   - Set its Culling Mask to include only the UI layer
   - Set the position of the UI Camera similar to the Main Camera.
      - The simplest way to do this is to make it a child of the Main Camera and zero the Transform for Position and Rotation.

![[uiCam1.png]]

![[uiCam2.png]]

2. Create a time of day indicator using the day/night gradient:
   - `Right-click in Hierarchy > UI > Image`
   - Rename it to "TimeOfDayIndicator"
   - Ensure it's on the UI layer
   - In the Inspector, set the Image component's Source Image to "None" or to a white color icon.
   - Add a new script to this GameObject called "TimeOfDayDisplay"

3. Implement the TimeOfDayDisplay script:

```csharp
using UnityEngine;
using UnityEngine.UI;

public class TimeOfDayDisplay : MonoBehaviour
{
    public DayNightController dayNightController;
    public Image timeIndicatorImage;

    void Start()
    {
        if (timeIndicatorImage == null)
            timeIndicatorImage = GetComponent<Image>();
    }

    void Update()
    {
        if (dayNightController != null && timeIndicatorImage != null)
        {
            float timeOfDay = dayNightController.timeOfDay;
            timeIndicatorImage.color = dayNightController.sunColor.Evaluate(timeOfDay);
        }
    }
}
```

4. Configure the TimeOfDayDisplay in the Inspector:
   - Drag your DayNightController into the corresponding field
   - Ensure the Time Indicator Image field is set to the Image component of the TimeOfDayIndicator GameObject

1. Adjust the UI layout:
   - Position the TimeOfDayIndicator where you want it on the screen
   - Change the Canvas `Render Mode` to Screen Space - Camera and assign the UI Camera as the `Render Camera`

> [!tip] Visual Enhancement
> You can add additional UI elements, such as a sun icon or clock face, to make the time of day indicator more informative and visually appealing. There are several free UI Icon Packs on the Asset Store. Just be sure to choose a White colored icon.

1. (Optional) Add text to display the time:
   - Add a TextMeshPro Text component as a child of the TimeOfDayIndicator
   - Modify the TimeOfDayDisplay script to update the text:
      - Be sure to assign the TMPro text object in the Inspector window
![[uiText.png]]

```csharp
using TMPro;

public class TimeOfDayDisplay : MonoBehaviour
{
    // ... previous code ...
	public TextMeshProUGUI timeText;

    void Update()
    {
        if (dayNightController != null && timeIndicatorImage != null)
        {
            float timeOfDay = dayNightController.timeOfDay;
            timeIndicatorImage.color = dayNightController.sunColor.Evaluate(timeOfDay);

            if (timeText != null)
            {
                int hours = Mathf.FloorToInt(timeOfDay * 24);
                int minutes = Mathf.FloorToInt((timeOfDay * 24 - hours) * 60);
                timeText.text = string.Format("{0:00}:{1:00}", hours, minutes);
            }
        }
    }
}
```

1. Modify your main camera's CameraStack:
   - Select your main camera in the hierarchy (under the Player Controller)
   - In the Inspector, find the `Stack` section of the camera component
   - Click `+` to add your UI Camera to this spot

> [!tip] Camera Stacking
> Camera stacking allows you to render separate elements (like UI) separately from your main game view, providing more control over how different elements are displayed.

## Part 7: Implementing Reflection Probes

1. Add a Sphere your scene and ensure it is set to Static
2. Create a highly reflective material for the sphere. Something with full Metallic Map and Smoothness should work.
![[metalMaterial.png]]

1. Add a reflection probe to your scene:
   - `Right-click > Light > Reflection Probe`
   - Generally, place probes in key areas of your environment (e.g., near water bodies, in the center of clearings) where accurate reflections are needed. 
      - Place this probe around the sphere with the reflective material.

2. Configure the Reflection Probe:
   - Set the `Type` to Realtime
   - Set `Refresh Mode` to Every Frame
   - Adjust the `Box Size` to cover the desired area

> [!note] Real-time Reflection Probes
> Setting the Reflection Probe to update every frame ensures that it will always reflect the current state of your scene, including changes in lighting from the day/night cycle. However, be aware that this can be performance-intensive, especially for larger or more complex scenes.

3. (Optional) For performance optimization, you can adjust the Time Slicing setting:
   - Set `Time Slicing` to All Faces At Once for immediate updates (more performance-intensive)
   - Or choose "Individual Faces" to spread the update over multiple frames (better performance, slight delay in reflections)

> [!tip] Performance Considerations
> If you notice performance issues, consider reducing the update frequency or using a mix of real-time and baked probes in your scene. You can also adjust the resolution of the probe to balance between quality and performance.

> [!note] Reflection Probes
> Reflection probes will now update as the day-night cycle progresses, providing dynamic reflections that match the changing lighting conditions.
## Conclusion

Test your scene by entering play mode and observing how the lighting, post-processing, and camera effects change over the course of the day-night cycle.