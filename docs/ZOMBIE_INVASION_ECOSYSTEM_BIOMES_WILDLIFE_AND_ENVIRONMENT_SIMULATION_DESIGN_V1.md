# Zombie Invasion — Ecosystem, Biomes, Wildlife and Environmental Simulation Design V1

**Status:** Long-term ecosystem architecture; wildlife/ecology scope was user-approved; detailed mechanics and balance are design specifications, not implementation.
**Date:** 2026-11-28
**World baseline:** Continuous, regionally organized, hybrid-authored/procedural, incrementally expandable world.
**Platform targets:** Java 26.3 + Fabric; Bedrock 26.60 + stable Script API 2.11.0 where needed; experimental Bedrock APIs disabled.

## 1. Purpose and design principles

This document defines one coherent ecosystem rather than independent animal, crop, weather and hunting features. Every living population and natural resource belongs to a region and habitat, has explicit state, and interacts through bounded, auditable events.

Principles:
- A living world: animals, plants, crops, water, soil, weather, seasons, disease, fire, zombies and survivors influence one another.
- Gameplay readability: important risks and changes have discoverable signs, not hidden arbitrary penalties.
- Persistence: harvesting, fires, migration, disease outbreaks and player construction have durable consequences.
- Conservation by rules: populations and resources can decline and recover; no infinite free food loops.
- Player agency: hunting, farming, trapping, fishing, habitat protection, controlled burning, reforestation and settlement choices matter.
- Performance first: nearby life can use entity AI; distant life is represented by regional population summaries.
- Edition parity: shared outcomes and data contracts, independent Java and Bedrock adapters and tests.

The first playable abandoned town is not expanded by this long-term specification. Full ecosystem simulation is a staged world feature.

## 2. Authoritative subsystem ownership

| State / responsibility | Authoritative owner | Other systems |
|---|---|---|
| Region, biome, climate and habitat tags | World/region service | Ecology, weather, map and spawn systems read |
| Weather and world clock | World time/weather service | Ecology, farming, power, water and visibility read |
| Wild animal population and migration | Ecology service | Wildlife AI presents nearby animals; hunting requests harvest |
| Individual active animal behavior | Wildlife AI adapter | Reads ecology state; reports death, birth or migration events |
| Plant/wild resource population | Ecology/resource-node service | Gathering and farming request harvest |
| Cultivated crops and livestock ownership | Farming/animal husbandry service | Ecology provides habitat/climate context |
| Food item creation and quality | Loot/harvest + item registry | Food system handles storage, spoilage and consumption |
| Disease exposure and outbreak state | Disease service | Reads water, food, wounds, animal and environmental events |
| Fire spread and environmental damage | Environmental hazard service | Reads fuel/material/weather; ecology receives habitat damage |
| Zombie infection and individual infected AI | Zombie AI + outbreak/lore service | Ecology only receives explicitly defined interaction events |
| Regional horde scheduling | Encounter Director | Reads noise, light, population and region danger inputs |
| NPC needs, tasks and animal care assignments | NPC simulation | Farming/ecology expose valid tasks |
| Region persistence and distant summaries | World persistence/simulation scheduler | All regional services serialize their owned state |

No subsystem may directly mutate another subsystem's authoritative state. It must submit a validated command or event.

## 3. Biome and habitat catalogue

Biome identity is multi-tagged, not a single visual label. A location may be, for example, temperate forest + mountain foothill + river corridor. Each region defines climate band, elevation, water availability, soil classes, vegetation profile, wildlife profile, hazards, season behavior and resource tables.

### 3.1 Temperate forest
- Mixed deciduous/coniferous woodland, clearings, undergrowth, fallen timber and forest streams.
- Resources: timber, branches, mushrooms, berries, medicinal plants, game trails and hunting sites.
- Wildlife profile: deer-like herbivores, wild boar, foxes, wolves, rabbits, birds and insects (exact species roster remains configurable).
- Hazards: poor visibility, getting lost, storms, falling trees, forest fire and predators.
- Gameplay: hunting, gathering, shelter, tracking, timber production and fire management.

