95# GMAP 395-001 SU24 - Final Project Guide

## <font color="#ffc000">Overview</font>

Your final project is a culmination of the art and technical work covered in all five modules of this course. You will create an integrated, interactive game-like experience (not a full game) that showcases your skills in procedural workflows, custom shaders, visual effects, game audio implementation, and game lighting. This project should be an expansion and realization of the concept you developed in your pitch assignment.

Your project will focus on one of the following areas:
- Prop-focused experience
- Character-focused experience
- Environment-focused experience

> [!attention] 
> - While you may use existing assets and asset packs for supporting elements, all VFX, shaders, and materials for your main focus area must be original creations.
> - Ensure your project aligns with the game's theme and visual style as detailed in your original pitch document.
> - The final project must make use of proceduralism or modularity in the design of one or more assets or mechanics.
> - All assets and project elements not created by you must be cited in the postmortem documentation.

---
## <font color="#002060">Project Requirements by Module</font>

### 1. Procedural + Modular Modeling and Workflows (Procedural Game Art)

<font color="#002060">Definition:</font>
Procedural and modular modeling refers to the creation of game assets and environments using automated processes or reusable components. This approach allows for efficient content creation, easy iteration, and the potential for dynamic, varied game elements.

<font color="#ffc000">Requirements:</font>
- Implement ***<font color="#ffc000">a procedural and/or modular system</font>*** for your chosen focus area (prop, character, or environment)

<font color="#0070c0">Metrics:</font>
- Complexity and effectiveness of the procedural/modular system
- Creativity in applying procedural techniques to your chosen focus area

### 2. Material + Shader Development (Parameterized Shaders)

<font color="#002060">Definition:</font>
Shader and material development involves creating custom visual properties for game objects. This includes writing shader programs to control how objects are rendered and designing complex materials that define surface properties like color, texture, reflectivity, and visual effects.

<font color="#ffc000">Requirements:</font>
- Create ***<font color="#ffc000">at least 2</font>*** custom shaders using either Shader Graph or HLSL
- Shaders must be original creations and integral to your game's visual style

<font color="#0070c0">Metrics:</font>
- Technical complexity and correct implementation of shader techniques
- Visual impact and appropriateness of shaders to the game's aesthetic

### 3. Image + Particle Effects (VFX)

<font color="#002060">Definition:</font>
Image and particle effects encompass a range of visual enhancements that bring life and dynamism to a game scene. This includes creating particle systems for elements like fire or smoke, implementing shaders and meshes for VFX, and utilizing post-processing effects for designing dynamic visual feedback for player actions.

<font color="#ffc000">Requirements:</font>
- Develop ***<font color="#ffc000">at least 3</font>*** unique visual effects using either VFX Graph or the Particle System
- Effects should be meaningfully integrated into your game scene

<font color="#0070c0">Metrics:</font>
- Visual quality and complexity of effects
- Integration and interaction of effects with other game elements

### 4. Lighting + Camera Effects (Dynamic Game Lighting)

<font color="#002060">Definition:</font>
Lighting and camera effects focus on creating mood, atmosphere, and visual interest in a game scene. This involves setting up complex lighting scenarios, implementing dynamic lighting systems, and utilizing camera techniques and post-processing effects to enhance the visual experience.

<font color="#ffc000">Requirements:</font>
- Implement ***<font color="#ffc000">at least 3</font>*** distinct lighting sources in your scene (not including the Directional Light)
- Utilize ***<font color="#ffc000">2 or more</font>*** image effects or post-processing techniques

<font color="#0070c0">Metrics:</font>
- Effectiveness of lighting in setting mood and enhancing visual style
- Appropriate use of post-processing to enhance the overall aesthetic


### 5. Game Audio and Implementation (SFX)

<font color="#002060">Definition:</font>
Game audio implementation involves creating and integrating sound effects and music into a game environment. This includes designing spatial audio systems, creating reactive audio that responds to player actions, and ensuring that audio enhances the overall game experience.

<font color="#ffc000">Requirements:</font>
- Integrate ***<font color="#ffc000">at least 2</font>*** audio effects and/or music tracks
- Ensure proper spatial audio implementation where appropriate

<font color="#0070c0">Metrics:</font>
- Quality and appropriateness of audio to enhance game experience
- Integration of audio with game events and player actions

---
## <font color="#0070c0">Game-Based Interactivity</font>

Your project must provide meaningful, ***<font color="#ffc000">game-based (real-time) interactivity</font>*** that allows users to engage with and appreciate your custom-built elements. Consider the following aspects when designing your interactive experience:

