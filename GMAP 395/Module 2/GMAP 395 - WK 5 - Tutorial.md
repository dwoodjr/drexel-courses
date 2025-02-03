# Game-Based Real-Time Shader Control w/ DOTween

## Objective

In this tutorial, students will **control shader parameters in real-time** using C# scripts and game-based events. The goal is to modify the **Eldritch Portal Shader** from Week 4 dynamically, based on game logic (e.g., an enemy spawning from the portal).

---

## Video Tutorial
<iframe src="https://1drv.ms/v/s!AqQzGx8l4o2wk_IOiSIk0gRqbP1vLw?embed=1" width="640" height="320" frameborder="0" scrolling="no" allowfullscreen></iframe>
[gmap395_tut4.mp4](https://1drv.ms/v/s!AqQzGx8l4o2wk_IOWxZ2Vcsusxzvng?e=ONBhuI)

---

## Prerequisites

✅ Unity 2022.3 with URP  
✅ [DOTween](https://dotween.demigiant.com/getstarted.php)
✅ Completion of **Week 4’s Eldritch Portal Shader**  
✅ Basic familiarity with **Shader Graph & C# Scripting**

---

## Part 1: Setting Up DOTween in Unity

#### Installing DOTween and Basic Animation Example

Before we start controlling shader parameters, we need to **install and set up DOTween** in Unity. DOTween is a tweening engine that allows us to animate values smoothly over time, including object positions, UI elements, and shader properties.

---

### Step 1: Installing DOTween from the Unity Asset Store

1. Open **Unity** and go to the **Asset Store** (`Window > Asset Store`). The asset store can also be accesses from the Unity Hub (`Community > Asset Store`)
2. Search for **DOTween** (by **Demigiant**). The *free* version is fine for this course.
3. Click **Add to My Assets**, then **Open in Unity** it into your project. Then **Import** it.
4. After importing, go to `Tools > DOTween Utility Panel` in the top menu bar.
5. Click **Setup DOTween** (this generates the necessary setup files).

![[dotween1.png]]

> ✅ DOTween is now ready to use in your project! 🎉

---

### Step 2: Creating a Simple DOTween Animation

Let’s create a quick **cube animation** to test DOTween.

#### 1. Create a Test Cube

1. In a new test scene, in the **Hierarchy**, right-click and select `3D Object > Cube`.
2. Rename it **"TweenCube"**.
3. Reset its **Transform** (`Right-click Transform > Reset` in the **Inspector**).

#### 2. Create a DOTween Script

1. In the **Project Window**, in your Scripts folder create a new C# script named **`DOTweenTest.cs`**.
2. Attach it to **TweenCube**.
3. Open the script and replace its contents with:

```csharp
using UnityEngine;
using DG.Tweening; // Import DOTween

public class DOTweenTest : MonoBehaviour
{
    void Start()
    {
        // Move the cube up and down repeatedly
        transform.DOMoveY(3f, 1f) // Move to Y = 3 in 1 second
            .SetLoops(-1, LoopType.Yoyo) // Infinite loop with Yoyo effect
            .SetEase(Ease.InOutSine); // Smooth transition
    }
}
```

#### 3. Run the Scene and Observe

4. Click **Play** in Unity.
5. The cube will **move up and down smoothly** forever.
6. Try modifying values like:
    - Changing `DOMoveY(3f, 1f)` to `DOMoveX(5f, 2f)` to move **sideways** instead.
    - Adjusting `.SetEase(Ease.InOutSine)` to `.SetEase(Ease.OutBounce)` for a different effect.

---

### Understanding the Code

✅ **`DOMoveY(3f, 1f)`** → Moves the cube’s Y position to `3` over `1` second.  
✅ **`.SetLoops(-1, LoopType.Yoyo)`** → Makes it loop **infinitely** (up and down).  
✅ **`.SetEase(Ease.InOutSine)`** → Creates a **smooth, natural motion**.


> [!NOTE] DOTween Documentation
> All of the possible functions/methods and concepts around the tweening engine can be learned from the [documentation](https://dotween.demigiant.com/documentation.php).


---
## Part 2: Exposing Shader Properties for DOTween Control

### Step 1: Modify the Eldritch Portal Shader (Only if Needed)

1. Open the EldritchPortalShader in Shader Graph.
2. Locate the **`EdgeWidth`** property in the Blackboard.
3. Check its **Reference Name** is set to `_EdgeWidth` in the **Graph Inspector** > **Node Settings** (for C# access).
4. Check that *Exposed* is ticked on.
5. Save and Apply changes.

---

## Part 3: Writing the Portal Shader Controller Script

We will use **DOTween** to smoothly animate the portal’s `EdgeWidth` when an "enemy is about to spawn."

### Step 1: Create the `PortalShaderController` Script

6. In Unity, create a new C# script named **`PortalShaderController.cs`**.
7. Attach it to the **Portal GameObject**, the one with the shader and material applied to it.
8. Replace its contents with the following:

```csharp
using UnityEngine;
using DG.Tweening; // Import DOTween

public class PortalShaderController : MonoBehaviour
{
    public Material portalMaterial;  // Assign the material in the Inspector
    private static readonly int EdgeWidthProperty = Shader.PropertyToID("_EdgeWidth");

    public float normalWidth = 0.2f;
    public float alertWidth = 0.6f;
    public float transitionDuration = 1.0f; // How long the animation takes

    void Start()
    {
        if (portalMaterial == null)
        {
            Debug.LogError("Portal material not assigned!");
            return;
        }

        // Ensure EdgeWidth starts at normal width
        portalMaterial.SetFloat(EdgeWidthProperty, normalWidth);
    }

    // Triggered when an enemy is about to spawn
    public void ActivateAlert()
    {
        Debug.Log("Portal activating.");
        
        // DOTween smoothly changes EdgeWidth over time
        portalMaterial.DOFloat(alertWidth, EdgeWidthProperty, transitionDuration)
            .SetEase(Ease.InOutQuad);
    }

    // Reset the effect after a delay
    public void DeactivateAlert()
    {
        Debug.Log("Portal deactivating.");
        
        // DOTween smoothly returns EdgeWidth to normal
        portalMaterial.DOFloat(normalWidth, EdgeWidthProperty, transitionDuration)
            .SetEase(Ease.InOutQuad);
    }
}
```

### What’s Happening?

✅ **`DOFloat()`**: Smoothly transitions the shader property over time.  
✅ **`SetEase(Ease.InOutQuad)`**: Adds a smooth acceleration/deceleration.  
✅ **`ActivateAlert()`**: Expands the portal effect.  
✅ **`DeactivateAlert()`**: Resets the effect after a delay.


> [!warning] Inspector Values
> Be sure to assign the correct `POrtal Material` and tweak the `Normal Width` and `Alert Width` values in the Inspector for this script. If not errors may arise, such as a "*NullReferenceExcpetion*"

![[portalInspector.png]]

---

## Part 4: Triggering the Shader Effect with an Enemy Spawn Event

### Step 1: Simulating an Enemy Spawn Event

1. Create an **empty GameObject** named **"EnemySpawner"**.
2. Create a new script called **EnemySpawner**.
3. Attach the script to it and replace its contents:

```csharp
using UnityEngine;
using System.Collections;

public class EnemySpawner : MonoBehaviour
{
    public PortalShaderController portalShader;
    public float spawnDelay = 5f;  // Time before enemy spawns

    void Start()
    {
        StartCoroutine(TriggerPortalAlert());
    }

    IEnumerator TriggerPortalAlert()
    {
        while (true)
        {
            yield return new WaitForSeconds(spawnDelay);
            
            Debug.Log("Enemy spawning. Triggering portal effect.");
            portalShader.ActivateAlert();
            
            yield return new WaitForSeconds(3f);
            
            Debug.Log("Enemy spawned. Resetting portal.");
            portalShader.DeactivateAlert();
        }
    }
}
```

### Step 2: Assign References

1. Drag the **Portal GameObject** into the `portalShader` field in the **EnemySpawner script**.
2. **Play the scene**—the **portal will expand and contract smoothly** when an enemy is "about to spawn."

![[enemySpawnerInspector.png]]

---

## Part 5: Final Testing and Tweaks

✅ Test different `EdgeWidth` values to fine-tune the visual effect.  
✅ Experiment with DOTween easing settings (`Ease.OutBounce`, `Ease.InCirc`, etc.).  
✅ Try different game triggers instead of a timer (e.g., using `OnTriggerEnter`).

---

## Summary

✅ Connected a C# script to Shader Graph to modify `EdgeWidth` dynamically.  
✅ Used DOTween for smooth, animated transitions.  
✅ Triggered the effect using a simulated enemy spawn event.  
✅ Enhanced the experience with sound and particles.

### Next Steps for Students

- Try **controlling other shader properties** (like `SwirlSpeed` or `EdgeColor`).
- Replace the **enemy timer with a real game event** (e.g., player proximity).  
- Experiment with **DOTween sequencing** for more complex VFX.


---
---
>[!info]  [[GMAP 395 - Module 2| Return to the Module Page]]