### 3.2 Dense / dark forest
- Reduced visibility, dense canopy, difficult navigation and fewer open firing lanes.
- More sheltered animal habitats, hidden dens and abandoned ranger structures.
- Increased navigation and ambush pressure; do not arbitrarily increase all hostile spawns.

### 3.3 Grassland and open plains
- Open sightlines, grass and seasonal wild plants, grazing and migration corridors.
- Resources: forage, seeds, small game, grazing land and wind exposure.
- Hazards: limited cover, storms, heat/cold exposure and long travel distances.

### 3.4 Farmland and rural settlement
- Crop fields, orchards, greenhouses, barns, silos, irrigation and wells.
- Domestic animals, pests, scavengers and wildlife incursions.
- Resources depend on crop stage, season, irrigation, soil and prior harvesting.
- Farm buildings can provide seeds, tools, feed and preservation equipment, subject to loot and ownership rules.

### 3.5 Mountain, highland and alpine
- Elevation bands, rocky slopes, conifer belts, snowline and sheltered valleys.
- Resources: stone, ores, alpine plants, mountain water and specialist wildlife.
- Hazards: cold, steep traversal, falling, snow, blocked passes and reduced oxygen only if a later approved mechanic justifies it.
- Animal density and plant growth vary with elevation and season.

### 3.6 Wetlands, marsh and river delta
- Reeds, mud, shallow water, insects, amphibians, waterfowl and fish habitats.
- Resources: reeds, fish, selected plants, clay and water access (not automatically potable).
- Hazards: difficult movement, contamination, insects and low visibility.
- Water quality remains owned by the water service.

### 3.7 Freshwater: rivers, lakes and reservoirs
- Flowing and still water habitats with fish populations, shore plants and water access points.
- Fishing pressure, pollution, drought and seasonal changes affect local availability.
- Dams, treatment plants and player infrastructure may change access or flow only through defined world rules.

### 3.8 Coastal, island and marine
- Beaches, cliffs, tidal shore, marinas, islands, estuaries and offshore routes.
- Resources: fish, shellfish where modelled, sea plants, driftwood and maritime salvage.
- Hazards: storms, exposure, tides only if supported, difficult resupply and limited escape routes.
- Boats and fishing systems connect to transport and food production.

### 3.9 Desert, arid and semi-arid
- Sparse vegetation, water scarcity, heat/cold swings, dry riverbeds and isolated settlements.
- Wildlife has lower density and specialized water/heat behavior.
- Resources are scarce and region-specific; wells, cisterns and water infrastructure are strategically valuable.
- Heat exposure must be configurable and clearly signalled.

### 3.10 Snow, boreal and frozen regions
- Snow cover, frozen water, conifer forest, short growing seasons and winter shelters.
- Wildlife migration, hibernation/dormancy or reduced activity may be represented with regional summaries.
- Hazards: cold exposure, blizzards, frozen routes and limited crop options.
- Snow and ice effects must be tested independently in Java and Bedrock.

### 3.11 Urban, industrial and contaminated habitats
- Parks, drainage corridors, rooftops, vacant lots, industrial edges and abandoned buildings.
- Common urban wildlife and scavengers may adapt to food waste and shelter.
- Pollution, chemical spills and disease hotspots are explicit site events, not a global invisible debuff.
- Some plants may colonize abandoned structures over time if performance permits.

### 3.12 Underground caves and mines
- Cave-adapted or cave-visiting species only where justified by the chosen world setting.
- Fungi, underground water, mineral nodes and limited food webs.
- Darkness and navigation hazards; avoid inventing a complex underground ecosystem if it adds no gameplay loop.

## 4. Wildlife classification and species framework

The roster is data-driven and extensible. The following are species families and design candidates, not a final mandatory species count.

