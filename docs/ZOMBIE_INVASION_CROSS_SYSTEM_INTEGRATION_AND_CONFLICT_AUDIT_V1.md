# Zombie Invasion — Cross-System Integration and Conflict Audit V1

Status: Architecture/design audit for the user-approved expanded scope. This is not implementation or runtime validation.
Date: 2026-11-28

## 1. Executive result
The newly approved systems are compatible with the existing design direction if they use shared authoritative state and clear subsystem ownership. The principal risks are duplicated resource simulation, conflicting event ownership, excessive per-block/per-entity ticking, and feature scope being mistaken for first-playable scope.

## 2. Canonical shared registries
The project should define canonical data contracts for:
- Resource item/material identity, quality, condition, quantity and provenance.
- Water state and contamination class.
- Fuel type and engine/generator compatibility.
- Electrical generation, storage, consumption and network faults.
- NPC identity, profession, skills, needs, faction, inventory and task.
- Faction identity, relations, territory and stock.
- Structure ownership, integrity, access and zone.
- Vehicle identity, class, condition, fuel, cargo, passengers and route.
- World event identity, source, region, severity, lifecycle and evidence.
- Quest/research/blueprint identity and prerequisites.

All subsystem docs and manifest components should reference these shared IDs rather than inventing parallel definitions.

## 3. Ownership boundaries
| Domain | Authoritative owner | Other systems may |
|---|---|---|
| Player injury/health/thirst/hunger | Survival and injury state | Read and react; never overwrite |
| Loot and item creation | Loot/crafting/economy | Request drops/recipes through contracts |
| Water quantity and quality | Water infrastructure | Consume, transfer via network contract |
| Fuel quantity/type | Fuel inventory/storage registry | Consume only if compatible |
| Electricity supply and faults | Power network | Request/consume power |
| Base claims/structure integrity | Base building | Query access, damage via approved events |
| NPC identity/needs/tasks | NPC simulation | Assign valid tasks, read state |
| Faction relations/stock | Faction/economy service | Request diplomacy/trade actions |
| Horde schedule and budget | Encounter Director | Receive events; no duplicate spawning |
| Individual zombie behavior | Zombie AI | Receive target/pressure context |
| Fire propagation | Environmental hazard service | Receive ignition/extinguish/damage events |
| Disease exposure | Disease service | Read exposure/treatment state |
| Wildlife population | Ecology service | Request hunting/harvest interactions |
| Radio transmissions | Communications service | Publish/receive known signals |
| Research unlocks | Research/blueprint service | Check prerequisites; no direct item grants |
| Quests/story state | Quest/story service | Consume events and set objectives |
| Skills | Character progression | Modify permitted action outcomes |
| Trade stock/prices | Economy service | Request transactions |
| Vehicle state/transport | Vehicle/transport service | Query route, capacity and condition |

## 4. Explicit conflict checks and resolutions
### 4.1 Water vs thirst, food and disease
One water ledger owns quantity and quality. Drinking, cooking, medicine, showers and sanitation request consumption from it. Disease exposure reads source/quality events; it does not independently contaminate inventory. This prevents double consumption and contradictory potable states.

### 4.2 Water vs power
Pumps and treatment plants request electricity from the power network. Manual collection, gravity flow and hand pumps provide fallback paths. Avoid circular dependencies and make critical consumers configurable.

### 4.3 Fuel vs vehicles, generators and fire
A single fuel registry defines gasoline/diesel and compatibility. Vehicle engines and generators consume from the same inventory/storage service. Fire reads fuel leak/ignition events; it does not own or duplicate fuel quantities.

### 4.4 Base defense vs zombie AI and encounter director
The Encounter Director schedules bounded horde events. Zombie AI controls each infected. Base systems expose fortifications, noise, light, entrances and integrity. The director must not spawn an independent siege on top of a horde event.

### 4.5 NPCs vs quests, economy and dialogue
NPC simulation owns identity, inventory, needs and task. Quest service owns objectives; economy owns stock and transactions; dialogue reads authoritative state. Dialogue cannot grant rewards, diagnose injuries or change faction reputation without an explicit action/event.

### 4.6 Skills vs crafting and injuries
Skills modify valid actions and efficiency but do not bypass station, material, blueprint or treatment requirements. A skill cannot heal a fracture or create missing components.

### 4.7 Wildlife vs loot and food
Harvesting wildlife generates defined resources once, with population accounting. Loot service handles item drops; ecology service updates population. No duplicate animal loot and hunting reward.

### 4.8 Research vs story and crafting
Research unlocks blueprint/knowledge records. Crafting consumes recipes and inputs. Story discovers evidence and prerequisites. Research must not directly spawn a finished weapon, vehicle or cure.

### 4.9 Transport vs vehicles, map and NPC simulation
The existing vehicle registry remains canonical. Convoy, train, boat and helicopter are transport modes/classes, not separate inventory or fuel systems. NPC driving and distant travel are abstracted outside active simulation range.

### 4.10 Fire vs electrical faults and fuel storage
Electrical and fuel systems emit fault/leak/ignition events; the environmental hazard service resolves fire. One fire state owns spread, damage and extinguishing.

## 5. Performance and persistence architecture
- Prefer event-driven updates over continuous per-block polling.
- Use bounded network graphs for power/water rather than fluid simulation at every block.
- Use region-based simulation and distance-based fidelity for NPCs, wildlife, hordes and convoys.
- Cap concurrent active entities, horde budgets, fire fronts, automation rules and network recalculations.
- Persist durable state transitions; reconstruct transient visual effects after load.
- Save event IDs and lifecycle state to prevent duplicate raids, quests, fires, transactions or resource consumption after reload.
- Avoid loading distant chunks solely to simulate NPC or vehicle movement.

## 6. Cross-edition compatibility gates
The shared design contract defines equivalent player-facing outcomes, not identical code. Java Fabric and Bedrock stable Script API receive separate capability checks and adapters. Any feature requiring experimental Bedrock APIs remains out of scope under the current no-experimental-API decision unless the user changes that decision. If a capability cannot be delivered equivalently, document a constrained implementation or explicit platform limitation before approval. Validate exact target-version support; do not infer it from a nearby preview or later version.

## 7. First playable scope protection
The long-term feature scope is now broad, but it does not mean every system enters the first playable build. First playable remains a bounded vertical slice. Each subsystem needs a milestone, dependency list, implementation estimate, Java/Bedrock capability status and acceptance evidence before being assigned to a build.

## 8. Audit findings
- No fundamental design contradiction found between the new systems and existing power, crafting, NPC, injury, vehicle, map and encounter specifications.
- Main integration risk: multiple systems independently owning the same resource or world event. Resolved by the ownership table and shared registries above.
- Main technical risk: simulating large-scale water/power graphs, autonomous NPC populations, horde sieges, fire spread and transport continuously on both editions. Mitigation: bounded graphs, event-driven updates, regional simulation and staged fidelity.
- Main scope risk: treating user-approved long-term feature coverage as first-slice delivery. Mitigation: separate scope approval from milestone approval.

## 9. Required future validation
1. Build a shared resource/state schema for water, fuel, power, NPC, faction, structure, event and vehicle.
2. Map every feature to manifest component IDs and dependencies.
3. Produce Java and Bedrock API capability matrices for exact target versions.
4. Profile water/power network updates and entity/event budgets.
5. Test save/reload idempotency for resource transactions, horde events, fires and NPC tasks.
6. Run cross-system integration tests before any production claim.
