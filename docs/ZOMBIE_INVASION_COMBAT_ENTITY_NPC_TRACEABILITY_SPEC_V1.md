# Zombie Invasion — Combat, Entity and NPC Traceability Specification v1

**Status:** Feature-level design mapping; exact balance and some optional scopes remain open  
**Date:** 2026-11-28  
**Feature IDs:** COM-001..COM-012 and ENT-001..ENT-018  
**Supporting designs:** combat/weapons, zombie roster, encounter director, NPC dialogue, survivor factions/settlements, horde/ecology and multiplayer proposal

## 1. Purpose and scope

This specification maps 30 combat, entity and NPC features to requirements, target behavior, acceptance criteria and test cases. It separates the user-approved first-slice combat and zombie roster from optional or deferred capabilities. It does not claim any runtime implementation or test execution.

Confirmed first-slice combat: melee and firearms, weapon noise, durability and limited ammunition. Confirmed first-slice zombies: Walker, Runner and Brute. Single-player is sufficient for the first playable slice. Bosses, explosives, PvP, dedicated server and multiplayer synchronization remain separate scope decisions or later milestones.

NPC requirements include state-aware dialogue, the chosen in-game player name, persistent survivor identity and dialogue grounded in actual game state. For example, an NPC may mention a fracture only after the injury system has recorded that fracture; dialogue must never invent a diagnosis.

Targets remain Java 26.3 + Fabric and Bedrock 26.60 + stable Script API 2.11.0 where needed; experimental APIs are disabled.

## 2. Cross-system ownership

- Combat owns hit/damage resolution; player health/injury owns player condition; item/inventory owns equipment and ammunition; loot owns drops.
- Zombie AI owns individual infected perception, navigation and attacks; Encounter Director owns bounded spawn requests and encounter phases.
- NPC simulation owns survivor identity, needs, schedules, tasks and faction affiliation; dialogue reads that state but does not mutate it.
- World simulation owns time/weather/biome state; entities consume that state rather than creating independent clocks.
- Asset pipelines own models, hitboxes, animation, sound and localization references; presentation cannot authorize damage.
- Java and Bedrock use separate adapters, registries and evidence records.

## 3. Feature-level mapping

### COM-001 — Damage types and damage calculation

**Requirement:** REQ-COM-001  
**Purpose:** Define one authoritative damage pipeline for physical, environmental, fire, fall, infection-related and other approved damage types.  
**Target mapping:** Java and Bedrock map target-native damage events into the same logical damage stages.

**Acceptance criteria**
- AC-COM-001-01: Damage source, amount, mitigation, absorption and injury side effects resolve once in deterministic order.
- AC-COM-001-02: Invalid, duplicate or recursive damage events are rejected; damage logs retain source and target context.

**Test cases**
- TC-COM-001-01: TC-COM-001-01 damage pipeline ordering and source attribution
- TC-COM-001-02: TC-COM-001-02 duplicate/recursive damage event rejection

**Prerequisite feature IDs:** PLY-002, ITEM-001.

### COM-002 — Melee weapons, reach, attack speed, combos

**Requirement:** REQ-COM-002  
**Purpose:** Define melee hit windows, reach, attack speed, stamina cost, durability and optional combo rules.  
**Target mapping:** Equivalent player-facing combat outcomes; target-specific input and hit detection adapters.

**Acceptance criteria**
- AC-COM-002-01: Reach and hit timing are bounded and validated against line of sight/collision; attacks consume durability/stamina once.
- AC-COM-002-02: Melee remains a viable combat path when firearm ammunition is exhausted.

**Test cases**
- TC-COM-002-01: TC-COM-002-01 melee reach, timing and collision
- TC-COM-002-02: TC-COM-002-02 durability/stamina and repeated input handling

**Prerequisite feature IDs:** ITEM-005, PLY-003.

### COM-003 — Ranged weapons, projectiles, trajectory

**Requirement:** REQ-COM-003  
**Purpose:** Define projectile creation, travel, collision, damage, range and retrieval/consumption behavior.  
**Target mapping:** Target-native projectile or supported scripted equivalent; no experimental Bedrock API.

