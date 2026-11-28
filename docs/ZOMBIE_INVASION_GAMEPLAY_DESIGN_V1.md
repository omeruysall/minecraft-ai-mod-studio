# Zombie Invasion — Gameplay Design v1.0

**Status:** User-selected gameplay direction; detailed design proposal  
**Decision date:** 2026-11-28  
**First playable targets:** Java 26.3 + Fabric; Bedrock 26.60 + stable `@minecraft/server` 2.11.0  
**Experimental Bedrock APIs:** Disabled  
**Design principle:** Broad long-term gameplay vision, deliberately narrow first playable vertical slice

## 1. Executive summary

The first shared gameplay concept is **Zombie Invasion**: a survival, scavenging, preparation and base-defence experience in which players endure recurring zombie attacks while restoring and expanding a defensible settlement.

The experience should feel like a coherent survival scenario rather than a sequence of disconnected mob spawns. Players explore a bounded but atmospheric world, gather supplies, reinforce shelters, manage risk, complete objectives and survive escalating nights.

The Java and Bedrock implementations share the same player-facing rules and progression intent. They do not share binaries or assume identical engine internals. Each edition receives its own implementation, world package, compatibility validation and playable test evidence.

## 2. Product pillars

1. **Readable survival pressure:** players understand why danger is increasing and what they can do about it.
2. **Preparation has value:** daylight and safe windows create meaningful decisions.
3. **Defensible space:** doors, windows, walls, gates, lights and fallback positions matter.
4. **Escalating threat:** enemy composition and pressure evolve in readable stages.
5. **Scavenging with trade-offs:** every expedition balances reward, time, noise and exposure.
6. **World tells a story:** abandoned homes, barricades, supply caches and environmental clues explain the outbreak.
7. **Fair difficulty:** attacks are challenging, telegraphed and testable; unavoidable spawn damage is not a design goal.
8. **Cross-edition parity:** core objectives, unlock conditions, wave schedule and victory/defeat rules remain equivalent.
9. **Modular expansion:** advanced systems can be added without rewriting the shared project identity.
10. **Honest verification:** a successful build is not proof that the invasion is playable.

## 3. Player fantasy and setting

The player arrives in a settlement after an outbreak has already begun. Most of the region is abandoned. A small safe zone can be repaired, but its supplies are limited and the surrounding streets become increasingly dangerous after dark.

The player is not expected to defeat an infinite army by fighting alone. Survival comes from preparation, route knowledge, resource management, defensive construction and choosing when to retreat.

The setting should support multiple visual themes later: rural town, forest outpost, industrial district, underground shelter or ruined city. The first map uses one compact settlement theme to keep testing deterministic.

## 4. Core gameplay loop

### Day / preparation phase
1. Review the next threat warning and current objectives.
2. Inspect the base perimeter, repair damage and reposition defensive resources.
3. Choose a short expedition route.
4. Search buildings and points of interest for food, materials, medical supplies and equipment.
5. Return before the danger window or accept the risk of being outside after dark.
6. Craft or place a limited number of defensive upgrades.
7. Secure the shelter and prepare for the attack.

### Night / invasion phase
1. An explicit warning signals the start of the invasion.
2. Zombies approach from designated threat lanes or validated spawn regions.
3. Players defend gates, windows and fallback positions.
4. Structural damage, breaches and player injuries create pressure.
5. Players can fight, distract, retreat or use defensive choke points.
6. The attack ends when its objective conditions are met; survivors receive a short recovery window.

### Recovery / progression phase
1. Show a concise attack report: duration, breaches, damage and resources spent.
2. Allow repair and inventory preparation.
3. Unlock the next objective or threat tier.
4. Repeat with controlled escalation.

## 5. First playable vertical slice

The first playable release should demonstrate the complete loop in a small, authored settlement. It is not the full campaign.

