---
tags:
  - teaching
---
## Lily Durand
  
So far I have not had the time to make any major improvements on my project outside of the goals for this week's progress report. I would say my biggest challenge so far is finding time outside of school, work, and other school work to make major progress on this game. Hopefully, my schedule will be a bit less tight in the coming weeks and I can flesh out the game further. 

As for what's been added since my last update, I have created a shader and particle system to denote my haunted fish. To be honest, I struggled a bit envisioning where I would want to use a shader in this game. They're not something I'm used to working with, and I don't want the look of this game to be too overwhelming. However, as stated above I did find at least one good use for them. 

I created a shader for my haunted fish that makes them pulse in color from dark to light purple, and has the fish wiggle along its x axis. I am very happy with the product that resulted from this, and I am still thinking of other potential shader opportunities for this game. Additionally, I honestly would not say I had any significant issues with the development of this feature.

## Feedback - Lily
Thanks for the update on your haunted fish game. Your progress is notable, despite the time constraints. Remember, you only need two shaders, so one more shader for the final. Focus on what enhances your game's atmosphere/feel most effectively. 
Additional shader suggestions:
1. Water shader: Could include day/night color shifts. https://www.youtube.com/watch?v=yJrc_ywpTJw
2. Emissive object shader: For atmospheric spooky lighting on key objects. https://www.youtube.com/watch?v=IKcgv7ZsBCI
Let me know if you need any clarification or have questions.
---

## Fox
For my assignment, I created a fireball shader. While in shadergraph, this is a simple shadercombining 2 noise maps with a fresnel map to give it a soft edge, in game view it created aninteresting distorted sphere which I quite like. I think this is a glitch because the shadergraphview shows something completely different but I really like how it looks so I’m going to hold onto it.

## Feedback - Fox

Bob Ross's "happy little accidents" certainly applies in game development too. It's interesting how the in-game result differs from the Shader Graph preview, but as you've discovered, these unexpected outcomes can sometimes lead to compelling effects.

Keep experimenting and iterating. If you need any help troubleshooting, let me know.

---

## Kristin
  
In this progress report I was able to add UI, a way to move around the game,thestart of placing items in the world, shaders and particles. The shader I have created sofar is a shader for my water that moves and has a custom moving image for the watertexture. I also have some controlled by code and editor window materials that havebeen created for the world generation. I have also created models for three tree typesand the houses. Most just still needs to be textured but my big thing was figuring outmodel placement, which I have been having a huge issue with.My current biggest issue that has really been holding me back is not being ableto get the objects (currently trees) to be able to be placed only on land and at thecorrect level. I talk about this in a little more detail on the video and hope to have thisissue fixed and work on adding in the models and finishing up the UI. For UI, I need tofigure out a click on a button that then allows you to place the object you clicked on. Ialso later plan to add nav meshes for people walking around and maybe cars driving,but placement needs to come first.

## Kristin - Feedback
Thanks for the detailed update on your project. Good progress on multiple fronts.
Reference code for tree placement (as previously discussed):
Feedback on other aspects:
- UI and object placement:
    - For click-to-place functionality, consider using a state machine pattern.
    - On button click, set a "placementMode" variable.
    - In Update(), check for mouse clicks only when in placement mode.
    - 
