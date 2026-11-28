# AI Asset Generation Pipeline Specification

**Status:** Design draft  
**Version:** 1.0  
**Scope:** Shared asset production pipeline for Minecraft AI Mod Studio  
**Implementation status:** Not implemented  
**Decision policy:** Open decisions remain unresolved until explicitly approved.

## 1. Purpose

Define a platform-aware, reproducible pipeline for creating, importing, validating, transforming, reviewing, versioning, and delivering game assets used by Java mods, Bedrock add-ons, datapacks, resource packs, maps, structures, NPCs, items, animations, audio, and complete modpacks.

The pipeline is a shared production capability. It does not replace the domain-specific production engines; those engines declare asset requirements and consume approved asset outputs.

## 2. Design principles

- Treat every asset as a versioned project artifact with provenance and a stable identifier.
- Keep source files, editable intermediates, generated derivatives, and runtime exports distinct.
- Bind assets to the project manifest, target platform, Minecraft version, loader, and consuming component.
- Never silently substitute an asset or overwrite an approved version.
- Require explicit approval for consequential creative changes and final project-plan approval before production.
- Prefer deterministic transformations and reproducible builds where feasible.
- Record model/provider, prompt, parameters, seed when supported, toolchain, licenses, and validation evidence.
- Do not claim an asset is game-ready merely because an image, model, or audio file was generated.

## 3. Asset taxonomy

The pipeline supports:
- 2D raster: textures, icons, sprites, GUI elements, paintings, particle sheets.
- 2D vector: scalable interface and design source where supported by downstream tools.
- 3D: block/item/entity models, geometry, rigs, skeletons, collision proxies.
- Animation: skeletal, keyframe, block/entity animation, camera and motion data.
- Audio: sound effects, ambient loops, music, dialogue, voice lines and metadata.
- Text: localization, dialogue, lore, names, descriptions, credits and captions.
- World/build assets: schematics, structure templates, palettes, procedural-generation inputs.
- Data assets: recipes, loot definitions, tags, predicates, configuration and manifests.
- Composite assets: themed sets and coordinated asset bundles.

## 4. Pipeline architecture

Logical stages:
1. Requirement intake from a component engine.
2. Asset brief normalization.
3. Reference and style analysis.
4. Rights, safety and policy screening.
5. Modality and toolchain selection.
6. Generation or import.
7. Technical conversion and optimization.
8. Automated validation.
9. Preview and human review.
10. Revision and approval.
11. Versioned publication to the project asset registry.
12. Export through platform-specific adapters.

Each stage emits a structured result, status, logs, and artifact references. Stages must be resumable and idempotent where possible.

## 5. Asset brief contract

An asset brief should include:
- Stable asset ID and requested asset type.
- Intended gameplay purpose and consuming component IDs.
- Target platform(s), Minecraft version, loader and API constraints.
- Dimensions, resolution, geometry, format, duration, sample rate or other modality-specific constraints.
- Visual/audio style tokens and approved references.
- Required variants, language, accessibility and fallback requirements.
- Performance and memory budgets.
- License and provenance requirements.
- Acceptance criteria and preview requirements.
- Whether the asset is generated, imported, edited, or a hybrid.

Missing critical constraints must be clarified before generation rather than guessed.

## 6. Project Asset Registry

The registry is the authoritative index of project assets. It stores metadata and references, not necessarily the binary payload itself.

Required metadata:
- asset_id, project_id, component_id(s), asset_type.
- version, status, created_at, updated_at.
- source artifact reference and derived artifact references.
- content hash, MIME type, byte size and dimensions/duration where applicable.
- target compatibility declarations.
- provenance, provider/toolchain, prompt and generation parameters.
- rights/license declaration and attribution.
- validation report, review decisions and approval revision.
- dependency and supersession links.

Asset states: requested, briefing, queued, generating, converting, validating, needs_review, changes_requested, approved, published, superseded, failed, blocked, archived.

## 7. Generation adapters

Define provider-neutral adapter contracts for image, texture, 3D model, animation, audio, voice, text, and procedural asset generation.

Adapters must expose capability discovery, input schema, output schema, cancellation, timeout, retry classification, cost/usage reporting where available, and provenance. Provider-specific implementations remain replaceable.

No provider is assumed to be available, free, licensed for commercial use, or capable of a requested output until verified at runtime.

## 8. Import and reference workflow

