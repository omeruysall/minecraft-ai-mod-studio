# Zombie Invasion — World, Map, Biomes and Exploration Design v1.0

**Status:** Long-term world architecture approved by user; first playable map remains separately scoped  
**Decision date:** 2026-11-28  
**Design principle:** One persistent, expandable survival world with staged regions and edition-specific implementations

## 1. Vision and scope

The world should feel like a large region affected by a systemic outbreak, not a collection of disconnected arenas. Settlements, wilderness, infrastructure, transport corridors, weather, seasons, resources, factions, wildlife and zombie activity should form one connected simulation.

The existing abandoned expandable town remains the first playable map. This document defines the long-term world architecture and expansion vocabulary; it does not silently enlarge the first playable milestone.

The design supports:
- Authored, handcrafted regions for important story and gameplay locations.
- Procedurally assembled or generated terrain and secondary settlements where technically feasible.
- Hand-authored points of interest placed into generated or authored regions.
- Discoverable routes, secrets, facilities and resource zones.
- Persistent changes caused by player activity and world events.
- Separate Java and Bedrock implementation tracks with equivalent gameplay intent, not identical internal files.

## 2. World structure

Use a layered world model:

1. **World:** the complete save and its global rules.
2. **Region:** a broad geographic and simulation partition.
3. **District / settlement:** city quarter, town, village, industrial zone or facility.
4. **Site:** a building, compound, cave, bunker, station or landmark.
5. **Interior / sublevel:** rooms, floors, basements, tunnels and underground spaces.
6. **Encounter and resource zones:** bounded areas used by spawning, loot, events and simulation.

Every persistent site receives a stable identifier in the shared project manifest. Region boundaries must not create duplicate ownership, loot, NPCs or resource nodes.

## 3. Geographic region catalogue

The following are proposed long-term region families. They are not all required in the first playable slice.

### A. Urban regions
- Dense metropolitan centre with high-rise buildings.
- Residential neighbourhoods and apartment blocks.
- Commercial streets, shopping centres and markets.
- Industrial districts, warehouses and factories.
- Civic districts, offices and public buildings.
- Suburbs and outer-ring roads.

Gameplay identity: dense loot opportunities, vertical exploration, blocked streets, high encounter density, rooftop routes and difficult evacuation.

### B. Small towns and villages
- Small rural towns.
- Villages with houses, farms and workshops.
- Remote hamlets and roadside settlements.
- Abandoned settlements with varying outbreak histories.

Gameplay identity: lower density but fewer guaranteed supplies, local survivor stories, farms, wells, workshops and faction control.

### C. Agricultural regions
- Crop fields, greenhouses and orchards.
- Livestock farms and barns.
- Irrigation channels, silos and food-processing sites.
- Rural depots and agricultural machinery.

Gameplay identity: food production, seeds, animal care, seasonal yields, water requirements and exposed travel.

### D. Forest and wilderness
- Dense forests, woodland, clearings and logging camps.
- Mountain forests and highland routes.
- Hunting cabins, ranger stations and fire-watch towers.
- Wildlife habitats and remote campsites.

Gameplay identity: hunting, gathering, timber, navigation risk, wildlife encounters, weather exposure and low infrastructure density.

### E. Mountain and underground regions
- Mountain passes, cliffs and valleys.
- Mines, quarries and tunnels.
- Caves, underground rivers and natural shelters.
- Research bunkers and concealed underground complexes.

Gameplay identity: rare minerals, difficult traversal, temperature/exposure risks where enabled, limited exits and high-value discoveries.

### F. Water and coastal regions
- Rivers, lakes, reservoirs and wetlands.
- Coastlines, beaches and islands.
- Fishing settlements and marinas.
- Ports, docks, shipyards and coastal industrial sites.

Gameplay identity: fishing, water collection/treatment, boat transport, island isolation, storms and maritime supply routes.

### G. Transport and logistics corridors
- Highways, bridges, tunnels and road checkpoints.
- Railway lines, stations, yards and depots.
- Airports, airfields and helicopter landing zones.
- Ports, ferry terminals and cargo facilities.

Gameplay identity: convoy travel, repair/recovery, fuel logistics, blocked routes and contested infrastructure.

### H. Restricted and high-risk zones
- Military bases and forward operating posts.
- Quarantine perimeters and evacuation camps.
- Bio-research laboratories and outbreak facilities.
- Power stations, water-treatment plants and fuel depots.
- Secure prisons and emergency command centres.

Gameplay identity: high threat, controlled access, rare equipment, story evidence, specialist crafting resources and faction conflict.

## 4. First playable map boundary

The first playable map remains the compact authored abandoned town already defined in `ZOMBIE_INVASION_MAP_DESIGN_V1.md`.

Its required functional locations remain:
- Safehouse.
- Residential section.
- Market.
- Hospital.
- Police Station.
- Two validated zombie approach lanes.

