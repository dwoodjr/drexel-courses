# Module 4D: Camera Effects Scripting and Advanced Techniques

> [!info] Module Overview 
> **Learning Focus:** Practical Cinemachine implementation and camera control scripting 
> **Tools:** Unity Cinemachine, C# scripting, Timeline integration 
> **Builds On:** Camera fundamentals from [[GMAP 395 - Module 4C - Cinemachine and Camera Systems Fundamentals]]

> [!summary] Submodule Video Overview
> <iframe src="https://1drv.ms/v/c/b08de2251f1b33a4/IQRTpUIC7ky1RJi5x2Dl91w8Ad0cFH1Qn5x_tAxGiGJZf5M?width=2560&height=1440" width="800" height="600" frameborder="0"></iframe>
> 
> [gmap395_md4d.mkv](https://1drv.ms/v/c/b08de2251f1b33a4/EVOlQgLuTLVEmLnHYOX3XDwBqCqyFyzan7EFCFRYF5PvTA?e=8E5yUk)

---

## 🚀 Practical Cinemachine Implementation

### Essential Setup Process ⚙️

**Step 1: Install Cinemachine**
1. **Window → Package Manager**
2. **Unity Registry → Search "Cinemachine"**
3. **Click Install**

**Step 2: Set Up Your Main Camera**
1. **Select your Main Camera**
2. **Add Component → Cinemachine Brain**
3. **Leave settings as default** for now

**Step 3: Create Your First Virtual Camera**\
1. **Right-click in Hierarchy**
2. **Cinemachine → Virtual Camera**
3. **Name it** "PlayerFollowCam"

### Your First Virtual Camera Setup 📸

Let's create a basic third-person follow camera:

1. **Select your Virtual Camera**
2. **Drag your Player** into the **Follow** field
3. **Drag your Player** into the **Look At** field
4. **Set Priority** to **10**

**Press Play** - your camera should now follow your player!

---

## 💻 Core Camera Control Scripts

### Basic Multi-Camera System

```csharp
using UnityEngine;
using Cinemachine;

// Simple camera switching system
public class BasicCameraSwitcher : MonoBehaviour
{
    [Header("Virtual Camera Setup")]
    [SerializeField] private CinemachineVirtualCamera[] cameras;
    
    [Header("Control Settings")]
    [SerializeField] private KeyCode switchKey = KeyCode.Tab;
    [SerializeField] private bool enableDebugMessages = true;
    
    private int currentCameraIndex = 0;
    
    void Start()
    {
        // Initialize camera priorities
        // Only the first camera should be active initially
        for (int i = 0; i < cameras.Length; i++)
        {
            cameras[i].Priority = (i == 0) ? 10 : 0;
        }
        
        if (enableDebugMessages)
        {
            Debug.Log($"Camera system initialized with {cameras.Length} cameras");
            Debug.Log($"Active camera: {cameras[0].name}");
        }
    }
    
    void Update()
    {
        // Handle camera switching input
        if (Input.GetKeyDown(switchKey))
        {
            SwitchToNextCamera();
        }
        
        // Allow number key switching for quick testing
        for (int i = 0; i < Mathf.Min(cameras.Length, 9); i++)
        {
            if (Input.GetKeyDown(KeyCode.Alpha1 + i))
            {
                SwitchToCamera(i);
            }
        }
    }
    
    void SwitchToNextCamera()
    {
        // Cycle to next camera in array
        int nextIndex = (currentCameraIndex + 1) % cameras.Length;
        SwitchToCamera(nextIndex);
    }
    
    public void SwitchToCamera(int cameraIndex)
    {
        // Validate camera index
        if (cameraIndex < 0 || cameraIndex >= cameras.Length)
        {
            Debug.LogError($"Invalid camera index: {cameraIndex}");
            return;
        }
        
        // Set priorities: active camera gets 10, all others get 0
        for (int i = 0; i < cameras.Length; i++)
        {
            cameras[i].Priority = (i == cameraIndex) ? 10 : 0;
        }
        
        currentCameraIndex = cameraIndex;
        
        if (enableDebugMessages)
        {
            Debug.Log($"Switched to camera: {cameras[cameraIndex].name}");
        }
    }
    
    // Public method for other scripts or UI buttons
    public void SwitchToCameraByName(string cameraName)
    {
        for (int i = 0; i < cameras.Length; i++)
        {
            if (cameras[i].name == cameraName)
            {
                SwitchToCamera(i);
                return;
            }
        }
        
        Debug.LogWarning($"Camera not found: {cameraName}");
    }
}
```

### How to Use the Camera Switcher 📝

1. **Create an empty GameObject** and name it "CameraSwitcher"
2. **Add the script** to this GameObject
3. **Create multiple Virtual Cameras** in your scene
4. **Drag all Virtual Cameras** into the "Cameras" array
5. **Press Play** and test with **Tab** or **number keys**!

> [!tip] Pro Tip This script is perfect for testing different camera angles quickly. Use it to experiment with camera positioning!

---

## 📳 Professional Camera Shake Implementation

Camera shake adds **impact and juice** to your game events. Here's a comprehensive system:

```csharp
using UnityEngine;
using Cinemachine;

// Comprehensive camera shake system for gameplay events

public class CameraShakeController : MonoBehaviour

{

    [System.Serializable]
    public class ShakeSettings

    {

        [Header("Shake Parameters")]

        public float intensity = 1f;

        public float duration = 0.5f;

        public float frequency = 1f;

        [Header("Directional Control")]

        [Range(0f, 1f)] public float horizontalShake = 1f;

        [Range(0f, 1f)] public float verticalShake = 1f;

        public ShakeSettings(float intensity, float duration)

        {

            this.intensity = intensity;

            this.duration = duration;

            this.frequency = 1f;

            this.horizontalShake = 1f;

            this.verticalShake = 1f;

        }

    }

    [Header("Camera References")]

    [SerializeField] private CinemachineVirtualCamera virtualCamera;

    [Header("Predefined Shake Types")]

    public ShakeSettings lightShake = new ShakeSettings(0.5f, 0.2f);

    public ShakeSettings mediumShake = new ShakeSettings(1f, 0.5f);

    public ShakeSettings heavyShake = new ShakeSettings(2f, 1f);

    [Header("Debug Testing")]

    [SerializeField] private KeyCode testLightShake = KeyCode.Keypad1;

    [SerializeField] private KeyCode testMediumShake = KeyCode.Keypad2;

    [SerializeField] private KeyCode testHeavyShake = KeyCode.Keypad3;

  

    // Component references

    private CinemachineBasicMultiChannelPerlin noise;

    private float shakeTimer;

    private float originalAmplitude;

    private float originalFrequency;

    void Start()

    {

        // Get noise component for camera shake

        noise = virtualCamera.GetCinemachineComponent<CinemachineBasicMultiChannelPerlin>();

        if (noise == null)

        {

            Debug.LogError("No BasicMultiChannelPerlin component found on virtual camera!");

            Debug.LogError("Add it via: Virtual Camera → Noise → BasicMultiChannelPerlin");

            return;

        }

        // Store original values for restoration

        originalAmplitude = noise.m_AmplitudeGain;

        originalFrequency = noise.m_FrequencyGain;

    }

    void Update()

    {

        // Handle shake timer countdown

        if (shakeTimer > 0)

        {

            shakeTimer -= Time.deltaTime;

            if (shakeTimer <= 0)

            {

                StopShake();

            }

        }

  

        // Debug testing inputs

        if (Input.GetKeyDown(testLightShake))

        {

            TriggerShake(lightShake);

            Debug.Log("Light shake triggered");

        }

        if (Input.GetKeyDown(testMediumShake))

        {

            TriggerShake(mediumShake);

            Debug.Log("Medium shake triggered");

        }

        if (Input.GetKeyDown(testHeavyShake))

        {

            TriggerShake(heavyShake);

            Debug.Log("Heavy shake triggered");

        }

  

    }

  

    /// <summary>

    /// Trigger camera shake with predefined settings

    /// </summary>

    public void TriggerShake(ShakeSettings settings)

    {

        if (noise == null) return;

        // Apply shake settings

        noise.m_AmplitudeGain = settings.intensity;

        noise.m_FrequencyGain = settings.frequency;

        // Set timer

        shakeTimer = settings.duration;

        Debug.Log($"Camera shake triggered - Intensity: {settings.intensity}, Duration: {settings.duration}s");

    }

    /// <summary>

    /// Quick shake method with just intensity and duration

    /// </summary>

    public void TriggerShake(float intensity, float duration)

    {

        ShakeSettings quickShake = new ShakeSettings(intensity, duration);

        TriggerShake(quickShake);

    }

    /// <summary>

    /// Stop shake immediately and restore original settings

    /// </summary>

    public void StopShake()

    {

        if (noise == null) return;

        noise.m_AmplitudeGain = originalAmplitude;

        noise.m_FrequencyGain = originalFrequency;

        shakeTimer = 0;

        Debug.Log("Camera shake stopped");

    }

    /// <summary>

    /// Gradually reduce shake intensity over time for smoother transitions

    /// </summary>

    public void StartDecayingShake(float initialIntensity, float totalDuration)

    {

        StartCoroutine(DecayingShakeCoroutine(initialIntensity, totalDuration));

    }

    private System.Collections.IEnumerator DecayingShakeCoroutine(float initialIntensity, float duration)

    {

        if (noise == null) yield break;

        float timer = 0f;

        while (timer < duration)

        {

            timer += Time.deltaTime;

            float progress = timer / duration;

            // Exponential decay for natural feeling

            float currentIntensity = initialIntensity * Mathf.Exp(-progress * 3f);

            noise.m_AmplitudeGain = currentIntensity;

            yield return null;

        }

        StopShake();

    }

}
```

### Setting Up Camera Shake 🔧

1. **Select your Virtual Camera**
2. **Noise → CinemachineBasicMultiChannelPerlin**
3. **Assign a noise profile and set the `Amplitude Gain` and `Frequency Gain` lower (0-0.25)**
4. **Create an empty GameObject** and add the CameraShakeController script
5. **Drag your Virtual Camera** into the script's "Virtual Camera" field
6. **Press Play** and test with **1, 2, 3 keys**!

> [!example] When to Use Different Shake Intensities
> 
> - **Light Shake (0.5):** Footsteps, small impacts, UI feedback
> - **Medium Shake (1.0):** Weapon firing, landing from heights, explosions nearby
> - **Heavy Shake (2.0):** Boss attacks, huge explosions, dramatic moments

---
## 💡 Additional Tips and Useful Camera Assets

### Camera Stacking 📚

With Unity's Scriptable Render Pipelines (URP/HDRP), you can **[stack multiple cameras](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@7.2/manual/camera-stacking.html)** to render different parts of your game separately. This powerful technique allows you to:

- **UI Camera:** Render user interface elements with different post-processing
- **Player Camera:** Focus on character with specific visual effects
- **Environment Camera:** Handle world rendering with separate optimization
- **Effects Camera:** Overlay special effects or HUD elements

> [!example] Camera Stacking Use Cases
> 
> - **UI overlays** that don't get affected by world post-processing
> - **Minimap cameras** rendering a top-down view simultaneously
> - **Picture-in-picture** effects for security cameras or scopes
> - **Different render styles** per layer (realistic world + stylized UI)

<iframe width="560" height="315" src="https://www.youtube.com/embed/OmCjPctKkjw?si=shwS2aXA7Tb8A_LY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

**Quick Setup:**

1. Create additional cameras in your scene
2. Set **Render Type** to "Overlay" on secondary cameras
3. Add overlay cameras to main camera's **Stack** list

### Unity Starter Assets - Camera Examples 🎮

Unity's **[Starter Assets](https://assetstore.unity.com/packages/essentials/starter-assets-thirdperson-updates-in-new-charactercontroller-pa-196526)** packages provide excellent Cinemachine implementations that serve as perfect learning references:

#### First Person Controller

- **Pre-configured mouse look** system with Cinemachine
- **Smooth camera rotation** with customizable sensitivity
- **Great foundation** for FPS games and first-person exploration

#### Third Person Controller

- **Professional 3rd-person camera** setup using Cinemachine
- **Orbit controls** with collision detection and smoothing
- **Industry-standard** character following and framing

> [!tip] How to Access Starter Assets
> 
> 1. **Go to the Unity Asset Store and search for** `Starter Assets`. **Add them to your assets (they are free).**
> 2. **Window → Package Manager**
> 3. **My Assets → Search "Starter Assets"**
> 4. **Install First Person** or **Third Person** package
> 5. **Study the camera scripts** and Cinemachine configurations!

These assets demonstrate **real-world camera implementations** that you can learn from and adapt for your own projects.

---
## 🔧 Troubleshooting Common Cinemachine Issues

> [!warning] Problem: "My Virtual Camera isn't active!" **Solution:** Check these in order:
> 
> 1. ✅ Does Main Camera have **Cinemachine Brain** component?
> 2. ✅ Is Virtual Camera **Priority** higher than others (try 10)?
> 3. ✅ Is Virtual Camera **enabled** in hierarchy?

> [!warning] Problem: "Camera shake isn't working!" **Solution:**
> 
> 4. ✅ Did you add **BasicMultiChannelPerlin** extension to Virtual Camera?
> 5. ✅ Is the **amplitude** value greater than 0?
> 6. ✅ Are you calling the shake function correctly?

> [!warning] Problem: "Camera movement is too jerky!" **Solution:**
> 
> 7. ✅ Increase **damping** values in Transposer settings
> 8. ✅ Check if **target framerate** is consistent
> 9. ✅ Reduce prediction strength if using movement prediction

---

## 📈 Performance Optimization Tips

**Performance Guidelines:**

- Set inactive virtual cameras to **"Never"** for Standby Update mode
- Limit simultaneous active virtual cameras (recommend maximum 3-4)
- Use object pooling for frequently created/destroyed cameras
- Consider Timeline for complex sequences instead of runtime switching

---

## 🎓 Extension Opportunities

**For Advanced Students:**

- Add camera behaviors for specific gameplay scenarios (combat lock-on, stealth mode, puzzle solving)
- Experiment with custom Cinemachine extensions for unique creative effects
- Create dynamic camera systems that respond to music or gameplay metrics
- Integrate with AI systems for intelligent camera positioning

**Portfolio Projects:**

- **Horror Game:** Camera system that builds tension through limitation and reveals
- **Racing Game:** Speed-responsive camera with multiple viewpoint options
- **Platformer:** Predictive camera that shows upcoming challenges
- **RPG:** Context-sensitive camera that adapts to different gameplay modes

---

> [!tip] Remember: Great camera work is invisible to the player but essential to the experience. Focus on how your cameras make the game **feel** rather than just how they look!

---

> [!info] 🧭 Module Navigation 
> **Previous:** [[GMAP 395 - Module 4C - Cinemachine and Camera Systems Fundamentals|Module 4C]]  
> **Return to:** [[GMAP 395 - Module 4|Module Page]]