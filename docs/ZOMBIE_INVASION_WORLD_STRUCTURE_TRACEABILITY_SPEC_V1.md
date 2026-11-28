# Zombie Invasion — World, Map and Structure Traceability Specification v1

**Status:** Detailed feature mapping; world topology approved, per-feature target feasibility unverified  
**Date:** 2026-11-28  
**Feature IDs:** WORLD-001..WORLD-017 and STRUCT-001..STRUCT-010  
**Supporting designs:** world map/biomes, world simulation/resource cycles, ecosystem, water/sanitation, base building and first map

## 1. Purpose and world decisions

This document maps 27 world and structure features to requirements, target behavior, acceptance criteria and test cases. The user-approved long-term topology is one large continuous world organized into connected regions, with authored major locations, deterministic procedural secondary content and incremental expansion. The first playable remains a compact authored abandoned town.

Confirmed first-map requirements: the Market, Hospital and Police Station must be functional. The first-slice world is not required to implement every long-term biome, dimension, region, settlement or transport system.

## 2. Critical Java/Bedrock feasibility boundary

World generation, terrain modification, biome control, chunk tickets and existing-world conversion must be assessed separately for Java 26.3 + Fabric and Bedrock 26.60 + stable APIs. Do not assume Bedrock stable Script API exposes the same terrain-generation hooks as Java. Where runtime generation is unavailable or unsuitable, use pre-generated/authored world artifacts and deterministic assembly. Experimental APIs remain disabled.

## 3. Shared world contracts

- One authoritative world clock and stable world/region/POI/structure IDs.
- Authored landmarks must remain stable across procedural expansion.
- Procedural generation is deterministic under pinned seed/configuration and cannot overwrite player-owned structures.
- Active/near/distant simulation tiers bound chunk/entity work; distant simulation never force-loads remote chunks.
- Water, ecology, resource, zombie, NPC and transport systems consume shared world/region state rather than creating duplicate clocks or inventories.
- World save migration is backed up and edition-specific.

## 4. Feature-level mapping

### WORLD-001 — World type and dimension plan

**Requirement:** REQ-WORLD-001  
**Purpose:** Define the persistent world topology, dimension policy, region identity and target-specific world bundle structure.  
**Target mapping:** First slice uses one compact overworld town; long-term world uses one continuous regionally organized world with staged expansion.

**Acceptance criteria**
- AC-WORLD-001-01: Every world has stable project/world/region IDs and explicit dimension policy; first-slice dimensions are declared rather than implicitly generated.
- AC-WORLD-001-02: Java and Bedrock world deliverables are separate and load with their declared target profiles.

**Test cases**
- TC-WORLD-001-01: TC-WORLD-001-01 first-slice world profile and stable region IDs
- TC-WORLD-001-02: TC-WORLD-001-02 undeclared dimension/world target rejected

**Prerequisite feature IDs:** BASE-001, BASE-002.

### WORLD-002 — Biome registry and biome distribution

**Requirement:** REQ-WORLD-002  
**Purpose:** Define biome/habitat IDs, climate/resource relationships and regional distribution.  
**Target mapping:** Use native biomes where suitable and explicit target mapping; custom distribution feasibility is assessed separately per edition.

**Acceptance criteria**
- AC-WORLD-002-01: Every biome has stable ID, climate/habitat/resource metadata and valid target representation.
- AC-WORLD-002-02: No biome is reported supported if its target generation or presentation mapping is unverified.

**Test cases**
- TC-WORLD-002-01: TC-WORLD-002-01 biome registry and metadata validation
- TC-WORLD-002-02: TC-WORLD-002-02 target biome support and fallback report

**Prerequisite feature IDs:** WORLD-001.

### WORLD-003 — Terrain height, shapes, noise, erosion

**Requirement:** REQ-WORLD-003  
**Purpose:** Define terrain generation profiles and authored terrain geometry with reproducible seeds.  
**Target mapping:** Java and Bedrock terrain-generation capability must be independently verified; authored/prebuilt world geometry is the fallback path.

