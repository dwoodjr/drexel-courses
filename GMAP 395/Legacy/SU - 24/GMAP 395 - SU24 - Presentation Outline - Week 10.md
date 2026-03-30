# Week 10: Advanced Audio Techniques & Generative Sound

---

# Review of Week 9

- Audio Fundamentals
- Unity Audio System
- Audio Implementation in Unity
- Scripting Audio in Unity
- Advanced Audio Concepts
- Introduction to Procedural Audio

---

# How Music Gets into Games

[Insert YouTube video: "How Sounds Get Into Games - Fundamentals Of Game Audio Implementation"]

---

# Reverb & Reverb Zones

- Simulates sound reflections in different environments
- Unity's Audio Reverb Zone component
- Customizable parameters: Room Size, Reflections, Decay Time
- Multiple zones for different areas in your game

---

# Spatialization in Unity: Practical Implementation

- Why spatialize?
  - Creates immersive 3D soundscapes
  - Enhances player orientation and feedback

- How to spatialize in Unity:
  1. Set Audio Source's "Spatial Blend" to 1 (Full 3D)
  2. Adjust "3D Sound Settings":
     - Min Distance: Sound at full volume
     - Max Distance: Sound fades to zero
  3. Choose appropriate "Volume Rolloff":
     - Logarithmic: Natural sound falloff
     - Linear: Gradual, even falloff

- Use Audio Listener on player/camera

```csharp
// Example: Dynamically spatialize based on distance
public class DynamicSpatializer : MonoBehaviour
{
    public AudioSource audioSource;
    public float fullSpatialDistance = 10f;
    
    void Update()
    {
        float distanceToListener = Vector3.Distance(transform.position, Camera.main.transform.position);
        float spatialBlend = Mathf.Clamp01(distanceToListener / fullSpatialDistance);
        audioSource.spatialBlend = spatialBlend;
    }
}
```

---

# Audio Mixer & Dynamic Control

- Grouping and organizing audio sources
- Applying effects to groups
- Controlling mix at runtime

---

# Scripting Mixer Control: Code Example

```csharp
using UnityEngine;
using UnityEngine.Audio;

public class MixerController : MonoBehaviour
{
    public AudioMixer masterMixer;

    public void SetMusicVolume(float volume)
    {
        masterMixer.SetFloat("MusicVolume", Mathf.Log10(volume) * 20);
    }

    public void SetReverbLevel(float amount)
    {
        masterMixer.SetFloat("ReverbLevel", amount);
    }
}
```

---

# Process of Controlling Mixer Effects

1. Create exposed parameters in the Audio Mixer
2. Reference the Audio Mixer in your script
3. Use SetFloat() to adjust parameters
4. Connect to UI elements or game events

---

# Generative & Dynamic Music

- Algorithmic composition
- Adaptive music systems
- Layered approach for dynamic transitions
- Real-time synthesis and manipulation

---

# PureData (Pd) Introduction

- Visual programming language for audio
- Modular approach to sound design
- Flexible and powerful for real-time audio processing

---

# PureData + Unity: LibPd

- LibPd: Embeddable PureData
- Allows running Pd patches in Unity
- Bridge between visual audio programming and game engine

---

# Simple Generative Music Sequence

[Insert image or code snippet of a 10-note generative sequence in PureData]

- Random Note Generation: Creates unpredictable melodies
- Counter Mechanism: Keeps track of the number of notes played
- MIDI to Frequency Conversion: Translates note numbers to playable frequencies
- Envelope Generator: Shapes the amplitude of each note for a plucky sound
- Oscillator: Produces the actual sound waveform
- Metro Object: Controls the timing and triggering of notes
- Transposition: Shifts notes to an appropriate octave range
- Spigot Object: Acts as a gate to start and stop the melody sequence
- Message Box: Defines the envelope shape for each note

---

# Using Pd in Unity: Demo

[Live demonstration or video of implementing a PureData patch in Unity]

---

# Final Project Overview

- Create an integrated, interactive game-like experience
- Showcase skills from all five course modules
- Expand on your pitch assignment concept
- Focus on one area: prop, character, or environment

---

# Project Requirements by Module

1. Procedural + Modular Modeling and Workflows
   - Implement procedural/modular system for chosen focus
2. Material + Shader Development
   - Create at least 2 custom shaders (Shader Graph or HLSL)
3. Image + Particle Effects
   - Develop at least 3 unique visual effects
4. Lighting + Camera Effects
   - Implement 3+ distinct lighting sources
   - Use 2+ image effects or post-processing techniques
5. Game Audio and Implementation
   - Integrate 2+ audio effects and/or music tracks
   - Ensure proper spatial audio implementation

---

# Game-Based Interactivity

- Provide meaningful, real-time interactivity
- Consider:
  - Player Interaction
  - User Interface
  - Feedback and Response
  - Narrative or Contextual Framing

---

# Deliverables

1. Playthrough Video (Max 10 minutes)
2. Presentation Video (Max 15 minutes)
3. Unity Project (Zipped folder)
4. Windows/PC Build
5. Postmortem Document

---

# Break

---

# Final Project Drafts

[Instructions for draft presentations]

---

