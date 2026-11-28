# Magic, Abilities & Technology Engine Specification

**Document status:** Design draft  
**Version:** 0.1  
**Implementation status:** Not implemented; design requirements only.  
**Approval status:** Awaiting product decisions and baseline approval.

## 1. Purpose
Define extensible systems for magical disciplines, spells, abilities, technology trees, devices, energy networks, research, progression gates, and interactions between supernatural and technological mechanics in generated Minecraft projects. The engine must support distinct fantasy, science-fiction, steampunk, and hybrid project styles without imposing these mechanics on vanilla gameplay.

## 2. Ownership boundaries
- This engine owns ability/spell/technology definitions, activation contracts, costs, cooldown metadata, unlock graphs, and effect composition.
- Combat Engine owns authoritative combat resolution, damage, targeting, and encounter outcomes.
- Progression Engine owns player XP, skills, classes, and unlock eligibility.
- Item/Inventory Engine owns catalysts, tools, devices, equipment, and consumable transactions.
- Crafting Engine owns recipes, machines, production queues, and resource consumption.
- World/Environment Engine owns block interactions, spatial constraints, and environmental facts.
- NPC and Quest engines own their character and objective state, consuming ability events through contracts.
- Multiplayer Engine owns network authority, replication, and session consistency.
- Platform adapters translate approved definitions to Java loaders, Bedrock, datapacks, or supported combinations.

## 3. Principles
- All mechanics are opt-in and project-scoped.
- Effects are declarative, bounded, permission-checked, and server-authoritative.
- A visual or UI representation is not proof that an ability or device works.
- Resource costs, cooldowns, range, targeting, and failure behavior are explicit.
- No arbitrary executable scripts are accepted as user-authored ability definitions.
- Balance and compatibility are tested on exact target versions.
- Cross-system effects use stable contracts and a single authoritative owner.

## 4. Scope
In scope: spells, abilities, passive effects, skill trees, magical schools, technology trees, research, devices, machines, energy sources, conduits, automation hooks, crafting integration, progression gates, targeting, status effects, visual/audio cues, and balance simulation.

Out of scope: unrestricted arbitrary code execution, real-world weapon guidance, real-money gambling mechanics, or assuming every mechanic is portable across Java and Bedrock.

## 5. Project system profiles
A project selects one or more profiles: magic-focused, technology-focused, hybrid, or disabled. Profiles define enabled disciplines, progression model, resource model, target platforms, compatibility constraints, and content tone. The manifest records enabled features and dependencies.

## 6. Ability definition model
Each ability has a stable namespaced ID, display metadata, category, activation mode, target rules, range, duration, cooldown, resource costs, prerequisites, effect references, platform support, permissions, version, and failure states. Definitions are schema-versioned and cannot contain unrestricted code.

## 7. Spell and magical discipline model
Magical schools define themes, prerequisites, resource rules, spell families, progression gates, and interactions. Spell effects are composed from allowlisted primitives such as projectile, area effect, shield, teleport, summon, detection, or world interaction where supported. Each primitive declares limits and platform capability.

## 8. Technology and research model
Technology trees define research nodes, prerequisites, unlock rewards, research costs, time policy, and mutually exclusive branches. Research may use items, crafting outputs, quest completion, exploration facts, or server events. Progression Engine owns player unlock state; this engine defines the research graph and requirements.

## 9. Resource and energy economy
Define mana, charge, heat, fuel, power, or other project-specific resources with bounds, regeneration, consumption, conversion, and storage rules. Item/Inventory and Economy engines own physical items and currency. Crafting and automation own machine processing. Prevent circular conversion loops and unbounded energy creation.

## 10. Activation and execution lifecycle
An activation request validates actor, unlock state, target, range, line of sight, cooldown, resource availability, permissions, and world context. The authoritative executor commits costs once, applies approved effects, and records outcome. Failed activations specify whether costs are refunded and how retries are handled.

## 11. Effect composition and limits
Effects are built from typed primitives with bounded parameters, duration, stacking, priority, and cancellation rules. Define effect ordering and conflict resolution. Prevent recursive triggers, infinite chaining, excessive entity creation, and oversized area operations. Dangerous or destructive world effects require explicit project configuration and permissions.

## 12. Targeting and spatial rules
Targeting modes may include self, entity, block, area, direction, location, or linked device. Define range, visibility, dimension boundaries, protected-region rules, target filters, and multiplayer ownership. Platform limitations must be surfaced before approval.

## 13. Devices, machines, and energy networks
Technology devices define inputs, outputs, energy requirements, operating state, throughput, range, permissions, and failure behavior. Crafting Engine owns production jobs; Transportation/Logistics owns routing; World Interaction owns block access. Network topology and updates must be bounded and avoid per-tick global scans.

## 14. Summoning, constructs, and temporary entities
Optional summons or constructs define entity type, lifetime, owner, cap, behavior profile, despawn, persistence, and multiplayer authority. NPC/Combat engines own entity behavior and combat. Enforce per-player and per-world caps and prevent entity multiplication exploits.

