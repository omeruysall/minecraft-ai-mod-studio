# Zombie Invasion — Proposed First-Slice Feature Scope Review v1

**Status:** Proposed candidate list; not approved for production  
**Date:** 2026-11-28  
**Manifest:** `schemas/zombie-invasion.project-manifest.v2.draft.json`  
**Catalog:** `catalogs/feature-traceability-matrix.v1.json` v1.3.0

## 1. Decision boundary

This review expands the 84 candidate feature IDs in the manifest into a readable review list. Every item below is a proposed candidate for the first playable slice. The list is not an approval and does not override the 232-feature long-term catalog. Features not selected for the first playable remain in the project backlog.

Java and Bedrock implementation statuses for all features remain `not_assessed`; no candidate has been implemented or tested. The final first-slice scope must be approved against a new manifest revision and digest before generation.

## 2. Candidate inventory by feature family

**Candidate count: 84.**

### BASE (8)

| Feature ID | Feature | Current design owner | First-slice interpretation |
|---|---|---|---|
| `BASE-001` | Edition selection: Java / Bedrock | `docs/MINECRAFT_VERSION_COMPATIBILITY_ENGINE_SPEC.md` | Project/target foundation and compatibility controls. |
| `BASE-002` | Minecraft version and supported version range | `docs/MINECRAFT_VERSION_COMPATIBILITY_ENGINE_SPEC.md` | Project/target foundation and compatibility controls. |
| `BASE-004` | Loader/platform selection: NeoForge, Forge, Fabric, Paper, Spigot, Bukkit, Bedrock Add-on, datapack-only, or vanilla | `docs/MINECRAFT_VERSION_COMPATIBILITY_ENGINE_SPEC.md` | Project/target foundation and compatibility controls. |
| `BASE-007` | Project namespace, identifiers, naming rules | `docs/MINECRAFT_VERSION_COMPATIBILITY_ENGINE_SPEC.md` | Project/target foundation and compatibility controls. |
| `BASE-008` | Configuration format, defaults, validation, migration | `docs/MINECRAFT_VERSION_COMPATIBILITY_ENGINE_SPEC.md` | Project/target foundation and compatibility controls. |
| `BASE-009` | Save compatibility, upgrades, downgrade policy | `docs/MINECRAFT_VERSION_COMPATIBILITY_ENGINE_SPEC.md` | Project/target foundation and compatibility controls. |
| `BASE-011` | Environment detection and unsupported-platform warnings | `docs/MINECRAFT_VERSION_COMPATIBILITY_ENGINE_SPEC.md` | Project/target foundation and compatibility controls. |
| `BASE-012` | Licensing, attribution, third-party asset register | `docs/MINECRAFT_VERSION_COMPATIBILITY_ENGINE_SPEC.md` | Project/target foundation and compatibility controls. |

### PLY (4)

| Feature ID | Feature | Current design owner | First-slice interpretation |
|---|---|---|---|
| `PLY-001` | Player attributes and attribute modifiers | `docs/ZOMBIE_INVASION_PLAYER_JOURNEY_CAMPAIGN_AND_LONG_TERM_PROGRESSION_DESIGN_V1.md` | Required support candidate; exact depth must be frozen. |
| `PLY-002` | Health, absorption, regeneration, damage resistance | `docs/ZOMBIE_INVASION_PLAYER_JOURNEY_CAMPAIGN_AND_LONG_TERM_PROGRESSION_DESIGN_V1.md` | Required support candidate; exact depth must be frozen. |
| `PLY-003` | Stamina/energy and recovery | `docs/ZOMBIE_INVASION_PLAYER_JOURNEY_CAMPAIGN_AND_LONG_TERM_PROGRESSION_DESIGN_V1.md` | Required support candidate; exact depth must be frozen. |
| `PLY-004` | Hunger, thirst, temperature, fatigue, hygiene (optional survival modules) | `docs/ZOMBIE_INVASION_PLAYER_JOURNEY_CAMPAIGN_AND_LONG_TERM_PROGRESSION_DESIGN_V1.md` | Required support candidate; exact depth must be frozen. |

