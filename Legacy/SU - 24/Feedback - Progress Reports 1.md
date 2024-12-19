---
tags:
  - teaching
---
---
- [ ] E - modular issue and UI shader issue
I hope I am understanding the List thing. So, you want to generate a list, but only have it appear when the Manual Code generation happens, you don't just want a list to be there empty, correct? Try using Unity's SerializedProperty API class to handle your lists. - https://docs.unity3d.com/ScriptReference/SerializedProperty.html Something like a custom Editor function to only display the list when a condition is met might work. The list is serialized property, so it can show in the editor if needed. Check out the two attached scripts. Place the "LicesePlate.cs" on an empty game object to see the list show based on the Boolean check. If this is not what you are talking about, let me know. 

As for UI Shaders, this is really dependent on what type of object you want a shader/material on. Any UI "Image" object has a material property for placing custom shader/materisl on. But I am not sure all UI Object types are supported.



```c#

```

---


This is an excellent start! I actually think the grime cleaning mechanic functionallity is good, this is very close to how other games cleaning mechanics work. You could have something like vertex painting, similar to the PolyBrush. But doing that in real-time as a game mechanic is likely to be very involved and complex. https://docs.unity3d.com/Packages/com.unity.polybrush@1.0/manual/modes_color.html  
  
I would stick with the current system. My only suggestion at the moment is to work on a secondary way to communicate the amount of grime to the player.

For the shaders, going back to the model and cleaning u UVs, while a pain, is going to be beneficial. While you are at that, you could define some edge UV's that will be used to display dirt, or even just having the UVs divided in a way that some are meant for dirt and other parts are not, so the entire surface is not just covered.

The snapping also looks to be working well. My only suggestion for more accurate snapping is to define a snap tolerance, similar to the provided example. Or to use raycasts from the object or mouse position to determine if the object/cursor is close to/over the correct snap location.

---

For Car navigation/path finding. NavMesh and NavMesh Agents are going to be the best bet here. This is for having the cars drive around on their own around the scene. If you are doing procedural placement with scripts, you will need to either build/update the navmesh at runtime when the game starts. Or you will need to build in logic for your car AI to avoid placed obstacles. 

https://docs.unity3d.com/ScriptReference/AI.NavMesh.html

So balancing placement of spawned objects is challenging. One method is to use a combination of predetermined spots for larger assets line building and better defining the area(s) the other objects spawn in leaving some room for negative space. You could develop some rule/algorithm using object type like small, medium, large, and essentially saying that based on area size only x number of small, medium, or large objects can be spawned in this space at a time.

For Neon elements, the best performance will come from being elective with emissive materials + bloom post processing and balancing that with some real-time lighting. The materials are much less expensive than lights, so lean towards those. https://www.youtube.com/watch?v=sAH0mj0tGMo

---

Devon Morrison

I was just working on your feedback for this when we had the office hours. So I will answer those questions instead as It seems you got the other part figured out. Based on what you showed you are definitely in a good place for the final!

So for a binary probability check do something like this: 

For color lerp animation using DOTween: 

So, for the combinations, you can define them all in a comma delimited text file like this:

```txt
fire, fire, explosion
fire, water, steam
water, earth, mud
earth, fire, lava
```

Then use method that reads in the two element string variables to produce a combination. See the attached script:  

---

Jason King:

For bottle generation, why not both? I would actually suggest doing this: Making a small selection of bottle shapes then using C# script to randomly adjust their scale dimension in X,Y and Z just a bit here and there to create multitudes of variations. You could then have a small selection of bottle cap shapes and do the same thing. Pair a random bottle with a random cap. Then you can easily add variation to to the liquid with random color selection.

For the random colors, to me, the simplest solution is to make a color property then use C# to assign random values to that property. But you could also do something like this: https://www.youtube.com/watch?v=nT3W0qLYKWI 
If you wish to pick random colors from a specific subset of colors. 

Also this for liquid in a bottle: https://www.youtube.com/watch?v=tI3USKIbnh0

---

This is a good start. I'm sure you've gotten a bunch more done on the modeling side of things. For creating curvature, curve/spline modeling is you best friend. Defining the shape of the handle/blade using a curve, then sweeping geometry across that usually works well. Or based on what you showed, more edge loops going up the blade will allow for more points to manipulate and make the curve happen. Sorry, I am not a big Maya modeler anymore, so I am not super in depth with it, but any modeling software has curves and NURBS for mesh sweeping. 
https://www.youtube.com/watch?v=zo0Mc7sS-Ys

I like the material editing idea. You can absolutely define sliders more metallic properties like metalness, you can even create an atlas of metal textures that players can choose from and apply those to a default sword material. I know this is SW again, but the lightsaber customization in SW: Jedi Fallen Order is very similar to what you are describing, Have predefined metals/material that can easily be swapped onto the mesh UVs with a simple icon click.
https://www.youtube.com/watch?v=oj8_aZaexjg

---



