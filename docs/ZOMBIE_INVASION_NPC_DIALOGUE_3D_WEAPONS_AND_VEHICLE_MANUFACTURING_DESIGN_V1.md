# Zombie Invasion — NPC Dialogue, 3D Weapons and Vehicle Manufacturing Design V1

Status: USER-REQUESTED SYSTEMS — requirements captured; detailed scope and balancing remain proposals
Date: 2026-11-28

## 1. Purpose

Define three connected pillars requested for the Zombie Invasion project:
1. Interactive NPCs that can converse with the player, including selected fourth-wall-breaking characters.
2. Distinct 3D weapon models and visible attachment customization.
3. A staged vehicle manufacturing and modification ecosystem, from a basic bicycle to buses and mobile living spaces.

This is a design document only. It does not claim that these features have been implemented or tested.

## 2. Interactive NPCs and dialogue

### 2.1 Core interaction
- The player can initiate conversations with eligible in-world characters.
- Dialogue may support selectable responses and free-text input, subject to target-platform capabilities and the final AI/runtime architecture.
- NPCs have stable identities, names, roles, personality traits, goals and knowledge boundaries.
- Dialogue can support quests, trading, warnings, directions, recruitment, aid and world-state information.
- Characters should react to relevant player actions and local events rather than repeating context-free lines.

### 2.2 Character memory and continuity
- Track only game-relevant facts: prior meetings, completed quests, promises, faction reputation and important player choices.
- Memory must be scoped to the world/save and have explicit persistence rules.
- NPC memory must not imply access to the player's real-world identity, device data or private information.
- Dialogue state must be deterministic/replayable enough for testing and quest continuity.

### 2.3 Fourth-wall-breaking characters
The user specifically wants some in-game characters to break the fourth wall and address the player directly.

- This is a deliberate narrative device reserved for selected characters, events or hidden story routes.
- Such characters may distinguish the in-world avatar from the person controlling the game, speak to the player rather than the avatar, or comment on game conventions.
- The effect must be authored and context-aware, not random dialogue spam.
- The narrative must not falsely claim access to real-world personal data or device state.
- Frequency, tone, triggers and whether this is horror, comedy or mystery remain open creative decisions.

### 2.4 NPC roles
Potential roles include survivors, traders, mechanics, medics, guards, scouts, faction leaders and hostile human characters. These are candidates; not all are required in the first playable slice.

### 2.5 Acceptance tests
1. Eligible NPCs expose a clear interaction affordance.
2. Dialogue choices lead to the correct state transitions.
3. Quest/trade state persists correctly across save/load.
4. NPCs do not claim knowledge they were not given in game state.
5. Fourth-wall dialogue occurs only at authored triggers and remains coherent.
6. Java and Bedrock offer equivalent core narrative outcomes, with target-specific UI/implementation.
7. Any test not executed is marked NOT_RUN.

## 3. 3D weapon models and customization presentation

The user requires weapons to have 3D models rather than being represented only by flat inventory icons.

Requirements:
- Distinct model identity for each weapon family and meaningful variants.
- First-person and third-person presentation where supported by each edition.
- Visible reload, firing, aiming, holding and melee animations to the extent supported by the target platform.
- Attachments such as optics, sights, suppressors, grips and magazines should visibly appear on compatible weapons.
- Weapon condition/durability and selected attachments should be reflected in the model or UI where practical.
- Muzzle flash, projectile/tracer presentation, sound and recoil must be consistent with the approved combat design.
- Models, textures, animation rigs and attachment sockets must use a shared asset naming/metadata contract while allowing separate Java and Bedrock exports.

Technical caveat:
- Java/Fabric and Bedrock do not share one universal runtime model/animation format. The Studio must maintain a common logical weapon definition and separate target-specific model, geometry, animation and resource-pack outputs.
- Visual parity should be assessed by equivalent gameplay readability and attachment visibility, not by assuming identical rendering pipelines.

Acceptance tests:
1. Every shipped weapon has the correct 3D model in supported views.
2. Attachments appear only on compatible sockets and visibly affect the model.
3. Reload and firing animations do not desynchronize ammunition state.
4. Model/texture assets load on both target tracks.
5. Low-end performance budgets are measured on agreed test devices.
6. Missing assets fail validation clearly rather than silently substituting unrelated models.

