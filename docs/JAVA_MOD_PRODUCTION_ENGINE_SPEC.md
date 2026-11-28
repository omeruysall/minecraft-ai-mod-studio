# Java Mod Production Engine Specification

**Document status:** Draft design specification  
**Version:** 0.1  
**Scope:** Java Edition mod production for Fabric, Forge, and NeoForge targets  
**Implementation status:** Not implemented  
**Approval status:** Awaiting design review

## 1. Purpose

The Java Mod Production Engine converts an approved, version-pinned mod component specification into a reproducible Java project, source code, resources, build outputs, and verifiable test evidence. It is a production subsystem orchestrated by Project Architect; it is not the conversational planner and it must never begin generation before the relevant project revision has explicit approval.

A successful Gradle build is evidence of build success only. It is not proof that a mod loads correctly, behaves correctly, or is playable.

## 2. Scope and boundaries

The engine owns Java Edition mod source projects and loader-specific integration. It supports target profiles selected by the user and resolved by the Version Compatibility Engine.

In scope:
- Fabric, Forge, and NeoForge adapter contracts.
- Gradle project and source-set generation.
- Mod metadata, entry points, registries, events, lifecycle, configuration, networking, data generation, assets, localization, and packaging.
- Supported blocks, items, entities, effects, recipes, creative tabs, commands, screens, and other Java runtime features.
- Dependency declarations, generated resource references, build diagnostics, repair proposals, and test evidence.
- Deliverable source project, reproducible build instructions, JARs where build succeeds, and source archive.

Out of scope:
- Bedrock add-on production.
- Datapack-only features and world/map authoring as primary ownership.
- Resource-pack-only production except Java mod assets required by the mod.
- Server plugin production.
- Independent version compatibility decisions; those belong to the Version Compatibility Engine.
- Unapproved changes to the approved feature scope.

## 3. Inputs and preconditions

The engine accepts a versioned production request containing:
- Project ID, component ID, immutable approved revision ID, and approval record.
- Java Edition target profile: exact Minecraft version, loader, loader version, Java toolchain requirement, mappings/API profile where applicable.
- Mod identity: namespace, mod ID, display name, version, description, authors, license, and optional homepage/contact metadata.
- Feature specifications with stable requirement and feature IDs.
- Component ownership and dependency graph.
- Required registries and runtime behavior.
- Asset, localization, configuration, networking, and data-generation requirements.
- Build, test, and delivery policy.
- Explicit user constraints and approved assumptions.

Precondition checks:
1. Approval is valid for the exact revision being produced.
2. Target profile is resolved and internally consistent.
3. Every requested feature has an assigned technical owner.
4. Required dependencies and licenses have been evaluated.
5. No blocking ambiguity remains in the production request.
6. The selected adapter declares support for the requested target profile.

If a precondition fails, return a structured blocked result; do not silently guess or generate a partial deliverable as if complete.

## 4. Engine architecture

The engine is divided into explicit stages:

1. **Request Validator** — validates schema, approval, revision, target profile, and required fields.
2. **Capability Mapper** — maps approved features to Java/loader capabilities and identifies unsupported or conditional operations.
3. **Project Blueprint Builder** — creates a deterministic file and module plan before writing files.
4. **Loader Adapter** — translates neutral feature contracts into Fabric, Forge, or NeoForge integration points.
5. **Code and Resource Generator** — generates source, metadata, data, assets, and localization.
6. **Dependency Resolver** — validates declared libraries, loader APIs, optional integrations, and version constraints.
7. **Static Validator** — checks source structure, identifiers, references, schemas, and prohibited patterns.
8. **Build Orchestrator** — executes the pinned Gradle build in an isolated workspace.
9. **Diagnostic Analyzer** — normalizes compiler and build failures into actionable diagnostics.
10. **Repair Planner** — proposes bounded changes tied to failing requirements; changes requiring scope expansion return to approval.
11. **Test Orchestrator** — runs available tests and records evidence levels.
12. **Packager** — creates deliverables and a manifest with checksums.
13. **Evidence Recorder** — stores provenance, logs, toolchain versions, test outcomes, and limitations.

Each stage has typed inputs and outputs. A stage failure must not be represented as success by a later stage.

## 5. Neutral feature model and loader adapters

The engine maintains a loader-neutral feature model. It describes intent and expected behavior without assuming a particular loader API.

