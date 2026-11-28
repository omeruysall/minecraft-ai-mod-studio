# Minecraft Datapack Production Engine Specification

**Document status:** Draft design specification  
**Version:** 0.1  
**Scope:** Java Edition datapack authoring, validation, packaging, and world integration  
**Implementation status:** Not implemented  
**Approval status:** Awaiting design review

## 1. Purpose

The Datapack Production Engine transforms an explicitly approved datapack component specification into a version-pinned, structured, validated datapack with editable source files, test evidence, and a distributable ZIP package.

It is orchestrated by Project Architect and must only generate against the exact approved project revision. It must not be used to force unsupported runtime mechanics into datapack functions when a Java mod or another component is the correct technical owner.

A datapack that passes file/schema checks is not automatically proven to load or behave correctly in a world. Validation, load testing, and gameplay acceptance are separate evidence levels.

## 2. Scope and technical boundaries

In scope:
- Datapack folder and pack metadata generation.
- Namespaces, functions, tags, predicates, loot tables, recipes, advancements, and supported data-driven definitions.
- Supported world-generation data such as configured/placed features, structures, biome modifiers or equivalent version-specific mechanisms where available.
- Supported item, entity, block, and dimension data definitions where the target version permits them.
- Function scheduling, tick/load tags, scoreboards, storage, and supported command-driven systems.
- Cross-component references to Java mods, resource packs, and world/map projects.
- Version migration, validation, diagnostics, repair proposals, packaging, and world integration.
- Editable source folder, ZIP archive, manifests, and evidence reports.

Out of scope:
- Client-side visual assets as primary ownership.
- Java runtime classes, custom registries, arbitrary event listeners, or unsupported code execution.
- Bedrock behavior/resource packs.
- Server plugin logic.
- Direct modification of an existing world without backup, preview, and explicit approval.

Ownership rules:
- Datapacks own supported data-driven rules and command/function behavior.
- Java mods own custom runtime code, custom registries, and mechanics that require Java APIs.
- Resource packs own textures, models, sounds, and localization assets.
- World/map components own terrain, placed structures, and world-specific composition.
- A project may connect these components through explicit contracts and dependencies.

## 3. Inputs and preconditions

A production request includes:
- Project ID, component ID, immutable approved revision ID, and approval record.
- Exact Java Edition Minecraft target version and applicable pack format.
- Target environment and world type where relevant.
- Datapack identity, namespace, display name, version, description, authors, and license.
- Approved feature and requirement IDs.
- Function, data-definition, world-generation, and gameplay specifications.
- Component ownership, dependencies, and external mod requirements.
- Required tests, packaging, and world-integration policy.

Preconditions:
1. Approval matches the exact revision.
2. Minecraft version and target pack format are resolved.
3. Every requested feature has a valid technical owner.
4. Required vanilla/modded registries and dependencies are known.
5. All blocking ambiguities are resolved.
6. Each requested data type is supported by the target profile.
7. World-specific operations have an approved backup and rollback policy.

Unsupported or uncertain features are reported as unsupported/unknown or routed to another component. The engine must not silently invent commands, fields, registries, or mechanics.

## 4. Architecture and pipeline

1. **Request Validator** — checks schema, approval, revision, target version, and required inputs.
2. **Capability Resolver** — maps requested behavior to version-specific datapack capabilities.
3. **Ownership Router** — confirms that each feature belongs in a datapack rather than Java mod, resource pack, or world component.
4. **Pack Blueprint Builder** — plans namespaces, directories, files, references, and dependencies.
5. **Metadata Generator** — creates version-appropriate pack metadata.
6. **Data Definition Generator** — generates functions and supported JSON data resources.
7. **Reference Resolver** — validates identifiers, tags, function calls, loot/recipe references, and dependencies.
8. **Static Validator** — validates schemas, command syntax where tooling exists, paths, and resource ownership.
9. **Packager** — produces the source archive and distributable ZIP.
10. **World Test Orchestrator** — performs available load and gameplay tests in an isolated test world.
11. **Diagnostic Analyzer** — classifies validation, load, command, and runtime failures.
12. **Repair Planner** — proposes bounded fixes linked to approved features.
13. **Evidence Recorder** — records provenance, environment, logs, outcomes, and limitations.

