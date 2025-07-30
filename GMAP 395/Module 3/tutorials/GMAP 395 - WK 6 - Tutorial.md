# Enhancing the Eldritch Portal with VFX

## Objective

In this tutorial, we will enhance the Eldritch Portal Shader (from Week 4 & 5) by creating a particle-based anticipatory effect in Unity’s VFX Graph. This effect will foreshadow the portal’s opening using an ever-present particle ring that intensifies and converges before triggering a vertical energy beam just before the portal activates.  *This first tutorial will focus ion just setting up the particle systems that will be animated later.*

![[portalVFXSplash.png]]

## Prerequisites

✅ Unity 2022.3 with URP and VFX Graph Installed  
	Ensure Visual Effect Graph is installed and updated via Unity Package Manager.
	Go to the Unity Registry tab and search for "Visual Effect Graph"  
✅ Completion of the Eldritch Portal Shader tutorial  
✅ Basic understanding of Unity’s VFX Graph & Shader Graph


> [!warning] Disclaimer: Video Tutorial
> You will likely need to follow this written tutorial AND watch the companion video tutorial (below) in order to grasp all of the steps and concepts of the complete tutorial.

---
## Video Tutorial

<iframe src="https://1drv.ms/v/s!AqQzGx8l4o2wk_Ir0KkkmojoBZRspw?embed=1" width="640" height="320" frameborder="0" scrolling="no" allowfullscreen></iframe>

