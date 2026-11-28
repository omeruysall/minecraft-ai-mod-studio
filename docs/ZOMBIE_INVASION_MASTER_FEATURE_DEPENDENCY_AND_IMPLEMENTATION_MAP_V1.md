# Zombie Invasion — Master Feature, Dependency and Implementation Map V1

**Status:** Integrated design map; dependency direction and subsystem ownership proposed for review. User-approved feature requests remain distinct from proposed sequencing. Not implemented.
**Date:** 2026-11-28
**Targets:** Java Edition 26.3 + Fabric; Bedrock 26.60 + stable `@minecraft/server` 2.11.0; experimental APIs disabled.
**Source references:** `docs/MOD_SYSTEM_INVENTORY.md`, `catalogs/feature-traceability-matrix.v1.json`, `docs/COMPONENT_OWNERSHIP_MATRIX_V1.md`, `docs/PROJECT_MANIFEST_V2_DESIGN.md`, `docs/MASTER_DEVELOPMENT_ROADMAP_V2.md`, zombie-invasion subsystem specifications, world-simulation and player-progression specifications.

## 1. Purpose and interpretation

This document is the cross-system navigation map for the Zombie Invasion test project. It consolidates feature families, authoritative owners, prerequisite relationships, cross-system contracts, proposed delivery waves and verification gates.

It does not replace detailed subsystem specifications or the Studio's canonical project manifest. The master inventory remains the feature source catalog; the traceability matrix remains the feature-by-feature status ledger; this map explains how the feature families connect.

Status vocabulary:
- **User-confirmed requirement:** explicitly requested or approved by the user.
- **Designed proposal:** documented architecture or suggested behavior not yet explicitly approved as a detailed gameplay rule.
- **Open:** exact values, content, scope, platform feasibility or milestone placement remain undecided.
- **Not implemented:** no gameplay code or playable artifact is claimed by this design map.

A feature being listed, linked or assigned an owner does not make it approved, implemented or tested.

## 2. Global dependency rules

1. Shared identity and versioned data contracts precede dependent gameplay features.
2. Each canonical state has one authoritative owner, as defined in the component ownership matrix.
3. Consumers request changes through owner contracts; no subsystem writes another subsystem's canonical state directly.
4. Resource creation, transfer, consumption, spoilage and destruction are explicit idempotent transactions.
5. The world clock is the only time authority.
6. World state and player/NPC/faction knowledge are separate.
7. Java and Bedrock share feature intent and stable IDs, but have separate target components, build jobs, capability assessments and evidence.
8. A feature cannot be marked parity-complete until both target implementations pass their own acceptance criteria.
9. First playable scope is a bounded vertical slice; long-term features do not automatically enter it.
10. No dependency cycle may be hidden by an implicit free item, unlock, NPC, facility or resource source.

## 3. Dependency layers

| Layer | Shared capability | Provides | Depends on |
|---|---|---|---|
| L0 | Project identity, manifest, stable IDs, schemas, version policy | Canonical project and component identity | None |
| L1 | World persistence, migration, event ledger, idempotency | Durable state and safe event processing | L0 |
| L2 | World clock, region registry, configuration, difficulty | Shared time, region and rules context | L0–L1 |
| L3 | Item/resource registry, inventory, transaction contracts | Item identity, quantity, quality, containers and transfers | L0–L2 |
| L4 | Actor, player, NPC and faction identity; permission/access model | Actors, ownership, roles and access decisions | L0–L3 |
| L5 | World geometry, structures, claims, interaction and navigation | Sites, blocks/structures, routes and interaction surfaces | L0–L4 |
| L6 | Core survival, combat, injury, zombie AI and encounter scheduling | Immediate playable threat/survival loop | L2–L5 |
| L7 | Crafting, loot, harvesting, food, water, medical and equipment | Player supply and recovery loops | L2–L6 |
| L8 | Power, water, sanitation, farming, ecology, weather and hazards | Environmental and utility simulation | L2–L7 |
| L9 | NPC needs/tasks, factions, settlement and economy | Persistent human community and trade | L2–L8 |
| L10 | Transport, logistics, factories, advanced research and regional simulation | Wider-world production and movement | L2–L9 |
| L11 | Campaign, quests, story, radio knowledge and endgame objectives | Player-facing long-term direction | L2–L10 |
| L12 | Target adapters, pack assembly, integration validation and evidence registry | Separate Java/Bedrock outputs and proof | All applicable layers |

