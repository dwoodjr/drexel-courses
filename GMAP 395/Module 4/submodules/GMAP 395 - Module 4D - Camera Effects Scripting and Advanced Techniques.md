# Module 4D: Camera Effects Scripting and Advanced Techniques

> [!info] Module Overview 
> **Learning Focus:** Practical Cinemachine implementation and camera control scripting 
> **Tools:** Unity Cinemachine, C# scripting, Timeline integration 
> **Builds On:** Camera fundamentals from [[GMAP 395 - Module 4C - Cinemachine and Camera Systems Fundamentals]]

---

## 🚀 Practical Cinemachine Implementation for Beginners

### Essential Setup Process ⚙️

**Step 1: Install Cinemachine**

1. **Window → Package Manager**
2. **Unity Registry → Search "Cinemachine"**
3. **Click Install**

> [!tip] Unity 6 Update **Cinemachine 3.1** provides redesigned interface and improved performance specifically optimized for Unity 6!

**Step 2: Set Up Your Main Camera**

1. **Select your Main Camera**
2. **Add Component → Cinemachine Brain**
3. **Leave settings as default** for now

**Step 3: Create Your First Virtual Camera**

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

## 💻 Core Camera Control Scripts for Beginners

### Basic Multi-Camera System

```csharp
using UnityEngine;
using Cinemachine;

// Simple camera switching system for art students
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
    [SerializeField] private KeyCode testLightShake = KeyCode.Alpha1;
    [SerializeField] private KeyCode testMediumShake = KeyCode.Alpha2;
    [SerializeField] private KeyCode testHeavyShake = KeyCode.Alpha3;
    
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
            Debug.LogError("Add it via: Virtual Camera → Add Extension → BasicMultiChannelPerlin");
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
        #if UNITY_EDITOR
        if (Input.GetKeyDown(testLightShake))
            TriggerShake(lightShake);
        else if (Input.GetKeyDown(testMediumShake))
            TriggerShake(mediumShake);
        else if (Input.GetKeyDown(testHeavyShake))
            TriggerShake(heavyShake);
        #endif
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
2. **Add Extension → CinemachineBasicMultiChannelPerlin**
3. **Create an empty GameObject** and add the CameraShakeController script
4. **Drag your Virtual Camera** into the script's "Virtual Camera" field
5. **Press Play** and test with **1, 2, 3 keys**!

> [!example] When to Use Different Shake Intensities
> 
> - **Light Shake (0.5):** Footsteps, small impacts, UI feedback
> - **Medium Shake (1.0):** Weapon firing, landing from heights, explosions nearby
> - **Heavy Shake (2.0):** Boss attacks, huge explosions, dramatic moments

---

## 🎯 Smart Follow Camera with Advanced Features

This script creates a sophisticated follow camera that predicts player movement:

```csharp
using UnityEngine;
using Cinemachine;

// Advanced follow camera with customizable smoothing and prediction
public class SmartFollowCamera : MonoBehaviour
{
    [Header("Camera Target")]
    [SerializeField] private Transform target;
    [SerializeField] private CinemachineVirtualCamera virtualCamera;
    
    [Header("Follow Behavior Settings")]
    [SerializeField] private Vector3 followOffset = new Vector3(0, 5, -10);
    [SerializeField] private Vector3 lookOffset = Vector3.up;
    
    [Header("Smoothing Control")]
    [Range(0.1f, 5f)] [SerializeField] private float positionDamping = 1f;
    [Range(0.1f, 5f)] [SerializeField] private float rotationDamping = 1f;
    
    [Header("Prediction Settings")]
    [SerializeField] private bool enableMovementPrediction = true;
    [Range(0f, 2f)] [SerializeField] private float predictionStrength = 0.5f;
    
    [Header("Boundary Constraints")]
    [SerializeField] private bool constrainToBounds = false;
    [SerializeField] private Bounds movementBounds;
    
    // Component references
    private CinemachineTransposer transposer;
    private CinemachineComposer composer;
    private Vector3 previousTargetPosition;
    private Vector3 targetVelocity;
    
    void Start()
    {
        InitializeCameraComponents();
        
        if (target != null)
        {
            previousTargetPosition = target.position;
        }
    }
    
    void InitializeCameraComponents()
    {
        // Get Cinemachine components
        transposer = virtualCamera.GetCinemachineComponent<CinemachineTransposer>();
        composer = virtualCamera.GetCinemachineComponent<CinemachineComposer>();
        
        if (transposer == null)
        {
            Debug.LogError("No CinemachineTransposer found on virtual camera!");
            Debug.LogError("Set Body to 'Transposer' in the virtual camera settings");
            return;
        }
        
        // Configure initial settings
        transposer.m_FollowOffset = followOffset;
        transposer.m_XDamping = positionDamping;
        transposer.m_YDamping = positionDamping;
        transposer.m_ZDamping = positionDamping;
        
        if (composer != null)
        {
            composer.m_TrackedObjectOffset = lookOffset;
            composer.m_HorizontalDamping = rotationDamping;
            composer.m_VerticalDamping = rotationDamping;
        }
    }
    
    void Update()
    {
        if (target == null) return;
        
        // Calculate target velocity for prediction
        targetVelocity = (target.position - previousTargetPosition) / Time.deltaTime;
        previousTargetPosition = target.position;
        
        // Update camera settings in real-time
        UpdateCameraSettings();
        
        // Apply movement prediction
        if (enableMovementPrediction)
        {
            ApplyMovementPrediction();
        }
        
        // Handle boundary constraints
        if (constrainToBounds)
        {
            EnforceBoundaryConstraints();
        }
    }
    