[gmap395_wk6.mp4](https://1drv.ms/v/s!AqQzGx8l4o2wk_IrSYR-9QRFCYz4JA?e=fqUvll)

---

## Part 1: Setting Up the Particle Ring

In this section, we will create the particle ring effect that surrounds the portal, acting as a constant, pulsing energy field. As the portal prepares to open, the particles will intensify, swirl, and shimmer to build anticipation. This effect establishes a visual anchor around the portal, reinforcing its mystical energy and foreshadowing the activation sequence.

### Step 1: Create a VFX Graph
1. Right-click in the Project window and create a "**VFX**" folder to organize all VFX assets.
2. Inside the VFX folder, select `Create > Visual Effects > Visual Effect Graph`.
3. Name it ***PortalRingVFX***.
4. Drag the VFX Graph into the Scene and position it near the portal asset's center.
5. Open the VFX Graph by double-clicking `PortalRingVFX`.
6. In the Spawn context, increase the `Rate` from 16 to `100` or more (experiment for desired effect).

### Step 2: Create a Circular Particle Ring
1. Inside the VFX Graph, locate the `Initialize Particle` block.
2. Set the Capacity to `500` (Adjust for performance needs).
3. Add a `Set Position (Arc Circle)` block:
    - Radius: Create a *float* parameter in the Blackboard named `PortalRingRadius` and connect it.
    - Arc Max: `6.28` (Full circle).
    - Position Mode: `Surface`.
    - Spawn Mode: `Random` (Feel free to experiment).
    - Set *Angles X* position to `90°` in the `Circle > Transform > Angles` dropdown.
4. Remove the default `Set Velocity` block.
5. Add a `Set Velocity from Direction and Speed (Tangent)` block:
    - Create a *float* parameter `RingRotationSpeed` and connect it to `Max Speed`.
6. Set color by Speed (Gradient):
    - Create a *Gradient* parameter (`PortalRingColor`) in the Blackboard.
    - Adjust gradient *Intensity* for each color selected to ensure strong Bloom interaction.
    - Use `RingRotationSpeed` to set max speed in the *Speed Range*.
7. Use the default `Set Lifetime (Random Uniform)` block already present:
    - Create a *Vector2* parameter (`RingLifetimeMinMax`) via the Blackboard.
    - Connect `X` (Min) and `Y` (Max) to the Set Lifetime block.
8. To see color take effect:
    - Change the main texture of the particles (**Default-Particle** (a B/W gradient) works well).
    - Delete the `Set Color Over Life` block in the Output Particle Quad context.

### Step 4: Adding More Visual Variation
1. Use the Update Particle context to enhance visual interest:
2. Add a `Conform to Sphere` block:
    - Set Sphere Radius using `PortalRingRadius` parameter.
3. Add a `Turbulence` block:
    - Mode: `Relative`
    - Noise Type: `Perlin` (Feel free to experiment).
4. Adjust force parameters for desired motion.

### Step 5: Adjusting the Output Particle Quad Context
1. Experiment with Blend Modes:
    - Suggested: `Additive` for glowing effects.
2. Adjust `Set Size (Random from Curve)`:
    - Click the curve and set linear increase from `(0,0)` to `(1,0.1)`.
    - Set a random seed value or leave it at `0`.
3. Ensure there is an `Orient: Face Camera Plane`.
4. Use a custom particle shape:
    - Set the Main Texture to `Default-Particle` or create a custom texture with an alpha mask in an external program.

---

## Part 2: Creating the Vertical Energy Beam

In this section, we will create the vertical energy beam effect that erupts from the center of the portal just before it opens. This effect will consist of a core beam and trailing energy ribbons to enhance the feeling of the activation sequence, give it more visual "punch".

### Step 1: Initializing the Beam Particles
1. Create a new VFX Graph (`Right-click > Visual Effects > Visual Effect Graph`), name it ***PortalBeamVFX***.
2. Drag the VFX Graph into the Scene and position it at the center of the portal, aligned with the swirling portal effect.
3. Increase the Spawn Rate:
    - In the Spawn context, set `Rate (Over Time)` to `250` to match the ring effect.
4. Define the Beam’s Shape:
    - Add a `Set Position (Line)` block.
    - Set Start Position to `(X: 0, Y: 0, Z: 0)`.
    - Set End Position to `(X: 0, Y: 1, Z: 0)`.
    - Create a *float* parameter `BeamLineEnd` in the Blackboard (default `1`) and connect it to *End Y*.
5. Apply Velocity Randomization:
    - Add a `Set Velocity Random` block. Delete the old set velocity if needed.
    - Set X & Z Ranges: `-0.01 to 0.01` (slight horizontal drift).
    - Set Y Range: `0 to 1` (upward motion).
6. Control Particle Lifetime:
    - Add a `Set Lifetime Random (Uniform)` block.
    - Create a *Vector2* parameter `BeamLifetimeMinMax` in the Blackboard.
    - Set `X = 5` and `Y = 10`, then connect to `A` and `B` inputs.
7. Set Beam Color Based on Speed:
    - Add a `Set Color by Speed (Gradient)` block.
    - Create a Gradient parameter `BeamColor`.
        - Reverse the gradient values so that darker colors are on the left and brighter colors are on the right.
        - Increase alpha from 0% (left) to 100% (right) to make the beam fade in over its lifespan.

---

### Step 2: Setting Up the Update Context
Now, we will create GPU Events to be used later when we expand the beam effect.

8. Add GPU Event Blocks:
    - Create a `Trigger Event Always` block and set the count to `250`.
    - Create a `Trigger Event Rate (Over Time)` block and set the Rate to `250`.

---

### Part 3: Expanding the Beam with Trails
To add visual complexity, we will duplicate the particle system and create a trailing energy effect.

#### Step 1: Duplicating the Beam Network
1. Remove the Output Particle Quad (it is not needed for this effect).
2. Duplicate the entire particle network (`Drag Select > Right-click > Duplicate`).
3. Modify the Duplicate:
    - Remove the `Trigger Event Always` from the *duplicate*.
    - Create a GPU Event in an empty area.
    - Connect the `Trigger Event Always` from the first network to this GPU Event.
    - Connect this GPU Event to the `Initialize Particle` block of the duplicate network.

#### Step 2: Inverting the Second Beam
1. Reverse the Direction of the Second Beam:
    - Add a `Multiply` by (`-1`) node.
    - Connect `BeamLineEnd` to this node and then to the `Shape: Line End (Y)` of the duplicate.
2. Ensure Both Beams Share Parameters:
    - Connect `BeamLifetimeMinMax` and `BeamColor` to the duplicate network.

---

### Step 4: Adding Energy Trails
To create trailing effects, we will use Unity's built-in `Example Heads and Trails` system network.

1. Add an `Example Heads and Trails` node.
2. Delete the `Heads Network` section (we only need the `Trail Bodies`).
3. Connect the First Beam’s Trigger Event Rate:
    - Connect `Trigger Event Rate` from the first network to the `GPU Event` of Trail Bodies.
4. Refine the Trail Behavior:
    - Remove `Set Lifetime` and replace it with `Inherit Source Lifetime (Set)`.
    - Remove `Turbulence` from `Update Particle Strip`.
    - Change `Blend Mode` in `Output Particle Strip Quad` to *Additive*.
    - Replace `Set Size Over Life` with `Set Size Random (Uniform)`.
        - Create a *Vector2* parameter `BeamSize` (`X = 0.01`, `Y = 0.05`) to connect to the Set Size inputs.

#### Step 5: Duplicating the Trails for the Second Beam

5. Duplicate the Trail Bodies network.
6. Connect the Second Beam’s Trigger Event Rate to the `GPU Event` of the duplicate.

---

### Final Check

✅ Two beams should now be shooting both upwards and downwards from the portal’s center.  
✅ No need to animate exposed values yet; we’ll handle this next week.  
✅ You should now have a visually busy portal effect with swirling particles and beams.

---
---
>[!info]  [[GMAP 395 - Module 3| Return to the Module Page]]