## 4. Vehicle manufacturing ecosystem

### 4.1 Core principle
Vehicles are not all obtained as finished loot. The player can manufacture them through a staged production process at a suitable factory or mechanical facility, then modify and maintain them.

The normal Minecraft Crafting Table remains the entry-level crafting station. It must not directly produce complete cars, trucks, buses, engines or advanced vehicle systems.

### 4.2 Vehicle progression family
The requested vehicle range includes:
- Bicycle as the simplest and earliest craftable vehicle.
- Motorcycles and off-road motorcycles as possible intermediate vehicles.
- Cars and off-road vehicles.
- Pickup trucks and cargo trucks.
- Minibuses and buses.
- Campers, caravans and specialized expedition vehicles.

The bicycle is the baseline entry point. Exact catalogue and progression order remain to be balanced.

### 4.3 Manufacturing stages
A proposed vehicle production flow:
1. Discover a factory, garage or suitable workshop and gain access.
2. Find or unlock the relevant vehicle blueprint/design.
3. Scavenge raw materials, tools and specialist components.
4. Process materials and manufacture subassemblies at the required stations.
5. Assemble the chassis/frame, drivetrain, wheels, controls, electrical system and body.
6. Install fuel/power systems where applicable.
7. Complete safety/functional checks and commission the vehicle.
8. Modify, repair and maintain it over time.

Different vehicle classes require different tools, station tiers, component quantities and build complexity. A bicycle must be achievable earlier and more simply than a bus.

### 4.4 Factories and facilities
Potential facilities:
- Basic bicycle/metalworking bench.
- Mechanical workshop/garage.
- Vehicle assembly bay.
- Advanced factory with heavy assembly capability.
- Electrical/electronics station.
- Paint/bodywork station.

Facilities may be found in the world, restored, powered or constructed, subject to future map and progression design. A full factory production line is a long-term system; the first playable slice may implement a compact assembly bay while preserving the scalable architecture.

### 4.5 Vehicle modification
Modifiable systems may include:
- Engine, transmission and drivetrain.
- Wheels, tires, suspension and brakes.
- Fuel tank and fuel delivery.
- Battery and electrical components.
- Body panels, paint and visual accessories.
- Storage, cargo racks and internal layout.
- Protective armor and defensive equipment, balanced against weight/performance.
- Lighting, navigation and utility equipment.

Every modification must have compatibility rules and measurable effects. Avoid cosmetic attachments that claim nonexistent gameplay benefits.

## 5. Mobile living spaces: buses, caravans and trailers

The user specifically wants a manufactured bus to function as an interior living space, and wants a small living/cargo unit attachable to a bicycle (for example, a small trailer or compact camper).

### 5.1 Bus as a mobile base
A bus may be converted into a mobile living space with modular interior functions:
- Sleeping area.
- Storage and inventory containers.
- Cooking area.
- Water storage/purification equipment.
- Medical/rest area.
- Workbench modules, if size/power requirements are met.
- Battery/electrical system and interior lighting.
- Optional defensive reinforcement.

The bus must be a usable interior space, not merely a large vehicle model. The implementation must define how players enter, navigate and interact with the interior. Depending on platform constraints, this may be implemented as a physically walkable interior or a linked interior space; the player-facing behavior must be clear and consistent.

### 5.2 Bicycle trailer and compact attachments
- A bicycle may tow a small cargo trailer or compact utility module.
- Later progression may unlock a lightweight micro-camper or sleeping pod if technically feasible.
- The attachment must have a clear hitch/connection point, weight/load limit and handling trade-off.
- Do not assume a full walk-in caravan can be attached to a bicycle; the small bicycle attachment is a compact trailer/utility pod concept.

### 5.3 Caravans and larger mobile bases
- Caravans/campers can provide larger storage and living functions.
- They may attach to compatible cars or trucks, subject to towing limits.
- Larger vehicles may support more modules but consume more fuel and require more maintenance.
- Interior modules and vehicle systems must share a consistent storage/power/persistence model.

### 5.4 Vehicle physics and gameplay
- Vehicle movement, collision, turning radius, braking, speed and load should be coherent.
- Cargo and interior modules affect mass/handling where supported.
- Fuel, condition, repair and maintenance integrate with the existing survival economy.
- Vehicle noise may attract zombies according to bounded encounter rules; it must not spawn unlimited enemies.
- Vehicles must have safe enter/exit and recovery behavior to avoid trapping players.

