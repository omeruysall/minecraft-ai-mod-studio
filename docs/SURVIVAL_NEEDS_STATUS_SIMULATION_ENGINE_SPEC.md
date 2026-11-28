# Survival, Needs & Status Simulation Engine Specification

**Document status:** Design draft  
**Version:** 0.1  
**Implementation status:** Not implemented; design requirements only.  
**Approval status:** Awaiting product decisions and baseline approval.

## 1. Purpose
Define optional survival needs and player status mechanics beyond or extending vanilla Minecraft, such as thirst, temperature, fatigue, sleep, hygiene-like abstractions, injuries, disease-like hazards, stress, and environmental exposure. The engine must be modular, configurable, accessible, and compatible with vanilla survival rather than forcing one survival model on every project.

## 2. Ownership boundaries
- This engine owns need meters, status-effect rules, exposure calculations, recovery conditions, and survival simulation policies.
- Combat Engine owns combat damage and encounter state.
- Item/Inventory Engine owns food, medicine-like items, equipment, and item transactions.
- Crafting Engine owns consumable production and recipes.
- Agriculture Engine owns food production and freshness definitions.
- Ecology and World Events engines own environmental facts and hazards.
- Progression Engine owns skill-based mitigation and unlocks.
- NPC Engine owns NPC identity and behavior; NPC needs are referenced through explicit contracts.
- Platform adapters apply supported status/effect mechanics.

## 3. Principles
- All mechanics are optional and independently configurable.
- Vanilla hunger, health, and status behavior is preserved unless explicitly overridden.
- Every meter has a clear purpose, bounded range, decay/recovery rules, and player feedback.
- Avoid excessive micromanagement and unavoidable death spirals.
- Multiplayer state is server authoritative.
- Accessibility settings can reduce or disable nonessential pressure mechanics.
- No real-world medical or physiological accuracy is implied.
- User approval is required before enabling new survival burdens.

## 4. Scope
In scope: thirst, temperature, fatigue, sleep, stamina-like resources, environmental exposure, injury abstractions, status conditions, recovery, shelter/clothing/food/water interactions, difficulty profiles, safe zones, optional NPC needs, UI feedback, and admin controls.

Out of scope: medical diagnosis, real-world health simulation, mandatory bodily-function mechanics, and unbounded debuffs that remove player agency.

## 5. Survival profile
A profile defines stable ID, enabled needs, difficulty, tick/update policy, death policy, recovery rules, dimension/biome overrides, multiplayer scope, UI visibility, accessibility options, and persistence. Projects may select vanilla-compatible, light survival, hardcore simulation, or custom profiles.

## 6. Need meter model
Each need defines stable ID, value range, initial value, decay function, update cadence, warning thresholds, critical threshold, recovery sources, stacking rules, and effects. Define whether meters pause in menus, unloaded chunks, safe zones, or offline sessions. Calculations must be bounded and deterministic where required.

## 7. Thirst and hydration
Optional thirst mechanics define consumption rate, water source validation, container interactions, water quality abstraction, recovery amount, and environmental modifiers. Item/Inventory owns containers and item stacks. Avoid punishing players for unclear or unavailable water sources. Water quality is a game mechanic, not real-world safety guidance.

## 8. Temperature and exposure
Temperature may depend on biome, weather, altitude, dimension, time, shelter, armor/clothing, and nearby heat/cold sources. Define thresholds, update cadence, mitigation, and status effects. World/Events engines provide environmental facts; this engine calculates player exposure. Avoid expensive per-tick scans.

## 9. Fatigue, sleep, and rest
Define fatigue accumulation, rest recovery, sleep requirements, safe sleeping conditions, multiplayer sleep rules, and consequences of prolonged wakefulness if enabled. Distinguish vanilla night-skip behavior from custom fatigue mechanics. Avoid forced real-time schedules unless explicitly chosen.

## 10. Stamina and exertion
Optional stamina may affect sprinting, jumping, swimming, climbing, blocking, or abilities. Define costs, regeneration, exhaustion, caps, and interaction with vanilla food/attributes. Combat and Progression engines consume validated stamina facts through explicit interfaces.

## 11. Injuries and status conditions
Status conditions define source, severity, duration, stacking, symptoms/effects, treatment, immunity, and expiration. Keep injury and disease-like content abstract and non-graphic. Combat owns damage events; this engine may translate approved event facts into status conditions. No medical claims or advice are made.

## 12. Food, water, shelter, and equipment integration
Food and water sources reference Item and Agriculture systems. Shelter references World/Map structures and Environment Interaction permissions. Clothing/armor references Equipment definitions. All recovery and consumption actions use authoritative inventory transactions and cannot duplicate items.

## 13. Environmental hazards and events
Heat waves, cold snaps, storms, toxic-like fictional zones, altitude, and dimension hazards consume facts from World Events and Environment systems. Define safe-zone rules, hazard immunity, warning lead time, and exit routes. Hazards must be visible and avoid trapping players in unavoidable failure states.

