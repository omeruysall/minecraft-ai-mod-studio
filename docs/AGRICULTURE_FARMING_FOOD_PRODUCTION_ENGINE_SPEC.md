# Agriculture, Farming & Food Production Engine Specification

**Document status:** Design draft  
**Version:** 0.1  
**Implementation status:** Not implemented; design requirements only.  
**Approval status:** Awaiting product decisions and baseline approval.

## 1. Purpose
Define crop cultivation, soil and climate interactions, orchards, livestock, fisheries, food processing, cooking, storage, and agricultural supply chains for generated Minecraft projects. The engine coordinates agricultural rules while delegating inventory, crafting, ecology, NPC, economy, and world state to their authoritative systems.

## 2. Ownership boundaries
- This engine owns agricultural definitions, crop growth rules, farm plans, husbandry rules, and food quality/production configuration.
- World/Map Engine owns terrain, farmland placement, water bodies, and structures.
- Ecology Engine owns wild species, habitat, and ecosystem simulation.
- Crafting Engine owns recipe execution, processing machines, and production jobs.
- Item/Inventory Engine owns item stacks, containers, and transfers.
- Economy Engine owns prices, wallets, and transactions.
- NPC Engine owns animal/entity identity where applicable, residents, and worker behavior.
- Settlement Engine owns farm district and service planning.
- Environment Interaction Engine owns permission-checked block interactions.

## 3. Principles
- Native Minecraft farming remains available unless the project explicitly replaces or extends it.
- Growth and production are bounded, configurable, and reproducible.
- Chunk unload and offline behavior are explicit.
- Animal welfare-like mechanics are game rules, not real-world husbandry advice.
- Item creation and resource consumption are authoritative and duplication-resistant.
- Performance limits prevent per-tick global crop/animal scans.
- User approval is required before generation and balance changes.

## 4. Scope
In scope: crops, seeds, soil, irrigation, seasons, weather, greenhouse systems, orchards, livestock, breeding, feed, animal products, fisheries, cooking, food processing, storage, spoilage options, farm automation, yield, pests/disease abstractions, agricultural contracts, and farm management UI.

Out of scope: real-world agricultural simulation accuracy, real-money commodity trading, unbounded animal populations, and replacing native mechanics by default.

## 5. Crop definitions
A crop profile defines stable ID, seed/item references, growth stages, growth conditions, light/temperature/moisture ranges, soil requirements, yield, harvest method, regrowth, seasonality, biome constraints, and platform mappings. Each stage has clear transitions and failure behavior.

## 6. Soil and farmland
Soil profiles may represent fertility, moisture, nutrients, compaction, salinity, or custom abstract attributes. Define which are enabled, how they change, and how they recover. Native farmland behavior must not be assumed identical across platforms. Soil updates are event-driven or scheduled, not continuous per-block scans.

## 7. Irrigation and water
Irrigation supports manual watering, channels, sprinklers, reservoirs, pumps, and automated networks where platform capabilities allow. Define water source, range, capacity, flow, consumption, access, and failure behavior. Water blocks and fluid state remain owned by platform/world systems.

## 8. Climate, seasons, and weather
Optional climate profiles define temperature, rainfall, frost, drought, seasons, and crop compatibility. World Events and Weather systems own global time/weather events; this engine consumes climate facts and evaluates crop impact. Define world-time versus real-time, dimension rules, and behavior in unloaded chunks.

## 9. Greenhouses and controlled environments
Greenhouses define structure requirements, light/temperature control, irrigation, capacity, energy/resource use, and crop eligibility. Structural validation references World Engine geometry. Avoid claiming climate control where only decorative blocks exist.

## 10. Orchards and perennial crops
Perennial profiles define planting, maturation, seasonal yield, pruning/maintenance abstractions, harvest cycles, and replacement. Define whether growth persists while unloaded and how tree structure changes are generated without damaging player builds.

## 11. Livestock and animal husbandry
Animal profiles define species, habitat, feed, breeding, growth, products, movement, capacity, and interaction rules. Ecology/NPC systems own entity identity and population limits. Define tame/domestic versus wild classification and prevent farm breeding from bypassing global entity caps.

## 12. Feed, breeding, and animal products
Feed recipes and breeding conditions reference Item and Crafting engines. Define cooldowns, offspring limits, product intervals, health/status abstraction, and resource costs. Product generation uses idempotent events and respects animal/entity ownership.

## 13. Fisheries and aquatic production
Optional fisheries define species, habitat, water quality abstraction, catch methods, stocking, breeding, and harvest limits. Ecology owns wild populations; farmed populations use explicit ownership and caps. Prevent unlimited renewable output unless deliberately configured.

## 14. Food processing and cooking
Processing recipes reference Crafting Engine. Food definitions may include nutrition, effects, quality, freshness, and preparation requirements. Item Engine owns item instances; Progression and Combat systems consume effect references through explicit contracts. Define whether native food values are preserved or extended.

