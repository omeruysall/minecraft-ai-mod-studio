# Zombie Invasion — Horde Director, Fire, Disease and Wildlife Ecology Design V1

Status: User-approved system scope; detailed mechanics are design proposals. Not implemented.

## 1. Ownership boundaries
- Encounter Director owns encounter scheduling, event budgets, warning cues and spawn-point validation.
- Zombie AI owns individual infected perception, navigation, attack, obstacle interaction and state.
- World simulation owns environmental events, fire, disease exposure and wildlife populations.
- Loot system owns drops and scavenging.
- Base system owns structures, fortifications and breachable access points.
These systems communicate through explicit world events; they must not duplicate ownership or independently spawn the same hostile event.

## 2. Horde and siege behavior
- Horde events have a cause, warning phase, target region, threat budget, duration and resolution state.
- Causes can include noise, lights, generators, gunfire, alarms, scent/attraction rules if later approved, story triggers or migration.
- Horde size and composition are bounded by performance budgets and scenario difficulty.
- Siege pressure may test weak entrances, damaged barricades and noisy activity, but must not pathfind every zombie toward a base from unlimited distance.
- Breach progress is represented by structural damage and access changes, coordinated with base-building.
- Player counterplay includes decoys, noise discipline, lights-off decisions, barriers, traps, escape routes and evacuation.
- Bosses and special infected are event/roster content, not a separate uncontrolled spawn pipeline.

## 3. Fire simulation
- Fire can originate from defined sources: fuel accidents, lightning, combat, damaged electrical systems, deliberate ignition or scripted events.
- Fire spreads only through eligible materials and bounded adjacency/time rules.
- Water, extinguishers, fire blankets, sand or isolation may counter it depending on fire type.
- Fire damages structures, crops, equipment and stored resources under explicit rules; avoid indiscriminate destruction of entire worlds.
- Smoke/heat exposure has readable effects and warning cues.
- Fire and fuel storage share one hazard model; generators and electrical faults do not each invent separate fire behavior.

## 4. Disease and outbreak events
- Disease states are explicit: exposure, incubation (if used), symptomatic, recovery and fatal/severe outcome only where deliberately designed.
- Infection sources can include contaminated water, spoiled food, animal contact, wounds or outbreak zones, each with traceable rules.
- Hygiene, clean water, sanitation, medical supplies and treatment reduce risk.
- Avoid making ordinary gameplay randomly lethal. Disease severity, transmission and treatment windows must be transparent.
- The zombie infection/lore is separate from ordinary survival illness unless the story explicitly connects them.
- No real-world medical claims; this is fictional game logic.

## 5. Wildlife and ecology
- Wildlife populations are region-based and bounded. Animals have habitat, food, water, activity windows, threat response and population limits.
- Categories can include prey, predators, scavengers and domestic livestock. Exact species list remains open.
- Hunting, fishing, trapping and animal husbandry must connect to food, crafting and ecosystem recovery.
- Overhunting can reduce local availability; populations may recover slowly under defined conditions.
- Predators and scavengers can interact with corpses, crops and settlement waste, without turning every animal into an enemy.
- Wildlife can attract or avoid zombies only through explicit, testable rules.

## 6. Performance and fairness controls
Use regional simulation, event budgets, distance-based detail levels and deterministic state transitions. Distant areas use abstract simulation; active regions use fuller entity behavior. Cap concurrent horde agents and fire propagation work. Save/restore event state safely. Provide difficulty and accessibility controls for attack frequency and environmental penalties.

## 7. Acceptance criteria
1. Hordes have causes, warnings, budgets, target regions and resolution.
2. Zombie AI and encounter scheduling have separate responsibilities.
3. Base damage and breaches are owned by base structure state.
4. Fire spreads only by documented rules and can be countered.
5. Fuel, electrical faults and fire share consistent hazard events.
6. Disease exposure and treatment are traceable and fair.
7. Ordinary illness is not silently equated with zombie infection.
8. Wildlife populations remain bounded and region-aware.
9. Distant simulation does not create unbounded entity or tick costs.
10. Event state survives save/reload without duplicate hordes or fires.

## 8. Open decisions
Horde size, siege duration, breach rate, fire spread cadence, disease catalog, infection transmission, wildlife species, population density and first-slice event selection remain unresolved.


## 9. Comprehensive ecosystem specification

The concise wildlife and environmental ownership rules in this document are expanded by the integrated specification:
`docs/ZOMBIE_INVASION_ECOSYSTEM_BIOMES_WILDLIFE_AND_ENVIRONMENT_SIMULATION_DESIGN_V1.md`.

That specification is the detailed source for biome/habitat profiles, wildlife species data, food webs, regional populations, animal AI, hunting, fishing, wild plants, farming, livestock, seasons, water/environmental quality, disease, hazards, NPC work, crafting integration, distant simulation, shared event contracts and Java/Bedrock parity. In case of overlap, this document retains the high-level ownership boundaries; the comprehensive specification supplies the detailed feature contracts. No implementation is implied.
