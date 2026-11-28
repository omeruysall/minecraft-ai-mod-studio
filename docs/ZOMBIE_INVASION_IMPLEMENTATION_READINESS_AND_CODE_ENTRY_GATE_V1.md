# Zombie Invasion — Implementation Readiness and Code Entry Gate v1

**Status:** Design traceability complete; implementation gate not yet open  
**Date:** 2026-11-28  
**Feature matrix:** `catalogs/feature-traceability-matrix.v1.json` v1.3.0  
**Required targets:** Java 26.3 + Fabric; Bedrock 26.60 + stable Script API 2.11.0 where needed

## 1. Purpose

This document establishes the conditions for moving from design into actual Java and Bedrock implementation. It prevents the completion of design documents from being mistaken for a playable mod.

The 232-feature catalog is now fully mapped for design traceability. Implementation must still proceed in approved, testable vertical slices. The full long-term scope is not a requirement to put all 232 features into the first playable build.

## 2. Current verified readiness

| Area | Current state |
|---|---|
| Feature catalog | 232/232 mapped |
| Feature-specific acceptance criteria | 495 defined |
| Feature-specific test cases | 490 defined |
| Proposed feature dependency edges | 486 |
| Static dependency graph | 232 nodes topologically sorted; no cycle detected |
| Java implementation coverage | 232 not assessed |
| Bedrock implementation coverage | 232 not assessed |
| Java/Bedrock parity | 232 not assessed |
| Implementation status | 232 not implemented verified |
| Runtime/build/test evidence | 0 records |

The graph validation is a static design check only. It is not a Java/Bedrock compatibility test, build, game launch or gameplay test.

## 3. Confirmed project decisions that can be treated as baseline

- Java Edition target: Minecraft 26.3 + Fabric.
- Bedrock target: Minecraft 26.60 + stable `@minecraft/server` 2.11.0 where scripting is required.
- Experimental Bedrock APIs are disabled.
- Both editions are mandatory delivery targets; their implementations and evidence remain independent.
- First playable is single-player.
- Selected game concept: Zombie Invasion.
- First map direction: compact, authored, abandoned and expandable town.
- Market, Hospital and Police Station are functional first-slice locations.
- Approved first-slice zombie roster: Walker, Runner and Brute.
- Approved first-slice combat: melee and firearms; weapon noise enabled; durability enabled; ammunition limited and finite.
- Backpack variety is a confirmed requirement.
- Vanilla Crafting Table remains the first crafting stage; specialist workstations are progression-gated.
- Long-term world topology: one continuous, regionally organized world with authored landmarks, deterministic procedural secondary content and incremental expansion.

Exact Fabric Loader/API, Loom, Gradle, mappings and Java runtime patch versions must be revalidated and pinned immediately before implementation. Bedrock pack format and stable API support must be verified against the actual target runtime.

## 4. Remaining code-entry blockers

These are the minimum decisions/evidence needed before a playable milestone can be frozen.

### 4.1 First-playable feature freeze

The 232 features are mapped, but not all are first-playable scope. A revisioned manifest must select the exact first-slice feature IDs and bind them to Java and Bedrock components.

Required scope groups to decide:
- Core player state and survival needs.
- World clock/day-night behavior.
- Inventory, loot and required backpack variants.
- Combat, weapon roster and Walker/Runner/Brute behavior.
- Functional Market, Hospital and Police Station content.
- Medical recovery and the injury subset included in the first slice.
- Basic crafting recipes and the specialist stations required for the first slice.
- Required NPC interactions, if any.
- Required assets, sounds, models and UI surfaces.

Long-term systems such as all biomes, complete ecosystem simulation, advanced prosthetics, all vehicles, all factories, full faction economy, multiplayer and large-scale procedural expansion must be explicitly staged rather than silently included.

### 4.2 Target toolchain and test environment

Before code generation:
- Verify official compatibility of Minecraft 26.3 with the selected Fabric Loader/API and build toolchain.
- Pin Java runtime, Gradle, Loom, mappings and dependency versions.
- Verify Bedrock 26.60 pack format and stable Script API 2.11.0 availability.
- Identify an actual Java test runtime and an actual Bedrock test device/runtime.
- Record OS/device constraints and a reproducible clean-install path.
- Define which tests can run automatically and which require human gameplay.

A build that cannot be imported/launched in the actual target runtime is not a playable deliverable.

### 4.3 Execution and delivery workflow

The first production workflow must specify:
- Where Java and Bedrock builds execute (local, isolated cloud worker or hybrid).
- How generated code is sandboxed.
- Where source, build logs and artifact hashes are stored.
- How the user reviews and approves the plan revision before generation.
- How both target bundles are installed and tested independently.
- How failures are repaired without overwriting approved source or user data.

### 4.4 Decisions that can remain deferred if the first slice avoids them

- Death, respawn, recovery and permadeath policy.
- Exact damage, health, speed, ammo, durability and spawn balance values.
- Carry-weight/encumbrance model and exact backpack capacities.
- Exact food, drink, thirst, spoilage and season rates.
- Full weapon attachment catalogue and all 3D asset variants.
- Boss identities and special zombie types beyond Walker/Runner/Brute.
- Multiplayer, PvP, dedicated server, cross-play and shared quest/trade behavior.
- Additional dimensions, helicopters, submarines, full procedural continents and complete regional economy.

