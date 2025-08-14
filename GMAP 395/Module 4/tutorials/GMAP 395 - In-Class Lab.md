# In-Class Lab: Introduction to Cinemachine in Unity URP

## Objective
This lab aims to guide you through setting up **Cinemachine** in Unity's Universal Render Pipeline (URP), understanding its core components, and implementing dynamic camera controls

## Prerequisites
- Unity 2022.3 LTS or late 
- Basic familiarity with the Unity interface

---  

## Part 1: Setting Up the Unity Project

### Step 1: Create a New URP Project
1. **Open Unity Hub**: Launch the Unity Hub application
2. **Create a New Project**: Click on the **"New Project"** button
3. **Select URP Template**: Choose the **"3D (URP)"** template
4. **Name and Location**: Enter a project name (e.g., "CinemachineIntro") 
	1. Select a location to save the project
5. **Create**: - Click **"Create Project"**

---  

## Part 2: Installing Cinemachine

### Step 1: Open the Package Manager
1. **Access Package Manager**: 
	1. In Unity, navigate to **Window > Package Manager**

### Step 2: Install Cinemachine
1. **Find Cinemachine**: 
	1. In the Package Manager, ensure **"Unity Registry"** is selected in the dropdown 
	2. Scroll to locate **"Cinemachine"** or use the search bar
2. **Install**:
	1. Select **"Cinemachine"** and click the **"Install"** button

---  

## Part 3: Understanding Cinemachine Components

### Cinemachine Overview
Cinemachine is a powerful Unity package that simplifies camera control, allowing for dynamic and complex camera behaviors without extensive coding

### Key Components
1. **`Cinemachine Brain`**:
    -  **Function**: Acts as the link between Unity's main camera and Cinemachine's virtual cameras. It interprets and blends the instructions from virtual cameras to control the main camera's behavior
    -  **Usage**: Attached to the **Main Camera**
2. **`Cinemachine Virtual Camera`**:
    -  **Function**: Defines specific camera behaviors, such as position, rotation, and follow targets. Unlike the main camera, virtual cameras don't render scenes but provide instructions to the Cinemachine Brain
    -  **Usage**: Multiple virtual cameras can be created to achieve various cinematic effects, like cutscenes or dynamic following

---  

## Part 4: Setting Up Cinemachine in the Scene

### Step 1: Add Cinemachine Brain to Main Camera
1. **Select Main Camera**: In the **Hierarchy** window, click on the **"Main Camera"**
2. **Add Cinemachine Brain**: In the **Inspector** window, click **"Add Component"** - Search for **"Cinemachine Brain"** and select it

*Note*: If you star by just creating a Virtual Camera (Right-Click -> Cinemachine -> Virtual Camera) a brain will automatically be added to the scene Main Camera.

### Step 2: Create a Cinemachine Virtual Camera
1. **Add Virtual Camera**: In the **Menu Bar**, navigate to **Cinemachine > Create Virtual Camera**
2. **Configure Virtual Camera**: A new GameObject named **"Virtual Camera"** appears in the **Hierarchy** 
	1. Select it
	2. In the **Inspector** window, you'll see the **CinemachineVirtualCamera** component

---  

## Part 5: Configuring the Virtual Camera

### Step 1: Set Up the Scene
1. **Create a Target Object**:
	1. In the **Hierarchy**, create a **Cube** (`Right- click > 3D Object > Cube`)
	2. Position it at **(0, 0.5, 0)**

### Step 2: Configure Virtual Camera to Follow the Target
1. **Assign Follow and Look At Targets**: 
	1. Select your **"Virtual Camera"** 
	2. In the **Inspector**, set the **"Follow"** and **"Look At"** fields to the **Cube** (drag the Cube from the Hierarchy to these fields)
2. **Adjust Camera Settings**: 
3. Modify the **"Lens"** settings, such as **Field of View**, to achieve the desired framing 
	1. Under **"Aim"**, explore options like **Composer** to fine-tune how the camera tracks the target

---  

