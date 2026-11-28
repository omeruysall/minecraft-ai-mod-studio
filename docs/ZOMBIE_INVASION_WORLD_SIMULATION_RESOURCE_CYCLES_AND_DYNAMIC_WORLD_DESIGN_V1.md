# Zombie Invasion — World Simulation, Resource Cycles and Dynamic World Design V1

**Status:** Long-term integrated world-simulation design; based on user-approved world, survival, ecology, infrastructure, faction, horde and economy requirements. Detailed rates and balancing remain open. Not implemented.
**Date:** 2026-11-28
**World baseline:** One continuous, regionally organized, hybrid-authored/procedural and incrementally expandable persistent world.
**Targets:** Java 26.3 + Fabric; Bedrock 26.60 + stable Script API 2.11.0 where required; experimental Bedrock APIs disabled.

## 1. Purpose

This specification defines how the world changes over time as one connected system. It joins resource production and extraction, scarcity, logistics, settlements, factions, player-built infrastructure, ecological recovery, weather and seasons, zombie pressure, outbreaks, research, trade and regional change.

It is not a promise to simulate every block, entity or resident continuously. The world must produce persistent, understandable consequences while remaining performant on both target editions. The first playable abandoned town remains a deliberately bounded slice; this document defines the long-term simulation architecture.

## 2. Core simulation principles

1. One persistent world state: durable changes survive save/reload and later content expansion.
2. Single ownership: each resource, population, transaction, clock and event has one authoritative owner.
3. Finite flows: extraction, production, consumption, spoilage, transfer and loss reconcile; resources are never duplicated by parallel systems.
4. Renewal with limits: renewable resources recover only under valid environmental and time conditions.
5. Consequences with counterplay: scarcity, hazards and horde pressure provide warning, information and meaningful player choices.
6. Regional relevance: local conditions matter; a resource-rich region does not make every other region equally supplied.
7. Simulation fidelity by distance: active areas receive detailed behavior; distant areas use deterministic summaries.
8. Player agency: the player can change regional outcomes through settlement, trade, protection, production, diplomacy, research and deliberate disruption.
9. No hidden omniscience: NPCs, factions and radio reports know only what they could plausibly observe or receive.
10. Edition parity by outcome: Java and Bedrock share data contracts and gameplay intent but use independently validated platform adapters.

## 3. Canonical world state hierarchy

The canonical hierarchy is:
- World: save identity, world clock, global rules, progression flags and global event ledger.
- Region: geography, climate, resource budgets, danger, population summaries, ownership influence and infrastructure links.
- Settlement/district: residents, faction influence, facilities, stock, demand, defenses and local services.
- Site/structure: stable ID, owner/claim, condition, access, storage, workstations and local network endpoints.
- Actor/asset: player, NPC, zombie, wildlife, vehicle, machine or portable container.
- Transaction/event: immutable identity, source, target, quantities, cause, time, lifecycle and outcome.

Every persistent region, settlement, site, resource node, faction, NPC, vehicle and major event uses a stable ID. Coordinates alone are not identity. Expansion or regeneration must not silently replace a player-built or discovered object.

## 4. Authoritative domain ownership

| Domain | Authoritative owner | Other systems interact through |
|---|---|---|
| World clock, day/night, season and weather snapshot | World time/weather service | Read-only snapshots and scheduled events |
| Region identity, biome and climate band | World/region service | Region queries and controlled region updates |
| Wild populations and natural resource patches | Ecology service | Harvest, migration and habitat events |
| Crops and claimed livestock | Farming/animal husbandry | Water, climate, item and task contracts |
| Water quantity, quality and sanitation streams | Water infrastructure | Consume, transfer, treat and contamination events |
| Power generation, storage and network state | Power network | Generation, charge, consume and fault requests |
| Fuel quantities and compatibility | Fuel/storage registry | Atomic transfer and consumption |
| Items, inventories and item quality | Item/inventory registry | Validated item transactions |
| Production recipes and workstation jobs | Crafting/manufacturing | Input reservation and output commit |
| NPC identity, needs, skills and tasks | NPC simulation | Work, trade, rescue and dialogue contracts |
| Faction identity, relations, territory influence and stock | Faction/economy service | Diplomacy, trade and conflict events |
| Regional markets and prices | Economy service | Atomic buy/sell and supply updates |
| Zombie individual AI | Zombie AI | Perception and bounded encounter commands |
| Horde event scheduling and threat budget | Encounter Director | One event request and resolution |
| Disease exposure and ordinary illness | Disease service | Exposure, diagnosis-state and treatment events |
| Fire, flood, drought and environmental damage | Environmental hazard service | Ignition, mitigation and damage events |
| Structures, claims, integrity and base defenses | Base-building service | Build, repair, breach and access contracts |
| Vehicles, routes and transport condition | Transport service | Fuel, cargo, passenger and route contracts |
| Research and blueprint unlocks | Research service | Evidence submission and unlock records |
| Story objectives and quest state | Quest/story service | Objective and evidence events |
| Persistence, migrations and event deduplication | World persistence layer | Versioned snapshots and idempotent event commits |