**Acceptance criteria**
- AC-COM-003-01: Projectile ownership, lifetime, collision and damage are authoritative and bounded.
- AC-COM-003-02: Projectile spam, duplication and unloaded-world persistence exploits are prevented.

**Test cases**
- TC-COM-003-01: TC-COM-003-01 projectile trajectory and collision
- TC-COM-003-02: TC-COM-003-02 projectile lifetime and duplication abuse

**Prerequisite feature IDs:** ITEM-005, ITEM-001.

### COM-004 — Firearms, ammunition, reload, recoil

**Requirement:** REQ-COM-004  
**Purpose:** Implement approved first-slice firearms with finite ammunition, reload state, recoil/handling and weapon noise.  
**Target mapping:** Java Fabric and Bedrock stable API use separate weapon implementations with equivalent outcomes.

**Acceptance criteria**
- AC-COM-004-01: A shot consumes one valid round, reload consumes compatible reserve ammo and no operation duplicates ammunition.
- AC-COM-004-02: Gunfire emits bounded noise events; noise may alert nearby zombies but cannot bypass encounter budgets.

**Test cases**
- TC-COM-004-01: TC-COM-004-01 shot/reload/ammo conservation
- TC-COM-004-02: TC-COM-004-02 noise event bounded and zombie response reproducible

**Prerequisite feature IDs:** ITEM-005, ITEM-009, CRAFT-001.

### COM-005 — Explosives and area damage

**Requirement:** REQ-COM-005  
**Purpose:** Provide an optional explosive/area-damage framework without making explosives mandatory for the first slice.  
**Target mapping:** Only target-supported implementations are allowed; area effects are bounded in radius and workload.

**Acceptance criteria**
- AC-COM-005-01: Explosion damage, block damage, fire and noise are separately configurable and cannot exceed declared limits.
- AC-COM-005-02: Explosives remain excluded from first-slice production until exact scope and balance are approved.

**Test cases**
- TC-COM-005-01: TC-COM-005-01 area damage and radius caps
- TC-COM-005-02: TC-COM-005-02 first-slice scope gate blocks unapproved explosives

**Prerequisite feature IDs:** ITEM-014, ITEM-001.

### COM-006 — Armor penetration, resistance, hit zones

**Requirement:** REQ-COM-006  
**Purpose:** Resolve hit zones, armor coverage, penetration and resistance without bypassing health/injury ownership.  
**Target mapping:** Shared hit-zone model with target-specific hit detection and equipment adapters.

**Acceptance criteria**
- AC-COM-006-01: Armor and penetration are applied in one defined order; unarmored regions remain distinguishable.
- AC-COM-006-02: Hit-zone state cannot be spoofed by client-only presentation or duplicated collision events.

**Test cases**
- TC-COM-006-01: TC-COM-006-01 armor and penetration ordering
- TC-COM-006-02: TC-COM-006-02 hit-zone validation and duplicate-hit rejection

**Prerequisite feature IDs:** PLY-002, ITEM-006.

### COM-007 — Blocking, parrying, dodging

**Requirement:** REQ-COM-007  
**Purpose:** Define defensive actions, timing windows, stamina cost, recovery and injury restrictions as optional combat mechanics.  
**Target mapping:** Target input differences are adapted; no unsupported invulnerability behavior is assumed.

**Acceptance criteria**
- AC-COM-007-01: Defensive windows are bounded and cannot grant indefinite invulnerability.
- AC-COM-007-02: Stamina, weapon condition and injury constraints are applied consistently.

**Test cases**
- TC-COM-007-01: TC-COM-007-01 defensive timing and stamina cost
- TC-COM-007-02: TC-COM-007-02 invulnerability window and repeated-action exploit

**Prerequisite feature IDs:** PLY-003, PLY-005.

### COM-008 — Critical hits, status effects, knockback

**Requirement:** REQ-COM-008  
**Purpose:** Define critical hit conditions, status application and knockback with caps and clear feedback.  
**Target mapping:** Equivalent gameplay result using target-native effect and motion capabilities.

**Acceptance criteria**
- AC-COM-008-01: Critical hits require declared conditions and are not random unbounded multipliers.
- AC-COM-008-02: Status effects have source, duration and stacking rules; knockback respects collision and boss resistance.