Layers describe logical prerequisites, not mandatory separate services or a rigid runtime deployment architecture.

## 4. Feature-family dependency matrix

| Feature family | Authoritative owner | Core prerequisites | Main consumers / integrations | Status notes |
|---|---|---|---|---|
| Project manifest, stable IDs and schema registry | Project/manifest engine | L0 | All components and Studio workflows | Architecture specified; implementation not claimed |
| Save persistence, event ledger, migrations | Persistence layer | L0 | All persistent systems | Required foundation |
| World clock, day/night, seasons, weather | World time/weather | L1–L2 | Crops, NPC schedules, visibility, spoilage, power, hazards, encounters | Day/night and seasons requested; exact calendar open |
| Regions, biomes, world generation and expansion | World/region engine | L0–L2, target world capabilities | Ecology, resources, routes, settlements, exploration | Continuous hybrid world topology approved; technical limits require validation |
| Item registry, inventory, backpacks and containers | Item/inventory | L0–L3 | Loot, crafting, trade, storage, vehicles, medical | Backpack variety requested; detailed balance open |
| Loot and scavenging | Loot/inventory integration | Item registry, world sites, encounter state | Crafting, survival, economy, exploration | Loot system requested |
| Combat, weapons, ammunition, noise and durability | Combat/weapons | Actor identity, items, world time, zombie perception | Zombie AI, crafting, injuries, loot | Melee + firearms first-slice scope approved; noise YES, durability YES, limited ammo |
| 3D weapon models and customization | Weapon/asset pipeline | Weapon definitions, item variants, target asset adapters | Combat UI, inventory, manufacturing | 3D models and customization requested; asset details open |
| Zombie roster and AI | Zombie AI | Actor, navigation, perception, combat contracts | Encounter Director, injury, loot, settlement defense | Walker/Runner/Brute approved; exact values open |
| Horde and boss encounter scheduling | Encounter Director | World clock, region threat, zombie roster, event budget | Combat, settlement defense, radio warnings | Hordes and bosses requested; schedule/budget open |
| Injury, fracture, amputation and prosthetics | Medical/injury | Combat damage events, item registry, medical crafting | NPC dialogue, progression, research | Injury and complex bionic progression requested; medical balance open |
| Food, cooking, hunger and nutrition | Survival/food | Items, clock, fire/power, water | Farming, ecology, trade, NPC needs | Broad food scope requested |
| Thirst, drinks and potable water | Survival + water service | Item registry, water quality authority, clock | Player/NPC needs, farming, sanitation | Broad thirst/drink scope requested |
| Water collection, wells, treatment, tanks and pipes | Water infrastructure | World regions, item/resource, power, construction | Survival, farming, hygiene, sanitation, settlement | Explicitly approved |
| Showers, toilets, sewage and sanitation | Sanitation/water | Water network, structures, power where required | Disease, settlement needs, environmental hazards | Explicitly approved |
| Power generation, solar, wind, fuel and batteries | Power/fuel network | World weather, items, structures, clock | Water pumps, lighting, workshops, refrigeration, communications | Explicitly requested |
| Base construction, claiming and defenses | Base-building | Structures, claims, items, crafting, combat | Power, water, traps, NPCs, settlement | Free construction/claiming and defenses approved; detailed limits open |
| Traps, alarms and security systems | Defense/interaction | Items, power where applicable, threat perception | Zombie AI, NPC defense, base | Explicitly approved |
| Farming, crops, livestock and food storage | Farming | Clock/weather, water, soil/ecology, items, storage | Food, trade, NPC tasks, economy | Broad ecosystem scope; exact crop/animal content open |
| Ecology, wildlife, vegetation and habitats | Ecology | Regions, clock/weather, water, hazard events | Hunting, farming, resources, disease, zombie displacement | Integrated design documented; species roster open |
| Fire, flood, drought, disease and pollution | Hazard/disease services | World clock, region state, water/soil, structures | Ecology, settlement, infrastructure, survival | Fire/disease/outbreak events approved; rates open |
| Crafting and specialist workstations | Crafting/manufacturing | Item registry, recipes, skills, tools, power, station access | Weapons, medicine, vehicles, utilities, prosthetics | Vanilla Crafting Table must remain first tier; advanced benches later |
| NPC identity, dialogue, needs and professions | NPC simulation | Actor, clock, items, world knowledge, tasks | Settlement, quests, trade, research, defense | Survivor rescue, professions and routines approved; dialogue state-aware |
| Factions, relations, territory and diplomacy | Faction service | NPC/actor identity, economy, knowledge, world events | Trade, settlement, quests, transport, combat | Different factions/alliances/hostilities approved |
| Settlement management and population | Settlement service | NPC, base, water, power, food, sanitation, security | Economy, logistics, quests, regional simulation | Recruitment and settlement development approved |
| Trade, economy and scarcity | Economy service | Item transactions, stock summaries, factions, logistics | NPC, settlements, manufacturing, player progression | Trade/economy/scarcity approved; currency and price curves open |
| Vehicles and vehicle customization | Transport/vehicle | Items, manufacturing, fuel/power, routes, physics/capabilities | Exploration, logistics, settlement, mobile bases | Broad vehicle scope requested; exact roster open |
| Bicycles, trailers, buses and interiors | Transport/vehicle | Vehicle framework, structures/interior persistence, inventory | Mobile base, logistics, NPC passengers | Bicycle entry vehicle, attachable small trailer and usable bus interior requested |
| Convoys, trains, boats and helicopters | Transport/logistics | Vehicle framework, route graph, fuel, world regions | Factions, trade, exploration, rescue | Explicitly approved long-term transport scope; target feasibility open |
| Factory and advanced manufacturing | Manufacturing | Crafting, recipes, power, logistics, skills, NPC work | Vehicles, weapons, electronics, prosthetics | Factory vehicle production requested; detailed factory chain proposed |
| Research, laboratories and blueprints | Research | Evidence registry, items, NPC expertise, facility/power | Crafting, medical, story, advanced systems | Research/labs approved; exact unlock tree open |
| Radio, communication and knowledge | Communication/knowledge | Power, network/relay, faction/NPC knowledge, events | Quests, warning, diplomacy, exploration | Radio and communication approved |
| Quests, campaign and player progression | Quest/story/progression | Events from all relevant owners, knowledge, rewards | UI, NPC dialogue, research, faction, settlement | Long-term design proposed; campaign chapters/ending open |
| Map discovery and exploration | World knowledge/exploration | Region registry, navigation, evidence/knowledge | Radio, quests, trade routes, resources | Continuous world architecture approved |
| Multiplayer/co-op/server | Session/network layer | Actor ownership, authority, persistence, synchronization | All gameplay domains | Design proposal only; not first-playable commitment |
| Target-specific Java/Bedrock packaging | Target build adapters | Component manifest, toolchain, assets, scripts | Build, validation, delivery | Java/Bedrock separate artifacts and tests required |