## Part 6: Testing the Setup
1. **Play the Scene**:
	1. Click the **"Play"** button to enter Play Mode
	2. Observe how the virtual camera follows and looks at the Cube
2. **Move the Target**:
3. While in Play Mode, select the Cube and move it around (or create a script to animate it)
	1. Notice how the camera dynamically adjusts to keep the Cube in view


---  

## Part 7: Transitioning Between Multiple Virtual Cameras
Cinemachine allows seamless transitions between multiple virtual cameras, enabling dynamic and cinematic camera movements in your scene.

### Step 1: Create Additional Virtual Cameras
1. **Add a Second Virtual Camera**:
    -  Navigate to **Cinemachine > Create Virtual Camera**.
    -  A new GameObject named **"Virtual Camera (1)"** will appear in the **Hierarchy**.
2. **Configure the Second Virtual Camera**:
    -  Select **"Virtual Camera (1)"**.
    -  In the **Inspector**, set the **"Follow"** and **"Look At"** fields to a different target or adjust its **Transform** to a new position.
    -  For example, create another **Cube** at a different location and assign it as the target.

### Step 2: Control Camera Transitions
Cinemachine manages transitions between virtual cameras based on their **Priority** and **Activation**.

1. **Set Camera Priorities**:
    -  Each virtual camera has a **Priority** property. The camera with the highest priority becomes active.
    -  To switch cameras, adjust their priorities accordingly.
2. **Activate/Deactivate Cameras via Script**:
    -  You can enable or disable virtual cameras through C# scripts to control transitions.
    -  For example, to switch to **"Virtual Camera (1)"** when pressing a number key:
    
    ```csharp
using UnityEngine;
using Cinemachine;

public class CameraSwitcher : MonoBehaviour
{
    public CinemachineVirtualCamera vcam1;
    public CinemachineVirtualCamera vcam2;

    void Start()
    {
        ActivateCamera(vcam1); // Start with vcam1 active by default
    }

    void Update()
    {
        if (Input.GetKeyDown(KeyCode.Alpha1))
        {
            ActivateCamera(vcam1);
        }

        if (Input.GetKeyDown(KeyCode.Alpha2))
        {
            ActivateCamera(vcam2);
        }
    }

    void ActivateCamera(CinemachineVirtualCamera activeCam)
    {
        vcam1.gameObject.SetActive(activeCam == vcam1);
        vcam2.gameObject.SetActive(activeCam == vcam2);
    }
}
    ```
    
    -  Attach this script to an empty GameObject and assign **Virtual Camera1** and **Virtual Camera2** in the **Inspector**.
### How this works:
- Press **1** → activates `Virtual Camera1`.
- Press **2** → activates `Virtual Camera2`.
- Deactivates the other camera automatically.
- Starts with `Virtual Camera1` active by default in `Start()`.

1. **Customize Transition Blends**:
    -  Cinemachine allows customization of the blending between cameras.
    -  Select the **Main Camera** and, in the **Cinemachine Brain** component, adjust the **Default Blend** settings to control the transition style and duration.

---  

## Part 8: Utilizing Cinemachine's Advanced Features
Cinemachine offers advanced functionalities to enhance camera behavior.

### Step 1: Implementing Camera Noise for Shake Effects
1. **Add Noise to a Virtual Camera**:
    -  Select a virtual camera (e.g., **"Virtual Camera"**).
    -  In the **Inspector**, expand the **"Noise"** section.
    -  Choose a **Noise Profile** (e.g., **Basic Multi Perlin**) to add procedural camera shake.
2. **Adjust Noise Parameters**:
    -  Modify the **Amplitude Gain** and **Frequency Gain** to control the intensity and speed of the shake effect.

---  

## Part 9: Finalizing and Testing the Camera Setup
1. **Play the Scene**:
    - Click the **"Play"** button to enter Play Mode.
    - Interact with your scene and observe the camera behaviors, transitions, and effects implemented.
2. **Refine Camera Settings**:
    - Based on the playtest, tweak virtual camera settings, noise profiles, and transition blends to achieve the desired cinematic experience.