**Test cases**
- TC-COM-008-01: TC-COM-008-01 critical-hit eligibility and cap
- TC-COM-008-02: TC-COM-008-02 status stacking and knockback collision

**Prerequisite feature IDs:** PLY-002, PLY-011.

### COM-009 — Friendly fire, PvP rules, team damage

**Requirement:** REQ-COM-009  
**Purpose:** Define player-versus-player and team damage policy for a future multiplayer profile.  
**Target mapping:** First playable is single-player; PvP/team damage is not applicable until multiplayer scope is approved.

**Acceptance criteria**
- AC-COM-009-01: No PvP or friendly-fire behavior is enabled by default in the single-player milestone.
- AC-COM-009-02: When multiplayer is enabled later, damage permissions are server/world authoritative and configurable.

**Test cases**
- TC-COM-009-01: TC-COM-009-01 single-player profile disables PvP paths
- TC-COM-009-02: TC-COM-009-02 declared multiplayer profile enforces team damage policy

**Prerequisite feature IDs:** BASE-003, QA-012.

### COM-010 — Combat feedback, indicators, logs

**Requirement:** REQ-COM-010  
**Purpose:** Provide readable hit, damage, reload, ammo, durability, noise and injury feedback with structured diagnostics.  
**Target mapping:** Java HUD/chat/sound and Bedrock supported UI/message channels may differ but must communicate the same critical state.

**Acceptance criteria**
- AC-COM-010-01: Feedback is derived from committed combat state; it cannot report hits, injuries or ammunition changes that did not occur.
- AC-COM-010-02: Logs identify event source, target, weapon, damage and relevant result without exposing secrets.

**Test cases**
- TC-COM-010-01: TC-COM-010-01 combat feedback matches authoritative state
- TC-COM-010-02: TC-COM-010-02 combat event log provenance and redaction

**Prerequisite feature IDs:** PLY-002, QA-017.

### COM-011 — Loot, death drops, durability and repair rules

**Requirement:** REQ-COM-011  
**Purpose:** Connect combat outcomes to loot, death drops and item condition without duplicating ownership with inventory/crafting systems.  
**Target mapping:** Target adapters emit logical loot/death events; inventory and loot engines own item creation/transfer.

**Acceptance criteria**
- AC-COM-011-01: Each death/drop/loot event is idempotent and follows approved scenario and save policies.
- AC-COM-011-02: Repair and drop behavior consume/transfer real items and respect the still-open death/restart policy.

**Test cases**
- TC-COM-011-01: TC-COM-011-01 death drop and loot idempotency
- TC-COM-011-02: TC-COM-011-02 durability/repair state preserved after combat

**Prerequisite feature IDs:** ITEM-009, ITEM-001, QA-015.

### COM-012 — Balance configuration and difficulty scaling

**Requirement:** REQ-COM-012  
**Purpose:** Define data-driven damage, health, speed, spawn pressure and difficulty modifiers with safe ranges.  
**Target mapping:** Shared balance intent, independently validated Java and Bedrock configuration adapters.

**Acceptance criteria**
- AC-COM-012-01: All balance values are versioned, bounded and reproducible under a fixed test seed.
- AC-COM-012-02: No exact numeric balance or wave count is assumed before dedicated solo-player playtests.

**Test cases**
- TC-COM-012-01: TC-COM-012-01 balance schema bounds and deterministic scenario
- TC-COM-012-02: TC-COM-012-02 difficulty change creates revision and impact report

**Prerequisite feature IDs:** PLY-008, QA-014, QA-011.

### ENT-001 — Custom entity registration and attributes

**Requirement:** REQ-ENT-001  
**Purpose:** Register custom zombies, survivors, wildlife and bosses with stable logical identities and target-native entity definitions.  
**Target mapping:** Java Fabric entity registration and Bedrock entity/behavior definitions are separate.

**Acceptance criteria**
- AC-ENT-001-01: Each entity has unique ID, owner, attributes, capabilities and target-specific registration evidence.
- AC-ENT-001-02: Unregistered or unsupported entity properties block packaging rather than silently degrading.

