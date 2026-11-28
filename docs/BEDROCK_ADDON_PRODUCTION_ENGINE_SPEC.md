# Bedrock Add-on Production Engine Specification

**Document status:** Draft design specification  
**Version:** 0.1  
**Scope:** Minecraft Bedrock Edition add-on production  
**Implementation status:** Not implemented  
**Approval status:** Awaiting design review

## 1. Purpose

The Bedrock Add-on Production Engine converts an explicitly approved, version-pinned Bedrock component specification into valid Behavior Packs, Resource Packs, scripts where supported, integrated test packages, and verifiable delivery artifacts. It is orchestrated by Project Architect and must validate approval for the exact revision before writing files.

JSON validation does not prove that a pack is loadable; successful loading does not prove correct behavior or playability. These are separate evidence levels.

## 2. Scope and ownership

In scope:
- Behavior Pack generation and Resource Pack generation.
- Manifest, UUID, module, version, and dependency management.
- Supported entity, item, block, recipe, loot, spawn, trade, and other data-driven definitions.
- Script API integration where the selected Bedrock target supports the required capability.
- Localization, textures, models, sounds, animations, controllers, and pack-stack integration.
- World-level installation/integration when explicitly requested.
- Validation, packaging, diagnostics, repair proposals, and test evidence.
- Editable source folders, ZIP archives, .mcpack and .mcaddon packages where appropriate.

Out of scope:
- Java Edition mods and loader adapters.
- Java server plugins.
- Unsupported or undocumented runtime hooks.
- Automatic modification of an existing world without backup and explicit approval.

Ownership boundaries:
- Behavior Pack owns supported gameplay definitions and behavior data.
- Resource Pack owns visual/audio assets, client presentation, and localization assets.
- Script modules own supported runtime logic that requires scripting.
- World/map components own terrain, structures, placed content, and world-specific configuration.
- Multi-component projects connect these artifacts through explicit dependencies without collapsing ownership into one opaque package.

## 3. Inputs and preconditions

The production request contains project/component IDs, immutable approved revision and approval record, exact Bedrock target profile, target environment, pack identity and metadata, approved feature/requirement IDs, component ownership, dependencies, assets, licensing, validation policy, and delivery policy.

Precondition checks:
1. Approval is valid for the exact revision.
2. Target Bedrock version/build and environment are identified.
3. Every feature has a technical owner.
4. Required capabilities exist in the selected target profile.
5. Dependencies and pack-stack relationships are resolvable.
6. Blocking ambiguities are resolved.
7. Preview or experimental API usage is explicitly identified and approved.

Unsupported or uncertain features must be reported as such. The engine must not silently substitute behavior and claim equivalence.

## 4. Architecture and production pipeline

1. **Request Validator** — validates schema, approval, revision, target version, and environment.
2. **Capability Resolver** — maps features to supported Bedrock capabilities and evidence.
3. **Pack Architecture Planner** — assigns Behavior Pack, Resource Pack, script, and world responsibilities.
4. **Manifest and Identity Manager** — manages UUIDs, versions, dependencies, and metadata.
5. **Definition Generator** — generates supported JSON definitions and references.
6. **Script Generator** — generates script modules only when the target API supports the required capability.
7. **Asset Pipeline** — generates/imports textures, models, sounds, animations, controllers, and localization.
8. **Reference and Stack Validator** — validates identifiers, dependencies, pack order, and cross-pack references.
9. **Package Builder** — creates installable packages and source archives.
10. **Runtime Test Orchestrator** — runs available import, load, behavior, multiplayer, and gameplay tests.
11. **Diagnostic Analyzer** — normalizes schema, import, script, and runtime failures.
12. **Repair Planner** — proposes bounded repairs tied to approved features.
13. **Evidence Recorder** — stores provenance, target profile, logs, test outcomes, and limitations.

Each stage has explicit inputs and outputs. Failure in one stage cannot be represented as success by a later stage.

## 5. Bedrock capability profiles

The capability registry describes each feature against a concrete Bedrock target profile. Each record includes stable capability ID, supported versions/environments, pack format or module type, required Script API modules, stability status, world prerequisites, restrictions, incompatibilities, validation method, evidence source, and verification date.

Capability statuses:
- Stable supported.
- Supported with explicit prerequisites.
- Preview or experimental.
- Version-dependent.
- Unsupported.
- Unknown / requires verification.

A feature is not supported merely because a sample file exists. Exact formats, schemas, and API modules must be checked against the pinned target profile. Preview and experimental dependencies must never be silently enabled.

## 6. Pack architecture

### 6.1 Behavior Pack

Owns supported gameplay data such as entity definitions, component groups, events, spawn rules, supported AI behavior, items, blocks, recipes, loot tables, trade tables, functions, and script references. Identifiers, component availability, event references, and cross-file links must be validated.

### 6.2 Resource Pack

Owns textures, atlases, geometry, render controllers, materials, animations, animation controllers, sounds, UI assets where supported, language files, and client-side presentation. Every resource reference must resolve to an included file or declared dependency. Missing assets are reported; placeholders cannot be presented as finished artwork.

