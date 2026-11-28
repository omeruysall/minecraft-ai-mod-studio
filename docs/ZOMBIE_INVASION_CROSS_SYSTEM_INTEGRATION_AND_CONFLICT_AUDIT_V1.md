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


## 10. Multiplayer authority extension (proposal; pending user approval)

If optional multiplayer is approved, the server becomes the authoritative writer for shared world state. Existing domain owners remain unchanged:
- Inventory, loot, crafting and trade remain owned by their existing services; multiplayer adds server validation and atomic commit, not duplicate ownership.
- Base claims and permissions remain owned by the base/authorization contract; client UI is never the security boundary.
- NPC, faction, quest, horde, zombie, fire, disease, ecology and transport services each retain their single authoritative world owner.
- Replication distributes committed state; it must not replay gameplay side effects on clients.
- Event and transaction IDs are idempotent across reconnect, retry and server recovery.
- Java and Bedrock server adapters remain separate. Cross-edition play is not assumed.
- The single-player path uses the same gameplay contracts without requiring a network server.

Detailed multiplayer rules, proposed modes and open policy decisions are in `docs/ZOMBIE_INVASION_MULTIPLAYER_COOPERATION_AND_SERVER_DESIGN_V1.md`. This extension is a proposal only until the user approves multiplayer and its policies.


## 11. Ecosystem and environmental simulation integration

The comprehensive contract is `docs/ZOMBIE_INVASION_ECOSYSTEM_BIOMES_WILDLIFE_AND_ENVIRONMENT_SIMULATION_DESIGN_V1.md`.

Additional integration rules:
- World/region service owns biome, habitat and climate identity; ecology must not independently infer a different biome for the same location.
- Weather service owns the authoritative clock and weather snapshot; farming, wildlife, fire, water, power and zombie perception consume that snapshot.
- Ecology owns wild populations and natural resource patches; farming owns cultivated crops and claimed livestock; item/loot services own resulting item creation and quality.
- Hunting/fishing/gathering uses a single idempotent harvest transaction. Ecology updates population/resource quantity; loot creates the item output exactly once.
- Water service owns water quantity and quality. Farming and wildlife may consume water only through its contract; disease reads contamination/exposure events and cannot independently mutate water quality.
- Environmental hazard service owns fire/flood/drought/pollution propagation; ecology receives habitat-damage events and updates regional suitability/population summaries.
- Disease service owns exposure and disease state. Zombie infection remains a distinct system unless a deliberately approved story rule links it.
- Wildlife/zombie interactions are explicit, bounded events. Animals do not automatically become infected, and wildlife cannot bypass encounter budgets.
- NPC simulation owns profession, needs and tasks. Farming/ecology provide valid work contracts; dialogue reads resulting state but cannot fabricate completed work.
- Active, near-region and distant simulation use different fidelity levels; distant simulation never loads chunks just to tick entities.
- Stable IDs, event idempotency, save migrations and Java/Bedrock independent evidence are mandatory.

This integration audit is architectural analysis only. No simulation, performance or compatibility test is claimed.


## 12. Dynamic world simulation and resource-accounting integration

The integrated specification is `docs/ZOMBIE_INVASION_WORLD_SIMULATION_RESOURCE_CYCLES_AND_DYNAMIC_WORLD_DESIGN_V1.md`.

Additional conflict controls:
- World time/weather is the only authoritative clock and weather snapshot; crops, NPC schedules, spoilage, power, water and hazards consume the same time basis.
- Regional summaries are derived views, not duplicate inventories. Resource quantities remain owned by ecology, farming, item/inventory, water, fuel, power and economy domains as defined in their contracts.
- Resource transactions reconcile opening stock, production/import/recovery, consumption/export, spoilage and loss. Negative stock and duplicate commits are invalid.
- Production reserves inputs and commits outputs once; blueprint unlocks do not grant finished goods.
- Logistics moves existing stock and records route capacity, cost, interruption and loss; it must not create resources.
- Market transactions atomically validate stock, payment/barter, capacity, access and price to prevent duplication and buy/sell loops.
- Settlement population changes only through explicit rescue, recruitment, departure, death or relocation events. NPC knowledge and faction reactions obey information boundaries.
- Regional outbreak pressure is a bounded summary; Encounter Director owns horde events and Zombie AI owns individual behavior.
- Distant simulation aggregates elapsed-time changes without loading remote chunks; activation/save/reload must conserve quantities and event order.
- The shared manifest must bind stable IDs, event schemas, dependencies, platform capabilities and acceptance criteria. Java and Bedrock require separate evidence.

These are architecture constraints, not test results. Resource reconciliation, transaction idempotency, distant simulation, save migration, market exploits and edition parity remain required validation work. First playable scope remains separately controlled.


## 13. Player journey and progression ownership audit

Integrated progression design: `docs/ZOMBIE_INVASION_PLAYER_JOURNEY_CAMPAIGN_AND_LONG_TERM_PROGRESSION_DESIGN_V1.md`.

