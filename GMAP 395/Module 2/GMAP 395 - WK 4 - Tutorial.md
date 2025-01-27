# Creating an Eldritch Portal Shader

## Objective
Create a swirling circular portal shader using Unity’s Shader Graph, complete with dynamic transparency and procedural motion effects.

![[portalShaderGrab.png|640]]

---
## Video Tutorial

<iframe src="https://1drv.ms/v/s!AqQzGx8l4o2wk_F1iR6SHuAP0Vb5yg?embed=1" width="320" height="320" frameborder="0" scrolling="no" allowfullscreen></iframe>
[gmap395_tut3.mp4](https://1drv.ms/v/s!AqQzGx8l4o2wk_F1UOYs8x0W2JbJRQ?e=JOQ7gp)

---
## Prerequisites
1. Unity 2022.3 with URP installed.
2. Basic understanding of Shader Graph.
3. Completion of previous shader lab (recommended).

---

## Part 1: Setting Up the Shader Graph
### Step 1: Create a New Shader Graph
1. In Unity, navigate to the Project tab.
2. Right-click and select **Create > Shader Graph > URP/Lit Shader Graph**.
3. Name it **"EldritchPortalShader"**.


> [!warning] Important ***Graph Inspector*** Settings
> *Surface Type* : Transparent
> *Blending Mode*: Multiply or Alpha
> *Render Face*: Both
> *Alpha Clipping*: ✅

> [!NOTE] Swirl Pattern Texture
> - Use a PNG with an alpha channel
> - Find something with a lot of "texture" or noise
> What I used: [liquid_swirl_alpha.png](https://1drv.ms/i/s!AqQzGx8l4o2wk_F0d_KPRwOyyq1jzg?e=mqpCpS)

### Step 2: Add Properties to the Blackboard
1. Open the Shader Graph and access the Blackboard.
2. Add the following properties:
    - **Color:** `EdgeColor` (default: Purple)
    - **Float:** `EdgeWidth` (default: 0.5, range: 0 to 1)
    - **Texture2D:** `SwirlPattern` (default: Procedural noise texture)
    - **Float:** `SwirlSpeed` (default: 1)
    - **Float:** `Power` (default: 2, range: 0.1 to 10)
    - **Vector2:** `CenterPosition` (default: 0,0)

---

## Part 2: Creating the Swirling Portal Effect
### Basic Swirl Node Structure
1. **Time-Based Swirl Rotation:**
    - Add a **Time** node and connect it to the *A* input of a **Multiply** node.
    - Link `SwirlSpeed` to the *B* input of the Multiply node.
        - the swirl speed can be set to a *Slider (Mode)* in the ***Graph Inspector (Node Settings)***
        - Set the desired *Min* and *Max*; e.g. 0.1 - 1.
    - Connect the output to the *Rotation* input of a **Rotate** node.
2. **Swirl UV Transformation:**
    - Pass the output of the Rotate node to the *UV* input of a **Tiling and Offset** node.
    - Connect the output of Tiling and Offset to  to the *UV* input of a **Polar Coordinates** node.
    - Use `CenterPosition` as the *Center* input of the **Polar Coordinates**.
    - In **Polar Coordinates** *Radial Scale* should be ~1.25 and *Length Scale* ~1
3. **Texture Sampling:**
    - Add a **Sample Texture 2D** node.
    - Connect `SwirlPattern` to the *Texture* input and the output of Polar Coordinates to the *UV* input.
        - <font color="#ff0000">An important note</font> for the next section, change the *Mip Sampling Mode* of the **Sample Texture 2D** node to *Gradient* in the ***Graph Inspector (Node Settings)***
    - Use a **DDX** node, a **DDY** node, and the `SamplerState` to refine UV sampling.
        - Drop down a **UV** node and connect it to both **DDX** and **DDY**
        - Connect **DDX** to the *DDX* input of the **Sample Texture 2D**
        - Connect **DDY** to the *DDY* input of the **Sample Texture 2D**
    - Drop down a **Sampler State** node: set its *Filter* to Linear and its *Warp* to Mirror
        - Connect this node to the *Sampler* input of **Sample Texture 2D**
4. **Swirl Blend:**
    - Add a **Blend** node.
    - Connect the output of the **Sample Texture 2D** node to the *Base* input.
    - Connect `EdgeColor` to the *Blend* input.
        - The *Mode* should be set to Multiply (but feel free to experiment with looks)

---

### Additional Noise Textures for the Swirl
1. **Noise Generation:**
    - Add a **Time** node and connect it to a **Multiply** node for animation.
        - Multiply by ~.25
    - Pass the output to the *Offset* a **Tiling and Offset** node.
2. **Noise Texture Sampling:**
    - Add a **Voronoi** noise node and use the output of **Time** as its *Angle Offset*.
        - Experiment with *Cell Density*, but a good value is ~3.
    - Add a **Gradient Noise** node, connecting the output of **Tiling and Offset** to its *UV* input.
        - The *Scale* of the gradient node should be ~5.75.
3. **Noise Blending:**
    - Use a **Blend** node to combine the outputs of Voronoi and Gradient Noise.
        - I think the *Mode* Negation works well here; but again, experiment with it.

---

## Part 3: Radial Alpha Gradient
1. **Radial Transparency:**
    - Add a **Polar Coordinates** node.
        - Set the *Length Scale* to ~2.45
    - Connect `EdgeWidth` as the *Radial Scale* input.
2. **Gradient Sampling:**
    - Pass the output of Polar Coordinates to the *Time* input of a **Sample Gradient** node.
    - Set the Gradient so it goes from `Black >> White` with more black showing, about halfway point.

---

## Part 4: Connecting It All Together
1. **Base Swirl and Noise Combination:**
    - Add a **Multiply** node.
    - Connect the output of the **Blend** node from the ***Basic Swirl Nodes*** section to *A*.
    - Connect the output of the **Blend** node from the ***Additional Noise*** section to *B*.
2. **Power Adjustment:**
    - Add a **Power** node and connect `Power` to its second input.
    - Pass the output of the Multiply node to the *A* input of **Power**.
3. **Blend Blending:**
    - Add a **Blend**(1) node to combine the outputs of the **Power** (into *Blend* input) node and the **Sample Gradient** node (into *Base* input) from the  ***Radial Alpha*** section.
        - Set the *Opacity* to ~1
    - Now `Copy and Paste` this **Blend**(2) node (you should now have 2)
        - Set this ones *Opacity* to ~0.5
4. **Final Blend**
	- Drop down a new **Blend**(Final) node.
	- Connect **Blend**(1) to *Base*
	- Connect **Blend**(2) to *Base*
	- Set the *Opacity* to ~0.5
5. **Fragment Shader Stack:**
    - Connect the final blend output to the main **Fragment Shader** output:
        - **Base Color**
        - **Emission**
        - **Alpha**
        - **Alpha Clip Threshold**


---

## Part 5: Testing and Enhancing
### Step 1: Apply the Shader to a Mesh
1. Create or import a circular plane in Unity (or use a cylinder primitive).
2. Create a material from the Shader Graph (`right-click > create > material`)
3. Assign the material using the Eldritch Portal Shader to this mesh.

### Step 2: Test and Adjust
1. Adjust the properties (_EdgeWidt_, _SwirlSpeed_, _CenterPosition_, etc.) to fine-tune the effect.
2. Experiment with different textures for `SwirlPattern` and different types of noise to create unique styles.

### Optional Enhancements
- **Color Shifting:** Use a **Sample Gradient** node linked to **Time**(Sine) for dynamic color transitions and pulsating effect.


---
---