**Test cases**
- TC-ENT-001-01: TC-ENT-001-01 entity registry and target mapping
- TC-ENT-001-02: TC-ENT-001-02 invalid entity attribute/capability rejection

**Prerequisite feature IDs:** ITEM-001, BASE-007.

### ENT-002 — Passive wildlife and ambient creatures

**Requirement:** REQ-ENT-002  
**Purpose:** Define wildlife/ambient species, habitat, needs, behavior and bounded population simulation.  
**Target mapping:** Java and Bedrock use native entity capabilities where possible; distant ecology may use aggregate state.

**Acceptance criteria**
- AC-ENT-002-01: Wildlife population, spawning and resource use follow habitat and regional budgets.
- AC-ENT-002-02: Animal state and loot/products cannot duplicate on chunk unload/reload; first-slice species remain separately scoped.

**Test cases**
- TC-ENT-002-01: TC-ENT-002-01 habitat and population cap enforcement
- TC-ENT-002-02: TC-ENT-002-02 wildlife persistence and resource accounting

**Prerequisite feature IDs:** ITEM-002, CRAFT-007.

### ENT-003 — Hostile mobs and enemy archetypes

**Requirement:** REQ-ENT-003  
**Purpose:** Implement the approved Walker, Runner and Brute roster with distinct perception, movement, attack and counterplay.  
**Target mapping:** Separate target AI adapters; equivalent archetype identity, role and gameplay outcomes.

**Acceptance criteria**
- AC-ENT-003-01: Each approved archetype has explicit state machine, attributes, attack rules and bounded navigation/target budgets.
- AC-ENT-003-02: Deferred special zombies remain disabled until separately approved; first-slice roster cannot silently expand.

**Test cases**
- TC-ENT-003-01: TC-ENT-003-01 Walker Runner Brute state and role validation
- TC-ENT-003-02: TC-ENT-003-02 deferred archetypes blocked from first-slice manifest

**Prerequisite feature IDs:** COM-001, ENT-001.

### ENT-004 — Friendly, neutral, and recruitable NPCs

**Requirement:** REQ-ENT-004  
**Purpose:** Define survivor NPC identity, needs, skills, inventory, affiliation, recruitment and task availability.  
**Target mapping:** Target-specific entity and interaction implementations with shared NPC state contract.

**Acceptance criteria**
- AC-ENT-004-01: Rescue/recruitment consumes valid conditions/resources and creates one persistent NPC identity.
- AC-ENT-004-02: NPC tasks and dialogue read authoritative state; no free labor, duplicated survivor or fabricated completed task.

**Test cases**
- TC-ENT-004-01: TC-ENT-004-01 survivor rescue/recruitment transaction
- TC-ENT-004-02: TC-ENT-004-02 NPC identity/task persistence and duplicate prevention

**Prerequisite feature IDs:** PLY-014, ENT-001.

### ENT-005 — Bosses, mini-bosses, elite variants

**Requirement:** REQ-ENT-005  
**Purpose:** Define boss/elite encounter contracts, phases, telegraphs, resistances, rewards and world impact.  
**Target mapping:** Boss mechanics must fit each target's supported AI and entity limits; exact roster is open.

**Acceptance criteria**
- AC-ENT-005-01: Bosses have readable attack phases and counterplay; rewards and phase transitions are idempotent.
- AC-ENT-005-02: Boss count, names, stats and first-slice inclusion remain open; no boss is assumed approved solely from the broad request.

**Test cases**
- TC-ENT-005-01: TC-ENT-005-01 boss phase and telegraph state transitions
- TC-ENT-005-02: TC-ENT-005-02 boss reward and encounter reset idempotency

**Prerequisite feature IDs:** ENT-003, COM-001.

### ENT-006 — Entity health, armor, damage, resistances

**Requirement:** REQ-ENT-006  
**Purpose:** Define common entity combat attributes and integrate them with damage resolution.  
**Target mapping:** Java entity attributes and Bedrock components/scripts map to the same logical stat contract.

**Acceptance criteria**
- AC-ENT-006-01: Entity health, armor and resistance are bounded and resolve through the authoritative combat pipeline.
- AC-ENT-006-02: Entity state cannot bypass encounter caps or be duplicated by target-specific health logic.

