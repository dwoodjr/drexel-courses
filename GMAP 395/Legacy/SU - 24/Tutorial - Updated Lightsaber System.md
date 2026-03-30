# Lightsaber Customization System - Guide to Updated Code

This guide provides an explanation of each script in the updated lightsaber customization system, how they interconnect, and how the system works as a whole. 
	
> [!attention] A complete system
Remember, the system shown in the guide is a more complete system that takes into consideration several of the `Further Challenges` outlined in the first assignment, and combines them together. You are not expected to make a system this extensive for the assignment. Just pick ONE to try and implement.

## Core Scripts Overview

1. `LightsaberPartSO.cs`: Defines the base ScriptableObject for lightsaber parts.
2. `BladePartSO.cs`: Extends LightsaberPartSO for blade-specific properties.
3. `LightsaberPart.cs`: Base class for all lightsaber parts.
4. `BladePart.cs`: Extends LightsaberPart for blade-specific functionality.
5. `Lightsaber.cs`: Manages the collection of parts that make up a lightsaber.
6. `LightsaberPartFactory.cs`: Factory for creating lightsaber parts.
7. `LightsaberBuilder.cs`: Handles the construction of lightsabers.
8. `LightsaberGenerator.cs`: Orchestrates the lightsaber building process.
9. `LightsaberUIController.cs`: Manages the UI for customizing lightsabers.

*Let's dive into each script and its functionality:*

---
## 1. LightsaberPartSO.cs

**Description:** This script defines the base `ScriptableObject` for all lightsaber parts, providing a foundation for part data management.

```csharp
[CreateAssetMenu(fileName = "New Lightsaber Part", menuName = "Lightsaber/Part")]
public class LightsaberPartSO : ScriptableObject
{
    public PartType type;
    public GameObject partPrefab;
}
```

**Explanation:**
* **CreateAssetMenu Attribute**: Allows creation of LightsaberPartSO instances directly in the Unity Editor.
* **type**: Enum field defining the part's type (e.g., Emitter, Sleeve).

> [!NOTE]
> The complete Enumeration (enum) list is found in `LightsaberPart.cs`. Enums can be defined in their own script file, or that of another script (where it makes sense to have them).

* **partPrefab**: Reference to the GameObject prefab for this part.

**Connections:**
* Used by `LightsaberPartFactory` to create part instances.
* Referenced in `LightsaberGenerator` to define part pools.
* Initialized in `LightsaberPart.Initialize()`.

---
## 2. BladePartSO.cs

**Description:** This script **extends** `LightsaberPartSO` to include blade-specific properties, allowing for specialized blade customization.

```csharp
[CreateAssetMenu(fileName = "New Blade Part", menuName = "Lightsaber/Blade Part")]
public class BladePartSO : LightsaberPartSO
{
    public float defaultLength = 1f;
    public float defaultThickness = 0.1f;
}
```

**Explanation:**
* **Inheritance**: Extends `LightsaberPartSO`, indicating it's a specific type of lightsaber part.