## 15. Freshness, spoilage, and preservation
Optional freshness mechanics define decay rates, environmental modifiers, storage requirements, preservation methods, and expiry. Define whether time advances in unloaded chunks or offline sessions. Avoid irreversible loss without clear UI, opt-in policy, and recovery settings.

## 16. Pests, disease, and crop hazards
Optional hazards define trigger conditions, spread, severity, treatment, and prevention. Keep simulation bounded and legible. Hazard effects must not spread across protected/player areas without project-defined rules. Medical or biological realism is not implied.

## 17. Farm automation and logistics
Machines, harvesters, conveyors, storage, and delivery routes integrate with Crafting, Item, and Transportation engines. Each automation node defines throughput, input/output, power/resource use, permissions, and failure states. Automation must not duplicate items or bypass claim permissions.

## 18. Yield, quality, and balance
Yield formulas define base output, modifiers, caps, randomness, and quality tiers. Use seeded deterministic outcomes where reproducibility matters. Include simulation reports for expected output, labor, resource cost, and potential exploits. Prevent infinite feedback loops in automated production chains.

## 19. Farm labor and settlement integration
Farm jobs reference NPC professions and settlement capacity. NPC Engine owns worker identity and schedule; Settlement Engine owns district/service planning. Define physical versus abstract labor simulation and behavior when workers/chunks are unloaded.

## 20. Multiplayer and persistence
Server authority governs planting, harvesting, breeding, feeding, processing, and ownership. Persist crop stages, soil state, animal population, production cooldowns, freshness, and automation queues as configured. Handle concurrent harvest, reconnect, server restart, and chunk transitions without duplicate output.

## 21. Security and performance
Validate all actions server-side. Enforce per-area crop/animal/machine caps, bounded tick work, scheduled updates, and rate limits. Prevent harvest replay, breeding exploits, automated item duplication, and unauthorized farm access. Define performance budgets for loaded and unloaded areas.

## 22. Authoring experience
Provide crop catalog, farm plot editor, soil/climate controls, irrigation graph, livestock configuration, food/recipe references, automation layout, yield simulator, and seasonal preview. Conversational requests become a farm plan with land, water, labor, materials, outputs, platform limitations, and dependencies before approval.

## 23. Validation and testing
Validate crop stages, growth ranges, soil/water dependencies, animal caps, breeding rules, recipe references, yield bounds, automation graph, permissions, and persistence. Runtime tests cover planting, growth, harvest, irrigation failure, weather changes, breeding, feed consumption, processing, spoilage, chunk unload/reload, multiplayer races, and restart recovery. Balance simulations test production loops and resource sustainability. Unrun tests are reported as not run.

## 24. Diagnostics and repair
Expose crop growth reasons, soil/water state, animal population accounting, production queues, yield calculations, and failed transfers. Repair plans preserve player farms and animal ownership. Changes to growth speed, yields, breeding, spoilage, or automation throughput require renewed approval.

## 25. Delivery
Deliver crop/animal/food definitions, farm plans, irrigation and automation configuration, recipes/references, platform adapters, migration rules, compatibility report, yield simulations, and test evidence. Include editable source and applicable runnable packages.

## 26. Acceptance criteria
- Crop and animal definitions have stable IDs and bounded rules.
- World, ecology, NPC, item, crafting, and economy ownership boundaries are respected.
- Growth, production, and offline behavior are explicit.
- Harvest and breeding cannot duplicate resources or exceed caps.
- Automation is permission-checked and throughput-bounded.
- Yield and balance claims have simulation evidence.
- Multiplayer persistence and recovery are tested.
- Native versus custom mechanics are clearly distinguished.
- Player-authored farms and protected regions are preserved.
- Material balance changes require renewed approval.

## 27. Open decisions
1. Which editions, versions, and Java loaders are launch requirements?
2. Is farming a core first-release module or optional expansion?
3. Which native crop behaviors are preserved?
4. Which custom crop types and soil mechanics are required?
5. Are seasons and climate simulation included?
6. Is irrigation required, and which transport methods are supported?
7. Are greenhouses and controlled environments included?
8. Which livestock species and husbandry features are required?
9. Are breeding and offspring simulation physical or abstracted?
10. Are fisheries and aquaculture in scope?
11. Which food nutrition/effect mechanics are supported?
12. Is spoilage enabled by default, opt-in, or excluded?
13. Are pests and crop disease included?
14. Which automation machines and logistics links are supported?
15. What crop, animal, machine, and farm area caps apply?
16. What happens to production in unloaded chunks and offline worlds?
17. How are farm labor and NPC jobs simulated?
18. Which yield and economy balancing targets are required?
19. Which farm data is shared with multiplayer players?
20. What migration guarantees apply to crop/animal registry changes?
21. Which external farming libraries are allowed and under what licenses?
22. What admin recovery and audit tools are required?
23. Which performance hardware and server-load profiles define support?
24. What gameplay tests establish fun, fairness, and sustainability?

## 28. Current status
Design draft only. All open decisions remain unresolved until explicitly decided by the product owner. No custom crop system, livestock simulation, food production pipeline, or playable farming module is implemented by this document.
