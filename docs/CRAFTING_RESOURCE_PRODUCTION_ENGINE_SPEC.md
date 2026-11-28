# Crafting & Resource Production Engine Specification

**Document status:** Design draft  
**Version:** 0.1  
**Implementation status:** Not implemented; design requirements only.  
**Approval status:** Awaiting product decisions and baseline approval.

## 1. Purpose
Define a modular crafting and resource-production subsystem for Minecraft projects. It supports vanilla-compatible recipes, custom recipes, workstations, processing chains, machines, resource conversion, production queues, and automation where the selected platform permits. It must generate actual loadable and testable content rather than merely describing recipes.

## 2. Ownership boundaries
- This engine owns recipe definitions, processing rules, production jobs, machine behavior contracts, and resource conversion logic.
- Platform inventory and item storage adapters own authoritative item stacks and inventory mutations.
- Economy Engine owns currency, prices, and transaction ledger.
- World/Map Engine owns machine placement and spatial layout.
- Environment Interaction Engine owns authorized interaction with blocks, containers, and workstations.
- NPC/Profession systems own worker identity, profession, and schedules.
- Quest Engine owns objectives that reference crafting outputs.
- Java/Bedrock/Datapack adapters implement platform-specific recipes and runtime logic.

A resource or item must have one authoritative inventory owner. Do not duplicate stock or transaction state across modules.

## 3. Principles
- Platform/version-aware recipe generation.
- Exact ingredient and output accounting.
- Server-authoritative crafting and machine execution in multiplayer.
- Bounded queues, resource use, and automation.
- Clear recipe provenance, identifiers, dependencies, and conflicts.
- Preserve vanilla recipes unless the user explicitly requests replacement/override.
- Approval before generation and before material changes to approved recipes.
- Build success does not prove recipe loading or gameplay correctness.

## 4. Scope
In scope: shaped/shapeless recipes, cooking/smelting/processing, custom workstations, machine recipes, multi-stage production, byproducts, catalysts, fluids/energy abstractions where supported, batch processing, queues, automation, recipe unlocks, profession interfaces, resource requirements, recipe book/UI integration, and compatibility validation.

Out of scope: real-world manufacturing simulation, unrestricted duplication, external payment, and universal machine/energy systems assumed to work identically across platforms.

## 5. Recipe model
Every recipe includes stable ID, namespace, version, category, input slots/ingredients, quantities, alternatives, catalysts, required station, processing time, output(s), byproducts, experience/reward hooks, unlock conditions, priority, and platform constraints.

Ingredients may reference items, tags, components, fluids, or project-defined resources only where supported. Ambiguous ingredients must be resolved before approval. Output quantities and chance-based results must be bounded and explicit.

## 6. Recipe types and platform adapters
Support platform-appropriate types such as shaped, shapeless, cooking, stonecutting, smithing, custom machine, and scripted processing. The capability registry must identify native, adapter-generated, experimental, or unavailable support for each game version. Never silently downgrade a recipe into a different mechanic.

## 7. Identifier and namespace governance
All custom recipes, items, blocks, entities, stations, and machine types use stable namespaced identifiers. Validate collisions with vanilla, loader, and dependency namespaces. Renames require migration/alias policy. Cross-component references must resolve through the project manifest.

## 8. Ingredient matching and consumption
Define exact item, tag, component, durability, metadata, and count matching where supported. Specify whether ingredients are consumed, damaged, returned, or retained as catalysts. Prevent item substitution and duplicated consumption. Matching rules must be deterministic and testable.

## 9. Processing stations and machines
A station/machine definition includes identity, platform implementation, input/output slots, allowed recipes, processing speed, resource/energy requirements if applicable, operating conditions, permissions, interaction UI, persistence, and failure behavior.

Machine visuals and models are owned by Resource Pack; placement and world geometry by World Engine; authoritative processing by this engine's runtime adapter. Unsupported machine behavior must be identified before approval.

## 10. Production jobs and queues
A job records recipe ID/version, owner, inputs reserved, outputs expected, progress, station, status, timestamps, and idempotency key. Lifecycle may include Queued, Reserved, Processing, Paused, Completed, Cancelled, Failed, and Recovered.

Queues require limits, priority, cancellation/refund policy, station availability, and recovery. Never consume inputs without a recoverable job record. Prevent duplicate output after crashes or retries.

## 11. Multi-stage production chains
Production graphs may link recipes into stages with dependencies, intermediate storage, quality/variant rules, and failure handling. Validate cycles, missing inputs, impossible quantities, dead ends, and resource bottlenecks. Define whether intermediate outputs are reserved, stored, or transferred between machines.

## 12. Automation and logistics
Automation may include item transfer, machine routing, conveyor-like systems, pipes, filters, storage networks, and worker-operated production where platform support exists. Define network topology, transfer rate, capacity, access permissions, chunk boundaries, power/resource costs, and failure fallback. Avoid unbounded item scans or cross-region ticking.

## 13. Energy, fluids, and abstract resources
Optional systems may define energy, heat, fluids, pressure, or custom process resources. Each resource declares unit, storage, transfer, production, consumption, conversion, limits, and UI representation. These are project-defined mechanics, not assumed native Minecraft features. Their simulation must be bounded and platform-specific.