Each stage has typed inputs/outputs and explicit failure states. A failed stage cannot be reported as successful by a later stage.

## 5. Version and pack-format compatibility

The capability registry maps exact Minecraft versions to:
- Pack format and metadata requirements.
- Available resource directories and JSON schemas.
- Command syntax and behavior changes.
- Function scheduling and tag semantics.
- Recipe, loot, advancement, predicate, and tag formats.
- World-generation data formats and migration requirements.
- Removed, renamed, deprecated, or experimental fields.
- Vanilla and modded registry availability.

A compatibility record includes version range, exact tested versions, evidence source, validation tooling, migration path, and confidence/evidence level.

The engine must target one explicit Minecraft version per build profile. Multi-version output is a set of separately generated and validated targets, not one assumed universally compatible ZIP.

Unknown or unverified fields are not emitted as if valid. Version migrations require a diff and revalidation.

## 6. Datapack structure and namespaces

The blueprint defines a deterministic directory tree according to the target pack format. It may include:
- Pack metadata.
- Namespace-scoped function directories.
- Function tags and supported data tags.
- Loot tables.
- Recipes.
- Advancements.
- Predicates or version-equivalent condition resources.
- Item modifiers or equivalent supported data resources.
- World-generation data.
- Structures or structure references where supported.
- A generation manifest, documentation, and license notices.

All project-owned identifiers must use a collision-resistant namespace. Namespace and path rules are validated. Vanilla identifiers and external mod namespaces must be explicitly declared rather than accidentally shadowed.

Every generated file is linked to its owning feature and requirement IDs.

## 7. Function system

The function subsystem supports:
- Ordinary functions.
- Load and tick entry points through supported tags.
- Nested function calls.
- Scheduling and cancellation where supported.
- Scoreboard objectives and score operations.
- Storage and data operations.
- Conditional execution and entity/location selectors.
- Namespaced function organization and shared utility functions.

Function generation controls:
- Detect direct and indirect recursion.
- Detect unbounded or excessively frequent scheduling.
- Identify expensive selectors and repeated broad scans.
- Validate referenced functions and tags.
- Flag command chains that may exceed target execution limits.
- Keep initialization idempotent where possible.
- Provide explicit uninstall/cleanup functions when the design creates persistent scoreboard/storage state.
- Avoid destructive global cleanup that can affect unrelated datapacks.

Tick-driven systems must include a documented performance budget and a test plan.

## 8. Data resource generation

### 8.1 Recipes
Generate supported recipe types, ingredients, results, conditions, and unlock behavior. Validate item identifiers, counts, serializer/type compatibility, and external dependencies. Custom recipe serializers requiring Java code belong to a Java mod component.

### 8.2 Loot tables
Generate supported pools, entries, conditions, functions, and references. Validate item/entity/block identifiers and detect invalid or unreachable branches where possible.

### 8.3 Advancements
Generate criteria, triggers, requirements, rewards, parent references, and display metadata. Validate trigger availability and cross-references against the target version.

### 8.4 Predicates and conditional data
Generate only condition formats supported by the target version. Validate referenced predicates and data resources. Version-specific alternatives must be explicit.

### 8.5 Tags
Generate supported block, item, fluid, entity, function, and other tag types. Validate replace semantics, required/optional references where supported, and dependency ownership. Detect conflicting tag definitions and unintended replacement of vanilla or third-party content.

### 8.6 World generation
Generate supported configured features, placed features, structures, biome modifications, dimension-related data, and other target-specific world-generation resources. The capability resolver must account for major version changes and modded registry dependencies. Existing world-generation changes may not affect already-generated chunks; this limitation must be explained and tested.