Each adapter must declare:
- Supported Minecraft version ranges and exact tested target profiles.
- Supported feature capabilities and known limitations.
- Required Java toolchain and build plugin constraints.
- Metadata format and entry-point conventions.
- Registry and lifecycle integration strategy.
- Event, configuration, networking, and data-generation facilities.
- Required mappings or API artifacts.
- Known migration and incompatibility notes.

Adapters:
- Fabric Adapter
- Forge Adapter
- NeoForge Adapter

The adapter must not claim compatibility merely because a dependency can be downloaded. Compatibility requires validated metadata and, where available, build/load evidence. Loader-specific source may be generated in separate source sets or adapter modules where that is safer than forcing a false common abstraction.

No loader-specific API names or versions are hardcoded as timeless facts in this specification. Exact API choices are resolved against the pinned target profile during implementation.

## 6. Generated project structure

The blueprint defines a predictable Gradle project structure. A typical project may contain:
- Gradle wrapper and settings/build scripts.
- Project metadata and mod metadata.
- Main Java source.
- Loader-specific Java source or adapter modules.
- Main resources and loader-specific resources.
- Data-generation source and generated data.
- Textures, models, sounds, language files, and other assets.
- Configuration defaults and schemas where supported.
- Unit/integration test source sets.
- Documentation, licenses, notices, and generation manifest.

The actual structure is adapter- and target-profile-dependent. The engine records why a file exists and which requirement or feature owns it.

Generated files must not overwrite user-authored files without an explicit conflict policy. Regeneration must preserve user edits through ownership metadata, protected regions, or a merge/conflict workflow. The initial implementation must prefer safe conflict reporting over destructive replacement.

## 7. Feature generation contracts

Every generated feature is represented by a feature contract containing:
- Stable feature ID and linked requirement IDs.
- User-visible behavior and acceptance criteria.
- Owning component and loader adapter.
- Source files and resource files owned by the feature.
- Registrations, identifiers, references, and dependencies.
- Configuration and networking implications.
- Tests required and evidence level achieved.
- Generation provenance and repair history.

Supported feature families include:

### 7.1 Registries and content
- Blocks and block properties/states.
- Items and item groups/creative tabs.
- Block entities and custom data where required.
- Entities, attributes, spawn rules, and AI behavior where supported.
- Effects, potions, enchantments, particles, sounds, and other supported registries.
- Biomes, world features, structures, and placement only where the target APIs and component ownership permit it.

### 7.2 Gameplay and data
- Recipes and serializers where custom behavior requires Java code.
- Loot integration, tags, advancements, predicates, and functions when Java ownership is genuinely required.
- Commands and permissions.
- Interactions, tools, custom mechanics, and server-authoritative behavior.
- World-generation hooks and custom placement logic.

Data-driven functionality should be delegated to a datapack component when that is the correct technical owner. The Java engine must not duplicate datapack responsibilities merely to keep all files in one component.

### 7.3 Client presentation
- Screens, menus, HUD elements, key bindings, renderers, particles, and client-only assets.
- Strict separation of client-only and dedicated-server-safe code.
- Explicit checks for accidental client class loading on a dedicated server.

### 7.4 Configuration and networking
- Typed configuration with defaults, validation, and documented ranges.
- Clear distinction between client, server, and common configuration.
- Network message schemas, direction, validation, authorization, and compatibility checks.
- Server-side validation for all gameplay-critical state changes.
- No trust in client-supplied values for privileged or authoritative actions.

### 7.5 Assets and localization
- Stable namespaced identifiers.
- Model/texture/sound references validated against actual files.
- Localization keys generated consistently and checked for missing values.
- Asset licensing and attribution recorded.
- Missing assets must be reported; placeholders must never be silently represented as final artwork.

## 8. AI code-generation policy

AI generation is constrained by the approved blueprint and feature contracts.

Required controls:
- Generate only files assigned to the current component and approved revision.
- Use target-profile-aware templates and verified adapter capabilities.
- Prefer small, traceable changes over broad rewrites.
- Do not invent APIs, dependencies, registry identifiers, or version compatibility.
- When evidence is insufficient, stop and request clarification or mark the feature blocked.
- Preserve requirement and feature IDs in generation metadata.
- Produce a change summary linking each changed file to the reason and owning feature.
- Keep generated code deterministic where practical; record model/provider and template versions for provenance.
- Separate generated code from user-authored code and third-party code.
- Do not embed secrets, API keys, private tokens, or personal data in source, logs, or artifacts.