Users may upload assets, provide references, or import assets from approved sources. The system must:
- Preserve original files as immutable source artifacts.
- Record source URL or user-provided provenance and license evidence.
- Scan file type, size, archive structure and malware risk.
- Detect duplicate content by hash.
- Flag unsupported or ambiguous licenses.
- Avoid treating a reference image as permission to reproduce protected characters, logos, or other restricted material.
- Keep reference material separate from generated deliverables.

## 9. Style and consistency management

A project may define approved style guides for palette, shape language, material, lighting, typography, audio identity and naming conventions.

Style profiles are versioned. Assets reference the exact style-profile revision used. Updating a style profile creates a reviewable impact proposal; it must not silently regenerate approved assets.

Cross-asset consistency checks may compare palettes, dimensions, naming, model scale, audio loudness and semantic tags. Automated similarity is advisory and cannot replace review.

## 10. Modality-specific validation

### 10.1 Textures and images
Validate dimensions, power-of-two requirements where relevant, alpha channel, color mode, tiling/seams, atlas constraints, animation frame layout and target format.

### 10.2 3D models
Validate geometry/schema, polygon and bone budgets, UV mapping, texture references, pivots, scale, hierarchy, collision representation and target renderer compatibility.

### 10.3 Animation
Validate rig binding, bone names, clip duration, frame rate, interpolation, missing tracks, root motion assumptions and target animation format.

### 10.4 Audio and voice
Validate codec, sample rate, channels, duration, peak/loudness policy, loop boundaries, silence, clipping, metadata and target engine format. Voice assets must retain consent and provenance records where applicable.

### 10.5 Text and localization
Validate encoding, placeholder integrity, key uniqueness, fallback language, formatting tokens, length constraints and missing translations.

### 10.6 Structures and world assets
Validate bounds, palette references, block/entity identifiers, version compatibility, placement rules, protected-region constraints and world corruption risk.

## 11. Conversion and optimization

Use explicit, versioned conversion profiles. Preserve originals and intermediate files. Optimization may include texture resizing/compression, model simplification, audio encoding, atlas generation and metadata normalization.

Every conversion records input/output hashes, tool version, settings and warnings. Lossy transformations require preview and must not overwrite source artifacts.

## 12. Preview and review workspace

Provide modality-aware previews:
- Texture and image viewer with transparency and tiling checks.
- 3D viewer with model, texture, rig and animation inspection.
- Audio player with waveform, loop and loudness information.
- Text/localization diff and placeholder inspection.
- Structure preview with bounds, palette and placement context.

Review actions: approve, request changes, reject, compare versions, annotate, and assign reviewer. Approval is bound to the exact asset version and project-plan revision.

## 13. Human approval and project gate

Generation may produce draft candidates before final approval only where the project workflow explicitly permits non-destructive previews. No approved project production job may consume an unapproved required asset.

Changing a brief, source reference, style profile, conversion settings or target compatibility after approval creates a new candidate version and invalidates the prior approval for the changed candidate.

## 14. Component engine integration

Each production engine declares:
- Required asset IDs/types and constraints.
- Optional asset slots and fallback behavior.
- Target formats and runtime identifiers.
- Whether generated assets are mandatory or user-supplied assets are acceptable.
- Validation and acceptance criteria.

The Asset Pipeline returns immutable asset-version references and validation evidence. Domain engines remain responsible for packaging assets into their own runtime outputs.

## 15. Dependency and impact graph

Represent dependencies between source assets, derived assets, style profiles, component specs and final packages.

When a source changes, compute the transitive impact set. Regenerate only affected derivatives, retain unaffected outputs, and request approval for changed deliverables. Detect cycles and reject invalid dependency graphs.

## 16. Storage and lifecycle

Separate:
- Original uploads.
- Generation outputs.
- Editable source/intermediate artifacts.
- Optimized derivatives.
- Published runtime assets.
- Validation reports and preview metadata.

Support content-addressed storage, deduplication, retention policies, archive and restore. Deletion must respect project ownership, legal retention and dependency constraints. Never silently delete an asset still referenced by a published project.

## 17. Security and isolation

Treat all uploads, archives, model files, scripts, metadata and provider outputs as untrusted. Enforce file size/type limits, archive path traversal protection, decompression limits, malware scanning, sandboxed parsers/converters, CPU/memory/time quotas, secret isolation and least-privilege access.

