# Zombie Invasion — Three-Night Extraction Scenario v1.0

**Status:** Recommended first-slice scenario proposal — awaiting explicit user confirmation  
**Date:** 2026-11-28  
**Targets:** Minecraft Java 26.3 + Fabric; Minecraft Bedrock 26.60 + stable Script API 2.11.0 where required  
**Player count:** Single-player  
**Experimental Bedrock APIs:** Disabled

## 1. Purpose

Define a compact, testable ending for the first playable Zombie Invasion scenario. The proposed structure connects the already selected abandoned town, safehouse, market, hospital and police station into one readable survival arc.

This document is a proposal. It does not record the three-night schedule or extraction ending as a user-confirmed decision until the user explicitly approves it.

## 2. Scenario premise

The player is isolated in an abandoned town after an outbreak. The safehouse is the primary defence objective. A working radio eventually receives an evacuation transmission. The player must prepare, endure escalating attacks, then reach a designated extraction point.

The scenario should remain completable by one player without requiring multiplayer, external servers, survivor NPCs or experimental APIs.

## 3. Proposed mission sequence

### Phase 0 — Arrival and orientation

- Spawn the player at or immediately beside the safehouse.
- Introduce the safehouse, objective marker/signage and basic controls through concise in-world guidance.
- Establish the initial objective: secure the shelter and search nearby supplies.
- Keep the first minutes free of overwhelming enemy pressure.

### Day 1 — Scavenge and prepare

- The player can search the market for food and general supplies.
- The player can search the hospital for medical supplies and use the approved basic recovery interaction.
- The player can search the police station for tactical and defence supplies within the first-slice combat scope.
- The player collects a limited set of construction/repair materials.
- The player reinforces a small number of designated safehouse defence points.
- A clear warning announces the first attack window.

### Night 1 — Initial contact

- A small, readable group of baseline zombies approaches through a marked attack lane.
- The player learns to defend, reposition and use repaired barriers.
- The phase ends when its bounded attack objective is met, not through unlimited spawning.
- A recovery report communicates damage, remaining threats and repair needs.

### Day 2 — Repair and resupply

- The player repairs damaged designated defence points.
- Remaining supply locations can be searched if not already looted.
- The player receives a warning that the next attack will use more than one approach lane.
- The player can choose where to spend limited repair materials.

### Night 2 — Perimeter pressure

- A larger baseline horde approaches using at least two validated lanes.
- The attack tests whether the player prepared more than one side of the safehouse.
- A bounded breach or fallback condition may be used, but the player must receive clear feedback.
- The phase ends in a recovery state with an updated report.

### Day 3 — Final preparation

- The player receives an explicit escalation warning.
- The safehouse can be repaired one final time using remaining resources.
- The radio begins to provide an evacuation signal or a clear objective hint.
- The extraction destination is identified before the final attack begins; it must not be a hidden or randomly inaccessible point.

### Night 3 — Final assault

- The largest first-slice attack begins, within measured entity and performance budgets.
- The horde uses the established approach lanes and does not spawn directly on the player.
- The player must meet the approved survival condition long enough for the evacuation transmission to complete.
- When the final assault objective is met, the scenario transitions to EXTRACTION_READY.

### Extraction — Final objective

- A clear radio message announces that the evacuation route is available.
- The player leaves the safehouse and follows a readable, bounded route to the extraction point.
- The route presents tension but does not require an unapproved boss, vehicle, NPC convoy or multiplayer mechanic.
- Entering the extraction zone and interacting with its completion trigger ends the scenario.
- The result screen records completion and offers restart/replay.

## 4. Scenario state model

Proposed states:

`INTRO → DAY_1_PREPARATION → NIGHT_1 → DAY_2_PREPARATION → NIGHT_2 → DAY_3_PREPARATION → NIGHT_3 → EXTRACTION_READY → EXTRACTION_ACTIVE → VICTORY`

Failure path:

`Any active survival phase → DEFEAT → RESULTS → RESET`

Reset must restore wave counters, objective state, defence points, fixed loot state, radio progression and extraction trigger. Repeated reset must not duplicate entities or leave stale scenario flags.

