# GMAP 395 - Week 7 Tutorial

### "Anticipation and Release: Timing VFX for Impact"

---

## Objective

This tutorial refines the timing and sequencing of portal-based visual effects in Unity. Using C# scripting and DOTween, we will:

1. Animate the Portal Ring VFX to pulse before the portal opens.
2. Trigger the Energy Beam VFX after the portal closes.
3. Align these effects with gameplay logic (enhancing game feel).

By the end, students will understand how sequencing and timing-based VFX create stronger player anticipation and response.

![[portalBeamVFX.png]]

---

## Video Tutorial

[gmap395_wk7.mp4](https://1drv.ms/v/s!AqQzGx8l4o2wk_JLePfLQVEQnJr33w?e=dFmT9U)

<iframe src="https://1drv.ms/v/s!AqQzGx8l4o2wk_JLWQ7rPG-qQIjiMQ?embed=1" width="640" height="320" frameborder="0" scrolling="no" allowfullscreen></iframe>

---
## Prerequisites

✅ Unity 2022.3 with URP and VFX Graph Installed  
✅ Completion of Week 5’s "Game-Based Real-Time Shader Control w/ DOTween"  
✅ Completion of Week 6’s "Enhancing the Eldritch Portal with VFX"  
✅ Basic understanding of C# scripting, DOTween, and Unity Events


> [!example] Unity VFX Scripting API
> The scripts from todays class will be using Unity's [VFX Scripting API](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VFX.VisualEffect.html) for VFX graph. Particle System has a separate API.


---

## Game Feel & Design Intent

> VFX are not just visuals—they are part of gameplay feedback.  
> Players subconsciously react to anticipation and payoff sequences before major in-game events.

In this case:

- The portal doesn’t just "pop open," it builds anticipation with a pulsing particle ring.
- After the portal closes, the energy beam fires, creating a dramatic "release" effect.
- Why?
    - Anticipation (Ring) = Builds tension before the event.
    - Payoff (Beam) = Reinforces impact and finality after the event.

This creates a stronger connection between VFX, game feel, and gameplay metaphor/mechanics.

---

# Part 1: Creating the Porta Effect Controller

### Overview

In this section, we will create the `PortalEffectsController` from scratch.  
This script will control the portal ring effect, animating its exposed VFX properties from Week 6 using DOTween.

The Portal Ring Effect serves as an anticipatory visual cue before the portal opens.  
By animating its properties over time, we create a build-up sequence that enhances game feel.


## Step 1: Review Exposed Properties from Week 6

In Week 6, we created a portal ring effect using Unity's VFX Graph.  
The following exposed properties were created in the VFX Graph Blackboard:

| Property Name         | Type  | Description                           |
| --------------------- | ----- | ------------------------------------- |
| `PortalRingRadius`    | Float | Controls the size of the ring         |
| `PortalRotationSpeed` | Float | Controls the brightness/intensity     |
| `PortalRingColor`     | Float | Controls the visibility of the effect |

## Step 2: Create the PortalEffectsController Script

Now, let's create the PortalEffectsController script to control the Portal Ring Effect.

### 1. Create the Script

1. In Unity, go to the Project Window.
2. Navigate to the Scripts folder (or create one if needed).
3. Right-click > Create > C# Script and name it PortalEffectsController.
4. Open the script in Visual Studio or VS Code.


### 2. Write the PortalEffectsController Script

Replace the default code with the following:

```csharp
using UnityEngine;
using UnityEngine.VFX;
using DG.Tweening;
using System.Collections;

public class PortalEffectsController : MonoBehaviour
{
    // Reference to the VFX Graph for the ring effect (assign in the Inspector)
    [SerializeField] private VisualEffect portalVFX;

    /// <summary>
    /// Plays the portal ring burst effect.
    /// Animates PortalRingRadius from 1.0 -> 1.35 -> 0.0, then stops the VFX.
    /// </summary
    public IEnumerator PlayPortalEffect()
    {
        if (portalVFX == null)
        {
            Debug.LogError("Portal VFX reference not set!");
            yield break;
        }

        // Set the starting value.
        portalVFX.SetFloat("PortalRingRadius", 1.0f);
        // Create a DOTween sequence to animate the ring.
        Sequence ringSequence = DOTween.Sequence();
        ringSequence.Append(
            DOTween.To(
                () => portalVFX.GetFloat("PortalRingRadius"),
                x => portalVFX.SetFloat("PortalRingRadius", x),
                1.35f,
                1f
            )
        );

        ringSequence.Append(
            DOTween.To(
                () => portalVFX.GetFloat("PortalRingRadius"),
                x => portalVFX.SetFloat("PortalRingRadius", x),
                0.0f,
                1f
            )
        );

        // When complete, stop the VFX.
        ringSequence.OnComplete(() => portalVFX.Stop());

        // Wait until the sequence is finished.
        yield return ringSequence.WaitForCompletion();

    }

    /// <summary>
    /// Restarts the portal ring effect (e.g. after the sequence finishes).
    /// </summary>

    public void RestartRingEffect()
    {
        if (portalVFX != null)
        {
            // Reset initial values required for the portal ring effect.
            portalVFX.SetFloat("PortalRingRadius", 1.0f);
            // Restart the VFX.
            portalVFX.Play();
        }
    }

}
```


## Step 3: Assign the Script in Unity

1. Attach the Script to a GameObject
    - In Unity, create an empty GameObject in the Hierarchy.
    - Rename it "VFX Controller".
    - Drag and attach the PortalEffectsController.cs script to this GameObject.
2. Assign the VFX Graph
    - Select the GameObject.
    - In the Inspector, locate the Portal VFX field.
    - Drag the Portal Ring VFX Graph from the Hierarchy into this field.


---

# Part 2: Implementing the PortalBeamEffect

## Overview

In this section, we will implement the `PortalBeamEffect` script using the provided code.  
This script controls the portal beam effect, which fires after the portal closes as a visual payoff for the event.

The Beam Effect enhances game feel, reinforcing the impact of the portal cycle completion.  
By properly sequencing this after the portal closes, we strengthen player response and timing in gameplay.


## Step 1: Understanding the PortalBeamEffect Script

The PortalBeamEffect script is set up to start and stop the Energy Beam Effect.

### Code Breakdown:

```csharp
using UnityEngine;
using UnityEngine.VFX;
using System.Collections;

public class PortalBeamEffect : MonoBehaviour
{
    // Reference to the beam VFX Graph (assign in the Inspector)
    public VisualEffect beamVFX;
    // Duration for which the beam effect remains active.
    public float beamDuration = 2.0f;

    private void Start()
    {
        // Ensure the beam doesn't play automatically on scene start.
        if (beamVFX != null)
        {
            beamVFX.Stop();
        }
    }

    /// <summary>
    /// Plays the beam effect by starting the VFX, waits for the duration, then stops it.
    /// </summary>
    public IEnumerator PlayBeamEffect()
    {
        if (beamVFX == null)
        {
            Debug.LogError("Beam VFX reference not set!");
            yield break;
        }
        
        beamVFX.Play();
        yield return new WaitForSeconds(beamDuration);
        beamVFX.Stop();
    }
}
```

#### Key Features of This Script:
- References the Beam VFX Graph (must be assigned in Unity).
- Ensures the beam does NOT play automatically on scene start.
- Provides a coroutine to play the beam, wait, then stop it.


## Step 2: Assign the Script in Unity

3. Attach the Script to a GameObject
    - In Unity, in the Hierarchy, locate the GameObject from Part 1.
    - Drag and attach the PortalBeamEffect.cs script to this GameObject.
4. Assign the VFX Graph
    - Select the GameObject.
    - In the Inspector, locate the Beam VFX field.
    - Drag the Energy Beam VFX Graph from the Hierarchy into this field.


---

# Part 3: Recreating the EnemySpawner

## Overview

In this section, we will recreate the EnemySpawner script from its original version to match the intended tutorial sequence design.  Additionally, we will review and verify the PortalShaderController to ensure it functions correctly within this sequence.

The EnemySpawner is responsible for orchestrating the VFX timing, enemy spawning logic, and game feel elements. *An argument could be made that the sequencing should be a separate script from enemy spawning logic, but I wanted to keep it a bit simpler for now.*

## Step 1: Reviewing the PortalShaderController

Before we proceed with EnemySpawner, we need to verify that PortalShaderController is correct for the tutorial.

### Reviewing the Provided PortalShaderController.cs

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

### Confirmations:
✔️ Uses DOTween to animate the shader property `_EdgeWidth`, expanding when activated and resetting when closed.  
✔️ The `ActivateAlert()` function properly transitions the effect when the portal is "opening."  
✔️ The `DeactivateAlert()` function ensures it returns to normal after closing.  
✔️ The `transitionDuration` parameter can be adjusted to fine-tune timing.

No modifications should be needed. The PortalShaderController functions correctly for the purposes of our tutorial. It is jus a good habit to check code you will be referencing/interacting with in the editor.


## Step 2: Recreating the EnemySpawner Script

Now, we will REBUILD the EnemySpawner script from its original version, incorporating the full game feel sequence.

### 1. Create the EnemySpawner Script

5. In Unity, go to the Project Window.
6. Navigate to the Scripts folder (or create one if needed).
7. Right-click > Create > C# Script and name it EnemySpawner (or open the original script if you have one).
8. Open the script in your IDE.


### 2. Write the Recreated EnemySpawner Script

Replace the code with the following:

```csharp
using UnityEngine;
using System.Collections;
using DG.Tweening;

public class EnemySpawner : MonoBehaviour
{
    [Header("Portal Settings")]
    public PortalEffectsController portalEffects; // Controls the ring effect
    public PortalShaderController portalShader;   // Controls the shader opening/closing
    public PortalBeamEffect portalBeamEffect;     // Controls the beam effect

    [Tooltip("Delay after shader opens before spawning the enemy.")]
    public float enemyInstantiationDelay = 1.0f; 

    [Tooltip("Delay after beam effect stops before restarting the portal ring effect.")]
    public float ringRestartDelay = 0.5f;

    [Header("Enemy Settings")]
    public GameObject enemyPrefab;         // Enemy prefab to spawn
    public Transform releasePoint;         // Target position on the ground
    public float dropDuration = 3f;        // Duration of the enemy falling

    void Update()
    {
        // For testing: trigger the full sequence with the Space key.
        if (Input.GetKeyDown(KeyCode.Space))
        {
            StartCoroutine(TriggerFullSequence());
        }
    }

    IEnumerator TriggerFullSequence()
    {
        Debug.Log("Starting enemy spawn sequence...");

        // --- STEP 1: Portal Ring Effect (Anticipation) ---
        yield return portalEffects.PlayPortalEffect();

        // --- STEP 2: Portal Shader Opens (Portal Begins to Activate) ---
        portalShader.ActivateAlert();
        yield return new WaitForSeconds(portalShader.transitionDuration);

        // --- STEP 3: Enemy Spawning (Gameplay Event) ---
        yield return new WaitForSeconds(enemyInstantiationDelay);
        GameObject enemyInstance = Instantiate(enemyPrefab, transform.position, Quaternion.identity);
        enemyInstance.transform.DOMove(releasePoint.position, dropDuration)
            .SetEase(Ease.Linear)
            .OnComplete(() =>
            {
                // Unparent the enemy so it moves freely in the scene
                enemyInstance.transform.parent = null;
            });
        yield return new WaitForSeconds(dropDuration);

        // --- STEP 4: Portal Shader Closes (Portal Powers Down) ---
        portalShader.DeactivateAlert();
        yield return new WaitForSeconds(portalShader.transitionDuration);

        // --- STEP 5: Portal Beam Effect (Powerful Release) ---
        yield return StartCoroutine(portalBeamEffect.PlayBeamEffect());

        // --- STEP 6: Restart Portal Ring Effect (Loop Back to Idle State) ---
        yield return new WaitForSeconds(ringRestartDelay);
        portalEffects.RestartRingEffect();

        Debug.Log("Enemy spawn sequence complete.");
    }
}
```


## Step 3: Explanation of the Sequence Timing

The updated script ensures proper sequencing and game feel through timing considerations:

### Game Feel Enhancements

| Step                 | Purpose                              | Game Feel Contribution                            |
| -------------------- | ------------------------------------ | ------------------------------------------------- |
| Portal Ring Burst    | Builds anticipation                  | Player sees a pre-cue before the portal activates |
| Portal Shader Opens  | Signals the enemy is about to appear | Establishes expectation and tension               |
| Enemy Spawn & Drop   | Core gameplay event                  | Visual reinforcement of the game action           |
| Portal Shader Closes | Closes the portal to show completion | Confirms event has concluded                      |
| Portal Beam Fires    | Creates a dramatic payoff            | Reinforces weight and finality of the event       |
| Portal Ring Restarts | Resets for next activation           | Ensures seamless looping behavior                 |

✅ Now, the entire sequence works as a fully structured event.


## Step 4: Testing the Full Sequence in Play Mode

9. Click Play in Unity.
10. Press Space to trigger the full sequence.
11. Observe the correct ordering of effects:
    - Portal Ring pulses
    - Portal Shader expands
    - Enemy spawns
    - Portal Shader closes
    - Energy Beam fires
    - Portal Ring resets
12. Adjust timing variables in the Inspector to fine-tune the pacing.


---

## Final Steps:

The tutorial is now complete! 🎉  
The full portal cycle now functions as an engaging game-based metaphor!

---
---
>[!info]  [[GMAP 395 - Module 3| Return to the Module Page]]
