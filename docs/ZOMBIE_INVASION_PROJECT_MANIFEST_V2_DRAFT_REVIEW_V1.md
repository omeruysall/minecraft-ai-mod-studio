# Zombie Invasion — Project Manifest v2 Draft Review v1

**Status:** Draft, not approved for production  
**Date:** 2026-11-28  
**Manifest:** `schemas/zombie-invasion.project-manifest.v2.draft.json`

## 1. Purpose

The manifest is the machine-readable source of truth for the Zombie Invasion project plan. It keeps shared gameplay intent separate from Java and Bedrock implementation components, and binds requirements, dependencies, validation plans and deliverables to a revision.

This file is a draft planning artifact. It is not a generated project, source-code tree, build output or playable mod.

## 2. Manifest contents

| Area | Current draft |
|---|---:|
| Manifest schema | 2.0.0 |
| Manifest revision | 1 |
| Project requirements | 18 |
| Target profiles | 2 |
| Planned components | 9 |
| Component dependency edges | 8 |
| Validation plans | 14 (7 per target) |
| Deliverable definitions | 8 |
| Approval records | 0 |
| Test evidence records | 0 |
| User approval | Not approved |

The two target profiles remain distinct:
- Java Edition 26.3 + Fabric.
- Bedrock Edition 26.60 + stable `@minecraft/server` 2.11.0 where required; experimental APIs disabled.

## 3. First-slice feature scope proposal

The manifest contains 84 candidate feature IDs drawn from the 232-feature catalog. They are a proposed first-slice scope, not a user-approved feature freeze.

The candidate set covers:
- Target identity, version, project namespace, config and save compatibility.
- Player state and survival primitives.
- Item, food/medical, weapon, backpack and durability systems.
- Crafting, loot and specialist workstation hooks.
- Walker/Runner/Brute entity framework, combat and AI foundations.
- Day/night and prepared town/map/structure integration.
- HUD, menus, inventory, crafting UI, accessibility and localization.
- Required art/audio assets and target pack validation.
- Schema, dependency, build, import, gameplay, persistence, performance and delivery gates.

The proposal deliberately excludes broad long-term families by default, including vehicles, multiplayer, economy, faction/social administration, quests and full procedural world expansion. Those remain in the overall 232-feature project catalog and are not removed from the long-term vision.

The user must approve or revise the exact candidate feature IDs before the manifest can move to an approved production revision.

## 4. Requirements provenance

The manifest records project-level user-confirmed requirements separately from first-slice inclusion. For example, food/drink/thirst and day/night are confirmed project requirements, but their exact first-slice depth, rates and content are not frozen. This distinction prevents a confirmed long-term feature from being silently treated as a fully specified first-release feature.

All components remain `proposed`. No component is marked approved, generating, built, tested or delivered.

## 5. Toolchain research captured

The manifest and supporting research document record:
- Java 26.3: current Fabric documentation candidates Loader 0.20.1, Loom 1.19-SNAPSHOT, Fabric API 0.166.0+26.3 and Java 25+. Official pack formats: data pack 121.0 and resource pack 97.1. Gradle wrapper selection remains unresolved until the selected Loom build is resolved.
- Bedrock 26.60: official changelog confirms stable `@minecraft/server` 2.11.0. Pack format and actual import/load remain unverified.

See `docs/ZOMBIE_INVASION_TARGET_TOOLCHAIN_COMPATIBILITY_RESEARCH_2026-11.md`.

## 6. Structural validation performed

The draft was checked against the repository's Project Manifest v2 schema structure for:
- Required top-level and nested fields.
- Declared types, enums, constants, string patterns and date-time/UUID formats.
- Target, requirement, component and dependency references.
- Candidate feature IDs against the 232-feature catalog.
- Component dependency graph endpoints and cycle detection.
- Revision digest format and recomputation.

Result: no structural errors were found; all 84 candidate feature IDs exist in the catalog; all 9 component nodes were topologically ordered with no cycle.

The revision digest is SHA-256 over the manifest serialized with `revision.digest` set to an empty string, using deterministic insertion-order JSON serialization in the manifest generation workflow. Any content change requires recomputing the digest and creating a new revision according to the project change-control policy.

This structural check is not a full external JSON Schema validator run, target compatibility test, build, package import or game runtime test.

## 7. Current blockers

1. User approval of the exact first-slice feature-ID list and any changes to the 84 candidates.
2. Exact first-slice values: weapon roster/balance, backpack variants/capacities, injury subset, survival rates, crafting recipes/stations and loot tables.
3. Java build pin: choose the Loom release/snapshot strategy and compatible Gradle wrapper; verify Fabric API and JDK in a clean build.
4. Bedrock pack format, module declarations, peer dependencies and 26.60 import/load validation.
5. Actual Java and Bedrock test devices/runtimes and clean-install process.
6. Local/cloud/hybrid build execution, isolation/sandboxing and artifact storage.

## 8. Approval transition

The manifest may move from draft planning to `awaiting_approval` only after the exact candidate scope and unresolved first-slice choices are presented clearly. Production may start only after approval is recorded against the exact manifest revision digest and scope digest.

A change after approval creates a new manifest revision and invalidates approval for the changed scope. Test evidence is appended only after tests are actually executed.

## 9. Related records

- `schemas/project-manifest.v2.schema.json`
- `schemas/zombie-invasion.project-manifest.v2.draft.json`
- `catalogs/feature-traceability-matrix.v1.json`
- `docs/ZOMBIE_INVASION_IMPLEMENTATION_READINESS_AND_CODE_ENTRY_GATE_V1.md`
- `docs/ZOMBIE_INVASION_TARGET_TOOLCHAIN_COMPATIBILITY_RESEARCH_2026-11.md`
- `docs/FIRST_PLAYABLE_VERTICAL_SLICE_SPEC_V1.md`
