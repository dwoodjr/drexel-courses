# Student Guide: Understanding the ForceFieldController Script

This guide will break down the `ForceFieldController` script, explaining its key components and how it works to control our force field shader.

## Script Overview

The `ForceFieldController` script is designed to:
1. Control the force field shader parameters
2. Simulate damage effects
3. Use [DOTween](https://assetstore.unity.com/packages/tools/animation/dotween-hotween-v2-27676) for smooth animations
	1. To use this code, DOTween needs to be installed and set up.

## Key Components

### 1. Namespaces and Class Declaration

```csharp
using UnityEngine;
using UnityEngine.UI;
using DG.Tweening;

public class ForceFieldController : MonoBehaviour
{
    // ... (rest of the code)
}
```

- `UnityEngine`: Gives access to Unity's core functionality
- `UnityEngine.UI`: Needed for working with UI elements (like our button)
- `DG.Tweening`: This is the DOTween library, used for smooth animations

### 2. Public Variables

```csharp
public Material forceFieldMaterial;
public Button damageButton;

[Header("Shader Properties")]
public float baseIntensity = 1f;
public float damageIntensitySpike = 2f;
public float basePatternSpeed = 1f;
public float damagePatternSpeed = 3f;
public Color baseRimColor = Color.white;
public Color damageRimColor = Color.red;

[Header("Animation Settings")]
public float damageDuration = 0.5f;
public float recoverDuration = 1f;
```

These variables are accessible in the Unity Inspector, allowing easy adjustment:
- `forceFieldMaterial`: Reference to the material using our shader
- `damageButton`: Reference to the UI button that triggers the damage effect
- Shader property variables: Control various aspects of the force field's appearance
- Animation settings: Control the duration of damage and recovery animations

### 3. Shader Property IDs

```csharp
private static readonly int IntensityProperty = Shader.PropertyToID("_Intensity");
private static readonly int PatternSpeedProperty = Shader.PropertyToID("_PatternSpeed");
private static readonly int RimColorProperty = Shader.PropertyToID("_RimColor");
```

These lines create efficient references to shader properties. Using `PropertyToID` is faster than using string names directly. 

> [!attention] 
> The property `Reference/ID` names need to match with the Shader/Shader Graph exactly.

### 4. Start Method

```csharp
private void Start()
{
    if (damageButton != null)
    {
        damageButton.onClick.AddListener(SimulateDamage);
    }
}
```

This method runs when the script starts. It adds a listener to the damage button, so when clicked, it calls the `SimulateDamage` method. Listeners are common for an UI event or element being referenced in C# code.

### 5. SimulateDamage Method

```csharp
public void SimulateDamage()
{
    // Intensity spike
    DOTween.To(() => forceFieldMaterial.GetFloat(IntensityProperty),
        value => forceFieldMaterial.SetFloat(IntensityProperty, value),
        damageIntensitySpike, damageDuration)
        .SetEase(Ease.OutQuad)
        .OnComplete(() => RecoverIntensity());

    // Pattern speed increase
    // ... (similar structure for pattern speed)

    // Rim color change
    // ... (similar structure for rim color)
}
```

This method is called when the damage button is clicked. For each shader property (intensity, pattern speed, rim color):
1. It uses DOTween to smoothly change the property's value
2. The animation goes from the current value to the "damage" value

> [!NOTE]
> `DOTween.To` One value goes TO another value

3. It uses an "ease out" animation curve for a snappy effect
4. When the animation completes, it calls a recovery method

### 6. Recovery Methods

```csharp
private void RecoverIntensity()
{
    DOTween.To(() => forceFieldMaterial.GetFloat(IntensityProperty),
        value => forceFieldMaterial.SetFloat(IntensityProperty, value),
        baseIntensity, recoverDuration)
        .SetEase(Ease.InOutQuad);
}

// ... (similar methods for RecoverPatternSpeed and RecoverRimColor)
```

These methods are called after the damage effect to return the shader properties to their base values:
1. They use DOTween to smoothly animate the property back to its original value
2. The animation uses an "ease in-out" curve for a smooth transition

## How It All Works Together

1. When the script starts, it sets up the damage button to trigger the `SimulateDamage` method when clicked.
2. Clicking the button calls `SimulateDamage`, which:
   - Increases the shader's intensity
   - Speeds up the pattern movement
   - Changes the rim color to the damage color
3. Each of these changes is animated smoothly using DOTween.
4. After each damage animation completes, a corresponding recovery method is called.
5. The recovery methods smoothly transition the shader properties back to their original values.


## How to Use the ForceFieldController Script in Unity

Follow these steps to set up and use the ForceFieldController script in your Unity project:

### Step 1: Prepare Your Scene

1. Ensure you have a 3D object in your scene that will represent your force field (e.g., a sphere or custom mesh).
2. Make sure this object has a MeshRenderer component with your force field material applied.

### Step 2: Add the Script to Your Force Field Object

1. Select your force field object in the Hierarchy window.
2. In the Inspector, click "Add Component".
3. Search for "Force Field Controller" and select it to add the script.

### Step 3: Set Up the Script References

1. With your force field object selected, look at the Force Field Controller component in the Inspector.
2. Drag your force field material from the Project window into the "Force Field Material" field in the script component. Or select it using the little target search function.

### Step 4: Create a UI Button for Testing

1. Right-click in the Hierarchy, select UI > Button to create a new button.
2. Position the button where you want it in the Game view.
3. (Optional) Change the button text to "Simulate Damage" for clarity.

### Step 5: Connect the UI Button to the Script

1. In the Force Field Controller component, find the "Damage Button" field.
2. Drag the Button object from your Hierarchy into this field.

### Step 6: Adjust Script Parameters

In the Force Field Controller component, you'll see several editable fields:

1. Under "Shader Properties":
   - Adjust Base/Damage Intensity to control the force field's glow strength.
   - Modify Base/Damage Pattern Speed to change how fast the texture animates.
   - Set Base/Damage Rim Color to define the force field's edge colors.

2. Under "Animation Settings":
   - Adjust Damage Duration to control how long the damage effect lasts.
   - Change Recover Duration to set how long it takes to return to normal.

### Step 7: Test Your Force Field

1. Enter Play Mode in Unity.
2. Click the "Simulate Damage" button you created.
3. Watch your force field react with increased intensity, faster pattern movement, and color change.
4. Observe it smoothly return to its base state.

### Step 8: Iterate and Refine

1. Exit Play Mode and adjust the parameters in the Inspector.
2. Experiment with different values to achieve your desired effect.
3. Remember, changes made in Play Mode aren't saved, so make your final adjustments in Edit Mode.

### Troubleshooting Tips

- If the effect doesn't work, ensure all fields in the script component are properly assigned.
- Check that your shader has properties named exactly `_Intensity`, `_PatternSpeed`, and `_RimColor`.
- If using a custom mesh, make sure its UV mapping is suitable for your texture animation.