# Lab: Introduction to Shader Language (HLSL in Unity)

## Objective

Gain hands-on experience writing and modifying basic shaders using High Level Shader Language (HLSL) in Unity. 

## Introduction

In this tutorial, you'll learn how to create a custom shader in Unity using High Level Shader Language (HLSL). We'll start with a simple color shader, add texture support, and finally implement basic vertex manipulation for a wave effect.

> 📘 **What are Shaders?**
> 
> Shaders are specialized programs that run on the GPU. They determine how 3D geometry is rendered into 2D pixels on the screen. Shaders control various aspects of rendering, including vertex positions, color calculations, lighting, and special effects.

## Prerequisites

- Unity 2022.3 or later installed
- Basic understanding of Unity interface


---

## Part 1: Creating a Simple Color Shader

### Step 1: Set up a new shader file

1. In Unity, right-click in the Project window
2. Right Click Create → Shader → Unlit Shader
3. Name it "MyFirstShader"
4. Double-click to open it in your code editor

### Step 2: Modify the shader code

Replace the entire content of the file with the following code:

```glsl
Shader "Custom/MyFirstShader"
{
    Properties
    {
        _Color ("Color", Color) = (1,1,1,1)
    }
    SubShader
    {
        Tags { "RenderType"="Opaque" }
        LOD 100

        Pass
        {
            CGPROGRAM
            #pragma vertex vert
            #pragma fragment frag
            #include "UnityCG.cginc"

            struct appdata
            {
                float4 vertex : POSITION;
            };

            struct v2f
            {
                float4 vertex : SV_POSITION;
            };

            float4 _Color;

            v2f vert (appdata v)
            {
                v2f o;
                o.vertex = UnityObjectToClipPos(v.vertex);
                return o;
            }

            fixed4 frag (v2f i) : SV_Target
            {
                return _Color;
            }
            ENDCG
        }
    }
}
```

> 🟢 **Shader Structure**
> 
> Shaders are broken into `Blocks`. The main blocks in a Unity shader are:
> - `Properties`: Defines variables that can be set in the Unity Inspector.
> - `SubShader`: Contains the actual shader code. A shader can have multiple SubShaders for different rendering capabilities.
> - `Pass`: Defines a single render pass. A SubShader can have multiple passes.
> 
> The `CGPROGRAM` and `ENDCG` tags denote where the actual HLSL code begins and ends.

### Step 3: Understand the code

- `Properties`: Defines the `_Color` property that will appear in the Inspector
- `SubShader` and `Pass`: Defines how the shader should be rendered
- `vert` function: Transforms vertex positions from object to clip space
- `frag` function: Returns the color for each pixel

> 🔍 **Vertex and Fragment Shaders**
> 
> A basic shader typically consists of two main functions:
> 1. `Vertex Shader (vert)`: Processes each vertex of the 3D model. It's responsible for transforming 3D positions to 2D screen positions.
> 2. `Fragment Shader (frag)`: Runs for each pixel that needs to be drawn. It determines the final color of each pixel.

### Step 4: Apply the shader to a 3D object

1. In Unity, create a new 3D object (e.g., Sphere) in your scene
2. In the Project window create a Materials folder
3. In the Materials wolder `Right Click > Create > Material`. Name the material appropriately.
4. In the Inspector window locate the Shader dropdown (at the top). Find your shader.
	Hint: `Shader "Custom/MyFirstShader"` 
5. Adjust the Color property in the Inspector to see changes

## Part 2: Adding Texture Support

### Step 1: Modify the shader to accept a texture input

Update the `Properties` block in your shader:

```glsl
Properties
{
    _Color ("Color", Color) = (1,1,1,1)
    _MainTex ("Texture", 2D) = "white" {}
    _TilingX ("Tiling X", Float) = 1
    _TilingY ("Tiling Y", Float) = 1
    _OffsetX ("Offset X", Float) = 0
    _OffsetY ("Offset Y", Float) = 0
}
```

> 💡 **Texture Properties**
> 
> - `_MainTex ("Texture", 2D) = "white" {}`: Defines a 2D texture property. The "white" default creates a white texture if none is assigned.
> - Tiling and Offset properties allow for texture repetition and positioning adjustments directly in the Unity Inspector.

### Step 2: Update the shader code

Modify the shader code to include texture sampling:

```glsl
// Add these lines after the existing variable declarations
sampler2D _MainTex;
float _TilingX;
float _TilingY;
float _OffsetX;
float _OffsetY;

struct appdata
{
    float4 vertex : POSITION;
    float2 uv : TEXCOORD0;
};

struct v2f
{
    float2 uv : TEXCOORD0;
    float4 vertex : SV_POSITION;
};

v2f vert (appdata v)
{
    v2f o;
    o.vertex = UnityObjectToClipPos(v.vertex);
    o.uv = float2(v.uv.x * _TilingX + _OffsetX, v.uv.y * _TilingY + _OffsetY);
    return o;
}

fixed4 frag (v2f i) : SV_Target
{
    fixed4 col = tex2D(_MainTex, i.uv) * _Color;
    return col;
}
```