``` c#
public enum PlacementMode //define a PlacementMode enum to keep track of what the player is trying to place
{
    None,
    PlacingTree,
    PlacingHouse
    // Add more as needed
}

public class ObjectPlacer : MonoBehaviour
{
    private PlacementMode currentMode = PlacementMode.None;
    
    void Update()
    {
        if (currentMode != PlacementMode.None && Input.GetMouseButtonDown(0)) //only check for mouse clicks if we're in a placement mode.
        {
            TryPlaceObject();
        }
    }

    void TryPlaceObject() //handles the actual placement logic:It casts a ray from the mouse position (like before). If it hits terrain above water level, it places the appropriate object.
    {
        Ray ray = Camera.main.ScreenPointToRay(Input.mousePosition);
        RaycastHit hit;
        
        if (Physics.Raycast(ray, out hit, Mathf.Infinity, terrainLayer))
        {
            if (hit.point.y > waterLevel)
            {
                switch (currentMode)
                {
                    case PlacementMode.PlacingTree:
                        PlaceTree(hit.point);
                        break;
                    case PlacementMode.PlacingHouse:
                        PlaceHouse(hit.point);
                        break;
                }
            }
        }
    }

    // UI Button callbacks
    public void OnTreeButtonClicked() //called by UI buttons to set the placement mode
    {
        currentMode = PlacementMode.PlacingTree;
    }

    public void OnHouseButtonClicked()
    {
        currentMode = PlacementMode.PlacingHouse;
    }

    // Implement these methods to instantiate objects
    void PlaceTree(Vector3 position) { /* Instantiate logic here... */ }
    void PlaceHouse(Vector3 position) { /* Instantiate logic here... */ }
}
```
- NavMesh for NPCs:
    - Good idea, but I agree it should come after object placement.
    - Consider baking the NavMesh at runtime after terrain generation: https://www.youtube.com/watch?v=bELFjNNOfn0
- Shaders and particles:
    - Water shader looks good., try moving your size variable to the Cell Size input of the Voronoi (I think you were using that noise type) Consider adding simple foam or edge detection: https://www.youtube.com/watch?v=yJrc_ywpTJw
    - For other shader ideas, look into foliage. Stylized grass could work well: https://danielilett.com/2021-08-24-tut5-17-stylised-grass/
      https://nedmakesgames.medium.com/creating-a-foliage-shader-in-unity-urp-shader-graph-5854bf8dc4c2

Keep iterating. If you need more specific guidance on any of these points, let me know.

---
## Chris
In this Dungeons-and-Dragons fantasy, players create a shrine to a deity in a customizableenvironment.Users can choose the deity's body design and associated trinkets and plants. The shrine will thenbe assigned power based on these choices, each of which has a specific characteristic.Following the completion of the collection of 3D models and the creation of several low-polymodels using Maya 2025, I am presently working on developing a system that will enable theplayer to select statue components (heads, torsos, and limbs) that may be combined andrearranged in a manner that is analogous to that of a bespoke identity creator. The feedbacksuggested setting up specific spots on the shrine so users can switch between trinkets and plantsthat grow naturally there.This week I was trying to create a more familiar workflow while working with the URP shadergraph in Unity. I followed a tutorial that guided me in creating a shader in Unity. This shaderenables me to blend two textures over a base color, adjust the tiling and offset of each texture,adjust smoothness and ambient occlusion, and configure additional material options such asrender queue, GPU instancing, double-sided global illumination, and emission. This shaderwould be the start of the customization system for shaders I wanted. I still have some challengesmaking the textures work on the shader, but it's coming together well.I really like the suggestion of parameterizing my shaders to allow for a wide range ofappearances (metallic, stone, glowing, etc.). That not only adds an appealing style to the statue'scustomization, but also seems achievable in the short time I have.

## Chris - Feedback
It's great to see you're making progress with the shader development. 

1. Custom Stylized Maps in Shader Graph:
    - I love that you are creating you own custom textures with your style! Consider using that "master" shader that you are developing to blend multiple texture maps (you could use a URP Lit Shader as a starting point): https://www.youtube.com/watch?v=jVNC0Z2p9qw
        - Albedo (base color)
        - Normal map
        - Metallic/Smoothness map
        - Emission map
    - Use other tools to auto generate some of your maps from a single texture image: https://www.youtube.com/watch?v=zKYr3Ca-xqg
      Another (older) but good post on creating your own game maps from your texture images: https://tl.net/forum/sc2-maps/463734-creating-your-own-custom-textures
      Basically, you will be using a pseudo-PBR workflow to apply tour custom textures to your shader/material.

1. VFX Ideas:
    - Deity aura: Particle system that emits from the statue, color-coded to deity type?
    - Offering effects: Sparkles or small floating objects around placed trinkets
    - Elemental effects: Fire, water, air, or earth particles based on deity alignment
    - Spawn Effects: Particles/dust that spawns whenever a part is swapped our or an item is placed

