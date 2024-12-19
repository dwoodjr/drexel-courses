Creating and Implementing a C# VFX Controller in Unity

Objective: Learn how to create a VFX Controller that manages both particle effects and character reveal (material/shader) animations using tweening.

Prerequisites:
- Unity project with VFX Graph set up
- DOTween package installed
- A 3D character model with a material that supports transparency and emission 

> [!hint] 
> A `Material` with `Transparency` + `Emmision`

Step 1: Create the VFXController Script

1. In Unity, right-click in the Project window.
2. Select Create > C# Script and name it "VFXController".
3. Double-click the script to open it in your code editor.

Step 2: Set Up the Script

Replace the contents of the script with the following code:

```csharp
using UnityEngine;
using UnityEngine.VFX;
using DG.Tweening;

public class VFXController : MonoBehaviour
{
    public VisualEffect vfxGraph;
    public Renderer characterRenderer;
    public float revealDuration = 2f;
    public float peakMultiplier = 100f;
    public float characterRevealDelay = 0.5f;
    public float characterRevealDuration = 1.5f;
    public float maxEmissionIntensity = 1f;

    private Material characterMaterial;
    private static readonly string EmissionColor = "_EmissionColor";
    private Color originalEmissionColor;

    // ... (rest of the script as provided in the previous response)
}
```

> [!note] 
> The `using` statements at the top import necessary Unity and DOTween functionalities.

Step 3: Implement the Initialization Methods

Add the following methods to your script:

```csharp
private void Awake()
{
    StopVFX();
    SetupCharacterMaterial();
}

private void Start()
{
    vfxGraph.SetFloat("Multiplier", 0.1f);
}

private void SetupCharacterMaterial()
{
    if (characterRenderer != null)
    {
        characterMaterial = characterRenderer.material;
        originalEmissionColor = characterMaterial.GetColor(EmissionColor);
        SetCharacterAlpha(0);
        SetEmissionIntensity(0);
        characterRenderer.enabled = false;
    }
    else
    {
        Debug.LogError("Character Renderer not assigned!");
    }
}
```

> [!tip]
> The `Awake` method runs before `Start`, making it ideal for initialization. We use it to set up our VFX and character material.

Step 4: Implement the Reveal Methods

Add these methods to control the reveal animation:

```csharp
public void RevealCharacter()
{
    StartVFX();
    AnimateVFX();
    DOVirtual.DelayedCall(characterRevealDelay, AnimateCharacterReveal);
}

private void AnimateVFX()
{
	DOTween.Kill(vfxGraph);  
  
Sequence sequence = DOTween.Sequence();  
  
sequence.Append(DOTween.To(() => vfxGraph.GetFloat("Multiplier"),  
                           x => vfxGraph.SetFloat("Multiplier", x),  
                           peakMultiplier, revealDuration * 0.1f).SetEase(Ease.OutExpo));  
  
sequence.Append(DOTween.To(() => vfxGraph.GetFloat("Multiplier"),  
                           x => vfxGraph.SetFloat("Multiplier", x),  
                           peakMultiplier * 0.5f, revealDuration * 0.2f).SetEase(Ease.InOutQuad));  
  
sequence.AppendInterval(revealDuration * 0.4f);  
  
sequence.Append(DOTween.To(() => vfxGraph.GetFloat("Multiplier"),  
                           x => vfxGraph.SetFloat("Multiplier", x),  
                           1f, revealDuration * 0.3f).SetEase(Ease.InOutQuad));  
  
sequence.OnComplete(StopVFX);
}

private void AnimateCharacterReveal()
{
	if (characterMaterial != null)  
{  
    characterRenderer.enabled = true;  
  
    Sequence sequence = DOTween.Sequence();  
  
    sequence.Append(DOTween.To(() => characterMaterial.color.a,  
                               x => SetCharacterAlpha(x),  
                               1f, characterRevealDuration)  
                   .SetEase(Ease.InOutQuad));  
  
    sequence.Join(DOTween.To(() => 0f,  
                             x => SetEmissionIntensity(x),  
                             maxEmissionIntensity, characterRevealDuration)  
                  .SetEase(Ease.InOutQuad));  
}
}
```

> [!NOTE]
> The `RevealCharacter` method is our main entry point. It starts the VFX, animates it, and then triggers the character reveal after a short delay.

Step 5: Implement Utility Methods

Add these helper methods to your script: 
These helper methods are very similar in nature animating material properties of a custom shader.

```csharp
private void SetCharacterAlpha(float alpha)
{
    if (characterMaterial != null)
    {
        Color color = characterMaterial.color;
        color.a = alpha;
        characterMaterial.color = color;
    }
}

private void SetEmissionIntensity(float intensity)
{
    if (characterMaterial != null)
    {
        characterMaterial.SetColor(EmissionColor, originalEmissionColor * intensity);
    }
}

private void StartVFX()
{
    vfxGraph.SendEvent("OnPlay");
}

private void StopVFX()
{
    vfxGraph.SendEvent("OnStop");
}
```

> [!tip]
> These utility methods handle specific tasks like setting material properties and controlling the VFX Graph. Breaking these out into separate methods makes our code more readable and maintainable.

Step 6: Set Up the Scene

1. Ensure you have setup the VFX Graph and "Character" from the visual effect graph tutorial.
4. Ensure your character's material has:
   - Transparency mode enabled
   - An emission color or map set up

> [!attention] 
> The character's material settings are crucial for the reveal effect. Make sure your shader supports both transparency and emission!

Step 7: Configure the VFXController in the Inspector

1. Select the VFXController GameObject.
2. In the Inspector, you'll see fields for the VFXController script:
   - Drag your VFX Graph asset to the "Vfx Graph" field.
   - Drag your character's Renderer component to the "Character Renderer" field.
   - Adjust other parameters like reveal duration and emission intensity as desired.![[tut_csharp_vfx_script 1.png]]


Step 8: Ensure the Set Up the VFX Graph

1. Open your VFX Graph asset.
2. Ensure you have "OnPlay" and "OnStop" events set up to control your effect.
3. Add a "Float" parameter named "Multiplier" to your graph.
4. Use this Multiplier to control aspects of your effect (e.g., particle count, size, or emission rate).

![[tut_csharp_vfx_graph.png]]

Step 9: Trigger the Reveal

To trigger the reveal effect, you'll need to call the `RevealCharacter()` method. You can do this in response to a game event, user input, or for testing, you can add this to a UI button:

1. Create a UI Button in your scene.
2. In the Button's Inspector, find the OnClick() section.
3. Drag the VFXController GameObject to the object field.
4. From the function dropdown, select VFXController > RevealCharacter().
![[tut_csharp_vfx_buttonEvent 1.png]]


You've now created a  VFX Controller script that manages both particle effects and character material/shader reveal animations via `DOTWeen`. This script demonstrates how to coordinate and layer multiple visual elements to create a compelling game-based effect.