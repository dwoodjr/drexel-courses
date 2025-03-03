# GMAP 395 - WK 9 Tutorial

## "Designing Game Feel with Post-Processing and Cinemachine Zoom"

![[tutWk9Splash.png]]

[gmap395_wk9.mp4](https://1drv.ms/v/s!AqQzGx8l4o2wk_NKaj-oxfZpUrjR7Q?e=4frRJP)
<iframe src="https://1drv.ms/v/s!AqQzGx8l4o2wk_NKcpStl3WcUMfuTg?embed=1" width="640" height="320" frameborder="0" scrolling="no" allowfullscreen></iframe>


---

## Objective

In this tutorial, we will add two key interactive systems to our enemy spawn sequence:

1. A **Post-Processing Vignette Effect** that uses **DOTween** to pulse the screen green, reinforcing the anticipation of enemy arrival.
2. A **Cinemachine Zoom Control**, allowing the player to zoom in with a button press to get a closer look at the action.



> [!example] Scripting APIs for this Tutroial
> [Unity Doc on Volumes](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@7.1/manual/Volumes.html)
> [Editing Volumes at Runtime](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@12.0/manual/Volumes-API.html)
> [Unity Doc on Cinemachine](https://docs.unity3d.com/Packages/com.unity.cinemachine@2.3/manual/index.html)
> [CinemachineVirtualCamera Class](https://docs.unity3d.com/Packages/com.unity.cinemachine@2.1/api/Cinemachine.CinemachineVirtualCamera.html)


### Why are we doing this?

**Design Reasoning:** Visual feedback and real-time control are critical parts to guiding the player's emotions and attention. A subtle green vignette can signal danger and build tension, while player-controlled zoom provides agency, allowing players to focus on dramatic events like an enemy spawning.

---

## Prerequisites
- Unity 2022.3 LTS with URP
- DOTween installed and set up
- Cinemachine installed
- Completion of the Week 7 sequence (Portal, Shader, EnemySpawner, etc.)

---

# Part 1: Post-Processing Alert Feedback

### Why Post-Processing?

Post-processing effects are a final layer of polish that add emotional weight.  
For example:

- Vignette = Focus and tension
- Green Tint = Danger, sickness, or otherworldly energy

#### Goal: 
Pulse a green vignette during the enemy spawn sequence.

---

### Step 1: Add a Vignette Effect

1. **Locate your Global Volume** in the Hierarchy.
2. In the Inspector, find the attached **Volume Profile**.
3. Click **Add Override → Post-processing → Vignette**.
4. Enable these settings:
    - **Color:** Black (for now)
    - **Intensity:** `0.3`
    - **Smoothness:** `0.5`

📝 _Design Note:_  
We start subtle so the change to green is noticeable and feels meaningful during the event.

---

### Step 2: Create the VignetteController Script

> Scripts (Folder) → Create → C# Script → Name it **VignetteController**

Paste this code:

```csharp
using UnityEngine;
using DG.Tweening;
using UnityEngine.Rendering;
using UnityEngine.Rendering.Universal;

public class VignetteController : MonoBehaviour
{
    public Volume postProcessVolume;
    private Vignette vignette;

    public Color normalColor = Color.black;
    public Color alertColor = Color.green;
    public float alertIntensity = 0.6f;
    public float transitionDuration = 1.0f;

    void Start()
    {
        postProcessVolume.profile.TryGet(out vignette);
        vignette.color.value = normalColor;
        vignette.intensity.value = 0.3f;
    }

	public void ActivateAlert()
	{
	    DOTween.To(() => vignette.color.value, x => vignette.color.value = x, alertColor, transitionDuration);
	    DOTween.To(() => vignette.intensity.value, x => vignette.intensity.value = x, alertIntensity, transitionDuration);
	}

	public void DeactivateAlert()
	{
	    DOTween.To(() => vignette.color.value, x => vignette.color.value = x, normalColor, transitionDuration);
	    DOTween.To(() => vignette.intensity.value, x => vignette.intensity.value = x, 0.3f, transitionDuration);
	}

}
```

---

### Step 3: Attach the Script

1. Create an empty GameObject in the Hierarchy → Name it **VignetteController**.
2. Add the **VignetteController.cs** script.
3. Drag the **Global Volume** into the **Post Process Volume** field.

---

### Step 4: Connect to EnemySpawner

1. In **EnemySpawner.cs**, (at the top with the other variables) add:

```csharp
public VignetteController vignetteController;
```

1. Before the portal ring effect starts, activate the vignette (inside `TriggerFullSequence()`):

```csharp
vignetteController.ActivateAlert();
```

1. After the enemy has spawned and the sequence ends, reset it  (inside `TriggerFullSequence()`):

```csharp
vignetteController.DeactivateAlert();
```

📝 _Design Note:_  
Players need _signals_ when big events happen. This pulse grabs attention without needing UI text.

---

### Step 5: Test
1. One all scripts have been made/modified.
2. Ensure that the Vignette Controller game object is created as has the `VingetteController.cs` attached.
3. Ensure the `EnemySpawner.cs` has the Vignette Controller game object assigned.
4. Play the scene and activate the sequence with the assigned key press.
	1. You should now see the edges of teh screen skrink in and turn green.
	2. Note: if your scene has little light, the effect will not be as noticeable, as Vignette uses alpha transparency. 

### Step 6 (Optional): Add a Pulsing effect to Vignette
By adding one private variable and updating the `ActivateAlert()` and `DeactivareAlert()` methods to use DOTween sequencing, we can have the vignete color or intensity pusle while the alert is active.

```c#
private Tween pulseTween; //add this new variable

public void ActivateAlert() //update this function call
{
    // Transition to the alert color
    DOTween.To(() => vignette.color.value, x => vignette.color.value = x, alertColor, transitionDuration);

    // Start pulsing the intensity
    pulseTween = DOTween.To(() => vignette.intensity.value, x => vignette.intensity.value = x, alertIntensity, transitionDuration)
        .SetLoops(-1, LoopType.Yoyo)
        .SetEase(Ease.InOutSine);
}

public void DeactivateAlert() //update this function call
{
    // Stop pulsing
    if (pulseTween != null)
    {
        pulseTween.Kill();
    }

    // Reset to normal color and intensity
    DOTween.To(() => vignette.color.value, x => vignette.color.value = x, normalColor, transitionDuration);
    DOTween.To(() => vignette.intensity.value, x => vignette.intensity.value = x, 0.3f, transitionDuration);
}

```

1. Make the above code changes and play the scene again. You should now see the effect pulse.

---
----
# Part 2: Cinemachine Zoom Control

### Why Player-Controlled Zoom?

Zoom gives the player agency to focus on something important. It's also a dramatic tool—getting close to the action increases intensity and makes the experience feel more "personal."

---

### Step 1: Set Up Cinemachine

1. Go to **Package Manager → Cinemachine** (install if not done).
2. In the Hierarchy, **Cinemachine → Create Virtual Camera**.
3. Set the Virtual Camera’s Field of View (**FOV**) to `60`.

---

### Step 2: Create the Cinemachine Camera Assets
Note: The following steps will reset the transform of the **Main Camera**. So take note of its transforms!
1. Right-Click in the Hierarchy --> **Cinemachine** --> **Virtual Camera**.
2. You will now a Virtua Camera in the scene and your Main Camera will have a Cinemachine Brain attached to it.
	1. Note: Changing the Main Cameras transforms will do nothing. The **Virtual Camera** not controls the Main Camera.
3. In the Virtual Camera, set Transition -> Body to *Do Nothing.*
4. In the Virtual Camera, set Aim to *POV.*
5. To reposition your camera, use the Virtual Camera -> *Transform* -> *Position* to move it. 
6. To rotate use the Virtual Camera -> Aim -> *Vertical Axis* Value) and *Horizontal Axis* (Value).
7. Reposition your camera to a desired location.
---
### Step 3: Create CameraZoomController Script

> Scripts → Create → C# Script → Name it **CameraZoomController**

Paste this code:

```csharp
using UnityEngine;
using DG.Tweening;
using Cinemachine;

public class CameraZoomController : MonoBehaviour
{
    public CinemachineVirtualCamera virtualCamera;
    public float normalFOV = 60f;
    public float zoomedFOV = 30f;
    public float zoomDuration = 0.5f;

    private bool isZoomed = false;

    void Update()
    {
        if (Input.GetKeyDown(KeyCode.Z))
        {
            ToggleZoom();
        }
    }

	void ToggleZoom()
	{
	    float targetFOV = isZoomed ? normalFOV : zoomedFOV;
	    DOTween.To(
	        () => virtualCamera.m_Lens.FieldOfView,
	        x => {
	            var lens = virtualCamera.m_Lens;
	            lens.FieldOfView = x;
	            virtualCamera.m_Lens = lens;
	        },
	        targetFOV,
	        zoomDuration
	    );
	    isZoomed = !isZoomed;
	}

}
```

---

### Step 3: Attach the Script

1. Create an empty GameObject → Name it **CameraController**.
2. Add the **CameraZoomController.cs** script.
3. Drag your **Virtual Camera** into the script’s **Virtual Camera** field.

---

### Step 4: Test It

✅ Press **Z** to zoom in/out during gameplay.  
✅ Trigger the enemy sequence and see how zoom + vignette work together.

---
### Step 5 (Optional): Update Camera Controller for "Focus" Mode
If you would like to have the ability to click into the game window and remove the cursor (or called playing in focus) add the following code to `CameraZoomController.cs`.

```c#
	private bool cursorLocked = true;
	
	void Start()
	{
	    LockCursor();
	}
	
	void Update()
	{
	    if (Input.GetKeyDown(KeyCode.Z))
	    {
	        ToggleZoom();
	    }
	    if (Input.GetKeyDown(KeyCode.Escape))
	    {
	        UnlockCursor();
	    }
	    // Click to re-lock when unlocked
	    if (!cursorLocked && Input.GetMouseButtonDown(0))
	    {
	        LockCursor();
	    }
	}
	
	void LockCursor()
	{
	    Cursor.lockState = CursorLockMode.Locked;
	    Cursor.visible = false;
	    cursorLocked = true;
	}
	
	void UnlockCursor()
	{
	    Cursor.lockState = CursorLockMode.None;
	    Cursor.visible = true;
	    cursorLocked = false;
	}
```

#### How it works:
- Press **Escape** → unlocks cursor, makes it visible.
- Click **anywhere** (left mouse click) → re-locks cursor.
- Keeps track of whether the cursor is locked with the `cursorLocked` flag so it doesn't keep trying to lock it when it's already locked.
- Works in **Play Mode** and builds.
---
### Final Design Reflection:

- The **vignette** builds subconscious tension—danger is coming!
- The **zoom** gives the player control to witness the danger up close.
- Together, they turn a simple spawn event into a cinematic-esq, dramatic moment.

---
---
> [!info] [[GMAP 395 - Module 4| Return to the Module Page]]