### Required first-slice content
- One compact settlement map with a clearly marked safehouse.
- One player start and one primary defence objective.
- A small set of searchable supply containers or fixed loot points.
- Basic supplies: building material, food/medical recovery item and ammunition-equivalent or combat resource.
- A simple repair/reinforcement interaction using stable, edition-supported mechanics.
- One basic zombie enemy archetype using vanilla-compatible behaviour or a minimal custom variant.
- Three escalating attack nights/waves.
- At least two attack routes or approach lanes.
- A warning and phase transition for each attack.
- A clear survival condition and a clear defeat condition.
- A post-wave report and a restart/replay path.

### Explicit first-slice exclusions
- Open-world procedural generation.
- Large survivor population and complex NPC schedules.
- Full hunger, thirst, temperature and disease simulation.
- Complex firearms, ballistics and weapon attachment systems.
- Vehicles and fuel simulation.
- Persistent multi-session economy.
- Advanced boss AI and large special-zombie roster.
- Cross-server matchmaking, public servers or cloud persistence.
- Experimental Bedrock APIs.
- Unbounded horde simulation.

These exclusions are not permanent product exclusions; they are scope controls for the first playable milestone.

## 6. Threat phases and pacing

The first slice uses three clearly differentiated attacks:

| Phase | Threat intent | Example composition | Player learning goal |
|---|---|---|---|
| Night 1 — Contact | Introduce pressure | Small group of basic zombies | Understand warning, approach and basic defence |
| Night 2 — Breach attempt | Test perimeter | Larger group, split approach | Repair weak points and cover more than one lane |
| Night 3 — Full assault | Validate the loop | Largest basic horde within performance budget | Manage supplies, fallback and survival condition |

Exact spawn counts, timing, health, damage and movement values are balance parameters, not hard-coded design assumptions. They must be measured on both editions and tuned to comparable challenge.

## 7. World and map structure

### First map zones
- **Safehouse:** primary defence objective, spawn/restart point and basic supply storage.
- **Main street:** exposed approach lane with limited cover.
- **Residential block:** searchable buildings and secondary route.
- **Supply point:** higher-value loot location with greater exposure.
- **Fallback position:** secondary defensible space used if the outer perimeter fails.
- **Boundary:** readable playable area that prevents players wandering beyond the test scenario.

### Environmental storytelling
Use broken lighting, blocked roads, warning signs, abandoned vehicles as static scenery, damaged homes and visible barricades. Environmental details should communicate risk and history without requiring dialogue or cinematic systems.

### Navigation
Use landmarks, lighting and simple signage. The player should always be able to identify the safehouse and the current objective. Avoid relying on custom HUD APIs for essential information.

## 8. Zombie archetype roadmap

The full system can grow into the following archetypes. Only the basic archetype is required for the first playable slice.

| Archetype | Role | Signature behaviour | Planned stage |
|---|---|---|---|
| Shambler | Baseline pressure | Slow, persistent pursuit | First slice |
| Runner | Fast flanker | Closes distance quickly, low durability | Later |
| Brute | Perimeter breaker | High durability, high structural pressure | Later |
| Screamer | Horde amplifier | Emits a warning call that attracts nearby threats | Later |
| Spitter | Area denial | Ranged hazard with visible telegraph | Later |
| Crawler | Low-profile ambush | Uses low openings and cluttered spaces | Later |
| Armoured | Tactical threat | Resists selected damage types | Later |
| Exploder | Breach threat | Dangerous close-range area effect with clear warning | Later |
| Alpha / boss | Set-piece encounter | Multi-stage, telegraphed attack pattern | Later |

Every archetype must have a distinct gameplay purpose, counterplay, spawn rules, performance budget and target-specific parity classification. Special abilities that require unsupported or experimental APIs are deferred or redesigned.

## 9. Horde director and spawn governance

A future Horde Director controls threat pacing. It should not spawn unlimited entities.

Responsibilities:
- Select an attack profile based on the current phase.
- Respect maximum active entity budgets per target and test environment.
- Prefer approved approach zones and avoid spawning directly on top of players.
- Avoid protected safehouse spawn volumes unless a specific breach rule permits entry.
- Maintain minimum warning and reaction time.
- Stop or reduce spawning when performance thresholds are exceeded.
- Track active, defeated, despawned and stuck entities.
- Recover safely after player death, world reload or phase interruption.

