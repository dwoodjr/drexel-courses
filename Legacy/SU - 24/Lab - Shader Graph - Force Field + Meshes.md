# In-Class Lab: Creating a Stylized Force Field Shader

## Objective

Create a stylized force field shader using Unity's Shader Graph that can be applied to various VFX meshes.

---
## Prerequisites

- Completion of the previous basic shader graph lab
- Unity 2022.3 with URP
- Basic understanding of Shader Graph
---
## Part 1: Setting Up the Force Field Shader

### Step 1: Create a new Shader Graph

1. In Unity, create a new Shader Graph (URP/Lit Shader Graph)
2. Name it "StylizedForceFieldShader"

### Step 2: Set up basic properties

In the Blackboard, add the following properties:

- Color: `_BaseColor` (default: light blue)
- Color: `_RimColor` (default: white)
- Float: `_RimPower` (default: 5, range: 0.1 to 10)
- Texture2D: `_PatternTexture`
- Float: `_PatternSpeed` (default: 1)
- Float: `_Intensity` (default: 10, range: 0 to 20)

---
## Part 2: Creating the Force Field Effect

### Step 1: Implement rim lighting

1. Add a `Fresnel Effect` node
2. Connect the `_RimPower` to its Power input
3. Add a `Multiply` node and connect: 
	1. The Fresnel output to one input 
	2. `_RimColor` to the other
4. Add another `Multiply` node and connect:
   - The output of the first `Multiply` 
   - The `_Intensity` to the other input
5. Create a `Blend` node set to `Mode: Screen` and connect:
	1. The output of the last `Multiply` node to Blend (second input)
	2. The `_RimPower` parameter to the Opacity (third input)
	3. We will return t this node later to apply Base (first input)

### Step 2: Add moving pattern

1. Add a `Time` node
2. Add a `Multiply` node and connect:
   - Time node output to one input
   - `_PatternSpeed` to the other input
3. Add a `Tiling And Offset` and `Position` (set to World) nodes:
   - Connect output from Position node to UV input of Tiling and Offset
   - Connect the Multiply node output to Offset input
4. Add a `Sample Texture 2D` node:
   - Connect `_PatternTexture` to its Texture input
   - Connect Tiling And Offset output to its UV input

### Step 3: Combine effects

1. Add a `Multiply` node:
   - Connect the `_BaseColor` one input
   - Connect the sampled texture to the other input
2. Now return to the first `Blend` (Step 1) node:
   - Connect the Multiply node output to the Base input of the Blend node
3. Apply the out put of the Blend node to:
   - The `Base Color` of the `Fragment` shader
   - The `Emision` of the `Fragment` shader

### Step 4: Set up a procedural animated texture
1. Create `Time`(x2), `Multiply`(x2),  `Voronoi`(x2) nodes
2. Multiply the Time nodes by two different values (0.5 and 1.25 for example)
3. Connect each Multiply node output to an Angle Offset input of a Voronoi
4. Create a `Blend` (`Mode:Difference`) node and connect:
	1. The output of one Voronoi to the Base input
	2. The output of the other Voronoi to the Blend input
	3. Set the Opacity Value
5. Create a `One Minus` node and connect the Blend output to its input

### Step 5: Set up final color and emission
1. Create a new `Blend` node in `Mode:Overlay`
2. Connect the final `_BaseColor` calculation to:
   - The Base input of the Blend node
   - The `One Minus` to the Blend input of the Blend node
   - Set Opacity to 1
3. Replace the Base input the first Blend node (Fresnel one) with the output of the Blend node just created

### Step 6: Set up the Alpha and Alpha Clipping

1. In `Graph Settings`:
   - Set Surface Type to Transparent
   - Set Blend Mode to Additive
   - Set Render Face to Both
   - Tick on Alpha Clipping
2. From the `Fresnel Effect` node in Step 1
	1. Connect the first `Fresnel Effect` node to the Alpha Clip Threshold of the Fragment Shader
	2. Connect a `One Minus` node and set its output to the Alpha of the Fragment shader


---
## Part 3: Adding Vertex Displacement

### Step 1: Create pulsing effect

In the Blackboard, add the following properties:

- Float: `_RippleSpeed` (default: 1)
- Vector 2: `_RippleCenter` (default: 0, 0)
- Float: `_RippleFrequency` (default: 1)
- Float: `_RippleHeight` (default: 0.15, range: 0 to 0.5)

1. Add a `Sine` node
2. `Multiply` a `Time` node by `_RippleSpeed`
3. Create an `Add` node and connect the Multiply to the B input (A will be connected later)
4. Connect the Add a to the Sine input

### Step 2: Apply displacement

1. Add a `Position` node (Object space)
2. Add a `Split` node and connect the Position to it
3. Create a `Combine` and connect the R and G from the split node
4. Add a `Subtract` node and subtract `_RippleCenter` from the combined RG output
5. Create a `Multiply` node and multiply the Subtraction calculation by `_RippleFrequency`
6. Connect the new Multiply output to the A input of the Add node from Step 1
7. Create an `Add` node and a `Multiply` node: Multiply `_RippleHeight` by the Sine output. Then Add this to the Original G (Y) position from the Split node.
8. Lastly, create a `Combine` node and connect the original G(X) and B(Z) from the Split node. Place the output of the Add node from previous step into the G(Y) input. 
9. Connect RGBA output to the Position of the `Vertex` shader


---
## Part 4: Testing on Various VFX Meshes

1. Create or import several VFX meshes (e.g., sphere, custom shield shape, energy wave)
2. Apply your force field shader to each mesh
3. Experiment with different textures and UV configurations:
   - Use different tiling values for each mesh
   - Try both simple and complex patterns
4. Adjust shader properties to see how they affect different mesh shapes

---
## Challenge: Enhance the Force Field

Choose one or more of these enhancements to implement:

1. **Impact Effect**: Add a parameter to control an "impact" effect, distorting the force field where it's been hit.
2. **Color Variation**: Implement a gradient or color-shifting effect based on viewing angle or time.
3. **Noise Distortion**: Use a noise texture to add subtle distortions to the pattern movement.
4. **Adaptive Intensity**: Make the force field more intense (brighter, more distorted) when taking damage or under stress.

## Conclusion

In this lab, you've created a  force field shader that can be applied to various VFX meshes. You've explored how different UV configurations and mesh shapes interact with shader effects, and you've implemented vertex displacement for added dynamism. This shader demonstrates practical applications in game development, enhancing visual feedback and game feel.

Remember to experiment with different textures, colors, and parameters to achieve diverse effects suitable for various game scenarios!