A service may publish facts but may not directly overwrite another service's authoritative state.

## 5. World clock and simulation calendar

The world clock is authoritative and shared. It provides:
- Continuous game time with configurable day length.
- Day/night phase and sunrise/sunset boundaries.
- Calendar day, week and season.
- Weather state and forecast confidence.
- Scheduled regional events and NPC work periods.
- Save-safe clock progression and pause/single-player behavior.

Time scaling must be consistent: a crafting job, crop stage, fuel consumption, NPC schedule and spoilage process must not each invent separate clocks. Systems register time-based work against the shared clock or receive explicit elapsed-time budgets.

The exact real-time-to-game-time ratio, calendar length and season duration are balance decisions still open.

## 6. Regional state vector

Each region maintains a compact state vector, with detailed values selected by the relevant subsystem:
- Biome/habitat and climate band.
- Temperature, precipitation, wind and current weather category.
- Soil moisture/fertility and water availability summary.
- Wild population and vegetation/resource summaries.
- Renewable and non-renewable resource availability.
- Human population, settlement capacity and faction influence.
- Food, clean water, medicine, fuel, ammunition and construction-material stock summaries.
- Power and water infrastructure coverage/reliability.
- Zombie activity, known horde pressure and outbreak history.
- Environmental hazards: fire, flood, drought, pollution and disease alerts.
- Roads, rail, ports, air access and route condition.
- Discovery/knowledge confidence and last simulation timestamp.

Summaries are derived from their authoritative owners and must not become competing inventories.

## 7. Resource taxonomy and finite-flow accounting

Every resource definition specifies:
- Stable item/resource ID and category.
- Source class: renewable, conditionally renewable, finite, manufactured or recovered.
- Units and stack/container rules.
- Quality/condition and contamination where relevant.
- Extraction method, tool/station requirements and yield limits.
- Regeneration or replenishment rules, if any.
- Storage constraints, spoilage/degradation and hazard class.
- Crafting, construction, food, medical, energy or trade uses.
- Region/biome availability and rarity band.
- Provenance and transaction history where needed.

Resource accounting follows:

**Closing stock = opening stock + valid production + imports + recovery − consumption − exports − spoilage − damage/loss.**

The equation is a reconciliation rule, not a user-facing requirement to show every calculation. Negative stock is invalid. A transaction either commits fully or does not commit.

## 8. Resource source and renewal cycles

### 8.1 Natural resources
Timber, plants, forage, stone, ores, fish, wildlife and surface water originate from region-specific resource nodes or populations. Harvesting reduces the relevant source. Regrowth, migration or replenishment follows ecology rules and environmental suitability.

### 8.2 Renewable resources
Solar, wind, rainfall, crop production and biological regrowth are renewable but variable and capacity-limited. Generation depends on conditions and infrastructure; it is not an infinite item generator.

### 8.3 Finite resources
Scavenged canned food, ammunition, medicine, spare parts, refined fuel, industrial components and abandoned stockpiles are finite at a given site. They may be redistributed, manufactured or recovered only through defined processes.

### 8.4 Manufactured resources
Manufacturing converts reserved inputs, power/fuel, labor, tools, recipes and machine capacity into outputs. Jobs have duration, output quality, waste/by-products and interruption state. No finished high-tier item appears merely because a blueprint is unlocked.

### 8.5 Recovered resources
Dismantling, recycling, salvage and repair recover only a documented fraction of usable materials. Recovery depends on tool, skill, damage, contamination and station. The same object cannot be dismantled twice.

