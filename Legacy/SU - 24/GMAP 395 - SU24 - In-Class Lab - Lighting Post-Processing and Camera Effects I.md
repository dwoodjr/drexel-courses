# Lab Exercise: Lighting, Post-Processing, and Dynamic Camera in Unity URP

## Objective
In this lab, you'll create a simple 3D scene using the Universal Render Pipeline (URP), apply basic lighting techniques, explore emissive materials, add post-processing effects, and implement a dynamic camera zoom using Cinemachine.

## Prerequisites
- Unity 2022.3 LTS or later
- Basic familiarity with the Unity interface

---
## Part 1: Setting Up the Scene

1. Create a new URP 3D Unity project.
   - When creating a new project, select "3D (URP)" as the template.

2. In the Hierarchy window, right-click and select 3D Object > Plane to create a ground plane.

3. Scale the plane to (10, 1, 10) using the Scale tool or the Inspector.

4. Create a few simple objects in the scene (feel free to change positions to suit your needs):
   - Add a cube (3D Object > Cube) and position it at (0, 0.5, 0).
   - Add a sphere (3D Object > Sphere) and position it at (2, 0.5, 2).
   - Add a capsule (3D Object > Capsule) and position it at (-2, 1, -2).

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
![[colorHexCode 1.png]]
> [!tip] Tip
> Use color theory to create mood and depth in your scene. Warm colors tend to advance (appear closer), while cool colors recede (appear farther away).

---
## Part 3: Implementing Post-Processing

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

---
## Part 4: Lighting Configuration and Baking

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
## Part 8: Dynamic Camera with Cinemachine

1. Install Cinemachine:
   - Go to Window > `Package Manager > Unity Registry`.
   - Search for "Cinemachine" and click "Install".

> [!NOTE]
> For an easy to follow example of a Cinemachine camera follow setup, download and install the Starter Assets - ThirdPerson (Unity Technologies) character from the Unity Asset Store.   

2. Create a Cinemachine Virtual Camera:
   - In the Hierarchy, `right-click > Cinemachine > Virtual Camera`.
   - This will create a Cinemachine Brain on your Main Camera and a Virtual Camera in the scene.

3. Configure the Virtual Camera:
   - Select the Virtual Camera in the Hierarchy.
   - In the Inspector, set the `Follow` target and `Look At` to a primitive object in your scene.
   - Adjust the Body settings:
     - Set Lens > Field of View to 60.
     - In Aim > Composer, set the Dead Zone Width and Height to 0.1.

1. Add a simple zoom script:
   - Create a `Scripts` folder.
   - Create a new script (`right-click in Project window > Create > C# Script`).
   - Name it "CameraZoom".
   - Double-click to open it in your code editor.

5. Replace the contents of the script with the following code:

```csharp
using UnityEngine;
using Cinemachine;

public class CameraZoom : MonoBehaviour
{
    public CinemachineVirtualCamera virtualCamera;
    public float zoomSpeed = 10f;
    public float minFOV = 10f;
    public float maxFOV = 90f;

    private float targetFOV;

    void Start()
    {
        targetFOV = virtualCamera.m_Lens.FieldOfView;
    }

    void Update()
    {
        float scrollInput = Input.GetAxis("Mouse ScrollWheel");
        targetFOV -= scrollInput * zoomSpeed;
        targetFOV = Mathf.Clamp(targetFOV, minFOV, maxFOV);

        virtualCamera.m_Lens.FieldOfView = Mathf.Lerp(virtualCamera.m_Lens.FieldOfView, targetFOV, Time.deltaTime * 10f);
    }
}
```

1. Apply the zoom script:
   - Select the Virtual Camera in the Hierarchy.
   - Add the CameraZoom component (`Add Component > Scripts > Camera Zoom`).
   - Drag the Virtual Camera from the Hierarchy into the `Virtual Camera` field in the CameraZoom component.

![[virtualCamera.png]]

> [!note] Connection to Lecture
> Dynamic cameras are crucial in many games, providing players with control over their view of the game world. This zoom mechanic is commonly used in strategy games, RPGs, and exploration-based games.

7. Test your scene:
   - Press Play and use the mouse scroll wheel to zoom in and out.
   - Move around the scene to see how the lighting and post-processing effects change your view.
