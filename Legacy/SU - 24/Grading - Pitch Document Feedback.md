Grading Scale:

D:64 - C: 70 - B-: 80 - B: 84 - B+: 87 - A-: 90 - A: 94 - A+: 100

---

- [x] **Anakin - "Neon District"** ✅ 2024-07-04

Anakin, I've got to say, your "Neon District" concept is looking pretty solid! You've clearly put a lot of thought into how you're going to bring this cyberpunk cityscape to life.

I'm particularly intrigued by your approach to using pre-existing assets in a modular way. That's a smart move - it'll give you a good foundation to build on. But have you considered taking it a step further? Here's a wild idea: what if you used something like OpenStreetMap data to generate your city layout? Imagine basing your neon-drenched streets on real-world locations like Philadelphia. That could add an interesting layer of familiarity-meets-futurism to your project.

Your technical breakdown is comprehensive - I like how you're planning to cover all the course modules. The custom shaders for neon signs and holograms sound particularly cool. Emissive materials, which we will touch on, will be a boon for this style.

The particle effects for rain and steam are a great touch. They'll really help bring your city to life.

Speaking on lighting, your plan for dynamic lighting to create the neon atmosphere sounds awesome. A good skybox would be great for this, you may even be able to incorporate some ay/night lighting. 

Your production pipeline looks well-thought-out. As you move forward, keep thinking about how you can push the procedural aspects in each stage.

---

- [x] Mosadi - Tank Mechanic ✅ 2024-07-04

Mosadi, your "Tank Mechanic" concept has potential for an engaging, prop-focused experience. The idea of customizing and then testing a fantasy tank is intriguing. Let's explore some aspects of your pitch:

The core concept is solid and seems manageable.

Regarding the procedural generation, you've listed several tank components, but I'm wondering about your approach. Have you considered using a modular system with a main "body" GameObject as a base? This could serve as the central hub with pivot points for attaching other procedurally generated parts. This approach might help you manage the complexity of having interchangeable parts on a moving object. The main body, will house movement logic and points for attaching parts procedurally. Or alternatively, you can choose t focus on a single tank, with a few various swappable parts, all modeled procedurally. 

Your technical breakdown touches on several course modules, which is great. Custom shaders breakdown is good and we will touch on emissive materials, which will be great for lights. The dynamic particle simulation for exhausts and explosions sounds exciting as well.

I'm particularly intrigued by your idea for a reactive sound system. How might you procedurally generate sound based on the tank's properties? Consider how you might blend different audio samples based on the tank's weight, speed, and surface material it's driving on. We will touch on some of these things, like surface material sounds.

One area that needs more thought is the interactivity. How will players interact with the customization process? For the sandbox testing, what kind of environment are you envisioning? Will there be obstacles or targets?

