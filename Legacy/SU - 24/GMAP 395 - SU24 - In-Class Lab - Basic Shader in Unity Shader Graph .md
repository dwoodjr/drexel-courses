## Objective

Gain hands-on experience creating and modifying basic shaders using Unity's Shader Graph. 
	Reference the HLSL version of this lab for some additional information on shaders.

## Prerequisites

- Unity 2022.3
- Basic understanding of Unity interface
- Universal Render Pipeline (URP) set up in your project

---
## Part 1: Creating a Simple Color Shader

### Step 1: Set up a new Shader Graph

1. In Unity, right-click in the Project window
2. Select Create > Shader > Universal Render Pipeline > Unlit Shader Graph
3. Name it "MyFirstShaderGraph"
4. Double-click to open it in the Shader Graph window

### Step 2: Create a simple color shader

1. In the Shader Graph window, locate the Blackboard (usually on the left side)
2. In the Blackboard:
   - Click the `+` button
   - Choose `Color` from the dropdown
   - Name it `_Color` (or any appropriate name)
   - Set a default color if desired (found in the `Graph Inspector` > `Node Settings`)
3. In the graph area:
   - Click and drag the `_Color` property from the Blackboard directly into the graph area
4. Connect the Color property node's output to the `Base Color` input of the "Fragment" node
5. Click "Save Asset" to save your shader graph

### Step 3: Apply the shader to a 3D object

1. In Unity, create a new 3D object (e.g., Sphere) in your scene
2. Create a new material:
   - Right-click in the Project window > Create > Material
   - Name it appropriately
3. In the new material's Inspector:
   - Set the Shader to your "Shader Graph/MyFirstShaderGraph"
   - Adjust the Color property to see changes on your 3D object

---
## Part 2: Adding Texture Support

### Step 1: Modify the shader to accept a texture input

1. In the Blackboard, add the following properties:
   - Texture2D named `_MainTex`
   - Vector2 named `_Tiling` (set default to 1,1)
   - Vector2 named `_Offset` (set default to 0,0)

1. In your Shader Graph, add the following nodes:
   - Drag the `_MainTex`, `_Tiling`, and `_Offset` properties from the Blackboard into the graph
   - Add a `Tiling And Offset`node
   - Add a `Sample Texture 2D` node


> [!NOTE] Hotkey
> SPACEBAR is the hotkey shortcut to open the create node dialogue box.


3. Connect the nodes:
   - Connect the `_Tiling` and `_Offset` outputs to the respective inputs of the `Tiling And Offset` node
   - Connect the UV output of `Tiling And Offset` to the `UV` input of `Sample Texture 2D`
   - Connect the `_MainTex` property to the Texture input of `Sample Texture 2D`

### Step 2: Combine texture with color

1. Add a `Multiply` node
2. Connect:
   - The RGBA output of `Sample Texture 2D` to one input of `Multiply`
   - The `_Color` property to the other input of `Multiply`
   - The output of `Multiply` to the `Base Color` of the Fragment node

3. Save the Shader Graph

### Step 3: Test the texture support
1. Select your 3D object in the scene
2. In the Inspector, you should now see slots for Texture, Tiling, and Offset
3. Assign a texture to the Texture slot
4. Adjust Tiling and Offset values to see how they affect the texture

---
## Part 3: Basic Vertex Manipulation (Wave Effect)

### Step 1: Add vertex displacement effect

1. In the Blackboard, add these Float properties:
   - `_WaveAmount` (default 1)
   - `_WaveSpeed` (default 1)
   - `_WaveFrequency` (default 1)

1. In your Shader Graph, add these nodes:
   - Drag the new Float properties from the Blackboard into the graph
   - Add `Time` node
   - Add `Position` node (set to World)
   - Add `Sine` node
   - Add several `Multiply` (3) nodes
   - Add `Add` node
   - Add `Split` node

3. Connect the nodes to create the wave effect:
	- Connect the output of the World Position node to the input of the Split node
	- Connect the `R` output of the Split node (which represents the X component) to one input of a `Multiply` node
	- Connect the `_WaveFrequency` to the other input of this `Multiply` node
	- Multiply `_WaveSpeed` by `Time`
	- Add the results of the above two operations using an `Add` node
	- Feed the output of the Add node into the Sine node
	- Multiply the Sine output by `_WaveAmount`

4. Add a `Combine` node:
   - Connect the `R` (X) and `B` (Z) from the `Split` node to the corresponding inputs on the `Combine`
   - For the `G`(Y) input of the `Combine` node, add the wave calculation to the `G`(Y) output of the `Split` node and connect it.

5. Connect the `Combine` node's output (RGBA or RGB) to the `Position` input of the Vertex node

### Step 2: Test the vertex manipulation

1. Save the Shader Graph
2. Select your 3D object in the scene
3. In the Inspector, you should now see Wave Amount, Wave Speed, and Wave Frequency properties
4. Adjust these values to see how they affect the object's shape

---
## Challenge: Color Blending

### Objective
Modify your shader to blend between two colors based on a custom parameter.

### Steps

1. In the Blackboard, add:
   - Another Color property named `_Color2`
   - A Float property named `_BlendFactor` (set range 0 to 1)
	
> [!hint] Modes in Graph Inspector
> You can change the `Mode` of a property in the `Graph Inspector` to something like `Slider`

2. In the graph area:
   - Drag the new properties from the Blackboard
   - Add a `Lerp` node

3. Connect the nodes:
   - Connect `_Color` and `_Color2` to the A and B inputs of the Lerp node respectively
   - Connect `_BlendFactor` to the T input of the Lerp node

4. Use the output of the Lerp node in your final color calculation (e.g., multiply it with your texture sample)

5. Save the Shader Graph and adjust the Blend Factor in your material's Inspector to blend between the two colors.

### Challenge Extensions

- Try blending based on vertex position instead of a custom parameter
- Implement a smooth transition that cycles between the colors over time (Time or Sine)
- Add a third color and blend between all three

> [!check] 
> Remember to save your Shader Graph after each major change, and don't hesitate to experiment with different connections and values!