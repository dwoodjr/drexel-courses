# ASN 2

# ASN 3

## Maya

The issue with the VFX phasing through the floor—I would check under the "collision module". There should be a plane option, and I would just have the stretch well over the area that the road is taking up. There may also be an option to adjust the thickness of the collision plane. You may also want to take a look at the bounce/kill for the particles, depending on the desired behavior. I can see a world in which some of the sparks bounce a bit when they contact the floor. Nicely done using the scripting to control the color gradient. I am curious if it would be possible to increase the "intensity" of the color gradient values so you get some of that nice bloom effect of the particle sparks as well.

## Wells

Excellent work! I love to see your thinking and reasoning behind your design choices, and I agree that reducing the clutter was an excellent choice; we want to see that hero asset. It might be nice to have some color/hue shifts during the particle animations that maybe hint at the "time of day" we are shifting to. Something else subtle to subconsciously give the player more reinforcement of the time mechanic. Also, fantastic job (throughout the quarter) with the scripting and connecting your many assets to the game states and changes, this is really helping to tie everything together and bring the world to life. I am excited to see it all come together for the final. Great work this quarter Wells!

## Skylar

Very well done with the collision script and using the shader graph with your VFX! I love the explanation of having another element to limit the vision of the player that is based on a world interaction. Something that could be great to couple with this collision trigger is using some scripting of post-processing effects (like a white intense vignette or desaturation) to trigger as the player enters and leaves the collider. So it is almost like for a moment the steam has obscured the player's vision for a short time after entering. Nice solution for getting the particle smoke/steam to fill the area as well. There is a world in which you create some volumetric/voxel based VFX, but that is for something beyond this class I think.

## Jason

Very nicely done using multiple systems to create a layered VFX! It looks really good and the timing seems quite well done too; if you ever plan to have the character fully rigged, it may be beneficial to have the "skinned mesh renderer" act as the mesh emission for one or more of the 3 systems. Nicely done!

## Keira

Very nicely done with the firefly particle system and the clicking interaction via scripting! Very creative solution to have the pirate ship stay stationary and have the environment move around it. You may even want to add some of that motion to the water shader as well using some UV marching to add to that moving/motion of the ship. Oh and a small DOTween ship that subtly moves the ship up and down could help sell the motion too; as well as some Cinemachine camera sway (we will look at this later).

## Ryan

Hmm, yeah the "hologram projection" effect is actually usually more shader based than VFX/particle based. They usually consist of a couple of layers of semi-transparent emissive materials with some slight noise animation or flickering. You could make some subtle particles to enhance the "reveal" of this look, but yeah it is mostly shader/material based; much like you already have. I think the particles you did make do a nice job of adding to the hologram though! Maybe if you could get a similar level of transparency to the trails, that could help sell it more too. Nice work!!!

## Lindsey (August)

I really like the motion/look of the bolt effect. Something that we didn't quite cover (but that I do have an older tutorial on) is using position points to "arc" a VFX Graph particle from location to another. Essentially you use a spline to have the particle follow a path. Kind of like: https://www.youtube.com/watch?v=hiyv9vZAOvA. For the interactivity, don't sweat it too much and don't overthink it, it can be as simple as pushing the "launch" button and the particles spin up (activate). Nothing overly fancy needed. Good job!

## Isaiah

Excellent as always! It was a very good idea to use some variation/randomness to get more "realism" to the various VFX instances. This is precisely what randomness/variation is good for in these use cases. You have also just done a great job at "layering meaningful stuff" with the dust, the periodic sparks, fire, etc. They feel like they belong to the world and they have a reason for being there. There is a good use of "scale" to your effects as well; if anything, I would maybe get a bit smaller on the particles that spawn when close to a fire, but that is really just nitpicking.

# ASN 4

## Isaiah

Incredible work this quarter Isaiah, you have really hit it out of the park in this course with both the timeliness and quality of work! One thing I would maybe adjust is the amount of sway or perhaps more the timing, you could do some math to have the camera shake/sway happen at less intense and more intense intervals with some math that mimics "footsteps". Something like every x distance travelled by the controller = 1 footstep, then use that trigger moment to activate or multiply the Cinemachine sway, just give it a bit more randomness and "liveliness." Yeah, I just have very few notes because this work is top notch, excellent job.