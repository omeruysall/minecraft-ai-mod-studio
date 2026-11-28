# Combat & AI Behavior Engine Specification

**Document status:** Design draft  
**Version:** 0.1  
**Implementation status:** Not implemented; design requirements only.  
**Approval status:** Awaiting product decisions and baseline approval.

## 1. Purpose and boundaries
Define the combat and tactical AI subsystem for generated Minecraft projects. It supports hostile, neutral, elite, boss, companion, and squad combat. It complements the NPC & Character Engine: that system owns character identity, dialogue, appearance, relationships, and general schedules; this engine owns combat states, target decisions, tactics, attacks, abilities, encounter behavior, and balance.

## 2. Design principles
- Generation is blocked until the exact project-plan revision is approved.
- Java, Bedrock, datapack, resource-pack, and world capabilities must be distinguished honestly.
- AI autonomy is bounded by goals, permissions, world boundaries, and resource budgets.
- Multiplayer-critical state and damage are server authoritative.
- Behavior is inspectable, explainable, configurable, and testable.
- Missing targets, unloaded chunks, failed navigation, and unavailable abilities must produce safe fallbacks.
- Build or packaging success alone never proves gameplay functionality.

## 3. Scope
In scope: state machines, behavior trees or utility selection, perception, target acquisition, threat, navigation, melee/ranged/area attacks, defense, abilities, status effects, boss phases, squad coordination, companions, factions, difficulty, encounter orchestration, multiplayer, persistence, performance, diagnostics, testing, and repair.

Out of scope: character backstory and dialogue, general terrain generation, full player economy/progression, replacing the vanilla combat system wholesale, and unbounded self-modifying agents.

## 4. Runtime ownership
The Project Architect assigns every feature to a runtime owner:
- **Java mod:** custom entity AI/goals, advanced pathing, custom damage, boss logic, squad coordination, authoritative server logic.
- **Bedrock add-on:** supported entity components, events, behaviors, animations, and Script API for the selected version. Experimental or unsupported capabilities must be disclosed.
- **Datapack:** bounded data-driven mechanics using supported functions, predicates, advancements, scoreboards, and tags. It must not be presented as equivalent to arbitrary Java AI.
- **Resource pack:** combat visuals, animations, sounds, particles where supported, icons, and localization; not authoritative combat logic.
- **World/map:** arenas, encounter placement, spawn conditions, environmental layout.
- **Quest/story engine:** owns narrative objectives and progression; consumes validated combat events.

Each feature records owner, platform/version, dependencies, fallback, and test method.

## 5. Behavior architecture
Use a high-level finite-state machine (FSM) for authoritative lifecycle and a behavior tree or utility selector for tactical action choice. Candidate states include dormant, patrol, suspicious, alert, pursue, engage, reposition, defend, retreat, disabled, and defeated. Each transition requires guards, timeout/interruption rules, and fallback. The authoring model may vary by platform, but any loss of capability during translation must be shown to the user.

## 6. Perception and awareness
Inputs may include vision, field of view, line of sight, sound/noise, damage received, ally alerts, proximity, hazards, and scripted triggers. Every channel defines support, range, occlusion, sensitivity, update cadence, awareness decay, and whether information can be shared with allies. Agents must not have omniscient knowledge of hidden players unless explicitly approved.

## 7. Targeting and threat
Target scoring may consider distance, line of sight, recent damage, threat, vulnerability, role, protected objectives, and encounter scripting. Define acquisition and retarget thresholds, retention, loss timeout, search behavior, faction permissions, and safe handling of invalid/unloaded targets. Avoid rapid target oscillation. Threat is not assumed to be identical to vanilla aggro; implementation and synchronization are platform-specific.

## 8. Movement and tactics
Supported intents may include approach, maintain range, circle, flank, retreat, cover, hold, guard, pursue, escape hazards, and regroup. Planning accounts for terrain, doors, elevation, arena boundaries, collision, crowding, line of sight, projectile constraints, chunk loading, and server tick budgets. Path failures use bounded retries and safe fallback; expensive path requests must not run every tick without throttling.

