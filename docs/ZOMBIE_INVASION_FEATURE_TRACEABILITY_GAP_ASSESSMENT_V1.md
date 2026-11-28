# Zombie Invasion — Feature Traceability Gap Assessment V1

**Date:** 2026-11-28  
**Source:** `catalogs/feature-traceability-matrix.v1.json` (matrix v1.1.0), sourced from `catalogs/mod-system-inventory.v0.2.json`.  
**Status:** Baseline assessment only; no feature approvals or implementation claims.

## 1. Executive assessment

The current matrix contains **232 feature records across 18 inventory sections**. All 232 are still `current_status: planned`, `design_status: needs_traceability_review`, and `implementation_status: not_implemented_verified`.

For both target editions, all 232 records currently show `not_assessed`; parity is also `not_assessed` for all 232. The matrix contains **zero dependency edges**, **zero feature-level acceptance criteria marked defined**, and **zero feature-level test cases marked defined**. The existing owner and primary-specification assignments are proposed traceability assignments, not final approvals.

This means the master feature/dependency map is a family-level architecture view. It does not yet constitute feature-by-feature traceability closure. This assessment records that gap explicitly so it cannot be mistaken for completed design.

## 2. Coverage snapshot

| Measure | Current count |
|---|---:|
| Total feature records | 232 |
| Inventory sections represented | 18 |
| Features still planned | 232 |
| Features needing traceability review | 232 |
| Java target mappings assessed | 0 |
| Bedrock target mappings assessed | 0 |
| Parity results assessed | 0 |
| Explicit dependency edges | 0 |
| Acceptance criteria defined | 0 |
| Test cases defined | 0 |
| Evidence records | 0 |

## 3. Feature inventory by section

### 2 — Project foundation and compatibility (12 features)
- **IDs:** BASE-001, BASE-002, BASE-003, BASE-004, BASE-005, BASE-006, BASE-007, BASE-008, BASE-009, BASE-010, BASE-011, BASE-012
- **Proposed owner:** Minecraft Compatibility Engine
- **Primary specification:** `docs/MINECRAFT_VERSION_COMPATIBILITY_ENGINE_SPEC.md`

### 3 — Player, character, and progression (14 features)
- **IDs:** PLY-001, PLY-002, PLY-003, PLY-004, PLY-005, PLY-006, PLY-007, PLY-008, PLY-009, PLY-010, PLY-011, PLY-012, PLY-013, PLY-014
- **Proposed owner:** Professions & Player Progression Engine
- **Primary specification:** `docs/PROFESSIONS_SKILLS_PLAYER_PROGRESSION_ENGINE_SPEC.md`

### 4 — Items, materials, blocks, and equipment (16 features)
- **IDs:** ITEM-001, ITEM-002, ITEM-003, ITEM-004, ITEM-005, ITEM-006, ITEM-007, ITEM-008, ITEM-009, ITEM-010, ITEM-011, ITEM-012, ITEM-013, ITEM-014, ITEM-015, ITEM-016
- **Proposed owner:** Items, Equipment & Loot Engine
- **Primary specification:** `docs/ITEMS_EQUIPMENT_LOOT_ENGINE_SPEC.md`

### 5 — Crafting, processing, and resource loops (10 features)
- **IDs:** CRAFT-001, CRAFT-002, CRAFT-003, CRAFT-004, CRAFT-005, CRAFT-006, CRAFT-007, CRAFT-008, CRAFT-009, CRAFT-010
- **Proposed owner:** Crafting & Resource Production Engine
- **Primary specification:** `docs/CRAFTING_RESOURCE_PRODUCTION_ENGINE_SPEC.md`

### 6 — Entities, mobs, NPCs, and AI (18 features)
- **IDs:** ENT-001, ENT-002, ENT-003, ENT-004, ENT-005, ENT-006, ENT-007, ENT-008, ENT-009, ENT-010, ENT-011, ENT-012, ENT-013, ENT-014, ENT-015, ENT-016, ENT-017, ENT-018
- **Proposed owner:** NPC & Character Production Engine
- **Primary specification:** `docs/NPC_CHARACTER_PRODUCTION_ENGINE_SPEC.md`

### 7 — Combat, weapons, and damage (12 features)
- **IDs:** COM-001, COM-002, COM-003, COM-004, COM-005, COM-006, COM-007, COM-008, COM-009, COM-010, COM-011, COM-012
- **Proposed owner:** Combat & AI Behavior Engine
- **Primary specification:** `docs/COMBAT_AI_BEHAVIOR_ENGINE_SPEC.md`

### 8 — Vehicles, mounts, and machinery (14 features)
- **IDs:** VEH-001, VEH-002, VEH-003, VEH-004, VEH-005, VEH-006, VEH-007, VEH-008, VEH-009, VEH-010, VEH-011, VEH-012, VEH-013, VEH-014
- **Proposed owner:** Transportation, Logistics & Infrastructure Engine
- **Primary specification:** `docs/TRANSPORTATION_LOGISTICS_INFRASTRUCTURE_ENGINE_SPEC.md`

