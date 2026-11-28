# Zombie Invasion — Encounter Director Design V1

Status: **DESIGN PROPOSAL — scenario timing and balance awaiting approval**
Date: 2026-11-28

## 1. Purpose

The Encounter Director controls when, where and in what composition hostile groups enter the first-slice scenario. It translates approved scenario phases into bounded spawn requests and coordinates the approved roster:

- Walker — baseline enemy.
- Runner — fast pressure enemy.
- Brute — durable defence-pressure enemy.

The roster itself is user-approved. This document does not approve exact wave counts, timings, difficulty values or the previously proposed three-night extraction scenario.

## 2. Responsibilities

The director owns:
- Scenario phase and encounter progression.
- Spawn-group selection from approved archetypes.
- Spawn-point validation and safehouse exclusion.
- Active-hostile and weighted encounter budgets.
- Difficulty profile application.
- Spawn pacing and warning cues.
- Cleanup and state reset integration.
- Runtime safety limits and diagnostic counters.

It does not own:
- Individual zombie navigation and combat state machines.
- Loot generation or inventory.
- Map geometry authoring.
- Player health, death or restart policy.
- Final victory/extraction rules.

Those systems communicate through explicit interfaces and shared scenario state.

## 3. Logical lifecycle

1. **DISABLED** — scenario not active.
2. **PREPARING** — validate configuration, spawn points and target capabilities.
3. **ACTIVE** — schedule and dispatch eligible encounter groups.
4. **PAUSED** — no new groups are dispatched; existing enemies follow the scenario's pause policy.
5. **COMPLETING** — stop new spawns and resolve or clean up remaining scenario enemies.
6. **STOPPED** — scenario ended.
7. **RESETTING** — clear scenario-owned state and return to a known baseline.
8. **ERROR_SAFE** — stop new spawns and report a recoverable configuration/runtime fault.

Transitions must be explicit, idempotent where possible and safe if invoked more than once.

## 4. Encounter group definition

Each encounter group should be data-driven and include:

- Stable group ID and schema version.
- Eligible scenario phase.
- Archetype composition and count ranges.
- Weighted budget cost.
- Minimum and maximum active-hostile constraints.
- Spawn-point tags or lane preferences.
- Minimum distance and visibility rules.
- Delay/cooldown constraints.
- Warning cue identifier.
- Retry/fallback policy if no valid spawn point exists.

No user-authored or AI-generated group is executable until validated against the schema, target capabilities and approved project manifest.

## 5. Budget model

Use two simultaneous limits:

- **Entity cap:** maximum number of active scenario hostiles.
- **Weighted threat budget:** each archetype consumes a configurable cost; Brutes cost more than Walkers, and Runners may have a distinct cost reflecting their pressure.

The exact values are not fixed in this document. They must be tuned independently for Java and Bedrock runtime performance while preserving equivalent player-facing difficulty.

A spawn request is rejected or deferred when either budget would be exceeded. The director must never bypass a cap to satisfy a scheduled wave.

## 6. Spawn validation

Before dispatch, validate:
- Spawn point belongs to the active map and approved spawn registry.
- Position is loaded and suitable for entity placement.
- Position is not inside solid blocks or an inaccessible cavity.
- Spawn is outside the safehouse protected zone.
- Spawn is not an unfair immediate-hit position adjacent to the player.
- Spawn lane is not blocked in a way that guarantees a stuck entity.
- The selected archetype is enabled for the current phase and target.
- Entity and weighted budgets remain available.

If validation fails, try a bounded list of alternative points. If none are valid, defer the group or report a controlled encounter failure. Never loop indefinitely.

## 7. Pacing and fairness

- Introduce threats with readable warning cues where the scenario permits.
- Avoid simultaneous spawn bursts that overwhelm a solo player without counterplay.
- Keep a minimum recovery interval between high-pressure groups.
- Use encounter composition to create variety rather than only increasing health and damage.
- Ensure the player can understand likely attack lanes and reach meaningful defensive choices.
- Do not spawn enemies inside the safehouse or protected interaction zones.
- Avoid scaling difficulty from hidden or personal telemetry.

## 8. Cross-edition contract

Java Edition 26.3 + Fabric and Bedrock Edition 26.60 + stable `@minecraft/server` 2.11.0 must implement separate runtime adapters.

The shared contract covers:
- Phase semantics.
- Encounter-group schema.
- Archetype identifiers.
- Budget accounting outcomes.
- Spawn validation rules.
- Pause, stop, cleanup and reset semantics.
- Diagnostic result categories.

Runtime scheduling frequency, entity APIs and internal data structures may differ. Experimental Bedrock APIs are prohibited in this first-slice path. If a behavior cannot be implemented reliably on both targets, the feature must be reduced or deferred with an explicit parity exception; silent divergence is not acceptable.

## 9. Failure handling

- Invalid group configuration: reject before scenario activation.
- No valid spawn point: bounded retry, then defer and record reason.
- Entity creation failure: release reserved budget and record failure.
- Entity exceeds lifetime/area constraints: invoke approved recovery or cleanup policy.
- Director fault: enter ERROR_SAFE and stop new spawn dispatch.
- Scenario end/restart: stop dispatch before cleaning scenario-owned entities.

Errors must be visible in test reports. They must not be hidden by silently marking an encounter complete.

## 10. Diagnostics and balance evidence

Record scenario-local counters:
- Spawn requests, accepted, deferred, rejected and failed.
- Active entity count and weighted budget peak.
- Per-archetype spawn and defeat counts.
- Invalid spawn-point reasons.
- Navigation recovery and stuck-entity counts.
- Phase duration and player outcome.
- Runtime performance warnings.

Do not collect personal telemetry or transmit data to a cloud service for the first slice.

## 11. Acceptance tests

Run separately on both target editions:

1. Director cannot spawn while DISABLED, STOPPED or ERROR_SAFE.
2. Valid group activates only in an eligible phase.
3. Entity and weighted budgets are never exceeded.
4. Invalid spawn points are rejected.
5. Safehouse and immediate-hit exclusion rules hold.
6. Failed entity creation releases reserved budget.
7. No-valid-point fallback is bounded and terminates.
8. Pause prevents new dispatch according to policy.
9. Stop prevents all future dispatch.
10. Reset cleans only scenario-owned hostiles and restores director state.
11. Repeated start/stop/reset calls do not duplicate groups or corrupt counters.
12. Solo-player playtests show each approved archetype has readable counterplay.
13. Equivalent scenario outcomes are verified on Java and Bedrock.

Tests not executed must be marked NOT_RUN. Static validation, successful packaging and actual in-game runtime tests must be reported separately.

## 12. Open decisions

The following remain unresolved and must not be inferred from the approved roster:
- Whether the first scenario uses three nights, continuous waves or another schedule.
- Whether victory requires survival alone or a final extraction objective.
- Exact phase durations and warning intervals.
- Exact spawn counts, entity cap and weighted costs.
- Difficulty presets and any adaptive scaling.
- Whether pause freezes existing enemies or only suspends new dispatch.
- Whether restart behavior follows the proposed death/restart policy.

## 13. Implementation boundary

This is a design specification only. It does not implement a spawn director, entity AI, map, scenario, mod, add-on or playable artifact. Application source code remains unchanged.