First-slice implementation may use deterministic wave tables rather than a fully adaptive director. Adaptive difficulty is a later layer.

## 10. Base defence and structural damage

Long-term defence categories:
- Doors, gates and windows.
- Barricades and reinforcement panels.
- Perimeter walls and choke points.
- Lighting and alarm devices.
- Traps and distraction devices.
- Repair stations and fallback shelters.

First slice uses a deliberately small set of repairable or reinforceable defence points. Structural health must be represented consistently and visibly; avoid silently changing block states without feedback.

The first release does not require arbitrary destruction of every world block. Target-specific block interactions must be safe, bounded and reversible.

## 11. Scavenging and loot

Loot categories:
- Construction materials.
- Food and basic recovery.
- Medical supplies.
- Combat supplies.
- Utility items such as light sources.
- Objective-critical items.

First slice uses fixed, authored loot placements or deterministic loot tables so acceptance tests are repeatable. Randomized loot weights can be introduced later with seeded test fixtures.

Loot rules:
- No critical objective item may become permanently inaccessible.
- Supply value should correspond to exposure and travel risk.
- Repeated farming exploits must be considered before adding respawnable containers.
- The player receives clear feedback when an item is collected or a container is empty.

## 12. Crafting and progression

Future crafting tiers:
1. Improvised repairs and basic barricades.
2. Reinforced defences and improved tools.
3. Advanced traps, alarms and specialised equipment.
4. Late-game shelter systems and high-risk expedition gear.

First slice only needs a small, explicit recipe set or predefined upgrade interactions. A full crafting economy is deferred.

Progression should be objective-driven rather than requiring large amounts of grind. Unlocks must be recorded in the project specification and be equivalent in gameplay outcome across editions.

## 13. Survivor and NPC roadmap

Potential future survivor roles:
- Medic: recovery and medical supply efficiency.
- Engineer: repair and construction bonuses.
- Scout: route and threat information.
- Guard: defensive assistance.
- Quartermaster: inventory and supply management.

Survivor recruitment, morale, schedules, trust, injuries and task assignment are advanced systems. They are not required for the first playable slice. Do not imply NPC companions exist until their AI, pathfinding and interaction are implemented and tested.

## 14. Survival needs and status effects

Potential later systems:
- Health and injury.
- Hunger and thirst.
- Fatigue and sleep.
- Infection and contamination.
- Temperature and weather exposure.
- Bleeding, recovery and medicine.

For the first slice, use the edition's reliable health/death systems and one simple recovery mechanism if required. Avoid introducing multiple meters before the core invasion loop is proven.

## 15. Sound, lighting and atmosphere

Atmosphere should reinforce gameplay:
- Distant groans or warning sounds before an attack.
- Distinct phase-start and phase-end cues.
- Visible night lighting and safehouse illumination.
- Environmental darkness without making navigation unreadable.
- Clear sound/visual telegraphs for later special zombies.

Custom audio and extensive animation are optional for the first slice. If included, they must not obscure essential combat feedback or require unverified client APIs.

## 16. Difficulty and fairness

Difficulty dimensions:
- Number of active enemies.
- Attack duration.
- Approach route count.
- Time between warning and contact.
- Resource availability.
- Defence durability.
- Recovery window.

Change a limited number of dimensions between the three first-slice nights so testers can identify why difficulty changed.

Fairness rules:
- No unavoidable spawn directly beside the player.
- No critical objective blocked by random loot.
- No invisible attack state.
- No instant, unexplained base destruction.
- Provide a viable response to every introduced threat.
- Death and restart must not corrupt the scenario state.

## 17. Multiplayer direction

The product should be designed so cooperative play can be added without changing the project identity. However, player count, dedicated-server support, shared inventory rules, revive mechanics, friendly fire, host migration and network authority remain separate decisions.

The first slice must not claim multiplayer support unless it has been run and passed on both target editions in an identified multiplayer environment.

