# Zombie Invasion — Zombie Roster Design V1

Status: **USER-APPROVED FIRST-SLICE ROSTER — design specification; not implemented**
Date: 2026-11-28

This document proposes a staged enemy roster for the first playable Zombie Invasion slice. It does not authorize implementation and does not mark any proposed archetype as user-approved.

## 1. Design goals

- Preserve a readable difficulty curve in a compact single-player scenario.
- Give each enemy a distinct tactical role and recognizable counterplay.
- Keep shared gameplay semantics consistent across Java Edition 26.3 + Fabric and Bedrock Edition 26.60 + stable `@minecraft/server` 2.11.0.
- Avoid experimental Bedrock APIs.
- Keep entity counts, navigation work, target acquisition and special effects within explicit performance budgets.
- Make difficulty arise from encounter composition and pressure, not only inflated health.

## 2. Proposed first-slice roster

### 2.1 Walker — normal zombie

Role: baseline pursuer and the most common enemy.

- Movement: standard ground pursuit; no exceptional burst movement.
- Durability: baseline.
- Damage: baseline melee damage.
- Perception: acquires the player within a configured detection range, subject to line-of-sight and noise rules selected by the encounter system.
- Group behavior: may form small groups; no complex squad coordination is required.
- Counterplay: maintain distance, use chokepoints, manage ammunition/tools and avoid being surrounded.
- Spawn role: establishes the baseline threat in all attack phases.

### 2.2 Runner — fast zombie

Role: pressure and target disruption.

- Movement: faster than Walker, with lower durability.
- Damage: equal to or modestly above baseline only if balance tests justify it; speed is its primary threat.
- Behavior: closes distance quickly and punishes exposed players or poorly covered approaches.
- Counterplay: narrow routes, obstacles, prepared defence points and accurate early engagement.
- Spawn role: introduced in controlled numbers after the player has learned the baseline loop.

### 2.3 Brute — durable zombie

Role: breach pressure and defence-point threat.

- Movement: slower than Walker.
- Durability: substantially higher than Walker, with no arbitrary immunity to ordinary damage.
- Damage: high enough to make close contact dangerous, but bounded for solo play.
- Behavior: advances persistently toward the player or a designated scenario target; it must not destroy arbitrary world blocks.
- Counterplay: focus fire, distance, route planning and use of the environment.
- Spawn role: limited appearances in later attack phases; never use large groups of Brutes in the first slice.

## 3. Deferred archetypes

These are future candidates, not first-slice requirements:

- **Screamer:** emits an alert that attracts nearby zombies. Needs clear audio/visual telegraphing and a cooldown to avoid endless chain-spawning.
- **Exploder:** creates a dangerous area effect after a readable fuse/telegraph. Must not cause uncontrolled terrain destruction.
- **Poisoner:** applies a bounded status effect with visible warning and a reliable recovery/counterplay path.
- **Crawler:** uses low-profile movement and alternate navigation constraints; defer until pathfinding and accessibility tests exist.
- **Armored variant:** uses a readable protection mechanic rather than simply extreme health; defer until equipment and damage feedback are mature.

No deferred archetype should enter the first playable build without a new scope decision, cross-edition compatibility review and acceptance tests.

## 4. Encounter progression proposal

The following is a balancing proposal, not a confirmed scenario schedule:

- Early phase: Walker only, low simultaneous entity count.
- Middle phase: Walker groups with a small, clearly signalled Runner presence.
- Late phase: Walker pressure with rare Runner and a limited Brute appearance.
- Final encounter: composition is tuned to the selected victory/extraction objective and solo-player test evidence.

Exact spawn counts, timings, health, speed, damage, detection ranges and cooldowns must be data-driven and tuned through repeatable tests. This document intentionally does not invent final numeric balance values.

## 5. Shared behavior contract

Each archetype must expose equivalent gameplay semantics on both editions:

- Stable archetype identifier and configuration version.
- Health, movement profile, attack profile and target-selection policy.
- Spawn eligibility and encounter-budget cost.
- Detection, pursuit, attack, recovery and despawn/death states.
- Damage feedback and readable threat cues.
- Cleanup behavior when the scenario ends or restarts.
- Deterministic test hooks where the target platform permits them.

Java and Bedrock implementations may use different engine APIs and internal state mechanisms. They must not be forced into identical code. Parity means equivalent player-facing rules and verified outcomes.

## 6. AI state model

Minimum logical states:

1. Idle / Spawned
2. Investigate
3. AcquireTarget
4. Pursue
5. Attack
6. Recover
7. Staggered (only if enabled by the approved combat rules)
8. Dead / Cleanup

State transitions must be bounded and must not create permanent loops. If navigation fails, the entity should retry a limited number of times, select a valid fallback route or be safely recovered by scenario logic. It must not remain permanently stuck while consuming unbounded processing.

## 7. Performance and fairness constraints

- Encounter director enforces a maximum active-hostile budget.
- Brutes and future special types consume a higher budget cost than Walkers.
- Spawn points must be outside unfair immediate-hit zones and must respect safehouse protections.
- Avoid spawning inside solid blocks, inaccessible cavities or directly on the player.
- Avoid continuous expensive target scans; use bounded update intervals and event-driven updates where supported.
- All special attacks require readable telegraphing and a counterplay window.
- No archetype may rely on experimental Bedrock APIs in the approved first-slice target.
- If a target cannot meet the behavior contract reliably, reduce or defer that archetype rather than silently weakening parity.

## 8. Acceptance tests

For each included archetype, test on both editions:

- Correct spawn eligibility and encounter-budget accounting.
- Correct health, movement and attack profile within agreed tolerances.
- Target acquisition and pursuit in open terrain and around the town's common obstacles.
- No spawning inside blocks or protected safehouse space.
- No permanent navigation loops or excessive stuck entities.
- Correct cleanup on death, scenario defeat, victory and restart.
- Solo-player fairness across repeated runs.
- Performance under the maximum approved encounter composition.

A test not executed must be recorded as NOT_RUN. A successful package build is not evidence that the enemy works in-game.

## 9. User-approved first-slice roster (2026-11-28)

The user explicitly selected **Option C: Walker + Runner + Brute** for the first playable slice.

- Walker is the baseline common enemy.
- Runner adds controlled speed pressure.
- Brute is a limited high-durability threat intended to pressure defence positions.
- Encounter budgets, solo-player fairness, target parity and performance tests are mandatory.
- Screamer, Exploder, Poisoner, Crawler and Armored variants remain deferred and are not first-slice requirements.

This approval confirms the roster scope only. It does not approve exact health, speed, damage, spawn counts, timings or other balance values; those remain subject to tuning and test evidence.

## 10. Implementation boundary

This is an approved design specification, not an implementation. No entity, AI, spawn director, animation, sound, pack, mod or playable artifact has been implemented by this document. Application source code remains unchanged.