## 9. Roles and archetypes
Editable templates may include bruiser, skirmisher, ranged attacker, artillery/area denial, defender, support, summoner/controller, assassin, elite/champion, and multi-phase boss. Each template declares engagement range, mobility, survivability, threat profile, preferred actions, counters, and team interactions. Templates are not fixed classes.

## 10. Attacks, damage, and abilities
Every attack definition records stable ID, delivery type, startup/active/recovery/cooldown, range/area, target and line-of-sight rules, damage type/value where supported, knockback, interruption, status effects, friendly-fire behavior, cost, cancellation, telegraph, and platform limitations.

Abilities may be passive, active, reactive, defensive, mobility, control, or special. They require activation conditions, target rules, cooldown, cost, duration, interruption, failure fallback, and presentation hooks. Cooldown/resource state has one authoritative owner. Damage uses authoritative platform mechanisms and must prevent duplicate or recursive event chains.

## 11. Fairness and counterplay
High-impact attacks should communicate through wind-up animation, sound, particles, warning areas, target locks, or environmental cues. Document what players can observe, reaction time, evasion/block/interrupt options, tracking after startup, and accessibility alternatives. Unavoidable damage requires explicit justification and must appear in the approval plan.

## 12. Defense and status effects
Potential mechanics include block, guard, dodge, parry, shield, resistance windows, interrupt, and retreat, subject to platform support. Each status effect defines duration, stacking, refresh, immunity, cleanse, source attribution, multiplayer replication, and death/respawn behavior. Prevent unintended runaway stacking and contradictory states.

## 13. Boss encounters
Bosses use explicit phase graphs/state machines. Each phase declares entry/exit conditions, attacks, ability weights, arena interactions, summons, vulnerability windows, and recovery. Encounter plans define activation, transitions, telegraphs, phase protection, summon limits/cleanup, reset/despawn/unload/death/player-abandonment behavior, reward events, and solo/multiplayer scaling. Transitions must be idempotent and recover safely after unload/restart where persistence is required.

## 14. Squad coordination
Group tactics may include shared alerts, role assignment, focus fire, flanking, guarding, coordinated retreat, reinforcement calls, and formations. Define membership, leader policy, communication radius/cadence, group-size limits, shared versus individual perception, target reservation, conflict resolution, and behavior on leader loss/member death/unload. Coordination must degrade gracefully and avoid synchronized pathfinding spikes or alert loops.

## 15. Difficulty and balance
Difficulty is a named, reviewable profile, not an opaque multiplier. Tunable dimensions may include health, damage, cadence, perception, aggression, ability selection, telegraph duration, resource limits, group size, and recovery windows. Separate player-count scaling from difficulty; expose override precedence; record expected player gear/progression; and produce balance warnings and playtest scenarios. No numeric defaults are approved by this draft.

## 16. Companions, factions, and friendly fire
Companions may defend, follow, assist, hold, protect, or avoid combat under user-approved rules. Integrate with NPC identity/relationship data. Define owner/team recognition, commands, target permissions, friendly fire, death/revive, catch-up, and multiplayer ownership. Relations distinguish friendly, neutral, hostile, allied, protected, and unknown. Unknown relations require a safe configurable default. Friendly-fire rules cover direct, area, projectile, summon, environmental, and reflected damage.

## 17. Encounter authoring and integrations
An encounter binds entities, spawn rules, arena/world references, waves, triggers, difficulty, objectives, and completion/failure events. NPC engine supplies identity/role metadata; World engine supplies arena constraints; Quest engine consumes combat events; platform adapters implement runtime; Resource Pack supplies presentation; shared project manifest tracks references and version constraints. Missing references block packaging unless explicitly optional.

## 18. Studio authoring experience
Provide structured editors for combat states/transitions, behavior priorities, perception/targeting, attacks/abilities, boss phases, squad roles, difficulty, and encounter waves/triggers. Conversational input is converted into a reviewable specification. AI must expose unsupported features and trade-offs and request approval before generation. Advanced users can edit structured values directly.

## 19. Validation and test evidence
Validation includes schema/ID uniqueness, cross-reference integrity, platform/version capability, state-graph reachability/dead ends, behavior cycles/starvation/priority conflicts, attack timing/range/cooldown/resource consistency, damage/friendly-fire policies, dependency/packaging checks, isolated builds, in-game target/navigation/attack/phase/group/unload/multiplayer tests, performance tests, and human playability review.