## 9. Modded datapack integration

When a datapack references modded content:
- Declare the required mod/component and compatible target profile.
- Validate registry identifiers against dependency metadata where available.
- Mark optional dependencies distinctly from required dependencies.
- Detect missing dependency packs and version mismatches.
- Avoid generating references to modded IDs that have not been confirmed.
- Record load-order or tag-order requirements where relevant.

The datapack engine does not create custom Java registries. If a requested recipe, entity, block, or mechanic requires a custom serializer, runtime hook, or registry, Project Architect must route that part to a Java mod component.

## 10. AI generation policy

AI generation is constrained by the approved blueprint:
- Generate only approved files and features.
- Use exact target-version schemas and command references.
- Do not invent command syntax, resource fields, or identifiers.
- Prefer small, traceable changes.
- Preserve user-authored files and namespace conventions.
- Link each file to feature/requirement IDs.
- Record generator, template, and model/provider provenance.
- Never embed secrets or private user data.
- Ask for clarification when requested behavior has multiple materially different interpretations.
- Route unsupported behavior to the appropriate component rather than approximating silently.

AI confidence is not validation evidence.

## 11. Static validation and performance analysis

Static checks include:
- Pack metadata and pack-format validation.
- JSON parsing and schema validation.
- Namespace and path validation.
- Function reference resolution.
- Function/tag/data reference integrity.
- Recipe, loot, advancement, predicate, and tag schema checks.
- Identifier existence checks against vanilla and declared mod registries.
- Duplicate/conflicting resource detection.
- Unsupported/deprecated field detection.
- Function recursion and scheduling analysis.
- Potentially expensive selector and tick-function warnings.
- Dependency and license checks.

Validation results include severity, file/line or JSON path, affected feature IDs, target version, evidence source, and suggested action.

## 12. World testing and evidence levels

Evidence levels are distinct:
1. **Schema validation** — metadata and JSON schemas pass.
2. **Reference validation** — identifiers, paths, functions, tags, and dependencies resolve.
3. **Command validation** — commands parse against the target version where a reliable validator exists.
4. **Package validation** — archive is structurally valid and contains expected files.
5. **World load test** — datapack is enabled in a clean target-version test world without relevant load errors.
6. **Function execution test** — load/tick/functions execute as expected.
7. **Gameplay acceptance test** — user-defined scenarios are executed in-game.
8. **Performance test** — tick impact and relevant resource use are measured.
9. **Manual review** — gameplay balance, usability, and intended experience are reviewed.

Each test records target version, world seed/configuration where relevant, enabled datapacks and order, dependencies, experiment settings, test IDs, feature/requirement IDs, timestamp, logs, outcome, and limitations.

Tests that cannot be run are NOT_RUN, never PASSED. Static validation cannot be described as in-game verification.

## 13. World installation, pack order, and rollback

Installation is separate from generation. For an existing world, the engine must:
- Create or verify a restorable backup.
- Show the intended file/world changes and datapack order.
- Identify required dependencies and version constraints.
- Explain whether new world generation is required for worldgen changes.
- Request explicit approval before modifying the world.
- Preserve unrelated datapacks and world data.
- Record the previous state and provide rollback instructions.

The engine must not silently overwrite an existing datapack with a matching name or namespace.

## 14. Packaging and delivery

Deliverables:
- Editable datapack source directory.
- Distributable ZIP with correct root structure.
- Generation manifest and dependency list.
- Target Minecraft version and pack-format declaration.
- Installation/activation instructions.
- License and attribution notices.
- Validation and test report.
- Known limitations and unrun tests.
- Checksums and provenance metadata.

The package builder checks archive paths, duplicate entries, unexpected files, metadata location, and required resources. It must prevent path traversal and unsafe archive content.

## 15. Repair and incremental regeneration

