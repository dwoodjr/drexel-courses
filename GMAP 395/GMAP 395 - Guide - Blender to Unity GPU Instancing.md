# Blender to Unity GPU Instanced "Greeble"

> [!tip] What You'll Learn 
> This guide will teach you how to create thousands of detailed objects (like panels, bolts, and vents) in Blender and display them efficiently in Unity using GPU instancing. Perfect for creating detailed sci-fi walls, tech panels, or industrial surfaces!

---

## 🎯 What is Greeble?

**Greeble** refers to small detailed elements that make surfaces look complex and interesting - like the panels, bolts, vents, and mechanical details you see on spaceships in movies like Star Wars.

**Traditional Problem:** Adding thousands of these details would slow down your game to a crawl.

**Our Solution:** Create the details in Blender, then use Unity's GPU instancing to display thousands of them with better performance.

---

## 📋 What You'll Need

### Software Requirements
- **Blender 4.0+** (free from [blender.org](https://www.blender.org/))
- **Unity 2022.3+ LTS** (free from [unity.com](https://unity.com/))
- **Basic knowledge:** Opening software, creating objects, running scripts

### Expected Results
- **Performance:** 50,000+ detailed objects running smoothly
- **Workflow:** Easy to modify and iterate
- **Quality:** Full 3D detail, not fake textures

---

## Part 1: Creating Greeble in Blender

### Step 1: Set Up Your Base Surface

1. **Open Blender** and delete the default cube (Select it, press Delete)
2. **Add a plane:**

> [!note] Why a plane? 
> We're creating a wall or panel surface. *You can use any shape really* - cube faces, complex geometry, etc.

### Step 2: Add Geometry Nodes

1. **Select your plane**
2. **Go to Modifiers panel** (wrench icon on the right)
3. **Add Modifier** → Geometry Nodes
4. **Click "New"** to create a new node group

### Step 3: Create the Node Network

You'll work in the **Geometry Nodes editor**. If you don't see it, go to the top and switch to the "Geometry Nodes" workspace.

**Create this exact node setup:**

```
Group Input 
    ↓
Transorm Geometry (for scale of Plane)
     ↓   
Distribute Points on Faces (Density: 50)
    ↓
Random Value (Vector) → Store Named Attribute (Name: "rotation")
    ↓
Random Value (Float) → Math Node → Store Named Attribute (Name: "scale")  
    ↓
Random Value (Float) → Math Node → Store Named Attribute (Name: "greeble_type")
    ↓
Points to Vertices
    ↓
Group Output
```

### Step 4: Setting Up Each Node

**Distribute Points on Faces:**

- Set Density to 50 (start small for testing)
- This scatters points across your surface

**First Random Value (for rotation):**

- Set Type to "Vector"
- Min: (0, 0, 0)
- Max: (360, 360, 360)

**Store Named Attribute (rotation):**

- Name: `rotation`
- Domain: Point

**Second Random Value (for scale):**

- Set Type to "Float"
- Min: 0.0
- Max: 1.0
- Connect to Math node (Multiply) set to 0.8
- Connect Math output to another Math node (Add) set to 0.4
- This gives scale range from 0.4 to 1.2

**Store Named Attribute (scale):**

- Name: `scale`
- Domain: Point

**Third Random Value (for type):**

- Set Type to "Float"
- Min: 0.0
- Max: 1.0
- Connect to Math node (Multiply) set to 3.0
- Connect to Math node (Floor)
- This gives integers 0, 1, 2 for different greeble types

**Store Named Attribute (greeble_type):**

- Name: `greeble_type`
- Domain: Point

**Points to Vertices:**

- This converts the points to vertices that our script can read

> [!warning] Important! You should see small dots scattered on your plane surface. If you see actual cubes or geometry, you've added the wrong nodes!

### Step 5: Export the Data

1. **Switch to Scripting workspace** (top tab)
2. **Click "New" in the text editor**
3. **Copy and paste this entire script:**

```python
import bpy
import json

def export_greeble_with_attributes():
    obj = bpy.context.active_object
    
    def show_message(message):
        def draw(self, context):
            self.layout.label(text=message)
        bpy.context.window_manager.popup_menu(draw, title="Export Info", icon='INFO')
    
    if not obj:
        show_message("No object selected!")
        return
    
    # Get evaluated mesh
    depsgraph = bpy.context.evaluated_depsgraph_get()
    eval_obj = obj.evaluated_get(depsgraph)
    eval_mesh = eval_obj.to_mesh()
    
    if len(eval_mesh.vertices) == 0:
        show_message("No vertices found! Make sure you have 'Points to Vertices' node!")
        return
    
    positions_x = []
    positions_y = []
    positions_z = []
    rotations_x = []
    rotations_y = []
    rotations_z = []
    scales = []
    types = []
    
    # Get attribute data
    rotation_attr = eval_mesh.attributes.get("rotation")
    scale_attr = eval_mesh.attributes.get("scale")
    type_attr = eval_mesh.attributes.get("greeble_type")
    
    for i, vert in enumerate(eval_mesh.vertices):
        # Position
        world_pos = obj.matrix_world @ vert.co
        positions_x.append(world_pos.x)
        positions_y.append(world_pos.y)
        positions_z.append(world_pos.z)
        
        # Rotation
        if rotation_attr:
            rot_vec = rotation_attr.data[i].vector
            rotations_x.append(rot_vec.x)
            rotations_y.append(rot_vec.y)
            rotations_z.append(rot_vec.z)
        else:
            rotations_x.append(0.0)
            rotations_y.append(0.0)
            rotations_z.append(0.0)
        
        # Scale
        if scale_attr:
            scale_val = scale_attr.data[i].value
            scales.append(scale_val)
        else:
            scales.append(1.0)
        
        # Type
        if type_attr:
            type_val = int(type_attr.data[i].value)
            types.append(type_val)
        else:
            types.append(0)
    
    # Export with flattened arrays
    data = {
        "positions_x": positions_x,
        "positions_y": positions_y,
        "positions_z": positions_z,
        "rotations_x": rotations_x,
        "rotations_y": rotations_y,
        "rotations_z": rotations_z,
        "scales": scales,
        "types": types,
        "count": len(positions_x)
    }
    
    # Save
    import os
    blend_filepath = bpy.data.filepath
    if blend_filepath:
        directory = os.path.dirname(blend_filepath)
        filepath = os.path.join(directory, "greeble_data.json")
    else:
        filepath = "greeble_data.json"
    
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)
    
    show_message(f"Exported {len(positions_x)} points to {filepath}")
    
    eval_obj.to_mesh_clear()

# Run the export
export_greeble_with_attributes()
```

4. **Make sure your object is selected**
5. **Click "Run Script"**
6. **You should see a popup** saying how many points were exported
7. **Find the file** `greeble_data.json` in the same folder as your .blend file

> [!success] Success Check If you see "Exported X points to..." popup, you're ready for Unity! If you get errors, double-check your Geometry Nodes setup.

---

## Part 2: Setting Up Unity

### Step 6: Create Unity Project

1. **Open Unity Hub**
2. **Create new project** → 3D URP (Universal Render Pipeline)
3. **Name it** something like "GreebleTest"

### Step 7: Import Your Data

1. **Copy your `greeble_data.json`** file into the Unity Assets folder
2. **In Unity,** you should see it appear in the Project window

### Step 8: Create Simple Greeble Meshes

We need some basic 3D objects to instance. Let's create them in Unity:

1. **Create a Cube** (GameObject → 3D Object → Cube)
    
2. **Scale it** to (0.1, 0.05, 0.02) - this makes a flat panel
    
3. **Drag it to Project window** to make it a prefab
    
4. **Delete it from the scene**
    
5. **Create a Cylinder** (GameObject → 3D Object → Cylinder)
    
6. **Scale it** to (0.02, 0.01, 0.02) - this makes a small bolt
    
7. **Drag it to Project window** to make it a prefab
    
8. **Delete it from the scene**
    
9. **Create another Cube**
    
10. **Scale it** to (0.2, 0.02, 0.02) - this makes a vent
    
11. **Drag it to Project window** to make it a prefab
    
12. **Delete it from the scene**
    

### Step 9: Get the Meshes

We need to extract the actual mesh data from these prefabs:

1. **Select each prefab in Project window**
2. **Look in the Inspector** - you'll see a "Mesh Filter" component
3. **Note the mesh names** (usually "Cube", "Cylinder", etc.)
4. **We'll use these mesh references in our script**

### Step 10: Create the GreebleRenderer Script

1. **Right-click in Project window** → Create → C# Script
2. **Name it** `GreebleRenderer`
3. **Double-click to open** in your code editor
4. **Replace all the code** with this:

```csharp
using UnityEngine;
using UnityEngine.Rendering;
using System.Collections.Generic;

public class GreebleRenderer : MonoBehaviour
{
    [System.Serializable]
    public class GreebleData
    {
        public float[] positions_x;
        public float[] positions_y;
        public float[] positions_z;
        public float[] rotations_x;
        public float[] rotations_y;
        public float[] rotations_z;
        public float[] scales;
        public int[] types;
        public int count;
    }
    
    [Header("📦 Greeble Assets")]
    [Tooltip("Drag your 3 mesh assets here (Panel, Bolt, Vent)")]
    public Mesh[] greebleMeshes = new Mesh[3];
    
    [Tooltip("Material for all greeble (must have GPU Instancing enabled)")]
    public Material greebleMaterial;
    
    [Header("📄 Data File")]
    [Tooltip("Drag your greeble_data.json file here")]
    public TextAsset greebleDataFile;
    
    [Header("🎚️ Scale Settings")]
    [Tooltip("Overall size multiplier for everything")]
    public float globalScale = 1f;
    
    [Tooltip("Base size for greeble elements")]
    public float baseGreebleSize = 0.1f;
    
    [Header("⚡ Performance")]
    [Tooltip("Lower this if you get performance issues")]
    public int maxInstancesPerBatch = 1023;
    
    [Header("🐛 Debug")]
    public bool showDebugInfo = true;
    
    private GreebleData greebleData;
    private Dictionary<int, List<Matrix4x4>> instanceMatrices;
    private Dictionary<int, List<Matrix4x4[]>> batches;
    
    void Start()
    {
        LoadGreebleData();
        PrepareInstanceData();
    }
    
    void LoadGreebleData()
    {
        if (greebleDataFile != null)
        {
            try
            {
                string jsonText = greebleDataFile.text;
                greebleData = JsonUtility.FromJson<GreebleData>(jsonText);
                
                if (showDebugInfo && greebleData != null)
                {
                    Debug.Log($"✅ Loaded {greebleData.count} greeble instances");
                    if (greebleData.positions_x != null && greebleData.positions_x.Length > 0)
                    {
                        Debug.Log($"📍 First position: [{greebleData.positions_x[0]:F2}, {greebleData.positions_y[0]:F2}, {greebleData.positions_z[0]:F2}]");
                        Debug.Log($"📏 Scale range: {System.Math.Round(greebleData.scales.Min(), 2)} to {System.Math.Round(greebleData.scales.Max(), 2)}");
                    }
                }
            }
            catch (System.Exception e)
            {
                Debug.LogError($"❌ Failed to load greeble data: {e.Message}");
            }
        }
        else
        {
            Debug.LogError("❌ No greeble data file assigned! Drag greeble_data.json to the script.");
        }
    }
    
    void PrepareInstanceData()
    {
        if (greebleData == null || greebleData.positions_x == null)
        {
            Debug.LogError("❌ No valid greeble data!");
            return;
        }
        
        instanceMatrices = new Dictionary<int, List<Matrix4x4>>();
        batches = new Dictionary<int, List<Matrix4x4[]>>();
        
        // Process each greeble point
        for (int i = 0; i < greebleData.count; i++)
        {
            int type = greebleData.types[i];
            
            // Make sure we don't go outside our mesh array
            type = Mathf.Clamp(type, 0, greebleMeshes.Length - 1);
            
            if (!instanceMatrices.ContainsKey(type))
            {
                instanceMatrices[type] = new List<Matrix4x4>();
            }
            
            // Convert coordinates from Blender to Unity
            Vector3 pos = new Vector3(
                greebleData.positions_x[i] * globalScale,
                greebleData.positions_z[i] * globalScale,  // Swap Y and Z
                greebleData.positions_y[i] * globalScale
            );
            
            Vector3 rot = new Vector3(
                greebleData.rotations_x[i] * Mathf.Rad2Deg,
                greebleData.rotations_z[i] * Mathf.Rad2Deg,  // Swap Y and Z
                greebleData.rotations_y[i] * Mathf.Rad2Deg
            );
            
            // Calculate final scale
            float finalScale = baseGreebleSize * greebleData.scales[i] * globalScale;
            
            // Create transformation matrix
            Matrix4x4 matrix = Matrix4x4.TRS(
                transform.TransformPoint(pos),
                transform.rotation * Quaternion.Euler(rot),
                Vector3.one * finalScale
            );
            
            instanceMatrices[type].Add(matrix);
        }
        
        CreateBatches();
        
        if (showDebugInfo)
        {
            foreach (var kvp in instanceMatrices)
            {
                Debug.Log($"🎯 Type {kvp.Key}: {kvp.Value.Count} instances");
            }
        }
    }
    
    void CreateBatches()
    {
        foreach (var kvp in instanceMatrices)
        {
            int type = kvp.Key;
            List<Matrix4x4> matrices = kvp.Value;
            
            batches[type] = new List<Matrix4x4[]>();
            
            // Split into batches for GPU instancing
            for (int i = 0; i < matrices.Count; i += maxInstancesPerBatch)
            {
                int batchSize = Mathf.Min(maxInstancesPerBatch, matrices.Count - i);
                Matrix4x4[] batch = new Matrix4x4[batchSize];
                
                for (int j = 0; j < batchSize; j++)
                {
                    batch[j] = matrices[i + j];
                }
                
                batches[type].Add(batch);
            }
        }
    }
    
    void Update()
    {
        RenderGreeble();
    }
    
    void RenderGreeble()
    {
        if (batches == null || greebleMaterial == null) return;
        
        foreach (var typeKvp in batches)
        {
            int type = typeKvp.Key;
            
            if (type >= greebleMeshes.Length || greebleMeshes[type] == null)
                continue;
                
            Mesh mesh = greebleMeshes[type];
            
            foreach (Matrix4x4[] batch in typeKvp.Value)
            {
                Graphics.DrawMeshInstanced(
                    mesh,
                    0,
                    greebleMaterial,
                    batch,
                    batch.Length
                );
            }
        }
    }
}
```

5. **Save the script** (Ctrl+S)

---

## Part 3: Putting It All Together

### Step 11: Create the Material

1. **Right-click in Project** → Create → Material
2. **Name it** "GreebleMaterial"
3. **Select it** and in Inspector find **"Enable GPU Instancing"**
4. **CHECK that box** - this is crucial!
5. **Set any color/texture** you want

### Step 12: Set Up the Renderer

1. **Create empty GameObject** (GameObject → Create Empty)
2. **Name it** "GreebleRenderer"
3. **Add the script:** Add Component → search "GreebleRenderer"

### Step 13: Assign Everything

In the GreebleRenderer script component:

1. **Greeble Meshes** (size 3):
    
    - Element 0: Drag "Cube" mesh from your prefab
    - Element 1: Drag "Cylinder" mesh from your prefab
    - Element 2: Drag "Cube" mesh from your other prefab
2. **Greeble Material:** Drag your GreebleMaterial
    
3. **Greeble Data File:** Drag your greeble_data.json file
    

### Step 14: Test It!

1. **Press Play**
2. **Check the Console** for success messages
3. **You should see** lots of small objects scattered on your surface!

---

## 🔧 Troubleshooting

### "No greeble data file assigned!"

- Make sure you dragged the .json file to the "Greeble Data File" slot

### "Failed to load greeble data"

- Check that your .json file is in the Assets folder
- Try re-importing it (select and press Ctrl+R)

### Nothing appears when I play

- Check "Enable GPU Instancing" is checked on your material
- Make sure all 3 mesh slots are filled
- Look at the Console for error messages

### Objects are too big/small

- Adjust "Base Greeble Size" (try 0.01, 0.05, 0.1, 0.2)
- Adjust "Global Scale"

### Performance is bad

- Lower "Max Instances Per Batch" to 511
- Reduce the density in your Blender Geometry Nodes

---

## 🎯 Understanding the Code

### What the Python Script Does

1. **Finds your selected object** with Geometry Nodes
2. **Reads the point positions** from the Points to Vertices
3. **Extracts the stored attributes** (rotation, scale, type)
4. **Converts everything to simple arrays** that Unity can understand
5. **Saves it as JSON** for Unity to import

### What the Unity Script Does

1. **Loads the JSON data** when the game starts
2. **Converts positions** from Blender coordinate system to Unity
3. **Groups instances by type** (0=panel, 1=bolt, 2=vent)
4. **Creates transformation matrices** for each instance
5. **Uses GPU instancing** to draw thousands of objects efficiently

### Key Components Explained

**Matrix4x4:** This stores position, rotation, and scale for each instance **Graphics.DrawMeshInstanced:** Unity's function to draw many copies efficiently **Batches:** GPU instancing has limits, so we split large numbers into smaller batches

---

## 🚀 Next Steps

Once you have this working, you can:

- **Add more greeble types** (just increase the multiply value in Blender)
- **Create more complex base surfaces** (curved walls, complex shapes)
- **Add LOD systems** for even better performance
- **Animate individual instances** for interactive elements
- **Use different materials** for each greeble type

---

## 📚 Quick Reference

### Blender Node Order

```
Distribute Points on Faces → Store Attributes → Points to Vertices → Output
```

### Unity Setup Checklist

- [ ] JSON file in Assets folder
- [ ] Material has "Enable GPU Instancing" checked
- [ ] All 3 mesh slots filled
- [ ] Script attached to GameObject
- [ ] All fields assigned in Inspector

### Common Scale Values

- **Base Greeble Size:** 0.05 - 0.2
- **Global Scale:** 0.1 - 2.0
- **Density in Blender:** 10 - 100 for testing, up to 1000+ for final

---

> [!success] You Did It! You now have a powerful system for creating detailed environments with excellent performance. This technique is used in AAA games for creating rich, detailed worlds that run smoothly on all platforms.