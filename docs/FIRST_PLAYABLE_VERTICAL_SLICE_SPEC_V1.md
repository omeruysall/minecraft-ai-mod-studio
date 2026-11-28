# First Playable Vertical Slice Specification v1.0

**Status:** Proposed scope definition — pending detailed feature selection and baseline approval  
**User-selected platform scope:** Java Edition + Bedrock Edition  
**User-selected content scope:** Mod/world bundle  
**Implementation status:** Not implemented

## 1. Purpose

Define the first end-to-end playable milestone for Minecraft AI Mod Studio. The milestone validates the complete product workflow across both Minecraft editions while preserving separate platform-specific generation and runtime behavior.

This specification narrows the first release without shrinking the long-term 232-feature product vision.

## 2. User decisions captured

The user selected:
- Both Java Edition and Bedrock Edition.
- A mod/world bundle rather than a standalone mod-only demonstration.

The bundle includes the relevant modification/add-on, playable map/world, and resource pack. Datapacks are included in the Java track where required and supported. Bedrock equivalents are implemented as behavior packs and, where required, Script API modules; Java datapack format is not copied into Bedrock.

## 3. Milestone structure

The milestone consists of two target tracks sharing one project identity, requirements model and approval workflow:

- Track A: Java Edition.
- Track B: Bedrock Edition.

Each track has its own compatibility profile, dependency graph, generation jobs, build/import pipeline, runtime tests, evidence and deliverable package. The milestone is not complete until both tracks independently pass their required playable acceptance gates, unless the user explicitly revises the milestone to staged delivery.

## 4. Shared workflow

1. User describes the desired mod/world experience in chat or voice.
2. Conversation and Requirement Analyzer identify gameplay intent and ambiguities.
3. Project Architect creates one shared project concept and feature requirement set.
4. Compatibility Engine evaluates Java and Bedrock independently.
5. Component Planner creates target-specific components and dependencies.
6. User reviews the complete cross-platform plan and approves the exact revision.
7. Production Orchestrator dispatches separate Java and Bedrock jobs.
8. Target-specific engines generate artifacts.
9. Integration Engine validates references and component contracts within each target.
10. Build/import/load/runtime/gameplay tests run in the appropriate target environment.
11. Repair workflow addresses bounded failures without silently changing approved scope.
12. Delivery service provides separate Java and Bedrock bundles plus a combined project export.

## 5. Java Edition track

Expected artifact classes:
- Java mod source and distributable JAR.
- Playable Java world/map.
- Datapack when the selected gameplay feature requires it.
- Resource pack when the selected gameplay feature requires it.
- Dependency metadata and installation instructions.
- Target profile recording exact Minecraft version, loader, runtime requirements and dependency pins.

The user selected Minecraft Java Edition 26.3 with Fabric. Current Fabric documentation candidates and remaining build-pin work are recorded in `docs/ZOMBIE_INVASION_TARGET_TOOLCHAIN_COMPATIBILITY_RESEARCH_2026-11.md`. Fabric, Forge and NeoForge remain non-interchangeable; the project must use the selected Fabric target and must not silently switch loaders.

Validation gates:
- Source/schema/static validation.
- Dependency resolution.
- Reproducible build.
- Mod loader startup/load.
- World import/load.
- Datapack/resource pack load.
- Cross-component integration.
- Gameplay acceptance in the selected Minecraft runtime.
- Multiplayer test only if multiplayer is in the approved feature scope.

## 6. Bedrock Edition track

Expected artifact classes:
- Behavior Pack / add-on source and package.
- Bedrock world/map.
- Resource Pack and package.
- Script API module only when necessary and supported by the selected target.
- Manifest UUID/dependency metadata and installation instructions.

The user selected Bedrock 26.60, stable `@minecraft/server` 2.11.0 where scripting is required, and disabled experimental APIs. Pack format, peer dependencies and actual import/load behavior still require verification.

Validation gates:
- Manifest/schema validation.
- UUID and dependency validation.
- Pack import/activation.
- World import/load.
- Behavior/resource pack load.
- Script API validation where applicable.
- Runtime behavior and gameplay acceptance on the selected Bedrock target.
- Multiplayer test only if multiplayer is in the approved feature scope.

## 7. Cross-platform feature parity

The same user-visible gameplay intent may require different technical implementations. Each selected feature must be classified independently per target:

- SUPPORTED_NATIVE
- SUPPORTED_ADAPTED
- SUPPORTED_WITH_LIMITATIONS
- NOT_SUPPORTED
- NOT_VERIFIED
- NOT_IN_SCOPE

A Java implementation does not establish Bedrock support and vice versa. The project summary must show target-specific results and explain differences.

## 8. Shared versus target-specific data

Shared project data:
- Project identity and revision.
- User intent and requirement provenance.
- Feature intent and acceptance criteria.
- Shared narrative/world design decisions.
- Asset provenance and reusable source assets where licensing permits.
- Approval record and global change history.

