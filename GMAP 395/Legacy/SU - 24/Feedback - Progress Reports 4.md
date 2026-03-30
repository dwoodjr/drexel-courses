Kristin - 
1. Check your prefab's rotation:
    - Ensure the prefab's forward vector (blue arrow) in local space points in the intended direction.
    - Assign a rotation value to each prefab in your script.
2. When instantiating road pieces:
    - Use Quaternion.Euler() to apply the assigned rotation.
    - Example: Quaternion.Euler(0, prefabRotation, 0) * Quaternion.identity
    - Or ensure that the instantiation actually recognizes the prefabs rotation via Quaternion.Identify. Check the API for this Bleow.
https://docs.unity3d.com/2020.1/Documentation/ScriptReference/Object.Instantiate.html

For UI item placement, make sure your raycasts are ignoring UI layers and use a boolean to create a "selection state" and a "placement state".

```csharp
public class PlacementManager : MonoBehaviour
{
    public bool isPlacementMode = false;
    public LayerMask uiLayer;
    public LayerMask placementLayer;

    void Update()
    {
        if (Input.GetKeyDown(KeyCode.Tab)) // Or any other key/button
        {
            TogglePlacementMode();
        }

        if (Input.GetMouseButtonDown(0)) // Left click
        {
            if (isPlacementMode)
            {
                HandlePlacement();
            }
            else
            {
                HandleUISelection();
            }
        }
    }

    void TogglePlacementMode()
    {
        isPlacementMode = !isPlacementMode;
        // Update UI to reflect current mode
    }

    void HandlePlacement()
    {
        Ray ray = Camera.main.ScreenPointToRay(Input.mousePosition);
        RaycastHit hit;

        if (Physics.Raycast(ray, out hit, Mathf.Infinity, placementLayer))
        {
            // Place object at hit.point
        }
    }

    void HandleUISelection()
    {
        Ray ray = Camera.main.ScreenPointToRay(Input.mousePosition);
        RaycastHit hit;

        if (Physics.Raycast(ray, out hit, Mathf.Infinity, uiLayer))
        {
            // Handle UI interaction
        }
    }
}
```

https://docs.unity3d.com/ScriptReference/Physics.Raycast.html

- We use a boolean `isPlacementMode` to toggle between UI selection and object placement modes.
- The `Update` method checks for a key press (Tab in this example) to switch modes. You can change this to a UI button if you prefer.
- We use different layermasks for UI and placement. This ensures raycasts only hit the appropriate objects based on the current mode.
- The `HandlePlacement` and `HandleUISelection` methods use these layermasks to ensure clicks only interact with the intended elements.
- Remember to update your UI to show which mode the player is currently in.

##
---

Vanessa - 

Great progress on your project! For the dynamic music, here's a simple Unity-based solution using C# that you could implement:

```csharp
public class MusicManager : MonoBehaviour
{
    public AudioSource musicSource;
    public AudioClip[] musicPlaylist;
    public float crossfadeDuration = 2f;

    private int currentTrackIndex = -1;
    private float transitionTime = 0f;
    private AudioSource nextMusicSource;

    void Start()
    {
        nextMusicSource = gameObject.AddComponent<AudioSource>();
        PlayNextTrack();
    }

    void Update()
    {
        if (transitionTime > 0)
        {
            transitionTime -= Time.deltaTime;
            float t = 1 - (transitionTime / crossfadeDuration);
            musicSource.volume = 1 - t;
            nextMusicSource.volume = t;

            if (transitionTime <= 0)
            {
                SwapAudioSources();
            }
        }
        else if (!musicSource.isPlaying)
        {
            PlayNextTrack();
        }
    }

    void PlayNextTrack()
    {
        currentTrackIndex = (currentTrackIndex + 1) % musicPlaylist.Length;
        CrossfadeToTrack(musicPlaylist[currentTrackIndex]);
    }

    void CrossfadeToTrack(AudioClip newTrack)
    {
        nextMusicSource.clip = newTrack;
        nextMusicSource.Play();
        transitionTime = crossfadeDuration;
    }

    void SwapAudioSources()
    {
        var temp = musicSource;
        musicSource = nextMusicSource;
        nextMusicSource = temp;
    }

    public void ChangeTrackBasedOnGameState(int stateIndex)
    {
        if (stateIndex != currentTrackIndex)
        {
            CrossfadeToTrack(musicPlaylist[stateIndex]);
            currentTrackIndex = stateIndex;
        }
    }
}
```

This psuedo-script creates a playlist system with semi-smooth crossfading between tracks. You can trigger track changes based on game events or states using something like the `ChangeTrackBasedOnGameState` method. 

To use this:
1. Attach this script to an empty GameObject in your scene.
2. Assign your music clips to the `musicPlaylist` array in the inspector.
3. Call `ChangeTrackBasedOnGameState(int stateIndex)` when you want to change the music based on game events.

This should give you a good starting point for dynamic music without needing to implement WWISE. Let me know if you need any clarification or have questions about implementing this!

##
---
Chris - Instead of exporting/importing packages, try directly copying assets and prefabs between projects. This should work well if you're using the same Unity version across projects.
- When copying assets:
    - Make sure to include all required scripts and components
    - Check for any missing references in the inspector after copying
    - Copy over any required materials, textures, or audio files
- For your scenes:
    - Create a new, clean scene
    - Drag in the necessary prefabs from your consolidated asset folder
    - Adjust lighting and camera settings as needed