### 9 — World, biomes, terrain, and environment (17 features)
- **IDs:** WORLD-001, WORLD-002, WORLD-003, WORLD-004, WORLD-005, WORLD-006, WORLD-007, WORLD-008, WORLD-009, WORLD-010, WORLD-011, WORLD-012, WORLD-013, WORLD-014, WORLD-015, WORLD-016, WORLD-017
- **Proposed owner:** Map / World Production Engine
- **Primary specification:** `docs/MAP_WORLD_PRODUCTION_ENGINE_SPEC.md`

### 10 — Structures, buildings, and points of interest (10 features)
- **IDs:** STRUCT-001, STRUCT-002, STRUCT-003, STRUCT-004, STRUCT-005, STRUCT-006, STRUCT-007, STRUCT-008, STRUCT-009, STRUCT-010
- **Proposed owner:** Structure & Building Engine
- **Primary specification:** `docs/MAP_WORLD_PRODUCTION_ENGINE_SPEC.md`

### 11 — Quests, narrative, and events (12 features)
- **IDs:** QUEST-001, QUEST-002, QUEST-003, QUEST-004, QUEST-005, QUEST-006, QUEST-007, QUEST-008, QUEST-009, QUEST-010, QUEST-011, QUEST-012
- **Proposed owner:** Quest & Story Production Engine
- **Primary specification:** `docs/QUEST_STORY_PRODUCTION_ENGINE_SPEC.md`

### 12 — Economy, trade, and ownership (12 features)
- **IDs:** ECON-001, ECON-002, ECON-003, ECON-004, ECON-005, ECON-006, ECON-007, ECON-008, ECON-009, ECON-010, ECON-011, ECON-012
- **Proposed owner:** Economy & Trade Simulation Engine
- **Primary specification:** `docs/ECONOMY_TRADE_SIMULATION_ENGINE_SPEC.md`

### 13 — Factions, teams, and social systems (10 features)
- **IDs:** SOC-001, SOC-002, SOC-003, SOC-004, SOC-005, SOC-006, SOC-007, SOC-008, SOC-009, SOC-010
- **Proposed owner:** Collaboration & Social Systems
- **Primary specification:** `docs/SECURITY_PERMISSIONS_MODERATION_ENGINE_SPEC.md`

### 14 — Multiplayer and server operations (12 features)
- **IDs:** MP-001, MP-002, MP-003, MP-004, MP-005, MP-006, MP-007, MP-008, MP-009, MP-010, MP-011, MP-012
- **Proposed owner:** Multiplayer & Server Runtime
- **Primary specification:** `docs/SECURITY_PERMISSIONS_MODERATION_ENGINE_SPEC.md`

### 15 — Interface, controls, and accessibility (12 features)
- **IDs:** UI-001, UI-002, UI-003, UI-004, UI-005, UI-006, UI-007, UI-008, UI-009, UI-010, UI-011, UI-012
- **Proposed owner:** Studio Interface & Client Workspace
- **Primary specification:** `docs/STUDIO_INTERFACE_AND_COMMUNITY_SPEC.md`

### 16 — Visual, audio, and animation assets (12 features)
- **IDs:** ASSET-001, ASSET-002, ASSET-003, ASSET-004, ASSET-005, ASSET-006, ASSET-007, ASSET-008, ASSET-009, ASSET-010, ASSET-011, ASSET-012
- **Proposed owner:** AI Asset Generation Pipeline
- **Primary specification:** `docs/AI_ASSET_GENERATION_PIPELINE_SPEC.md`

### 17 — Commands, admin, and configuration (9 features)
- **IDs:** ADMIN-001, ADMIN-002, ADMIN-003, ADMIN-004, ADMIN-005, ADMIN-006, ADMIN-007, ADMIN-008, ADMIN-009
- **Proposed owner:** Security & Permissions Engine
- **Primary specification:** `docs/SECURITY_PERMISSIONS_MODERATION_ENGINE_SPEC.md`

### 18 — Technical quality, security, and testing (18 features)
- **IDs:** QA-001, QA-002, QA-003, QA-004, QA-005, QA-006, QA-007, QA-008, QA-009, QA-010, QA-011, QA-012, QA-013, QA-014, QA-015, QA-016, QA-017, QA-018
- **Proposed owner:** Validation & Test Evidence System
- **Primary specification:** `docs/MASTER_INTEGRATION_AUDIT_V1.md`

### 19 — Build, packaging, and delivery (12 features)
- **IDs:** SHIP-001, SHIP-002, SHIP-003, SHIP-004, SHIP-005, SHIP-006, SHIP-007, SHIP-008, SHIP-009, SHIP-010, SHIP-011, SHIP-012
- **Proposed owner:** Publishing & Versioning Engine
- **Primary specification:** `docs/PUBLISHING_VERSIONING_UPDATE_ENGINE_SPEC.md`

