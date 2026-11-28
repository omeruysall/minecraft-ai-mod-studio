# Zombie Invasion — Base Building, Property Claim, Defense and Automation Design V1

Status: User-approved system scope; detailed mechanics are design proposals. Not implemented.
Targets: Java 26.3 + Fabric; Bedrock 26.60, stable APIs only unless separately approved.

## 1. Vision
Players can claim, restore, fortify and expand abandoned structures or build a settlement from the ground up. Bases are persistent operational spaces that connect construction, NPCs, power, water, storage, crafting, vehicles, threats and economy.

## 2. Claiming and ownership
- Claimable sites include houses, shops, hospitals, police stations, warehouses, farms, garages and selected industrial buildings.
- A claim process may require clearing hostiles, securing entrances and activating a claim marker/registry.
- Claims store owner/faction, permissions, access points, protected areas, maintenance state and linked infrastructure.
- Multiplayer permission concepts must be designed without assuming the first playable milestone is multiplayer; single-player owner behavior is the default.
- Avoid blanket protection that makes the world indestructible. Damage, repair and access rules are explicit.
- Players can abandon, transfer or lose a claim through defined scenario rules; no silent ownership reassignment.

## 3. Free construction
- Build with vanilla blocks and modded structural pieces: walls, floors, roofs, doors, gates, windows, stairs, platforms, scaffolds and modular rooms.
- Defensive pieces include barricades, reinforced doors, shutters, fences, concrete barriers, watchtowers and vehicle barriers.
- Placement must respect collision, support, access and target-platform limitations.
- Existing building restoration should be viable alongside new construction.
- Provide structural categories and preview/placement feedback where feasible; do not require a proprietary building grid for ordinary Minecraft blocks.

## 4. Defense and traps
- Passive defense: walls, fences, doors, shutters, trenches and chokepoints.
- Active defense: alarms, spotlights, sirens, cameras/sensors, guard posts and powered defenses.
- Traps: noise lures, trip alarms, snares, spike/barrier traps and crafted defensive devices, with clear arming/disarming and friendly-fire rules.
- Traps have durability, maintenance and resource costs. They do not generate unlimited damage or loot.
- Noise/light emissions feed the shared threat/noise system and can attract infected.
- Defensive systems must not create an unavoidable base-death loop. Give warning cues and counterplay.

## 5. Power, water and automation
- Electrical consumers use the power network: lights, alarms, cameras, workstations, pumps, communications and selected defenses.
- Water consumers use the water network: taps, showers, medical/cooking stations and irrigation.
- Switches, timers, sensors, valves and distribution panels allow basic automation.
- Automation rules are bounded and inspectable: trigger, condition, action, cooldown and power/water cost.
- Fail-safe manual controls remain available for essential systems.
- Avoid circular dependencies (e.g. a pump requiring power from a generator that cannot be fueled without the pump).

## 6. Base operations and upkeep
- Base status panel summarizes integrity, entrances, hostile pressure, power, water, storage, fuel, food and NPC needs.
- Maintenance tasks are prioritized by severity. Degradation should be gradual and legible, not a constant repair tax.
- Zones may be designated as sleeping, medical, workshop, storage, farming, livestock, vehicle and public areas.
- Fire safety, waste separation, lighting discipline and noise management are part of base planning.

## 7. NPC roles and permissions
NPCs can be assigned to guard, repair, farm, cook, medical care, logistics, water/power maintenance and research. Assignment requires relevant skill, tools and access. NPCs cannot perform impossible tasks or conjure resources. The player can define work zones, schedules and priority tasks.

## 8. Threat integration
Encounter Director owns hostile event scheduling and budgets; base-defense system supplies target attractiveness, noise/light, fortification and breach state. Zombie AI owns individual navigation and attack behavior. Do not let the base system spawn or directly control zombies. Breaches and damage feed the shared world-state event bus.

## 9. Acceptance criteria
1. A player can secure and claim supported abandoned buildings.
2. The player can build a defensible base with vanilla and modded construction pieces.
3. Permissions and ownership are inspectable.
4. Defensive devices have costs, states, durability and counterplay.
5. Powered defenses stop or degrade when their supply fails.
6. Water-dependent services respond to water availability.
7. Automation rules cannot bypass resource requirements.
8. Base status reflects actual linked subsystem state.
9. Threat pressure reacts to noise, light, access and defense state.
10. Both editions deliver equivalent gameplay outcomes.

## 10. Open decisions
Exact claim radius, multiplayer claim permissions, structural damage rules, building-piece catalog, automation complexity, trap balance, repair cadence and first-slice base-building subset remain open. Technical implementation must be profiled per edition; large redstone-like networks and per-block ticking are explicitly not assumed.