**Test cases**
- TC-ENT-006-01: TC-ENT-006-01 entity health/armor damage resolution
- TC-ENT-006-02: TC-ENT-006-02 resistance bounds and duplicate damage prevention

**Prerequisite feature IDs:** COM-001.

### ENT-007 — Navigation, pathfinding, obstacle handling

**Requirement:** REQ-ENT-007  
**Purpose:** Define navigation goals, obstacle response, route budgets, door/window/breach interactions and fallback behavior.  
**Target mapping:** Use target-native navigation where possible; scripted behavior must respect platform performance limits.

**Acceptance criteria**
- AC-ENT-007-01: Pathfinding has bounded search/work budgets and does not force-load distant chunks.
- AC-ENT-007-02: Blocked routes transition to defined investigate, reroute, breach or abandon states without infinite loops.

**Test cases**
- TC-ENT-007-01: TC-ENT-007-01 obstacle and route recovery
- TC-ENT-007-02: TC-ENT-007-02 navigation budget and no remote chunk force-load

**Prerequisite feature IDs:** ENT-001, BASE-003.

### ENT-008 — Target selection, threat, aggro, retreat

**Requirement:** REQ-ENT-008  
**Purpose:** Define perception, hearing, sight, threat scoring, target switching, memory and retreat conditions.  
**Target mapping:** Both targets use equivalent perception inputs and bounded update frequency.

**Acceptance criteria**
- AC-ENT-008-01: Gunfire/noise, movement and visibility update threat state through explicit events; no unlimited spawn side effect.
- AC-ENT-008-02: Target selection is deterministic under fixed conditions and cannot access undiscovered hidden player state.

**Test cases**
- TC-ENT-008-01: TC-ENT-008-01 sight/hearing threat acquisition and decay
- TC-ENT-008-02: TC-ENT-008-02 target switching and information boundary

**Prerequisite feature IDs:** ENT-007, COM-001.

### ENT-009 — Patrol, guard, follow, flee, escort behaviors

**Requirement:** REQ-ENT-009  
**Purpose:** Define reusable behavior roles for zombies, survivors, guards and escorted actors.  
**Target mapping:** Role state machines map to supported target AI capabilities.

**Acceptance criteria**
- AC-ENT-009-01: Behavior transitions have clear preconditions, cancellation and recovery; tasks do not duplicate actor control.
- AC-ENT-009-02: NPC follow/escort respects player location, actor health, route and threat state.

**Test cases**
- TC-ENT-009-01: TC-ENT-009-01 patrol/guard/follow transition validation
- TC-ENT-009-02: TC-ENT-009-02 escort interruption and recovery

**Prerequisite feature IDs:** ENT-007, ENT-004.

### ENT-010 — Group tactics, formations, territory

**Requirement:** REQ-ENT-010  
**Purpose:** Define horde movement, group pressure, flanking, territory and faction squad behavior under bounded simulation.  
**Target mapping:** Group logic is adapted to each target's entity and tick budgets.

**Acceptance criteria**
- AC-ENT-010-01: Group coordination uses bounded shared decisions and does not multiply pathfinding work per actor without limits.
- AC-ENT-010-02: Territory/group state persists as regional summaries and cannot spawn unlimited reinforcements.

**Test cases**
- TC-ENT-010-01: TC-ENT-010-01 group tactics budget and territory state
- TC-ENT-010-02: TC-ENT-010-02 horde group unload/reload consistency

**Prerequisite feature IDs:** ENT-008, ENT-003.

### ENT-011 — Day/night, weather, biome, and event reactions

**Requirement:** REQ-ENT-011  
**Purpose:** Connect entity behavior to authoritative world time, weather, biome and world events.  
**Target mapping:** Both targets consume shared world-state contracts with edition-specific event hooks.

**Acceptance criteria**
- AC-ENT-011-01: Entities react only to committed world state and configured perception modifiers.
- AC-ENT-011-02: No independent entity clock or duplicate weather state is created; behavior remains bounded at distant simulation tiers.

**Test cases**
- TC-ENT-011-01: TC-ENT-011-01 day/night and weather reaction consistency
- TC-ENT-011-02: TC-ENT-011-02 biome/event changes do not duplicate actor state