## 5. Dependency graph: critical paths

The following graph describes logical direction. Arrows mean “must provide a stable contract before the dependent capability can be integrated,” not necessarily “must be fully feature-complete.”

### 5.1 Foundational persistence and identity
`Project/Manifest IDs → Versioned Schemas → Persistence/Event Ledger → World Clock/Region Registry → Domain Registries`

### 5.2 Immediate survival and combat
`Actor + Item Registry + World/Region + Clock → Loot/Inventory → Equipment → Combat → Injury Events → Medical Treatment`

`Zombie Roster + Navigation/Perception + Noise Events → Zombie AI`

`Zombie AI + Regional Threat Budget + Clock → Encounter Director → Horde/Boss Events → Combat/Defense`

### 5.3 Base and self-sufficiency
`Structures/Claims + Items + Crafting → Base Construction`

`Water Sources → Collection/Well → Treatment → Storage → Pipes/Pumps → Player/NPC/Farm Consumption`

`Weather → Solar/Wind Generation; Fuel → Generator → Battery/Network → Pumps/Lights/Workstations/Communications`

`Soil + Water + Seeds + Weather + Farming Jobs → Crop Growth → Harvest Items → Food Storage/Cooking → Consumption`

### 5.4 Community and regional economy
`NPC Identity + Needs + Skills + Tasks → Professions → Settlement Services`