**Acceptance criteria**
- AC-WORLD-003-01: Terrain generation is deterministic for fixed seed/config and respects declared world bounds.
- AC-WORLD-003-02: Unsupported runtime terrain APIs are not assumed; target-specific limitations are surfaced before generation.

**Test cases**
- TC-WORLD-003-01: TC-WORLD-003-01 deterministic terrain generation from fixed seed
- TC-WORLD-003-02: TC-WORLD-003-02 unsupported target generation capability is blocked/reported

**Prerequisite feature IDs:** WORLD-001, WORLD-014.

### WORLD-004 — Surface materials, strata, caves

**Requirement:** REQ-WORLD-004  
**Purpose:** Define surface layers, underground strata, cave networks and material placement.  
**Target mapping:** Target-specific world-generation/structure tools; shared logical material distribution and cave intent.

**Acceptance criteria**
- AC-WORLD-004-01: Layer and cave definitions stay within world bounds and reference valid block IDs.
- AC-WORLD-004-02: Resource placement and cave generation do not create invalid blocks or bypass world performance budgets.

**Test cases**
- TC-WORLD-004-01: TC-WORLD-004-01 strata and cave bounds validation
- TC-WORLD-004-02: TC-WORLD-004-02 material registry and generated block validation

**Prerequisite feature IDs:** WORLD-003, ITEM-011.

### WORLD-005 — Rivers, lakes, oceans, water systems

**Requirement:** REQ-WORLD-005  
**Purpose:** Define freshwater and marine geography as world features connected to the water-cycle system.  
**Target mapping:** Use authored/prebuilt water geography where runtime generation is unavailable; water behavior maps to water infrastructure contracts.

**Acceptance criteria**
- AC-WORLD-005-01: Water bodies have stable region/feature identity and connect to terrain, climate and water-quality systems.
- AC-WORLD-005-02: Generated water does not create unbounded fluid updates or bypass contamination/storage rules.

**Test cases**
- TC-WORLD-005-01: TC-WORLD-005-01 water body geometry and regional references
- TC-WORLD-005-02: TC-WORLD-005-02 water quality and fluid simulation boundary

**Prerequisite feature IDs:** WORLD-002, WORLD-003.

### WORLD-006 — Vegetation, flora, crops, trees

**Requirement:** REQ-WORLD-006  
**Purpose:** Define native and custom vegetation, regrowth, harvestability and biome suitability.  
**Target mapping:** Java and Bedrock use separate block/feature registrations; shared species and crop definitions.

**Acceptance criteria**
- AC-WORLD-006-01: Plant placement obeys biome/season/growth rules and valid block/asset references.
- AC-WORLD-006-02: Harvest/regrowth changes authoritative resource stock and cannot duplicate yields after reload.

**Test cases**
- TC-WORLD-006-01: TC-WORLD-006-01 vegetation suitability and placement
- TC-WORLD-006-02: TC-WORLD-006-02 harvest/regrowth conservation

**Prerequisite feature IDs:** WORLD-002, WORLD-008.

### WORLD-007 — Ore and resource distribution

**Requirement:** REQ-WORLD-007  
**Purpose:** Define regional resource deposits, scarcity, extraction and finite/renewable classifications.  
**Target mapping:** Target-specific worldgen or authored resource placement with shared resource accounting.

**Acceptance criteria**
- AC-WORLD-007-01: Deposits have region, quantity/classification, extraction and replenishment policy.
- AC-WORLD-007-02: Resource distribution is deterministic under fixed seed and cannot be duplicated by chunk regeneration.

**Test cases**
- TC-WORLD-007-01: TC-WORLD-007-01 resource deposit placement and quantity accounting
- TC-WORLD-007-02: TC-WORLD-007-02 chunk regeneration does not duplicate deposits

**Prerequisite feature IDs:** WORLD-003, WORLD-004.