## 9. Production, consumption and demand

Demand is generated by actual consumers and activities:
- Player hunger, thirst, medical needs, equipment and crafting.
- NPC population, professions, hygiene, shelter and medical needs.
- Livestock feed and water.
- Crops and greenhouses.
- Vehicles, generators and machinery.
- Settlement defenses, lighting, communications and workshops.
- Construction, repair, research and manufacturing.
- Trade caravans, convoys and faction logistics.

Each consumer submits a bounded request. Criticality/priority is configurable by context; for example, a settlement may prioritize drinking water and medical refrigeration over decorative lighting. Power and water networks expose allocation results and shortages instead of silently granting full service.

## 10. Supply chains and logistics

A supply chain is a sequence of production, storage, transport and consumption nodes. Examples:
- Farm → silo/cold storage → truck/rail/boat → market → settlement inventory.
- Well/rain collector → treatment → cistern → pipe network → residents.
- Scrap/ore → workshop/factory → components → vehicle or weapon assembly.
- Fuel depot → tanker/container → settlement tank → generator/vehicle.
- Research evidence → laboratory analysis → blueprint unlock → manufacturing recipe.

Each logistics route defines capacity, travel time, access, risk, fuel/energy cost, condition, ownership and interruption behavior. Routes may be blocked by weather, damage, faction conflict, hordes or missing infrastructure. Lost cargo is recorded once and can be recovered if the game rules allow it.

## 11. Storage, spoilage and inventory integrity

Storage is a finite capacity with item compatibility, condition and environmental properties. Cold storage, dry storage, sealed containers, fuel tanks, ammunition lockers, medical cabinets and water cisterns have different constraints.

Food spoilage depends on food type, time, temperature, packaging, contamination and storage. Medicines and chemicals may degrade under specified conditions. Fuel may leak from damaged containers. Batteries lose condition according to documented rules. These are item/service state transitions, not random deletion.

The UI should show useful states: fresh/usable/aging/spoiled, potable/untreated/contaminated, full/partial/empty, safe/damaged/leaking. Exact shelf lives and degradation rates remain open balance data.

## 12. Scarcity and regional economy

Scarcity emerges from finite stock, demand, production limits, transport access and risk—not from arbitrary global price multipliers alone.

Regional market price may consider:
- Local stock and recent supply/demand.
- Item rarity and substitution options.
- Settlement population and urgent needs.
- Route safety, distance and transport capacity.
- Faction control, taxes, reputation and embargoes.
- Season, weather and outbreak damage.
- Recent transactions, with smoothing and configured price bounds.

Markets must not create infinite buy/sell arbitrage. A trade is atomic: validate stock, funds/barter, capacity, permissions and price; then commit both sides exactly once. NPC merchants and faction depots use the same economy ledger.

The exact currency/barter model, price curves and price limits remain design/balance decisions.

## 13. Settlements and population dynamics

A settlement tracks residents, shelter capacity, food/water/medical demand, sanitation, power, security, morale, jobs, faction influence and known threats.

Population changes only through explicit events such as rescue, recruitment, departure, death or relocation. No population is silently added to balance a shortage. NPCs can be assigned professions and tasks; their productivity depends on skill, tools, health, morale, safety, workstation and available inputs.

Settlement service levels can be summarized as:
- Stable: essential needs and defenses meet configured thresholds.
- Strained: one or more needs are under pressure.
- Critical: essential services or security are failing.
- Abandoned/overrun: no functioning resident community remains, subject to story rules.

These labels are presentation states derived from data, not independent world variables.

## 14. Factions, territory and diplomacy

Factions maintain identity, leadership, membership, territory influence, resources, policies, reputation and known relationships. Territory control is influence and access data, not an assumption that every block has a separate ownership entity.

Faction behavior may include:
- Trade, aid, recruitment and shared missions.
- Alliances, neutral relations, rivalry and hostility.
- Patrols, checkpoints, tolls and protected routes.
- Resource claims, disputes and embargoes.
- Raids, defense and settlement evacuation.
- Information sharing or misinformation based on faction knowledge.

Relations change only from recorded actions and events. A faction cannot react to hidden player actions it has not learned about. Diplomacy, combat and trade all write to the same faction/economy records.