### ITEM (6)

| Feature ID | Feature | Current design owner | First-slice interpretation |
|---|---|---|---|
| `ITEM-001` | Item registry, identifiers, rarity, stack limits | `docs/ZOMBIE_INVASION_INVENTORY_SCAVENGING_AND_LOOT_DESIGN_V1.md` | Required support candidate; exact depth must be frozen. |
| `ITEM-003` | Food, drinks, consumables, medicine | `docs/ZOMBIE_INVASION_INVENTORY_SCAVENGING_AND_LOOT_DESIGN_V1.md` | Required support candidate; exact depth must be frozen. |
| `ITEM-005` | Weapons and ammunition | `docs/ZOMBIE_INVASION_INVENTORY_SCAVENGING_AND_LOOT_DESIGN_V1.md` | Required support candidate; exact depth must be frozen. |
| `ITEM-007` | Backpacks, containers, storage items | `docs/ZOMBIE_INVASION_INVENTORY_SCAVENGING_AND_LOOT_DESIGN_V1.md` | Required support candidate; exact depth must be frozen. |
| `ITEM-009` | Durability, repair, degradation, quality | `docs/ZOMBIE_INVASION_INVENTORY_SCAVENGING_AND_LOOT_DESIGN_V1.md` | Required support candidate; exact depth must be frozen. |
| `ITEM-016` | Item/block model, texture, sound, localization references | `docs/ZOMBIE_INVASION_INVENTORY_SCAVENGING_AND_LOOT_DESIGN_V1.md` | Required support candidate; exact depth must be frozen. |

### CRAFT (3)

| Feature ID | Feature | Current design owner | First-slice interpretation |
|---|---|---|---|
| `CRAFT-001` | Crafting recipes and recipe categories | `docs/ZOMBIE_INVASION_CRAFTING_AND_WORKSTATION_PROGRESSION_DESIGN_V1.md` | Required support candidate; exact depth must be frozen. |
| `CRAFT-004` | Custom workstations and interfaces | `docs/ZOMBIE_INVASION_CRAFTING_AND_WORKSTATION_PROGRESSION_DESIGN_V1.md` | Required support candidate; exact depth must be frozen. |
| `CRAFT-010` | Loot tables, drops, rewards, weighted outcomes | `docs/ZOMBIE_INVASION_CRAFTING_AND_WORKSTATION_PROGRESSION_DESIGN_V1.md` | Required support candidate; exact depth must be frozen. |

### ENT (9)

| Feature ID | Feature | Current design owner | First-slice interpretation |
|---|---|---|---|
| `ENT-001` | Custom entity registration and attributes | `docs/ZOMBIE_INVASION_SURVIVOR_NPC_FACTIONS_AND_SETTLEMENT_DESIGN_V1.md` | Required support candidate; exact depth must be frozen. |
| `ENT-003` | Hostile mobs and enemy archetypes | `docs/ZOMBIE_INVASION_SURVIVOR_NPC_FACTIONS_AND_SETTLEMENT_DESIGN_V1.md` | Required support candidate; exact depth must be frozen. |
| `ENT-006` | Entity health, armor, damage, resistances | `docs/ZOMBIE_INVASION_SURVIVOR_NPC_FACTIONS_AND_SETTLEMENT_DESIGN_V1.md` | Required support candidate; exact depth must be frozen. |
| `ENT-007` | Navigation, pathfinding, obstacle handling | `docs/ZOMBIE_INVASION_SURVIVOR_NPC_FACTIONS_AND_SETTLEMENT_DESIGN_V1.md` | Required support candidate; exact depth must be frozen. |
| `ENT-008` | Target selection, threat, aggro, retreat | `docs/ZOMBIE_INVASION_SURVIVOR_NPC_FACTIONS_AND_SETTLEMENT_DESIGN_V1.md` | Required support candidate; exact depth must be frozen. |
| `ENT-011` | Day/night, weather, biome, and event reactions | `docs/ZOMBIE_INVASION_SURVIVOR_NPC_FACTIONS_AND_SETTLEMENT_DESIGN_V1.md` | Required support candidate; exact depth must be frozen. |
| `ENT-012` | Spawning rules, caps, density, despawning | `docs/ZOMBIE_INVASION_SURVIVOR_NPC_FACTIONS_AND_SETTLEMENT_DESIGN_V1.md` | Required support candidate; exact depth must be frozen. |
| `ENT-016` | Entity animation, sounds, particles, hitboxes | `docs/ZOMBIE_INVASION_SURVIVOR_NPC_FACTIONS_AND_SETTLEMENT_DESIGN_V1.md` | Required support candidate; exact depth must be frozen. |
| `ENT-017` | Persistence, chunk unload/reload, entity data | `docs/ZOMBIE_INVASION_SURVIVOR_NPC_FACTIONS_AND_SETTLEMENT_DESIGN_V1.md` | Required support candidate; exact depth must be frozen. |