> [!info]
> By following this comprehensive tutorial, you've learned how to set up and utilize Cinemachine in Unity to create dynamic and professional camera systems for your projects.

For a visual walkthrough and more advanced techniques, consider watching the following tutorial:
<iframe width="532" height="299" src="https://www.youtube.com/embed/asruvbmUyw8" title="How to use Cameras in Unity: Cinemachine Virtual Cameras Explained" frameborder="0" allow="accelerometer; autoplay; clipboard- write; encrypted- media; gyroscope; picture- in- picture; web- share" referrerpolicy="strict- origin- when- cross- origin" allowfullscreen></iframe>

Video: How to use Cameras in Unity: Cinemachine Virtual Cameras

--- 
--- 

# In-Class Lab: Enhancing Visuals with Post- Processing in Unity URP

## Objective
This lab aims to introduce you to **post- processing** in Unity's Universal Render Pipeline (URP), enabling you to enhance your game's visual quality by applying various effects


## Part 1: Configuring Post- Processing in URP
URP integrates post- processing effects using the Volume framework. Follow these steps to set it up

### Step 1: Enable Post- Processing on the Camera
1. **Select the Main Camera**:
	1. In the **Hierarchy**, click on **"Main Camera"**
2. **Enable Post- Processing**:
	2. In the **Inspector** under **Rendering**, check the **Post Processing** box

### Step 2: Create a Global Volume for Post- Processing
1. **Add a Global Volume**: 
	1. In the **Hierarchy**, right- click and select **Volume > Global Volume**
2. **Create a Volume Profile**:
	2. With the **Global Volume** selected, click **"Add Component"** in the **Inspector** 
	3. Choose **"Volume"** - Click **"New"** next to the **Profile** field to create a new Volume Profile

--- 

## Part 2: Adding Post- Processing Effects

Now that the Volume is set up, let's add some common post- processing effects

### Step 1: Add a Bloom Effect
1. **Add Bloom**: 
	1. In the **Inspector** of the **Global Volume**, click **"Add Override"**
	2. Select **"Post- processing" > "Bloom"**
2. **Configure Bloom**: 
	1. Enable the **Intensity** property by checking its box and set it to **0.5** 
	2. Adjust the **Threshold** to control the brightness level at which Bloom starts

### Step 2: Add a Vignette Effect
1. **Add Vignette**: 
	1. Click **"Add Override"** again 
	2. Select **"Post- processing" > "Vignette"**
2. **Configure Vignette**: 
	1. Enable the **Intensity** property and set it to **0.3**
	2. Adjust the **Smoothness** to **0.5** for a subtle darkening around the edges

### Step 3: Add Color Adjustments
1. **Add Color Adjustments**: 
	1. Click **"Add Override"** 
	2. Select **"Post- processing" > "Color Adjustments"**
2. **Configure Color Adjustments**: 
	1. Enable the **Post Exposure** property and set it to **0.5** to brighten the scene 
	2. Adjust the **Contrast** to **10** for more depth 
	3. Modify the **Saturation** to **- 10** for a slight desaturation effect

--- 

## Part 3: Observing the Effects

After adding these effects, you should notice changes in your scene
- **Bloom**: Bright areas emit a soft glow
- **Vignette**: Edges of the screen are subtly darkened, focusing attention toward the center
- **Color Adjustments**: Overall brightness, contrast, and color saturation are modified To see the effects in action

- Ensure you're in **Scene** or **Game** view 
	- If effects aren't visible in the **Scene** view, click the **"Gizmos"** dropdown and ensure **"Post- Processing"** is enabled
	- Also ensure it is enabled on the Main Camera and in the URP Settings Asset

--- 

## Part 4: Experimenting with Additional Effects
Feel free to explore other post- processing effects
- **Depth of Field**: Blurs objects based on their distance from the camera
- **Film Grain**: Adds a cinematic grainy texture
- **Lens Distortion**: Simulates lens imperfections for creative effects To add these

- Click **"Add Override"** in the **Global Volume** - Select the desired effect