### 6.3 Script modules

Scripts are used only when supported data-driven definitions cannot safely implement the requested behavior. The subsystem must:
- Pin compatible Script API modules and target versions.
- Separate client/server responsibilities where supported.
- Validate event subscriptions and API usage against the capability registry.
- Avoid undocumented APIs and runtime patching.
- Validate untrusted player/entity/input data.
- Enforce server-authoritative checks for gameplay-critical actions.
- Handle lifecycle, initialization, and runtime errors.
- Prevent unbounded loops and excessive ticking work.

TypeScript may be used with a reproducible compilation step where supported. The package must contain runtime-compatible output and required metadata.

### 6.4 World integration

A world component may install/reference required packs, configure pack-stack order, and include world-specific settings. Existing-world modification requires a backup, preview, explicit approval, rollback path, and preservation checks. Global pack installation must not be assumed to configure an existing world automatically.

## 7. Manifest, identity, and versioning

The identity manager validates manifests against the target profile and manages:
- Unique pack and module UUIDs.
- Module type and entry-point metadata.
- Pack versions and minimum engine declarations where required.
- Explicit Behavior Pack, Resource Pack, and script dependencies.
- Dependency UUID/version consistency.
- Distinct identities for independent packs.

UUID policy:
- Generate unique UUIDs for new pack/module identities.
- Preserve UUIDs across ordinary revisions of the same logical pack.
- Do not regenerate identity during routine builds.
- Create new identities for intentionally forked or independent packages.
- Detect collisions across the project dependency graph.

Manifest schemas and format-version constraints are target-specific and must be verified before implementation.

## 8. Feature generation contracts

Each feature contract includes stable feature and requirement IDs, user-visible behavior, acceptance criteria, owning pack/module, target profile, required capabilities, generated files, cross-file references, identifiers, dependencies, asset references, tests, evidence status, and generation/repair provenance.

Feature families:
- **Entities:** custom entities, components, component groups, events, spawn rules, supported AI, health, movement, interactions, equipment, and presentation links.
- **Blocks and items:** definitions, supported components, properties/states, interactions, durability, placement/destruction, recipes, loot, inventory categorization, and visual/localization references.
- **Gameplay:** crafting, loot, trades, interactions, events, functions, and script-backed mechanics where necessary; multiplayer-safe and server-authoritative behavior.
- **Presentation:** geometry, textures, animations, controllers, particles, sounds, UI, and localization.

The engine must clearly identify requested features that Bedrock cannot support in the chosen target profile.

## 9. AI generation policy

AI generation is constrained by the approved pack blueprint and feature contracts:
- Generate only files assigned to the component and approved revision.
- Use target-aware schemas and verified capabilities.
- Do not invent JSON fields, components, Script API methods, or version support.
- Prefer small, traceable edits.
- Preserve stable identifiers and UUIDs.
- Link generated files to feature and requirement IDs.
- Separate generated, user-authored, and third-party files/assets.
- Record generator, template, and model/provider provenance.
- Never embed credentials or private user data.
- Stop and request clarification when behavior cannot be represented reliably.

AI confidence is not validation evidence.

## 10. Asset production and licensing

Asset records include asset ID/type/format/path, dimensions or duration where applicable, owning feature and pack, source (generated/user/third-party), license/permission, attribution, references, and validation status.

Checks include format and dimension constraints, naming/path conventions, missing or duplicate references, invalid animation/controller links, unused assets, packaging omissions, and licensing. Third-party assets must not be bundled unless rights permit it. Unknown rights trigger review.

## 11. Validation ladder

Evidence levels are separate:
1. **Schema validation** — manifests and JSON definitions match the target schemas.
2. **Reference validation** — identifiers, paths, dependencies, UUIDs, and pack relationships resolve.
3. **Script validation** — scripts compile/type-check against pinned API declarations and pass static checks.
4. **Package validation** — archives are structurally valid and contain expected files.
5. **Import test** — target client/server imports the package without rejection.
6. **Load test** — packs activate in the intended world/environment.
7. **Runtime test** — scripts, entities, items, blocks, and interactions execute without relevant errors.
8. **Multiplayer/server test** — behavior works in the intended multiplayer/server environment.
9. **Gameplay acceptance test** — user-defined scenarios are executed in-game.
10. **Manual review** — visual quality, usability, balance, and gameplay are reviewed where automation is insufficient.

Each test records test ID, feature/requirement IDs, game version, environment, pack stack, experiment settings, timestamp, status, evidence, and limitations. Tests unavailable in the environment are NOT_RUN, never PASSED.

## 12. Packaging and installation

Deliverables may include editable Behavior Pack and Resource Pack folders, script source/build configuration, .mcpack individual packs, .mcaddon bundles, source ZIP, installation instructions, dependency/pack-stack manifest, validation/test report, known limitations, checksums, and provenance manifest.

The package builder validates archive paths, duplicate entries, manifests, dependencies, and expected files; it protects against path traversal and unsafe archive content.

