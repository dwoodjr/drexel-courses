# Lab Exercise: Lighting, Post-Processing, and Dynamic Camera in Unity URP

## Objective
In this lab, you'll create a simple 3D scene using the Universal Render Pipeline (URP), apply basic lighting techniques and a dynamic day-night cycle that affects gameplay and mood. This scene will be incorporating you *Procedural Game Art* Asset from `Module 1 - Part 1`.

## Prerequisites
- Unity 2022.3 LTS or later
- Basic familiarity with the Unity interface
- Basic familiarity with C# scripting in Unity

## Video Tutorials

| Part 1                                                                                                                                                     | Part 2                                                                                                                                    | Part 3 |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| <iframe src="https://1drv.ms/v/s!AqQzGx8l4o2wk_FXBBGHCZ_2nr6Zqg?embed=1" width="320" height="320" frameborder="0" scrolling="no" allowfullscreen></iframe> | <iframe src="https://1drv.ms/v/s!AqQzGx8l4o2wk_FZNnHemy6Zo2OReA?embed=1" width="98" height="120" frameborder="0" scrolling="no"></iframe> |        |
| [gmap395_tut2_p1.mp4](https://1drv.ms/v/s!AqQzGx8l4o2wk_FXZ7EobnQCfylfDg?e=KvqpM3)                                                                         | [gmap395_tut2_pt2.mp4](https://1drv.ms/v/s!AqQzGx8l4o2wk_FZzrRRBJsoZsmerA?e=xmapGB)                                                       |        |


---
## Part 1: Setting Up the Scene + Importing Assets 

### Blender Geometry Setup and Export
We will need to do some very simple [Retopology](https://docs.blender.org/manual/en/latest/modeling/meshes/retopology.html) in blender with out geometry then apply some simple [UVs](https://docs.blender.org/manual/en/latest/modeling/meshes/uv/index.html) before we export and import into Unity.

#### Procedural Retopology and UV Unwrapping
> [!NOTE] Modularity and Reuse
> We will be doing the following operations to all of our procedural geometry. So just pick one object from Part 1 and and follow along (e.g. start with `tendrals_base_geo`).

For this portion of the tutorial watch and follow along with the video from *Entagma*, on doing the Retopology and UV Unwrapping procedurally using geometry nodes. You will apply this same process to all sections of the procedural game art from Part 1. 

> [!example] Blender Tutorial: Procedural UV Unwrapping with Geometry Nodes
> <iframe width="560" height="315" src="https://www.youtube.com/embed/02XNGOVpSV4?si=m6rZ6AbTA1Dph8kE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
> 
> https://www.youtube.com/watch?v=02XNGOVpSV4

> [!NOTE] Types of Retopology
> It is important to note that we are aiming for a quick version of retopology that is rapid for our prototyping in this course. IF you were going to work on retopology for animation, it would be best to do a more traditional method like Quad Remeshing with some manual retopology. Like in this video: https://www.youtube.com/watch?v=hQ8HvDuSWCQ


### Unity Scene Setup
1. Create a new URP 3D Unity project.
   - When creating a new project, select "3D (URP)" as the template.

2. In the Hierarchy window, right-click and select 3D Object > Plane to create a ground plane. ONLY IF NEEDED.


### Blender Geometry Import


> [!tip] Tip
> Use different materials for each object to make them visually distinct. Select each object, create a new material (right-click in Project window > Create > Material), and set a unique color in the Inspector. Make sure to use the "Universal Render Pipeline/Lit" shader for these materials.

---
## Part 2: Basic Lighting Setup

1. The default URP project comes with a Directional Light. Adjust its settings:
   - Set the Directional Light rotation to (50, -30, 0) and reduce its `Intensity` to 0.5.

2. Create two additional lights:
   - Create a Point Light (`GameObject > Light > Point Light`)
   - Create a Spot Light (`GameObject > Light > Spot Light`)

1. Configure the lights:
   - Position the Point Light at (0, 3, 0) and set its Range to 10. Set intensity to 5
   - Position the Spot Light at (-5, 5, -5), rotate it to (45, 45, 0), and set its Range to 15 and Spot Angle to 30. Set intensity to 35
   - Set all of the lights' `Mode` to `Mixed` in their Light component settings.
![[lightingMode.png]]

> [!note] Connection to Lecture
> Each Light type serves a specific purpose in lighting your scene. The Directional Light acts as your main light source (like the sun), while Point and Spot Lights add depth and focus to specific areas.

1. Experiment with light colors:
   - Set the Directional Light to a warm color (e.g., FFF4E0).
   - Set the Point Light to a cool blue color (e.g., ADD8E6).
   - Set the Spot Light to a subtle purple (e.g., 8A2BE2).
![[colorHexCode.png]]
> [!tip] Tip
> Use color theory to create mood and depth in your scene. Warm colors tend to advance (appear closer), while cool colors recede (appear farther away).

---
## Part 3: Implementing the Day-Night Cycle

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

## Part 4: Dynamic Lighting + Colors

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

---
## Part 5: Lighting Configuration and Baking

1. Open the `Lighting` window:
   - Go to `Window > Rendering > Lighting`

1. Familiarize yourself with the Lighting window:
   - Scene: Contains general lighting settings for the current scene
   - Environment: Controls skybox and ambient lighting and fog
   - Realtime Lightmaps: Shows real-time lightmaps
   - Baked Lightmaps: Shows baked lightmaps

> [!note] Connection to Lecture
> The Lighting window is your central hub for controlling global lighting settings and baking lightmaps.

![[lightingWindow.png]]

3. Create a Lighting Settings Asset:
   - In the Lighting window, click "New" next to "Lighting Settings Asset"
   - Save it as "MainLightingSettings" in your project's Settings folder

1. Configure Lighting Settings:
   - In the `Scene` section
      - Create a new Lighting Settings Asset
         - Name it "LightSettings_" + your scene name 
      - Turn on Realtime Global Illumination
         - Adjust Indirect Resolution to 2 Texels Per Unit
   - In the `Environment` section:
     - Set Skybox Material to "Default-Skybox"
     - Change `Sun Source` to your scene Directional Light
   - In the Mixed Lighting section:
     - Set Lighting Mode to "Baked Indirect"
   - In the Lightmapping Settings section:
     - Set Lightmapper to "Progressive GPU (Preview)"
     - Leave the default settings for now. You can adjust with these later.

1. Open the `Light Explorer`:
   - Go to Window > Rendering > Light Explorer
   - The Light Explorer has taps to access quick settings changes for Lights, 2D Lights, Reflection Probes, Light Probes, and Static Emissives.

6. Use the Light Explorer to quickly adjust multiple lights:
   - Review and adjust thing like the Mode, Intensity, and Range of your lights among other settings.

> [!tip] Tip
> The Light Explorer is excellent for getting an overview of all lights in your scene and making bulk adjustments.

![[lightExplorer.png]]

7. Prepare for lightmap baking:
   - Select all static objects in your scene (ground plane and any non-moving objects)
   - In the Inspector, check "Static" at the top
   - Expand the Static dropdown and ensure "Contribute Global Illumination (Contribute GI)" is checked

8. Generate lighting:
   - In the Lighting window, scroll to the bottom
   - Click "Generate Lighting"
   - Wait for the baking process to complete

> [!warning] Important
> Lightmap baking can take some time, especially for complex scenes. Be patient!

> [!warning] 
> It is not recommended to tick on `Auto Generate`. This is because lighting will constantly cook anytime a change is made. For very large scene with Mixed or Baked lighting, this can take hours and slows down the Unity Editor.

1. Review the results:
   - Once baking is complete, examine your scene in both the Scene and Game views
   - Look for any areas where the lighting seems off or could be improved

---
## Part 6: Creating and Using Emissive Materials

1. Create a new material:
   - In the Project window, `right-click > Create > Material`
   - Name it "EmissiveMaterial"

2. Configure the emissive material:
   - Select the EmissiveMaterial in the Project window
   - In the Inspector, ensure the Shader is set to "Universal Render Pipeline/Lit"
   - Scroll down to the `Emission` section
   - Check the "Emission" box to enable it
   - Click the color picker next to Emission to choose a color (e.g., a bright blue 00FFFF)
   - Set the Emission color `Intensity` to 2 (you can adjust this value to increase or decrease the glow intensity)

1. Apply the emissive material:
   - Drag the EmissiveMaterial onto the Sphere in your scene.
   - Place another primitive object close to the sphere with the emissive material applied.

> [!note] How Emissive Materials Work
> Emissive materials simulate light-emitting surfaces. They don't actually emit light that affects other objects in real-time, but they appear to glow and can contribute to the overall lighting of the scene when lighting is generated.

![[emissiveMat.png]]

4. Observe the difference in Realtime vs Baked lighting: For Realtime:
    
    - The emissive object will appear to glow.
    - If the object is marked as "Static" in the Inspector, it can contribute to real-time Global Illumination (GI).
    - Open the Light Explorer (Window > Rendering > Light Explorer) and ensure the emissive object has "Contribute Global Illumination" checked.
    - Non-static (dynamic) emissive objects will not affect GI but will still glow.
    
    For Baked:
    - Make sure the Sphere is marked as "Static" in the Inspector.
    - In the Lighting window, under Baked Lightmaps, ensure "Baked Global Illumination" is enabled.
    - Click "Generate Lighting" to bake the lighting.

> [!tip] Emissives and Global Illumination In both realtime and baked scenarios, static emissive materials can contribute to global illumination, subtly lighting nearby surfaces. This creates a more realistic and integrated lighting effect. However, moving (dynamic) emissive objects are not supported.

> [!warning] Performance Consideration Realtime GI from emissive materials can be performance-intensive. For mobile or performance-critical projects, consider using baked lighting or limiting the use of emissive materials that contribute to realtime GI.

5. Experiment with static vs dynamic emissive objects:
    - Create a copy of your emissive sphere and place it in the scene.
    - Keep one sphere marked as "Static" and the other unmarked.
    - Compare how they interact with the environment in both realtime and baked lighting scenarios.

2. Iterate and refine:
    - Adjust light settings, object materials, or lightmapping settings as needed
    - Regenerate lighting after making significant changes

> [!note] Connection to Lecture
> Baked lighting is crucial for performance in many games, especially on mobile or VR platforms. It allows for complex lighting scenarios without the performance cost of real-time lights.

> [!tip] Experiment
> Try adjusting the light positions, intensities, and colors. See how these changes affect the mood of your scene. Also, experiment with different post-processing settings to achieve various visual styles.

---

## Part 3: Implementing Post-Processing

> [!warning] Post Processing Lesson
> We will revisit Post Processing at a later time in the course in more detail, for now, we need it to comprehend Emissive Materials and how they affect lighting.

1. Set up the Post-Processing Volume:
   - Create a Global Volume (`GameObject > Volume > Global Volume`)

2. Create a Post-Processing Profile:
   - Create a `Rendering` folder in your Project window.
   - In the Project window, `right-click > Create > Volume Profile`.
   - Name it "Main Profile".
   - Drag this profile into the `Profile` slot of your Global Volume component.

3. Add and configure effects:
   - Select the "Main Profile" in the Project window.
   - Click `Add Override` and add the following:
     - Bloom
     - Color Adjustments (URP uses this instead of Color Grading)
     - Vignette

1. Configure the effects:
   - Bloom: Set `Intensity` to 1 and `Threshold` to 0.9.
   - Color Adjustments: Change `Contrast` to 10 and `Saturation` to 10. Give the `Color Filter` a *slightly* warmer or cooler tone using the color picker.
   - Vignette: Set `Intensity` to 0.4 and `Smoothness` to 0.3.
![[globalVolume.png]]

> [!note] Connection to Lecture
> Post-processing effects are applied after the scene is rendered, similar to filters in photo editing software. They can dramatically enhance the mood and style of your game.

1. Enable post-processing on the camera:
   - Select the Main Camera in the Hierarchy.
   - Ensure it has a "Universal Additional Camera Data" component.
   - Under the `Rendering` section tick on Post Processing
   - In this component, set "Render Type" to "Base" if it isn't already.
![[cameraPP.png]]


> [!warning] Important
> If you don't see any change, ensure that your Scene View is set to have Post-Processing turned on using the top right hotbar.

## Part 7: Understanding and Using Light Probes

1. Create a Light Probe Group:
   - In the Hierarchy, `right-click > Light > Light Probe Group`

1. Position Light Probes:
   - With the Light Probe Group selected, you'll see spheres in the scene view
   - Position these spheres around your scene, focusing on areas where dynamic objects will move. 
   - Select the Light Probe Group in the Hierarchy. In the Inspector, click `Edit Light probe Positions`. You can now move the yellow spheres.
   - Place probes near corners, under overhangs, and in open areas. Anywhere where moving objects or better lighting data is needed.
   - Aim for a good coverage without overdoing it (start with about 8-10 probes for our small scene)

![[editLightProbe.png]]

> [!tip] Light Probe Placement
> Think of light probes as sampling points for lighting. Place them where you want dynamic objects to pick up lighting information, especially in areas with significant lighting changes or dynamic objects.

3. Create a dynamic object:
   - Add a new cube to your scene (`GameObject > 3D Object > Cube`)
   - Position it slightly above the ground plane
   - *Ensure it's not marked as Static in the Inspector*

4. Set up a simple movement script:
   - Create a new script called "ObjectMover"
   - Add this script to your new cube
   - Open the script and replace its contents with:

```csharp
using UnityEngine;

public class ObjectMover : MonoBehaviour
{
    public float speed = 2f;
    public float distance = 4f;

    private Vector3 startPosition;

    void Start()
    {
        startPosition = transform.position;
    }

    void Update()
    {
        float newX = startPosition.x + Mathf.Sin(Time.time * speed) * distance;
        transform.position = new Vector3(newX, transform.position.y, transform.position.z);
    }
}
```

5. Bake lighting:
   - Ensure your static objects are marked as Static
   - Open the Lighting window (`Window > Rendering > Lighting`)
   - Click "Generate Lighting" to bake your lightmaps and light probes

6. Observe the results:
   - Play the scene and watch how the moving cube picks up lighting information from the probes
   - The cube should show smooth lighting transitions as it moves through different areas of your scene

> [!note] Light Probes and URP
> In URP, Light Probes work seamlessly with the scriptable render pipeline, providing efficient lighting for dynamic objects in both forward and deferred rendering paths.

7. Experiment with probe placement:
   - Try adding more probes or adjusting their positions
   - Rebake lighting and observe how it affects the lighting on your moving cube

> [!warning] Performance Consideration
> While Light Probes are more performance-friendly than real-time lighting, too many probes can increase memory usage and baking times. Start with a minimal set and add more only where needed.

8. Combine with emissive materials:
   - Try placing some light probes near your emissive object from the previous sections
   - Observe how the moving cube picks up the glow from the emissive object as it passes nearby

---
## Part 8: Implementing Reflection Probes

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

