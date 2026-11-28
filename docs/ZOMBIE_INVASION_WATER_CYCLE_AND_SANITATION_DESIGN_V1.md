# Zombie Invasion — Water Cycle, Treatment and Sanitation Design V1

Status: User-approved system scope; this document defines a detailed design proposal. No implementation is claimed.
Targets: Java 26.3 + Fabric; Bedrock 26.60 + stable API target, subject to compatibility verification.

## 1. Goals and boundaries
Water is a finite survival resource with collection, extraction, treatment, storage, distribution, use and waste handling. The system must integrate with thirst, food, weather, seasons, base construction, power, NPC populations, disease, crafting and vehicles. It must remain understandable and avoid tedious micromanagement.

## 2. Water sources
- Rain catchers: roof gutters, collection surfaces, barrels and cisterns. Collection depends on rainfall, catchment area, cleanliness and available capacity.
- Wells: hand-dug or constructed wells, with depth/quality tiers. Water availability may vary by region and season; well placement is a world-data decision, not random infinite output.
- Natural sources: rivers, lakes, ponds and springs. Untreated surface water is not automatically potable.
- Scavenged water: bottles, tanks and containers found in buildings, vehicles and loot sites. Container condition and contamination are tracked.
- Advanced sources: powered groundwater pumps and larger settlement collection systems.

## 3. Water quality and treatment
Water quality is represented through clear gameplay states (potable, untreated, contaminated, chemically polluted) rather than hidden arbitrary values. Treatment methods include boiling, filters, purification tablets and advanced treatment stations. Each method has explicit input, output, capacity and limitations. Boiling requires a heat source and fuel; filters have finite service life; tablets are consumable. Chemical pollution may require specialist treatment and must not be solved by every basic filter.

## 4. Storage and containers
- Portable bottles and canteens; small jugs and barrels; large cisterns and fixed tanks.
- Storage tracks capacity, quantity, water state, container condition and leakage.
- Sealed potable storage prevents recontamination; open containers can be contaminated by environmental conditions.
- Separate potable and non-potable storage labels and connectors to prevent accidental mixing.
- Water transfer respects capacity and source quality.

## 5. Pipes, pumps and distribution
- Pipe segments, valves, connectors, taps, filters, pumps and pressure/storage components.
- Gravity-fed networks work where elevation and layout permit; powered pumps move water when gravity is insufficient.
- Network topology is inspectable; broken pipes leak, blocked pipes reduce flow, and unpowered pumps stop.
- Provide manual fallback pumps and hand-carried containers so power failure does not make water access impossible.
- Players can isolate damaged sections with valves and prioritize critical consumers.

## 6. Consumption and sanitation
- Drinking consumes potable water and satisfies thirst.
- Cooking and medical recipes may require clean water.
- Showers consume water and optionally power; they improve hygiene and reduce hygiene-related penalties.
- Toilets produce waste; latrines are early-game alternatives.
- Sewers, septic tanks and waste treatment are later infrastructure tiers. Waste must be routed away from drinking-water sources.
- Greywater (showers/washing) and blackwater (toilet waste) are distinct logical streams. Reuse is permitted only after suitable treatment.
- Handwashing and basic hygiene supplies reduce disease risk; do not make every routine action a mandatory chore.

## 7. Failure, contamination and events
Leaks, broken pumps, contaminated sources, sewage overflow and damaged storage create readable warnings and repair tasks. Flooding or storm events may damage exposed systems. Contamination spreads only through defined links and should be preventable through network separation, sealing and maintenance.

## 8. Progression and crafting
The vanilla Crafting Table remains the initial station. Early collection barrels, simple filters and hand pumps use basic recipes. Intermediate plumbing, pumps and filters require a plumbing/utility workbench. Advanced treatment plants and powered distribution require engineering/electronics stations. Blueprints and rare components gate advanced systems.

## 9. NPC and settlement integration
NPC population increases settlement water demand. Assignable water-operator/maintenance roles may inspect and repair infrastructure. NPC dialogue and status boards must use actual stored quantities, water quality and fault state. Medical and food facilities can be designated critical consumers.

## 10. Acceptance criteria
1. Rain catchment responds to rainfall and available storage.
2. Wells and surface sources have explicit source/quality states.
3. Treatment changes water state only when valid inputs and equipment are present.
4. Storage capacities and contamination boundaries are enforced.
5. Pipes, pumps, valves and leaks behave consistently.
6. Water can be moved manually without powered infrastructure.
7. Potable water is not silently mixed with sewage or untreated water.
8. Showers, toilets and waste systems have visible operating states.
9. Water shortages affect thirst and settlement services through documented rules.
10. NPC warnings reflect actual network state.

## 11. Open balance and technical gates
Exact water units, rainfall yields, thirst consumption, well-generation rules, treatment recipes, pipe simulation fidelity, pressure model, waste processing rates and first-slice inclusion remain open. Java and Bedrock must implement equivalent player-facing outcomes; if full fluid-network simulation is too expensive or unsupported, use bounded network nodes/connection data rather than pretending to simulate real fluid physics.