## 5. Victory and defeat proposal

### Proposed victory conditions

All of the following must be true:
1. The player completes the third attack's survival objective.
2. The extraction objective becomes available.
3. The player reaches the marked extraction zone.
4. The player activates the completion trigger.

Surviving the third wave alone does not finish the scenario; extraction is the final playable objective.

### Proposed defeat conditions

- Player death under the target edition's agreed death/restart policy; or
- A clearly defined safehouse failure condition, if the first-slice design chooses one.

A safehouse failure must never occur invisibly or through an untelegraphed instant block destruction. The exact death/restart rule and whether safehouse destruction can independently cause defeat remain open.

## 6. Required map connections

The first playable district connects:
- Safehouse — spawn, defence objective and radio.
- Residential block — route navigation and limited supplies.
- Market — food and general supplies.
- Hospital — medical supplies and recovery interaction.
- Police station — tactical and defence supplies.
- Two or more attack lanes — validated approach paths.
- Extraction zone — final objective, reachable through a clearly signposted route.

The extraction point may be placed at the edge of the authored district, such as a secured road checkpoint. It must not imply that the military checkpoint is fully simulated unless that location is separately included in scope.

## 7. First-slice feature boundaries

Included in this scenario proposal:
- One player.
- One compact authored abandoned-town district.
- Functional market, hospital and police station.
- One baseline zombie archetype.
- Three escalating attack phases.
- Day/preparation and night/attack transitions.
- Fixed or deterministic authored loot for repeatable tests.
- Designated repair/reinforcement points.
- Radio warnings and objective updates.
- One marked extraction route and completion trigger.
- Victory, defeat, results and reliable replay/reset.

Not implied by this proposal:
- Multiplayer or dedicated servers.
- Fully simulated survivors or rescue convoy.
- Vehicles or drivable evacuation.
- Custom firearms, ballistics or weapon attachments.
- Special zombie roster or boss fight.
- Procedural open world.
- Full hunger, thirst, temperature or disease simulation.
- Persistent campaign or save progression across multiple scenarios.

## 8. Cross-edition implementation contract

Java and Bedrock must implement equivalent player-facing sequence and acceptance outcomes using separate native components.

- Java: Fabric mod owns scenario state and custom interactions; Java world and optional datapack/resource pack provide the map and content.
- Bedrock: behavior pack and stable Script API 2.11.0 only where necessary; Bedrock world/resource pack provide the map and content.
- Experimental Bedrock APIs remain prohibited.
- Shared objective IDs, phase names, transition rules and acceptance tests must be represented in the shared project manifest.
- Edition-specific differences must be documented; neither target may inherit the other's test result.

## 9. Acceptance test outline

For each edition independently:
1. Start a fresh world and verify the player spawns at the safehouse.
2. Search all three functional buildings and collect their intended categories of supplies.
3. Verify searched containers/points update to their looted state.
4. Reinforce at least one designated defence point.
5. Receive a warning before each of the three attacks.
6. Verify attacks escalate and use the expected approach lanes.
7. Verify no zombie spawns directly on the player and entity counts stay within budget.
8. Complete each attack and enter the correct preparation/recovery state.
9. Receive the extraction transmission after the final attack.
10. Navigate to the extraction point and activate the completion trigger.
11. Verify victory/results and restart.
12. Replay from a clean scenario state without duplicated entities, stale flags or missing loot.

A test not executed on its target runtime must be marked NOT_RUN. A successful build alone does not establish playability.

## 10. Open decisions before implementation

The following remain unconfirmed:
- Whether the user approves the three-night schedule and extraction ending.
- Exact time scale and duration of each preparation/attack phase.
- Whether the safehouse can be breached and what constitutes objective failure.
- Player death and restart policy.
- Whether extraction is an interaction trigger, timed hold-zone or another stable cross-edition mechanism.
- Exact loot quantities and wave counts, to be tuned after performance tests.
- Whether the extraction location is a road checkpoint or another landmark.

## 11. Implementation boundary

This document is a scenario design proposal only. No game code, map, mod, add-on, world package or playable artifact has been generated by this document. The coding gate remains closed pending completion and approval of the design baseline.