### COM (7)

| Feature ID | Feature | Current design owner | First-slice interpretation |
|---|---|---|---|
| `COM-001` | Damage types and damage calculation | `docs/ZOMBIE_INVASION_COMBAT_AND_WEAPON_SYSTEM_DESIGN_V1.md` | Required support candidate; exact depth must be frozen. |
| `COM-002` | Melee weapons, reach, attack speed, combos | `docs/ZOMBIE_INVASION_COMBAT_AND_WEAPON_SYSTEM_DESIGN_V1.md` | Required support candidate; exact depth must be frozen. |
| `COM-003` | Ranged weapons, projectiles, trajectory | `docs/ZOMBIE_INVASION_COMBAT_AND_WEAPON_SYSTEM_DESIGN_V1.md` | Required support candidate; exact depth must be frozen. |
| `COM-004` | Firearms, ammunition, reload, recoil (if in scope) | `docs/ZOMBIE_INVASION_COMBAT_AND_WEAPON_SYSTEM_DESIGN_V1.md` | Required support candidate; exact depth must be frozen. |
| `COM-010` | Combat feedback, indicators, logs | `docs/ZOMBIE_INVASION_COMBAT_AND_WEAPON_SYSTEM_DESIGN_V1.md` | Required support candidate; exact depth must be frozen. |
| `COM-011` | Loot, death drops, durability and repair rules | `docs/ZOMBIE_INVASION_COMBAT_AND_WEAPON_SYSTEM_DESIGN_V1.md` | Required support candidate; exact depth must be frozen. |
| `COM-012` | Balance configuration and difficulty scaling | `docs/ZOMBIE_INVASION_COMBAT_AND_WEAPON_SYSTEM_DESIGN_V1.md` | Required support candidate; exact depth must be frozen. |

### WORLD (3)

| Feature ID | Feature | Current design owner | First-slice interpretation |
|---|---|---|---|
| `WORLD-010` | Day/night cycle and time rules | `docs/ZOMBIE_INVASION_WORLD_MAP_BIOMES_AND_EXPLORATION_DESIGN_V1.md` | Bounded authored town and required landmarks; broad procedural expansion deferred. |
| `WORLD-012` | World border, safe zones, protected areas | `docs/ZOMBIE_INVASION_WORLD_MAP_BIOMES_AND_EXPLORATION_DESIGN_V1.md` | Bounded authored town and required landmarks; broad procedural expansion deferred. |
| `WORLD-013` | Prepared map integration and spawn placement | `docs/ZOMBIE_INVASION_WORLD_MAP_BIOMES_AND_EXPLORATION_DESIGN_V1.md` | Bounded authored town and required landmarks; broad procedural expansion deferred. |

### STRUCT (4)