## 15. Zombie outbreak and regional threat evolution

The outbreak is a world threat layer, not an unrestricted global zombie counter. Regional threat can be influenced by:
- Initial outbreak seed and authored story conditions.
- Noise, gunfire, alarms, generators and light.
- Population density and active settlement activity.
- Migration corridors and explicit world events.
- Player-cleared zones, barricades, lures and controlled routes.
- Horde events scheduled by the Encounter Director.

The Encounter Director owns event budgets, warnings, target regions and resolution. Zombie AI owns individual behavior. Regional threat summaries may rise or fall from recorded migrations, losses and event outcomes. No duplicate siege or unbounded remote spawning is allowed.

Bosses and special infected belong to the approved content roster/encounter configuration; exact spawn rules and regional propagation are open.

## 16. Environmental feedback loops

World systems form explicit feedback loops:
- Deforestation changes habitat and may alter local wildlife/soil stability.
- Overhunting reduces local populations and future hunting yield.
- Poor waste handling can contaminate water or attract scavengers only through defined rules.
- Fire damages vegetation, structures and stored goods; regrowth follows ecology rules.
- Drought reduces water availability, crop yield and some wildlife suitability.
- Floods damage routes, basements, crops and utility networks.
- Pollution affects specified water/soil/air states; treatment and cleanup can restore them.
- Storms affect travel, power generation, exposed structures and visibility.
- Zombie pressure can displace survivors and wildlife, damage infrastructure and interrupt supply chains.

Each loop must have a visible cause, bounded effect, countermeasure and persistence rule. Avoid cascading total-world collapse from one local event.

## 17. Infrastructure as a regional service layer

Power, water, sanitation, roads, rail, ports, communications and production facilities connect sites into regional networks. A network has nodes, edges, capacity, condition, access and service status.

Network rules:
- Bounded graph evaluation, not continuous simulation of every connecting block.
- Stable endpoint and edge IDs.
- Explicit ownership and permissions.
- Capacity and flow limits.
- Damage/isolation/repair events.
- Manual fallback where the design specifies it.
- Power and water dependencies must avoid circular deadlocks.
- Remote regions use abstract service availability until activated.

A base or settlement may connect to regional infrastructure only after discovering, repairing, powering and securing the relevant link.

## 18. Player agency and world-state consequences

Player actions can:
- Harvest, farm, hunt, fish, craft, manufacture and recycle.
- Build/claim/repair bases and infrastructure.
- Protect or damage habitats and supply routes.
- Rescue, recruit, assign and trade with survivors.
- Negotiate with or oppose factions.
- Clear, redirect or provoke zombie threats.
- Research, discover and publish information through radio.
- Establish trade routes, convoys and mobile bases.
- Restore abandoned sites or allow them to collapse.

Consequences must be attributable to an action/event record. The player should be able to inspect important regional changes through maps, radio reports, NPC dialogue, site state and settlement dashboards.

## 19. Information, radio and world knowledge

The world state and the player's knowledge state are separate. A region may contain a resource cache or horde that the player has not discovered. Information can arrive through direct exploration, survivors, maps, radio transmissions, research, faction contacts or observation.

Reports include source, timestamp, confidence, age and known limitations. NPC dialogue uses only facts available to that NPC or faction. A radio operator cannot report a remote event unless a signal, scout, relay or story mechanism delivered it.

## 20. Simulation scheduler and fidelity tiers

### Active region
- Full nearby entity behavior for player-visible actors.
- Detailed combat, interaction, local network state and critical hazards.
- Strict caps on entities, pathfinding, fire propagation and automation.

### Near region
- Reduced-frequency NPC, wildlife, production, horde and route updates.
- Event-driven movement and work completion.
- No unnecessary entity ticking outside relevant chunks.

### Distant region
- Compact deterministic population/resource/settlement summaries.
- Production and consumption aggregated over elapsed time.
- Scheduled event resolution with bounded work.
- No forced chunk loading and no individual pathfinding.
- On activation, materialize only the entities and effects justified by the summary.

Transition between tiers must conserve quantities and preserve event order. Save/reload and region activation must not duplicate output, population, loot or damage.

## 21. Persistence, save integrity and expansion