- **Player Interaction**: Design intuitive ways for users to interact with your prop, character, or environment. This could involve direct manipulation, physics-based interactions, or other creative forms of engagement.
- **User Interface**: Develop a UI that enhances the interactive experience, allowing users to modify parameters, trigger effects, or navigate your creation.
- **Feedback and Response**: Ensure that your project provides clear, engaging feedback to user actions through visual, audio, and/or haptic means.
- **Narrative or Contextual Framing**: While a full game loop isn't necessary, consider providing a narrative or contextual frame that gives meaning to the user's interactions.

---
## <font color="#ffc000">Deliverables</font>

1. **Playthrough Video** (Max 10 minutes)
   - Demonstrate the core gameplay loop without narration

2. **Presentation Video** (Max 15 minutes)
   - Highlight how you've met each module's requirements
   - Discuss your creative and technical process

1. **Unity Project**
   - Zipped folder containing ***`Assets`, `Packages`, and `Project Settings`*** folders only
> [!danger] 
> Inclusion of any other folders, especially the ***Library*** folder, will result in a loss of points.

1. **Windows/PC Build**
   - Zipped folder with a playable build of your project
   - It is OK to include a ***`Builds`*** folder in the above zipped project folders.

1. **Postmortem Document**
   - Reflection on your development process (max 1 page)
   - Include at least one success, one challenge, and one new learning outcome
   - List all external assets used with appropriate citations
   - Revised game pitch based on the final result
> [!Danger]
> The postmortem document is meant to provide a space for reflection and documentation on your development journey, which is an important part of learning and developing a creative practice. It is ***not*** a space to vent: any derogatory remarks aimed at yourself, your peers, or the instructor will result in a ZERO (0) for your `Participation and Professionalism` portion of your final grade. *See the course syllabus for more info on this*.

---
## <font color="#002060">Evaluation Criteria</font>

Your project will be evaluated based on the following criteria:

- Technical execution and proper implementation of each module's concepts
- Creativity and originality in design and implementation
- Integration of procedural elements and modular design
- Visual cohesion and aesthetic appeal
- Functionality and engagement of the interactive experience
- Overall polish and user experience
### Grading Rubric

| Grade | Percentage | Description                                                                                                                                                                          |
| ----- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| A+    | 97-100%    | Exceptional work exceeding all requirements. Demonstrates mastery of all modules with innovative applications. Highly engaging and polished interactive experience.                  |
| A     | 93-96%     | Excellent work meeting all requirements with distinction. Deep understanding of all modules with creative implementation. Cohesive and engaging experience with minimal flaws.       |
| A-    | 90-92%     | Very good work meeting all requirements. Strong skills across all modules, some areas of excellence. Solid and engaging experience with minor issues.                                |
| B+    | 87-89%     | Good work meeting most requirements well. Competence in all modules, some areas of strength. Functional and mostly engaging experience with a few noticeable issues.                 |
| B     | 83-86%     | Satisfactory work meeting basic requirements. Understanding of all modules, may lack depth in some. Functional experience with some engagement or polish issues.                     |
| B-    | 80-82%     | Work meeting most basic requirements but inconsistent. Basic competence in most modules, may have one weak area. Experience may lack engagement or have several minor issues.        |
| C+    | 77-79%     | Work meeting some requirements, falling short in others. Basic understanding of most modules, significant weaknesses in one or two. Notable issues with functionality or engagement. |
| C     | 73-76%     | Work marginally meeting requirements. Basic competence in some modules, significant weaknesses in others. Functional but lacks polish and engagement.                                |
| C-    | 70-72%     | Work barely meeting minimum requirements. Minimal competence across modules, major weaknesses in several areas. Significant functionality or engagement issues.                      |
| D+    | 67-69%     | Work falling short of minimum requirements in several areas. Serious deficiencies across multiple modules. Incomplete or major functionality issues.                                 |
| D     | 63-66%     | Work significantly short of requirements. Lack of understanding in multiple crucial areas. Largely non-functional or incoherent experience.                                          |
| F     | 0-62%      | Work failing to meet most or all requirements. Fundamental lack of understanding of course concepts. Non-existent, non-functional, or completely misaligned with requirements.       |
|       |            |                                                                                                                                                                                      |

> [!attention] 
>  This rubric serves as a *guideline*. Final grades may be adjusted based on individual circumstances, effort, and improvement throughout the project development process and the class as a whole.

---