Let me know if you need more specific guidance on implementing any of these suggestions.

---
## Jason
Progress- Removed the click and drag script.- Cleaned up wobble script.- Created new UI/buttons for ingredients in an auto layout group.o Created sprites for those buttons.- Created two scriptable object classes for ingredients and potions.- Created a brewing manager and a potion manager to handle main gameplay experience.- Created an audio controller for the sound I included.o Music is AI generated.o Sound effects are royalty free downloads.- Created a basic particle system that plays when a potion is created.Challenges- My project is starting to get really cluttered despite my best efforts, so I need to organize my assets.Questions- I don’t have any questions at the moment but I will use your previous feedback from my first report when working on the potion/bottle generation

## Jason Feedback
Thanks for the progress update on your potion brewing game.

Just some notes:
- Asset organization:
    - Consider creating folders/subfolders for Scripts, Prefabs, Materials, Audio, etc.
    - Scene Orginization can be handled with nested gameobjects (I do this and it helps a bunch)
      ---PARENT OBJECT---
        - Child object
            - Grandchild object
    - Use naming conventions consistently - MAT_material, VFXG_visualeffctgraph, SG_shaderpgraph, etc.
- UI and Scriptable Objects:
    - Good choice using auto layout and SOs for ingredients/potions. This will make scaling/expanding easier.
- Audio:
    - Nice addition of AI-generated music and sound effects. I'm curous how this has works out, it is going to be done a lot for indie/student work I believe.
- Particle system:
    - For the potion creation effect, consider varying particles based on ingredient types: color, size, intensity, etc.

No questions is fine. Glad to hear you're referring back to previous feedback for potion/bottle generation. If you encounter any specific issues while implementing features, don't hesitate to ask.

