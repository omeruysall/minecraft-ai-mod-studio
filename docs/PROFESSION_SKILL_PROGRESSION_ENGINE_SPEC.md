# Profession, Skill & Progression Engine Specification

**Document status:** Design draft  
**Version:** 0.1  
**Implementation status:** Not implemented; design requirements only.  
**Approval status:** Awaiting product decisions and baseline approval.

## 1. Purpose
Define configurable player and NPC progression systems for Minecraft projects. The engine supports skills, professions, experience, levels, unlocks, specialization, perks, attributes, reputation hooks, and progression tracks. It must integrate with quests, combat, crafting, economy, NPCs, and settlements without duplicating their authoritative state.

## 2. Ownership boundaries
- This engine owns skill definitions, progression rules, experience awards, level state, unlock conditions, and specialization configuration.
- Quest Engine owns quest state and objective completion.
- Combat Engine owns damage, combat state, and encounter outcomes.
- Crafting Engine owns recipe execution and production jobs.
- Economy Engine owns currency, wallets, and transactions.
- NPC Engine owns character identity, dialogue, relationships, and schedules; this engine supplies profession/skill profiles by reference.
- Settlement Engine owns service/job capacity and settlement-level development.
- Platform adapters own runtime-specific storage and player/entity integration.

Each progression variable has one authoritative owner and a declared write contract.

## 3. Principles
- Progression is optional and project-configurable.
- Every award and unlock has an explicit source, rule, cap, and audit trail.
- Multiplayer progression is server authoritative.
- Progression changes are deterministic where required and idempotent under retries.
- Avoid opaque grind, runaway scaling, and irreversible softlocks.
- Platform/version limitations are disclosed.
- User approval is required before generation and material balance changes.

## 4. Scope
In scope: player levels, skill trees, professions, class-like specializations, XP sources, attribute modifiers, perks, unlocks, mastery, NPC skill profiles, profession job roles, progression curves, reset/respec rules, party/group progression, achievements integration, and admin tools.

Out of scope: real-money progression purchases, gambling/loot-box mechanics, unrestricted player profiling, and replacing all vanilla experience mechanics by default.

## 5. Progression profile
A profile defines stable ID, scope (player/NPC/faction/project), enabled tracks, starting state, maximum levels, progression curve, award sources, unlock policy, persistence, UI visibility, and reset rules. Profiles may inherit from templates only with explicit override precedence.

## 6. Experience and award events
An award event includes stable ID, actor, source event, amount/formula, eligibility, caps, cooldown, multiplier, reason, and idempotency key. Sources may include quests, crafting, exploration, combat, gathering, settlement tasks, discoveries, or authored challenges. Source systems emit facts; progression validates and commits awards. Repeated source events must not grant duplicate XP.

## 7. Levels and progression curves
Curves may be linear, polynomial, piecewise, milestone-based, or custom bounded formulas. Define level cap, XP thresholds, overflow, prestige/reset behavior, and migration. Display the next threshold and meaningful progression feedback. Avoid unbounded numeric growth and integer overflow.

## 8. Skills and skill trees
A skill includes stable ID, category, prerequisites, rank cap, unlock cost, effects, visibility, and platform capability. Trees are directed graphs with prerequisite validation, no unintended cycles, reachable nodes, and clear respec behavior. Effects must be bounded and must not bypass server-side authority.

## 9. Professions and specializations
Profession profiles may define role, permitted activities, skill dependencies, equipment requirements, station references, schedule hooks, and progression. Specializations provide mutually exclusive or combinable paths with explicit rules. NPC profession identity remains owned by NPC Engine; this engine stores skill/progression state by reference.

## 10. Attributes and modifiers
Attributes may include health, stamina-like resources, movement, defense, attack, crafting efficiency, carrying capacity, perception, or project-defined values. Each modifier declares base, additive/multiplicative order, cap, duration, stacking, source, removal, and persistence. Avoid hidden stacking and conflicting modifiers.

## 11. Perks and abilities
Perks may unlock passive bonuses, active abilities, recipes, interactions, dialogue choices, or access. Combat abilities are executed by Combat Engine; crafting unlocks by Crafting Engine; permissions by their owning system. This engine only owns unlock state and validated effect references.

## 12. NPC progression and worker competence
NPCs may have skills, profession ranks, training, or bounded competence values. Define whether NPC progress is static, event-driven, simulated while unloaded, or tied to player actions. Avoid continuous per-NPC computation. NPC Engine owns identity and behavior; settlement and crafting systems consume capability facts.

## 13. Party and shared progression
Optional group systems may support shared XP, party levels, role contribution, cooperative unlocks, and catch-up rules. Define eligibility, contribution, distance, party membership changes, split/merge behavior, and abuse prevention. Do not silently transfer individual progression when a player leaves a group.