Installation is separate from generation. No package is installed into the user's game and no world is modified without explicit confirmation. Instructions must identify required world settings, experiments, activation steps, and multiplayer limitations.

## 13. Repair and change control

Repair workflow:
1. Collect structured diagnostics.
2. Classify schema, capability, manifest, reference, asset, script, package, import, load, or runtime failure.
3. Map issue to feature/requirement IDs.
4. Propose bounded repair.
5. Verify it remains within approved scope.
6. Apply in an isolated revision.
7. Re-run relevant validators and regression tests.
8. Record diffs and before/after evidence.

Changes to user-visible behavior, features, target version, experiment requirements, pack ownership, or material dependencies require Project Architect review and explicit re-approval. Retry limits prevent endless loops.

## 14. Incremental regeneration and user edits

Track file ownership and dependency relationships. On feature changes, identify impacted definitions/scripts/assets/manifests, regenerate only safely owned files, preserve user-authored content, preview additions/modifications/deletions, require approval for destructive changes, preserve UUIDs, record diffs, and support rollback. If merge safety is uncertain, stop and present a conflict.

## 15. API and event contracts

Candidate internal operations:
- validate_bedrock_request
- resolve_bedrock_capabilities
- create_pack_blueprint
- generate_behavior_pack
- generate_resource_pack
- generate_script_module
- validate_pack_manifests
- validate_pack_references
- build_addon_packages
- run_import_tests
- run_runtime_tests
- analyze_bedrock_diagnostics
- propose_bedrock_repair
- package_bedrock_delivery
- get_bedrock_evidence

Long-running operations use job IDs and lifecycle events containing correlation ID, project/component/revision IDs, stage, status, timestamp, and safe diagnostic summary. Exact HTTP routes/schemas belong to the API contract design stage.

## 16. Security and isolation

Treat prompts, imported packs, JSON, scripts, archives, and assets as untrusted. Run processing in isolated workspaces; never execute arbitrary imported/generated scripts on the host. Restrict filesystem access and network egress. Enforce CPU, memory, archive-size, and execution-time limits. Scan archives for traversal paths, symlinks, duplicate paths, and oversized entries. Validate external references, redact secrets, and audit installation, world modification, and publishing actions.

## 17. Observability and provenance

Record target game version, environment, pack format, API module versions, experiment settings, generator/template/model versions, job status/duration/retries/resource usage, file ownership/provenance, validation/runtime logs, package checksums, and repair history. User-facing diagnostics must be actionable without exposing secrets or unsafe system details.

## 18. Acceptance criteria

The design is ready for implementation when:
- Generation requires approval for the exact revision.
- Target version/environment are validated before production.
- Behavior Pack, Resource Pack, scripts, and world responsibilities are separated.
- Capability status distinguishes stable, experimental, preview, unsupported, and unknown.
- Manifests, UUIDs, versions, and dependencies are validated.
- Generated files trace to approved features and requirements.
- Script API usage is pinned and checked against the target profile.
- Asset references and licensing are validated.
- Packages are structurally checked before delivery.
- Import, load, runtime, multiplayer, and gameplay evidence are distinct.
- Unrun tests are never reported as passed.
- Existing worlds are not modified without backup and explicit approval.
- User-authored files are never silently overwritten.
- Deliverables include editable source, valid installable packages, provenance, checksums, and honest test reports.

## 19. Open design decisions

1. Initial supported Bedrock version window and release policy.
2. Whether Education Edition and dedicated-server targets are included in the first release.
3. First-release feature matrix for entities, blocks, items, UI, animations, and advanced behavior.
4. Initial stable Script API modules.
5. Whether preview/experimental APIs are excluded or allowed by explicit opt-in.
6. TypeScript toolchain and compilation policy.
7. Authoritative schema/capability registry update process.
8. Hosted, local, or hybrid environment for automated import/load tests.
9. Supported operating systems and optional game-installation detection.
10. Whether existing-world integration is first-release scope.
11. Pack UUID/version policy for forks, copies, and published derivatives.
12. Asset providers, formats, and licensing controls.
13. Whether package signing/integrity attestations are required.
14. Artifact storage, retention, and cleanup policy.
15. Whether distribution-platform publishing belongs here or to the separate publishing subsystem.

## 20. Related specifications

- docs/PROJECT_ARCHITECT_DECISION_ENGINE.md
- docs/MINECRAFT_VERSION_COMPATIBILITY_ENGINE_SPEC.md
- docs/JAVA_MOD_PRODUCTION_ENGINE_SPEC.md
- docs/AI_CONVERSATION_AND_REQUIREMENTS_ANALYSIS_SPEC.md
- docs/STUDIO_INTERFACE_AND_COMMUNITY_SPEC.md
- docs/DESIGN_FIRST_DELIVERY_WORKFLOW.md

## 21. Change control

This document is a draft design specification. It does not authorize implementation. Changes to scope, capability policy, or decisions must be reflected in the design baseline and reviewed before implementation begins.