> 🎨 **Texture Sampling**
> 
> `tex2D(_MainTex, i.uv)` samples the texture at the given UV coordinates. Multiplying by `_Color` tints the sampled texture color. This allows for both texturing and color adjustment in the shader.

### Step 3: Test the texture support

1. In Unity, select your 3D object
2. In the Inspector, you should now see Texture, Tiling, and Offset properties
3. Assign a texture to the Texture slot
4. Adjust Tiling and Offset values to see how they affect the texture

## Part 3: Basic Vertex Manipulation

### Step 1: Add vertex displacement effect

Modify the `vert` function in your shader:

```glsl
// Add these properties
_WaveAmount ("Wave Amount", Float) = 1
_WaveSpeed ("Wave Speed", Float) = 1
_WaveFrequency ("Wave Frequency", Float) = 1

// Add variable declerations
float _WaveAmount;  
float _WaveSpeed;  
float _WaveFrequency;

// Modify the vert function
v2f vert (appdata v)
{
    v2f o;
    
    // Apply wave effect
    float3 worldPos = mul(unity_ObjectToWorld, v.vertex).xyz;
    float wave = sin(worldPos.x * _WaveFrequency + _Time.y * _WaveSpeed) * _WaveAmount;
    v.vertex.y += wave;
    
    o.vertex = UnityObjectToClipPos(v.vertex);
    o.uv = float2(v.uv.x * _TilingX + _OffsetX, v.uv.y * _TilingY + _OffsetY);
    return o;
}
```

> 🌊 **Vertex Displacement**
> 
> This code creates a wave effect by modifying the y-position of each vertex:
> - `worldPos` converts the vertex position to world space.
> - The `sin` function creates a wave pattern based on the x-position and time.
> - `_Time.y` is a built-in Unity variable that provides the current time, allowing for animation.
> - The resulting `wave` value is added to the y-component of the vertex position.

### Step 2: Test the vertex manipulation

1. In Unity, select your 3D object
2. In the Inspector, you should now see Wave Amount, Wave Speed, and Wave Frequency properties
3. Adjust these values to see how they affect the object's shape

> 🔧 **Shader Debugging Tip**
> 
> If your shader isn't working as expected, try visualizing intermediate values. For example, you could output the wave value as a color in the fragment shader to see how it's affecting each pixel:
> ```glsl
> fixed4 frag (v2f i) : SV_Target
> {
>     fixed4 col = tex2D(_MainTex, i.uv) * _Color;
>     return col * (sin(i.uv.x * _WaveFrequency + _Time.y * _WaveSpeed) * 0.5 + 0.5);
> }
> ```

## Conclusion

Congratulations! You've created a custom shader that includes color tinting, texture mapping with tiling and offset controls, and animated vertex displacement. Experiment with different values and try applying this shader to various 3D objects in your scene.

> 🚀 **Next Steps**
> 
> Now that you've got the basics down, consider exploring:
> - Normal mapping for added surface detail
> - Custom lighting models
> - More complex vertex animations
> - Using multiple textures for advanced effects like detail textures or masks (PBR)

---

# Challenge: Color Blending

## Objective
Modify your shader to blend between two colors based on vertex position or a custom parameter.

## Hints and Tips

ℹ **Concept**
Color blending involves interpolating between two colors. Think about how you can represent this interpolation using a single value that ranges from 0 to 1.

❗**Key Considerations**
- How will you determine the blend factor? (Vertex position, custom parameter, etc.)
- Which component of the vertex position will you use if basing on position?
- How can you ensure the blend factor stays within the 0 to 1 range?

❓ **Helpful Functions**
- `lerp(a, b, t)`: Linearly interpolates between `a` and `b` based on `t` (0 to 1)
- `saturate(x)`: Clamps `x` to the range [0, 1]

## Getting Started

1. Add properties for your two colors:

```glsl
Properties
{
    _Color1 //...
    _Color2 //...
    _BlendFactor //...
    // ... other properties ...
}
```

2. Declare these variables in your CGPROGRAM section:

```glsl
float4 _Color1;
float4 _Color2;
float _BlendFactor;
```

3. In your fragment shader, you can start with this basic blend:

```glsl
fixed4 frag (v2f i) : SV_Target
{
    // Calculate your blend factor here (example using a custom parameter)
    float blendFactor //...
    
    // Blend the colors
    fixed4 finalColor = lerp(//...);
    
    // Combine with existing shader logic (e.g., textures)

    //Return the final blended color
    return //...
}
```

## Challenge Extensions

- Try blending based on vertex position instead of a custom parameter
- Implement a smooth transition that cycles between the colors over time
- Add a third color and blend between all three
