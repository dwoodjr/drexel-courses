# Unity Lightsaber Builder Tutorial

## Introduction
In this Unity tutorial we will build a procedural lightsaber configuration system. This project will teach you about procedural generation, modular design, and user interface integration in Unity. By the end, you'll have created a dynamic lightsaber builder that allows users to mix and match different parts to create unique lightsabers.

This tutorial is designed for Unity 2022 and assumes basic familiarity with the Unity interface and C# scripting.

## Learning Objectives

1. Understand procedural generation in game development
2. Implement a modular design system
3. Create a user interface for customization
4. Learn about technical art in game development

## Project Setup

1. Create a new 3D Unity project using the Universal RP (SRP) Template in the Unity Hub.
2. In the Project window, within the Assets folder, create the following folders:
	- Scripts
	- Prefabs
	- Materials
3. Create a new scene and name it something meaningful. Save your new scene in the `Scenes` folder.
4. Make sure your code editor of choice in configured and any related packages are updated.
5. Install (if not already existing in the project) and update the following packages. *Package manager is found under Window > Package Manager.*
	- ProBuilder
	- TextMeshPro
	- Unity UI

## Part 1: Creating the LightsaberBuilder Script

Let's start by creating the main script that will handle our lightsaber building logic.

1. In the Scripts folder, right-click and select Create > C# Script. Name it "LightsaberBuilder".
2. Double-click the script to open it in your code editor.
3. Replace the contents with the following code:

```csharp
using UnityEngine;
using UnityEngine.UI;

public class LightsaberBuilder : MonoBehaviour
{
    [Header("Lightsaber Parts Pools")]
    public GameObject[] emitterPrefabs;
    public GameObject[] sleevePrefabs;
    public GameObject[] activationPlatePrefabs;
    public GameObject[] secondSleevePrefabs;
    public GameObject[] pommelPrefabs;

    [Header("UI Sliders")]
    public Slider emitterSlider;
    public Slider sleeveSlider;
    public Slider activationPlateSlider;
    public Slider secondSleeveSlider;
    public Slider pommelSlider;

    [Header("Lightsaber Configuration")]
    public Color bladeColor = Color.green;
    public float bladeLength = 3.0f;
    public float bladeThickness = 0.1f;
    public bool isDoubleBladed;

    // We'll add more code here in the next steps
}
```

This sets up the basic structure of our LightsaberBuilder class. Let's break down what we've done so far:

- We've defined arrays to hold different prefabs for each lightsaber part. These will be our "part pools" from which we'll select components.

> [!note] 
> 	Arrays in C# are denoted with `[]`

- We've added references to UI sliders that we'll use to let the user choose different parts.
- We've included some configuration options for the lightsaber, such as blade color, length, and whether it's double-bladed.

## Part 2: Adding Core Functionality

Now, let's add the core functionality to our LightsaberBuilder script. Add the following private variables and methods:

```csharp
private GameObject currentEmitter;
private GameObject currentSleeve1;
private GameObject currentActivationPlate;
private GameObject currentSleeve2;
private GameObject currentPommel;
private GameObject currentBlade;
private GameObject currentBottomEmitter;
private GameObject currentBottomBlade;

void Start()
{
    emitterSlider.maxValue = emitterPrefabs.Length - 1;
    sleeveSlider.maxValue = sleevePrefabs.Length - 1;
    activationPlateSlider.maxValue = activationPlatePrefabs.Length - 1;
    secondSleeveSlider.maxValue = secondSleevePrefabs.Length - 1;
    pommelSlider.maxValue = pommelPrefabs.Length - 1;

    BuildLightsaber();
}

public void BuildLightsaber()
{
    ClearExistingParts();

    Vector3 currentPosition = transform.position;

    // We'll fill this method in the next step
}

void ClearExistingParts()
{
    if (currentEmitter) Destroy(currentEmitter);
    if (currentSleeve1) Destroy(currentSleeve1);
    if (currentActivationPlate) Destroy(currentActivationPlate);
    if (currentSleeve2) Destroy(currentSleeve2);
    if (currentPommel) Destroy(currentPommel);
    if (currentBlade) Destroy(currentBlade);
    if (currentBottomEmitter) Destroy(currentBottomEmitter);
    if (currentBottomBlade) Destroy(currentBottomBlade);
}

public void OnSliderValueChanged()
{
    BuildLightsaber();
}
```

