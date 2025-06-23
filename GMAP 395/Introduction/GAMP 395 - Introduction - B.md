# Module 1B: Procedural Thinking Basics

> [!info] Module Overview 
> **Time Required:** 5-7 minutes 
> **Learning Focus:** Understanding procedural workflows and algorithmic content creation **
> Builds On:** Module 1A (Technical Art fundamentals)

---

## What is Procedural Thinking?

**Procedural thinking involves using algorithms and rules to automate content creation.** Instead of manually creating each element, you define a set of instructions that generate content automatically. This approach transforms repetitive manual work into systematic, scalable processes.

### The Procedural Mindset

Traditional approach: _"I need to model 50 unique trees"_ 
Procedural approach: _"I need to create rules that generate 50 unique trees automatically"_

**Key principle:** Write the rules once, generate infinite variations. (obviously developing rules takes time, but I hope you get the idea)

---

## Applications in Game Development

### Terrain and Foliage Generation
- **Landscape Creation**: Algorithmic height maps and erosion simulation
- **Vegetation Placement**: Rules-based distribution of plants and trees
- **Biome Systems**: Automatic climate-based environment generation

### Character Customization Systems
- **Modular Characters**: Mix-and-match clothing, accessories, and features
- **Procedural Animation**: Rule-based movement and behavior systems
- **Dynamic Scaling**: Automatic adaptation for different character sizes

### Level and Architecture Design
- **Building Generation**: Modular construction systems with infinite variations
- **Dungeon Creation**: Algorithmic layout with gameplay flow considerations
- **Urban Planning**: Procedural cities with realistic street layouts and zoning

---

## Benefits of Procedural Workflows

### Efficiency
- **Reduces time** spent on repetitive tasks
- **Accelerates iteration** through parameter adjustment
- **Eliminates manual errors** in repetitive processes

### Scalability
- **Enables creation** of vast, dynamic worlds
- **Supports rapid prototyping** of multiple design directions
- **Facilitates easy updates** across entire asset libraries

### Creative Enhancement
- **Generates unexpected results** that inspire new directions
- **Provides systematic exploration** of design spaces
- **Maintains consistency** while enabling variation

<iframe width="560" height="315" src="https://www.youtube.com/embed/-LHj7-kROoo?si=WSbIhUlEEd1RLDMv" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

> [!NOTE] GDC Talk = Long Video
> This is a lengthy video, please do not attempt to watch the full video during class!
> I recommend watching from the beginning to about 6:10 (Usual Evolution+)
> Feel free to watch the full outside of class if it particularly interesting to you.


---

## Procedural vs. Manual: When to Use Each

### Use Procedural When:
- Creating many similar but varied elements
- Needing to iterate quickly on design parameters
- Working with systematic, rule-based patterns
- Building scalable content pipelines

### Use Manual When:
- Creating hero assets requiring precise artistic control
- Working with unique, one-off designs
- Dealing with highly irregular or organic forms
- Fine-tuning specific aesthetic details

### Hybrid Approach (Most Common)

**Combine procedural generation with manual refinement:**
1. Generate base content procedurally
2. Manually adjust and refine key elements
3. Use procedural methods for variations and iterations

---

## Common Procedural Operations

### Scattering and Distribution
- **Random Placement**: Distributing objects with controlled variation
- **Density Control**: Using maps and rules to control placement frequency
- **Collision Avoidance**: Ensuring scattered objects don't intersect inappropriately

### Pattern Generation
- **Geometric Patterns**: Mathematical relationships creating regular designs
- **Noise-Based Variation**: Using algorithmic noise for organic randomness
- **Rule-Based Systems**: Logic that determines pattern behavior

### Parameter Manipulation
- **Randomization**: Controlled variation within specified ranges
- **Mathematical Relationships**: Linking parameters through equations
- **Conditional Logic**: Rules that trigger based on specific conditions