**Prerequisite feature IDs:** PLY-004.

### ENT-012 — Spawning rules, caps, density, despawning

**Requirement:** REQ-ENT-012  
**Purpose:** Define spawn eligibility, density, encounter budgets, region caps and despawn/persistence policies.  
**Target mapping:** Target spawn APIs are wrapped by the shared spawn contract and target-specific limits.

**Acceptance criteria**
- AC-ENT-012-01: Spawn requests validate location, player safety, encounter budget, entity cap and persistence ownership.
- AC-ENT-012-02: Despawn/unload cannot erase required persistent survivors or duplicate unique enemies on reload.

**Test cases**
- TC-ENT-012-01: TC-ENT-012-01 spawn budget and density caps
- TC-ENT-012-02: TC-ENT-012-02 unique actor persistence and despawn safety

**Prerequisite feature IDs:** ENT-001, ENT-003.

### ENT-013 — Breeding, taming, domestication, mounts

**Requirement:** REQ-ENT-013  
**Purpose:** Define optional wildlife domestication, breeding, care, mounts and animal product loops.  
**Target mapping:** Only target-supported interaction and mount capabilities are used; unsupported actions are marked limited.

**Acceptance criteria**
- AC-ENT-013-01: Breeding/taming consumes valid time/resources and respects population/habitat caps.
- AC-ENT-013-02: No infinite animal/product generation; first-slice inclusion remains optional and unselected.

**Test cases**
- TC-ENT-013-01: TC-ENT-013-01 breeding/taming prerequisites and population caps
- TC-ENT-013-02: TC-ENT-013-02 animal product conservation and mount state

**Prerequisite feature IDs:** ENT-002, ITEM-003, CRAFT-007.

### ENT-014 — NPC dialogue, schedules, relationships, reputation

**Requirement:** REQ-ENT-014  
**Purpose:** Define contextual dialogue, schedules, relationships and reputation using authoritative NPC/player/world state.  
**Target mapping:** Java and Bedrock dialogue interfaces differ; shared dialogue facts, conditions and player-facing outcomes remain consistent.

**Acceptance criteria**
- AC-ENT-014-01: NPC dialogue can address the player by the chosen in-game name and react only to recorded game state; injury lines require an actual injury record.
- AC-ENT-014-02: Schedules, relationships and reputation persist; dialogue cannot fabricate discoveries, diagnoses, completed tasks or resource changes.

**Test cases**
- TC-ENT-014-01: TC-ENT-014-01 injury-aware dialogue reads authoritative fracture state
- TC-ENT-014-02: TC-ENT-014-02 schedule/reputation and in-game player-name continuity

**Prerequisite feature IDs:** ENT-004, PLY-014, PLY-011.

### ENT-015 — Trading and service interactions

**Requirement:** REQ-ENT-015  
**Purpose:** Define NPC shops, services, treatment, repair, recruitment and trade interactions with atomic resource exchange.  
**Target mapping:** Target-specific UI; shared price, stock, permission and transaction semantics.

**Acceptance criteria**
- AC-ENT-015-01: Trade validates stock, payment, capacity and access then commits atomically or rolls back.
- AC-ENT-015-02: NPC services consume time/resources and cannot create free items, currency or duplicate service outcomes.

**Test cases**
- TC-ENT-015-01: TC-ENT-015-01 atomic trade and stock/payment validation
- TC-ENT-015-02: TC-ENT-015-02 service cost and duplicate request protection

**Prerequisite feature IDs:** ENT-014, ITEM-008.

### ENT-016 — Entity animation, sounds, particles, hitboxes

**Requirement:** REQ-ENT-016  
**Purpose:** Define entity visual rigs, animation states, sounds, particles and hitbox contracts.  
**Target mapping:** Java models/animations and Bedrock geometry/animation controllers are separate asset pipelines.

**Acceptance criteria**
- AC-ENT-016-01: Animation/hitbox state remains synchronized with authoritative attack/movement states; hitboxes are validated.
- AC-ENT-016-02: Missing assets and invalid animation references are caught before packaging; no visual-only attack hit is accepted.