Generated code must be reviewed by static validation and build/test stages. AI confidence is not test evidence.

## 9. Dependency and license governance

Every dependency record includes:
- Coordinate or source identifier, version/range, purpose, owning feature, scope, and required/optional status.
- Compatibility evidence for the selected Minecraft and loader profile.
- License identifier and attribution obligations where known.
- Repository/source provenance and integrity information where available.

Rules:
- No unapproved dependency additions.
- Prefer pinned, reproducible versions over floating versions.
- Detect duplicate/conflicting dependencies and incompatible transitive constraints.
- Do not bundle third-party code/assets unless licensing permits it.
- Flag unknown, restrictive, or incompatible licenses for review.
- Optional integrations must degrade safely when absent and must not become accidental hard dependencies.

## 10. Build orchestration and reproducibility

The build orchestrator:
- Runs in an isolated, disposable workspace with bounded CPU, memory, disk, and execution time.
- Uses the target profile's pinned toolchain and Gradle wrapper.
- Disables unnecessary network access after dependency resolution where practical.
- Captures command, environment summary, dependency resolution, stdout/stderr, exit code, and duration.
- Prevents generated scripts from accessing host credentials or unrelated workspace files.
- Uses clean builds for release evidence.
- Records artifact checksums and build provenance.

Build states:
- NOT_STARTED
- QUEUED
- RUNNING
- SUCCEEDED
- FAILED
- CANCELLED
- BLOCKED

A build result is SUCCEEDED only when the expected build task exits successfully and required artifacts are verified to exist and match the expected component.

## 11. Validation and testing ladder

Evidence levels must be reported separately:

1. **Schema validation** — request, blueprint, metadata, and manifest schemas pass.
2. **Static validation** — identifiers, file references, ownership, source checks, and dependency rules pass.
3. **Compilation/build** — pinned Gradle build succeeds.
4. **Artifact validation** — expected JAR and metadata are present and inspectable.
5. **Loader smoke test** — target Minecraft instance starts with the mod and records load evidence.
6. **Dedicated server test** — server starts without client-only class failures, when relevant.
7. **Integration test** — declared dependent components work together.
8. **Gameplay test** — acceptance scenarios are executed in a real or controlled game environment.
9. **Manual review** — visual, balance, usability, and gameplay behavior are reviewed by a human where automation is insufficient.

Each test record includes test ID, requirement/feature IDs, target profile, environment, timestamp, status, logs/evidence references, and limitations. Unavailable tests are NOT_RUN, not PASSED. A JAR build alone must never be described as playable or fully tested.

## 12. Repair loop and change control

The repair loop:
1. Collect structured diagnostics.
2. Classify the failure: generator, adapter, dependency, source, asset, environment, or test.
3. Map diagnostics to feature and requirement IDs.
4. Produce a bounded repair proposal.
5. Verify that the repair remains inside approved scope.
6. Apply repair in an isolated revision.
7. Re-run the smallest relevant checks, then required regression checks.
8. Record before/after evidence and changed files.

A repair that changes user-visible behavior, adds a feature, changes target profile, introduces a dependency with material implications, or alters approved requirements must return to Project Architect for clarification and explicit re-approval. No automatic scope expansion.

Retry limits and escalation thresholds will be configured by policy; endless generation/build loops are prohibited.

## 13. Incremental regeneration and user edits

The engine tracks file ownership and dependency edges. When a feature changes:
- Determine impacted features and files from the dependency graph.
- Regenerate only the affected owned files where safe.
- Preserve unaffected files and user-authored content.
- Show a preview of file additions, modifications, and deletions.
- Require approval for destructive changes or changes outside the approved revision.
- Record generated diffs and allow rollback to a prior component revision.

If ownership cannot be determined reliably, stop and present a conflict instead of overwriting.

## 14. Packaging and deliverables

A completed production attempt may produce:
- Source project directory.
- Source ZIP.
- Built mod JAR, only if build and artifact validation succeed.
- Required runtime assets and dependency manifest.
- Build instructions and target profile summary.
- License/attribution notices.
- Test report and known limitations.
- Generation manifest and checksums.

