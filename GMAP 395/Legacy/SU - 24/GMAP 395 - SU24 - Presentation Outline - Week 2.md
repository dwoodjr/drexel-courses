# PART I: Practical Applications of Technical Art and Procedural Workflows in Games

---

## Review: What is Procedural Generation?

- Method for creating data or content using algorithms
- Enables creation of vast amounts of varied content
- Used in various aspects of game development

---

## Procedural Content Generation (PCG) in Games

- Landscapes / Terrain / Levels
- Narratives
- Loot systems
- Sound Design
- Animation
- VFX / Simulation
- Modeling
- Texturing

---

## Types of Procedurally Generated Games

1. Roguelike games
2. Open-World / Exploration games
3. Survival games
4. Puzzle games
5. Racing games (track generation)

---

## Case Study: Roguelike Games

- Procedurally generated levels
- Random item placement
- Permadeath and high replayability
- Examples: Hades, Dead Cells, Enter the Gungeon

---

## Case Study: Open-World Games

- Vast, procedurally generated landscapes
- Dynamic weather and ecosystems
- Procedural quest generation
- Examples: No Man's Sky, Minecraft, Valheim

---

## Taxonomy of PCG for Games

1. Game Bits
2. Game Space
3. Game System
4. Game Scenarios
5. Game Design

---

## Game Bits

- Units of game content that don't directly affect gameplay
- Examples:
  - Sound effects
  - Textures
  - 3D models
  - Particle effects

---

## Game Space

- Representations of the game environment
- Examples:
  - Levels
  - Maps
  - Terrain
  - Vegetation

---

## Game System

- Clusters of bits and space components that operate together
- Examples:
  - Weather systems
  - Ecosystems
  - Enemy spawning mechanics
  - Day/night cycles

---

## Game Scenarios

- Events that occur for content creation
- Examples:
  - Narrative generation
  - Quest creation
  - Level concepts
  - Character backstories

---

## Game Design

- Procedural generation of game rules and mechanics
- Examples:
  - Adaptive difficulty systems
  - Procedural puzzle generation
  - Dynamic balancing of game economies

---

## Node-Based Workflows

- Visual programming interfaces for content creation
- Nodes represent operations or data
- Connections show data flow between nodes

---

## Advantages of Node-Based Workflows

1. Visual representation of logic
2. Easier for artists to understand and use
3. Rapid prototyping and iteration
4. Reusable components and subgraphs

---

## Examples of Node-Based Tools