### WORLD-008 — Climate, temperature, humidity

**Requirement:** REQ-WORLD-008  
**Purpose:** Define climate zones and regional temperature/humidity inputs for seasons, crops, disease and player survival.  
**Target mapping:** Shared climate state with edition-specific visual/environment adapters.

**Acceptance criteria**
- AC-WORLD-008-01: Climate values are bounded and derived from world/region/time data, not separate subsystem clocks.
- AC-WORLD-008-02: Player, NPC, crop and wildlife systems consume the same authoritative regional climate snapshot.

**Test cases**
- TC-WORLD-008-01: TC-WORLD-008-01 regional climate bounds and determinism
- TC-WORLD-008-02: TC-WORLD-008-02 climate snapshot consistency across consumers

**Prerequisite feature IDs:** WORLD-002.

### WORLD-009 — Weather, storms, environmental hazards

**Requirement:** REQ-WORLD-009  
**Purpose:** Define rain, snow, wind, storms, drought, flood and other environmental events.  
**Target mapping:** Use native weather where available and bounded scripted/world-event adaptations; no unsupported API assumptions.

**Acceptance criteria**
- AC-WORLD-009-01: Weather events have duration, region, severity and effects; hazards use explicit budgets and warnings.
- AC-WORLD-009-02: Fire/flood/storm consequences update world state once and respect safe zones and performance caps.

**Test cases**
- TC-WORLD-009-01: TC-WORLD-009-01 weather event lifecycle and region scope
- TC-WORLD-009-02: TC-WORLD-009-02 hazard warning, persistence and bounded propagation

**Prerequisite feature IDs:** WORLD-008, WORLD-010.

### WORLD-010 — Day/night cycle and time rules

**Requirement:** REQ-WORLD-010  
**Purpose:** Define the authoritative world clock, day/night phases, calendar and shared time consumers.  
**Target mapping:** Both editions map their native world time into one logical calendar and deterministic simulation ticks.

**Acceptance criteria**
- AC-WORLD-010-01: Only one authoritative clock drives NPC schedules, thirst/food decay, spoilage, crops, power and encounters.
- AC-WORLD-010-02: Time progression, pause/sleep behavior and save/reload cannot double-advance elapsed time.

**Test cases**
- TC-WORLD-010-01: TC-WORLD-010-01 day/night phase transitions and single clock
- TC-WORLD-010-02: TC-WORLD-010-02 save/reload and time consumer synchronization

**Prerequisite feature IDs:** WORLD-001.

### WORLD-011 — Dimension travel, portals, boundaries

**Requirement:** REQ-WORLD-011  
**Purpose:** Define optional dimension topology, travel gates and safe transition contracts.  
**Target mapping:** No additional dimension is required for the first slice; target support is assessed independently before any portal feature.

**Acceptance criteria**
- AC-WORLD-011-01: Cross-dimension transitions preserve player/world identity and cannot duplicate entities or inventory.
- AC-WORLD-011-02: Unapproved dimensions and unsupported portal behavior are excluded from first-slice manifests.

**Test cases**
- TC-WORLD-011-01: TC-WORLD-011-01 dimension policy validation
- TC-WORLD-011-02: TC-WORLD-011-02 transition state and duplication prevention

**Prerequisite feature IDs:** WORLD-001.

### WORLD-012 — World border, safe zones, protected areas

**Requirement:** REQ-WORLD-012  
**Purpose:** Define playable bounds, protected regions, safehouse claims and restricted/high-risk zones.  
**Target mapping:** Target-specific world border/region protection implementation with shared logical region rules.

**Acceptance criteria**
- AC-WORLD-012-01: Bounds and protection rules are enforced for player actions, spawning, structures and world events.
- AC-WORLD-012-02: Safe zones do not become exploit paths for resource duplication or hostile actor teleporting.