Ownership and conflict rules:
- Quest/story service owns objectives, evidence and quest lifecycle; it reads committed events from combat, inventory, crafting, NPC, faction, research, transport and world services.
- Settlement projects are persistent work plans, not duplicate quest inventories. Construction, materials, labor and completion remain owned by their respective domain services.
- Research owns knowledge and blueprint unlock records; crafting/manufacturing owns actual production and item creation.
- Faction service owns reputation, relations and access policy; dialogue and quest text may present outcomes but cannot mutate them independently.
- NPC simulation owns recruitment, identity, needs, skills, availability and task completion; rewards cannot create duplicate NPCs or free labor.
- Skill progression may improve valid actions but cannot bypass authoritative injury, station, material, tool, power or qualification requirements.
- Campaign progress and player choices persist through stable IDs and idempotent events; migration must not duplicate rewards or reset completed objectives.
- Sandbox continuation remains possible after major story milestones. No ending should force world deletion by default.
- First-playable scope remains protected; long-term campaign breadth does not imply first-slice delivery.

This is a design-level audit. Quest soft-lock testing, save migration, reward idempotency, NPC availability and Java/Bedrock parity remain unvalidated implementation gates.


## 14. Master dependency map and cross-system controls

See `docs/ZOMBIE_INVASION_MASTER_FEATURE_DEPENDENCY_AND_IMPLEMENTATION_MAP_V1.md` for the integrated feature-family matrix and dependency layers L0–L12.

Additional controls consolidated in that map:
- No circular bootstrap dependency among power, fuel, water, factory, NPC labor, research, transport or prosthetics; each critical path must retain a valid bootstrap or alternate acquisition route.
- Shared feature requirements map to distinct Java and Bedrock components, build jobs and evidence records.
- First-playable feature IDs must be reconciled against the vertical-slice specification before scope freeze; long-term systems do not silently enter the first milestone.
- The 232-entry traceability matrix must be assessed feature by feature; a master dependency document does not imply all features are designed or approved.
- The project manifest remains the execution contract; discrepancies require an explicit revision rather than an implicit precedence decision.
- Test gates cover transaction integrity, save migration, gameplay state, regional performance and independent target validation.

This is a design-level consolidation, not runtime validation.


## 15. Feature traceability completeness status

The current 232-entry feature matrix was assessed in `docs/ZOMBIE_INVASION_FEATURE_TRACEABILITY_GAP_ASSESSMENT_V1.md`. At this snapshot all 232 entries remain planned / needs traceability review; no per-feature dependency edges, acceptance criteria or test cases are marked defined, and Java, Bedrock and parity statuses remain not assessed. The master dependency map is therefore an architecture-level guide only, not proof of completed feature-level mapping.


## 16. Foundation compatibility and traceability controls

The detailed BASE-001..BASE-012 specification is recorded in `docs/ZOMBIE_INVASION_FOUNDATION_COMPATIBILITY_AND_TRACEABILITY_SPEC_V1.md`.

Integration constraints:
- Edition selection precedes target version, loader/API, dependency and runtime resolution.
- Java and Bedrock have independent dependency locks, component graphs, packaging and test evidence.
- Stable logical IDs map to target-specific physical IDs; renames require migration aliases.
- Configuration schema migration and world-save migration are separate concerns with explicit backup/recovery gates.
- Client presentation state cannot become authoritative gameplay state.
- Dependency and asset provenance/license checks gate redistribution.
- First-slice local single-player evidence does not imply dedicated-server, Realm or hosted-runtime support.
- The 32 dependency edges, 55 acceptance criteria and 51 tests in the new specification are design artifacts; they have not been executed.

The feature traceability matrix remains at its prior review state pending formalization of machine-readable edge and target-status semantics. No implementation or compatibility test is claimed.
## 17. Foundation traceability matrix v1.2.0

## 18. QA, build and delivery integration controls

A second traceability batch has been added in `docs/ZOMBIE_INVASION_QA_BUILD_AND_DELIVERY_TRACEABILITY_SPEC_V1.md`, covering QA-001..QA-018 and SHIP-001..SHIP-012.

The current matrix v1.2.0 now records:
- 42 mapped features (BASE 12 + QA 18 + SHIP 12).
- 190 features still requiring traceability review.
- 115 feature-specific acceptance criteria and 110 unique test case IDs.
- 95 proposed feature-to-feature dependency edges.
- A static topological check of the 232-node feature graph found no cycle in this revision.
- Java, Bedrock and parity remain `not_assessed` for all 232 features.
- All 232 implementation statuses remain `not_implemented_verified`; no runtime evidence was added.

The DAG check verifies only the recorded graph structure. It does not test generated code, Minecraft runtime behavior, target compatibility or actual builds. Dedicated-server and multiplayer test definitions remain future/conditional gates, not first-playable scope.