Target-specific data:
- Edition/version/runtime profile.
- Loader/API and format declarations.
- Component implementation graph.
- Dependency pins.
- Build/import jobs.
- Runtime-specific assets and generated source.
- Test environment and evidence.
- Deliverable artifacts.

Shared data must not collapse distinct target runtime requirements into one generic flag.

## 9. World/map scope

The map/world must be a playable part of the project, not a decorative screenshot or empty placeholder. The initial world scope should be deliberately bounded and selected with the gameplay feature set.

The world specification must include:
- World purpose and gameplay loop.
- Spawn and onboarding.
- Required regions/structures.
- Player progression or objective path where applicable.
- Required blocks/entities/items and their ownership.
- World boundaries and performance constraints.
- Integration references to mod/add-on behavior.
- Save/load expectations.
- Test steps that prove the intended gameplay loop.

Procedural generation is optional for the first slice unless it is essential to the chosen user experience. The long-term hybrid prepared/procedural world strategy remains unchanged.

## 10. Mod/add-on scope

The first modification must implement a small, measurable gameplay feature set. It must not be a broad showcase of unrelated systems.

Each feature requires:
- Stable feature ID.
- Player-visible behavior.
- Trigger/conditions and expected outcome.
- Java implementation owner and Bedrock implementation owner.
- Dependencies and conflicts.
- Acceptance criteria.
- Target-specific tests.
- Known parity differences.

The exact gameplay feature set remains a user decision and must be designed before code generation.

## 11. Resource and data content

Resource packs should be generated only for required visual/audio/UI assets. Datapacks are Java-target components. Bedrock behavior packs provide relevant Bedrock runtime behavior. Resource formats and references are validated independently for each target.

Generated assets must include source/provenance, license/usage status, dimensions/format metadata, stable asset IDs and checksums where applicable.

## 12. Delivery format

Deliverables:
- Java target bundle with source, JAR, world, datapack/resource pack as applicable, dependency pins and install instructions.
- Bedrock target bundle with source, add-on/behavior/resource packs, world and install instructions.
- Combined project export containing manifest, shared requirements, target profiles, both target bundles, checksums, test evidence and known limitations.

A target bundle may not be marked playable if its target-specific load/runtime/gameplay gates were not run. If a test environment is unavailable, the result is NOT_RUN and the milestone is not declared fully playable.

## 13. Non-goals for the first slice

Unless explicitly approved later:
- All 232 catalog features at once.
- Every Java loader and every historical/current Minecraft version.
- Full parity for every feature across Java and Bedrock.
- Marketplace monetization and complex social/community systems.
- Full server hosting/deployment automation.
- Large-scale procedural continents or unlimited world sizes.
- Advanced simulation systems not needed by the selected gameplay loop.
- Automatic installation to arbitrary user/server paths.

## 14. Mandatory decisions before implementation

1. **Confirmed:** Java Edition 26.3.
2. **Confirmed:** Fabric loader family; exact Loader/Loom/Gradle/API pins require compatibility resolution and build verification.
3. **Confirmed:** Bedrock Edition 26.60.
4. **Confirmed:** stable `@minecraft/server` 2.11.0 where required; experimental APIs disabled.
5. Small shared gameplay feature set for both editions.
6. Whether Java and Bedrock tracks are built sequentially or in parallel.
7. Test environments and device/OS availability for both editions.
8. Local/cloud/hybrid execution model for first milestone.
9. Minimum asset scope and licensing policy.
10. Definition of a successful human gameplay acceptance test.

## 15. Acceptance criteria for the milestone

- One shared project manifest represents both target profiles without conflating them.
- User approval is bound to the exact plan and target-specific component scope.
- Java and Bedrock generation run through independent adapters.
- Every required component has a target-specific owner and acceptance criteria.
- Both target bundles contain editable source and the correct runnable/importable artifacts.
- Java build/load/runtime tests are distinct from Bedrock import/load/runtime tests.
- The world/map is playable and exercises the approved gameplay loop.
- Cross-component references are valid within each target.
- Unsupported or unverified parity is disclosed.
- No required test is reported as passed if it was not run.
- Both target tracks pass their agreed gameplay gates before the milestone is called complete.

## 16. Implementation boundary

This document defines a proposed first playable milestone. It does not mean that Java/Bedrock generation, world creation, pack assembly, runtime testing or delivery functionality currently exists. Implementation remains blocked by the master design baseline approval and the unresolved decisions listed above.


## 17. User-approved target profiles (2026-11-28)

The user approved the following first-slice compatibility targets:
- Java Edition 26.3 with Fabric.
- Bedrock Edition 26.60 with stable `@minecraft/server` 2.11.0 when scripting is required.
- Experimental Bedrock APIs are disabled.