| Feature ID | Feature | Current design owner | First-slice interpretation |
|---|---|---|---|
| `STRUCT-001` | Structure templates and placement rules | `docs/ZOMBIE_INVASION_MAP_DESIGN_V1.md` | Bounded authored town and required landmarks; broad procedural expansion deferred. |
| `STRUCT-003` | Houses, shops, workshops, public buildings | `docs/ZOMBIE_INVASION_MAP_DESIGN_V1.md` | Bounded authored town and required landmarks; broad procedural expansion deferred. |
| `STRUCT-008` | Loot, spawners, traps, secrets | `docs/ZOMBIE_INVASION_MAP_DESIGN_V1.md` | Bounded authored town and required landmarks; broad procedural expansion deferred. |
| `STRUCT-010` | POI discovery, map markers, exploration rewards | `docs/ZOMBIE_INVASION_MAP_DESIGN_V1.md` | Bounded authored town and required landmarks; broad procedural expansion deferred. |

### UI (7)

| Feature ID | Feature | Current design owner | First-slice interpretation |
|---|---|---|---|
| `UI-001` | HUD layout and information hierarchy | `docs/STUDIO_INTERFACE_AND_COMMUNITY_SPEC.md` | Target-specific player-facing surfaces; use native supported UI capabilities. |
| `UI-002` | Menus, screens, tabs, navigation | `docs/STUDIO_INTERFACE_AND_COMMUNITY_SPEC.md` | Target-specific player-facing surfaces; use native supported UI capabilities. |
| `UI-003` | Inventory and container interfaces | `docs/STUDIO_INTERFACE_AND_COMMUNITY_SPEC.md` | Target-specific player-facing surfaces; use native supported UI capabilities. |
| `UI-004` | Crafting, machine, vehicle interfaces | `docs/STUDIO_INTERFACE_AND_COMMUNITY_SPEC.md` | Target-specific player-facing surfaces; use native supported UI capabilities. |
| `UI-006` | Settings and configuration screens | `docs/STUDIO_INTERFACE_AND_COMMUNITY_SPEC.md` | Target-specific player-facing surfaces; use native supported UI capabilities. |
| `UI-008` | Tooltips, prompts, contextual help | `docs/STUDIO_INTERFACE_AND_COMMUNITY_SPEC.md` | Target-specific player-facing surfaces; use native supported UI capabilities. |
| `UI-012` | Localization and language fallback | `docs/STUDIO_INTERFACE_AND_COMMUNITY_SPEC.md` | Target-specific player-facing surfaces; use native supported UI capabilities. |

### ASSET (7)

| Feature ID | Feature | Current design owner | First-slice interpretation |
|---|---|---|---|
| `ASSET-001` | Art direction and visual style guide | `docs/AI_ASSET_GENERATION_PIPELINE_SPEC.md` | Only assets needed by approved gameplay features; all exports require target and license checks. |
| `ASSET-002` | Item and block textures/models | `docs/AI_ASSET_GENERATION_PIPELINE_SPEC.md` | Only assets needed by approved gameplay features; all exports require target and license checks. |
| `ASSET-003` | Entity models, rigs, animations | `docs/AI_ASSET_GENERATION_PIPELINE_SPEC.md` | Only assets needed by approved gameplay features; all exports require target and license checks. |
| `ASSET-005` | GUI textures, icons, fonts | `docs/AI_ASSET_GENERATION_PIPELINE_SPEC.md` | Only assets needed by approved gameplay features; all exports require target and license checks. |
| `ASSET-008` | Item, block, entity, weapon, vehicle sounds | `docs/AI_ASSET_GENERATION_PIPELINE_SPEC.md` | Only assets needed by approved gameplay features; all exports require target and license checks. |
| `ASSET-011` | Asset attribution, formats, optimization | `docs/AI_ASSET_GENERATION_PIPELINE_SPEC.md` | Only assets needed by approved gameplay features; all exports require target and license checks. |
| `ASSET-012` | Resource-pack compatibility and fallback | `docs/AI_ASSET_GENERATION_PIPELINE_SPEC.md` | Only assets needed by approved gameplay features; all exports require target and license checks. |