Do not execute uploaded code as part of asset preview. Network access from conversion workers is denied by default.

## 18. Rights, attribution and provenance

Track creator, source, license, attribution text, usage restrictions, model/provider terms and user declarations. Block publication when required rights evidence is missing or incompatible with the target distribution.

Do not imply that AI-generated content is automatically free of third-party rights. Provide a provenance report with each publishable asset bundle.

## 19. Queueing, scheduling and cost controls

Jobs support priority, cancellation, retry policy, concurrency limits, quotas, estimated usage where available, and user-visible status. Avoid duplicate work through idempotency keys and content hashes.

Costly external generation requires configured budget/usage controls and any required user confirmation. Free/local alternatives may be offered only when their capability and quality constraints are explicit.

## 20. Failure handling and recovery

Classify failures as validation, provider, conversion, storage, policy, compatibility, timeout, quota or user-cancellation. Preserve partial outputs and logs. Retry only transient failures. Provide actionable diagnostics and a resume path without duplicating completed stages.

A failed candidate must never replace the last approved asset version.

## 21. Observability and audit

Record job lifecycle, stage durations, tool/provider version, input/output hashes, warnings, validation results, approval events, user actions and resource usage. Redact secrets and sensitive prompt data from general logs. Provide trace IDs across component-engine jobs.

## 22. Export and delivery

Export approved assets in:
- Native editable source format where available.
- Intermediate interchange format where useful.
- Platform-specific runtime format.
- Metadata/provenance manifest.
- Validation and compatibility report.

Package outputs with deterministic paths and stable identifiers. The final mod/add-on/resource pack/world engine owns final package assembly.

## 23. API boundaries

Logical API capabilities:
- Create/update asset brief.
- Submit generation/import job.
- Get job status and logs.
- List/search project assets.
- Retrieve asset versions and metadata.
- Preview and compare versions.
- Approve/request changes/reject.
- Validate/convert/optimize.
- Resolve dependencies and impact.
- Export approved asset bundle.

Concrete endpoint names and schemas are deferred to the API contract phase.

## 24. Acceptance criteria

The design is acceptable when:
- Every asset is traceable to a brief, project revision and provenance record.
- Originals are immutable and derivatives are versioned.
- Platform compatibility is checked before publication.
- Approval is tied to an exact asset version.
- Failed generation cannot overwrite approved assets.
- Unsafe files are isolated and scanned.
- Dependency impact is calculable.
- Previews and validation evidence are available.
- Component engines consume stable asset references.
- Export contains editable sources where available and runtime-ready derivatives.
- Unavailable or unrun validation is clearly reported as not run.

## 25. Test strategy

Test asset schema validation, file scanning, malicious archive handling, conversion determinism, hash integrity, deduplication, provider timeout/retry, cancellation, quota enforcement, approval invalidation, dependency impact, concurrent edits, storage recovery, compatibility adapters, export reproducibility and end-to-end component integration.

Separate unit, integration, security, performance, compatibility and human-review tests. A generated preview is not proof of in-game correctness.

## 26. Open decisions

1. Which asset modalities are mandatory for the first release?
2. Which local generation tools are supported initially?
3. Which hosted providers, if any, are approved?
4. Is provider selection user-controlled, automatic, or hybrid?
5. What is the initial storage backend and size quota?
6. Which asset formats are canonical interchange formats?
7. Which preview capabilities are required in-browser versus desktop?
8. What are default texture/model/audio budgets?
9. Which rights evidence is mandatory for community publishing?
10. Who can approve assets in collaborative projects?
11. Are style profiles global, project-specific, or both?
12. What retention and deletion policies apply?
13. What is the initial job concurrency and quota policy?
14. Which modalities require human approval before every generation batch?
15. What is the minimum supported offline workflow?

## 27. Implementation boundary

This document defines intended behavior only. It does not assert that providers, converters, previews, scanners, storage services, or generation workers exist. Implementation requires approved scope, API contracts, security design, tests and an explicit development milestone.

## 28. Related specifications

Integrates with Product Requirements, Project Architect Decision Engine, Project Manifest, AI Model Provider Management, Java Mod Production, Bedrock Add-on Production, Datapack, Resource Pack, Map/World, NPC/Character, Animation/Model, Sound/Music/Voice, Modpack Resolver, Publishing and Security specifications.