These target selections are confirmed. Exact build tool/runtime patch versions must be revalidated and pinned before implementation. The target-specific acceptance gates in this specification remain independent and mandatory.


## 18. User-selected gameplay direction — Zombie Invasion (2026-11-28)

The user selected Zombie Invasion as the shared gameplay concept. The detailed authoritative gameplay specification is `docs/ZOMBIE_INVASION_GAMEPLAY_DESIGN_V1.md`. The user later approved the first-slice zombie roster as Walker, Runner and Brute, and approved melee plus firearms, weapon noise attraction, durability and finite ammunition. A one-basic-zombie scope and a three-phase/three-night extraction scenario are superseded proposals, not the current approved roster or an approved campaign. Exact first-slice feature IDs, victory/defeat policy, death/restart behavior and balance remain to be frozen in the manifest.


## 19. Confirmed first-slice player scope — single-player

The user accepted a single-player first playable release. All first-slice gameplay acceptance tests are performed with one player in each target edition. Cooperative multiplayer, dedicated-server operation, player synchronization, shared inventories and revive mechanics are deferred and are not release blockers for this milestone. Future multiplayer remains a possible later expansion and must receive its own design and test gate.


## 20. Confirmed first-map direction — abandoned expandable town

The user approved an abandoned, expandable town. The current first-slice landmark baseline requires a safehouse, residential section, functional Market, functional Hospital and functional Police Station, plus two validated attack lanes. Gas station, military checkpoint and underground shelter remain expansion landmarks unless separately promoted. Java and Bedrock maps must pass independent load, navigation, spawn-safety, gameplay and reset checks.

See `docs/ZOMBIE_INVASION_MAP_DESIGN_V1.md` for the detailed map design.


## 21. Confirmed first-slice functional buildings

The user selected all three proposed buildings: **Market, Hospital and Police Station**. Each is a required functional location in both Java and Bedrock first-slice maps.

Required acceptance:
- Market: player can enter, search identified supply points, collect food/general supplies and observe empty/looted state.
- Hospital: player can enter, search medical supply points and use at least one medical/recovery item or interaction supported by the first-slice survival rules.
- Police Station: player can enter, search tactical supply points and collect combat/defence supplies within the approved combat scope.
- Each location has a navigable route from the safehouse and a resettable, testable loot state.
- Equivalent gameplay roles and intended rewards are present in both editions.
- No custom firearm system is implied or approved by the Police Station decision.

The first-slice map now includes a functional safehouse, residential section, market, hospital and police station, plus two validated attack lanes. The gas station, military checkpoint and underground shelter remain planned expansion landmarks unless separately promoted.


## 22. Consolidated user-approved Zombie Invasion first-slice requirements (2026-11-28)

The following decisions were explicitly confirmed by the user and must be reflected in the first-slice manifest and both target plans:

- **Targets:** Java Edition 26.3 + Fabric; Bedrock Edition 26.60 + stable `@minecraft/server` 2.11.0 where scripting is required; experimental Bedrock APIs disabled.
- **Player count:** single-player is sufficient for the first playable slice.
- **Game direction:** Zombie Invasion survival experience.
- **Map:** compact, authored, abandoned and expandable town.
- **Functional locations:** Market, Hospital and Police Station in both target worlds.
- **Zombie roster:** Walker, Runner and Brute. Other special zombie variants remain deferred.
- **Combat:** melee and firearms; gunfire noise attracts nearby zombies within bounded encounter rules; weapon durability is enabled; ammunition is limited and finite.
- **Inventory:** multiple backpack varieties are a required feature, not a cosmetic-only option.
- **Crafting progression:** the vanilla Crafting Table remains the first stage; specialist stations are introduced later through progression.

These are user-approved design requirements, not implementation evidence. Exact weapon/item/loot values, first-slice recipes and station roster, injury subset, death/restart behavior, survival decay rates and the exact set of additional first-slice feature IDs remain to be frozen in a revisioned manifest. Long-term scope such as full seasons, the complete water/power grids, advanced prosthetics, all vehicles, full NPC/faction economy and world-scale procedural expansion is not automatically part of the first playable.

## 23. Feature traceability and remaining implementation gate

The 232-feature catalog is fully mapped in `catalogs/feature-traceability-matrix.v1.json` v1.3.0: 495 acceptance criteria, 490 test case IDs and 486 proposed dependency edges. This closes feature-level design traceability but does not close target feasibility or implementation.

Before production, the project must still freeze exact first-slice feature IDs, revalidate and pin the Java/Bedrock toolchains, identify real test environments for both editions, define build execution/sandboxing and record a human gameplay acceptance procedure. See `docs/ZOMBIE_INVASION_IMPLEMENTATION_READINESS_AND_CODE_ENTRY_GATE_V1.md`.

Java, Bedrock and parity statuses remain not assessed for all 232 features; all implementation statuses remain not implemented verified. No build, import, runtime or gameplay test is claimed.