Repair workflow:
1. Collect structured diagnostics.
2. Classify schema, syntax, reference, compatibility, dependency, performance, load, or gameplay failure.
3. Map to feature and requirement IDs.
4. Propose a bounded repair.
5. Verify approved-scope compliance.
6. Apply in an isolated revision.
7. Re-run relevant checks and regression tests.
8. Record diffs and evidence.

Changes to user-visible behavior, feature scope, target version, dependencies, or world-level effects require Project Architect review and explicit re-approval.

The engine tracks file ownership and dependency edges. It regenerates only safely owned affected files, preserves user work, previews deletions/modifications, and supports rollback. Uncertain ownership results in a conflict, not an overwrite.

## 16. Security and isolation

- Treat prompts, imported datapacks, JSON, commands, and archives as untrusted.
- Process archives in isolated workspaces with resource limits.
- Never execute arbitrary imported scripts or commands on the host.
- Validate archive paths and reject traversal, unsafe symlinks, duplicate paths, and oversized files.
- Restrict filesystem access and network egress.
- Do not permit generated functions to modify user worlds during validation.
- Use disposable test worlds and preserve backups.
- Redact secrets from logs and audit world modifications and publishing actions.

## 17. Observability and provenance

Record project/component/revision IDs, target version, pack format, validator/schema versions, generator/template/model versions, dependencies, file ownership, job stage/status/duration, resource usage, diagnostics, test environment, enabled datapacks, logs, checksums, and repair history.

User-facing diagnostics must identify the affected feature and actionable next step without exposing secrets or unsafe host details.

## 18. Acceptance criteria

The design is ready for implementation when:
- Generation requires approval for the exact revision.
- Exact Minecraft version and pack format are validated.
- Datapack ownership is distinguished from Java mod, resource pack, and world ownership.
- Functions, tags, recipes, loot, advancements, predicates, and worldgen are covered by explicit generators and validators.
- Modded dependencies are declared and checked.
- Unsupported mechanics are routed rather than silently approximated.
- Static, load, execution, gameplay, and performance evidence are distinct.
- Unrun tests are never reported as passed.
- Existing worlds are backed up and modified only with explicit approval.
- User-authored files are not silently overwritten.
- Deliverables include editable source, ZIP, dependencies, provenance, checksums, and honest test reports.

## 19. Open design decisions

1. Initial supported Minecraft Java version window and pack-format policy.
2. Whether first release targets vanilla datapacks only or also modded datapacks.
3. First-release data-resource feature matrix.
4. Whether world-generation authoring is first-release scope or a later milestone.
5. Which command parser/static-analysis tools are adopted.
6. Whether a real Minecraft test server/client is required for first-release validation.
7. Local, hosted, or hybrid test-world execution.
8. Whether the engine may create disposable worlds automatically.
9. Policy for datapack dependencies and required mod registry metadata.
10. Namespace allocation and collision policy across published projects.
11. Whether automatic migration between Minecraft versions is supported initially.
12. Performance budgets and warning thresholds for tick functions.
13. Whether installation into existing worlds is included in the first release.
14. Artifact retention, storage, and cleanup policy.
15. Whether publishing is part of this engine or the separate community/publishing subsystem.

## 20. Related specifications

- docs/PROJECT_ARCHITECT_DECISION_ENGINE.md
- docs/MINECRAFT_VERSION_COMPATIBILITY_ENGINE_SPEC.md
- docs/JAVA_MOD_PRODUCTION_ENGINE_SPEC.md
- docs/BEDROCK_ADDON_PRODUCTION_ENGINE_SPEC.md
- docs/STUDIO_INTERFACE_AND_COMMUNITY_SPEC.md
- docs/DESIGN_FIRST_DELIVERY_WORKFLOW.md

## 21. Change control

This document is a draft design specification. It does not authorize implementation. Changes to scope, target compatibility, or open decisions must be reflected in the design baseline and reviewed before implementation begins.
