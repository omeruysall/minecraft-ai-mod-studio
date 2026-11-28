# Zombie Invasion — Survivor NPCs, Professions, Factions and Settlement Design V1

Status: User-approved system scope; detailed mechanics are design proposals. Not implemented.

## 1. Core model
Survivors are persistent world actors with identity, needs, skills, relationships, schedule, knowledge, inventory, current task and faction affiliation. The game must distinguish actual simulated state from dialogue claims. Existing player-name-aware dialogue requirements remain authoritative.

## 2. Rescue and recruitment
- Survivors may be found trapped, hiding, injured, guarding locations, travelling or held by hostile groups.
- Rescue can require clearing threats, medical aid, supplies, negotiation or completing a task.
- Recruited survivors travel to a selected safehouse/settlement and require food, water, shelter and protection.
- Recruitment is not guaranteed; personality, trust, faction ties, player actions and settlement capacity influence willingness.
- NPC death, injury, departure or capture must follow clear rules and be signalled to the player.

## 3. Professions and skills
Initial profession taxonomy: medic, mechanic, guard, scavenger, farmer, cook, builder, electrician, water technician, trader, researcher and radio operator. A profession grants capabilities and efficiencies, not magical access to items. NPCs require tools, materials, station access and time to complete work. Cross-training is possible through mentorship or experience, with limits.

## 4. Schedules and autonomy
NPC daily routine uses a small set of readable states: sleep, eat, work, patrol, socialize, travel, treat patient, rest, shelter and emergency response. Schedules adapt to weather, injuries, threat alerts, resource shortages and assigned priorities. Off-screen simulation is abstracted and bounded; NPCs must not continue consuming resources or travelling in unloaded chunks in ways that create unbounded or unfair outcomes.

## 5. Dialogue, memory and player context
- NPCs converse with the player and, where feasible, each other.
- The player-selected in-game name is used naturally and contextually.
- Dialogue reads authoritative game state for injury, hunger, thirst, ammo, health, power, water, quest and vehicle condition.
- Medical dialogue may name a fracture only if the injury system has recorded it.
- NPC knowledge has sources and limits; they cannot know distant events without communication or observation.
- Selected authored characters may break the fourth wall, separate from ordinary in-world dialogue, without claiming real-world private knowledge.
- Relationship and personality alter tone, not factual state.

## 6. Factions and diplomacy
Faction data includes identity, goals, territory, resources, reputation, leadership, relations and known information. Relations include neutral, allied, trading, tense and hostile states. Actions that alter reputation are recorded with context. Alliances can enable trade, safe passage, recruitment or joint defense; hostility can cause ambushes, blockades or raids. Avoid irreversible faction hostility from a single ambiguous action; provide clear warnings and recoverable diplomacy paths where appropriate.

## 7. Settlement governance
Players can set work priorities, ration policies, patrol areas, access permissions and emergency protocols. NPCs have morale/trust and basic needs, but avoid excessive hidden management meters. Settlement capacity depends on beds, food, water, medical capacity and defense. Population growth must not be automatic or limitless.

## 8. Trading and resource accounting
NPC inventories and faction stock are finite. Trade uses item barter and/or a defined currency system; the currency choice is unresolved. Prices respond to scarcity and faction conditions within bounded ranges. No NPC may sell an item that is not in its stock or valid trade generation rules.

## 9. Acceptance criteria
1. Survivors can be discovered, rescued and recruited through explicit interactions.
2. NPC needs and settlement capacity are visible at useful levels.
3. Professions require tools, materials and suitable workstations.
4. Schedules respond to emergencies and world conditions.
5. NPC-to-NPC dialogue and off-screen simulation respect knowledge and loaded-world boundaries.
6. Faction relations respond to recorded player actions.
7. Trade inventory is finite and auditable.
8. Dialogue reflects real gameplay state and player-selected in-game name.
9. No NPC silently creates resources or completes impossible tasks.

## 10. Open decisions
Recruitment limits, population scale, exact morale/trust model, faction count, diplomacy depth, currency model, schedule granularity, multiplayer behavior and AI dialogue runtime are unresolved. Java and Bedrock must share the same authored behavior contract while using edition-specific implementation.