The delivery manifest records each artifact's type, path, size, checksum, target profile, source revision, build status, and test evidence. Failed or blocked runs may deliver diagnostic bundles, but must not be presented as completed mods.

## 15. API and event contract

The engine is exposed through versioned internal service contracts. Candidate operations:
- validate_production_request
- create_project_blueprint
- generate_component
- validate_component
- start_build
- get_build_status
- analyze_diagnostics
- propose_repair
- apply_approved_repair
- run_component_tests
- package_component
- get_production_evidence

Long-running operations use job IDs and emit lifecycle events. Events include correlation ID, project/component/revision IDs, stage, status, timestamp, and safe diagnostic summary. Exact HTTP routes and schemas belong in the API contract design stage and are not fixed by this document.

## 16. Security and isolation

- Treat user prompts, imported source, mod assets, build scripts, and dependency metadata as untrusted input.
- Run builds and tests in isolated sandboxes with least privilege.
- Restrict filesystem access to the job workspace.
- Apply network egress policy and dependency allow/deny controls.
- Scan archives for path traversal, symlinks, oversized entries, and malicious payload patterns.
- Never execute arbitrary generated scripts on the host.
- Redact secrets and sensitive environment variables from logs.
- Enforce resource/time limits and cancellation.
- Record security-relevant actions in an audit trail.

## 17. Observability and operational records

Record:
- Stage and job status, durations, retries, and resource usage.
- Generator, adapter, template, model/provider, Gradle, Java, and dependency versions.
- File-level provenance and feature ownership.
- Build/test logs and artifact checksums.
- Failure classification and repair history.

Logs must be structured, correlated, access-controlled, and scrubbed of secrets. User-facing messages should summarize actionable failures without exposing internal secrets or unsafe host details.

## 18. Acceptance criteria

The engine design is acceptable for implementation when:
- It refuses generation without approval for the exact revision.
- It validates a complete Java target profile before generation.
- Fabric, Forge, and NeoForge are isolated behind explicit adapter contracts.
- A blueprint can be reviewed before files are written.
- Generated files are traceable to feature and requirement IDs.
- Client/server separation and dependency/license checks are enforced.
- Build execution is isolated and reproducible.
- Build, load, integration, and gameplay evidence are reported as distinct levels.
- Unrun tests are never marked passed.
- Repair cannot silently expand scope.
- User-authored files are not destructively overwritten.
- Deliverables include source, provenance, checksums, and truthful test reports.
- A successful build is never equated with confirmed playability.

## 19. Open design decisions

The following are intentionally unresolved and must be decided before implementation:
1. Initial supported Minecraft Java version window and release policy.
2. Which loaders are included in the first implementation milestone: Fabric, Forge, NeoForge, or staged rollout.
3. Whether the first release supports one loader per component or multi-loader source generation.
4. First-release feature matrix: blocks/items only, or also entities, world generation, screens, networking, and advanced mechanics.
5. Whether data generation is Gradle-task-driven, runtime-driven, or both per adapter.
6. Supported Java toolchain policy and exact toolchain acquisition strategy.
7. Whether mod metadata and build templates are maintained internally, generated from schemas, or both.
8. Whether external dependency resolution is unrestricted, allowlisted, or approval-gated.
9. Whether automated Minecraft client/server launch tests are required in the first release.
10. Whether the build sandbox is hosted, local, or hybrid in the first release.
11. Whether generated source is always fully editable or includes protected/generated regions.
12. Artifact retention, storage limits, and cleanup policy.
13. Required license selection and default policy for newly generated projects.
14. Whether signing/release publishing is in scope for the initial engine or a later publishing subsystem.

## 20. Related specifications

- docs/PROJECT_ARCHITECT_DECISION_ENGINE.md
- docs/MINECRAFT_VERSION_COMPATIBILITY_ENGINE_SPEC.md
- docs/AI_CONVERSATION_AND_REQUIREMENTS_ANALYSIS_SPEC.md
- docs/AI_MODEL_PROVIDER_MANAGEMENT_SPEC.md
- docs/REALTIME_VOICE_COMMUNICATION_SPEC.md
- docs/STUDIO_INTERFACE_AND_COMMUNITY_SPEC.md
- docs/DESIGN_FIRST_DELIVERY_WORKFLOW.md

## 21. Change control

This document is a draft design specification. It does not authorize implementation. Changes to its scope or decisions must be reflected in the design baseline and reviewed before implementation begins.