- Herbivores: deer, rabbit/hare, goat, sheep, cattle and other grazing animals.
- Omnivores: wild boar, bear-like species and adaptable small mammals.
- Carnivores: wolf, fox and other region-appropriate predators.
- Scavengers: crows, ravens, vultures, rats and other carrion consumers.
- Birds: poultry, waterfowl and forest birds.
- Aquatic life: freshwater and marine fish; other aquatic species only where the fishing loop needs them.
- Insects and small fauna: pollinators, pests and ambient life; low-cost representation preferred.
- Domestic livestock: chickens, ducks, sheep, goats, pigs and cattle as the initial candidate families.

Each species definition includes:
- Stable species ID, display name and edition-specific entity/asset IDs.
- Valid biome/habitat tags and elevation/climate ranges.
- Population cap, group size and regional density range.
- Food, water and shelter requirements.
- Activity windows, seasonal migration/dormancy and reproduction conditions.
- Threat response: flee, hide, defend, group, investigate or ignore.
- Predator/prey/scavenger relationships where explicitly enabled.
- Harvestable products, quality rules and ethical/gameplay restrictions.
- Disease susceptibility and transmission routes if enabled.
- Sound, tracks, droppings, nests, dens and other discoverability evidence.
- AI complexity tier and active simulation budget.

Animals must not be universally hostile. Predators may defend territory or hunt; herbivores generally flee; scavengers may approach corpses or waste; domestic animals follow ownership and care rules.

## 5. Population dynamics and food webs

Regional population state tracks at minimum:
- Current estimated population by species.
- Habitat suitability and carrying capacity.
- Birth/recruitment and mortality summaries.
- Food and water availability.
- Hunting/harvest pressure.
- Predation and disease pressure.
- Migration in/out.
- Human disturbance, fire and habitat damage.
- Last simulation timestamp and deterministic seed/state.

Population transitions use bounded, deterministic intervals. Avoid simulating every animal each tick. Distant regions update aggregate values; nearby regions instantiate a limited number of active animals consistent with the aggregate.

Food-web rules:
1. Herbivores consume eligible vegetation/forage.
2. Predators consume or pressure eligible prey only through bounded events.
3. Scavengers may consume eligible carcasses and waste.
4. Wildlife competes indirectly with farming for habitat/food only when a region rule enables it.
5. Zombie interactions with animals are defined separately and must not create an unlimited infection chain.
6. A population cannot exceed its regional carrying capacity without an explicit temporary migration/food-supply rule.
7. Carcasses and harvested remains have one owner for item creation, spoilage and disease exposure.

Overhunting lowers future availability. Recovery depends on habitat, food, water, season and pressure; it is not an instant respawn. Extinction of a local population may be possible for selected species, but global extinction and irreversible soft-locks require deliberate design and safeguards.

## 6. Animal AI and player interaction

Active wildlife behaviors:
- Idle, graze, drink, forage, rest, patrol, migrate, flee, hide, defend, hunt, return to den and follow/obey (domestic only).
- Perception uses bounded range and line-of-sight checks.
- Group movement uses a leader or shared target rather than independent expensive pathfinding for every member.
- Animals react to gunfire, explosions, fire, vehicles, player approach and zombie presence using species-specific response profiles.
- Tracks, calls, nests and feeding areas support hunting and discovery without mandatory minimap UI.
- Taming/domestication, breeding and riding remain separate feature gates; they are not automatically assumed from wildlife inclusion.
- Animal handling uses interaction/animation appropriate to each edition; no real-world animal-care simulation is required.

Hunting and capture:
- Hunting can use approved weapons, traps, bows or tools according to the combat/crafting catalogue.
- Trap placement, bait, catch eligibility, durability and retrieval are explicit.
- Harvest requires a valid kill/capture state and produces one harvest event.
- Butchering/processing may require tools or a workstation at higher tiers.
- Animal remains can spoil and attract scavengers under bounded rules.
- Hunting must not duplicate loot through both entity drops and harvest interaction.