**Test cases**
- TC-WORLD-012-01: TC-WORLD-012-01 boundary and protected action enforcement
- TC-WORLD-012-02: TC-WORLD-012-02 safe-zone threat and exploit checks

**Prerequisite feature IDs:** WORLD-001.

### WORLD-013 — Prepared map integration and spawn placement

**Requirement:** REQ-WORLD-013  
**Purpose:** Integrate authored map content, player spawn, safehouse and first-slice landmarks.  
**Target mapping:** Java world save and Bedrock world bundle are separately assembled and validated.

**Acceptance criteria**
- AC-WORLD-013-01: First playable includes compact abandoned town and functional Market, Hospital and Police Station; spawn is safe and repeatable.
- AC-WORLD-013-02: Prepared map loads with required packs, structures and spawn metadata without missing references.

**Test cases**
- TC-WORLD-013-01: TC-WORLD-013-01 first map landmarks and spawn validation
- TC-WORLD-013-02: TC-WORLD-013-02 fresh import and safe spawn repeatability

**Prerequisite feature IDs:** WORLD-001, STRUCT-001.

### WORLD-014 — Procedural generation settings and seeds

**Requirement:** REQ-WORLD-014  
**Purpose:** Define deterministic seed, region rules, feature toggles and reproducible generation configuration.  
**Target mapping:** Generation inputs and seed behavior are pinned per target; unsupported runtime generation uses pre-generated artifacts.

**Acceptance criteria**
- AC-WORLD-014-01: Same seed and configuration produce the same authored/procedural selection and stable region IDs.
- AC-WORLD-014-02: User-visible seed/config changes create a new revision and do not mutate an existing approved world silently.

**Test cases**
- TC-WORLD-014-01: TC-WORLD-014-01 deterministic seed/config output
- TC-WORLD-014-02: TC-WORLD-014-02 generation settings revision and reproducibility

**Prerequisite feature IDs:** WORLD-001.

### WORLD-015 — Hybrid prepared-world plus procedural-generation rules

**Requirement:** REQ-WORLD-015  
**Purpose:** Combine authored cities/story landmarks with deterministic procedural secondary settlements, POIs and resource nodes.  
**Target mapping:** Java and Bedrock use independent generation/assembly pipelines but preserve shared world topology and logical IDs.

**Acceptance criteria**
- AC-WORLD-015-01: Authored landmarks remain stable while procedural content obeys region templates, exclusions and deterministic seeds.
- AC-WORLD-015-02: Expansion does not overwrite player builds, discovered state or owned structures.

**Test cases**
- TC-WORLD-015-01: TC-WORLD-015-01 authored landmark preservation with procedural additions
- TC-WORLD-015-02: TC-WORLD-015-02 expansion preserves player-owned/discovered state

**Prerequisite feature IDs:** WORLD-013, WORLD-014.

### WORLD-016 — Chunk generation, loading, tickets, performance

**Requirement:** REQ-WORLD-016  
**Purpose:** Define chunk/region loading policy, generation queues, simulation tiers and performance budgets.  
**Target mapping:** Target-native chunk APIs and limitations are validated separately; no force-loading unsupported distant regions.

**Acceptance criteria**
- AC-WORLD-016-01: Active/near/distant simulation obeys bounded work and does not load remote chunks solely to simulate distant actors.
- AC-WORLD-016-02: Region activation, unload and save preserve actors/resources/events without duplication or data loss.

**Test cases**
- TC-WORLD-016-01: TC-WORLD-016-01 chunk/region work budget and no distant force-load
- TC-WORLD-016-02: TC-WORLD-016-02 unload/reload conservation and event idempotency

**Prerequisite feature IDs:** WORLD-003, WORLD-015.

### WORLD-017 — Existing-world conversion and compatibility

**Requirement:** REQ-WORLD-017  
**Purpose:** Define import/upgrade of existing worlds and safe compatibility checks for pre-existing data.  
**Target mapping:** Java and Bedrock conversion pipelines are separate; support only declared source versions and world types.