## 14. Difficulty and player agency
Difficulty profiles tune decay, severity, recovery, warning thresholds, and death penalties. Provide opt-in and server-configured policies. Define whether players can disable individual needs, use accessibility settings, or receive grace periods. Competitive servers may enforce a shared profile, clearly shown before joining.

## 15. Death, respawn, and recovery
Define what happens to meters and conditions on death, respawn, revival, teleport, dimension change, and world reset. Coordinate item drops with Item Engine and spawn safety with World/Map Engine. Prevent persistent status bugs and ensure recovery is possible.

## 16. NPC needs (optional)
NPC needs may be represented as aggregate settlement demand or individual state. NPC Engine owns identity and behavior; Settlement and Agriculture engines own service/food supply. Avoid simulating every need for every unloaded NPC. Player and NPC rules may differ but must be declared.

## 17. Multiplayer authority and persistence
Server validates need updates, consumption, recovery, status application, and death transitions. Define synchronization frequency, late join, disconnect, offline progression, pause behavior, and server restart. Persist only necessary state and use versioned migrations.

## 18. UI, feedback, and accessibility
Provide configurable meters, contextual warnings, status detail, recovery guidance, source attribution, and accessibility settings. Do not rely on color alone. Avoid excessive screen clutter; allow compact HUD, full status screen, and notification controls. Clearly distinguish urgent gameplay warnings from informational prompts.

## 19. Authoring experience
Provide need editor, decay curve editor, environment modifier map, recovery source selector, status effect builder, difficulty presets, and simulation preview. Conversational requirements become a structured survival profile with example timelines, death risks, accessibility implications, platform support, and dependencies before approval.

## 20. Balance and simulation
Simulate representative play sessions across biomes, dimensions, difficulty settings, and player activity. Measure time-to-warning, time-to-critical, recovery availability, and softlock risk. Ensure new mechanics do not make basic exploration or building unreasonably burdensome. Provide tuning reports and reproducible seeds.

## 21. Security and exploit prevention
Validate all meter changes and item consumption server-side. Prevent client-forged recovery, status clearing, meter freezing, duplicated consumables, and modifier exploits. Bound custom formulas and update rates. Admin overrides are permission-checked and audited.

## 22. Validation and testing
Validate meter bounds, decay/recovery formulas, threshold ordering, status stacking, item references, environment inputs, difficulty profiles, accessibility behavior, and migration. Runtime tests cover decay, recovery, shelter, weather transitions, death/respawn, dimension changes, reconnect, concurrent item use, and multiplayer synchronization. Balance tests include edge cases and softlock checks. Unrun tests are reported as not run.

## 23. Diagnostics and repair
Expose need history, decay source, environment modifiers, recovery attempts, status application/removal, and server reconciliation. Repair plans must restore valid meter ranges and preserve intended player state. Changes to decay, critical thresholds, death penalties, or recovery availability require renewed approval.

## 24. Delivery
Deliver survival profiles, need/status definitions, platform adapters, UI metadata, configuration presets, migration scripts, compatibility report, balance simulations, test evidence, and player guide. Manifest declares enabled mechanics and dependencies.

## 25. Acceptance criteria
- Every need is optional, bounded, and explainable.
- Vanilla mechanics are not silently replaced.
- Recovery sources are discoverable and available.
- No unavoidable death spiral or softlock exists in supported scenarios.
- Multiplayer state is server authoritative and recoverable.
- Item consumption and status effects cannot be duplicated or forged.
- Accessibility and difficulty settings are respected.
- Performance is bounded for loaded and unloaded worlds.
- Balance claims have simulation and gameplay evidence.
- Material survival-rule changes require renewed approval.

## 26. Open decisions
1. Is custom survival a core feature or optional module?
2. Which platforms, versions, and loaders are required?
3. Which needs are supported initially: thirst, temperature, fatigue, stamina, or others?
4. Are vanilla hunger and health systems preserved, extended, or replaced?
5. Which difficulty presets are included?
6. Can servers enforce a profile while players configure accessibility presentation?
7. Do meters advance while offline, paused, or in unloaded chunks?
8. Which water quality mechanics, if any, are permitted?
9. Which environmental temperature inputs are supported?
10. Are sleep/fatigue mechanics tied to world time or real time?
11. Which actions consume stamina?
12. Are injury/status conditions included in the first release?
13. What is the policy for disease-like fictional effects?
14. Which items and equipment mitigate survival conditions?
15. What are death, respawn, and recovery defaults?
16. Are NPC needs simulated individually or in aggregate?
17. What HUD elements and warning controls are mandatory?
18. Which accessibility options can disable or reduce pressure mechanics?
19. What survival simulation scenarios define balance acceptance?
20. Which performance caps apply to active players and NPCs?
21. Which admin override and audit features are required?
22. What happens when a required recovery resource is unavailable?
23. Which external survival libraries are allowed and under what licenses?
24. What softlock, multiplayer, and human playtests are release blockers?

## 27. Current status
Design draft only. All open decisions remain unresolved until explicitly decided by the product owner. No custom thirst, temperature, stamina, fatigue, injury, or survival status runtime is implemented by this document.