`Item Transactions + Stock Ledgers + Faction Access + Route Logistics → Regional Trade/Economy`

`Settlement Demand + Production + Storage + Routes + Threat/Weather → Regional Resilience or Scarcity`

### 5.5 Advanced industry and progression
`Discovery/Evidence + Research Facility + NPC Expertise + Inputs → Research Result/Blueprint`

`Blueprint + Recipe + Station/Factory + Inputs + Power + Skilled Work → Manufactured Item/Vehicle/Prosthetic`

`Committed World Events + Player Knowledge + Faction/NPC State → Quest/Story Progression`

### 5.6 Target delivery
`Shared Feature Contract → Java Component Adapter → Java Build/Test Evidence`

`Shared Feature Contract → Bedrock Component Adapter → Bedrock Build/Test Evidence`

`Both Target Evidence Sets + Integration Audit → Parity Result → Target Bundles + Combined Project Export`

## 6. Critical circular-dependency hazards and resolutions

| Potential cycle | Why it is dangerous | Required resolution |
|---|---|---|
| Power requires fuel; fuel production requires powered factory | Player can be soft-locked without a bootstrap source | Preserve a basic non-powered/manual acquisition or production route; advanced scale may require power |
| Water pumps require power; power generation requires water | Utility deadlock | Define at least one bootstrap water source and one bootstrap power source; never require each other to start |
| Research requires advanced components; components require research unlock | Blueprint deadlock | Every critical recipe has an alternate salvage, trade, lower-tier or discovery path |
| NPC settlement needs food; farming requires NPC labor | Population starvation loop | Player/manual bootstrap farming and scavenging remain viable; NPC labor improves scale, not basic possibility |
| Vehicle requires factory; factory requires vehicle logistics | Manufacturing deadlock | Initial tools/hand transport and a basic workshop can bootstrap later industrial transport |
| Prosthetic requires laboratory; lab access requires a prosthetic | Medical progression deadlock | No required path may assume the player already has the treatment it unlocks |
| Faction access requires reputation; reputation requires faction-only missions | Social lock | Multiple reputation sources and non-faction essential survival routes |
| Quest reward is needed to complete the same quest | Reward cycle | Quest prerequisite graph validation rejects self-dependency; reward is committed only after objective completion |
| Resource generator outputs item; same item powers generator without loss | Infinite resource loop | Atomic input/output accounting, conversion loss/limits and machine capacity |
| Region expansion regenerates old resource nodes | Duplication/exploit | Stable IDs, persistent depletion state and versioned region migration |

## 7. First playable versus long-term feature boundary

The approved target platform baseline is Java 26.3 + Fabric and Bedrock 26.60 + stable Script API 2.11.0, with experimental APIs disabled. The selected first playable content is a mod/world bundle on both platforms, centered on a compact abandoned town and a zombie-invasion survival loop.

### First-playable candidates already grounded in user decisions
- Compact abandoned town with market, hospital and police station.
- Day/night cycle and core survival loop.
- Melee and firearm combat; weapon noise attracts zombies; durability; limited ammunition.
- Walker, Runner and Brute zombie types.
- Loot/scavenging and varied backpack system.
- Broad initial weapon, food, drink/thirst and equipment definitions as the user expects; exact item roster still needs mapping.
- Core injury/medical interaction only to the extent accepted in the vertical-slice specification and feasible on both targets.
- Vanilla Crafting Table remains the first crafting stage; specialist workstations are later progression.
- First defensible base interaction and a deliberately bounded water/power demonstration only if included in the approved vertical-slice manifest.