Here's what we've added:

- Private variables to keep track of the current lightsaber parts.
- A `Start` method that sets up the UI sliders and builds the initial lightsaber.
- A `BuildLightsaber` method (which we'll fill in next) that constructs the lightsaber.
- A `ClearExistingParts` method to remove old parts when rebuilding.
- An `OnSliderValueChanged` method that rebuilds the lightsaber when the user adjusts a slider.

> [!important] 
> 	The `OnSliderValueChnaged` is an important method for allowing real-time control using Unity UI

## Part 3: Implementing the BuildLightsaber Method

Now, let's implement the `BuildLightsaber` method. Replace the empty method with this code:

```csharp
public void BuildLightsaber()
{
    ClearExistingParts();

    Vector3 currentPosition = transform.position;

    // Instantiate and configure the bottom emitter if double-bladed, otherwise instantiate the pommel
    if (isDoubleBladed)
    {
        currentBottomEmitter = Instantiate(emitterPrefabs[(int)emitterSlider.value], currentPosition, Quaternion.identity);
        currentBottomEmitter.transform.parent = transform;
        float bottomEmitterHeight = currentBottomEmitter.GetComponent<Renderer>().bounds.size.y;
        currentPosition += Vector3.up * bottomEmitterHeight;
    }
    else
    {
        currentPommel = Instantiate(pommelPrefabs[(int)pommelSlider.value], currentPosition, Quaternion.identity);
        currentPommel.transform.parent = transform;
        float pommelHeight = currentPommel.GetComponent<Renderer>().bounds.size.y;
        currentPosition += Vector3.up * pommelHeight;
    }

    // Instantiate and configure the second sleeve above the pommel
    currentSleeve2 = Instantiate(secondSleevePrefabs[(int)secondSleeveSlider.value], currentPosition, Quaternion.identity);
    currentSleeve2.transform.parent = transform;
    float sleeve2Height = currentSleeve2.GetComponent<Renderer>().bounds.size.y;
    currentPosition += Vector3.up * (sleeve2Height);

    // Instantiate and configure the activation plate above the second sleeve
    currentActivationPlate = Instantiate(activationPlatePrefabs[(int)activationPlateSlider.value], currentPosition, Quaternion.identity);
    currentActivationPlate.transform.parent = transform;
    float activationPlateHeight = currentActivationPlate.GetComponent<Renderer>().bounds.size.y;
    currentPosition += Vector3.up * (activationPlateHeight/(sleeve2Height));

    // Instantiate and configure the first sleeve above the activation plate
    currentSleeve1 = Instantiate(sleevePrefabs[(int)sleeveSlider.value], currentPosition, Quaternion.identity);
    currentSleeve1.transform.parent = transform;
    float sleeve1Height = currentSleeve1.GetComponent<Renderer>().bounds.size.y;
    currentPosition += Vector3.up * (sleeve1Height);

    // Instantiate and configure the top emitter above the first sleeve
    currentEmitter = Instantiate(emitterPrefabs[(int)emitterSlider.value], currentPosition, Quaternion.identity);
    currentEmitter.transform.parent = transform;
    float emitterHeight = currentEmitter.GetComponent<Renderer>().bounds.size.y;

    // Correct the emitter position
    currentPosition += Vector3.up * ((emitterHeight / 2) - emitterHeight);
    currentEmitter.transform.position = currentPosition;

    // Instantiate and configure the top blade
    currentBlade = InstantiateBlade(currentEmitter.transform, bladeLength);

    if (isDoubleBladed)
    {
        // Instantiate and configure the bottom blade
        currentBottomBlade = InstantiateBlade(currentBottomEmitter.transform, -bladeLength);
    }
}
```

This method does the following:

1. Clears any existing lightsaber parts.
2. Determines whether to start with a bottom emitter (for double-bladed sabers) or a pommel.
3. Instantiates each part of the lightsaber, positioning them vertically.
4. Creates the blade(s) using a helper method we'll define next.

## Part 4: Creating the Blade

Add the following method to create the lightsaber blade:

```csharp
GameObject InstantiateBlade(Transform parent, float bladeHeight)
{
    GameObject blade = GameObject.CreatePrimitive(PrimitiveType.Cylinder);

    // Set the blade as a child of the emitter
    blade.transform.parent = parent;

    // Adjust the blade position so its bottom aligns with the top of the emitter
    blade.transform.localPosition = new Vector3(0, bladeHeight, 0);
    blade.transform.localRotation = Quaternion.identity;
    blade.transform.localScale = new Vector3(bladeThickness, bladeHeight, bladeThickness);

    Renderer bladeRenderer = blade.GetComponent<Renderer>();
    bladeRenderer.material.color = bladeColor;

    return blade;
}
```

This method creates a cylinder primitive for the blade, sets its parent, position, rotation, and scale, and applies the blade color.

## Part 5: Setting Up the Scene

Now that we have our script ready, let's set up the Unity scene:

1. Create an empty GameObject in the Hierarchy and name it "LightsaberBuilder".
2. Add the LightsaberBuilder script to this GameObject.
3. Create UI sliders for each lightsaber part: 
4. In the Hierarchy, right-click and select UI > Slider to create a new UI Canvas, Slider, and Event System. 

> [!important] 
> 	1. The `Canvas` and `Event System` objects are required for the sliders to work with the script. Make sure they are present.

5. Rename the slider to "EmitterSlider". 
6. In the Inspector for the Slider, set the following properties:
    - Min Value: 0
    - Max Value: Leave this at 1 for now (we'll set it programmatically later)
    - Whole Numbers: Check this box 
    - With the Slider selected, in the Inspector, find the "On Value Changed (Single)" event. 
    - Click the + button to add a new event. 
    - Drag the LightsaberBuilder GameObject from the Hierarchy into the object field of this new event. 
    - In the function dropdown, select LightsaberBuilder > OnSliderValueChanged(). 
7. Repeat `Steps 4-6` for "SleeveSlider", "ActivationPlateSlider", "SecondSleeveSlider", and "PommelSlider".

8. Assign the sliders to the corresponding fields in the LightsaberBuilder component: 
	1. Select the LightsaberBuilder GameObject in the Hierarchy. 
	2. In the Inspector, you'll see the LightsaberBuilder component with empty fields for each slider. 
	3. For each slider field (Emitter Slider, Sleeve Slider, etc.), click the circular target icon to the right of the field. 
	4. In the "Select Slider" window that appears, choose the corresponding slider you created (EmitterSlider, SleeveSlider, etc.). 
	5. Repeat this process for all five slider fields.
9. Create prefabs for each lightsaber part using ProBuilder: First, ensure you have the ProBuilder package installed:
    1. Go to Window > Package Manager. Search for "ProBuilder" and click "Install" if it's not already installed.
    2. In the Project window, create a new folder called "Lightsaber Parts" under `Prefabs` folder. 
    3. For each part type (emitter, sleeve, activation plate, second sleeve, pommel), follow these steps: 
        1. Go to Tools > ProBuilder > New Shape 
        2. In the Shape Selector, choose an appropriate basic shape (e.g., Cylinder, Cube, etc.) 
            - It is best for the current system to set the following parameters: **Height: Set between 0.5 and 1.0** (adjust as needed for each part) - Radius (for cylinders): Adjust to get an appropriate thickness - Width and Depth (for cubes): Adjust to get an appropriate size 
        3. Click "Build" to create the shape 
        4. With the new shape selected, go to Tools > ProBuilder > Center Pivot 
        5. In the Inspector, set the Position to (0, 0, 0) to center it on the world origin 
        6. Use ProBuilder tools to modify the shape as desired: - Use the Extrude tool to add details - Use the Bevel tool to soften edges - Use the Insert Edge Loop tool to add more geometry for detailed shaping, etc. 
        7. Once you're happy with the shape, rename it appropriately (e.g., "Emitter_01", "Sleeve_01", etc.) 
        8. Drag the object from the Hierarchy into the "Lightsaber Parts" folder in the Project window to create a prefab 
        9. Delete the object from the Hierarchy after creating the prefab 
    4. Repeat `Step 3` for each variation of each part type, creating multiple prefabs for emitters, sleeves, etc.
10. Assign the prefabs to the LightsaberBuilder component: 
	1. Select the LightsaberBuilder GameObject in the Hierarchy. 
	2. In the Inspector, find the "Lightsaber Parts Pools" section of the LightsaberBuilder component. 
	3. For each array (Emitter Prefabs, Sleeve Prefabs, etc.), set the Size to the number of prefabs you created for that part type. 
	4. Drag the corresponding prefabs from the Project window into the slots in each array.

## Part 6: Testing and Iterating
1. Press Play in the Unity Editor to test your lightsaber builder.
2. Use the sliders to customize the lightsaber and watch it update in real-time.
3. Experiment with different prefabs, blade colors, and configurations.

## Conclusion

Congratulations! You've built a dynamic lightsaber customization system in Unity. This project demonstrates several important concepts in game development:

1. **Procedural Generation**: The lightsaber is built procedurally based on user input, showcasing how games can create content dynamically.
2. **Modular Design**: By breaking the lightsaber into interchangeable parts, we've created a flexible system that can be easily expanded or modified.
3. **User Interface Integration**: The UI sliders allow for real-time customization, illustrating how to connect user input to game systems.
4. **Technical Art**: This project bridges the gap between programming and art. Technical artists in the game industry often create systems like this, allowing for efficient creation and customization of game assets.
5. **Optimization**: By reusing prefabs and dynamically instantiating parts, we've created an efficient system that could be scaled to include many more options without significantly impacting performance.


## Further Challenges

To expand on this project and deepen your understanding of procedural workflows and game design, consider the following additions and challenges:

**Parametric Part Generation**: Instead of using prefabs, create a system that generates lightsaber parts procedurally based on parameters (e.g., length, radius, number of details). This will help you understand how to create infinitely varied assets from a set of rules.
	
> [!hint] Hint
> How is the blade currently constructed? Could you apply a similar approach to other parts? `Unity Primitrive API`


**Modular Attachment System**: Implement a system that allows for attaching additional modules to the lightsaber (e.g., handguards, focusing crystals, power cells). This will teach you about creating flexible, extensible systems in game design.
	
> [!hint] Hint
> Consider creating a base class for attachable modules. How might you define attachment points on your existing parts? Prefabs can have prefabs! `Nested Prefabs`


**Lightsaber Presets** (Random?): Implement a system for loading pre-defined lightsaber configurations. This will help you understand data serialization and how to create and manage presets in a procedural system.
	
> [!hint] Hint
> What data defines a lightsaber configuration? How might you serialize this data? Can this be randomized? `Array Index`


**Part Compatibility System**: Implement a system where certain parts are only compatible with specific other parts. This will teach you about creating rule-based systems and managing complex relationships between procedural elements.
	
> [!hint] Hint
> How might you categorize your parts? Consider using enums or maybe Unity's `Tagging` system, it's pretty good.


**Lightsaber Statistics**: Add a system that calculates various statistics for the lightsaber (e.g., weight, power output, handling) based on the chosen parts. This will help you understand how to derive gameplay-relevant data from procedural systems.
	
> [!hint] Hint
> How might you assign base statistics to each part? Maybe `Scriptable Objects` or simple enums.


**Improved Part Positioning**: Enhance the current positioning system to handle parts of varying sizes more elegantly, ensuring they always connect seamlessly regardless of their dimensions.
	
> [!hint] Hint
> How might you determine the connection points of each part dynamically? Consider using empty GameObjects as markers. `Nested Objects`


**Scalable Part System**: Refactor the code to allow for easy addition of new lightsaber part types without significant code changes. This exercise in extensible design will be valuable for larger procedural systems.
	
> [!hint] Hint
> How might you use inheritance or interfaces to create a more flexible part system? Maybe it works like a `Factory`



> [!NOTE]
> Remember, these challenges are designed to help you think procedurally and improve your design skills. As you work on them, consider how each modification makes the system more flexible, extensible, or capable of generating a wider variety of meaningful content. These skills are crucial in many areas of game development, from procedural level generation to complex character customization systems.