---
## Vanessa
ProgressCurrently, I’ve made good progress. I decided to pause on shaders while I got feedback,and focused on creating the final environment for my demo. I used assets from the Unity AssetStore to create a technical lab area that wasn’t too distracting from the main focus of the game.Then, to add cohesion, I finished development on my Toon Shader idea, which creates a cartoonoutline around any objects it is applied to. The outline can change in color and thickness, but I’mkeeping a consistent black outline for every object in the game so that it creates a cohesive lookfor the environment as well.ChallengesI am planning on finally finishing up the grime shader this week, which will also allowme to finish the VFX for the upcoming assignment. I will also put my different programs intoone big scene. I think my initial attempt at the grime shader was my strongest, so I should’vefocused more on that versus getting caught up in other attempts. Besides that though, I hadminimal issues with the environment and shader this week. I was having some issues with thematerial not functioning properly at first, but I found tutorials online that helped me.QuestionsAs I start thinking ahead, I’d ask what’s the best way to incorporate VFX into somethinglike the grime shader. My current plan is to have it attached to the cleaning script rather than theactual shader, focusing on the mouse clicks and movements so it appears to be working intandem with the shader (when really it's more about the script). If I wanted to have VFX withinshaders though, is that a possibility, and is it worth implementing in that way?
## Vanessa - Feedback
Thanks for the update on your project. It's good to see you're making progress and thinking ahead. 

Feedback:
Returning to your initial grime shader attempt is a good call. Sometimes first instincts are the strongest.

Regarding your question about incorporating VFX with shaders:

- Your current plan:
   - Attaching VFX to the cleaning script is a solid approach and what I would suggest.
   - It should allow for better performance and easier control of effects.
   - Something like some grime and dust flying up as the cleaning happens using the mouse click event to control the VFX playback.

- VFX within shaders:
   - It is possible, but can be complex and potentially performance-heavy.
   - Typically used for effects that are intrinsic to the material itself (e.g., dissolve effects, holographic looks).

- Hybrid approach:
   - Consider using shader properties to drive VFX parameters or visa versa with C#.
   - Example: Use shader's "cleanliness" value to control particle emission rate or color.

For your use case, sticking with script-controlled VFX that works alongside the shader is likely the most efficient and flexible approach. Let me know if you need any clarification or have more questions as you implement features.

---

## Vincent
The progress of my final project has been slow and steady, without much in the way ofmassive or explosive momentum. Much of my time was spent on the assets, dumping those intoUnity while making sure they were prepared to some extent. I chose not to texture the metalspecifically, however, inside of something like substance. Instead, I wanted to make it so I couldcontrol that sort of thing in the script itself later on.To that end, I created a shader graph to handle the metal, mentioned before. It’s beentested at least in appearance, and I believe it looks relatively solid when it comes to the swordsthemselves. Beyond that, that hasn’t been the only thing I’ve been working on, but merely theupdate on what I’ve done before. I specifically began work on a fire shader graph, to be used ina fireplace or forge. I’m not tremendously happy with the result, given that I think it looksperhaps not fuzzy or ephemeral enough to capture the fire feeling. Any advice on how tohandle that, since I think the real trouble comes from the Texture2D portion of the shader, wouldbe lovely.Lastly, I went beyond the remit of our initial progress check and made a vfx that used myoriginal shader. Specifically, sparks that fly, meant to play when the metal of the blade ischanged during the blacksmith simulator, accompanied by a clang of metal. This is actuallywhat I ended up liking the most, so if it is any consolation, exploring these concepts haveseriously helped me to discover the field I’ve had the most enjoyment with when it comes togame development. That’s the brunt of my progress of late.

## Vincent - Feedback
Thanks for the update on your blacksmith simulator project. It's good to see you're making steady progress. It's also so great that you've discovered some enjoyment in the VFX development stuff.

Feedback:
Asset preparation and importation into Unity is a crucial step. Good job on that!

Regarding your fire shader and VFX:

- Fire shader improvements:
   - To make the fire more fuzzy and ephemeral:
     - Try using multiple noise textures at different scales and speeds
     - Experiment with vertex displacement for more organic movement
     - Use a soft particle shader to blend edges (feathered edges) or maybe even a combo of a layered effect with soft and hard edges.
   - Consider using Voronoi noise for a more natural flame look
   - Adjust color gradients to enhance the fire's visual depth
     https://www.youtube.com/watch?v=XQlFokCzU6M

- VFX enhancements:
   - For the sparks:
     - Vary particle sizes and lifetimes for more random/realistic behavior
     - Add a subtle glow or emission to enhance the effect ( we will look at this soon)
   - Consider adding smoke particles to complement the sparks

- Sound design:
   - • The clang of metal is a good start. Consider layering multiple soun samples for richness.
   - • Add subtle ambient forge sounds for immersion (crackling fire, distant hammering, etc.)

Just a note: Think about how you can use your effects to provide clear feedback and enhance the overall user experience.

Let me know if you need any specific guidance on implementing these suggestions or if you have any other questions.

---

## Phoebe

## Phoebe - Feedback
Thanks for the detailed update on your island customization project.

Feedback:
For creating a combine skybox:
- SubGraph approach: https://www.youtube.com/watch?v=zElng0TRsY8
   - • Create separate SubGraphs for stars and clouds.
   - • In your main skybox shader, add these SubGraphs as nodes.
   - • Blend the outputs using a Blend node or custom blending logic.
- Texture-based approach: https://www.youtube.com/watch?v=WFSI3dR0DKA
   - • Render your star and cloud shaders to separate textures.
   - • In the main shader, sample both textures and blend them with a Blend node.

Quick tip: Start with the SubGraph approach. In this case, since they are already separate graphs, it may be the most straightforward for combining shaders.

Island height control: 
  - Good use of falloff map for natural-looking islands.
  - Think about adding noise to the height map for more organic terrain (if that is desired).
Water shader: 
  - The shader/material looks good! Consider making the water react to the day/night cycle (color shifts, reflection changes, etc.).

Keep iterating. If you need more specific guidance on implementing the combined skybox shader, let me know and I can try yo provide a more detail.

---

## Devin
For the Shader & Material Development component of my final project, Ihave my shader/material based off the previous assignment, but wasn’t ableto take the next big step I had wished for. However, I did find an importantissue and thankfully resolved it for this report. My hope with my mainshader/material is that I will be able to calculate the distance between theplayer and the vertices of an object, and have those vertices affecteddifferently based on that distance. If I can accomplish that, then theenvironment will naturally flow together visually as the player movesthrough it.The issue I found was that the material across all the objects in mydemonstration had the same values despite being at different distances. As Iunderstand it, because I only created public variables for gameobjects(player and object) and manually inserted them, the material only used thedistance variable for the most recent object variable. So I tweaked the scriptto refer to the object the script was assigned to, and that immediately fixedmy problem (you can see in my demo video).I think my only major questions would be how may I best affect theindividual vertices of a game object for the shader/material? Or if there’s nogood answer to that question, how else may I get a seamless result betweenthe environment’s meshes?

## Devin - Feedback
Thanks for your update on the shader project. I've prepared a Unity package demonstrating how to distort a mesh based on the vertex closest to the player. This should help you achieve the effect you're aiming for, hopefully.

Key points here:
- Uses Shader Graph's Vertex ID node to identify vertices
- C# script finds the closest vertex to the player
- Shader distorts the mesh based on proximity to this vertex

The package includes:
1. ClosestVertexFinder.cs: Calculates closest vertex
2. VertexDistortion.shadergraph: Applies the distortion effect (plus the test material)

To use (also in the readme here):
1. Apply ClosestVertexFinder to an empty GameObject
2. Set up references in the inspector
3. Apply VertexDistortion material to your mesh
4. Adjust Distortion Strength and Radius in material properties

This should give you a good starting point. Remember to consider performance in this case, especially for high-poly meshes.

---

## Prasin
  
My project was about making a chapel where you can enter the chapeland get some instructions, go outside, collect some flowers, and goinside the chapel, make a bouquet of flowers using the flowers, andthen put it on a grave.I'm pretty good in terms of shaders now that I have the one finalshader that I needed to make the art style kind of work together. Ireally wanted to highlight the dark and the light side in thisproject since I've been inspired by Rembrandt in recent while.In this video, I just went over to that shader which manages to takethe lighting data from the scene and sort of plugs it into emissionfor now. That should take care of any major shader issues that I willneed in this project. Since we're learning VFX and particles rightnow, I should be comfortable moving on to VFX without worrying aboutthe workload of shaders later on.I did not face any challenges, as mentioned last time in my previoussubmission, that I've been working with shaders in unreal for myfirst co-op so I am quite accustomed to these things.As for the 3d models and a bit of procedural work left to do, I willredo my overgrown vines since I don’t like the look of the one that Irecently made.
## Prasin - Feedback
Thanks for the update on your chapel project. It's great to hear you're making good progress!

Feedback:
- Shader Development:
  - Your Rembrandt-inspired shader for highlighting light and dark areas sounds intriguing. Rembrandt is one of my absolute favorites!!! His shadows can be very deep and muddy towards the edges, almost like a fog with very intense light areas, "chiaroscuro": https://en.wikipedia.org/wiki/Chiaroscuro 
    - Maybe there is some lighting/post processing that can be applied to achieve this affect as you mentioned in the video. Although, too be fair, Carravagio and Goya had more of that effect.

- Project Progress:
  - The concept of collecting flowers and creating bouquets for graves is engaging, I like it.
  - Consider how you might use VFX to enhance key moments (e.g., flower collection, bouquet creation, etc.).

- Next Steps:
  - For the overgrown vines, consider using something like L-systems if you have not looked at that already.

- Let me know if you need any specific advice as you move into VFX development or rework your vines, or anything else.

---

## Nate
This assignment was SUPPOSED to be in regards to the project’s shaderdevelopment, however I ultimately found the development of those aspects theleast important part of my final project development as I needed to know HOW toeven start with the city procedural development as I am NOT a coder. If it helps,I did make my shader assignment to ultimately be for this project so I am at leastnot making ZERO progress.However, I hope you understand that I feel a lot better knowing I have the actualprocedural aspect of the project somewhat built. I wanted to make substantialprogress in the technical aspect of the game/demo rather than work on things Ibelieved would not be (as) difficult to figure out despite my previous issues withshaders. This basically hung over my head more than the shaders which I justgot angry at rather than not understanding. The procedural generation aspectscared the crap out of me, and I am thankful many people have made tutorials onthis sort of stuff.While I have only worked on the base skeleton (I used a tutorial to make thegenerative aspect, I hope that is okay? I am not a programmer) I do know themain challenge will be using the assets from before to make a cohesive product,as they will all need to fit in near-perfectly. Hopefully that will be the fun part of

## Nate - Feedback
Thanks for your candid update on your project. It's understandable that you prioritized the procedural city development, as it's a core aspect of your project. 

Feedback:
  - Good call on tackling the aspect that worried you most. This proactive approach is commendable and Using tutorials for unfamiliar technical aspects is perfectly fine and acceptable.
  
  - It's good that you've at least incorporated your shader assignment into the project, this is very smart way to work. 
    I think for you, Emissive shaders/materials are going to be best for the city, and luckily there is quite a bit out there on them: https://www.youtube.com/watch?v=UScYhSAQpfU

  - As you move forward, consider how your shaders can enhance the procedurally generated city. Think about:
    * Time of day transitions (if you have those)
    * Signage and Holograms ( you could use tome time node trikery to get a flickering light effect too): https://www.youtube.com/watch?v=dkLUQ6XJVS0
    * Building material variations

  - Your concern about fitting assets into the procedural system is valid. Some tips:
    * Create a consistent scale system for your assets, they should be relative in scale to one another, look at asome of the modular asset packs as examples.
    * Use shader variants to add variety to similar models (this is done soo much in games and is totally procedural thinking as well)

Don't worry about deviating from the exact assignment structure. The goal is to create a cohesive project, and you're making progress towards that which is most important. 

Keep pushing forward, and don't hesitate to ask for help on specific shader or procedural generation issues as they arise.

---

## Lillie
  
For this check in I mostly just expanded on what I had before. A lot of this week was puttingthings together, modeling, and touching up what I already had. Part of the reason I did that wasto get the parts that would be needed for the coding to work I want to do first before I applyeverything together, which will probably be the next check in. Like I said in the video I goteverything I wanted to do this week done and I’m happy that I was able to get it all done withminimal setbacks. Also, it’s not really easy to tell but I’ve also been thinking about what I’mgonna do for the actual gameplay mechanics and balancing. I want the rage gimmick to be forthe power band, the spiked gloves raise flat attack, pegasus boots and winged cap raise speed,and the bulky boots raise defense alot but lower speed. Going forward I want to make some moredefensive oriented equipment as well.

## Lillie - Feedback
Thanks for the update on your project. It's great to hear you're making steady progress and thinking ahead about gameplay mechanics integration!

Feedback and general notes./suggestions:

- Shader Integration:
   - Consider how shaders could enhance your equipment visuals and actually communicate the gameplay.
   - Example: Pulsing effect on power band when rage is active

- VFX Opportunities:
   - Think about particle effects for speed boosts or skill activations
   - You could also use some mesh/skinned mesh particle emissions for different objects

- Balancing:
   - Good idea on attribute trade-offs (positive and negative feedback in games is crucial for balance) (e.g., defense vs. speed) https://machinations.io/articles/game-systems-feedback-loops-and-how-they-help-craft-player-experiences
      - Consider creating a simple spreadsheet to track and adjust these values


- Visual Feedback:
   - • Ensure each piece of equipment has a distinct visual identity or its own way of manipulating some visual properties af shaders and VFX to express its uniqeness. 
      - Use shaders or VFX to clearly communicate when effects are active

Let me know if you need any specific advice on shader implementation for your equipment effects.

---

## Anakin
  
Progress Report 2- In the past week, I've been working on developing shaders and materials for my project, focusing on creating a dynamic hologram flicker effect. The main progress I've made includes successfully implementing a C# script that controls the shader's `FresnelStrength` and `MinTransparency` properties, giving a realistic flickering appearance to the material. I also managed to make a fish model rotate smoothly in a circular path, facing the direction of its movement.- One of the main challenges I faced was figuring out how to properly animate shader properties in real-time. Initially, I struggled with getting the flickering effect to look natural, as it kept coming off too erratic or too subtle. After some experimentation with sine wave functions and adjusting the flicker speed, I found a good balance that looks both dynamic and believable.- Another challenge was ensuring the fish model rotated correctly along its circular path. The model kept moving sideways instead of facing forward. I resolved this by calculating the movement direction vector and using it to smoothly rotate the fish to always face its movement direction.- As for questions, I'm curious about other creative ways to manipulate shader properties through C#, especially for creating more complex animations like color transitions or texture blending.

## Anakin - Feedback
Thanks for the detailed update on your project. It's great to see you're making solid progress with shader development and object animation! 

Feedback:
Good job on balancing the flicker effect, this shows attention to detail. Also, nice solution for the fish rotation issue

Feedback and general suggestions:

- Shader Manipulation:
   - For color transitions, try lerping between colors in your shader:
     - Use a 'transitionFactor' property to get data from C# to the shader
     - Use lerp() in the shader to blend between colors (or textures)
     - Tweening, as I have shown, is an excellent way to handle material property animations (you could even try making your own animations in C# using `Time`): https://docs.unity3d.com/ScriptReference/Time.html

- Texture Blending:
   - Implement a multi-texture shader:
     - Use C# to control blend factors between textures
     - Experiment with different blend modes (add, multiply, overlay)
     - There is also a way to use subgraphs for this (more complex/advanced): https://www.youtube.com/watch?v=zElng0TRsY8

- Complex Animations:
   - Consider using noise textures for organic movement:
     - Sample a noise texture in your shader
     - Use the noise value to offset vertices or influence color
     - If you want to get more technical/advanced, use HLSL/GLSL: https://80.lv/articles/procedural-animated-organic-material-created-with-unity/

For your question about creative shader property manipulation:
• Use sin/cos waves with different frequencies for complex oscillations ( you can even combine waves for something more complex)
• Implement a simple particle system along with shader, controlled by C# parameters that affect both simultaneously.
• Experiment with UV manipulation for effects: https://www.youtube.com/watch?v=VxEN9djWGRQ

Let me know if you need anything more specific or further clarification.

---

## Benjamin
This week, I began work on the different materials I will be using for the various suit parts. I started with a glass material, as it was the material I was most concerned about due to some of itsunique qualities. I used some tutorials to create a shader graph, and in the end I’m pleased with how it turned out. I plan on using this material for the helmet visors, as well as any other miscellaneous suit parts that require glass. In addition, I may also use this material for the surrounding environment depending on how I design it.Looking forward, I need to create metal, plastic, and some sort of fabric materials. I will also need to make them customizable in terms of color so the user has full control over the color palette. Finally, I need to figure out how the erosion shader will work, as well as determine any other special effects that I will need shaders for.

## Benjamin - Feedback
Thanks for the update on your project.

Feedback:
- Color Customization:
   - Add some color parameters to your shaders including color lerps:
   - In Shader Graph, use Color nodes and connect them to your material properties using Blend or Multiply. 
- Different Materials: You will be using a PBR workflow to create different material effects by manipulating the basic shader parameters: https://www.alanzucconi.com/2015/06/24/physically-based-rendering/
	- Metal Shader:
	   - Focus on specularity and reflectivity
	- Plastic Shader:
	   - Blend between diffuse and specular reflections
	   - Add a smoothness parameter for varying plastic types
	- Fabric Shader:
	   - Consider adding a normal map for fabric weave patterns
	- Erosion Shader:
	    - Use noise/textures to drive the erosion effect
	   - Maybe Implement vertex displacement based on erosion intensity

For special effects, think about:
  - Energy shields (Fresnel-based glow): like from the lab
  - Holographic displays (scrolling UV + emission)
  - Active camouflage (screen-space distortion): https://www.youtube.com/watch?v=atPTr29vXUk

Let me know if you need more specific guidance on any of these shader implementations.

---

## Devon
Currently, for my final I was able to set up a very rough blockout for the environment and start to
get a feel of what the end result will look like. I ended up starting my code from scratch and
thinking of a better way to implement my combination code using scriptable objects. I was able
to get to a point where you can add items into the cauldron and can access the data in that one
script. This will make it easy to create combinations and results all in one script.
When it comes to shaders and materials, I already know the amount of shaders I will
have to create and what effects they will have. I feel like a lot of these shaders are similar which
will help out in the long run and I will be able to create many variables to get different effects
from one shader, for example, the Break, Shatter, and Crack effect are essentially all the same
shader just different intensities which I can create variables for. As of the shaders that I have
right now, I have the same shaders from last week's assignment that I believe are useful for
more “Background effects” such as the water in the cauldron that I currently have. I believe that
these larger effects will have more to do with the VFX graph so I will be working on completing
those for the upcoming assignment and hoping to knock out a few of these shaders that I need.

## Devon - Feedback
Thanks for the detailed update on your project. Your use of a Miro board for planning is great - it's an excellent practice for project management and visualization.

Feedback:
Environment Blockout:
  - Good start. This will help you get a sense of scale and spacing.
  - Consider how your shaders and VFX will interact/look with this environment. Doing something like a drawover using a screenshot is always good. 

Code Refactoring:
  - Smart move to restart with scriptable objects for your combination system.
  - This should make your code more modular and easier to maintain.
  - This happens quite a bit too as projects go along.

Shader Planning:
  - Your approach to creating versatile shaders with variables for different effects (Break, Shatter, Crack) is efficient and modular.
  - Consider creating a "master" shader that can handle all these variations:

Your methodical approach to planning and development is great to see. Don't hesitate to ask if you need specific advice on shader implementation or VFX as you start to tackle that stuff.

---

## Braden
For this assignment, I completed two scripts that populate the plants fully on Start. I thought it'd be important to have all the logic ready for when I implement the greater growing and time systems, which will be a much larger task. I also 3D modelled three unique parts for each segment of the plant. (Stem, middle, and bloom) The 3D models were carefully modelled in Maya and edited to have proper pivot points for easier procedural generation. I also designed the generation method to keep in mind where to instantiate the next model rather than just having it instantiate at the meshes highest y value. This means the parts can slope and swerve in any direction, leading to more plant variety. Now that this is done, I can begin implementing the time and growing systems which I'm excited to do.

For this submission, I've created a plant shader that lerps between a healthy green shade and an unhealthy brown shade depending on the growth factor of the plant. Without the greater plant growing mechanics in yet I wasn't able to hook it up, but I hope to get that in soon. I also want to go further by having the plant reflect its health in texture and posture. (e.g. having it rot or droop if unhealthy)

## Braden - Feedback

Hello. Thanks for the update on your plant project. It's great to see you're making progress.

Feedback and Suggestions:
- Procedural Generation:
   - Good thinking on pivot point placement for varied growth patterns
   - Consider adding randomization factors for more natural variety
	- Depending on mesh build, this could be for individual component transforms or for the entire plant growth.

- Plant Health Shader:
   - Nice start with color lerping based on health. Something that would be good to see in blending that with texture lerping as well.
	- https://www.youtube.com/watch?v=WFSI3dR0DKA
	- https://www.youtube.com/watch?v=zElng0TRsY8
- Possible Enhancements:
   - For drooping effect, consider subtle vertex displacement in your shader, or just creating a nice wind/foliage effect with vertex displacement
	   - https://www.youtube.com/watch?v=alPzRZEybdk
   - For rot effect, use a noise texture to drive opacity in unhealthy areas
- For the plant growth, one idea could be to have various plant models as different stages, then use some coroutine or other scripting to dynamically swap meshes for growth and decay. This could be paired with texture/shader/VFX parameter changes in real-time as well.
- Or it could be a shader: https://www.youtube.com/watch?v=LKaEMBLIw9s

Let me know if you need any specific guidance on shader implementation or growth mechanics.