This is a candidate mapping, not a silent expansion of the first-playable approval. The exact feature IDs must be reconciled against `docs/FIRST_PLAYABLE_VERTICAL_SLICE_SPEC_V1.md` and the user decision register before scope is frozen.

### Long-term scope
- Full global ecosystem and regional resource cycles.
- Large settlement networks, factions, dynamic markets and distant population simulation.
- Full power/water/sewage networks and advanced automation.
- Extensive farming, livestock, seasons and ecological feedback.
- Factory-scale production, advanced prosthetics and complete vehicle roster.
- Trains, boats, helicopters, convoys and large transport networks.
- Full campaign, research tree, multiple endgame paths.
- Multiplayer/co-op and dedicated server operations.
- Advanced bosses and special infected beyond the approved initial roster.

Long-term scope remains part of the vision but must be separately sequenced and approved by milestone.

## 8. Feature traceability workflow

The 232-entry feature catalog and current traceability matrix remain the granular source of feature IDs. Each catalog item must be reviewed in this order:

1. **Applicability:** required, optional, excluded, or unresolved for this Zombie Invasion project.
2. **Requirement source:** user-confirmed request, approved decision, or design proposal.
3. **Subsystem owner:** exactly one authoritative owner.
4. **Shared contract:** canonical IDs, events, inputs, outputs, persistence and error behavior.
5. **Dependency IDs:** all prerequisites; no implicit dependencies.
6. **Target mapping:** Java component and Bedrock component separately, or documented not-applicable reason.
7. **Design status:** needs review, mapped, designed, awaiting approval, approved, blocked, not applicable.
8. **Implementation status:** not started, in progress, implemented, verified; evidence required for verified.
9. **Acceptance criteria:** observable pass/fail outcomes for each target.
10. **Evidence:** build logs, test reports, runtime captures and artifact hashes tied to manifest/component revisions.

Do not bulk-mark all 232 features designed or approved because this master map exists. Existing matrix status remains authoritative until each feature has been individually assessed.

## 9. Project manifest integration

For each manifest revision:
- One shared project requirement may map to multiple target-specific components.
- Components declare owner, stable component ID, dependencies, target IDs, configuration schema, asset references and acceptance criteria.
- Each component revision is pinned to the manifest revision used for planning/build.
- Java mod, Java datapack, Bedrock behavior pack, Bedrock resource pack and world/map outputs remain distinct component/artifact types.
- Java and Bedrock never share a build job or binary artifact.
- Integration engine validates references within each target bundle.
- Evidence registry stores independent target results.
- Combined export contains separate installable target bundles and shared source/spec references.

The manifest is the execution contract; this document is the human-readable dependency map. If they conflict, do not silently choose: raise a manifest revision and resolve the discrepancy before approval.

## 10. Implementation sequence proposal

This is a dependency-driven proposal, not an implementation commitment.

| Wave | Focus | Exit gate |
|---|---|---|
| W0 | Freeze design baseline; feature applicability/traceability; target toolchain verification | No unresolved critical architecture contradictions; feature IDs and owners reviewed |
| W1 | Manifest, schemas, stable IDs, persistence, event ledger and migration test harness | Create/load/migrate a minimal project/world state without duplication |
| W2 | Target adapters and minimal build pipelines for Java and Bedrock | Independent empty/minimal artifact builds and import checks |
| W3 | First shared gameplay loop: world clock, compact town, player, items, loot, basic zombie encounter and survival | Both targets pass identical scenario outcomes within documented differences |
| W4 | Combat depth, approved zombie roster, injury and first medical recovery loop | Damage/noise/durability/ammo/injury state persists and tests pass |
| W5 | Crafting progression, backpacks, food/drink and first base loop | Recipe, inventory, storage and save/load integrity pass |
| W6 | First infrastructure slice: water and/or power demonstration selected by approved manifest | Capacity, consumption, outage and persistence tests pass |
| W7 | NPC survivor and small settlement slice | NPC tasks, needs, dialogue facts and resource costs are state-correct |
| W8 | Faction, trade and regional logistics slice | Atomic trade, reputation, route interruption and scarcity tests pass |
| W9 | Ecology, seasons, wider transport, advanced manufacturing and research | Performance and distant simulation budgets pass |
| W10 | Full campaign, world expansion, multiplayer and advanced content | Separate product/milestone approval and target validation |

