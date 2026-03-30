# Unity Material Instancing Guide - `C#`

## Introduction

In this guide, you'll learn how to create and modify material instances in Unity using C# scripting. We'll start with a basic color change and then extend our script to handle textures and UV offsets. This guide assumes you have followed the [[GMAP 395 - SU24 - In-Class Lab - HLSL in Unity]]

📘 **What is Material Instancing?**

Material instancing allows you to create unique variations of a material for individual objects without creating entirely new materials. This can be more memory-efficient than creating separate materials for each object. However, in most SRP workflows, multiple materials with a shared shader are okay, as the SRP Batcher batches based on shader not material.

## Part 1: Basic Material Instancing for Color

Let's start with a simple script that creates a material instance and changes its color.

```csharp
using UnityEngine;

public class MaterialInstancing : MonoBehaviour
{
    [SerializeField] private Material sourceMaterial;
    [SerializeField] private Color color = Color.white;

    private Material instancedMaterial;

    private void Start()
    {
        // Create a new instance of the material
        instancedMaterial = new Material(sourceMaterial);
        
        // Set the color of the instanced material
        instancedMaterial.color = color;

        // Apply the instanced material to the renderer
        Renderer renderer = GetComponent<Renderer>();
        renderer.material = instancedMaterial;
    }

    private void OnValidate()
    {
        // Update the material color in the editor
        if (instancedMaterial != null)
        {
            instancedMaterial.color = color;
        }
    }

    private void OnDestroy()
    {
        // Clean up the instanced material when the object is destroyed
        if (instancedMaterial != null)
        {
            if (Application.isPlaying)
            {
                Destroy(instancedMaterial);
            }
            else
            {
                DestroyImmediate(instancedMaterial);
            }
        }
    }
}
```

> 🟢 **Script Breakdown**
> 
> - `Start()`: Creates the material instance and applies it to the object.
> - `OnValidate()`: Updates the material in the Unity Editor when you change values.
> - `OnDestroy()`: Cleans up the material instance to prevent memory leaks.

### How to Use This Script

1. Create a new C# script in your Unity project and name it `MaterialInstancing`.
2. Copy and paste the above code into the script.
3. Attach this script to any GameObject that has a Renderer component.
4. In the Inspector, assign the source material to the "Source Material" field.
5. Adjust the "Color" field in the Inspector to set a unique color for this instance.

> 💡 **Tip**: Make sure your shader supports changing the main color property for this to work!

## Part 2: Extending the Script for Textures and Custom UV Properties

Now, let's modify our script to handle textures and custom UV properties that match our shader.

```csharp
using UnityEngine;

public class MaterialInstancing : MonoBehaviour
{
    [SerializeField] private Material sourceMaterial;
    [SerializeField] private Color color = Color.white;
    [SerializeField] private Texture mainTexture;
    [SerializeField] private Vector2 offset = Vector2.zero;
    [SerializeField] private Vector2 tiling = Vector2.one;

    private Material instancedMaterial;

    private void Start()
    {
        CreateMaterialInstance();
        UpdateMaterialProperties();
    }

    private void CreateMaterialInstance()
    {
        instancedMaterial = new Material(sourceMaterial);
        GetComponent<Renderer>().material = instancedMaterial;
    }

    private void UpdateMaterialProperties()
    {
        if (instancedMaterial != null)
        {
            instancedMaterial.SetColor("_Color", color);
            
            if (mainTexture != null)
            {
                instancedMaterial.SetTexture("_MainTex", mainTexture);
            }

            instancedMaterial.SetFloat("_TilingX", tiling.x);
            instancedMaterial.SetFloat("_TilingY", tiling.y);
            instancedMaterial.SetFloat("_OffsetX", offset.x);
            instancedMaterial.SetFloat("_OffsetY", offset.y);
        }
    }

    private void OnValidate()
    {
        if (instancedMaterial == null && Application.isPlaying)
        {
            CreateMaterialInstance();
        }
        UpdateMaterialProperties();
    }

    private void OnDestroy()
    {
        if (instancedMaterial != null)
        {
            if (Application.isPlaying)
            {
                Destroy(instancedMaterial);
            }
            else
            {
                DestroyImmediate(instancedMaterial);
            }
        }
    }
}
```

> 🔍 **Key Changes**
> 
> - We now use `SetColor`, `SetTexture`, and `SetFloat` methods to directly set shader properties.
> - Property names (e.g., `"_Color"`, `"_MainTex"`, `"_TilingX"`) match those defined in the shader.
> - Tiling and offset are set as individual float values to match custom shader properties.

### How to Use the Advanced Script

1. Replace your existing `MaterialInstancing` script code with this new updated`MaterialInstancing` script.
2. Ensure your shader has matching property names for color, texture, tiling, and offset.
3. In the Inspector, you'll see fields for Color, Texture, Offset, and Tiling.
4. Adjust these values to control the appearance of your instanced material.

> ⚠️ **Important**: Your shader must have properties that match the names used in this script (`_Color`, `_MainTex`, `_TilingX`, `_TilingY`, `_OffsetX`, `_OffsetY`). Here's an example of how your shader properties might look:

```glsl
Properties
{
    _Color ("Color", Color) = (1,1,1,1)
    _MainTex ("Texture", 2D) = "white" {}
    _TilingX ("Tiling X", Float) = 1
    _TilingY ("Tiling Y", Float) = 1
    _OffsetX ("Offset X", Float) = 0
    _OffsetY ("Offset Y", Float) = 0
}
```

## Tips for Working with Custom Shader Properties

1. **Property Naming**: Ensure the property names in your C# script exactly match those in your shader.
2. **Shader Compatibility**: This script assumes a custom shader with specific properties. Modify the property names if your shader uses different ones.
3. **Editor Updates**: The `OnValidate` method ensures properties update in real-time in the Unity editor.

## Conclusion
You've now learned how to create and modify material instances in Unity, controlling color, texture, and UV properties. This technique allows for great flexibility in creating varied appearances for objects in your scene.

> 🚀 **Next Steps**
> 
> - Experiment with modifying other material properties like metallic, smoothness, or emission.
> - Try creating a system that randomly assigns properties to create varied instances automatically.