**Acceptance criteria**
- AC-WORLD-017-01: Conversion is non-destructive, backed up and reports unsupported blocks/entities/components.
- AC-WORLD-017-02: A failed conversion leaves original world recoverable and never silently deletes player content.

**Test cases**
- TC-WORLD-017-01: TC-WORLD-017-01 supported existing-world conversion
- TC-WORLD-017-02: TC-WORLD-017-02 failed conversion backup/recovery

**Prerequisite feature IDs:** WORLD-001, WORLD-016, BASE-009.

### STRUCT-001 — Structure templates and placement rules

**Requirement:** REQ-STRUCT-001  
**Purpose:** Define reusable structure templates, bounds, rotation, terrain fit, placement validation and stable structure IDs.  
**Target mapping:** Target-specific structure assets/placement tools; shared template metadata and logical identities.

**Acceptance criteria**
- AC-STRUCT-001-01: Templates declare footprint, anchor, block references, rotations, collision and placement constraints.
- AC-STRUCT-001-02: Placement is deterministic and cannot overwrite player-owned structures without explicit permission.

**Test cases**
- TC-STRUCT-001-01: TC-STRUCT-001-01 template schema and placement validation
- TC-STRUCT-001-02: TC-STRUCT-001-02 rotation/terrain fit and player-build protection

**Prerequisite feature IDs:** WORLD-001, ITEM-011.

### STRUCT-002 — Villages, settlements, towns, cities

**Requirement:** REQ-STRUCT-002  
**Purpose:** Define settlement templates, districts, services, population slots and expansion links.  
**Target mapping:** Authored major settlements plus deterministic procedural secondary settlements; target world packaging remains separate.

**Acceptance criteria**
- AC-STRUCT-002-01: First playable compact abandoned town is authored; long-term settlements use stable region/settlement IDs.
- AC-STRUCT-002-02: Settlement expansion preserves discoveries, player ownership and NPC assignments.

**Test cases**
- TC-STRUCT-002-01: TC-STRUCT-002-01 first town district and service landmark validation
- TC-STRUCT-002-02: TC-STRUCT-002-02 settlement expansion and persistent identity

**Prerequisite feature IDs:** STRUCT-001, WORLD-015.

### STRUCT-003 — Houses, shops, workshops, public buildings

**Requirement:** REQ-STRUCT-003  
**Purpose:** Define building classes, interiors, searchable containers and functional service roles.  
**Target mapping:** Java/Bedrock building templates and interaction components are separate; shared building purpose and loot identity.

**Acceptance criteria**
- AC-STRUCT-003-01: Market, Hospital and Police Station are functional first-slice locations with their approved gameplay roles.
- AC-STRUCT-003-02: Interior routes, container ownership, loot identity and structure references validate before packaging.

**Test cases**
- TC-STRUCT-003-01: TC-STRUCT-003-01 Market Hospital Police Station functional role tests
- TC-STRUCT-003-02: TC-STRUCT-003-02 interior/container references and access rules

**Prerequisite feature IDs:** STRUCT-001, ITEM-011.

### STRUCT-004 — Dungeons, ruins, bunkers, underground sites

**Requirement:** REQ-STRUCT-004  
**Purpose:** Define optional exploration sites, interior progression, hazards, loot and underground navigation.  
**Target mapping:** Target-specific structure generation/import; first-slice underground shelter may remain later scope.

**Acceptance criteria**
- AC-STRUCT-004-01: Each site has stable identity, access rules, bounds, exit path and declared loot/encounter budgets.
- AC-STRUCT-004-02: No dungeon/ruin is included in first-slice scope without explicit manifest selection and tests.

**Test cases**
- TC-STRUCT-004-01: TC-STRUCT-004-01 site bounds, access and exit validation
- TC-STRUCT-004-02: TC-STRUCT-004-02 optional site scope and loot budget gate

**Prerequisite feature IDs:** STRUCT-001, WORLD-004.