Fishing:
- Freshwater and marine zones have species/availability tables.
- Catch depends on location, time/season, gear, bait and fishing pressure where enabled.
- Fishing gear is craftable/repairable through the staged crafting system.
- Fish is perishable and must integrate with cooking, storage and disease rules.

## 7. Plants, vegetation and natural resource cycles

Plant records include stable ID, species/category, biome, soil requirements, water/light range, growth stages, seasonal window, yield, regrowth, harvest method, seed source and hazard properties.

Wild plant categories:
- Edible berries, roots, nuts, fruits and herbs.
- Mushrooms with clearly distinguished edible, inedible and poisonous gameplay categories.
- Medicinal or crafting plants with fictionalized, non-medical game effects.
- Timber trees, saplings, shrubs, grasses, reeds and fibres.
- Toxic, irritating or otherwise hazardous plants where they add readable gameplay.
- Decorative/ambient plants with low simulation cost.

Rules:
- Plant growth depends on season, climate, soil, water and light.
- Harvesting can reduce a node's yield or remove it; regrowth has a defined interval and conditions.
- Seeds and saplings support replanting and reforestation.
- Fire, drought, flood, pollution and trampling can damage vegetation.
- Plants may spread into suitable empty habitat over long intervals, but only through bounded regional summaries.
- Wild plant identification can progress through discovery, books, survivor knowledge or research.
- Poisonous plants must be visually/educationally distinguishable before dangerous consumption or provide an accessible identification aid.

Mushroom/foraging safeguards:
- Do not rely on real-world mushroom identification knowledge.
- Use clear in-game categories and optional journal discovery.
- Unknown food should provide a warning or low-risk test mechanic rather than arbitrary unavoidable death.
- Poisoning is a fictional status with defined symptoms, treatment and duration.

## 8. Farming, orchards, greenhouses and soil

Farming is a managed subsystem distinct from wild ecology:
- Crop plots, planters, fields, orchards and greenhouse beds.
- Soil quality/nutrients represented in a simple bounded state, not per-block chemistry.
- Crop stages: seed, sprout, growing, mature, harvest-ready, damaged/dead.
- Inputs: seed, water, suitable soil, light, season and optional fertilizer.
- Threats: drought, frost, heat, pests, disease, weeds, wildlife and fire.
- Irrigation consumes water through the canonical water network; powered pumps consume electricity through the canonical power network.
- Manual watering and low-tech tools remain possible where practical.
- Crop rotation/soil recovery can be a later depth layer; it must not become an opaque mandatory chore.
- Greenhouses extend growing seasons but require materials, water and potentially power.
- Orchards and perennial plants use longer harvest cycles.
- Seeds can be recovered from harvests according to deterministic yield ranges.
- Food production is not infinite: land, water, time, seed, labour and storage constrain it.

Livestock and animal husbandry:
- Ownership/claim, shelter, feed, water, health/status, reproduction and product collection.
- Animals need appropriate enclosure and protection; overcrowding and neglect have explicit consequences.
- Products include eggs, milk, wool, meat and manure only for compatible species.
- Slaughter/harvest is a deliberate player action and not a hidden automatic reward.
- NPC farmers can tend assigned animals if they have valid skills, feed, water, shelter and safe access.
- Disease and veterinary care are fictional game systems with clear treatment paths.
- Livestock can be lost to predators, hordes, fire, disease or theft if protections fail.

## 9. Weather, climate and seasonal coupling

The world clock/weather service owns time and weather. Biomes interpret the same world state through local climate profiles.

Weather states may include clear, cloudy, rain, heavy rain, storm, fog, wind, snow, blizzard, heatwave and drought. Availability is biome/season constrained.

Seasonal effects:
- Spring: regrowth, planting windows, variable rain and animal breeding periods where enabled.
- Summer: crop growth, heat/water demand, dry vegetation and fire risk.
- Autumn: harvest, leaf cover, migration and preparation for cold.
- Winter: snow/frost, shorter growing windows, water access changes and increased shelter/fuel needs.