Lastly, your pitch doesn't include a production pipeline. Breaking down your workflow and identifying which tools you'll use for each stage (Unity, 3D modeling software, C# scripting) would help you plan your time more effectively.

---

- [x] Patrick - Chrome Caves ✅ 2024-07-04

Patrick, "Chrome Caverns" sounds like an intriguing concept! I'm curious about a few things though. First off, what's the main focus here - the cave environment, the mineral props, or the enemies? While it's tempting to tackle all three, you might want to zero in on one to really showcase your skills.

I'm particularly interested in how you're thinking about procedural generation. I really see this in two ways based on your pitch. Either, you might create diverse cave layouts algorithmically. Or how about a mineral placement and enemy spawning system? Any ideas on how these might work together in a procedural system?

That color-based power-up system sounds cool. How do you envision generating these minerals with their varying properties? This could be a great opportunity for shader development too - especially with that monochrome base and colorful mineral contrast.

Just a friendly reminder - while your game idea is exciting, remember that the focus of this course is on asset creation through procedural methods. How might you distill this down into an interactive demo that really shows off some design and  procedural workflows?

Your production pipeline looks solid, consider how you'll weave procedural techniques throughout each stage. Basically your 'Asset Creation' step makes for a good use of the course modules.

---
- [x] Phoebe - BYOI ✅ 2024-07-04

Phoebe, your "BYOI - Build Your Own Island" concept is looking pretty solid! You've really thought through how to incorporate all the course modules into a cohesive, interactive experience.

I'm particularly impressed with your procedural modeling ideas. Using sliders to control terrain height, foliage distribution, and other island elements is a great approach. Have you checked out Unity's terrain generation tutorials on BB Learn? There's one that covers hexagonal style terrain, which I noticed in one of your visual target images. That could be a cool direction to explore!

Your custom shader plans sound intriguing. The height-based color gradient for the terrain is a clever idea. Depending on how the terrain in generated, you may have room to explore shaders to cover foliage and have height map generated differently. 

The particle effects for falling leaves and swaying grass will really bring your island to life. How about adding some water effects too (this can also be done though shaders)? A gentle shore wave could add a lot to the ambiance.

I love the idea of the photo mode with customizable effects. It's a great way to let players showcase their creations. Have you thought about adding any post-processing effects to enhance the low-poly style, we will cover PP and photo modes in game often have filters that can be created through PP?

The production pipeline looks well-thought-out.

---

- [x] Lily - Abyssal Catch ✅ 2024-07-04

Lily, your "Abyssal Catch" concept seems to have a great blend of quirky humor and intriguing gameplay mechanics.

Planning to use procedural generation for the fish to add a ton of variety and replay value is good. Have you thought about how you might visually represent the different fish characteristics? Maybe some subtle color variations or unique patterns could hint at a fish's difficulty or possessed status? This would allow for a good blend of parametric design for modeling and shaders to work together. 

Your upgrade system sounds solid. I'm curious about how you're planning to implement the day-to-night cycle, possibly as a game mechanic, Night time = more possessed fish opportunity, etc.. C

The possessed fish mechanic is a great touch - it adds an element of surprise and risk/reward that could keep players on their toes. Have you considered how you might visually or audibly cue the player that they've hooked a possessed fish, or any different fish for that matter?

Your water splashing effects sound great for immersion. Your interactivity description is thorough - I like how you've broken down the different gameplay elements.

Your production pipeline looks solid. As you move forward, keep thinking about how you can best utilize procedural aspects like parameters in each stage to aid in development.

---

- [x] Vincent - Blacksmith Simulator ✅ 2024-07-04

Vincent, your "Blacksmith Simulator" concept sounds like it's really starting to take shape conceptually! I love the idea of putting players in the shoes of a blacksmith - it's a great premise for a prop-focused experience.

Your plan to focus on sword crafting is smart. It gives you a manageable scope while still offering plenty of room for creativity and technical challenges. If the system is built modularly, you should have little trouble expanding to different melee weapon types in the future. Have you thought about how you might use procedural generation to create variations in the blade shapes or hilt designs? That could add some extra depth to your modular system.

I'm really intrigued by your fire-based lighting idea. Real-time lighting can be tricky, but it'll add so much atmosphere to your smithy. Have you considered using particle systems to enhance the fire effects? Might be a cool way to add some extra visual flair. Post processing effects can help with atmosphere as well. 

Your material plans sound solid. Using Substance for the metal materials is a great choice. Have you thought about how you might represent the heating and cooling of metal in your shaders? That could be a really interesting technical challenge. You will also need to be sure you meshes for the sword parts have consistent and predictable UVs.

I like your approach to interactivity with buttons and sliders. It's straightforward and user-friendly. Have you considered adding any tactile elements to the smithing process? Maybe some simple mouse gestures for hammering or shaping the metal could add to the immersion.

Your production pipeline looks well-thought-out. It's great that you're aware of your strengths and the areas where you might need to put in extra work. Don't worry too much about the coding - remember you can make use of AI and I will be there to assist with coding as well.

---

- [x] Prasin - Chapel ✅ 2024-07-04

Prasin, your "Chapel: A Tribute to the Creator" concept is stunning!  I love how you're blending gothic architecture with lush, natural elements. It's a beautiful premise for an environment-focused experience. Something I am sure you can pull off.

Your technical breakdown is comprehensive. I'm particularly intrigued by your plans for procedural modeling. The idea of generating vines and overgrown thickets procedurally is fantastic - it'll add so much organic variety to your scene. Have you considered how you might use Unreal's Houdini Engine integration for some of these procedural elements? Vines are simple to do in Houdini and the getting them into Unreal is also fairly easy.

Your shader plans sound challenging but rewarding. The wind simulation on flora and the environmental blending will really bring your scene to life. And that strong Fresnel outline for highlighting flowers is a clever touch for guiding player interaction.

I'm excited about your VFX ideas, especially the blowing leaves and insect swarms. These small details will add so much to the atmosphere. Will you be using Unreal's Niagara system for these effects?

Your lighting setup sounds beautiful. The contrast between the sunlit outdoors and the candlelit chapel interior could create some really striking visuals.

The interactive elements you've outlined create a nice, focused gameplay loop. It's great that you're thinking about UI early - keeping it minimal will help maintain the immersive atmosphere you're creating.

Your production pipeline is well-thought-out. I appreciate that you're planning for optimization from the start - that'll save you headaches down the line.

---

- [x] Braden - Project Botany ✅ 2024-07-04

Braden, your "Project Botany" concept sounds like it could be something special. I love the idea of bringing a realistic gardening experience to mobile devices.

Your inspiration from Flower Town and Stardew Valley is a great starting point. The timed upgrade mechanic from mobile games like Clash of Clans is a clever way to encourage daily engagement. It's a nice balance between game design and simulating the real patience required in gardening. Another consideration is possibly using growth simulations from a tool like Houdini (which does plants well) as a different take on visually representing the plants growing. 

Your procedural generation plans for the plants sound exciting. Have you thought about how you might use algorithms to determine growth patterns / plant response based on the care given? 

The idea of flexible materials and shaders for the plants is smart. It'll give you a lot of room to create unique-looking flora. Have you considered how you might represent different states of health or growth stages in your shaders through parameters?

Your focus on effects and polish is great - those little details can really make or break the user experience in a game like this. For the VFX, have you thought about particle effects for things like water droplets or fertilizer dust, or falling leaves (for pruning)? And for SFX, maybe some subtle ambient nature sounds could add to the relaxing atmosphere?

The camera effects for transitioning between gameplay states sound like a nice touch. Have you considered any post-processing effects to enhance the cozy vibe you're going for?

Your interactivity breakdown is thorough. Your production pipeline looks solid. Using project planning software and GitHub is a smart choice for task management and version control.

---

- [x] Danny - Dungeon Crawly ✅ 2024-07-04
Danny, your "Dungeon Crawly" concept sounds like it could be an engaging experience! I love the idea of combining procedural generation with puzzle-solving and atmospheric exploration.

Your plan for procedurally generated levels is a great way to keep the game fresh and challenging. Have you considered looking into maze generation algorithms in Unity? Even though you're working on a dungeon, these algorithms could provide a solid foundation for your level layout. You could then swap out the maze elements for your dungeon walls, floors, and ceilings. I'll be posting some tutorials on our BB Learn site that might help you with this.

If you're feeling adventurous and want to take your procedural generation to the next level, you might want to explore `Wave Function Collapse` algorithms. This could give you even more complex and interesting dungeon layouts.

Your shader ideas for the torch lighting sound really atmospheric. And for the particle systems, consider how you might use them to hint at hidden passages or objectives, as well as enhance the torch.

I like your approach to the puzzles with hidden runes. It's a clever way to encourage exploration and make good use of your lighting mechanics. Have you considered how you might procedurally generate these puzzles to match your procedural levels? Maybe something like a percentage for a wall or floor tile to contain hidden runes.

Your production pipeline looks solid. As you move forward, keep thinking about how you can push the procedural aspects in each stage.
One thing to consider: how might you use audio to enhance the procedural nature of your dungeon? Perhaps different areas could have subtly different ambient sounds? We will look at using Reverb Zones to creating differences in sound propagation for different spaces.

---

- [x] Devin - Entropy ✅ 2024-07-04

Devin, your "Entropy: Explore the Chaos" concept sounds fascinating! I love the idea of a morphing, procedurally generated environment that changes as the player interacts with it. It's a great premise for an environment-focused experience.

Your plan for procedural generation using modular assets is solid. It's a smart way to create variety while maintaining control over the overall aesthetic. Have you considered looking into wave function collapse algorithms? This could be a really interesting way to generate your levels or "dungeon" layouts. It might give you even more complex and unpredictable environments, which fits perfectly with your chaos theme.

Your shader plans could use some expansion. Will they be for walls? Torches/Lights? Ambient Goop? Have you thought about how you might use these shaders to visually represent the transition between environments as well?

The immersive fog system is a great touch. It'll add a lot to the mysterious feel of your environments. Have you considered how you might use this fog dynamically? Maybe it could react to the player's movement or the opening of doors?

I'm intrigued by your plans for volumetric lighting. That, combined with the depth-of-field effect, should create some really striking visuals. Just be mindful of performance, especially with procedurally generated environments.

Your reactive ambient audio system sounds like it'll add a lot to the immersion. Your production pipeline looks well-structured. 

---

- [x] E - Punch Buddy ✅ 2024-07-04
E, your "Punch Buddy Demo Room" concept sounds like a fun and unique prop-focused experience. I love how you're taking a specific element from a larger game and really diving deep into it.

Your procedural generation system for the license plates sounds impressive. The variety of options you're including - fonts, colors, and realistic ID codes - will give you a lot of room for interesting variations. There is a Procedural Toolkit for Unity that has a 2D character generator that may be useful in helping to build out something else 2D like the plates. Having those identified parameters will really help with the knowing what to generate/randomize.  

Your visual target looks great - I like the simplified, vectorized style you're going for. It should work well with the toon shader you're planning to implement. The one thing with most toon shaders is they work best on objects that have some curvature, so just flat boxes, may bot show as well, but rounded edges should. 

The VFX for punching and dizziness sound fun. Have you considered how you might use particle systems to enhance these effects? Maybe some flying sparks or pieces of metal when a plate is damaged?

I'm intrigued by your plans for randomly generated punching audio. That's a clever way to add variety to a repetitive action. Having  some samples and randomizing pitch shifting or other parameters could work well. 

Your interactivity plan with the three different punch outcomes is solid. It's a simple system that should be easy for players to grasp but still offer some unpredictability. Your production pipeline looks well-thought-out. It's great that you've already got most of your art assets complete. As you move forward with the Unity implementation, keep thinking about how you can push the procedural aspects. 

---

- [x] Nate - Cassette Punk ✅ 2024-07-04

Nate, your concept of a procedurally generated "Cassettepunk" city is intriguing. However, I'd like to see more specifics on how you plan to implement the procedural generation. There are a couple of approaches you could consider:

1. Procedurally generated buildings: This would involve creating a system to generate unique building structures algorithmically. This approach allows for a high degree of variety but requires more complex algorithms.

2. Procedural city layout with pre-defined assets: This method involves generating the city layout (streets, block sizes, etc.) procedurally, then populating it with pre-made building assets. This approach is often more manageable and still provides significant variety.

Given your focus on the overall cityscape, I suspect you're leaning towards the second approach. If so, consider detailing:

- How will you generate the street layout? Will you use a grid system, or something more organic?
- What parameters will control the city generation (density, district types, etc.)?
- How will you handle asset placement to ensure buildings fit properly and look natural in the environment?
- Will you incorporate any procedural detailing for the buildings themselves, like varying textures?

For the VFX and Image effects there are some post-processing effects that can give you the VHS look very easily. It's about finding the right combination and parameter values. The glowing effects are going to come from emissive materials and bloom PP. 

Also, consider how your procedural system might interact with the other technical elements you've mentioned, like the neon lighting effects or the retro-futuristic UI. Could these elements also be influenced by your procedural generation?

Just a pointless note: Your visual target is very Cyberpunk / Synthwave, especially color palettes. Cassette Futurism / Retrofuturism is a bit more 1960's - 70's. More muted colors and rounder shapes overall. 

---

- [x] Chris - Make Your Maker ✅ 2024-07-04

Chris, your "Make Your Maker" concept presents an intriguing blend of fantasy elements and procedural generation. The idea of allowing players to create personalized deity shrines is creative and offers numerous opportunities for technical showcase.

Let's delve into some aspects of your proposal:

1. Procedural and Modular System:
   Your plan to use a modular system for shrine assembly is solid. Consider how you might push this further:
   - Could you implement a system where statue parts (heads, torsos, limbs) can be mixed and matched?
   - How might you procedurally generate variations in plant growth or arrangement? The entire area could be a series of snapping points and sectioned spaces for pseudo-randomly scattering plants and other shrine accessories. 

2. Shader Development:
   The idea of customizable statue shaders is promising. Some thoughts:
   - Consider how you might parameterize your shaders to allow for a wide range of appearances (metallic, stone, glowing, etc.). Look into how different materials are actually represented through shader parameters, like Specular-ity. 
   - For the mystical plant shaders, think about how you could incorporate subtle animations or effects to enhance their otherworldly nature (this could be through some subtle particles)

3. Particle Effects:
   Your ambition for shrine-specific effects is exciting. To make this more achievable:
   - Consider creating a base particle system that can be modified by parameters (color, shape, speed) based on the shrine's attributes
   - This approach could allow for unique effects without needing to create entirely separate systems for each type

4. Lighting and Camera:
   Your ideas here are good, but could be expanded:
   - Consider how dynamic lighting could change based on the shrine's attributes
   - For camera effects, think about how you might use post-processing to enhance the mystical atmosphere

5. Audio Implementation:
   This area could benefit from more detail:
   - Consider how you might layer different audio elements based on the shrine's attributes

6. Interactivity:
   Your UI-based interaction system sounds functional. Some additional thoughts:
   - Consider how you might make the shrine-building process more immersive. Could players physically place objects in the scene?
   - Think about how you might provide feedback to players about the "power" of their shrine as they build it (vfx, colors, sound, etc.)

Remember to keep your scope manageable. It's better to have a polished experience with fewer, well-implemented features than a broader but less refined project. Focus on pushing the procedural aspects of your core features to really showcase your technical skills.

---

- [x] Vanessa - Retro-Active Revive ✅ 2024-07-04

Vanessa, your "Retro-Active Revive" concept is really fascinating. The idea of restoring vintage electronics is not only nostalgic but also presents some interesting technical challenges.

I'm particularly impressed with your plans for procedural generation of dirt, rust, and wear patterns. If that props to be restored are also modularly designed, like the lightsaber example, it will be important to have the individual components be consistent and contain UVs as this is where the procedural textures will eb applied. Have you considered how you might vary these patterns based on the type of device? For instance, a camera might accumulate grime differently than a game console.

Your shader ideas sound promising. The grime shader, in particular, could be quite complex. You might want to think about layering different types of dirt/effects.

The modular assembly system is a great touch.

I like your plans for particle effects and lighting. These elements can really enhance the satisfaction of the cleaning process. Have you thought about how you might use lighting to guide the player's attention to areas that need cleaning?

Your audio plans are intriguing. The idea of changing ambient sounds based on cleanliness is clever. You might want to explore how you could blend different audio layers procedurally to achieve this effect smoothly.

Your production pipeline looks well-structured, and I appreciate that you've built in time for polishing at the end.

---

- [x] Kristin - Town Builder ✅ 2024-07-04

This is an interesting concept, Kristin. Your "Town Builder" idea has a lot of potential for showcasing procedural generation and modular design skills.

I like your approach to world generation. Have you considered how you might make the starting land more varied? Perhaps you could incorporate different biomes or terrain features to give players more diverse starting points, like selecting a Jungle starting biome.

Your modular system for roads and buildings sounds promising. You might want to think about how these elements could interact with the procedurally generated terrain. For instance, how might road placement adapt to hills or valleys?

The shader development for land could be fairy complex if it is aiming for specifics of the terrain like mountains, water, etc. A general shared for the Look dev of the land (i.e. a toon shader) could be simple, this could be mixed with somethin like water and foliage shaders. 

I'm intrigued by your plans for the town's inhabitants. How do you envision their behavior being influenced by the player's choices? 

Your production pipeline looks solid, but don't forget to allocate time for testing and refining your procedural systems. As you develop this project, keep thinking about how you can push the procedural aspects. Could you generate unique characteristics for each town?

---

- [x] Cooper - Ricky's Rolling Ruckus ✅ 2024-07-04

Cooper, I appreciate your on-time submission for "Ricky's Rolling Ruckus," but your pitch needs significant refinement to meet the requirements of this assignment. 

First and foremost, you need to decide whether your experience will be prop-focused, character-focused, or environment-focused. Remember, we're not working on a full game here, but rather a polished technical demo that showcases specific skills from the course modules.

Your visual target section is quite sparse. You should provide more concrete visual references once the concept is more fleshed out

The technical breakdown is lacking detail. We need to see how you plan to implement procedural generation and other course-specific techniques. How will you use shaders, particle effects, or procedural audio? These are key elements we're looking for in this project.

Your interactivity description is too game-oriented. Focus more on how users will interact with the specific technical elements you're showcasing in the limited-interaction build. You've omitted the production pipeline entirely. It is important to see your planned workflow and tools.

I'd suggest revisiting the assignment requirements and revising your pitch accordingly before presenting to the class next meeting. Focus on one aspect (prop, character, or environment) and detail how you'll use procedural techniques to bring it to life. Think about how you can create a focused, interactive experience that demonstrates your technical skills rather than a full game concept or MVP.

Lastly, I know I have made the use of LLMs and Generative AI acceptable for the course (and I do not plan to change that), but it is important to use if responsibly and ethically as per Drexel policy. At the very least remove the whole "Certainly!..." bit and read the assignment description in full before attempting to ask a GPT to address its content.

---

- [x] Benjamin - ??? ✅ 2024-07-04

Thank you for submitting your initial idea for a space-themed environment. While the concept has potential, your pitch falls short of meeting the assignment requirements in several key areas:

1. Project Title and Tagline: These are missing entirely.

1. Concept Overview: Your description is vague and lacks the specificity we're looking for in this assignment.
	1. Based on what was submitted: Spacesuit Centerpiece: The customizable spacesuit is an excellent prop to showcase. Think about how you could use procedural techniques to generate variations in suit design, colors, or patterns. Much like the lightsaber demo, you could have a base suit with points for snapping and swapping out parts. You could also explore shader development to create interesting material effects for the suit.

3. Visual Target: The few images provided do not do an adequate job of showing what your intentions are for the experience. They do however, show what the space the suit may live in is. 

4. Technical Breakdown: There's no detailed list of the key technical features you plan to implement. It is important to see how you'll incorporate procedural generation, custom shaders, particle effects, and other course-specific techniques.

5. Interactivity Description: Your explanation of how users will interact with your creation is missing.

6. Production Pipeline: You haven't outlined your planned workflow or the tools you intend to use.

Remember, this assignment isn't about conceptualizing a full game, but rather creating a focused, interactive experience that demonstrates some technical and artistic skills through procedural generation and other techniques we will cover in the class.

I encourage you to revisit the assignment description and revise your pitch to address each required element in detail before presenting next meeting. Think about how you can use procedural techniques to bring your space station / space suit to life, and how users will interact with what you create.

---

- [x] Fox - Jump Robot Death ✅ 2024-07-04

Thanks for submitting your pitch for "Jump Robot Death" You've got an intriguing concept here with the procedurally generated robot parts for the character. It's certainly a unique take on the character-focused experience for the final.

I appreciate the clear inspirations you've listed and the breakdown of the robot components. That's a good start for thinking about your procedural system. Here are a few areas where your pitch could use a bit of expansion:

2. Technical Breakdown: Your robot construction system sounds interesting, but we'd like to see more about how you'll implement the other modules we will cover in class. How might you use custom shaders or particle effects, for instance? And have you considered how you might incorporate audio?

3. Interactivity: Your description of the gameplay is vivid, but try to focus more on how users will interact with the procedural elements of your experience. How will they engage with the randomly generated robot parts, for example? Will there be a UI or is it totally random, you get what you get?

4. Production Pipeline: Your outline is a good start, but it would be helpful to know more about the specific tools you plan to use at each stage. Is this all in Unity? DO you plan to source assets or model them?

Overall, you've got some creative ideas here, but remember that the main goal is to showcase technical and artistic skills.

Keep developing these ideas - I'm looking forward to seeing how you refine this concept into a focused, impressive demo!

---

- [x] Jason - Alchemist's Workshop ✅ 2024-07-04

Jason, I'm impressed with your pitch for "The Alchemist's Workshop." You've done a great job of presenting a cohesive, prop-focused experience that aligns well with our course objectives.

Your visual target is particularly strong. The mood board you've provided gives a clear sense of the mystical, slightly whimsical atmosphere you're aiming for.

I appreciate how you've broken down the technical aspects of your project. Your plans for procedural generation of potion bottles and ingredients show a good understanding. Do you plan on generating different bottle shapes, and are those in anyway linked to the potential alchemic ingredients?  Parametric design will work well for this type of project both in models and shaders. 

The custom shaders for glowing liquids and magical auras sound especially intriguing. Have you considered how you might use these shaders to visually represent different potion properties?

Your interactivity description provides a clear picture of the user experience. The step-by-step process from ingredient selection to potion testing gives a good sense of the gameplay loop.

Your production pipeline looks solid.

---

- [x] Lillie - All My Fellas ✅ 2024-07-04

Thanks for sharing your "All My Fellas!" character creator concept, Lillie. You've got some interesting ideas here, particularly with the procedural generation of character add-ons and their effects on gameplay.

Your visual target provides a good sense of the colorful, dynamic style you're aiming for. The range of character types shown gives a nice indication of the variety you're hoping to achieve.

I appreciate how you've broken down the technical aspects of your project. Your plans for procedural and modular modeling sound promising. There is a nice demo in the 'Procedural Toolkit' for unity posted on BB Learn that has s 2D character generation. I'm particularly intrigued by your idea for a reactive shader for customizing equipment colors and designs. Could you elaborate on how you envision this working?

Your particle effects ideas for different equipment types are a nice touch. This could really help bring the characters to life and provide visual feedback on their abilities.

The interactivity description gives a clear picture of the user experience. The idea of testing characters in a small arena is great - it provides immediate feedback on the effects of the player's choices.

Your production pipeline look good. You may want to double-dip a bit and work on the UI selection while working on the character generation to test the UI and feedback. 

---

- [x] Devon - Enchanted Cave ✅ 2024-07-04

Devon, thanks for sharing your concept for "The Enchanted Cave: Unveiling the Secrets of the Magic Tome." This is an intriguing prop/VFX focused experience that seems to align well with our course objectives.

Your mood board is excellent, providing a clear visual direction for the mystical and atmospheric environment you're aiming to create.

I appreciate the detailed breakdown of your technical features. Your plans for procedural modeling, particularly the idea of generating different shapes for book emissions, sound promising. Have you considered how complex these shapes might be? And how player choices will change/effect the book look? I would not worry about generating the terrain. However, a nicely designed set could help frame the book and you could even have some elements in the background changed based on the book and player choices. 

Your shader development ideas are solid. The modular dissolve/reappear shader could be visually striking. I'm curious about how you might use this in conjunction with your procedural effects to create unique visual experiences.

The particle and VFX system plans sound exciting. The idea of generating different effects based on ingredient combinations offers a lot of potential for variety and player experimentation. How might you ensure that these effects remain visually coherent while still being diverse?

I like your thoughts on dynamic lighting affected by book emissions. This could really enhance the atmosphere of your cave environment. Maybe have a script or scriptable object that stores color information from potion combinations and uses that color to affect the lighting color as well. 

Your production pipeline looks well-structured. I appreciate that you've included time for polish and optimization.

---

- [x] Bashira ✅ 2024-07-08

Bashira, thanks for sharing your concept for "Am I the Only One Here?". This environment-focused, audio-centric experience sounds really interesting and has the potential to create a truly immersive and eerie/horror atmosphere. From what I've seen you are the only ne tacking a procedural spawning system, and the audio-focused experience is awesome

Your visual target is strong, providing a clear sense of the abandoned, creepy hospital environment you're aiming to create. 

I appreciate your technical breakdown. The idea of randomly generating the locations of photograph targets is a good use of procedural generation. Will you be sourcing the assets for the environment, like the buildings, etc.?

Your shader development plans for grungy surfaces and sparkly photo targets sound promising.  Have you thought about how you might use shaders to enhance the eerie atmosphere, perhaps with subtle, unsettling effects? Or maybe having items be player responsive, so when a  photo is taken, that object dissolves away.

The dust particle effects will certainly add to the abandoned feel. Consider how you might vary these effects in different areas of the hospital for added more narrative/emotional depth to world-building.

Your lighting and camera effects ideas are good, especially the shadowy figures. This could be a powerful way to build tension. Have you considered how you might use dynamic lighting to create more varied and unpredictable shadow effects? Or even have lights respond to player location/movement?

The audio implementation will be crucial to your concept. The idea of procedurally generated noises from empty rooms is great. What level of understanding do you have with this type of audio implementation? If you want to jump on it earlier than the module schedule, let me know.

Your interactivity description provides a clear picture of the player experience. The camera flash mechanic is a clever way to limit the player's vision and build tension. Post-processing effects like vignette will also help immensely. 