W3–W6 order may be adjusted only after reviewing the exact vertical-slice dependencies and toolchain constraints. Do not build all systems in parallel.

## 11. Required test gates

### Contract and data integrity
- Stable IDs and schema compatibility.
- No duplicate event processing.
- No negative stock, duplicate loot, duplicated reward or item creation.
- Atomic transaction rollback on invalid capacity/permissions.
- Migration backup and recovery.

### Gameplay logic
- Day/night transition and time-based systems share one clock.
- Combat noise and threat response are reproducible.
- Injury state and NPC dialogue agree with authoritative condition.
- Recipes require actual inputs, tools, stations and unlocks.
- Water and power capacity/consumption reconcile.
- NPC tasks consume real time/resources and respect skill/availability.
- Faction knowledge does not leak undiscovered world state.

### World simulation and performance
- Active/near/distant simulation preserves totals.
- Distant regions do not force-load chunks.
- Region activation/save/reload does not duplicate actors, resources or events.
- Entity/pathfinding/automation budgets are profiled on target hardware.

### Target-specific verification
- Java build/import/gameplay/save test.
- Bedrock pack validation/import/gameplay/save test using stable APIs only.
- Separate acceptance evidence and artifact hashes.
- Parity report identifies identical, adapted, limited and unsupported behaviors.

A test not run is recorded as not run, not passed.

## 12. Risks and mitigation

- **Scope explosion:** keep long-term inventory separate from first playable; freeze a revisioned slice.
- **Cross-system state duplication:** enforce ownership matrix and event contracts.
- **Java/Bedrock capability mismatch:** assess each feature early; use approved equivalent outcomes rather than assumed parity.
- **Performance overload:** active/near/distant tiers, caps and profiling gates.
- **Progression soft locks:** dependency-cycle detection and alternate acquisition paths.
- **Economy exploits:** atomic ledgers, stock conservation and bounded market curves.
- **Save corruption:** versioned migrations, backups and idempotent event replay.
- **Unverified implementation claims:** evidence registry and honest status vocabulary.
- **Content asset bottleneck:** asset pipeline and target-specific validation planned as separate dependency.
- **Campaign/first-slice confusion:** narrative and endgame remain optional long-term layers.

## 13. Open decisions that must not be guessed

- Exact first-playable feature IDs and frozen acceptance scenarios.
- Which of water, power, farming, NPC and base systems are in the initial vertical slice beyond the already selected scope.
- Exact item/weapon/backpack/food/drink/vehicle roster.
- Zombie health, damage, spawn and boss values.
- Day length, seasons, resource yields and spoilage rates.
- Recipe and workstation progression values.
- Java/Bedrock implementation feasibility for each feature ID.
- Test environments and minimum supported client/hardware profiles.
- Multiplayer scope and authority model.
- Which long-term feature waves receive priority after first playable.

## 14. Implementation boundary

This is a planning and architecture map only. It does not implement the mod, Studio engines, Java/Bedrock packs, world generation, assets, recipes, NPCs, AI, network systems or tests. All 232 catalog entries remain individually subject to traceability review; no blanket approval or implementation status is inferred.


## 15. Feature-level traceability gap report

The family-level map is supplemented by `docs/ZOMBIE_INVASION_FEATURE_TRACEABILITY_GAP_ASSESSMENT_V1.md`, based on the current 232-entry matrix. The assessment records 232/232 features as planned and requiring review, with 0 explicit dependency edges, 0 acceptance criteria marked defined, 0 test cases marked defined, and no Java/Bedrock/parity assessment for any entry.

The L0–L12 layers and family-level matrix in this document must not be mistaken for feature-level dependency closure. Each feature ID still requires applicability, requirement provenance, exact specification mapping, owner confirmation, dependency edges, target-specific acceptance criteria and evidence.


## 16. Foundation compatibility feature-level specification