Persist:
- World clock and calendar.
- Stable region/site/entity IDs.
- Resource stock and source depletion/regrowth state.
- Inventory, storage and manufacturing jobs.
- NPC population, needs, tasks and location summaries.
- Faction relations, stock and territory influence.
- Infrastructure topology and condition.
- Horde/world event lifecycle and event IDs.
- Environmental hazard and disease states.
- Discovery, ownership, quests, research and player construction.
- Simulation timestamps and migration versions.

On load, reconcile only from authoritative snapshots and uncommitted event journals. Event processing must be idempotent. Schema migrations must be versioned, reversible where practical, and backed by a save backup. Adding a new region must not regenerate or overwrite existing persistent regions.

## 22. Shared event and transaction contract

Every durable event should include:
- event_id, event_type and schema_version.
- world_id, region_id, optional site_id and actor references.
- occurred_at, processed_at and source subsystem.
- Cause, input references and bounded payload.
- Lifecycle/status and result references.
- Idempotency key and correlation ID where applicable.

Resource transactions additionally include resource ID, quantity, source, destination, quality, unit, reservation and commit status. A transaction must be rejected if it would create negative stock, exceed capacity, violate access rules or consume an incompatible resource.

Events are facts after commit; commands are requests before validation. Consumers must not reinterpret a committed fact as permission to repeat its side effects.

## 23. Java and Bedrock implementation contract

The shared manifest defines gameplay systems, dependencies, IDs, configuration, assets and acceptance criteria. Java Fabric and Bedrock stable Script API implementations use separate adapters and capability declarations.

- Shared simulation rules and schemas are platform-neutral where possible.
- Java implementation may use Fabric-native capabilities and appropriate data/world assets.
- Bedrock implementation must stay within the stable API target; experimental APIs remain disabled.
- If an equivalent outcome cannot be implemented on one edition, record the exact limitation and propose a constrained alternative for approval.
- Do not label parity complete because the same feature name exists in both packs.
- Build/import, save persistence, reload and gameplay tests are independent per edition.

## 24. First playable boundary

This world-scale architecture does not add all systems to the first playable milestone. The first playable remains a compact abandoned town and the explicitly approved core features. The full regional economy, distant settlement simulation, faction logistics, large transport network, world-scale outbreak evolution and detailed ecological feedback are staged long-term work.

A feature enters a milestone only after its dependency graph, Java/Bedrock capability, test environment, performance budget and acceptance criteria are defined and approved.

## 25. Acceptance criteria

The architecture is ready for implementation planning only when:
1. Each persistent state has one authoritative owner.
2. Every resource has a source class, unit, capacity and accounting rule.
3. Production, consumption, transfer, spoilage and loss reconcile without duplication.
4. Regional stock and demand can differ and change through recorded events.
5. Supply chains have capacity, route, cost, risk and interruption behavior.
6. Market transactions are atomic and cannot create arbitrage loops or negative stock.
7. Settlement population and needs change only through explicit events.
8. Faction knowledge and reactions respect information boundaries.
9. Horde pressure is bounded and owned by the Encounter Director.
10. Environmental feedback has clear causes, countermeasures and limits.
11. Active/near/distant simulation conserves state and avoids distant chunk loading.
12. Save/reload, region activation and migration do not duplicate transactions or events.
13. Java and Bedrock have separate capability and acceptance evidence.
14. The first playable scope remains protected from automatic expansion.

## 26. Open design and balance register

The following are intentionally not silently decided:
- Exact calendar scale, day length and season duration.
- Resource units, yields, regeneration rates and regional abundance.
- Item shelf lives, spoilage curves and storage multipliers.
- NPC consumption, work output, population growth and settlement thresholds.
- Market currency/barter rules, price curves, caps and faction taxation.
- Supply-route speed, cargo capacity, fuel costs and loss probabilities.
- Regional outbreak spread, horde budgets, boss conditions and recovery rates.
- Distant simulation interval and per-region CPU/entity budgets.
- Which world-scale loops enter each milestone after the first playable.
- Exact Java/Bedrock implementation feasibility for every network and simulation feature.

These values require a balance pass and target-edition profiling; this document does not claim they have been tested.

## 27. Implementation boundary

This is a design specification and integration contract only. It does not create game code, world files, entities, items, assets, recipes, AI, maps or playable builds. No runtime, performance, save-migration or cross-edition test is claimed.