##
---
Vincent
Absolutely, I recall we addressed the audio manager issue after class by fixing the errors in the sword part selection script using GetComponentsInChildren(). It sounded like it was working, but let me know if anything else arises via email.

##
---
Devin - 
Sounds good, you have been making steady good progress thorughout the course. You're on the right track! For this final week, focus on polishing these elements and integrating that flashlight if time allows. Let me know if any major issues arise via email.

##
---
Lillie - Thanks for the detailed update! It sounds like you've made significant progress despite some challenges and you have some achievable goals for your final push. Prioritize them based on their impact on your project's overall experience.

Button issue: I'm pretty sure we aggressed this in class, it was that you need to place the gameobject that will be controlled so the game has context on the script, not just the script itself from the project window.

Overall, you're in a good position. Keep up the good work!

##
---
Nate -
I understand you're facing some challenges, especially with the procedural generation. Let's break this down and look at some potential solutions: - The problem with tiles not loading correctly could be due to several factors and I will really need the script itself to really trouble shoot more, so send over a zip of your project when you get a chance (assets, packages, project settings folders) 
Here are some things to check: 
- Ensure all tile prefabs are correctly assigned in the Unity inspector. 
- Double-check that the tile rules are set up correctly. This is likely the culprit and something that requires some trial and error. But you can try; adding a debug log right before the backup tile is placed to understand why it's being chosen. Add a few more debug logs anywhere a tile should be placed/chosen to see how it may/may not be selecting things.
- Temporarily disable the backup tile to see if any other tiles are being selected.

##
---
Devon M. - 
Your project is shaping up nicely, keep up the great work. I like the the sound of the potential audio implementations. I would consider spatializing any of the sounds related to stationary objects like runes, etc. since you have the ability to walk around the space some. Also a "cave" Reverb Zone, which is one of the Unity options, would help with ambience as well. If you encounter any major hurdles or need specific help, don't hesitate to reach out via email. You're doing well, and I'm looking forward to seeing your final project!

##
---
Great progress on your cyberpunk game!

Honestly, I doubt you have much of a performance overhead with our post-processing given the size of the scene, but that is an important consideration. One thing is to utilize somethin like camera stacking and layers to be more selective of what gets post-processing, which overrides it gets, and how much of it is applies. Something else that is important is just setting all non moving/dynamic objects to static in the editor. it seems like a small thing and is easy to forget, but has major implications regarding batching for reducing draw calls.

I would watch out for the amount of intensity of some of the large lights in the scene, they are looking a bit blown out, but the adverts and smaller lights have a good about of bloom. Just needs some small tweaking.

It terms of your game, you can attach spatialized audio sources to things like cars with some engine sounds so if/when they pass by the camera those sounds travel around and seem more "real". A very good city ambience BG track would be good, there are some cyberpunk ones out there (https://www.youtube.com/watch?v=5tXeYhoa8uU). Also, just being very selective about what object get sounds and how those are triggered. Like doors opening, this can be a good trigger, adverts being activated/deactivated, weapons (if you have those) etc.

##
---

Fox-
Great progress on your environment and lighting. It's good that you've set up a solid foundation for showcasing your effects. If you are having trouble with the cinemachine post processing in URP, you may need to add a post process extension to the cinemachine virtual camera: https://docs.unity3d.com/Packages/com.unity.cinemachine@3.0/manual/CinemachinePostProcessing.html
Also check that the URP asset has all the correct post processing setup as well. It should, but doesn't hurt to double check.

##
---
Prasin - 
Great job on your progress. Your lighting and post-processing work looks like it's really enhancing the atmosphere of your game.
For the audio pitch shifting issue: So the sound cue system in the older system and its fictionality has mostly shifted to their MetaSounds workflow. Cues are more for just simple playback, if you want real-time modulation you need a metasound patch. Here are some easy to follow resources to get started: 

https://dev.epicgames.com/community/learning/tutorials/BKPD/unreal-engine-introduction-to-metasounds
https://www.youtube.com/watch?v=onxJszv9YEc
https://www.youtube.com/watch?v=ykpnCONGELY

So the Wave Player object has a pitch control on it, now, to access this vis blueprints you will need to first create an input (float type) for the pitch values in the MS patch. In BP, you will need an Audio Component, then use a Set Float Parameter to pass in the values to control the pitch object. The last video linked covers the basics pretty well.

You're in a good position for your final submission. Keep up the great work, and don't hesitate to reach out if you need any last-minute troubleshooting!

##
---
Pheobe -
You are on the right track with the shader. But two major changes. Your shader will need to be set to Lit not Unlit, this is because you need and emission property. You will also want to add a pretty high specularity and/or metalness value to the water shader as well. Also, your reflection robe box volume size is likely too small so increase the size. 
This tutorial is older, so the mater stack looks different, but connecting the cubemap should be the same basic process: https://www.youtube.com/watch?v=943P0dGR4rQ
Using reflection probes: https://www.youtube.com/watch?v=iGw5auyCvwc

##
---
Lilly - 
Good progress on your project. Your processing effects are really enhancing the atmosphere. I like sound of the audio implementation plans: For the splashing and wooden floor sound; Use trigger colliders on water bodies and wooden areas. Attach an audio source to the player and switch sound effects based on the surface they're walking on. Similar to what was done in the first audio lab. Keep refining these elements, and don't hesitate to experiment with subtle variations to find a good balance for your projects look and feel. Let me know via email if any major issues arise or you need help implementing s feature. 