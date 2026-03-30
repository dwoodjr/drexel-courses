
## Lab Title: Creating a Stream/Beam Effect with VFX Graph

### Objective: 
Create a modular, procedural beam/stream effect that follows a path(spline), and collides with surfaces.

### Part 1: Setting up the Base Effect

1. **Create a new VFX Graph:**
    - Right-click in the Project window
    - Select `Create > Visual Effects > Visual Effect Graph`
    - Name it `BeamEffect`
      
1. **Set up the basic structure:**
    - Add a `Spawn` context
    - Add an `Initialize Particle` context
    - Add an `Update Particle` context
    - Add an `Output Particle Quad` context
      
2. **In the Spawn context:**
    - Set the spawn rate to `Constant` with a value of `5000`
> [!tip] **Spawn Rate/Count**  
> A high spawn rate creates a dense, continuous stream effect.
    
1. **In the Initialize Particle context:**
    - Delete all default nodes except `Capacity`
    - Add a `Set Position` block
    - Add a `Set Velocity Random form Curve` block
      ![[lab_vfx2_init.png]]
2. **In the Update Particle context:**
    - Add a `Set Lifetime` node
        - Set the lifetime to a value of `5` seconds (adjustable based on desired effect duration)
    - Add a `Set Size over Lifetime` node
        - Create a size curve that stays consistent over the particle lifetime
          ![[Pasted image 20240729215838.png]]
          
3. **In the Output Particle Quad context:**
	- Set the particle rendering to `Quad` (which it should be by default)
	- Set the Blend Mode to `Addative`
	- Assign a gradient to the `Set Color over Life` block

> [!hint] **Blend Mode**  
> Ensure the `Blend Mode` set to an Additive shader to create a glowing beam effect with Post Processing.

### Part 2: Implementing Path Follow Sub-Graph

- **Create a Block Sub-graph for Path Following:**

    - Right-click in the Project window
    - Select `Create > Visual Effects > Visual Effect Sub-graph Block`
    - Name it `PathFollow`
    
> [!tip] **Sub-graphs**  
> Sub-graphs allow you to create reusable components for your VFX, making your graph more modular and easier to manage.
    
- **In the Block Sub-graph:**
    
    - Set the Suitable Contexts to `Update`
    - Add a `Set Position` node/block
    - Outside of the Bock Subgraph: 
	    - Create a `Sample Bezier` node
	    - Create am `Age Over Lifetime` node and connect it to the T input of the Sample Bezier
	    - Create a `Get Attribute: Particle ID` node
	    - Create an `Add` node and add the Position output of the Sample Bezier with the Particle ID output of the Get Attribute nodes
	    - Create a `Perlin Curl Noise 3D` node and plug the output of the Add node to the Coordinate input
	    - Create a `Multiply` node and plug the Noise output to the A input
	    - Create another `Add` node add the Multiply output with the Position output of the Sample Bezier 
	    - Plug the Add output into the Position input of the Block Subgraph `Set Position` block
	    - ![[lab_vfx2_baseSubgraph 1.png]]
- **Expose parameters in the Block Sub-graph:**
    - Add `Positon` (x4) parameters for the path and name them 1 - 4
	    - Plug these position parameters into the A - D inputs of the Sample Bezier
	    - ![[lab_vfx2_sampleBez.png]]
    - Add a `Float` parameter named Spread and default to 0.25
	    - Plug the Spread parameter into the B input of the Multiply node
	    - ![[lab_vfx2_multiplySubg 1.png]]
	- Save you VFX Subgraph
	  ![[lab_vx2_fullSubg.png]]
- **In your main VFX Graph, add your new Block Sub-graph node to the Update Particle context:**
    - You will need to create new exposed parameters for the `Spread - Float` and `1-4 - Position` parameters in the main graph Blackboard.
    - When this is done go into the Unity Editor and put your VFXG in the scene (if not done so already)
    - In the Unity `Hierarchy` add 4 empty game objects and name them `p1-p4` to represent the transform position of the spline
	    - ![[lab_vfx2_posSetup.png]]
    - In the `Inspector`, on your VFXG game object add a VFX Property Binder component
    - Add (x4) Position properties to the Property Bindings section
	    - `+ > Transform > Position` (x4)
		- Click on one the top property binding set the `Target` to `p1` and set the `Property` name to `1_position`
			- Repeat this step for the remaining 3 properties, making sure the Property name is `#_position`
			  ![[lab_vfx2_propBinders.png]]
			  
> [!attention] Naming Convention
> In the property binder the Property name should be the name of the property from the main graph Blackboard followed by an underscore and property type `PropertyName_TypeOfBinder`. So in this case it is `#_position`
		
> [!hint] **Modular Approach**  
> This modular approach allows you to easily change the path of the beam, enabling dynamic and flexible visual effects.
> 
- In the main VFX Graph your `Path Follow` node should have the 1-4 Position Properties and the Spread property plugged in to their respective inputs
  ![[lab_vfx2_followPath.png]]
### Part 3: Adding Procedural Elements + Collison

1. **In the Update Particle context, add a `Turbulence` node:**
    - Connect it to various exposed properties to control later in C# (if desired)
2. **In the Update Particle context, add a `Collision` node:**
    - There are a few collision types so pick one like `Collide with Sphere`
    - Set the Transform>Position of block/node to the end of the spline (the `4` position property)
![[lab_vfx2_4Pos.png]]
### Part 4: Adding Mesh Emission for Impact Effect

1. **Create a GPU Event (On Die)**
	1. In the new `Initialize Particle` context section:
		1. `Set Lifetime Random` using desired values
		2. `Set Velocity Random` sing desired values
		3. Create a `Set Position (Mesh)` block 
			1. Set the position to the last position (4) of the spline using the `4` position property as the input for Transform>Position input
> [!hint] First VFX Lab
> This is very similar in style to the GPU Event form the first VFX Graph Lab
1. **In the Blackboard:**
    - Create an exposed `Mesh` property called Spawn Mesh
        - Plug this property into the Mesh input of the Set Position (Mesh) block
    - Create a Vector 3 Called Mesh Scale
        - Plug this into the Transform>Scale input of the Set Position (Mesh) block![[lab_vfx2_gpuInit.png]]
          
2. **In the Update Particle context:**
    - Add nodes to create a desired On Die particle effect
    - For example:
	    - Add `Set Size Random`
	    - Add `Turbulence`
	    - Add `Gravity`
	    
	![[lab_vfx2_gpuUpdate.png]]
1. **In the Output Particle Quad context:**
   - Add a `Set Color over Life` block and use a gradient, like before
     ![[lab_vfx2_gpuOut.png]]
1. **In your main beam VFX Graph, add a `Trigger Event` node:**
    - Trigger this event on particle death `Trigger Event on Die`
    - Use this event to spawn your impact effect for the VFX Graph
      ![[lab_vfx2_gpuTrigger 2.png]]
> [!NOTE]
>     Combining multiple VFX Graphs/Subgraphs/GPU Events allows for more complex, layered effects.

---
### Advanced Challenges:

1. Make the beam reactive to player input, allowing real-time control of the path. (C# Scripting)
2. Implement a more complex impact response, like surface scorching or deformation. (Shader on Mesh)
3. Use ta shader to create a more complex procedural animation for the beam particles.
---