### QA (15)

| Feature ID | Feature | Current design owner | First-slice interpretation |
|---|---|---|---|
| `QA-001` | Schema and manifest validation | `docs/MASTER_INTEGRATION_AUDIT_V1.md` | Target-specific validation gate; must not be skipped or reported as passed without evidence. |
| `QA-002` | Identifier, registry, and reference validation | `docs/MASTER_INTEGRATION_AUDIT_V1.md` | Target-specific validation gate; must not be skipped or reported as passed without evidence. |
| `QA-003` | Dependency graph and cycle detection | `docs/MASTER_INTEGRATION_AUDIT_V1.md` | Target-specific validation gate; must not be skipped or reported as passed without evidence. |
| `QA-004` | Version and loader compatibility checks | `docs/MASTER_INTEGRATION_AUDIT_V1.md` | Target-specific validation gate; must not be skipped or reported as passed without evidence. |
| `QA-005` | Static analysis and code quality | `docs/MASTER_INTEGRATION_AUDIT_V1.md` | Target-specific validation gate; must not be skipped or reported as passed without evidence. |
| `QA-006` | Unit tests for isolated logic | `docs/MASTER_INTEGRATION_AUDIT_V1.md` | Target-specific validation gate; must not be skipped or reported as passed without evidence. |
| `QA-007` | Integration tests across components | `docs/MASTER_INTEGRATION_AUDIT_V1.md` | Target-specific validation gate; must not be skipped or reported as passed without evidence. |
| `QA-008` | Build tests for each deliverable | `docs/MASTER_INTEGRATION_AUDIT_V1.md` | Target-specific validation gate; must not be skipped or reported as passed without evidence. |
| `QA-010` | World creation/load test | `docs/MASTER_INTEGRATION_AUDIT_V1.md` | Target-specific validation gate; must not be skipped or reported as passed without evidence. |
| `QA-011` | In-game feature acceptance tests | `docs/MASTER_INTEGRATION_AUDIT_V1.md` | Target-specific validation gate; must not be skipped or reported as passed without evidence. |
| `QA-013` | Save/reload and migration tests | `docs/MASTER_INTEGRATION_AUDIT_V1.md` | Target-specific validation gate; must not be skipped or reported as passed without evidence. |
| `QA-014` | Performance profiling and memory tests | `docs/MASTER_INTEGRATION_AUDIT_V1.md` | Target-specific validation gate; must not be skipped or reported as passed without evidence. |
| `QA-015` | Crash, exploit, duplication, and abuse tests | `docs/MASTER_INTEGRATION_AUDIT_V1.md` | Target-specific validation gate; must not be skipped or reported as passed without evidence. |
| `QA-017` | Test evidence, logs, reproducibility | `docs/MASTER_INTEGRATION_AUDIT_V1.md` | Target-specific validation gate; must not be skipped or reported as passed without evidence. |
| `QA-018` | Known limitations and untested areas register | `docs/MASTER_INTEGRATION_AUDIT_V1.md` | Target-specific validation gate; must not be skipped or reported as passed without evidence. |

### SHIP (11)