Effects connect to:
- Farming yields, planting windows and crop loss.
- Wild plant growth and harvest availability.
- Wildlife activity, reproduction and migration.
- Player exposure and clothing only if survival rules enable it.
- Water collection, contamination/dilution and freezing rules.
- Solar/wind generation and power demand.
- Fuel use, vehicle traction/route conditions and repair.
- Fire ignition/spread and firefighting access.
- Visibility, sound propagation and zombie detection/navigation.
- NPC schedules, shelter and settlement needs.

Exact season duration, day length, temperature model and weather probabilities remain tunable. Scenario overrides must not corrupt the persistent world calendar.

## 10. Water, soil, pollution and environmental quality

The water system owns quantity and potable/contamination state. Ecology and farming may request or report environmental effects through explicit events.

Environmental states:
- Clean, contaminated, polluted or otherwise unsuitable water classes.
- Soil fertility/condition and contamination tags.
- Air/smoke exposure as temporary regional hazard summaries.
- Waste and sewage presence at bounded sites.
- Habitat quality and disturbance.

Interactions:
- Sewage, corpses, industrial spills and waste can create defined contamination events.
- Rainfall and water flow may spread/dilute contamination only through explicit hydrology rules.
- Treatment plants, filters and boiling operate on water quality through the water service.
- Soil contamination can affect crops only where a documented rule applies.
- Pollution cleanup can be a quest, research or settlement task.
- Never silently turn all nearby water into contaminated water because a distant event occurred.

## 11. Disease, parasites, food safety and zombie infection separation

Disease service owns exposure and status. This is fictional game logic, not real medical advice.

Potential gameplay categories:
- Food spoilage/foodborne illness.
- Waterborne illness.
- Animal-borne exposure.
- Wound infection.
- Crop/livestock disease.
- Environmental outbreak zones.
- Zombie infection, kept separate from ordinary disease unless a specific story rule connects them.

Each disease definition specifies:
- Exposure source and validated trigger.
- Incubation and symptom states if used.
- Transmission route and radius/contact conditions.
- Severity, duration and recovery outcomes.
- Treatment, prevention and resource costs.
- Player/NPC/animal susceptibility flags.
- Diagnostic evidence and UI/NPC notification rules.
- Save/load behavior and test cases.

Food safety:
- Perishable food has freshness/spoilage state.
- Storage temperature/preservation methods may slow spoilage.
- Raw/cooked/unsafe states are explicit.
- Cooking is not a universal cure for every poison or disease.
- Spoiled food must display clear cues before consumption where possible.

Animal disease:
- Disease does not automatically jump between every species.
- Transmission matrix is species- and pathogen-specific.
- Quarantine, cleaning, isolation and treatment use clear tasks.
- NPC dialogue can describe only recorded symptoms/diagnoses supplied by the disease service.

## 12. Fire, drought, flood, storm and habitat disturbance

Environmental hazard service owns hazard propagation and damage. Ecology receives the resulting habitat/resource changes.

- Forest fire: bounded ignition and spread by eligible fuel, weather and suppression.
- Drought: regional water/vegetation stress over time, not instant mass death.
- Flood: selected low-lying zones, crop damage, route disruption and contamination only where hydrology is modelled.
- Storm: wind/rain/lightning effects, structure/vehicle risk where explicitly enabled.
- Frost/heatwave: crop and exposure effects by climate band.
- Pollution/industrial accident: site/region-scoped contamination.
- Landslide/tree fall: rare, bounded terrain/route events only if supported by target editions.

Player/NPC counterplay:
- Firebreaks, controlled clearing, extinguishers, water supply and safe evacuation.
- Irrigation, rain storage, wells and water rationing.
- Drainage, raised storage and route alternatives.
- Shelter, clothing and work scheduling.
- Reforestation, cleanup and repair.
All hazard events have source, region, severity, duration, warning, counterplay, damage budget and stable event ID.

## 13. Zombie and wildlife interaction