## 18. Java and Bedrock implementation boundaries

### Java 26.3 + Fabric
- Fabric mod owns custom Java gameplay registrations and server-authoritative mechanics.
- Java world/map is delivered as a compatible world.
- Java datapack may own suitable data-driven functions, tags, loot tables or recipes where that separation is useful.
- Resource pack contains Java-specific assets.
- Fabric API and loader versions are pinned only after official compatibility verification at implementation start.

### Bedrock 26.60
- Behavior pack owns Bedrock gameplay definitions and supported logic.
- Stable `@minecraft/server` 2.11.0 may be used where required.
- Resource pack contains Bedrock-specific assets.
- World is delivered with the correct pack dependencies and manifest references.
- Experimental APIs and beta-only dependencies are prohibited in the first playable path.

### Shared design contract
- Shared feature IDs, objective semantics, phase names, progression conditions and acceptance tests.
- Separate target adapters, entity definitions, asset formats and runtime event handling.
- A parity record per feature: equivalent, adapted, unsupported or not verified.
- Never force identical implementation where platform mechanics differ.

## 19. Project manifest and dependency graph

The project manifest should identify:
- Shared gameplay profile: zombie invasion.
- Target profiles: Java 26.3/Fabric and Bedrock 26.60.
- Target-owned mod/add-on, world, datapack and resource-pack components.
- Cross-component dependency edges.
- Required stable API policy.
- Feature parity and verification state.
- Build outputs and test evidence.

A component cannot be marked complete merely because its dependency exists in the manifest. The generated artifact and integration evidence must be present.

## 20. Test strategy

### Static / content validation
- Manifest and pack metadata valid.
- Referenced assets and identifiers resolve.
- No experimental Bedrock API dependency.
- No duplicate identifiers or missing required files.
- World references and pack dependencies are valid.

### Build / packaging
- Java mod builds with pinned Fabric toolchain.
- Bedrock packs validate and package for the selected version.
- Target bundles contain correct assets and dependency metadata.

### Load / import
- Java client loads the mod and world without fatal errors.
- Bedrock imports the world and required packs without fatal errors.
- Correct target version and pack activation are recorded.

### Gameplay acceptance
1. Start the scenario from a clean world.
2. Find and collect the intended supplies.
3. Reinforce at least one defence point.
4. Receive a warning before each invasion.
5. Survive or fail according to defined conditions.
6. Verify attack completion and recovery transition.
7. Complete all three escalating phases.
8. Restart and replay without corrupted state.

### Performance and stability
- Measure active entity count, tick health/performance and memory where available.
- Check stuck entities and invalid spawn positions.
- Verify restart and world reload.
- Record device, edition, version, loader/API, test steps and results.

## 21. Failure, recovery and replay

The scenario needs explicit state transitions:
- PREPARATION
- WARNING
- INVASION_ACTIVE
- RECOVERY
- VICTORY
- DEFEAT
- RESETTING

Transitions must be idempotent where possible. Reset must restore wave counters, objective state, defence state and fixed loot state. Player death must not leave the invasion permanently stuck.

## 22. Accessibility and user experience

- Objective text must be concise and understandable.
- Essential state cannot be communicated only through colour or sound.
- Warnings need both text/visual and audio where feasible.
- Players must be able to distinguish safehouse, supply and threat zones.
- Difficulty and key bindings should respect native platform controls.
- Avoid excessive screen overlays.

## 23. Telemetry and balance evidence

For local testing, record only scenario-relevant metrics:
- Time to first contact.
- Duration of each wave.
- Number of enemies spawned/defeated/remaining.
- Defence breaches and repairs.
- Player deaths and objective completion.
- Performance warnings and stuck-entity count.

No personal telemetry or cloud collection is required for the first slice. Any later telemetry requires a separate privacy and consent design.

## 24. Content authoring and AI generation

The AI may help generate:
- Settlement layout plans.
- Loot placement plans.
- Wave tables and encounter composition.
- Objective text and environmental storytelling.
- Asset briefs and resource-pack manifests.
- Test scenarios and balance variants.