| Feature ID | Feature | Current design owner | First-slice interpretation |
|---|---|---|---|
| `SHIP-001` | Source project folder structure | `docs/PUBLISHING_VERSIONING_UPDATE_ENGINE_SPEC.md` | Delivery infrastructure required to produce verifiable outputs. |
| `SHIP-002` | Reproducible build configuration | `docs/PUBLISHING_VERSIONING_UPDATE_ENGINE_SPEC.md` | Delivery infrastructure required to produce verifiable outputs. |
| `SHIP-003` | Mod JAR / plugin JAR / add-on package | `docs/PUBLISHING_VERSIONING_UPDATE_ENGINE_SPEC.md` | Delivery infrastructure required to produce verifiable outputs. |
| `SHIP-004` | Datapack and resource-pack exports | `docs/PUBLISHING_VERSIONING_UPDATE_ENGINE_SPEC.md` | Delivery infrastructure required to produce verifiable outputs. |
| `SHIP-005` | World/map export and required metadata | `docs/PUBLISHING_VERSIONING_UPDATE_ENGINE_SPEC.md` | Delivery infrastructure required to produce verifiable outputs. |
| `SHIP-006` | Dependency and installation instructions | `docs/PUBLISHING_VERSIONING_UPDATE_ENGINE_SPEC.md` | Delivery infrastructure required to produce verifiable outputs. |
| `SHIP-008` | ZIP bundle with editable sources | `docs/PUBLISHING_VERSIONING_UPDATE_ENGINE_SPEC.md` | Delivery infrastructure required to produce verifiable outputs. |
| `SHIP-009` | Versioning, changelog, release notes | `docs/PUBLISHING_VERSIONING_UPDATE_ENGINE_SPEC.md` | Delivery infrastructure required to produce verifiable outputs. |
| `SHIP-010` | Checksums and artifact manifest | `docs/PUBLISHING_VERSIONING_UPDATE_ENGINE_SPEC.md` | Delivery infrastructure required to produce verifiable outputs. |
| `SHIP-011` | Clean-install verification | `docs/PUBLISHING_VERSIONING_UPDATE_ENGINE_SPEC.md` | Delivery infrastructure required to produce verifiable outputs. |
| `SHIP-012` | Final playable acceptance checklist | `docs/PUBLISHING_VERSIONING_UPDATE_ENGINE_SPEC.md` | Delivery infrastructure required to produce verifiable outputs. |

## 3. Explicit exclusions from the first-slice candidate baseline

These feature families remain in the overall project catalog but are excluded from the first-slice candidate list by default:

- Vehicles and factory transport systems.
- Multiplayer, dedicated servers, synchronization and cross-play.
- Economy, player trading, factions, social systems and remote moderation.
- Main/side quest and full campaign systems.
- Full biome/ecology/weather/season simulation and world-scale procedural expansion.
- Large-scale settlement, power, water, sanitation and automation networks.
- Full advanced injury catalogue, limb amputation and bionic prosthetics unless explicitly promoted.
- Full vehicle, aircraft, watercraft and convoy progression.

An exclusion from the first playable is staging, not cancellation of the long-term requirement.

## 4. Decisions still required before scope freeze

1. Confirm or revise the 84 candidate IDs as a complete set.
2. Decide whether food/drink/thirst and day/night are first-playable features or later milestone features; they remain confirmed project requirements either way.
3. Freeze exact first-slice weapon roster, ammunition types, durability rules and balance.
4. Freeze backpack variants and storage capacities.
5. Freeze the first-slice medical/injury/recovery subset.
6. Freeze initial crafting recipes and specialist workstation set.
7. Freeze loot source categories and initial table constraints.
8. Confirm whether Java datapack and Bedrock Script API modules are actually required after target-specific design.

## 5. Approval rule

Do not change feature status to approved, do not set component status to approved, and do not start generation until the user approves the exact final feature-ID set. Approval must reference the manifest revision number, revision digest and scope digest. Any subsequent scope change creates a new revision.

## 6. Related documents

- `schemas/zombie-invasion.project-manifest.v2.draft.json`
- `docs/ZOMBIE_INVASION_PROJECT_MANIFEST_V2_DRAFT_REVIEW_V1.md`
- `docs/ZOMBIE_INVASION_IMPLEMENTATION_READINESS_AND_CODE_ENTRY_GATE_V1.md`
- `docs/ZOMBIE_INVASION_TARGET_TOOLCHAIN_COMPATIBILITY_RESEARCH_2026-11.md`