**Test cases**
- TC-ENT-016-01: TC-ENT-016-01 attack animation and hitbox timing consistency
- TC-ENT-016-02: TC-ENT-016-02 entity asset/sound reference validation

**Prerequisite feature IDs:** ENT-001, ITEM-016.

### ENT-017 — Persistence, chunk unload/reload, entity data

**Requirement:** REQ-ENT-017  
**Purpose:** Persist unique entity identity, health, inventory, task, faction, encounter and world-owned state safely.  
**Target mapping:** Separate Java entity NBT/world persistence and Bedrock-supported world/script persistence adapters.

**Acceptance criteria**
- AC-ENT-017-01: Unload/reload preserves persistent entities exactly once; transient entities follow explicit despawn rules.
- AC-ENT-017-02: Migrations and region activation do not duplicate survivors, bosses, loot or encounter events.

**Test cases**
- TC-ENT-017-01: TC-ENT-017-01 entity state save/unload/reload
- TC-ENT-017-02: TC-ENT-017-02 duplicate actor and event migration rejection

**Prerequisite feature IDs:** BASE-009, QA-013.

### ENT-018 — AI performance limits and multiplayer authority

**Requirement:** REQ-ENT-018  
**Purpose:** Set entity budgets, AI update tiers, server authority and target-specific performance controls.  
**Target mapping:** First slice is single-player; multiplayer authority tests are conditional future gates, separately validated per target.

**Acceptance criteria**
- AC-ENT-018-01: Active/near/distant AI budgets are explicit and no distant entity forces chunk loading.
- AC-ENT-018-02: No multiplayer support claim is made from single-player tests; shared-world state has one declared authority owner.

**Test cases**
- TC-ENT-018-01: TC-ENT-018-01 horde/pathfinding stress budget
- TC-ENT-018-02: TC-ENT-018-02 authority profile and multiplayer scope gate

**Prerequisite feature IDs:** QA-014, BASE-003, QA-012.

## 4. Supporting design references

- `docs/ZOMBIE_INVASION_COMBAT_AND_WEAPON_SYSTEM_DESIGN_V1.md` — approved first-slice combat scope and weapon safeguards.
- `docs/ZOMBIE_INVASION_ZOMBIE_ROSTER_DESIGN_V1.md` — approved Walker, Runner and Brute roster.
- `docs/ZOMBIE_INVASION_ENCOUNTER_DIRECTOR_DESIGN_V1.md` — bounded spawn requests and encounter scheduling proposal.
- `docs/ZOMBIE_INVASION_NPC_DIALOGUE_3D_WEAPONS_AND_VEHICLE_MANUFACTURING_DESIGN_V1.md` — dialogue, 3D weapon models and player-name context.
- `docs/ZOMBIE_INVASION_SURVIVOR_NPC_FACTIONS_AND_SETTLEMENT_DESIGN_V1.md` — survivor identity, professions, schedules and factions.
- `docs/ZOMBIE_INVASION_HORDE_FIRE_DISEASE_ECOLOGY_DESIGN_V1.md` — horde, siege, environmental and wildlife ownership.
- `docs/ZOMBIE_INVASION_MULTIPLAYER_COOPERATION_AND_SERVER_DESIGN_V1.md` — future multiplayer/server proposal, not first-slice approval.

## 5. Open decisions preserved

- Exact weapon catalogue, damage, fire rate, magazine size, reload time, durability values and noise radius remain balance data.
- Explosives, PvP, friendly fire, blocking/parrying/dodging and advanced critical-hit rules are not automatically part of first-slice scope.
- Boss identities, boss phases, stats and first-slice boss inclusion remain open despite the broad boss requirement.
- Encounter timings, spawn counts, difficulty curves and special zombie archetypes beyond Walker/Runner/Brute remain unapproved.
- Exact wildlife species and first-slice animal roster remain open.
- Dedicated-server and multiplayer AI authority are future/conditional requirements, not proven by single-player behavior.

## 6. Implementation boundary

These 30 features are mapped for design traceability only. They remain `not_implemented_verified`; Java, Bedrock and parity remain unassessed until target-specific source, builds, runtime behavior and evidence are available. The presence of test case definitions does not mean tests have run.