The broader world catalogue does not add cities, airports, ports, trains, aircraft, full procedural generation or large-scale region simulation to the first playable milestone. These are staged expansions.

## 5. Points of interest and building interiors

Every point of interest (POI) must have a gameplay purpose, access model and test definition.

POI categories:
- Residential: houses, apartments, shelters and communal buildings.
- Medical: clinics, hospitals, pharmacies and laboratories.
- Security: police stations, checkpoints, prisons and armories.
- Supply: markets, warehouses, shops and depots.
- Industry: factories, workshops, power plants and refineries.
- Research: laboratories, archives and secure facilities.
- Transport: stations, terminals, garages, hangars, ports and depots.
- Community: schools, town halls, hotels and places of gathering.
- Wilderness: cabins, camps, caves, towers and hunting sites.

Interior design rules:
- Use readable floor plans and navigation landmarks.
- Provide multiple entry/exit routes where appropriate, but do not make every building trivially safe.
- Mark locked, blocked, breached and player-opened access states consistently.
- Support searchable containers, doors, power, lighting, alarms and relevant workstation interactions.
- Avoid empty decorative interiors that add performance cost without gameplay value.
- Large structures may use staged loading or bounded active interiors where supported by the target edition.

## 6. Procedural generation and authored content

Recommended hybrid model:

**Authored content**
- Main story locations.
- First playable town and its required buildings.
- Critical quest locations and progression gates.
- Unique laboratories, bunkers and major landmarks.

**Procedural or rule-based content**
- Secondary houses and small settlements.
- Loot distribution within approved tables.
- Minor roadblocks, abandoned vehicles and environmental details.
- Resource-node placement and selected wilderness points of interest.
- Optional encounter sites.

Generation must be seeded and reproducible for tests. A generated location must satisfy accessibility, navigation, loot, spawn-safety and performance constraints. Critical quest items and required progression must never depend on an unverified random placement.

Do not promise infinite terrain or seamless world generation until both target editions have been technically validated. Use bounded regions or staged expansion if that is the reliable cross-edition approach.

## 7. Discovery, navigation and mapping

Proposed navigation progression:
- Start with a basic paper map or limited local orientation.
- Discover roads, landmarks and settlements through exploration.
- Use signposts, road signs, towers, radio reports and survivor information.
- Unlock more detailed map information through maps, radios, terminals or NPC knowledge.
- Record visited locations and known hazards in the player's journal/map interface where supported.

Navigation must not require a custom minimap. Optional map UI may be added later, but world readability must work through landmarks, signage and route design.

Map information has states such as UNKNOWN, RUMOURED, DISCOVERED, VISITED and VERIFIED. Rumours may be incomplete; verified information must be backed by an actual world location or recorded event.

## 8. World time, weather and seasons

The user has requested a day/night cycle and seasons. These must be treated as world-level systems, not isolated visual effects.

Design responsibilities:
- A single authoritative world clock.
- Consistent day, dusk, night and dawn phases.
- Seasonal calendar and region-aware season presentation.
- Weather states such as clear, rain, storm, fog and snow where region/climate permits.
- Effects on visibility, travel, farming, water collection, power generation, fires, wildlife and zombie encounters.
- Indoor/outdoor shelter and lighting interactions.
- Clear configuration of time progression and scenario-specific overrides.

The first playable scenario may use a controlled time schedule for repeatability. Exact day length, season length, climate zones and weather probabilities remain open decisions.

## 9. Outbreak history and regional danger

Regions should communicate outbreak history through evidence:
- Evacuation routes and abandoned convoys.
- Quarantine barriers and warning signs.
- Emergency broadcasts and local radio logs.
- Barricades, improvised camps and failed defences.
- Infected hotspots and traces of previous hordes.
- Faction-controlled or contested locations.

A regional danger model may combine zombie activity, horde migration, recent noise, population density, weather and faction activity. It must use bounded updates and must not require every distant entity to run full AI continuously.

## 10. Regional persistence and simulation

Persistent world facts include:
- Site ownership/claim state.
- Loot container state and respawn policy.
- Player-built structures and damage.
- Power, water and fuel infrastructure.
- NPC identity, profession, schedule and current assignment.
- Faction presence and relations.
- Horde movement and regional threat summaries.
- Fire, disease and ecology state.
- Discovered map knowledge and quest state.

Use region-level summaries for distant simulation. Full entity AI should run only in active or nearby areas; distant regions use deterministic or aggregated state transitions. Re-entry must reconcile the summary with the active simulation without duplicating entities or resources.

## 11. Dynamic world events

Potential events include:
- Horde migration across roads or settlements.
- A settlement distress call.
- A convoy ambush or abandoned convoy discovery.
- Fire in a building or forest.
- Severe weather disrupting a route.
- Water/power infrastructure failure.
- Faction patrols, clashes or trade visits.
- Survivor rescue opportunities.
- Radio reports revealing a temporary point of interest.

Events must have prerequisites, region scope, duration, consequences and a stable event ID. They must not overwrite player-built assets or critical quest progress without an explicit rule.