## 14. Quality, variants, and byproducts
Optional outputs may include quality tiers, variants, durability, byproducts, waste, or probabilistic results. Define deterministic seed policy for tests, probability bounds, rounding, output caps, and item metadata compatibility. Do not add random outputs without showing them in the approved recipe specification.

## 15. Unlocks, progression, and professions
Recipe unlock conditions may depend on discoveries, quests, achievements, permissions, or professions. Quest system owns quest state; NPC/Profession system owns worker roles and schedules; this engine evaluates declared conditions and emits completion facts. Avoid circular dependency between recipe unlock and required recipe output.

## 16. Economy integration
Buying inputs, selling outputs, station fees, and market prices are delegated to Economy Engine. Crafting costs and item consumption are recorded as production events; currency movement is a separate transaction. Prevent duplicated deductions or rewards across retries.

## 17. Multiplayer and permissions
Server authority validates recipe, inputs, station, job ownership, queue access, and output delivery. Define shared machines, private stations, party ownership, permissions, simultaneous use, and disconnect handling. Protect inventories and prevent client-forged recipe completion.

## 18. Persistence and recovery
Persist job progress, reserved inputs, machine state, queue order, and required resource state. Use versioned schemas and migrations. Define crash recovery at reservation, processing, output commit, and cancellation. Reconciliation must not duplicate or destroy items. Corrupt state enters a safe recovery state and is surfaced to administrators.

## 19. Performance and scalability
Declare recipe lookup complexity, active machine caps, queue limits, processing cadence, transfer throughput, and per-tick budget. Prefer event-driven updates and batched processing. Avoid scanning all inventories or ticking idle machines. Benchmark large factories and multiplayer contention on declared server profiles.

## 20. Security and exploit prevention
Protect against item duplication, forged outputs, recipe spoofing, queue replay, negative counts, overflow, unauthorized machine access, and malicious recipe loops. Enforce quantity caps, server validation, bounded processing graphs, rate limits, and isolated generated builds/scripts.

## 21. Authoring UX
Provide recipe editor, ingredient/tag selector, station/machine designer, production graph, queue simulator, resource/energy editor, unlock-condition editor, compatibility view, and conflict detector. Conversational requests become structured recipes and production plans. Show inputs, outputs, byproducts, costs, platform limitations, and affected components before approval.

## 22. Validation and testing
Validate schema/IDs, ingredient references, namespace conflicts, recipe type support, quantities, catalysts, graph cycles, impossible production chains, output bounds, machine capabilities, queue transitions, persistence migrations, and permission rules. Runtime tests cover recipe discovery, crafting, station operation, input/output conservation, queue pause/resume/cancel, crash recovery, multiplayer contention, and performance. Unrun tests are reported as not run.

## 23. Diagnostics and repair
Expose opt-in recipe resolution, ingredient match, job lifecycle, machine state, resource consumption, output commit, and failure traces. Repair plans identify affected recipes/stations/dependencies and preserve user-edited assets. Changes to approved input/output balance, production time, random yield, or unlock progression require renewed approval.

## 24. Delivery
Deliver recipe definitions, machine/station configurations, runtime source/artifacts, required item/block assets, production graph, dependency and compatibility report, migration data, test evidence, and installation instructions. Include editable source and platform-appropriate package outputs.

## 25. Acceptance criteria
- Recipes have stable IDs and explicit platform support.
- Ingredient/output accounting is correct and testable.
- Production jobs are recoverable and idempotent.
- Queues and automation are bounded.
- Machine ownership and inventory authority are unambiguous.
- Vanilla overrides and dependency conflicts are visible.
- Multiplayer crafting is server-authoritative.
- Tests cover duplication, crash recovery, and concurrent use.
- Generated content is load-tested and gameplay-tested where possible.
- Approved recipe changes trigger impact review and renewed approval.

## 26. Open decisions
1. Which platforms, game versions, and Java loaders are mandatory at launch?
2. Which vanilla recipe types are required for first release?
3. Are custom workstations and machines in first-release scope?
4. Which Bedrock recipe and Script API capabilities are supported?
5. Should recipe ingredients support tags, components, durability, and metadata initially?
6. Are fluids, energy, heat, and other abstract resources included or deferred?
7. What are maximum recipe input/output counts and stack quantities?
8. Are probabilistic outputs supported at launch?
9. What queue size and concurrent machine limits are supported?
10. Is multi-stage factory automation part of first release?
11. Which logistics/transport mechanisms are required?
12. Are NPC workers allowed to operate machines initially?
13. How are recipe unlocks integrated with quests, achievements, and professions?
14. What is the default policy for overriding vanilla recipes?
15. How are recipe conflicts with other mods resolved?
16. What persistence guarantees apply to active jobs and reserved inputs?
17. What is the recovery/refund policy for interrupted production?
18. Which multiplayer ownership and shared-machine permissions are required?
19. What performance profiles and stress tests define acceptance?
20. Which machine visuals/UI assets are mandatory?
21. What item conservation and anti-duplication tests are release blockers?
22. Which external libraries/loaders are permitted and under what license policy?
23. Should recipe export/import and sharing be supported at launch?
24. What human playtests establish that a generated production chain is understandable and balanced?

## 27. Current status
Design draft only. All open decisions remain unresolved until explicitly decided by the product owner. No code, recipe, machine, production queue, or playable crafting system is implemented by this document.