Zombies remain a separate hostile-infected system. Wildlife does not automatically become infected or turn into zombie variants.

Possible explicit interaction rules:
- Animals flee from nearby zombies, gunfire, fire and large hordes.
- Certain scavengers approach corpses after a delay.
- Noise and lights may draw zombies toward animal pens or active farms only through defined attraction events.
- Predation/carcass consumption may create disease exposure only if an approved pathogen rule exists.
- Zombie attacks can kill livestock and damage enclosures.
- Wildlife may reveal nearby danger through alarm calls or sudden flight.
- Animal movement must not become a free global zombie locator or bypass encounter budgets.
- Infection of animals, zombie animals or mutation is excluded unless separately approved as a distinct feature with lore, balance and compatibility review.

## 14. Hunting, gathering, cooking, storage and economy integration

- Hunting/fishing/gathering submit one harvest request; ecology validates population/resource availability.
- Loot/harvest creates item outputs once; item registry assigns quality, freshness and provenance.
- Cooking/crafting consumes ingredients from the canonical inventory and workstation systems.
- Food preservation uses existing storage/energy design: drying, smoking, salting, canning, refrigeration/freezing where implemented.
- Economy/faction stock uses the same item IDs and freshness rules.
- Regional scarcity emerges from production, trade, harvest pressure and transport disruption.
- Rare materials and specialist ingredients must not be duplicated by both world loot and ecology harvest.

## 15. NPC, faction and settlement integration

NPCs can have roles such as farmer, hunter, fisher, cook, medic, mechanic, ranger, trader and animal handler.

Task contract:
1. NPC simulation owns identity, needs, profession, skill, inventory and current task.
2. Settlement assigns a valid task only if required tools, materials, access and safety exist.
3. Ecology/farming services expose task actions and report results.
4. Economy and inventory record produced/consumed goods.
5. Dialogue reads authoritative results and contextual game state; it cannot fabricate completed work.

Faction territory and policy may regulate hunting, grazing, fishing, crop access and protected habitat. Trade and reputation consequences must be explicit.

## 16. Crafting, equipment and progression

Ecosystem items feed the staged crafting system while preserving the vanilla Crafting Table as the first tier. Advanced processing may use specialist workstations.

Candidate equipment:
- Hunting tools, fishing rods/nets, traps and bait.
- Knives and processing tools.
- Seeds, hoes, watering cans, irrigation components and greenhouse parts.
- Animal feed, troughs, fences, shelters and transport crates.
- Storage, preservation and cooking equipment.
- Protective clothing and environmental tools where supported.

Recipes must reference canonical materials and unlocks. Skills may improve efficiency/yield within caps but cannot bypass missing ingredients, workstation tiers or research prerequisites.

## 17. Regional simulation and performance model

Three fidelity levels:
- **Active:** nearby animals/plants use bounded entity/block interactions and visible behavior.
- **Near-region:** aggregate groups and scheduled events; instantiate only when needed.
- **Distant:** deterministic population/resource summaries updated at coarse intervals without loading chunks or ticking every entity.

Required limits:
- Per-region species population caps.
- Active entity budgets and group pathfinding budgets.
- Bounded plant growth/harvest updates.
- Bounded disease, fire and weather event queues.
- No global per-tick scans.
- No chunk loading solely to simulate distant animals/NPCs.
- Deterministic seeded updates for reproducible tests.
- LOD transitions must not duplicate or erase populations.
- Save only durable state; reconstruct transient effects.

## 18. Shared data contracts and manifest requirements

Every ecosystem component must define:
- Stable component/species/biome/resource ID and schema version.
- Target platform capability requirements.
- Dependencies and conflicts.
- Authoritative state owner.
- Events emitted/consumed.
- Save schema and migration policy.
- Spawn/population/active simulation budgets.
- Asset/model/sound/animation references.
- User-facing settings and accessibility behavior.
- Acceptance tests and evidence status.

