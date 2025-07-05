
# ***Procedural Eldritch Portal + Environment: A Tutorial for Blender***

![[GMAP 395/Module 1/Media/395tut1portal.png|640]]

## Introduction

### Theme: "Something from the Void"
In this tutorial, we will create a **Procedural "Eldritch Portal" Environment Art**, an ominous and glowing gateway surrounded by rocky terrain and organic tendrils. This project aims to integrates procedural modeling techniques and node-based workflows to craft a dynamic and mystical game-based environment artifact.

### Learning Goals:
- Understand the **Geometry Nodes** system in Blender.
- Apply **procedural workflows** to create modular and reusable assets.
- Explore **node-based techniques** for attributes like scattering, randomization, and deformation.
- Gain insight into exporting assets for **game engines** like Unity.


> [!warning] Reminder: *Documentation* is your best friend!
> https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/index.html

***Intro Video***: 
<iframe src="https://1drv.ms/v/s!AqQzGx8l4o2wk_Ewa8MCYxCviVy2gg?embed=1" width="320" height="320" frameborder="0" scrolling="no" allowfullscreen></iframe>

[gmap395_tut1_intro.mp4](https://1drv.ms/v/s!AqQzGx8l4o2wk_Ewtu7qaLOfP_oFTQ?e=Dfjfxw)


##
---

## Part 1: Creating the Rocky Base

### Step 1: Setup and Nodes Overview
1. Open Blender and create a **new project**.
2. Switch to the **Geometry Nodes** workspace.
	1. This can be found on the top toolbar.
3. Add a Plane (`Shift + A` > Mesh > Plane) and assign a new **Geometry Nodes modifier**.

> [!tip] Name your Geometry Nodes setup descriptively, e.g., `Rocky_Base_Geo`.

---

### Step 2: Procedural Rock Formation
1. **Adding Noise Deformation:** Use a **Noise Texture** and **Displacement Modifier** to create an uneven, rocky surface.
	1. Let's start by subdividing our plan to allow for more detail when we apply a noise function. Create a `Subdivide Mesh` node and plug the `Group Input`'s geometry output into the mesh input slot. Adjust the subdivision *Level* to 6. 
	2. Next let's scale our plane to make more room. Create a `Transform Geometry` node and plug the mesh output of the subdivide mesh not into geometry input. Adjust the *Scale* property(attribute) to a desired size; but keep int under 5 for now just to keep things speedy/snappy.
	3. Now we can work on applying some noise distortion so our plane look smore like a terrain. We will need the following nodes: `Set Position`, `Position(Read)` `Combine XYZ`, and a `Noise Texture`
		1. Plug the geometry out from the transform node into the geometry input of `Set Position`. The geometry output from this node will go into the `Group Output` geometry input.
		2. Plug the `Position(Read)` into the position input of `Set Position`. What this does is get the position of our plane and makes sure set position uses its current position.
		3. Now the vector output of the `Combine XYZ` node will go into the offset input of `Set Position`.
		4. Finally the color output of `Noise Texture` will go into the Z input of `Combine XYZ`.
			1. From here you can adjust the values of the parameters for the noise node to reach a desired look. For more on how this node works and what those parameters mean have a look the the [noise texture node documentation](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/noise.html).
	4. For reference we are performing a noise deformation similar to this video: https://www.youtube.com/watch?v=LmPhbfb2DH8
2. **Scattering Rocks**: Now let's scatter some "rocks" by using **Point Distribution** to scatter stand-in geometry and vary the size by **Randomizing Attributes**.
    1. We'll add a `Distribute Points on Faces` node to the end of the chain. So, the geometry output from `Set Position` will go into the mesh input. This randomly scatters points onto the surface of our terrain geometry base. Use the *Density* and *Seed* values to adjust the amount of points.
    2. Next we will need an `Instance on Points` node and an `Ico Sphere` node. Take the points output of the distribute node and plug it into the points input of the `Instance on Points` node. This is assigning the points we generated as the points we will not copy(instance) more geometry onto.
    3. Now we need to adjust the size of our "rocks" so they look a bit more "natural" by randomizing the scale. You'll now need a `Random Value(Float)` and another `Combine XYZ` node. Plug the value output of the `Random Value` into the XYZ of the combine node. The vector output of this node will go into the scale input of the `Instance Geometry` node. 
        1. If you want you can duplicate this section and apply it to the rotation of the instance node to randomize the rotation too.
    4. Adjust the *Min*, *Max*, and *Seed* values to achieve a desired look.

> **Section Recap:** Now you've got a basic terrain base and some rocks scattered along the surface. The scattering and rock scale are randomized to provide a more natural look. If you want to later, you can procedurally model some rocks and replate the basic primitive used as a stand-in.  

<iframe src="https://1drv.ms/v/s!AqQzGx8l4o2wk_Ev2buzpZnIe8YM5A?embed=1" width="320" height="320" frameborder="0" scrolling="no" allowfullscreen></iframe>

[gmap395_tut1_p1.mp4](https://1drv.ms/v/s!AqQzGx8l4o2wk_Ev1DF4vxnCCHC5jw?e=fayUeZ)

##
---

## Part 2: Designing the Portal

### Step 1: Creating the Portal Structure
1. **Start with a Base Shape:**
    1. Add a Bezier Circle (`Shift + A` > Curve > Circle) to represent the outer edge of your portal. Name it appropriately, like `portal_base_geo`. Now assign a new geometry node modifier to it in the Geometry Nodes context. This provides a smooth and flexible base for the portal geometry.
    2. Drop down and `Curve to Points` node and an `Instance on Points` node. Adjust the *Count* of the curve points node to a number you like, I started with default 10. Plug the points output into the points input of the instance node.
    3. Now we need some geometry to instance onto the points of our curve to start making the portals base structure. create `Cube(Primitive)` and a `Transform Geometry` node. the mesh output of the cube will go into the geometry input of the transform node.
        1. Adjust the *Scale(XYZ)* of the transform node to get cubes of a desired size/shape.
    4. As you may have noticed, the cubes are all around the circle but their rotation does not face the form of the curve, we will fix that now. Create an `Align Rotation to Vector` node. This node can read the Normals or Tangent of the vector direction of the points along the curve and we can then assign that rotation to another object, like the cubes.
        1. Take the Tangent output of the `Curve to Points` node and plug it into the Vector input of the align node.
        2. The parameter values on the `Align Rotation to Vector` node I found most helpful are to pick the *X* axis (below *Rotation*), and set the *Pivot* to Z.
        3. Now the Rotation output of the align nodes goes to the Rotation input of the  `Instance on Points` node.
        4. This process is similar to what is found in this video: https://www.youtube.com/watch?v=J4RpyR3jN-U

### Step 2: Adding Additional Stones
1. **Creating additional portal stones:**
    1. Now that we have some basic stones for the portal we can duplicate some nodes and run essentially the same/similar operations to create the second set of stones.
    2. Start by creating  a `Transform Geometry` node; we will use this to offset the rotation of our points later. 
    4. Now you can duplicate(copy and paste) the nodes and connections for all of the nodes we used in **Part 2 - Step 1** from above. Connect the Geometry output of the transform node into the Curve input of the newly duplicated `Curve to Points` node.
    5. Now, keep all of the connections in tact from the nodes that were copied. We can now just go back into some of the nodes and adjust some parameters to get more of a stone portal look.
        1. Start with the `Transform Geometry` node and adjust the *Rotation(Z)*  offset the second set of cubes.
        2. Adjust the *Scale(XYZ)* of the cubes transform geometry node to make the smaller and a little longer in the second set.

> [!warning] To See All Geometry
> You will need to temporarily connect the Instances output from  both `Instance to Points` nodes into a `Join Geometry` node, then connect that to the `Group Output`.

### Step 3: Combining the Parts
1. **Apply Boolean Operations:**
    1. Drop down a `Mesh Boolean` node. If you used a `Join Geometry` node to see all of the geometry together, you can delete that now.
    2. The `Mesh Boolean` node will allow us to perform a boolean operation using the two sets of cube/stones we made for the portal. In this case we will use *Union* as the operation type and tick on both *Self Intersection* and *Hole Tolerant*.
    3. Now plug the *Instances* outputs from both chains/trees `Instance on Points` into the *Mesh* input of the `Mesh Boolean`. This can now be plugged into the main `Group Output` node.

> [!NOTE] Filling the Portal
> If you with to have a circular plane to fill the void in the portal (maybe for doing a shader later on) you can use a `Fill Curve` node. Just connect a new edge from the geometry output of the main `Group Input` node to it and then connect the *Mesh* output to the *Mesh* input of the `Mesh Boolean` 

> **Section Recap:** Boolean operations allow us to create complex shapes by combining or subtracting simpler ones. Here, we use the smaller set of geometry to combine with the larger set of geometry, forming the portal’s basic structure. Now, if you wish to later, you can model better stone using the cubes as a base to make the portal look better.

[gmap395_tut1_p2.mp4](https://1drv.ms/v/s!AqQzGx8l4o2wk_EuJDcode-o2D6LIA?e=rsBx7O)


<iframe src="https://1drv.ms/v/s!AqQzGx8l4o2wk_Eue0CpgFjlPwTaeA?embed=1" width="320" height="320" frameborder="0" scrolling="no" allowfullscreen></iframe>

##
---

## Part 3: Adding Tendrils

### Step 1: Generating Organic Shapes
1. **Define Tendril Paths:**
    1. Add a **Curve Line** (`Shift + A` > Curve > Curve Line) and then add a `Transform Geometry` node to a new modifier context.
    2. Us the transform node to adjust the *Rotation(X)* to around -90 degrees. Now we will essentially be using nodes used earlier in this tutorial to construct the rest of the tendrils. Create a `Curve to Points` node and an `Instance on Points` node. Adjust the *Count* of the curve points node to a larger number number, like 30. Plug the points output into the points input of the instance node.
    3. We will need another `Align Rotation to Vector` node. Connect it like before, where the vector comes from the `Curve to Points` tangent output and the rotation output goes to the rotation input of the `Instance to Points`.
    4. Create another `Mesh Boolean` node and plug the *Instances* output from instance points into the *Mesh* input.
        1. You will need to set the boolean nodes parameters to *Union* and *Exact* respectively.
    5. 

### Step 2: Connecting the Tendrils
1. **Adding Tendrils to their place :**
    1. We will use a `Curve Circle` node with a 0.5 *Radius* as a frame for the tendrils to be spawned on to. So, create this now.
    2. Then, use another `Curve to Points` node and `Instance to Points` node combo to create a 6 Count points and instance the tendrils onto those points. 
        1. Connect the *Mesh* output of the `Mesh Boolean` from earlier to the *Instances* input.
    3. You'll use another `Align Rotation to Vector` node to get the Tangent from the curve points to the vector input. Then the Rotation output from this node matches to the Rotation input of the `Instance on Points`.
    4. To create a more "natural" look we will add some random roatation so the tendrils are not all uniform. Grab a `Random Value` node set to *Vector*. *Max* value are 0.0, 0.1, and 1.90.
        1. The *Value* output goes to the Rotation input of a `Rotate Instances` node. This connects to the `Instance on Points` and the `Group Output` nodes. You can also use a `Transform Geometry` node to move all the tendrils into place.


<iframe src="https://1drv.ms/v/s!AqQzGx8l4o2wk_Etx1QgHhvQEc79vQ?embed=1" width="320" height="320" frameborder="0" scrolling="no" allowfullscreen></iframe>

[gmap395_tut1_p3.mp4](https://1drv.ms/v/s!AqQzGx8l4o2wk_EtzgD0ilFKv0Moww?e=JO4ROa)


---

## Export

> [!error] Optimization and Export
> We will do the optimization and mesh export in week 3 before importing to Unity. Just be sure to have some procedural game art ready to go.

---
---

>[!info]  [[GMAP 395 - Module 1| Return to the Module Page]]