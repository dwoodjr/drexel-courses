## Objective
Develop a shader + material system that interacts with its environment or user input in real-time. This system should be applicable to a prop-based, character-based, or environment-based asset of your choice, aligning with your Final Project focus.

## Requirements

### 1. Shader Development:
Create a shader (using either HLSL or Shader Graph) that incorporates at least two of the following effects:

1. Color changes based on a parameter (e.g., position, time, or custom input)
2. Texture distortion or displacement (e.g., UV/texture scrolling)
3. Emission (Emissive material property) that responds to a variable (e.g., simulated energy levels)
4. Simple vertex displacement (e.g., waves or pulsing)
5. Texture blending based on a parameter (e.g., height, time, or custom input)
6. Transparency/opacity control based on a parameter
7. Texture map/Normal map intensity based on a parameter

> 💡 **Tip:** Start simple! Begin with one effect and add complexity as you go. Remember, you can use the techniques we practiced in the in-class lab as a starting point.

> 📘 **Note:** If using Shader Graph, explore the Sample Texture node for texture effects and the Time node for animation.

### 2. C# Integration + Procedural Control:
Develop a C# script that controls at least two shader parameters in real-time. ***One of the two should controlled procedurally through C# scripting.***
Some examples:

- Object interaction (e.g., player proximity or mouse hover)
- Time-based variations (e.g., sin() wave animation)
- Simulated environmental factor (e.g., day/night cycle or "temperature")

> 🔍 **Example:** If you chose color changes in your shader, your C# script could change the color based on player proximity. For vertex displacement, you could control the amplitude based on a simulated energy level.

> ⚠️ **Important:** Remember to create public variables in your shader and link them in your Material Inspector to control them via C#.

### 3. Technical Art Showcase:
Create a demo scene that showcases your shader's capabilities in the context of your chosen asset type (prop, character, or environment).

> 🎨 **Idea:** For a prop, you could show how it reacts when a player approaches. For an environment, you could demonstrate how it changes over a day/night cycle.

### 4. Documentation:
Provide a brief (1-2 page) technical write-up explaining:
- Your shader's functionality
- How the C# script interacts with the shader
- How your system could be applied in a game context

> 📝 **Hint:** Include screenshots or diagrams to help explain your system. Don't forget to mention any challenges you faced and how you overcame them.

## Deliverables

1. Unity project folders (**ASSETS, PACKAGES, PROJECT SETTINGS**) zipped:
   - Your shader file(s) (HLSL or Shader Graph)
   - C# scripts for shader control
   - Demo scene showcasing your shader
   - Any necessary textures or additional assets
2. Technical write-up (PDF/DOCX format)
3. Short video (1-2 minutes) demonstrating your shader's capabilities and interactions

## Evaluation Criteria

- Shader Implementation and Effectiveness
- C# Integration and Real-time Control
- Creativity and Relevance to Chosen Asset Type
- Documentation and Presentation

## Tips for Success

- ***Start early and iterate often.*** It's okay if your first version is very simple!
- Test your shader on multiple objects to ensure it works well with different geometries.
- Don't hesitate to reach out for clarification or guidance.
- Remember, the goal is to learn and experiment. Have fun with it!