Canonical entities: BiomeProfile, HabitatProfile, SpeciesDefinition, RegionalPopulation, WildlifeGroup, PlantDefinition, ResourcePatch, CropDefinition, LivestockRecord, DiseaseDefinition, EnvironmentalHazard, HarvestTransaction, WeatherSnapshot and EcologyEvent.

Event envelope fields: event_id, event_type, source_component, region_id, subject_id, world_tick, seed, severity, payload_version and lifecycle_state. Events must be idempotent.

## 19. Java/Bedrock implementation and parity

Shared logical data and gameplay contracts do not imply shared code. Java Fabric and Bedrock stable Script API receive separate adapters and capability maps.

For each feature, record:
- Supported API/capability evidence for exact target version.
- Entity/model/animation/loot/interaction representation.
- Persistence mechanism and limits.
- Performance measurements.
- Known platform differences and fallbacks.
- Fresh-world and existing-save tests.

Experimental Bedrock APIs remain disabled. If a feature cannot be represented with stable APIs, it must be deferred, simplified with equivalent player-facing outcome, or reported as a platform limitation; never silently use experimental APIs.

## 20. Configuration, accessibility and difficulty

World settings may control:
- Wildlife density and group size.
- Hunting pressure and population recovery speed.
- Crop growth and season duration.
- Weather frequency and environmental severity.
- Food spoilage and disease severity.
- Fire spread and hazard frequency.
- Predator aggression and livestock vulnerability.
- Ecological simulation detail/performance budget.

Difficulty presets should modify documented parameters, not secretly change rules. Accessibility options include clearer plant/food identification, hazard warnings, reduced environmental penalties and readable event logs. Settings must be save-compatible and multiplayer-ready if that future proposal is approved.

## 21. First playable boundary

The current first playable remains a compact abandoned town, single-player, with the approved core locations and separately approved combat/backpack scope. This ecosystem design does not automatically add full wildlife population simulation, farming, seasons, fishing, livestock, disease or dynamic weather to the first playable.

A later vertical slice may select a small, testable subset such as one local wildlife group, a few harvestable plants and one weather-linked interaction. Selection requires explicit milestone planning and cross-edition feasibility evidence.

## 22. Acceptance criteria

A future ecosystem release is not complete until:
1. Every biome and species has stable IDs and validated habitat constraints.
2. Regional populations stay within configured bounds.
3. Hunting/harvesting changes population or resource availability exactly once.
4. Reproduction, recovery and migration are deterministic and bounded.
5. Active and distant simulation reconcile without duplication.
6. Crops respond to documented water, soil, season and hazard inputs.
7. Livestock requires valid feed/water/shelter and produces only valid outputs.
8. Weather/season changes propagate consistently to dependent systems.
9. Water, food, disease and contamination use one authoritative state per domain.
10. Fire and environmental hazards have warnings, counters and bounded propagation.
11. Wildlife/zombie interaction follows explicit rules and does not create uncontrolled infection/spawns.
12. NPC work and dialogue reflect actual recorded state.
13. Save/load and region re-entry preserve populations, crops, harvests and active events.
14. Java and Bedrock independently pass equivalent gameplay tests using stable APIs.
15. Performance stays within recorded active entity, tick and memory budgets.

## 23. Open balance and content decisions

The architecture is defined, but these values require content design and test tuning:
- Exact species roster per biome and total animal count.
- Population caps, group sizes, breeding rates, migration cadence and recovery periods.
- Plant species, growth rates, yield and regrowth.
- Crop catalogue, soil complexity and greenhouse bonuses.
- Disease catalogue, transmission matrix and treatment items.
- Weather/season durations and probabilities.
- Fire, flood, drought and pollution severity.
- Fishing tables, hunting yield and food spoilage rates.
- First ecosystem vertical-slice selection.
These are not blockers to documenting the architecture; they are data/balance work before implementation.

## 24. Implementation boundary

Design specification only. No animals, crops, biomes, ecological simulation, scripts, mods, worlds or playable artifacts have been generated or runtime-tested by this document.
