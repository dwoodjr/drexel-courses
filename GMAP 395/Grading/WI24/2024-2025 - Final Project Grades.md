## Ares - 80
- Glad to read you feel you have a stronger foundation on some of the topics covered int he course.
- It was good to read you relied on some outside sources to find a solution, very important soft skillset to have.
- There is a sudden flash of the "tentacle" like shapes periodically that is a bit jarring.
- The animation on the portal turn is good, it seem intentionally jerky and almost mechanical in nature.
- The transparency/color on the tentacle pieces during the sequence is good.
- I would like to see some more connection between the sequence and the camera shake
- Only one custom shader present
- Only two particle systems, but one is more complex (gpu events)
- Cinemachine dynamic camera is setup, but closer connection to game event/metaphor would be good
- I was not able to catch which module you did the polish for, but based on the scene I would say probably module 1
- The spawning object is not visible in the game scene. Maybe intentional?

## Chuanhui - 100
- You did a wonderful job in the course and per your postmortem I am glad to hear you got something from your time in the class. Being comfortable and willing to experiment and do some trial-and-error is rally important, especially with procedural tools.
- Thank you for taking time to attend office hours and engage and ask questions, it is really appreciated.
- This is wonderfully done! Your work throughout has really paid off in a cohesive and functional piece of interactive game art.
- Most notes are nitpicking a bit, but the spiraling crystals are split at the seams, I believe this is like due to the way the shader on them is processing vertex displacement. In your "Surface Distort" for the crystals shader, if you turn Normal Vector to Tangent space, it fixes this. The outer shell for the bubble, I want more subdivision so it is smother for vertex displacement, much more in line with the internal object.
EXCELLENT! Good luck to you and all you do in the future!

## Ethan - 82
- I am glad you feel you understood much of the visual knowledge and learned from the experience
- I enjoy  the minimal gameplay elements and their activations of the game art elements like VFX, this demonstrates some understanding in connecting interactivity.
- Many of the procedural art elements on the bike are too small or sparce to really appreciate well.
- The biggest overall detraction is visual cohesion between elements, something like a concrete style guide and references would help to just tie everything together. Push some of the color/lighting elements, skybox, etc.

## Hyungwoo - 100
- Very strong work throughout. I commend you on your creative use of your chosen toolset. 
- Also your use of very strong reference when designing and making mechanics and art. That really shoes in the final work. Don't ever go away from that, this is a crucial thing many students miss is using reference and using it well.
- When you speak in your video you really describe well the mythos and properties of the creature, it movement, its different states (like calcification) and you have great justifications for all of these things.
- Most feedback would be a bit "nitpicking". I think the muzzle flash would/could obscure more of the barrel. The gradual increase of the color, lighting, and camera shaking as the creature approaches could maybe start from further way to build some more suspense/intensity to the situation. The movement of the crate, I feel, would bee a bit les jerky, more weeping arcs and splines for pathing.
- Also, very well edited video too. A really good portfolio piece all around I believe.
This is a wonderful example of a piece of interactive game art! 

## Joshua - 92
- Excellent job getting much of what you described for the final interactivity/game metaphor working. I really like how the look at (via mouse) an clicking interactivity is functioning.
- This feedback is a bit nitpicky, but you could use some proximity based on delta from the mouse look to the portal objects to have a gradual shift or  and "in-between state" that is like halfway active.
-  The very subtle movement from the ground shader is really nice.
- This is is a more advanced coding idea for your "spaghetti code" on your hitscan (which is totally fine), but you cold store those variable lists for that states in an array structure within a scriptable object then refence that here; it would be much cleaner. 
- Nice work throughout the quarter engaging with the content and tutorials and adapting those to your needs and vision. Best of luck to you i the future!