> [!NOTE]
> Anytime you see one script extend or inherit from another, this is a refence to `Inheritence` in programming and often includes `Polymorphism`. This is how most scripts in Unity C# work, think `Monobehavior` and `ScriptableObject` 
[Inheritance vs. Polymorphism](https://www.geeksforgeeks.org/difference-between-inheritance-and-polymorphism/)

* **defaultLength and defaultThickness**: Define the default dimensions of the blade.
* **CreateAssetMenu Attribute**: Adds an option in the Unity Editor to create blade-specific part configurations.

**Connections:**
* Used by `LightsaberGenerator` to create and configure blade parts.
* Initialized in `BladePart.InitializeBlade()`.

---
## 3. LightsaberPart.cs

**Description:** This script defines the base class for all lightsaber parts in the scene, managing part properties and initialization. It also houses the list of enums used to define types of lightsaber parts.

``` c#
public enum PartType  
{  
    Emitter,  
    TopSleeve,  
    BottomSleeve,  
    ActivationSwitch,  
    Blade,  
    Pommel,  
    Guard  
}
```

```csharp
public class LightsaberPart : MonoBehaviour
{
    public PartType Type { get; set; }
    public Transform TopPivot { get; private set; }
    public Transform BottomPivot { get; private set; }
    public List<Transform> SwitchAttachmentPoints { get; private set; } = new List<Transform>();

    public void Initialize(LightsaberPartSO data)
    {
        Type = data.type;
        FindPivots();
        FindAttachmentPoints();
    }

    // ... (other methods)
}
```

**Explanation:**
* **Type Property**: Stores the part's type, set during initialization.
* **Pivot Properties**: Store references to the top and bottom connection points.
* **SwitchAttachmentPoints**: List of points where switches can be attached.
* **Initialize Method**: Sets up the part based on the provided ScriptableObject data.
* **FindPivots and FindAttachmentPoints Methods**: Automatically locate important points on the part's model.

**Connections:**
* Created by `LightsaberPartFactory`.
* Managed by `Lightsaber` class.
* Used by `LightsaberGenerator` for part positioning and assembly.

---
## 4. BladePart.cs

**Description:** This script extends `LightsaberPart` with blade-specific functionality, allowing for dynamic blade customization.

```csharp
public class BladePart : LightsaberPart
{
    public void InitializeBlade(LightsaberPartSO data, float length, float thickness)
    {
        base.Initialize(data);
        Type = PartType.Blade;
        SetDimensions(length, thickness);
    }

    public void SetDimensions(float length, float thickness)
    {
        transform.localScale = new Vector3(thickness, length / 2, thickness);
    }
}
```

**Explanation:**
* **Inheritance**: Extends `LightsaberPart`, adding blade-specific functionality.

> [!NOTE]
> The reason we extend `LightsaberPart` is that the blade is still a part of the lightsaber so it has **shared properties**. But the blade also has its own **unique properties** associated with it. Identifying shared and unique properties is important in modular and procedural design!

* **InitializeBlade Method**: Initializes the blade with custom dimensions.
* **SetDimensions Method**: Adjusts the blade's scale based on provided length and thickness.

**Connections:**
* Created by `LightsaberGenerator` when adding blades to the lightsaber.
* Managed alongside other parts in the `Lightsaber` class.

---
## 5. Lightsaber.cs

**Description:** This script manages the collection of parts that make up a lightsaber, providing methods for part management. Essentially, this class defines what a lightsaber ***is*** through it's parts and parameters.

```csharp
public class Lightsaber : MonoBehaviour
{
    private Dictionary<PartType, List<LightsaberPart>> parts = new Dictionary<PartType, List<LightsaberPart>>();

    public void AddOrReplacePart(LightsaberPart part)
    {
        if (!parts.ContainsKey(part.Type))
        {
            parts[part.Type] = new List<LightsaberPart>();
        }
        parts[part.Type].Add(part);
    }

    public void RemovePart(LightsaberPart part)
    {
        if (parts.ContainsKey(part.Type))
        {
            parts[part.Type].Remove(part);
            if (parts[part.Type].Count == 0)
            {
                parts.Remove(part.Type);
            }
            Destroy(part.gameObject);
        }
    }

    public LightsaberPart GetPart(PartType type)
    {
        return parts.ContainsKey(type) && parts[type].Count > 0 ? parts[type][0] : null;
    }

    public IEnumerable<LightsaberPart> GetAllParts()
    {
        return parts.Values.SelectMany(list => list);
    }
}
```

**Explanation:**
* **parts Dictionary**: Stores all parts of the lightsaber, organized by type.
* **AddOrReplacePart Method**: Adds a new part or replaces an existing one.
* **RemovePart Method**: Removes a part from the lightsaber and destroys its GameObject.
* **GetPart Method**: Retrieves a part of a specific type.
* **GetAllParts Method**: Returns all parts of the lightsaber.

**Connections:**
* Created by `LightsaberBuilder`.
* Used by `LightsaberGenerator` to manage the lightsaber's composition.
* Interacts with `LightsaberPart` instances.

---
## 6. LightsaberPartFactory.cs

**Description:** This factory class is responsible for creating lightsaber parts, centralizing the part creation process.

```csharp
public class LightsaberPartFactory
{
    public LightsaberPart CreatePart(LightsaberPartSO partData)
    {
        GameObject partObject = Object.Instantiate(partData.partPrefab);
        LightsaberPart part = partObject.AddComponent<LightsaberPart>();
        part.Initialize(partData);
        return part;
    }
}
```

**Explanation:**
* **CreatePart Method**: Creates a new LightsaberPart instance based on the provided ScriptableObject data.
* **Instantiation**: Uses Unity's Object.Instantiate to create a new GameObject from the prefab. Placing it in game space.
* **Component Addition**: Adds the LightsaberPart component to the instantiated object.
* **Initialization**: Calls the Initialize method on the newly created part.

**Connections:**
* Used by `LightsaberBuilder` to create part instances.
* Creates `LightsaberPart` instances.
* Uses `LightsaberPartSO` data for part creation.

---
## 7. LightsaberBuilder.cs

**Description:** This class implements the builder pattern for step-by-step lightsaber construction.

```csharp
public class LightsaberBuilder
{
    private GameObject _lightsaberObject;
    private LightsaberPartFactory _factory;
    private Dictionary<PartType, LightsaberPart> _currentParts = new Dictionary<PartType, LightsaberPart>();

    public LightsaberBuilder(LightsaberPartFactory factory, Transform parent)
    {
        _factory = factory;
        _lightsaberObject = new GameObject("Lightsaber");
        _lightsaberObject.transform.SetParent(parent);
    }

    public LightsaberBuilder AddPart(LightsaberPartSO partData, bool flipPart = false)
    {
        LightsaberPart part = _factory.CreatePart(partData);
        part.transform.SetParent(_lightsaberObject.transform);

        if (flipPart)
        {
            part.transform.localRotation = Quaternion.Euler(0, 0, 180);
        }

        if (_currentParts.ContainsKey(part.Type))
        {
            Object.Destroy(_currentParts[part.Type].gameObject);
        }
        _currentParts[part.Type] = part;

        return this;
    }

    public LightsaberBuilder AddBlade(float length, float thickness, Color color)
    {
        GameObject blade = GameObject.CreatePrimitive(PrimitiveType.Cylinder);
        blade.transform.SetParent(_lightsaberObject.transform);
        blade.transform.localScale = new Vector3(thickness, length / 2, thickness);
        blade.GetComponent<Renderer>().material.color = color;

        return this;
    }

    public Lightsaber Build()
    {
        Lightsaber lightsaber = _lightsaberObject.AddComponent<Lightsaber>();
        foreach (var part in _currentParts)
        {
            lightsaber.AddOrReplacePart(part.Value);
        }
        return lightsaber;
    }
}
```

**Explanation:**
* **Builder Pattern**: Implements a step-by-step construction process for lightsabers.
* **LightsaberPartFactory**: Uses a factory to create part instances.

> [!NOTE] On Factories and Builders
> When using a `Factory Pattern` or `Builder Pattern`, especially in more complex systems, it is common to see both patterns used together. Although this is not explicitly required.

* **AddPart Method**: Adds a new part to the lightsaber, replacing any existing part of the same type.
* **AddBlade Method**: Creates a custom blade based on provided parameters.
* **Build Method**: Finalizes the lightsaber construction, creating a Lightsaber component.

**Connections:**
* Used by `LightsaberGenerator` to construct lightsabers.
* Interacts with `LightsaberPartFactory` to create parts.
* Creates and configures `Lightsaber` instances.

---
## 8. LightsaberGenerator.cs

**Description:** This script orchestrates the entire lightsaber building process, managing part pools and handling updates. It could be though of as a `Director` or `GameManager`.

```csharp
public class LightsaberGenerator : MonoBehaviour
{
    [Header("Lightsaber Parts Pools")]
    public LightsaberPartSO[] emitterParts;
    public LightsaberPartSO[] topSleeveParts;
    public LightsaberPartSO[] activationSwitchParts;
    public LightsaberPartSO[] bottomSleeveParts;
    public LightsaberPartSO[] pommelParts;
    public LightsaberPartSO[] guardParts;

    [Header("Blade Configuration")]
    public BladePartSO bladePart;
    public Color bladeColor = Color.green;
    public float bladeLength = 3.0f;
    public float bladeThickness = 0.1f;

    private Lightsaber currentLightsaber;
    private LightsaberPartFactory factory;

    public void BuildLightsaber()
    {
        // Implementation
    }

    public void UpdatePart(PartType partType, int index)
    {
        // Implementation
    }

    private void SnapPartsTogether()
    {
        // Implementation
    }

    // ... (other methods)
}
```

**Explanation:**
* **Part Pools**: Arrays of ScriptableObjects for each part type, allowing for easy part selection.
* **Blade Configuration**: Properties for customizing the lightsaber blade.
* **BuildLightsaber Method**: Orchestrates the lightsaber construction process.
* **UpdatePart Method**: Handles updating individual parts of the lightsaber.
* **SnapPartsTogether Method**: Ensures proper positioning and alignment of parts.

**Connections:**
* Uses `LightsaberBuilder` to construct lightsabers.
* Interacts with `Lightsaber` to manage the current lightsaber instance.
* References `LightsaberPartSO` and `BladePartSO` for part data.
* Used by `LightsaberUIController` to handle user interactions.

---
## 9. LightsaberUIController.cs

**Description:** This script manages the UI for customizing lightsabers, connecting user inputs to the LightsaberGenerator.

> [!NOTE] UI GameManager
> This class is an example of a fairly common game manager type found in game design, explicitly handling `User Interfaces (UI)` or more specifically `Graphical User Interfaces (GUI)`


```csharp
public class LightsaberUIController : MonoBehaviour
{
    public LightsaberGenerator lightsaberGenerator;
    public Slider emitterSlider;
    public Slider topSleeveSlider;
    public Slider activationSwitchSlider;
    public Slider bottomSleeveSlider;
    public Slider pommelSlider;
    public Slider guardSlider;
    public Button finalizeButton;

    private void Start()
    {
        lightsaberGenerator.BuildLightsaber();

        emitterSlider.onValueChanged.AddListener(OnEmitterSliderChanged);
        // ... (other slider listeners)
        finalizeButton.onClick.AddListener(OnFinalizeButtonClicked);

        // Set max values for sliders
        emitterSlider.maxValue = lightsaberGenerator.emitterParts.Length - 1;
        // ... (set other slider max values)
    }

    private void OnEmitterSliderChanged(float value)
    {
        lightsaberGenerator.UpdatePart(PartType.Emitter, Mathf.RoundToInt(value));
    }

    // ... (other UI event handlers)

    private void OnFinalizeButtonClicked()
    {
        lightsaberGenerator.FinalizeLightsaber();
    }
}
```

**Explanation:**
* **UI Elements**: References to sliders and buttons for part selection and customization.
* **Start Method**: Sets up initial lightsaber and configures UI elements.
* **Slider Event Handlers**: Methods that respond to slider value changes, updating the lightsaber parts.
* **Finalize Button**: Triggers the finalization of the lightsaber customization.

**Connections:**
* Interacts directly with `LightsaberGenerator` to build and update the lightsaber.
* Provides the user interface for lightsaber customization.

---

## How the Entire System Works Together

1. **Initialization:**
   * `LightsaberUIController` starts the process by calling `BuildLightsaber()` on the `LightsaberGenerator`.
   * `LightsaberGenerator` uses `LightsaberBuilder` to construct the initial lightsaber.

2. **Part Creation:**
   * `LightsaberBuilder` uses `LightsaberPartFactory` to create individual parts.
   * `LightsaberPartFactory` instantiates `LightsaberPart` components based on `LightsaberPartSO` data.

3. **Lightsaber Assembly:**
   * `LightsaberBuilder` adds created parts to a new GameObject, which will become the complete lightsaber.
   * The `Build()` method of `LightsaberBuilder` creates a `Lightsaber` component on this GameObject, which manages all the parts.

4. **Part Management:**
   * The `Lightsaber` class maintains a dictionary of all parts, organized by their `PartType`.
   * It provides methods to add, remove, and retrieve parts, which are used throughout the customization process.

5. **User Interaction:**
   * `LightsaberUIController` listens for changes in UI elements (e.g., sliders).
   * When a change occurs, it calls the appropriate method on `LightsaberGenerator` to update the corresponding part.

6. **Part Updates:**
   * `LightsaberGenerator.UpdatePart()` method is called when a user changes a part.
   * This method removes the existing part of the specified type and adds a new one based on the user's selection.

7. **Blade Customization:**
   * Blade parts are handled slightly differently, using the `BladePart` class which extends `LightsaberPart`.
   * `BladePartSO` provides blade-specific data like default length and thickness.
   * The `LightsaberGenerator` uses this data to create and customize blade parts.

8. **Part Positioning:**
   * After updates, `LightsaberGenerator` calls `SnapPartsTogether()` to ensure all parts are correctly positioned.
   * This method uses the `TopPivot` and `BottomPivot` properties of each `LightsaberPart` to align them properly.

9. **Finalization:**
   * When the user is satisfied with their design, they can click the finalize button.
   * This triggers `LightsaberGenerator.FinalizeLightsaber()`, which ***could*** perform any final adjustments or save the configuration. although this feature is not fully functional, yet.

10. **Extensibility:**
    * The system is designed to be easily extensible. New part types can be added by:
      - Creating a new `PartType` enum value
      - Adding corresponding `LightsaberPartSO` assets
      - Updating `LightsaberGenerator` to include the new part type
    * The use of ScriptableObjects (`LightsaberPartSO`) allows for easy creation and management of new part variations without changing code.

This system demonstrates several key design principles for modular and procedural game design system:

- **Modularity**: Each script has a specific role, making the system easy to understand and modify.
- **Extensibility**: New part types and variations can be added with minimal changes to existing code.
- **Separation of Concerns**: UI, data management, and object creation are handled by separate components.
- **Use of Design Patterns**: The Builder pattern (LightsaberBuilder) and Factory pattern (LightsaberPartFactory) are employed to manage complex object creation.

By understanding how these components interact, you can extend the system to meet additional requirements, such as implementing parametric part generation, a modular attachment system, or a part compatibility system as outlined in the assignment challenges for Assignment `1 - Procedural Game Art`.