- Material editors (e.g., Unreal Engine's Material Editor)
- Visual scripting systems (e.g., Unity's Visual Scripting)
- Dedicated procedural tools (e.g., Houdini, Substance Designer)

---

## Basic Concepts: Nodes and Edges

- Nodes: Represent data or operations
- Edges: Connect nodes, showing data flow
- Directed Acyclic Graphs (DAGs): Ensure no infinite loops

---

## Practical Example: Building a Simple Material

[Insert image of a simple node-based material setup]

1. Texture input nodes
2. Mathematical operation nodes
3. Blending nodes
4. Output node

---

## Procedural Modeling Techniques

1. L-systems (for vegetation)
2. Shape grammars (for buildings)
3. Voronoi diagrams (for organic shapes)
4. Fractal algorithms (for terrains)

---

## L-systems for Vegetation

- Formal grammar for describing plant growth
- Rules for replacing parts of a simple object
- Applications: Trees, bushes, flowers

---

## Shape Grammars for Architecture

- Set of rules to generate complex structures
- Start with a basic shape, apply rules recursively
- Applications: Buildings, cities, spaceships

---

## Voronoi Diagrams in Game Design

- Partition space into regions based on distance to points
- Applications:
  - Terrain features (cracks, cell-like structures)
  - Territory division in strategy games
  - Organic textures and patterns

---

## Fractal Algorithms for Terrain

- Self-similar patterns at different scales
- Common algorithms:
  - Diamond-square algorithm
  - Perlin noise
  - Simplex noise

---

## Practical Applications in Game Development

1. Procedural terrain generation
2. Dynamic weather systems
3. Procedural character customization
4. Generative music and sound effects
5. Adaptive difficulty systems

---

## Terrain Generation Example

[Insert image of procedural terrain]

1. Generate heightmap using noise functions
2. Apply erosion algorithms
3. Distribute vegetation and other details
4. Optimize for runtime performance

---

## Implementing Modularity in Game Art

- Creating modular environment kits
- Developing modular character systems
- Best practices for asset organization

---

## Modular Environment Design

1. Define a grid system
2. Create reusable building blocks
3. Design connection points and variations
4. Use texture atlases for efficiency

---

## Modular Character Systems

1. Separate characters into swappable parts
2. Create a consistent rig for all characters
3. Design a system for mixing and matching parts
4. Implement runtime assembly of characters

---

## Tools for Technical Artists

- 3D modeling: Maya, Blender, 3ds Max
- Texturing: Substance Painter, Quixel Mixer
- Procedural generation: Houdini, World Machine
- Game engines: Unity, Unreal Engine

---

## 3D Basics for Technical Artists

- Geometry fundamentals
- UV mapping and texturing
- Basic 3D math concepts

---

## Geometry Fundamentals

- Vertices: Points in 3D space
- Edges: Lines connecting vertices
- Faces: Surfaces defined by edges
- Normals: Vectors perpendicular to surfaces

---

## UV Mapping and Texturing

- UV coordinates: 2D representation of 3D surfaces
- Texture mapping: Applying 2D images to 3D models
- Importance in game asset creation

---

## Basic 3D Math Concepts

- Vectors: Direction and magnitude
- Matrices: Transformations in 3D space
- Quaternions: Representing rotations

---

## Looking Ahead: Shaders and Materials

- Next module: Deep dive into shader development
- Combining procedural techniques with custom shaders
- Creating dynamic, responsive game materials

---

# PART II: Practical Procedural Workflows + Lightsaber Builder
## Thinking Procedurally in Practice

---

### Slide 1: Identifying Opportunities for Procedural Approaches

Content:
- Title: "Identifying Procedural Opportunities"
- Bullet points:
  - Repetitive content creation tasks
  - Need for scalable variety
  - Complex systems with interchangeable parts
  - Data-driven design requirements
  - Performance optimization needs

Speaker Notes:
These are general areas where procedural approaches can be beneficial in game development. Consider how these might apply to various systems in your games.

---

### Slide 2: Lightsaber Builder - Procedural Opportunities

Content:
- Title: "Lightsaber Builder - Procedural Opportunities"
- Bullet points:
  - Repetitive task: Creating individual lightsaber parts
  - Scalable variety: Generating diverse lightsaber designs
  - Interchangeable parts: Modular lightsaber components
  - Data-driven: Configurable part properties
  - Optimization: Efficient generation and rendering of complex lightsabers

Speaker Notes:
In our lightsaber system, we see procedural opportunities in the repetitive task of creating parts, the need for varied lightsaber designs, and the potential for a complex, interchangeable part system.

---

### Slide 3: Exercise - Analyzing Systems for Procedural Potential

Content:
- Title: "Exercise: Analyzing Systems for Procedural Potential"
- Questions to consider (for any system):
  1. What elements are currently created manually?
  2. Where do we need more variety or scalability?
  3. How could this system be more flexible for designers?
  4. Are there performance bottlenecks in content creation?

Speaker Notes:
These questions can be applied to any game system to identify areas where procedural approaches might be beneficial.

---

### Slide 4: Exercise - Analyzing the Lightsaber Builder

Content:
- Title: "Exercise: Analyzing the Lightsaber Builder"
- Lightsaber-specific questions:
  1. How are lightsaber parts currently created and assembled?
  2. Where do we need more variety in lightsaber designs?
  3. How can we make it easier for designers to create new lightsaber parts?
  4. Are there performance issues with complex lightsabers?

Speaker Notes:
Applying our general questions to the lightsaber builder helps us identify specific areas for procedural enhancement in this system.

---

### Slide 5: Modular Thinking in Game Design

Content:
- Title: "Modular Thinking in Game Design"
- Bullet points:
  - Breaking systems into reusable components
  - Identifying shared and unique properties
  - Creating flexible, composable elements
  - Designing for extensibility

Speaker Notes:
Modular thinking is crucial in procedural design. It allows for creating flexible, reusable components that can be combined in various ways.

---

### Slide 6: Modular Thinking in the Lightsaber Builder

Content:
- Title: "Modular Thinking in the Lightsaber Builder"
- Bullet points:
  - Breaking lightsabers into distinct parts (emitter, hilt, pommel, etc.)
  - Identifying shared properties (size, position) across all parts
  - Determining unique properties (emitter style, blade color)
  - Designing a flexible assembly system for parts

Speaker Notes:
In our lightsaber system, modular thinking means breaking down the lightsaber into distinct parts, identifying their shared and unique properties, and creating a flexible system for assembling these parts.

---

### Slide 7: Exercise - Designing Modular Components

Content:
- Title: "Exercise: Designing Modular Components"
- Steps:
  1. Identify the main components of your system
  2. List shared properties across all components
  3. Determine unique properties for each component type
  4. Consider how components will interact or combine

Speaker Notes:
These steps can be applied to any game system to break it down into modular, reusable components.

---

### Slide 8: Exercise - Designing Modular Lightsaber Components

Content:
- Title: "Exercise: Designing Modular Lightsaber Components"
- Lightsaber-specific steps:
  1. Identify main lightsaber parts (emitter, hilt, pommel, etc.)
  2. List shared properties (size, position, material)
  3. Determine unique properties (blade color for emitters, grip pattern for hilts)
  4. Design connection points between parts

Speaker Notes:
Applying our modular design steps to the lightsaber system helps us create a flexible, extensible set of lightsaber components.

---

### Slide 9: Algorithmic Thinking in Procedural Design

Content:
- Title: "Algorithmic Thinking in Procedural Design"
- Bullet points:
  - Defining clear rules and parameters
  - Creating systems for dynamic content generation
  - Balancing randomness and control
  - Ensuring consistency in procedural output

Speaker Notes:
Algorithmic thinking is about creating systematic approaches to content generation, balancing randomness with designer control.

---

### Slide 10: Algorithmic Thinking in Lightsaber Design

Content:
- Title: "Algorithmic Thinking in Lightsaber Design"
- Bullet points:
  - Defining rules for part generation and combination
  - Creating a system for dynamic lightsaber assembly
  - Balancing random elements (colors, sizes) with design constraints
  - Ensuring all generated lightsabers are functional and aesthetically pleasing

Speaker Notes:
In our lightsaber system, algorithmic thinking applies to generating part variations, ensuring proper assembly, and maintaining a consistent aesthetic across generated lightsabers.

---

### Slide 11: Exercise - Designing a Procedural Algorithm

Content:
- Title: "Exercise: Designing a Procedural Algorithm"
- General steps:
  1. Define input parameters
  2. Establish rules for content generation
  3. Implement variation and randomness
  4. Ensure output meets design requirements
  5. Optimize for performance

Speaker Notes:
These steps can be applied to design procedural algorithms for various game systems.

---

### Slide 12: Exercise - Designing a Lightsaber Assembly Algorithm

Content:
- Title: "Exercise: Designing a Lightsaber Assembly Algorithm"
- Lightsaber-specific steps:
  1. Define lightsaber parameters (part types, sizes, colors)
  2. Establish rules for part compatibility and assembly order
  3. Implement variation in part selection and properties
  4. Ensure every generated lightsaber is functional and visually appealing
  5. Optimize the generation process for real-time customization

Speaker Notes:
Applying our algorithmic design steps to the lightsaber system helps us create a robust, flexible lightsaber generation process.

---

## II. Designing Procedurally with Patterns

### Slide 13: Builder Pattern in Procedural Design

Content:
- Title: "Builder Pattern in Procedural Design"
- Key concepts:
  - Separates object construction from its representation
  - Allows for step-by-step creation of complex objects
  - Provides more control over the construction process
  - Useful for objects with many optional components or configurations

Speaker Notes:
The Builder pattern is valuable in many procedural systems, especially for creating complex objects with multiple configuration options.

---

### Slide 14: Builder Pattern in Lightsaber Construction

Content:
- Title: "Builder Pattern in Lightsaber Construction"
- Application to lightsabers:
  - Separates lightsaber assembly from individual part creation
  - Allows step-by-step addition of emitter, hilt, pommel, etc.
  - Provides control over the lightsaber construction process
  - Useful for creating diverse lightsaber configurations

Speaker Notes:
For our lightsaber builder, the Builder pattern allows us to construct lightsabers with various configurations of parts, providing a flexible way to create diverse designs.

---

### Slide 15: Exercise - Implementing a Builder

Content:
- Title: "Exercise: Implementing a Builder"
- General structure:
  ```csharp
  public class ComplexObjectBuilder
  {
      private ComplexObject _object = new ComplexObject();

      public ComplexObjectBuilder AddComponentA(ParametersA params)
      {
          // Add component A to the object
          return this;
      }

      public ComplexObjectBuilder AddComponentB(ParametersB params)
      {
          // Add component B to the object
          return this;
      }

      // More methods for other components

      public ComplexObject Build()
      {
          // Final construction and validation
          return _object;
      }
  }
  ```

Speaker Notes:
This structure can be applied to many types of game objects that require complex, step-by-step construction.

---

### Slide 16: Exercise - Implementing a Lightsaber Builder

Content:
- Title: "Exercise: Implementing a Lightsaber Builder"
- Lightsaber-specific structure:
  ```csharp
  public class LightsaberBuilder
  {
      private Lightsaber _saber = new Lightsaber();

      public LightsaberBuilder SetEmitter(EmitterType emitter)
      {
          _saber.Emitter = emitter;
          return this;
      }

      public LightsaberBuilder SetHilt(HiltType hilt)
      {
          _saber.Hilt = hilt;
          return this;
      }

      // More methods for other lightsaber parts

      public Lightsaber Build()
      {
          // Final lightsaber assembly and validation
          return _saber;
      }
  }
  ```

Speaker Notes:
This LightsaberBuilder implementation demonstrates how we can use the Builder pattern to create flexible, customizable lightsabers in our system.

---

### Slide 17: Factory Pattern in Procedural Generation

Content:
- Title: "Factory Pattern in Procedural Generation"
- Key concepts:
  - Centralizes object creation logic
  - Allows for dynamic object type selection
  - Facilitates addition of new object types
  - Useful for systems with families of related objects

Speaker Notes:
The Factory pattern is excellent for managing the creation of diverse but related objects in procedural systems.

---

### Slide 18: Factory Pattern in Lightsaber Part Generation

Content:
- Title: "Factory Pattern in Lightsaber Part Generation"
- Application to lightsaber parts:
  - Centralizes part creation logic
  - Allows for dynamic part type selection (emitters, hilts, etc.)
  - Facilitates addition of new part types
  - Useful for creating diverse but related lightsaber components

Speaker Notes:
In our lightsaber system, the Factory pattern can be used to generate different types of lightsaber parts based on input parameters, centralizing our part creation logic.

---

### Slide 19: Exercise - Designing a Factory

Content:
- Title: "Exercise: Designing a Factory"
- General structure:
  ```csharp
  public class ObjectFactory
  {
      public IObject CreateObject(ObjectType type, ObjectParameters parameters)
      {
          switch (type)
          {
              case ObjectType.TypeA:
                  return CreateTypeA(parameters);
              case ObjectType.TypeB:
                  return CreateTypeB(parameters);
              // More cases for other types
              default:
                  throw new ArgumentException("Invalid object type");
          }
      }

      private IObject CreateTypeA(ObjectParameters parameters)
      {
          // Creation logic for Type A
      }

      private IObject CreateTypeB(ObjectParameters parameters)
      {
          // Creation logic for Type B
      }
  }
  ```

Speaker Notes:
This factory structure can be adapted for various game systems that require creation of multiple related object types.

---

### Slide 20: Exercise - Designing a Lightsaber Part Factory

Content:
- Title: "Exercise: Designing a Lightsaber Part Factory"
- Lightsaber-specific structure:
  ```csharp
  public class LightsaberPartFactory
  {
      public ILightsaberPart CreatePart(PartType type, PartParameters parameters)
      {
          switch (type)
          {
              case PartType.Emitter:
                  return CreateEmitter(parameters);
              case PartType.Hilt:
                  return CreateHilt(parameters);
              // More cases for other part types
              default:
                  throw new ArgumentException("Invalid part type");
          }
      }

      private ILightsaberPart CreateEmitter(PartParameters parameters)
      {
          // Implementation for creating an emitter
      }

      private ILightsaberPart CreateHilt(PartParameters parameters)
      {
          // Implementation for creating a hilt
      }
  }
  ```

Speaker Notes:
This LightsaberPartFactory demonstrates how we can use the Factory pattern to centralize the creation of various lightsaber parts in our system.

---

## III. Developing Procedural Systems in Unity

### Slide 21: Leveraging Scriptable Objects in Procedural Systems

Content:
- Title: "Leveraging Scriptable Objects in Procedural Systems"
- Key benefits:
  - Data-driven design
  - Easy configuration for designers
  - Separation of data from logic
  - Improved performance for large datasets
  - Facilitates modular content creation

Speaker Notes:
Scriptable Objects are powerful tools for creating flexible, data-driven systems in Unity, particularly useful in procedural generation.

---

### Slide 22: Scriptable Objects in the Lightsaber System

Content:
- Title: "Scriptable Objects in the Lightsaber System"
- Applications:
  - Defining lightsaber part types and properties
  - Creating configurable generation rules
  - Storing preset lightsaber configurations
  - Managing performance for large part catalogs
  - Facilitating modular lightsaber design

Speaker Notes:
In our lightsaber builder, we can use Scriptable Objects to define part types, properties, and generation rules, making it easy for designers to create and modify parts without coding.

---

### Slide 23: Exercise - Creating Configurable Scriptable Objects

Content:
- Title: "Exercise: Creating Configurable Scriptable Objects"
- General structure:
  ```csharp
  [CreateAssetMenu(fileName = "New Configurable Object", menuName = "Procedural System/Configurable Object")]
  public class ConfigurableObjectSO : ScriptableObject
  {
      public ObjectType type;
      public float[] numericalParameters;
      public string[] textualParameters;
      public Gradient colorGradient;

      public GameObject GenerateObject()
      {
          // Implementation to generate an object based on this data
      }
  }
  ```

Speaker Notes:
This structure can be adapted for various game elements that require configurable, data-driven generation.

---

### Slide 24: Exercise - Creating Lightsaber Part Scriptable Objects

Content:
- Title: "Exercise: Creating Lightsaber Part Scriptable Objects"
- Lightsaber-specific structure:
  ```csharp
  [CreateAssetMenu(fileName = "New Lightsaber Part", menuName = "Lightsaber/Part")]
  public class LightsaberPartSO : ScriptableObject
  {
      public PartType type;
      public Mesh baseMesh;
      public Vector2 sizeRange = new Vector2(0.5f, 1.5f);
      public Color[] possibleColors;

      public GameObject GeneratePart()
      {
          // Implementation to generate a part based on this data
      }
  }
  ```

Speaker Notes:
This LightsaberPartSO demonstrates how we can use Scriptable Objects to define configurable lightsaber parts in our system, allowing for easy creation and modification of part types.

---

### Slide 25: Parametric Content Generation

Content:
- Title: "Parametric Content Generation"
- Key concepts:
  - Generating content based on adjustable parameters
  - Creating variations from base templates
  - Balancing randomness and designer control
  - Ensuring consistency across generated content

Speaker Notes:
Parametric generation allows for creating varied content from a set of rules and parameters, providing both flexibility and control in procedural systems.

---

###