Evidence labels must distinguish static validation, build, load, runtime, multiplayer, performance, and human playtest. Unrun tests are reported as not run. Compilation is not proof of playability.

## 20. Performance and scalability
Declare update cadence, per-entity work budget, group coordination budget, and supported active-agent counts. Prefer event-driven updates; throttle perception/pathfinding; cache stable data; bound searches/retries; avoid per-tick global scans; and define degraded behavior for distant/inactive encounters. Performance claims require measurements on declared hardware and representative workloads.

## 21. Multiplayer, persistence, and recovery
Server authority governs targets, damage, cooldowns, phases, and encounter completion. Define persistence across chunk/entity unload, world save/restart, server restart, player disconnect/reconnect, and encounter reset. Store only necessary versioned state. Corrupt/missing state must recover safely without duplicating bosses, rewards, or damage events.

## 22. Security and abuse prevention
Treat generated code/scripts as untrusted build inputs. Enforce bounded loops, resource limits, safe event handling, dependency policy, isolated builds, and server-side validation against client spoofing of damage, targets, cooldowns, rewards, or encounter state. Review multiplayer griefing and denial-of-service risks. Generated AI must not access secrets or execute unrestricted external commands/network operations.

## 23. Diagnostics and repair
Opt-in traces may record state transitions, target decisions, chosen actions, path failures, ability activation, damage, phase transitions, and squad messages. Correlate logs without exposing secrets or unnecessary player data. Debug overlays are reduced/disabled in production.

When tests fail, map the failure to owning features/dependency nodes and propose the smallest safe repair. Preserve user-edited assets and approved configuration. Changes to approved combat behavior, damage, difficulty, or progression reopen approval; unrelated components are not regenerated.

## 24. Delivery
Depending on scope: editable source/configuration, Java source and JAR, Bedrock packs/add-on package, datapack ZIP, resource pack, encounter/world references, dependency/compatibility report, validation/test evidence, limitations, installation, backup, and rollback instructions. Manifest records exact game version, loader/API, runtime owner, dependencies, and package types.

## 25. Acceptance criteria
- Every feature has explicit runtime ownership and version support.
- States/transitions, targeting, attacks, abilities, and friendly-fire are inspectable.
- Boss and squad behavior is bounded and recoverable.
- Difficulty is reviewable and testable.
- Multiplayer authority and persistence are defined.
- Unsupported capabilities are disclosed before approval.
- Evidence never overstates playability.
- Delivery includes editable source and applicable runnable packages.
- Scope changes trigger impact analysis and renewed approval.

## 26. Open decisions
1. Which platforms and Minecraft versions are mandatory for first release?
2. Which Java loaders are first-class: NeoForge, Forge, Fabric, or all?
3. Which Bedrock Script API versions/experimental features are permitted?
4. Is the authoring model FSM + behavior tree, FSM + utility AI, or selectable hybrid?
5. Which graph editor is required in the first UI release?
6. What determinism and seeded-randomness guarantees are required?
7. Which damage types/status effects are built-in versus user-defined?
8. Are custom hitboxes, projectile physics, and advanced collision first-release requirements?
9. What are maximum active combatants per encounter and per squad?
10. Which squad coordination capabilities are mandatory at launch?
11. Are boss phase graphs unrestricted or template-constrained initially?
12. What persistence is required across unload, world restart, and server restart?
13. What is the default friendly-fire policy for neutral/allied/unknown factions?
14. Which difficulty presets and balance targets ship?
15. Is player-count scaling automatic, manual, or both?
16. Which companion commands/ownership rules are required?
17. What automated in-game test harness exists per platform?
18. Which server/hardware profiles define performance thresholds?
19. Which diagnostic traces/debug overlays are user-facing?
20. What policy governs external combat libraries, dependencies, and licenses?
21. Which generated animation/sound/telegraph assets are mandatory?
22. How are combat rewards and quest events integrated without duplicate ownership?
23. Is PvP in the initial scope?
24. What minimum human playtest is required before an encounter is labeled playable?

## 27. Current status
This is a design draft only. All listed decisions remain open until explicitly resolved by the product owner. No source code, runtime behavior, mod, or playable encounter is created by this document.
