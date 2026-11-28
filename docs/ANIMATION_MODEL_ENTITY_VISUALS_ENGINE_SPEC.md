# Animation, Models & Entity Visuals Engine Specification

**Document status:** Design draft  
**Version:** 0.1  
**Implementation status:** Not implemented; design requirements only.  
**Approval status:** Awaiting product decisions and baseline approval.

## 1. Purpose
Define the pipeline for creating, importing, editing, validating, previewing, and packaging entity models, block models, animations, rigs, textures, visual effects, and cosmetic variants for Minecraft projects. The engine provides consistent visual assets while keeping gameplay behavior owned by the appropriate runtime systems.

## 2. Ownership boundaries
- This engine owns model/rig/animation asset definitions, visual metadata, conversion, validation, and packaging contracts.
- Resource Pack Engine owns texture/model resource-pack assembly and platform-specific resource delivery.
- NPC, Combat, and Item engines own gameplay entity/item behavior and stable content identities.
- AI Asset Generation Pipeline owns model/texture generation orchestration and provenance.
- Audio Engine owns sound assets and playback metadata.
- Java/Bedrock production adapters own runtime-specific registration and animation APIs.
- Project Architect owns approval, dependency impact, and manifest references.

## 3. Principles
- Visual assets are separate from gameplay logic and cannot imply unimplemented behavior.
- Every asset has a stable ID, version, source/provenance, license metadata, and target-platform declaration.
- Imported and generated assets are treated as untrusted until validated.
- Rig and animation behavior must be tested on exact target versions.
- Asset changes are versioned and dependency-aware.
- Preserve user-authored assets and provide reversible replacement workflows.

## 4. Scope
In scope: entity models, block/item models, rigs, bones, animation clips, controllers, texture sets, UV layouts, skins, variants, attachments, particles, visual effects, conversion, optimization, preview, and asset packaging.

Out of scope: arbitrary executable animation scripts, guaranteed support for every third-party renderer, and claiming a rendered preview proves in-game compatibility.

## 5. Asset identity and manifest
Each asset records stable namespaced ID, type, schema version, display metadata, file references, dimensions, target edition/version, dependencies, license/provenance, author, source lineage, and compatibility status. Manifest references must remain stable when display names change.

## 6. Model and rig representation
Define geometry, origin, scale, coordinate conventions, bones, pivots, hierarchy, constraints, attachment points, hitbox references, and animation channels. Validate bone count, hierarchy cycles, transforms, and platform-specific limits. Gameplay hitboxes remain owned by gameplay systems unless an explicit mapping is defined.

## 7. Animation clip model
Clips define target rig, duration, frame rate, keyframes, interpolation, loop mode, blend behavior, event markers, and playback conditions. Use bounded frame/key counts and deterministic playback metadata. Unsupported interpolation or channels are reported before packaging.

## 8. Animation controllers and state mapping
Controllers map declared entity states and events to animation clips with transitions, priorities, blend rules, and fallback states. NPC/Combat engines provide semantic state events; visual controllers do not independently decide combat or AI outcomes. Prevent transition loops and invalid state references.

## 9. Texture and UV pipeline
Define texture dimensions, formats, UV mapping, transparency, mipmap policy, color space, and atlas rules. Validate missing textures, invalid UVs, unsupported formats, and excessive resolution. Resource Pack Engine owns final pack composition and resource location mapping.

## 10. Entity and item visual variants
Variants define skins, palettes, equipment attachments, cosmetic layers, and conditional visual changes. Variant selection must not change gameplay stats or permissions unless a separate gameplay contract authorizes it. Stable variant IDs support saves and network synchronization.

## 11. Particles and visual effects
Effects define emitter type, shape, rate, lifetime, velocity, color/texture references, attachment, and visibility scope. Bound particle counts and update cost. Combat/Magic engines emit semantic effect events; this engine renders only approved visual feedback.

## 12. Import and conversion
Support declared formats and versions only. Validate archive paths, geometry bounds, texture sizes, rig hierarchy, animation channels, and external references. Conversion reports lost features and approximations. Preserve original source files alongside converted editable assets when permitted.

## 13. Preview and authoring tools
Provide model viewport, rig hierarchy, bone inspector, animation timeline, keyframe editor, texture/UV view, variant preview, and platform capability warnings. Preview metadata must clearly distinguish offline rendering from target-game runtime behavior.