## 4. Why the gaps matter

- **No dependency edges:** generation order cannot safely be inferred from the current matrix alone. The L0–L12 layers in the master map are logical architecture layers, not 232 completed feature-level dependency edges.
- **No acceptance criteria:** a feature cannot be objectively marked complete or verified.
- **No test cases:** there is no per-feature reproducible pass/fail procedure.
- **No target mapping:** a shared feature name does not prove that Java Fabric and Bedrock stable Script API can implement the same behavior.
- **Proposed owners/specs:** these are useful starting points, but conflicts and exact feature-to-spec coverage still require review.
- **Applicability not finalized:** general catalog entries may be irrelevant, optional or deferred for this zombie-invasion project.

## 5. Required closure workflow for each feature

For every feature ID, complete the following record before approval:

1. **Project applicability:** required / optional / excluded / unresolved, with reason.
2. **Requirement provenance:** exact user request or decision-register entry; otherwise mark it as a proposal.
3. **Detailed behavior:** link the precise section of the subsystem specification.
4. **Canonical owner:** one authoritative owner; list consumers separately.
5. **Inputs and outputs:** IDs, data contracts, commands/events, persistence and failure behavior.
6. **Dependencies:** explicit feature IDs and edge type (hard prerequisite, runtime integration, optional enhancement, or target-specific dependency).
7. **Cycle check:** prove that bootstrap paths exist and no dependency cycle creates a soft lock.
8. **Java mapping:** component type, supported API/capability, acceptance criteria and tests.
9. **Bedrock mapping:** component type, stable API capability, acceptance criteria and tests; experimental APIs remain disabled.
10. **Parity classification:** equivalent / adapted / limited / unsupported / not applicable, supported by evidence.
11. **Approval:** user approval bound to a manifest revision where required.
12. **Implementation evidence:** build/test/runtime evidence tied to component revision; otherwise leave implementation status unverified.

## 6. Recommended review order

Review in dependency order rather than catalog order:

- **Group A — foundation:** BASE, QA, SHIP and the manifest/persistence/toolchain prerequisites.
- **Group B — world and identity:** WORLD, STRUCT, ITEM, PLY and target world interactions.
- **Group C — core gameplay:** COM, ENT, CRAFT and the survival/inventory/loot loops.
- **Group D — environment and logistics:** farming/ecology/water/power/transport feature IDs in the catalog's detailed sections.
- **Group E — social and progression:** SOC, ECON, QUEST and NPC/faction/settlement interactions.
- **Group F — presentation and advanced delivery:** UI, ASSET, ADMIN, MP and advanced publishing/packaging, according to project applicability.

The group order is a review proposal. It does not make multiplayer, admin, Studio UI or every general catalog capability part of the mod's first playable.

## 7. Scope and approval safeguards

- Do not bulk-change all 232 entries to `designed`, `approved` or `implemented`.
- Do not infer that a long-form system document closes every related catalog item.
- Do not assign a feature to the first playable merely because the user approved its long-term concept.
- Keep explicit user-approved requirements separate from proposed implementation details and open balance decisions.
- Update the matrix only when each feature has supporting specification and evidence.
- Preserve separate Java and Bedrock status fields. One target's success cannot close the other target's status.
- Record unsupported capabilities honestly and request an approved equivalent where necessary.

## 8. Implementation boundary

This is a static assessment of the current planning matrix. It does not modify the 232 feature statuses, implement features, validate Java/Bedrock compatibility, or claim tests. The next traceability work must fill feature-level requirements, dependencies, acceptance criteria and target mappings in controlled revisions.
## 9. Controlled traceability update

The matrix has since been updated in a controlled revision to `catalogs/feature-traceability-matrix.v1.json` v1.2.0. The earlier section 2–4 figures above describe the v1.1.0 snapshot and remain historical, not the current matrix state.

Current state:
- 232 total feature records remain in the catalog.
- BASE-001 through BASE-012 now have detailed feature-level mappings and `design_status: mapped`.
- 220 features remain `needs_traceability_review`.
- The 12 mapped features link to 12 requirement IDs, 55 acceptance criteria and 50 unique test case IDs in `docs/ZOMBIE_INVASION_FOUNDATION_COMPATIBILITY_AND_TRACEABILITY_SPEC_V1.md`.
- 15 feature-to-feature dependency edges are recorded with `status: proposed`; they are not yet approved dependency decisions.
- The edge object contract is defined in `schemas/feature-dependency-edge.v1.schema.json`.
- Java, Bedrock and parity remain `not_assessed` for all 232 features.
- All 232 implementation statuses remain `not_implemented_verified`; evidence record count remains zero.

The matrix update records design traceability only. It does not claim toolchain compatibility, a successful build, runtime load, gameplay behavior or executed tests. The 16 dependency relations described in the human-readable foundation specification include cross-cutting engine/test/pipeline prerequisites; 15 of these are feature-to-feature edges and therefore appear in the machine-readable feature graph.