### STRUCT-005 — Military, industrial, research, and transport sites

**Requirement:** REQ-STRUCT-005  
**Purpose:** Define specialized POIs for military, factory, laboratory, rail/port/transport and advanced production progression.  
**Target mapping:** Use authored landmarks for critical progression; procedural placement only for approved secondary variants.

**Acceptance criteria**
- AC-STRUCT-005-01: Sites expose required stations/resources only when progression and ownership rules allow them.
- AC-STRUCT-005-02: First-slice military checkpoint, research lab and factory activation remain staged unless explicitly selected.

**Test cases**
- TC-STRUCT-005-01: TC-STRUCT-005-01 specialist POI role and progression gating
- TC-STRUCT-005-02: TC-STRUCT-005-02 staged landmark scope validation

**Prerequisite feature IDs:** STRUCT-001, WORLD-007.

### STRUCT-006 — Roads, bridges, tunnels, railways

**Requirement:** REQ-STRUCT-006  
**Purpose:** Define connected transport corridors, traversal geometry, crossing limits and route metadata.  
**Target mapping:** Authored primary routes with deterministic procedural secondary connections; target collision/pathing tested separately.

**Acceptance criteria**
- AC-STRUCT-006-01: Road graph connects required town landmarks and supports future vehicles/convoys without broken dead-end routes.
- AC-STRUCT-006-02: Bridge/tunnel/rail geometry respects terrain, water, world bounds and chunk performance.

**Test cases**
- TC-STRUCT-006-01: TC-STRUCT-006-01 town route connectivity and traversability
- TC-STRUCT-006-02: TC-STRUCT-006-02 road/bridge/tunnel geometry and loading budget

**Prerequisite feature IDs:** WORLD-003, WORLD-005, WORLD-015.

### STRUCT-007 — Randomized variants and procedural layout

**Requirement:** REQ-STRUCT-007  
**Purpose:** Define bounded variants for secondary buildings, interiors, loot rooms and settlement layouts.  
**Target mapping:** Use deterministic seed-based variants; major authored landmarks remain stable.

**Acceptance criteria**
- AC-STRUCT-007-01: Variants obey template bounds, structural integrity and required service/loot roles.
- AC-STRUCT-007-02: Variant generation does not create inaccessible rooms, duplicate unique items or overwrite player builds.

**Test cases**
- TC-STRUCT-007-01: TC-STRUCT-007-01 deterministic variant selection and bounds
- TC-STRUCT-007-02: TC-STRUCT-007-02 accessibility and duplicate loot prevention

**Prerequisite feature IDs:** STRUCT-001, WORLD-014.

### STRUCT-008 — Loot, spawners, traps, secrets

**Requirement:** REQ-STRUCT-008  
**Purpose:** Define structure-linked loot containers, encounter triggers, traps, secrets and one-time rewards.  
**Target mapping:** Target-specific container/spawn/trap implementations with shared loot/encounter budgets.

**Acceptance criteria**
- AC-STRUCT-008-01: Loot uses the canonical loot engine and is tied to structure/container identity; encounter spawns use Encounter Director.
- AC-STRUCT-008-02: One-time claims, reset behavior and trap triggers are idempotent and respect safe zones/permissions.

**Test cases**
- TC-STRUCT-008-01: TC-STRUCT-008-01 structure loot ownership and one-time claim
- TC-STRUCT-008-02: TC-STRUCT-008-02 trap/spawn trigger budget and reset behavior

**Prerequisite feature IDs:** STRUCT-001, CRAFT-010, ENT-012.

### STRUCT-009 — Structure integrity and regeneration

**Requirement:** REQ-STRUCT-009  
**Purpose:** Define damage, breach, repair, collapse and optional regeneration for buildings/fortifications.  
**Target mapping:** Target-native block/structure state adapters with shared integrity rules.

