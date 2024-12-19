# Game Audio and Implementation
## 9 - Game Audio Basics and Procedural Workflows

---

# Agenda

1. Audio Basics
2. Unity Audio System
3. Audio Implementation in Unity
4. Scripting Audio in Unity
5. Advanced Audio Techniques
6. Procedural Audio Introduction

---

# Audio Basics

---

# Why is Audio Important in Games?

- Enhances immersion and player engagement
- Provides crucial feedback to the player
- Sets mood and atmosphere
- Reinforces the game's narrative and themes

---

# Types of Game Audio

1. Sound Effects (SFX)
2. Music
3. Voice Acting
4. Ambient Sound

---

# Sound Effects (SFX)

- Short audio clips that accompany specific actions or events
- Examples:
  - Footsteps
  - Weapon sounds
  - UI feedback
  - Environmental sounds (wind, rain)

---

# Music in Games

- Background music to set the mood
- Can be:
  - Static (same track looping)
  - Dynamic (changes based on game state)
  - Adaptive (smoothly transitions between states)

---

# Voice Acting

- Brings characters to life
- Provides narrative context
- Can be:
  - Full voice acting
  - Partial voice acting (key scenes only)
  - Emotive sounds (grunts, laughs)

---

# Ambient Sound

- Creates a sense of place and atmosphere
- Often looping and subtle
- Examples:
  - Forest sounds
  - City traffic
  - Spaceship hum

---

# Unity Audio System

---

# Unity Audio System: Overview

- Based on emitters and listeners
- Key components:
  - Audio Source
  - Audio Listener
  - Audio Clip
  - Audio Mixer

---

# Audio Source Component

- Plays back Audio Clips
- Key properties:
  - Clip
  - Volume
  - Pitch
  - Spatial Blend (2D/3D)
  - Loop

---

# Audio Source: Spatial Blend

- Controls how the audio is perceived in 3D space
- 0 = 2D (no spatial effect)
- 1 = 3D (full spatial effect)
- Can be set anywhere in between for partial effect

---

# Audio Listener Component

- Acts as the "ears" of the scene
- Usually attached to the main camera
- Only one active Audio Listener per scene
- Crucial for 3D audio positioning

---

# Audio Clip

- Contains the actual audio data
- Supported formats:
  - WAV
  - MP3
  - OGG
  - AIFF
- Consider file size and quality when choosing format

---

# Audio Mixer

- Manages multiple audio sources
- Creates audio groups (e.g., SFX, Music, Dialogue)
- Applies effects to groups
- Controls overall mix
- Allows for dynamic volume control

---

# Audio Implementation in Unity

---

# Basic Audio Implementation Steps

1. Import audio files into Unity
2. Add Audio Source component to game object
3. Assign Audio Clip to Audio Source
4. Adjust Audio Source properties
5. Play audio through script or component settings

---

# 3D Sound in Unity

- Use Spatial Blend setting in Audio Source
- Adjust 3D Sound Settings:
  - Doppler Level (pitch change based on motion)
  - Volume Rolloff (how volume decreases with distance)
  - Min/Max Distance (audible range of the sound)

---

# Audio Mixer: Practical Use

1. Create Audio Mixer asset
2. Add groups (e.g., SFX, Music, Dialogue)
3. Assign Audio Sources to groups
4. Add effects to groups (e.g., reverb, EQ)
5. Control group volumes via script or UI

---

# Scripting Audio in Unity

---

# Playing Audio with C#: Concept

- Access the AudioSource component
- Use methods like Play(), Stop(), Pause()
- Can play one-shot sounds or looping audio
- Control volume, pitch, and other properties dynamically

---

# Playing Audio with C#: Code Example

```csharp
using UnityEngine;

public class AudioPlayer : MonoBehaviour
{
    public AudioSource audioSource;
    public AudioClip soundEffect;

    void Start()
    {
        audioSource = GetComponent<AudioSource>();
    }

    void PlaySound()
    {
        audioSource.PlayOneShot(soundEffect);
    }
}
```

---

# Terrain-based Footstep Sounds: Concept

- Detect the terrain texture at the player's position
- Select appropriate sound based on terrain type
- Play random variation of the selected sound
- Enhances immersion by providing realistic feedback

---

# Terrain-based Footstep Sounds: Code Example (Part 1)

```csharp
using UnityEngine;

public class FootstepAudio : MonoBehaviour
{
    public AudioClip[] grassSteps;
    public AudioClip[] woodSteps;
    public AudioClip[] stoneSteps;

    private AudioSource audioSource;
    private Terrain terrain;

    void Start()
    {
        audioSource = GetComponent<AudioSource>();
        terrain = Terrain.activeTerrain;
    }

    void Update()
    {
        if (Input.GetKeyDown(KeyCode.Space)) // Simulate a step
        {
            PlayFootstep();
        }
    }
```

---

# Terrain-based Footstep Sounds: Code Example (Part 2)

```csharp
    void PlayFootstep()
    {
        int terrainTextureIndex = GetMainTexture(transform.position);
        AudioClip[] currentSteps;

        switch (terrainTextureIndex)
        {
            case 0: currentSteps = grassSteps; break;
            case 1: currentSteps = woodSteps; break;
            case 2: currentSteps = stoneSteps; break;
            default: currentSteps = grassSteps; break;
        }

        AudioClip stepToPlay = currentSteps[Random.Range(0, currentSteps.Length)];
        audioSource.PlayOneShot(stepToPlay);
    }
```