## 14. Platform adapters
Map asset structures to supported Java loader/rendering APIs and Bedrock entity geometry/animation formats. Adapter capability matrices list supported bones, animation channels, controllers, texture rules, and limitations. No universal cross-platform parity is assumed.

## 15. Performance and optimization
Set budgets for geometry complexity, bones, keyframes, texture memory, particle rate, and concurrent animated entities. Support LOD or simplified variants where the platform allows. Avoid expensive per-frame logic and excessive texture atlases.

## 16. Multiplayer and synchronization
Gameplay state is server-authoritative. Clients receive bounded visual state and cosmetic selection where permitted. Define late-join state, animation event replication, cosmetic ownership, and fallback for missing assets. Visual desync must not alter gameplay outcomes.

## 17. Accessibility and readability
Provide configurable visual intensity, particle reduction, animation toggles where safe, contrast considerations, and nonvisual gameplay feedback where needed. Critical gameplay information cannot rely only on color, flashing, or subtle animation.

## 18. Licensing, provenance, and content review
Record source, generation lineage, author attribution, license, and redistribution permissions. Flag missing or incompatible rights. Apply project content policies to generated/imported visuals. User approval does not override third-party licensing restrictions.

## 19. Security and asset safety
Treat files as untrusted. Enforce archive path safety, size limits, decompression limits, image decoder safety, and sandboxed conversion. Do not execute scripts embedded in assets. Generated files are scanned and validated before packaging.

## 20. Authoring experience
Provide model/rig creation, animation authoring, texture editing/import, variant manager, effect designer, asset browser, dependency viewer, and preview. Conversational requests become a visual asset plan listing target entity, style, rig, animation set, texture requirements, platform limits, dependencies, and rights checks before approval.

## 21. Validation and testing
Validate schema, geometry, bone hierarchy, texture references, UVs, animation targets, controller transitions, particle budgets, licensing metadata, and platform mapping. Tests cover import/export, preview, in-game loading, animation playback, state transitions, multiplayer late join, missing-asset fallback, and performance with target entity counts. Unrun tests are reported as not run.

## 22. Diagnostics and repair
Expose asset dependency graph, missing references, unsupported channels, rig/clip mismatch, texture warnings, runtime load errors, and performance budget violations. Repair suggestions must preserve source assets and provide diffs before replacement.

## 23. Delivery
Deliver editable source assets, normalized model/rig files, animation clips/controllers, texture sets, variant definitions, platform-ready resource files, provenance/license manifest, compatibility report, and test evidence. Include previews but clearly label their evidence level.

## 24. Acceptance criteria
- Assets have stable IDs, versions, provenance, and target-platform declarations.
- Model, rig, animation, and texture validation runs before packaging.
- Gameplay state remains owned by gameplay engines.
- Unsupported platform features are reported accurately.
- Import/conversion preserves source and documents losses.
- Performance budgets are explicit and tested.
- Multiplayer visual state cannot alter authoritative gameplay.
- Licensing and content review metadata are retained.
- Target-game runtime tests confirm load and playback.
- User assets are never silently overwritten.

## 25. Open decisions
1. Which editions, versions, and loaders are first-release targets?
2. Which model and animation formats are supported for import/export?
3. Is in-app 3D model editing required or is external-tool integration sufficient?
4. Which rig standards and bone limits are supported?
5. Which animation controller capabilities are required?
6. Are block and item models included in this engine or delegated entirely to Resource Pack?
7. Which texture editing functions are included?
8. What are texture resolution and memory limits?
9. Which particle/effect primitives are supported?
10. Are cosmetic variants player-selectable, gameplay-unlocked, or both?
11. Which visual features must degrade gracefully across Java and Bedrock?
12. What is the default policy for missing or unsupported assets?
13. Which optimization/LOD features are required?
14. What are target entity counts and performance budgets?
15. Which animation events may be synchronized over multiplayer?
16. Which accessibility controls are mandatory?
17. Which third-party tools and formats are integrated?
18. What provenance and license metadata is mandatory?
19. What content moderation checks apply to generated/imported assets?
20. Which asset migrations are required when rigs or IDs change?
21. Where are source assets and generated previews stored?
22. What cache and retention policies apply?
23. Which external renderers/libraries are permitted and under what licenses?
24. Which in-game load, playback, and performance tests block release?

## 26. Current status
Design draft only. All open decisions remain unresolved until explicitly decided by the product owner. No model editor, rig system, animation authoring runtime, asset converter, or in-game visual pipeline is implemented by this document.