**Acceptance criteria**
- AC-STRUCT-009-01: Damage and repair update authoritative structure state; repair consumes real materials and time where configured.
- AC-STRUCT-009-02: Automatic regeneration remains disabled unless explicitly configured; player modifications are not silently reverted.

**Test cases**
- TC-STRUCT-009-01: TC-STRUCT-009-01 structure damage/repair material accounting
- TC-STRUCT-009-02: TC-STRUCT-009-02 player modification preservation and regen policy

**Prerequisite feature IDs:** STRUCT-001, ITEM-011, ITEM-012.

### STRUCT-010 — POI discovery, map markers, exploration rewards

**Requirement:** REQ-STRUCT-010  
**Purpose:** Define discovery states, map markers, notes, radio intel and exploration rewards.  
**Target mapping:** Shared POI IDs and discovery logic; Java/Bedrock map/UI presentation adapted separately.

**Acceptance criteria**
- AC-STRUCT-010-01: A POI is discovered only through valid proximity, intel or explicit objective event; rewards are idempotent.
- AC-STRUCT-010-02: Undiscovered locations are not leaked through NPC dialogue, map markers or faction knowledge.

**Test cases**
- TC-STRUCT-010-01: TC-STRUCT-010-01 POI discovery and reward idempotency
- TC-STRUCT-010-02: TC-STRUCT-010-02 map marker and information boundary

**Prerequisite feature IDs:** STRUCT-002, WORLD-013.

## 5. Supporting design references

- `docs/ZOMBIE_INVASION_WORLD_MAP_BIOMES_AND_EXPLORATION_DESIGN_V1.md` — world topology, regions, biomes, seasons, exploration and incremental expansion.
- `docs/ZOMBIE_INVASION_WORLD_SIMULATION_RESOURCE_CYCLES_AND_DYNAMIC_WORLD_DESIGN_V1.md` — world clock, resource cycles, regional simulation and persistence.
- `docs/ZOMBIE_INVASION_ECOSYSTEM_BIOMES_WILDLIFE_AND_ENVIRONMENT_SIMULATION_DESIGN_V1.md` — habitats, wildlife, crops, weather, seasons and environmental processes.
- `docs/ZOMBIE_INVASION_WATER_CYCLE_AND_SANITATION_DESIGN_V1.md` — rivers/water sources, quality, storage and infrastructure interactions.
- `docs/ZOMBIE_INVASION_BASE_BUILDING_CLAIM_DEFENSE_AUTOMATION_DESIGN_V1.md` — claim, construction, fortification and structure ownership.
- `docs/ZOMBIE_INVASION_MAP_DESIGN_V1.md` — compact abandoned town and functional Market/Hospital/Police Station.

## 6. Open decisions preserved

- Exact world dimensions, world bounds, region sizes and chunk budgets require target profiling.
- Exact biome/region catalogue and climate distribution remain content authoring work.
- Runtime procedural terrain generation feasibility must be verified independently for both editions; authored world bundles remain the fallback.
- Extra dimensions, portals, underground shelter, military/research/factory sites and full transport corridors are later-stage unless selected in a manifest revision.
- Structure regeneration policy is not assumed; player-built and modified structures must be protected.
- Exact season lengths, weather rates, resource yields and hazard severity remain open balance values.

## 7. Implementation order

1. World identity, target world profiles, clock and stable region IDs.
2. Authored first map, spawn placement, structures and functional building interiors.
3. Biome/climate/weather/day-night state contracts and water geography.
4. Seed/configuration, deterministic procedural additions and expansion safeguards.
5. Chunk/region performance, persistence, save migration and existing-world compatibility.
6. Wider biome, settlement, POI and transport content after first-slice validation.

## 8. Implementation boundary

These 27 features are mapped for design traceability only. They remain `not_implemented_verified`; Java, Bedrock and parity remain unassessed until target-specific world artifacts, imports, runtime tests and evidence exist. The topology approval is not proof of infinite, seamless or fully procedural world generation.