## 6. Cross-system integration

- Factories and garages are loot/exploration destinations.
- Blueprints and rare parts connect loot to manufacturing progression.
- Vehicle storage connects to backpacks and inventory without creating duplication exploits.
- Bus/caravan interiors connect to food, thirst, medical treatment, crafting and sleep systems.
- NPC mechanics may provide repair, manufacturing, trading or blueprint quests.
- 3D weapons connect to the approved attachment and durability systems.
- Fourth-wall narrative events may be linked to rare characters or story milestones, not ordinary system prompts.

## 7. Java and Bedrock compatibility contract

- Maintain shared logical definitions for NPCs, dialogue states, weapons, attachments, vehicles, parts, recipes and interior modules.
- Generate separate Java/Fabric and Bedrock implementation assets.
- Do not assume identical entity AI, UI, vehicle physics, model formats or script capabilities across editions.
- Any feature that cannot meet parity must be explicitly reported with target-specific limitations; never label it complete on both platforms without evidence.
- Runtime, world-save and performance testing are required on both target tracks.

## 8. Open decisions

- Which NPC dialogue features run fully offline, use an external AI service, or combine both.
- Whether NPC free-text chat is required in the first playable slice.
- Fourth-wall character count, narrative tone and trigger design.
- Exact weapon model/animation quality target and asset production pipeline.
- Vehicle catalogue and progression tiers.
- Whether factories are prebuilt world locations, player-buildable facilities or both.
- Vehicle assembly time and whether it can be interrupted.
- Exact bus interior implementation approach on each edition.
- Bicycle trailer versus micro-camper scope and towing rules.
- Multiplayer synchronization and vehicle ownership rules for later milestones.

## 9. Implementation boundary

Design only. This document does not implement NPC AI, dialogue services, 3D assets, vehicle physics, factories, recipes, interiors, Java mods, Bedrock add-ons or playable artifacts.


## 2.6 Player identity and contextual address (explicit user clarification)

The user clarified that NPCs should address the player by the player's chosen in-game name and speak naturally about live gameplay events. Example requested behavior: if the player name is Ömer, an NPC may say "Ömer, böyle olmaz" in response to a relevant action, or a medic may say "Ömer, kemiğin kırılmış" after detecting an in-game fracture.

Requirements:
- Ask for or allow the player to set a preferred character/player name at world or profile setup.
- Use that name naturally in dialogue; avoid inserting it into every sentence.
- NPC dialogue must be grounded in authoritative game-state facts such as injury state, ammunition, health, thirst, hunger, vehicle condition, quest progress and recent player actions.
- A medic may identify a fracture only if the game injury system has actually recorded that fracture; NPCs must not invent diagnoses.
- NPCs can express concern, frustration, encouragement, disagreement or urgency according to their personality and relationship with the player.
- Dialogue should reflect recent events and prior interactions where relevant.
- The player name is an in-game display choice. It must not be inferred from the player's real-world account identity or device data.
- Provide a fallback when no preferred name is set.
- Keep fourth-wall dialogue distinct: ordinary contextual NPC dialogue addresses the in-world player/avatar, while selected fourth-wall characters deliberately address the human player beyond the avatar.

Example event-to-dialogue contracts:
- Injury event: fracture recorded for left arm -> medic can say "Ömer, kolundaki kemik kırılmış. Önce sabitlememiz gerekiyor."
- Resource event: player repeatedly wastes scarce ammunition -> companion may say "Ömer, böyle olmaz. Cephanemiz sınırlı."
- Vehicle event: bus engine condition reaches critical threshold -> mechanic may warn the player by name.
- Quest event: player breaks a promise -> the relevant NPC may confront the player based on the recorded choice.

Acceptance tests:
1. Player can set and change the in-game display name.
2. NPC uses the selected name naturally and correctly.
3. Injury dialogue matches actual injury/body-region state.
4. Resource and vehicle warnings match actual game state.
5. NPC does not claim a fracture, missing limb or other event that has not occurred.
6. Dialogue varies by NPC personality and relationship state.
7. Missing player name produces a graceful fallback.
8. Fourth-wall dialogue remains an explicit authored behavior, not a side effect of ordinary name personalization.
