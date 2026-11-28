# Zombie Invasion — Expanded Transport Network: Convoys, Trains, Boats and Helicopters Design V1

Status: User-approved transport scope expansion; detailed mechanics and platform feasibility remain design proposals. Not implemented.

## 1. Transport architecture
The existing vehicle design remains authoritative for bicycles, motorcycles, cars, off-road vehicles, pickups, trucks, minibuses, buses, caravans and trailers. This document extends it with convoy coordination, rail, watercraft and aircraft. A shared vehicle definition describes role, seats, cargo, fuel/energy, durability, parts, handling and service needs; each vehicle class adds specific capabilities.

## 2. Convoys
- Multiple owned/recruited vehicles can travel as a convoy with lead/follow roles.
- Convoy manifest tracks passengers, cargo, fuel, condition and destination.
- NPC drivers require the appropriate role/skill and route knowledge.
- Convoy speed and formation are bounded by the slowest/most constrained vehicle.
- Ambush, breakdown, fuel shortage and route blockage create events; player retains manual control and recovery options.
- Do not simulate a long convoy as many fully ticking entities outside active range.

## 3. Rail transport
- Trains use authored rail corridors/stations in the map or a controlled extension.
- Train types may include freight, passenger and maintenance/armored variants.
- Cars/wagons have explicit capacity and coupling rules.
- Rail travel requires track continuity, powered/operational locomotive where applicable, crew/controls and station access.
- Derailment and track damage should be rare, readable and recoverable; avoid unpredictable destruction.
- Rail is a strategic transport layer, not a substitute for ordinary vehicles.

## 4. Boats and water travel
- Boats include small rowboats, motorboats and larger utility vessels as staged options.
- Watercraft have seats, cargo, durability, fuel/propulsion, docking and storage rules.
- Water routes may provide alternate access to islands, coastlines and river districts.
- Weather, water conditions and damage affect travel within a bounded model.
- Existing Minecraft boats and water mechanics should be respected where possible; custom systems must not create incompatible duplicate controls.

## 5. Helicopters and aircraft
- Helicopters are late-game/high-complexity assets requiring rare parts, fuel, maintenance, a trained pilot and suitable landing zones.
- Flight model may be simplified and platform-specific, but takeoff, landing, altitude limits, collision, fuel and damage must be explicit.
- Aircraft noise attracts threats; landing/repair requires space and infrastructure.
- If reliable cross-edition flight cannot be delivered with stable APIs, the first implementation may use a constrained scripted transport/landing abstraction. Do not claim full simulation until validated.
- No real-world flight instruction is implied; this is game logic.

## 6. Vehicle production and maintenance
Factory/workshop progression from the existing vehicle specification remains in force. New vehicle classes require blueprints, components, assembly and commissioning. Trains additionally require rail infrastructure; boats require docks/water access; helicopters require a hangar or service zone.

## 7. Integration
Fuel storage and generators use the common fuel registry. Convoys consume finite fuel and food/water for passengers where that system applies. NPC recruitment, faction trade, quest routing, map landmarks, radio and encounter events can all reference transport state. Bus mobile-base rules remain unchanged and can use the same shared power/water interfaces.

## 8. Acceptance criteria
1. Convoy manifests and ownership are persistent.
2. NPC driver assignments require capability and valid vehicle state.
3. Rail vehicles cannot travel without valid track/station conditions.
4. Boats require navigable water and valid docking/boarding.
5. Helicopter flight is bounded, fuelled and repairable.
6. Vehicle noise and travel events feed shared threat systems.
7. Transport capacity and cargo are finite.
8. All new vehicles use shared fuel, damage, inventory and ownership definitions.
9. Java and Bedrock provide equivalent outcomes or clearly declared edition-specific limitations.

## 9. Open decisions
Exact vehicle roster per milestone, rail map extent, locomotive power model, watercraft physics, helicopter control complexity, NPC driving autonomy, convoy size and multiplayer synchronization remain open.
