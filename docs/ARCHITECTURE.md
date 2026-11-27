# System Architecture

## Core concept: Project Architect

The Project Architect is the orchestration layer. It translates chat messages into a versioned project specification and a dependency graph. Generators do not invent independent project conventions; they consume the same manifest and component contracts.

## Main subsystems

- Chat Interface: conversation, attachments, plan review, approval controls.
- Requirement Analyzer: extracts features, constraints, and open questions.
- Version Resolver: validates user-selected Minecraft version, Java runtime, loader, mappings, and APIs.
- Component Planner: decides which features belong in a mod, world, datapack, resource pack, plugin, or add-on.
- Manifest Store: persists the project specification and revision history.
- Dependency Graph: records references between items, entities, structures, loot tables, quests, dimensions, and assets.
- Generators: produce component-specific files.
- Integration Engine: validates cross-component references and compatibility.
- Build/Test Workers: isolated execution environments with resource limits.
- Export Engine: assembles editable project folder and delivery archives.

## Shared manifest

`schemas/project.schema.json` defines the initial contract. It must be extended through explicit schema versions rather than silently changing existing project meanings.

## World strategy

Hybrid world generation supports:
1. Prepared custom world: authored terrain, structures, routes, points of interest, and spawn locations.
2. Procedural generation: registered biomes, structures, features, and world-generation rules.
3. Hybrid composition: a prepared scenario/start region combined with procedural expansion where technically supported.

The chosen approach is recorded per project. A prepared world and procedural generation are not assumed to be interchangeable.

## Component ownership

- Mod: custom Java gameplay systems, entities, items, blocks, capabilities/data attachments, networking, and runtime mechanics.
- Datapack: supported data-driven registries, loot tables, recipes, tags, functions, predicates, advancements, and world data.
- World: terrain, authored structures, region layout, spawn points, and scenario placement.
- Resource pack: textures, models, sounds, language files, and visual assets.
- Quests/story: quest definitions and progression, implemented in the component that best supports the chosen loader/version.

The planner must not force a feature into a datapack if it requires Java runtime behavior.

## Validation layers

1. Static file/schema validation.
2. Identifier and reference validation.
3. Dependency/version validation.
4. Component-specific build or pack validation.
5. World loading validation.
6. Combined integration tests.
7. In-game/game-test validation when supported.

## Security

Generated code and build scripts are untrusted. Build workers must be isolated, resource-limited, and denied unnecessary secrets and network access. Dependency downloads should use approved repositories and be cached where possible.