A deferred decision must be isolated behind a disabled/unavailable feature flag or excluded from the first-slice manifest. It must not receive an invented default that changes gameplay.

## 5. Proposed first playable implementation scope

This is a recommendation for a coherent first playable milestone, not a new user approval. The final scope must be bound to a manifest revision.

### Core loop
1. Create/load the compact abandoned town world.
2. Spawn safely at the safehouse.
3. Explore residential streets and enter the Market, Hospital and Police Station.
4. Search finite, location-specific supplies.
5. Equip and use one of the required backpack variants.
6. Fight Walker, Runner and Brute using melee and firearms.
7. Consume finite ammunition; gunfire emits bounded noise that can attract nearby zombies.
8. Use basic food, drink and medical items.
9. Experience the day/night cycle and save/reload persistent state.
10. Complete a repeatable, measurable survival objective selected in the approved manifest.

### Explicitly staged beyond the first playable
- Full seasons/climate simulation and broad weather hazards.
- Complete water network, sanitation, power grid and automation.
- Full NPC settlement, factions, research and regional trade.
- Factory vehicle manufacturing and complete transport network.
- Advanced prosthetics and full injury catalogue.
- Large world expansion, all biomes and high-fidelity distant simulation.
- Multiplayer and hosted server features.

This staging does not remove those long-term requirements from the project catalog.

## 6. Implementation waves

| Wave | Engineering work | Exit gate |
|---|---|---|
| W0 | Revalidate and pin target toolchains; freeze first-slice manifest | Both target profiles and first-slice IDs approved |
| W1 | Shared logical IDs, manifest validation, dependency locks, config and persistence contracts | Schema, migration and DAG tests pass |
| W2 | Java Fabric and Bedrock pack project skeletons | Both minimal target artifacts build, import and load |
| W3 | Player state, world clock, item registry, inventory and basic save/load | State survives target-native save/reload |
| W4 | Walker/Runner/Brute AI, combat, ammo, noise and durability | Solo combat acceptance passes on both targets |
| W5 | Abandoned town map, three functional buildings, loot and backpacks | Fresh-world exploration/scavenging loop passes |
| W6 | Food, water/medical first slice, basic crafting and station gates | Survival and crafting resource conservation passes |
| W7 | Required UI/assets/audio, localization and accessibility fallbacks | All referenced assets and UI flows validate |
| W8 | NPC, faction, advanced infrastructure and transport expansions | Each system receives its own manifest revision and tests |
| W9 | Full world expansion, ecology, economy, campaign and multiplayer | Separate target-specific milestones and approvals |

W0–W7 are the proposed first playable path. W8–W9 are later expansion waves and must not be treated as first-release blockers unless selected by an approved scope revision.

## 7. Mandatory release gates

A first playable is not complete until both editions independently pass:
1. Manifest/schema and dependency validation.
2. Clean target build.
3. Package import/load.
4. Fresh world creation and spawn validation.
5. Functional Market, Hospital and Police Station interactions.
6. Required zombie roster and combat behavior.
7. Inventory/backpack and loot persistence.
8. Survival/crafting behaviors included in the frozen scope.
9. Save/reload and migration safety.
10. Performance and exploit/duplication checks for the first-slice scenario.
11. Clean-install verification with exact instructions.
12. Human gameplay acceptance with logs and artifact hashes.

A skipped or unavailable test is recorded as `NOT_RUN`, not passed. A Java pass cannot close a Bedrock gate, or vice versa.

## 8. Approval and change control

- The project manifest revision and digest define the approved scope.
- No production starts until the exact first-slice plan is approved.
- Any change to target versions, loader/API, feature IDs, dependencies, deliverables or acceptance criteria creates a new revision and impact report.
- Generated code, downloaded dependencies and build tasks execute in isolated workers.
- No destructive edit may overwrite approved source or user data without backup and explicit confirmation.

## 9. Code entry decision

**Current status: NOT READY TO START FULL PLAYABLE IMPLEMENTATION.**

Design traceability is complete. The remaining blockers are the first-playable feature freeze, exact toolchain revalidation, actual Java and Bedrock test environments, execution/build workflow and a small set of gameplay policies if they are included in the first slice.

A minimal target project skeleton and schema/toolchain probes may be prepared after those prerequisites are approved, but they must not be presented as a playable mod.

## 10. Related documents

- `catalogs/feature-traceability-matrix.v1.json`
- `docs/ZOMBIE_INVASION_MASTER_FEATURE_DEPENDENCY_AND_IMPLEMENTATION_MAP_V1.md`
- `docs/ZOMBIE_INVASION_FEATURE_TRACEABILITY_GAP_ASSESSMENT_V1.md`
- `docs/FIRST_PLAYABLE_VERTICAL_SLICE_SPEC_V1.md`
- `docs/FIRST_PLAYABLE_DECISION_REGISTER_V1.md`
- `docs/PROJECT_MANIFEST_V2_DESIGN.md`
- `schemas/project-manifest.v2.schema.json`
- `docs/MINECRAFT_VERSION_COMPATIBILITY_ENGINE_SPEC.md`