---

# Terrain-based Footstep Sounds: Code Example (Part 3)

```csharp
    private int GetMainTexture(Vector3 worldPos)
    {
        // Convert world position to terrain coordinates
        Vector3 terrainPos = terrain.transform.InverseTransformPoint(worldPos);
        Vector3 splatMapPos = new Vector3(
            terrainPos.x / terrain.terrainData.size.x,
            0,
            terrainPos.z / terrain.terrainData.size.z);

        // Get the splat map data
        float[,,] splatmapData = terrain.terrainData.GetAlphamaps(
            (int)(splatMapPos.x * terrain.terrainData.alphamapWidth),
            (int)(splatMapPos.z * terrain.terrainData.alphamapHeight), 1, 1);

        // Find the texture with the highest weight
        float maxWeight = 0;
        int maxIndex = 0;
        for (int i = 0; i < splatmapData.GetLength(2); i++)
        {
            if (splatmapData[0, 0, i] > maxWeight)
            {
                maxWeight = splatmapData[0, 0, i];
                maxIndex = i;
            }
        }

        return maxIndex;
    }
}
```

---

# Smooth Audio Transition: Concept

- Gradually fade out one audio track while fading in another
- Use coroutines for time-based operations
- Adjust volume using Mathf.Lerp for smooth interpolation
- Enhances player experience during music or ambiance changes

---

# Smooth Audio Transition: Code Example

```csharp
using UnityEngine;
using System.Collections;

public class MusicTransition : MonoBehaviour
{
    public AudioSource source1;
    public AudioSource source2;
    public float transitionTime = 2.0f;

    public void TransitionMusic()
    {
        StartCoroutine(Transition());
    }

    private IEnumerator Transition()
    {
        float t = 0;
        source2.Play();

        while (t < transitionTime)
        {
            t += Time.deltaTime;
            source1.volume = Mathf.Lerp(1, 0, t / transitionTime);
            source2.volume = Mathf.Lerp(0, 1, t / transitionTime);
            yield return null;
        }

        source1.Stop();
    }
}
```

---

# Scripting with Audio Mixer: Concept

- Access the Audio Mixer through scripts
- Modify group volumes dynamically
- Use logarithmic scale for natural-sounding volume changes
- Allows for runtime audio adjustments (e.g., volume sliders in options menu)

---

# Scripting with Audio Mixer: Code Example

```csharp
using UnityEngine;
using UnityEngine.Audio;

public class VolumeControl : MonoBehaviour
{
    public AudioMixer audioMixer;

    public void SetMasterVolume(float volume)
    {
        audioMixer.SetFloat("MasterVolume", Mathf.Log10(volume) * 20);
    }

    public void SetSFXVolume(float volume)
    {
        audioMixer.SetFloat("SFXVolume", Mathf.Log10(volume) * 20);
    }
}
```

---

# Advanced Audio Techniques

---

# Ambisonics

- Full-sphere surround sound technique
- Captures and reproduces 3D sound field
- Ideal for VR and 360° video applications
- Supported in Unity for certain audio formats

---

# Binaural Audio

- 3D audio technique that simulates how we hear in real life
- Uses HRTF (Head-Related Transfer Function)
- Especially effective for headphone users
- Can be simulated in Unity with certain plugins

---

# Dynamic Music Systems

- Music that adapts to gameplay
- Can change based on:
  - Player location
  - Game state (e.g., combat, exploration)
  - Player health or stress level
- Implemented using multiple audio tracks or generative techniques

---

# Audio Occlusion and Obstruction

- Simulates how sound is affected by objects in the environment
- Occlusion: Sound passing through objects
- Obstruction: Sound going around objects
- Can be implemented using raycasts and audio filters

---

# Procedural Audio: Introduction

---

# What is Procedural Audio?

- Audio generated or manipulated in real-time
- Not pre-recorded, but created algorithmically
- Can be responsive to game state and player actions
- Reduces memory usage for audio assets

---

# Tools for Procedural Audio

- Pure Data
- Max/MSP
- Reaktor
- Unity's built-in audio effects
- Custom C# scripts for audio synthesis

---

# Benefits of Procedural Audio

- Infinite variations of sounds
- Responsive to gameplay parameters
- Reduced memory footprint
- Potentially smaller file sizes for games

---

# Challenges of Procedural Audio

- Can be CPU-intensive
- Requires different skill set (programming + sound design)
- May lack the nuance of carefully crafted recorded audio
- Tools and workflows still evolving

---

# Max/MSP: Brief Overview

- Visual programming language for audio and multimedia
- Used for sound design, music composition, and interactive audio
- Can export creations as plugins for use in games
- Full example and integration will be covered in the next session

---

# Conclusion

- Audio is a crucial element of game design
- Unity provides powerful tools for audio implementation
- Scripting allows for dynamic and interactive audio experiences
- Advanced techniques can greatly enhance immersion
- Procedural audio opens new possibilities for game sound

---

# Next Steps

- Experiment with the code examples provided
- Explore Unity's Audio Mixer
- Try creating a dynamic music system
- Look into procedural audio techniques

---

# Lab Time

Now, practice implementing some of these audio techniques for yourself

---