### Modular Assembly
- **Component Systems**: Combining pre-made pieces in systematic ways
- **Constraint-Based Placement**: Rules governing how pieces connect
- **Variation Generation**: Creating diversity from limited base components

---

## Procedural Thinking in Practice

### Example: Forest Generation System

**Manual Approach:**
1. Model individual trees
2. Place each tree by hand
3. Adjust size and rotation manually
4. Repeat for ***hundreds*** of trees

**Procedural Approach:**
1. Create base tree models (3-5+ variations)
2. Define placement rules (density, slope tolerance, clustering)
3. Set variation parameters (scale, rotation, species distribution)
4. Generate forest automatically with controllable parameters
	**Result:** Same visual quality, fraction of the time, infinite variation potential

---

## Learning Check: Procedural Analysis

> [!question] Pattern Recognition Exercise (3-4 minutes) **Identify Procedural Elements:** Think of games you've played recently and identify 3 examples where procedural generation might have been used. Consider:
> 
> **Examples to look for:**
> - Repeating but varied elements (buildings, trees, rocks)
> - Large-scale environments with systematic patterns
> - Character customization systems
> - Weapon or item generation systems
> 
> **Analysis Questions:**
> - What made you think this element was procedural?
> - What rules or patterns do you notice?
> - How does the system create variety while maintaining consistency?

**Write down your examples** - you'll share these during class discussion next week.

---

## Procedural Content Generation (PCG) Overview
PCG encompasses different types of automated content creation:

### Game Bits
- **Assets**: Textures, sounds, models
- **Components**: Individual game elements

### Game Space
- **Levels**: Playable areas and environments
- **Terrains**: Landscapes and geographical features
- **Maps**: Layout and spatial organization

### Game Systems
- **Rules**: Mechanical relationships and interactions
- **Mechanics**: Gameplay systems and features

### Game Scenarios
- **Events**: Dynamic occurrences and triggers
- **Narratives**: Story elements and branching paths
- **Quests**: Mission and objective generation

---

## Real-World Examples

### _No Man's Sky_
- **Infinite Universe**: Procedurally generated planets, flora, and fauna
- **Systematic Variety**: Consistent rules creating believable diversity
- **Player Discovery**: Each player experiences unique content

### _Minecraft_
- **Terrain Generation**: Algorithmic landscapes with biome systems
- **Structure Placement**: Villages, dungeons, and landmarks
- **Resource Distribution**: Ore placement following geological rules

### _Borderlands Series_
- **Weapon Generation**: Millions of unique weapons from modular components
- **Stat Calculation**: Mathematical systems determining weapon properties
- **Visual Variety**: Procedural combinations of parts and materials

---

## Additional Resources

> [!tip] Explore Further
> 
> - [Procedural Workflows Explained - Autodesk](https://www.autodesk.com/solutions/proceduralism)
> - [Procedural Content Generation in Games - Free Online Book](https://www.pcgbook.com/)
> - [The Art of Procedural Noise(Video)](https://www.youtube.com/watch?v=erI7k3lt4UY)

### Advanced Topics (For Later Exploration)

- **L-Systems**: Rule-based systems for generating fractal-like structures
- **Voronoi Patterns**: Mathematical techniques for organic-looking distributions
- **Flow Fields**: Directing procedural systems with vector fields

---

## Next: Module 1C - Node-Based Workflows

**Coming up:** We'll explore how visual scripting systems make procedural thinking accessible and powerful for artists.

> [!info] Progress Tracking
> 
> - [x] Module 1A: What is Technical Art? ✓
> - [x] Module 1B: Procedural Thinking Basics ✓
> - [ ] Module 1C: Node-Based Workflows Introduction

---
---

>[!info] Module Navigation 
>**Previous:** [[GMAP 395 - Introduction - A|Module IA]]  
>**Next:** [[GMAP 395 - Introduction - C|Module IC]]
>**Return to:** [[GMAP 395 - Introduction and Overview|Module Page]]