    void UpdateCameraSettings()
    {
        if (transposer != null)
        {
            transposer.m_FollowOffset = followOffset;
            transposer.m_XDamping = positionDamping;
            transposer.m_YDamping = positionDamping;
            transposer.m_ZDamping = positionDamping;
        }
        
        if (composer != null)
        {
            composer.m_TrackedObjectOffset = lookOffset;
            composer.m_HorizontalDamping = rotationDamping;
            composer.m_VerticalDamping = rotationDamping;
        }
    }
    
    void ApplyMovementPrediction()
    {
        if (transposer == null) return;
        
        // Calculate predicted position
        Vector3 predictedOffset = targetVelocity * predictionStrength;
        Vector3 dynamicOffset = followOffset + predictedOffset;
        
        // Apply predicted offset
        transposer.m_FollowOffset = dynamicOffset;
    }
    
    void EnforceBoundaryConstraints()
    {
        // Constrain camera position to defined bounds
        Vector3 cameraPosition = virtualCamera.transform.position;
        Vector3 constrainedPosition = new Vector3(
            Mathf.Clamp(cameraPosition.x, movementBounds.min.x, movementBounds.max.x),
            Mathf.Clamp(cameraPosition.y, movementBounds.min.y, movementBounds.max.y),
            Mathf.Clamp(cameraPosition.z, movementBounds.min.z, movementBounds.max.z)
        );
        
        // Apply constraint if position changed
        if (constrainedPosition != cameraPosition)
        {
            virtualCamera.transform.position = constrainedPosition;
        }
    }
    
    // Public methods for runtime control
    public void SetTarget(Transform newTarget)
    {
        target = newTarget;
        virtualCamera.Follow = newTarget;
        virtualCamera.LookAt = newTarget;
        
        if (newTarget != null)
        {
            previousTargetPosition = newTarget.position;
        }
    }
    
    public void SetFollowOffset(Vector3 offset)
    {
        followOffset = offset;
    }
    
    public void SetDamping(float position, float rotation)
    {
        positionDamping = position;
        rotationDamping = rotation;
    }
    
    // Visual debugging in Scene view
    void OnDrawGizmosSelected()
    {
        if (constrainToBounds)
        {
            Gizmos.color = Color.yellow;
            Gizmos.DrawWireCube(movementBounds.center, movementBounds.size);
        }
        
        if (target != null)
        {
            Gizmos.color = Color.green;
            Gizmos.DrawWireSphere(target.position + lookOffset, 0.5f);
        }
    }
}
```

---

## 🎬 Timeline Integration for Cinematic Sequences

### Creating Your First Timeline Sequence 🎞️

**Step 1: Set Up Timeline**

1. **Create empty GameObject** and name it "CinematicDirector"
2. **Add Component → Playable Director**
3. **Window → Sequencing → Timeline**
4. **Create new Timeline Asset**

**Step 2: Add Cinemachine Track**

1. **In Timeline window, right-click**
2. **Cinemachine → Cinemachine Track**
3. **Drag your Main Camera** to the track (the one with Cinemachine Brain)

**Step 3: Create Camera Shots**

1. **Right-click on Cinemachine Track**
2. **Add Cinemachine Shot Clip**
3. **Drag a Virtual Camera** into the clip's "Virtual Camera" field

> [!tip] Timeline Pro Tip Create multiple Virtual Cameras positioned around your scene, then use Timeline to cut between them like a movie director!

---

## 🏋️ Step-by-Step Advanced Exercise: Complete Camera System

### Project Goal 🎯

Create a third-person adventure camera system with multiple behaviors, smooth transitions, and interactive controls.

### Exercise Breakdown 📝

#### Phase 1: Basic Setup (15 minutes)

1. **Install Cinemachine** via Package Manager
2. **Create a simple scene** with a player character (use a capsule with movement script)
3. **Add Cinemachine Brain** to Main Camera
4. **Create first Virtual Camera** with basic follow

#### Phase 2: Multi-Camera System (20 minutes)

1. **Create 3 different Virtual Cameras:**
    - **Close-up camera:** For dialogue/interaction
    - **Wide camera:** For exploration overview
    - **Action camera:** For combat/dynamic moments
2. **Add the BasicCameraSwitcher script**
3. **Test switching** between cameras

#### Phase 3: Camera Shake Integration (15 minutes)

1. **Add BasicMultiChannelPerlin** to your action camera
2. **Implement CameraShakeController script**
3. **Connect shake to player actions** (jumping, landing, etc.)

#### Phase 4: Advanced Features (20 minutes)

1. **Implement SmartFollowCamera** on main camera
2. **Add movement prediction** and boundary constraints
3. **Test different damping** settings

#### Phase 5: Polish Phase (10 minutes)

1. **Fine-tune all camera settings**
2. **Add post-processing effects** (connect with previous modules!)
3. **Create simple Timeline sequence** for intro/outro

### Assessment Criteria ✅

**Technical Implementation (50%):**

- All scripts compile and run without errors
- Camera switching works smoothly
- Shake system responds correctly to events

**User Experience (30%):**

- Camera feels responsive and comfortable
- Transitions are smooth and not jarring
- Different cameras serve clear purposes

**Creative Application (20%):**

- Thoughtful use of different camera behaviors
- Good integration with post-processing
- Evidence of experimentation and polish

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

> [!tip] Unity 6 Specific Enhancements
> 
> - **Redesigned Inspector:** More intuitive workflow for art students
> - **Improved Blending:** Smoother transitions between virtual cameras
> - **Enhanced Performance:** Optimized update cycles and memory usage

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

> [!info] 🧭 Module Navigation **Previous:** [[GMAP 395 - Module 4C - Cinemachine Camera Fundamentals|Module 4C]]  
> **Return to:** [[GMAP 395 - Module 4|Module Page]]