The first 12 feature records in the Project Foundation and Compatibility inventory are expanded in `docs/ZOMBIE_INVASION_FOUNDATION_COMPATIBILITY_AND_TRACEABILITY_SPEC_V1.md`.

The specification defines REQ-BASE-001..012, 32 proposed dependency edges, 55 feature-specific acceptance criteria and 51 test cases. It maps the confirmed Java 26.3 + Fabric and Bedrock 26.60 + stable Script API 2.11.0 target profiles, while keeping runtime/toolchain verification and all implementation claims evidence-gated.

This closes a detailed design-documentation gap for BASE-001..BASE-012; it does not automatically advance the source matrix statuses. The matrix remains unchanged until its machine-readable edge vocabulary and target status semantics are formally validated. No implementation, build, load or gameplay test is claimed.
## 17. Foundation traceability matrix v1.2.0

## 18. QA, build and delivery feature mapping

A second traceability batch has been added in `docs/ZOMBIE_INVASION_QA_BUILD_AND_DELIVERY_TRACEABILITY_SPEC_V1.md`, covering QA-001..QA-018 and SHIP-001..SHIP-012.

The current matrix v1.2.0 now records:
- 42 mapped features (BASE 12 + QA 18 + SHIP 12).
- 190 features still requiring traceability review.
- 115 feature-specific acceptance criteria and 110 unique test case IDs.
- 95 proposed feature-to-feature dependency edges.
- A static topological check of the 232-node feature graph found no cycle in this revision.
- Java, Bedrock and parity remain `not_assessed` for all 232 features.
- All 232 implementation statuses remain `not_implemented_verified`; no runtime evidence was added.

The DAG check verifies only the recorded graph structure. It does not test generated code, Minecraft runtime behavior, target compatibility or actual builds. Dedicated-server and multiplayer test definitions remain future/conditional gates, not first-playable scope.


## 19. Player, item and crafting feature mapping

A third feature-mapping batch is recorded in `docs/ZOMBIE_INVASION_PLAYER_ITEMS_CRAFTING_TRACEABILITY_SPEC_V1.md`, covering PLY-001..PLY-014, ITEM-001..ITEM-016 and CRAFT-001..CRAFT-010.

Current matrix v1.2.0 state:
- 82 mapped features: BASE 12, QA 18, SHIP 12, PLY 14, ITEM 16 and CRAFT 10.
- 150 features remain in traceability review.
- 195 feature-specific acceptance criteria and 190 unique test case IDs are recorded.
- 161 proposed feature-to-feature dependency edges are recorded.
- The full 232-node graph passed a static topological cycle check in this revision.
- Java, Bedrock and parity remain `not_assessed` for all 232 features.
- All implementation statuses remain `not_implemented_verified`; no runtime/build/test evidence was created.

The mapping preserves unresolved decisions: death/restart policy, encumbrance, exact hunger/thirst rates, character creation scope, item/recipe quantities, loot weights and first-slice farming scope. The graph check validates only the declared dependency DAG; it does not validate gameplay or Minecraft APIs. The 40 features are mapped for design traceability, not all automatically included in the first playable milestone.


## 20. Combat, entity and NPC feature mapping

A fourth mapping batch is recorded in `docs/ZOMBIE_INVASION_COMBAT_ENTITY_NPC_TRACEABILITY_SPEC_V1.md`, covering COM-001..COM-012 and ENT-001..ENT-018.

Current matrix v1.2.0 state:
- 112 mapped features: BASE 12, QA 18, SHIP 12, PLY 14, ITEM 16, CRAFT 10, COM 12 and ENT 18.
- 120 features remain in traceability review.
- 255 feature-specific acceptance criteria and 250 unique test case IDs are recorded.
- 225 proposed feature-to-feature dependency edges are recorded.
- The full 232-node graph passed a static topological cycle check in this revision.
- Java, Bedrock and parity remain `not_assessed` for all 232 features.
- All implementation statuses remain `not_implemented_verified`; no build, import, runtime or gameplay evidence was created.

The mapping preserves scope boundaries: Walker/Runner/Brute and melee/firearms are approved first-slice decisions; explosives, PvP, exact boss roster, special zombie variants, multiplayer and dedicated-server support remain optional, unresolved or later-stage. NPC dialogue is required to read actual game state and must not invent injuries or diagnoses. The graph check validates only the recorded dependency structure.