## 12. Transport integration

The world layout must reserve meaningful corridors and access points for the previously requested transport systems:
- Bicycle and small bicycle trailer/pod.
- Cars, trucks, buses and larger road vehicles.
- Convoys and road logistics.
- Trains and railway infrastructure.
- Boats and coastal/inland water routes.
- Helicopters and suitable landing areas.

Vehicles must obey route width, bridge/load limits where modelled, fuel/energy needs, repair access and storage constraints. A bus interior may act as a mobile living space as already requested. Do not make every route accessible to every vehicle.

## 13. Resource and loot geography

Resource distribution should follow location identity:
- Markets and homes: food, household goods and common supplies.
- Hospitals and clinics: medical supplies.
- Police/security sites: tactical and defence supplies.
- Farms: crops, seeds, animal products and agricultural tools.
- Factories/workshops: components, tools and manufacturing materials.
- Fuel depots/gas stations: fuel and transfer equipment.
- Power/water facilities: infrastructure components.
- Wilderness: timber, stone, plants, hunting and fishing resources.
- Research/military sites: rare specialist components and story evidence.

High-value loot should carry access, danger, transport or faction consequences. Avoid a single universally optimal loot location.

## 14. Java and Bedrock parity

The shared world manifest should define logical region, POI, route, loot, event and progression identifiers. Java and Bedrock adapters may use different structure formats, scripting, block/entity representations and asset pipelines.

Parity is assessed by:
- Same intended gameplay purpose.
- Equivalent progression access.
- Equivalent critical loot/reward function.
- Equivalent event and encounter outcomes within platform constraints.
- Equivalent persistence expectations.
- Independently recorded load, gameplay and performance evidence.

Do not label a feature as cross-edition complete merely because the documentation or shared manifest exists.

## 15. Performance, safety and validation

- Bound active regions and entity counts.
- Avoid expensive global scans and per-tick world-wide searches.
- Use stable POI and region IDs.
- Keep procedural generation deterministic under a recorded seed.
- Ensure critical locations cannot spawn inside inaccessible terrain.
- Ensure zombies cannot spawn inside protected player/safehouse volumes.
- Validate chunk/region transitions and save/load boundaries.
- Test player-built structures and claimed buildings against reset rules.
- Measure Java and Bedrock performance independently on named environments.
- Provide fallback behavior when a target edition lacks an equivalent API.

## 16. Acceptance criteria for future world expansion

A region is not considered complete until:
1. It has a stable identifier and explicit gameplay purpose.
2. Its boundaries, routes and points of interest are documented.
3. Its navigation and accessibility have been tested.
4. Loot and resource placement follows the region's identity.
5. Spawn and encounter zones respect safety constraints.
6. Persistent state survives save/load without duplication.
7. Dynamic events reconcile correctly after leaving and re-entering.
8. Transport access and restrictions are documented.
9. Java and Bedrock evidence is recorded independently.
10. Performance remains within an explicitly measured budget.

## 17. User-approved world topology and generation model (2026-11-28)

**Decision: Combine all three proposed world models into one layered architecture.**

The long-term target is a **large, continuous, regionally organized and incrementally expandable open world**:

- **Continuous open world:** normal exploration should not be divided into disconnected arena-style maps or unnecessary loading-screen transitions. Technical constraints may require bounded simulation or staged asset/region activation, but these must preserve the player's sense of one connected world.
- **Connected regional structure:** the world is partitioned logically into distinct regions, districts, settlements, wilderness areas, transport corridors and points of interest. These are organizational and simulation boundaries, not necessarily separate playable instances.
- **Hybrid authored/procedural generation:** major cities, story locations, unique facilities and critical progression sites are authored and validated. Secondary settlements, selected buildings, road events, resource nodes and optional discovery sites may be generated by deterministic rules.
- **Incremental expansion:** new regions, districts, settlements and content packs can be added to an existing world without invalidating stable IDs, player-built structures, discovered locations or saved progression.

All region families catalogued in this document remain in the long-term design scope. This decision does not require every region to exist in the first playable slice. The compact abandoned town remains the first playable map.

Implementation must validate world-size, chunk-loading, persistence, procedural-generation and Java/Bedrock constraints before claiming a technically infinite or fully seamless world. If a platform requires staged activation or bounded simulation, that is an implementation detail; it must not silently turn the intended world into unrelated disconnected maps.

The following decisions remain open:
- Whether weather and seasons affect gameplay numerically from the first expansion or are initially mostly environmental.
- Whether map knowledge is shared with recruited survivors/factions.
- Whether regions can be permanently lost, reclaimed or dynamically change control.
- Whether expansion is delivered as one large release or separate region packs.

## 18. Implementation boundary

This is a design specification only. It does not generate terrain, structures, worlds, scripts, mods, maps or playable files. No implementation or runtime test is claimed. The first playable coding gate remains governed by the master design baseline and first-slice decision register.