## 15. Progression and unlock integration
Abilities and technologies may require level, skill, class, quest, research, faction, or achievement conditions. Progression Engine is authoritative for player progression. Unlock changes are versioned and idempotent; removing a node must define migration for already-unlocked players.

## 16. Item, crafting, and economy integration
Catalysts, tools, components, fuel, and upgrade materials reference stable item IDs. Costs and rewards use inventory transactions. Recipes and machines are delegated to Crafting Engine. Currency and trade use Economy Engine. No subsystem may directly duplicate item or currency state.

## 17. Quest, NPC, and world integration
Quests may require ability use, research, device activation, or world effects. NPCs may teach, sell, unlock, or react to abilities. These systems exchange events and references rather than sharing internal state. All world changes respect claims, permissions, and rollback rules.

## 18. Visual, animation, and audio feedback
Ability and device definitions reference asset IDs for particles, models, animations, sound, and UI cues. Asset pipelines own generated media and licensing/provenance. Missing assets must fall back safely and must not be represented as completed effects.

## 19. Multiplayer authority and anti-cheat
The server validates activation, resource consumption, cooldowns, targets, and effects. Client prediction is optional and reconciled. Prevent forged unlocks, cooldown bypass, replay, resource duplication, target spoofing, and packet flooding. Shared effects have explicit ownership and replication scope.

## 20. Balance and simulation
Provide deterministic simulations for resource loops, cooldown throughput, area coverage, damage/effect budgets, technology progression time, and device production. Compare intended playstyles and identify dominant strategies or softlocks. Tuning changes are versioned and require approval when materially affecting project balance.

## 21. Security and sandboxing
Ability definitions are data-only and schema-validated. Generated code is produced from trusted templates and allowlisted APIs. User-supplied assets and dependencies are treated as untrusted. Build/test environments are isolated with resource limits. No secrets are embedded in generated client artifacts.

## 22. Authoring experience
Provide ability editor, spell-school designer, technology graph, effect composer, resource model editor, device/network designer, compatibility matrix, and balance simulator. Conversational requests become a reviewable specification listing effects, costs, cooldowns, prerequisites, dependencies, platform limits, and risks before approval.

## 23. Validation and testing
Validate IDs, graph cycles, effect parameters, resource bounds, activation rules, permissions, asset references, and platform mappings. Tests cover activation success/failure, cooldowns, cost atomicity, target validation, effect stacking, disconnect/reconnect, multiplayer concurrency, device throughput, migration, and exploit cases. Run in actual supported game versions. Unrun tests are reported as not run.

## 24. Diagnostics and repair
Expose activation traces, rejected preconditions, resource ledger, effect provenance, cooldown state, research graph path, device network status, and compatibility failures. Repair plans preserve unlocks and player resources. Changes to effect semantics, costs, cooldowns, IDs, or progression prerequisites require renewed approval.

## 25. Delivery
Deliver system profiles, ability and spell catalogs, technology/research graphs, effect schemas, device definitions, resource configuration, platform adapters, asset references, migration plans, compatibility reports, balance simulations, and test evidence. Include editable source and runnable packages where supported.

## 26. Acceptance criteria
- Magic and technology systems can be independently enabled or disabled.
- Every ability/effect is declarative, bounded, and versioned.
- Resource costs and cooldowns are atomic and server-authoritative.
- Progression and item ownership remain with their designated engines.
- Effect chains, entity counts, and device networks have hard limits.
- Platform-specific unsupported features are disclosed before approval.
- Multiplayer validation prevents client-forged effects and duplicated costs.
- Balance claims have reproducible simulation and gameplay evidence.
- Migrations preserve player unlocks or provide explicit remapping.
- No arbitrary user script executes in the game or Studio runtime.

## 27. Open decisions
1. Which profiles are required at launch: magic, technology, hybrid, or all?
2. Which Minecraft editions, versions, and Java loaders are launch targets?
3. Which spell/ability primitives are supported initially?
4. Is mana a default resource or project-defined?
5. Which technology energy models are supported?
6. Are research trees mandatory or optional?
7. Which progression requirements can gate unlocks?
8. Are player-created custom effects restricted to a fixed primitive catalog?
9. Are summons, pets, constructs, or temporary entities included?
10. Which device and automation categories are required?
11. What are per-player, per-area, and per-world effect/entity caps?
12. Which effects may modify blocks or terrain?
13. How do claims, region protections, and permissions constrain abilities?
14. What are default cooldown, range, and resource cost policies?
15. How are effect stacking and conflicts resolved?
16. Are PvP abilities enabled by default or separately configured?
17. Which visual/audio asset formats and pipelines are supported?
18. Which research progress is shared in multiplayer?
19. What rollback and migration guarantees apply to removed abilities?
20. Which external libraries/APIs are allowed and under what licenses?
21. What simulation metrics define acceptable balance?
22. Which server performance budgets apply to active effects and devices?
23. What moderation and admin override controls are required?
24. Which exploit, load, and gameplay tests are release blockers?

## 28. Current status
Design draft only. All open decisions remain unresolved until explicitly decided by the product owner. No spell runtime, ability executor, technology tree service, energy network, or playable magic/technology system is implemented by this document.