## 21. World and structure feature mapping

A fifth mapping batch is recorded in `docs/ZOMBIE_INVASION_WORLD_STRUCTURE_TRACEABILITY_SPEC_V1.md`, covering WORLD-001..WORLD-017 and STRUCT-001..STRUCT-010.

Current matrix v1.2.0 state:
- 139 mapped features: BASE 12, QA 18, SHIP 12, PLY 14, ITEM 16, CRAFT 10, COM 12, ENT 18, WORLD 17 and STRUCT 10.
- 93 features remain in traceability review.
- 309 feature-specific acceptance criteria and 304 unique test case IDs are recorded.
- 277 proposed feature-to-feature dependency edges are recorded.
- The full 232-node graph passed a static topological cycle check in this revision.
- Java, Bedrock and parity remain `not_assessed` for all 232 features.
- All implementation statuses remain `not_implemented_verified`; no world generation, pack import, runtime or gameplay evidence was created.

The approved topology is a continuous regionally organized world with authored landmarks and deterministic procedural expansion. This does not prove that both editions expose equivalent runtime terrain-generation APIs. The design explicitly retains authored/prebuilt world bundles as a fallback, keeps first playable compact, and protects player-built/discovered state during expansion.


## 22. Complete feature-level dependency graph

The full 232-feature traceability pass is recorded in `catalogs/feature-traceability-matrix.v1.json` v1.3.0. All 232 feature IDs are now mapped to requirement IDs, feature-specific acceptance criteria and test case IDs.

Verified matrix totals:
- 232/232 features mapped for design traceability; 0 remain in `needs_traceability_review`.
- 495 acceptance criteria and 490 unique test case IDs.
- 486 proposed feature-to-feature dependency edges.
- All 232 feature nodes passed static graph validation: unique edge IDs, valid endpoints, no self-edges, unique acceptance/test IDs and a successful topological sort with no dependency cycle.
- Java coverage: 232 `not_assessed`; Bedrock coverage: 232 `not_assessed`; parity: 232 `not_assessed`.
- Implementation: all 232 remain `not_implemented_verified`; evidence records: 0.

This closes the feature-level design traceability gap, not implementation or compatibility. The 486 edges remain proposed, not approved. The test cases are specifications, not executed tests. Exact toolchains, target builds, imports, runtime gameplay and manual playtests are still required before any feature can advance to implemented/built/tested. The first playable scope remains separately bounded; long-term feature mapping does not put every feature into the first release.


## 23. Implementation readiness gate

The implementation gate is defined in `docs/ZOMBIE_INVASION_IMPLEMENTATION_READINESS_AND_CODE_ENTRY_GATE_V1.md`.

It records the current state as design traceability complete but not ready for full playable implementation. The remaining blockers are: (1) freeze exact first-playable feature IDs in a revisioned manifest; (2) revalidate/pin Fabric and Bedrock toolchains; (3) identify actual test runtimes/devices for both editions; (4) select local/cloud/hybrid build execution and sandbox workflow; and (5) resolve gameplay policies only if they are included in the first slice.

The document proposes W0–W7 for the first playable and W8–W9 for long-term expansions. It does not start source-code implementation or claim a playable mod. Existing user-approved targets and gameplay decisions remain unchanged.


## 24. Manifest v2 draft linkage

The draft manifest is `schemas/zombie-invasion.project-manifest.v2.draft.json`; its review and structural validation record is `docs/ZOMBIE_INVASION_PROJECT_MANIFEST_V2_DRAFT_REVIEW_V1.md`.

The draft has 18 project requirements, 9 proposed components, 8 unresolved component dependency edges, 14 target-specific validation plans and 8 planned deliverable definitions. It contains 84 candidate first-slice feature IDs, all present in the 232-feature catalog. The candidate list is explicitly `proposed_not_approved`; the manifest has no approval records or test evidence. Production remains blocked until the user approves the exact feature-ID scope and remaining implementation prerequisites.
