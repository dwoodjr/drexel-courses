# Unity Vertex Displacement Shader: Noise-Based Ripples

## Prerequisites: Mesh Setup (CRITICAL!)

**Before touching Shader Graph, your mesh MUST be dense enough:**

### Test Mesh Creation in Blender:

1. **Add Plane** → Tab (Edit Mode)
2. **Right-click → Subdivide** → Repeat 4-6 times
3. Or use **Modifier → Subdivision Surface** (3-4 levels)
4. **Export as FBX** → Import to Unity
5. **Target: 2000+ vertices minimum** for smooth displacement

### Unity Primitive Alternative:

- Use Unity's **Plane** primitive only for initial testing
- It has very few vertices (4) and won't show smooth displacement
- You'll see the corners moving but no surface detail

---

## Shader Graph Setup: Step-by-Step

### Step 1: Create the Base Shader

1. **Right-click** in Project → **Create → Shader Graph → URP → Lit Shader Graph**
2. **Name it** "WaveDisplacement"
3. **Double-click** to open

### Step 2: Noise-Based Displacement Nodes

**Add these nodes in order:**

#### A. Position and Time Input

```
1. Position Node → Set to "Object" space
2. Time Node → Use "Time" output
3. Multiply Node → Connect Time to input A
4. Set Multiply value to 2.0 (wave speed)
```

#### B. Create Spatial Noise Pattern

```
5. Simple Noise Node → Set to "Simplex 2D"
6. Split Node → Connect Position.XY to it
7. Vector2 Node → Connect Split XY to Simple Noise UV input
8. Add Node → Connect Multiply (step 4) to Simple Noise Time input
```

#### C. Scale and Control Noise

```
9. Multiply Node → Connect Simple Noise output
10. Set multiplier to 0.3 (displacement strength)
11. Normal Vector Node → Set to "Object" space
12. Multiply Node → Connect step 10 output to A, Normal Vector to B
```

#### D. Apply Displacement

```
13. Add Node → Connect Position (Object) + the normal displacement
14. Connect final Add to Vertex Position output
```

### Step 3: Complete Node Chain

**Your flow should look like:**

```
Position(Object) → Split → Vector2 → Simple Noise UV
Time → Multiply(2.0) → Simple Noise Time
Normal Vector(Object) → ready for displacement
Simple Noise → Multiply(0.3) → Multiply(Normal Vector) → Add(Position) → Vertex Position
```

---

## Advanced Ripple Effect

### For More Complex Waves:

#### Multiple Noise Layers:

```
1. Create 2-3 Simple Noise nodes
2. Use different Scale values (5, 10, 20)
3. Add them together with different strengths
4. Multiply sum by 0.1-0.2 for final displacement
```

#### Directional Waves:

```
1. Use only Position.X or Position.Z for wave direction
2. UV.x → Multiply(10) → Add(Time) → Sine → displacement
3. Creates waves moving in one direction
```

---

## Troubleshooting Checklist

### If Entire Object Moves Instead of Surface:

1. **✓ Check Position node is "Object" space**
2. **✓ Check Normal Vector node is "Object" space**
3. **✓ Displacement strength under 1.0** (try 0.1-0.3)
4. **✓ Mesh has 1000+ vertices**

### If No Movement at All:

1. **✓ Time node connected correctly**
2. **✓ Shader applied to material**
3. **✓ Material applied to mesh**
4. **✓ Check Vertex Position is connected**

### If Movement Too Fast/Slow:

1. **Adjust Time multiplier** (0.5 = slower, 3.0 = faster)
2. **Noise Scale affects frequency** (higher = more ripples)

---

## Quick Test Setup

### Immediate Test in Unity:

1. **Create Plane** → Scale up to see better
2. **Apply your material**
3. **Play Scene** and observe
4. **If corners move but no surface detail = need denser mesh**

### Values to Start With:

- **Time Multiply:** 1.0-2.0
- **Noise Scale:** 5-15
- **Displacement Strength:** 0.1-0.5
- **Mesh Density:** 50x50 subdivisions minimum

---

## Common Issues & Solutions

|Problem|Cause|Solution|
|---|---|---|
|Whole object translates|Low poly mesh|Use subdivided mesh|
|No movement|Time not connected|Check Time → noise connection|
|Too choppy|Displacement too strong|Reduce multiplier to 0.1-0.3|
|Too uniform|Need spatial variation|Use Position in noise UV|
|Performance issues|Too dense mesh|Balance detail vs performance|

---

## Next Steps

1. **Test with simple setup first**
2. **Gradually add complexity** (multiple noise layers)
3. **Experiment with different noise types** (Gradient, Voronoi)
4. **Combine with surface shaders** for visual effects
5. **Add wind direction controls** with Vector parameters