## Jonathan -  90
- I like to hear that you find shaders to not be as scary as initially thought. Once you realize that just about everything in the engine/game art/interactivity is manipulating data values, I feel many concepts become much less intense. It's just knowing *what* data and *how* to manipulate it.
- Very creative solution for the two camera system. I do believe that the cinemachine "look at" has a couple of properties, maybe max speed and gain, to adjust the speed of the transitions. But either way, good work.
- There are some more "programmatic" ways of hiding the seams on your shapes in the shader like using 3D noise or tilling noise, but these are not simple. IF the seams in cause by UV on the shape one solution is to try rotating the shape to move the seam side away from the camera. But generally, good solution to your UV issue.
- I really like the use of proximity to control some shader and scale aspects. one sort of nitpicky suggestion. It would cool to have the eye "reveal" more gradually, so if you broke each eye into its own prefab, you could have some randomization to the scale factor and distance delta that controls it so the eye reveal (scale up) at different times/rates.
- The subtle shaking and camera lock really help sell your game metaphor idea it it pulling you in.
- Generally, I would love to see more cohesion between texture, color, and shape ideas of the different part of the portal. I think one thing that could help is have more of the surround world/space filled in wit some other elements that tie it all together. 
- Nice work!

## Kai - 87
- I am glad to hear you feel you have gained some knowledge and experience (however small or large) in some tech art creation. 
- If you blender edits ere that slow, it should like the tower design and procedural elements were too much of a toll on your system. When stuff like that happens its best to start reducing values and seeing where you can optimize some elements, like reducing geometry, number of objects, etc.
- Yo! The updated tower looks awesome! I cand defiantly see how the animation would take some time. I appreciate you exampling the efforts and attempts at your idea, I can still imagine what you were attempting and I think not having the final animation is okay. If we had more time (and maybe used Houdini) I think this totally could be accomplished with some proxy geometry and simple curve anim/sim. But good work!
- I like the mid/smoke for obscuring the tower, something that could work well for mor visual cohesion is maybe a more "simple geometric" mask/sprite for the particle to match more with the low-poly look
- My mind is sort of wanting some more emissive around the tower in that more magenta color and maybe some floating slowly rotating boulders/rocks too. With the white VFX it feels like a storm should be around the tower.

## Monty - 95
- I am glad you were able to take some things away from the course and that you feel you are starting to make connections with knowledge from other sources/classes, that is a major accomplishment in my mind.
- Not to sound cheesy,  but the ground elements, textures, grass, etc. rally grounds the whole scene, it is really helping to tie this together visually.
- I like the metaphor with the cube, Arrival, Annihilation, what have you, those "other worldly" references are starting to manifest  in the scene. I do want the cube/ship to be a bit more organically formed and in the world, but that is nitpicking.
- Generally, I have few notes, I think there are some really strong things working well in this piece of interactive game art and you clearly have a grasp on much of the important concepts. I would say this is very close to professional/semi professional. What will push it over are things like considerations for optimization of elements and assets to meet more runtime framerate. Lean int the worldbuilding more: what is the game metaphor really? how are yo expressing it through each element, whether subtle or overt. For instance. The grass, trees, ground have a more "realistic" texturing, but as the scene evolves only the trees really shift into the more stylized/other worldly look. How could the grass and ground do this, more subtly? Maybe the player footsteps also trigger some emissive falloff/triggers for those. Stuff like that.
- It was a pleasure having you in the course. You have a clear strong foundation to build from, I only encourage you to explore more, learn more, and keep pushing yourself. be curious for these things. I know e didn't touch much on more of the pipeline td stuff you were wanting (sorry) but much of the basics apply across the board. Manipulating and managing data, it's just all about the context of what, when, and why, and how that data is being manipulated and managed. 
- Great work throughout! I wish you the best of luck on all of your future endeavors!

## Owen - 80
- I am glad to hear you gained some experience from the class and some knowledge you can take away and apply in the future.
- What you mentioned about overcrowding and overworking many different components is all about that balance in art and design, and it is a trick things to really get because it varies so greatly from project to project. But you are recognizing that, and that is great.
- I do like how you reconfigured the space and added some more elements with the crystals. And you have some randomization/ more "organic" elements for the crystals/rocks.
- Generally, tis was as very good project. The balance and simplicity of the elements have come a long way. I do want just a bit "more" and some more polish in different spaces. For instance, different particle shapes/masks that are more in line with the visuals of everything else. I think this cave needs more moisture/water, puddles, drips, etc. It would also help to have a character to explore and walk int the space. Things like this; ask yourself more questions about what the space is/is saying and how can it be better communicated.
- Overall, nice work this quarter.
- Also, I hope you had a good and rewarding experience at GDC!