AI output must be validated against target constraints before inclusion. AI-generated content is a proposal until accepted by the project planner and user approval gate. Generated map geometry must remain editable and reproducible.

## 25. Expansion roadmap

### Stage 1 — First playable
Compact settlement, safehouse, basic zombie, scavenging, repairs, three attack nights, victory/defeat, restart, Java and Bedrock parity.

### Stage 2 — Survival depth
More loot categories, basic crafting, hunger/thirst options, additional defensive structures, more attack layouts and difficulty settings.

### Stage 3 — Zombie roster
Runner, brute, crawler and one special archetype at a time, each with counterplay and performance budgets.

### Stage 4 — Settlement and survivors
Rescue objectives, survivor NPC roles, morale, tasks, shelter upgrades and settlement progression.

### Stage 5 — Expanded world
Multiple districts, controlled procedural points of interest, vehicles, weather, day/night scheduling and expedition routes.

### Stage 6 — Cooperative and scenario tools
Validated multiplayer, server configuration, scenario editor, custom wave authoring, modpack integration and community publishing.

Each stage requires its own approved scope and target-specific acceptance evidence.

## 26. Open design decisions

The user selected the Zombie Invasion concept and requested the most detailed treatment. The following parameters remain open and must not be silently assumed:
1. Solo-only first slice or cooperative multiplayer requirement.
2. Camera/visual perspective: standard Minecraft first/third person is assumed; no custom camera.
3. First map theme: small town, rural village, military outpost or industrial district.
4. Attack schedule: fixed three nights for the first slice is recommended.
5. Player death: immediate restart, limited lives or spectator/revive.
6. Victory condition: survive the third night or complete a final objective after the third wave.
7. Resource scarcity: fixed curated supplies or seeded randomized loot.
8. Build permissions: designated repair points or free-form defensive construction.
9. Combat style: vanilla weapons/tools initially or custom weapons in first slice.
10. Multiplayer and dedicated server milestone.
11. Whether the first map should be authored only or include controlled procedural variation.

## 27. Recommended defaults for the first playable slice

These are proposals, not user-confirmed decisions:
- One compact abandoned town map.
- Three fixed escalating night attacks.
- Standard Minecraft first/third-person camera.
- Single-player acceptance first; cooperative support remains a later milestone unless user requires it now.
- Fixed, authored loot placement.
- Designated repair/reinforcement points rather than unrestricted block destruction.
- Vanilla-compatible combat baseline; custom weapon systems deferred.
- Survive the third attack and activate a clearly marked extraction/evacuation objective.
- Immediate replay/reset after defeat or victory.

## 28. Implementation boundary

This is a gameplay design specification. It does not implement zombie AI, wave scheduling, maps, loot, crafting, NPCs, packs or playable outputs. Application source code remains unchanged. The coding gate remains closed until the first-slice choices are resolved or explicitly deferred and the master design baseline is approved.


## 29. User decision — single-player first release (2026-11-28)

The user accepted a **single-player first playable experience**. The first-slice gameplay and acceptance tests therefore assume one player. Cooperative multiplayer and dedicated-server support are deferred to a later milestone and are not required to declare the first slice complete.

This is a scope decision, not a permanent prohibition: the architecture should avoid unnecessary single-player-only assumptions where doing so is low-cost, but multiplayer must not delay or complicate the first playable release. No multiplayer support may be claimed until separately implemented and tested.


## 30. User decision — abandoned expandable town map (2026-11-28)

The user approved an **abandoned, expandable town** as the first map direction. Planned landmark vocabulary includes residential houses, hospital, police station, market, gas station, military checkpoint and underground shelter.

The first playable map remains a compact authored district around the safehouse. The full landmark set is a long-term map plan; not every building must be fully functional in the first slice. Detailed layout, attack lanes, loot policy, target parity and map acceptance criteria are in `docs/ZOMBIE_INVASION_MAP_DESIGN_V1.md`.