## 14. Reputation and faction integration
Reputation/faction standing may be referenced as unlock conditions or modifiers. Faction system owns standing values and events. Define thresholds, decay, visibility, and whether reputation is separate from skill progression. Avoid circular unlock dependencies.

## 15. Reset, respec, and migration
Define free/paid respec, cooldown, refund rules, partial reset, prestige, character deletion, and admin correction. Economy owns any currency fees. Migrations must preserve earned progress and prevent duplicate awards. Resets require confirmation and clear consequences.

## 16. Balance and anti-grind
Progression curves must be inspectable and testable across expected playtime. Define target pacing, catch-up mechanics, diminishing returns, repeatable source limits, anti-farm rules, and caps. Avoid punishing players for choosing different play styles. Balance profiles should be versioned and include example progression simulations.

## 17. Multiplayer and persistence
Server authority validates XP awards, levels, unlocks, attributes, and party state. Define offline progress, reconnect, cross-world scope, shared server profiles, and late join. Persist versioned state with migrations, audit records, and recovery for interrupted award transactions.

## 18. User interface and feedback
Provide progression overview, skill tree, profession selection, attribute sheet, perk details, unlock previews, award history, and respec confirmation. Show requirements, effects, caps, and source of modifiers. Accessibility includes keyboard/controller navigation, readable labels, and non-color-only status indicators.

## 19. Authoring experience
Provide curve editor, skill graph, profession builder, modifier editor, award-source mapping, unlock-condition builder, balance simulator, and migration preview. Conversational requirements become a structured progression plan. Show affected systems, numeric examples, exploit risks, and platform limitations before approval.

## 20. Security and exploit prevention
Validate all awards and modifiers server-side. Prevent client-forged XP, replayed awards, negative/overflow values, duplicated unlocks, unauthorized respec, and modifier stacking exploits. Bound formulas and graph traversal. Generated scripts must not access secrets or unrestricted external resources.

## 21. Validation and testing
Validate schema/IDs, graph reachability/cycles, level thresholds, curve monotonicity where required, award idempotency, modifier bounds/stacking, unlock references, platform capabilities, migration integrity, and permission contracts. Runtime tests cover XP awards, duplicate events, level-up, unlocks, respec, party changes, reconnect, server restart, and client tampering. Balance simulations and human playtests are required for pacing claims. Unrun tests are reported as not run.

## 22. Diagnostics and repair
Expose opt-in award provenance, progression state changes, modifier sources, unlock evaluation, and migration/recovery traces. Repair proposals identify affected profiles and dependent components. Preserve user-authored trees and approved balance. Changes to award rates, level curves, unlock costs, or competitive modifiers require renewed approval.

## 23. Delivery
Deliver progression schemas, profiles, skill trees, profession definitions, runtime source/artifacts, UI metadata, compatibility report, migration scripts, balance simulations, test evidence, and player-facing guide. Manifest records platform/version, progression scope, and dependency references.

## 24. Acceptance criteria
- Every award has a validated source and idempotency protection.
- Progression curves and caps are inspectable.
- Skill trees are reachable and cycle-checked.
- Modifiers have bounded stacking and authoritative application.
- NPC identity and profession ownership are not duplicated.
- Multiplayer state is server authoritative and recoverable.
- Respec/reset consequences are explicit.
- Balance claims have simulation and human playtest evidence.
- Platform limitations are disclosed before approval.
- Material changes to approved progression require renewed approval.

## 25. Open decisions
1. Is progression a core first-release feature or optional module?
2. Which platforms, versions, and Java loaders are mandatory?
3. Is vanilla XP preserved, extended, or replaced per project?
4. Which progression scopes are supported: player, NPC, party, faction, settlement?
5. What are default level caps and numeric limits?
6. Which curve types are exposed to creators?
7. Are skill trees mandatory, optional, or one of several progression models?
8. Which skill categories and attributes ship initially?
9. Are professions player-selectable, NPC-only, or both?
10. Which specializations and respec policies are required?
11. How are XP awards sourced, capped, and deduplicated?
12. Are offline progression and catch-up supported?
13. What party/shared progression rules are required?
14. How does faction reputation interact with progression?
15. Are NPC skills static, event-driven, or simulated?
16. Which modifiers can affect combat, crafting, movement, or permissions?
17. What is the default policy for stacking and diminishing returns?
18. Which anti-farm rules and repeatable-source limits are required?
19. What audit retention and privacy policy applies?
20. Which UI views and accessibility requirements are mandatory?
21. Which external progression libraries are allowed and under what license?
22. What balance targets and playtime scenarios define acceptance?
23. What migration guarantees apply when progression schemas change?
24. Which admin correction/reset tools are required?

## 26. Current status
Design draft only. All open decisions remain unresolved until explicitly decided by the product owner. No code, XP system, skill tree, profession progression, or playable progression feature is implemented by this document.
