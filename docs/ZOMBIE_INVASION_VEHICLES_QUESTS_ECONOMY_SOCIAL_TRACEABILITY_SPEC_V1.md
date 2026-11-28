# Zombie Invasion — Vehicles, Quests, Economy and Social Traceability Specification v1

**Status:** Feature-level design mapping; long-term and multiplayer scopes remain separately gated  
**Date:** 2026-11-28  
**Feature IDs:** VEH-001..VEH-014, QUEST-001..QUEST-012, ECON-001..ECON-012, SOC-001..SOC-010

## 1. Purpose and scope

This specification maps 48 transportation, quest/story, economy and social features to requirements, target mappings, acceptance criteria and test cases. It preserves the user's broad long-term requirements for vehicles, buses, trailers, convoys, research, radio, factions, trade and persistent settlements while keeping first-playable and multiplayer scope controlled.

Confirmed design directions include bicycle as the simplest entry vehicle, player-manufactured vehicles, modifiable vehicles, usable bus interiors, compact bicycle trailers, larger caravans for larger vehicles, and a broad transport network. Multiplayer, player-to-player trading, PvP/group sharing, moderation and server roles remain future/conditional until separately approved.

## 2. Shared ownership and economy rules

- Vehicle service owns vehicle identity, seats, movement, condition and cargo attachment; item/inventory owns cargo contents; power/fuel systems own energy quantities.
- Quest/story service owns objective state and branches; combat, NPC, world and inventory services emit committed events; rewards use atomic economy transactions.
- Economy owns currency/stock transactions and audit history; factions own relations/access; dialogue only reads these facts.
- Player-built claims and faction territories are separate ownership domains with explicit conflict rules.
- Java and Bedrock use separate runtime adapters and evidence. No multiplayer or cross-play claim is inferred from single-player.

## 3. Feature-level mapping

### VEH-001 — Vehicle base framework and ownership

**Requirement:** REQ-VEH-001  
**Purpose:** Define vehicle identity, type, owner, state, component slots, access and persistence.  
**Target mapping:** Separate Java/Bedrock vehicle adapters; shared vehicle specification and logical ownership.

**Acceptance criteria**
- AC-VEH-001-01: Every vehicle has a stable ID, owner/access policy, movement state and component manifest.
- AC-VEH-001-02: Spawn, storage, transfer and reload preserve one vehicle identity without duplication.

**Test cases**
- TC-VEH-001-01: TC-VEH-001-01 vehicle identity and ownership lifecycle
- TC-VEH-001-02: TC-VEH-001-02 vehicle duplicate/spawn replay prevention

**Prerequisite feature IDs:** BASE-007, ITEM-001, WORLD-001.

### VEH-002 — Ground vehicles: cars, trucks, motorcycles

**Requirement:** REQ-VEH-002  
**Purpose:** Define ground vehicle families and staged acquisition, manufacture, repair and modification.  
**Target mapping:** Target-native entities/controls; first entry vehicle is a bicycle, with cars/trucks/motorcycles as progression options.

**Acceptance criteria**
- AC-VEH-002-01: Each vehicle declares seats, speed/handling class, cargo, fuel/energy and repair requirements.
- AC-VEH-002-02: Vehicle roster is data-driven; first-slice availability is controlled by manifest and balance.

**Test cases**
- TC-VEH-002-01: TC-VEH-002-01 bicycle and ground vehicle capability profiles
- TC-VEH-002-02: TC-VEH-002-02 vehicle spawn/craft permission and persistence

**Prerequisite feature IDs:** VEH-001, ITEM-001, CRAFT-001.

### VEH-003 — Tracked vehicles and heavy transport

**Requirement:** REQ-VEH-003  
**Purpose:** Define optional tracked/heavy transport for late-game logistics and high-threat regions.  
**Target mapping:** Only supported target physics and interaction capabilities are used; advanced vehicles are later-stage.

**Acceptance criteria**
- AC-VEH-003-01: Heavy vehicle mass, terrain capability, fuel, cargo and repair needs are bounded and declared.
- AC-VEH-003-02: No heavy vehicle is included in first-slice output unless separately approved.

**Test cases**
- TC-VEH-003-01: TC-VEH-003-01 heavy vehicle capability and terrain constraints
- TC-VEH-003-02: TC-VEH-003-02 late-game scope and resource-cost gate

**Prerequisite feature IDs:** VEH-001.

### VEH-004 — Aircraft and helicopters

**Requirement:** REQ-VEH-004  
**Purpose:** Define aircraft/heli transport, landing, fuel, maintenance and risk systems as advanced transport.  
**Target mapping:** Target-specific flight simulation feasibility must be verified; scripted simplified handling may be used only if approved.

**Acceptance criteria**
- AC-VEH-004-01: Flight states, collision, fuel, landing zones and passenger capacity have explicit bounds.
- AC-VEH-004-02: Aircraft/heli remain long-term scope; no first-slice flight support is implied.

**Test cases**
- TC-VEH-004-01: TC-VEH-004-01 flight state and landing validation
- TC-VEH-004-02: TC-VEH-004-02 fuel and crash recovery bounds

**Prerequisite feature IDs:** VEH-001, WORLD-008.

### VEH-005 — Watercraft and submarines

**Requirement:** REQ-VEH-005  
**Purpose:** Define boats and water transport, with submarines as optional advanced content.  
**Target mapping:** Water movement and vehicle control are adapted to each edition's capabilities.

**Acceptance criteria**
- AC-VEH-005-01: Watercraft have buoyancy/movement, passenger/cargo, fuel and damage state contracts.
- AC-VEH-005-02: Watercraft routes and storage integrate with authoritative world water geography.

**Test cases**
- TC-VEH-005-01: TC-VEH-005-01 watercraft movement and passenger state
- TC-VEH-005-02: TC-VEH-005-02 water route and persistence validation

**Prerequisite feature IDs:** VEH-001, WORLD-005.

### VEH-006 — Seats, passengers, driver controls

**Requirement:** REQ-VEH-006  
**Purpose:** Define seat positions, driver permissions, passenger entry/exit and interior occupancy.  
**Target mapping:** Target-specific seat/ride APIs; shared seat ownership and safe exit rules.

**Acceptance criteria**
- AC-VEH-006-01: Only authorized actors occupy seats; driver control is exclusive and passengers cannot duplicate vehicle state.
- AC-VEH-006-02: Buses manufactured by the player have a usable interior/living-space layout, not merely an external shell.

**Test cases**
- TC-VEH-006-01: TC-VEH-006-01 seat occupancy and driver authority
- TC-VEH-006-02: TC-VEH-006-02 bus interior passenger/living-space interaction

**Prerequisite feature IDs:** VEH-001, ENT-004.

### VEH-007 — Fuel, energy, battery, refueling

**Requirement:** REQ-VEH-007  
**Purpose:** Connect vehicle fuel and batteries to finite fuel/energy storage and refueling networks.  
**Target mapping:** Target adapters expose the same logical fuel/charge accounting.

**Acceptance criteria**
- AC-VEH-007-01: Fuel/charge consumption and refueling are atomic and cannot create energy or exceed tank/battery capacity.
- AC-VEH-007-02: Vehicles can use declared energy types only; generators, storage and fuel stations retain their own ownership.

**Test cases**
- TC-VEH-007-01: TC-VEH-007-01 fuel/charge conservation and capacity
- TC-VEH-007-02: TC-VEH-007-02 refueling transaction and incompatible fuel rejection

**Prerequisite feature IDs:** CRAFT-005, ITEM-014.

### VEH-008 — Health, damage, repair, destruction

**Requirement:** REQ-VEH-008  
**Purpose:** Define vehicle health, component damage, breakdown, repair, recovery and destruction.  
**Target mapping:** Target-specific damage/physics implementation with shared condition states.

**Acceptance criteria**
- AC-VEH-008-01: Damage has source and component effects; repair consumes actual parts/materials and time where configured.
- AC-VEH-008-02: Destroyed vehicle recovery follows an explicit policy and cannot duplicate cargo or vehicle inventory.

**Test cases**
- TC-VEH-008-01: TC-VEH-008-01 vehicle damage and repair resource accounting
- TC-VEH-008-02: TC-VEH-008-02 destruction/recovery cargo preservation

**Prerequisite feature IDs:** VEH-001, ITEM-009.

### VEH-009 — Storage, cargo, towing, trailers

**Requirement:** REQ-VEH-009  
**Purpose:** Define vehicle inventories, cargo limits, hitching, towing and trailer attachment.  
**Target mapping:** Separate target inventory/attachment adapters with shared capacity and ownership rules.

**Acceptance criteria**
- AC-VEH-009-01: Cargo transfers are atomic and capacity-bounded; towing validates compatible hitch/weight limits.
- AC-VEH-009-02: A bicycle may tow a compact cargo/living trailer; full-size caravans are reserved for larger vehicle classes.

**Test cases**
- TC-VEH-009-01: TC-VEH-009-01 cargo transfer and capacity validation
- TC-VEH-009-02: TC-VEH-009-02 bicycle trailer and large caravan compatibility

**Prerequisite feature IDs:** VEH-001, ITEM-007, ITEM-013.

### VEH-010 — Physics, handling, collision, terrain response

**Requirement:** REQ-VEH-010  
**Purpose:** Define movement, acceleration, braking, turning, collision and terrain interaction.  
**Target mapping:** Use target-supported movement APIs and bounded approximations; do not assume identical physics engines.

**Acceptance criteria**
- AC-VEH-010-01: Vehicle movement respects collision and terrain; no clipping through protected or solid geometry.
- AC-VEH-010-02: Handling parameters are configurable and testable on declared reference hardware.

**Test cases**
- TC-VEH-010-01: TC-VEH-010-01 vehicle collision and terrain response
- TC-VEH-010-02: TC-VEH-010-02 speed/turning stability and world boundary

**Prerequisite feature IDs:** VEH-001, WORLD-003, STRUCT-006.

### VEH-011 — Weapons or utility modules, if permitted by project scope

**Requirement:** REQ-VEH-011  
**Purpose:** Define optional utility modules such as lights, storage, radios, winches or defensive modules; armed vehicle modules require separate approval.  
**Target mapping:** Target-native attachment and interaction constraints; optional modules do not assume unsupported APIs.

**Acceptance criteria**
- AC-VEH-011-01: Each module has explicit power, weight, permission and compatibility requirements.
- AC-VEH-011-02: Armed vehicle modules are not enabled by default; utility modules remain separately scoped.

**Test cases**
- TC-VEH-011-01: TC-VEH-011-01 module compatibility and power cost
- TC-VEH-011-02: TC-VEH-011-02 unapproved armed module blocked

**Prerequisite feature IDs:** VEH-001, COM-004.

### VEH-012 — Vehicle crafting, purchase, permissions, persistence

**Requirement:** REQ-VEH-012  
**Purpose:** Define factory/workshop production, salvage, purchase, ownership, permissions and persistent modifications.  
**Target mapping:** Shared manufacturing blueprint and ownership records; separate Java/Bedrock vehicle production components.

**Acceptance criteria**
- AC-VEH-012-01: Vehicle manufacturing consumes real materials, parts, labor/power and a valid factory/workshop stage.
- AC-VEH-012-02: Vehicle upgrades, ownership and modifications persist through save/reload and migration.

**Test cases**
- TC-VEH-012-01: TC-VEH-012-01 factory vehicle production input/output conservation
- TC-VEH-012-02: TC-VEH-012-02 ownership/upgrade persistence and permission checks

**Prerequisite feature IDs:** VEH-001, CRAFT-004, ITEM-009.

### VEH-013 — Multiplayer synchronization and anti-desync

**Requirement:** REQ-VEH-013  
**Purpose:** Define vehicle authority and synchronization for future multiplayer sessions.  
**Target mapping:** Multiplayer is deferred from first playable; Java and Bedrock network behavior requires independent validation.

**Acceptance criteria**
- AC-VEH-013-01: No multiplayer vehicle support claim is made from single-player testing.
- AC-VEH-013-02: When enabled later, vehicle ownership, passenger state, movement and cargo are server/world authoritative.

**Test cases**
- TC-VEH-013-01: TC-VEH-013-01 single-player scope excludes multiplayer claim
- TC-VEH-013-02: TC-VEH-013-02 future concurrent vehicle state synchronization

**Prerequisite feature IDs:** BASE-003, QA-012.

### VEH-014 — Machines, generators, power networks, automation

**Requirement:** REQ-VEH-014  
**Purpose:** Connect vehicle factories, pumps, charging stations and machines to the shared power/fuel infrastructure.  
**Target mapping:** Target-specific machine/block/network adapters; shared energy and production accounting.

**Acceptance criteria**
- AC-VEH-014-01: Machines consume actual power/fuel and expose bounded throughput, storage and fault state.
- AC-VEH-014-02: Automation cannot create resources or bypass power/water/fuel capacity and ownership rules.

**Test cases**
- TC-VEH-014-01: TC-VEH-014-01 machine energy and production conservation
- TC-VEH-014-02: TC-VEH-014-02 automation outage and restart consistency

**Prerequisite feature IDs:** ITEM-013, CRAFT-003, CRAFT-005.

### QUEST-001 — Quest data model and objectives

**Requirement:** REQ-QUEST-001  
**Purpose:** Define stable quest identity, objectives, states, evidence, prerequisites and completion transactions.  
**Target mapping:** Shared quest contract with Java/Bedrock event and persistence adapters.

**Acceptance criteria**
- AC-QUEST-001-01: Every objective has stable ID, trigger, evidence, state transition and completion policy.
- AC-QUEST-001-02: Quest completion/reward is idempotent and bound to actual committed world/game events.

**Test cases**
- TC-QUEST-001-01: TC-QUEST-001-01 quest state machine and objective evidence
- TC-QUEST-001-02: TC-QUEST-001-02 repeated completion/reward prevention

**Prerequisite feature IDs:** BASE-007, PLY-014.

### QUEST-002 — Main storyline and chapters

**Requirement:** REQ-QUEST-002  
**Purpose:** Define optional campaign chapters and story progression without forcing a single ending.  
**Target mapping:** Shared story state and branch identity; target-specific presentation and persistence.

**Acceptance criteria**
- AC-QUEST-002-01: Story chapters are optional/sandbox-compatible and do not reset the persistent world by default.
- AC-QUEST-002-02: The proposed three-night extraction scenario is not treated as approved campaign structure.

**Test cases**
- TC-QUEST-002-01: TC-QUEST-002-01 chapter progression and optional branch
- TC-QUEST-002-02: TC-QUEST-002-02 sandbox continuation after story milestone

**Prerequisite feature IDs:** QUEST-001, WORLD-001.

### QUEST-003 — Side quests and repeatable tasks

**Requirement:** REQ-QUEST-003  
**Purpose:** Define optional side quests, survivor requests, settlement projects and repeatable objectives.  
**Target mapping:** Shared quest templates and target-native trigger/UI adapters.

**Acceptance criteria**
- AC-QUEST-003-01: Repeatable tasks have cooldown/eligibility and cannot grant unlimited resources.
- AC-QUEST-003-02: Side quests respect NPC availability, faction knowledge and actual world state.

**Test cases**
- TC-QUEST-003-01: TC-QUEST-003-01 repeatable task cooldown and reward cap
- TC-QUEST-003-02: TC-QUEST-003-02 NPC task availability and state validation

**Prerequisite feature IDs:** QUEST-001, ENT-014.

### QUEST-004 — Dialogue, choices, branching outcomes

**Requirement:** REQ-QUEST-004  
**Purpose:** Connect dialogue choices to quest/faction/reputation state and persistent consequences.  
**Target mapping:** Dialogue UI differs per target; shared choice IDs and branch outcomes.

**Acceptance criteria**
- AC-QUEST-004-01: Choices are validated against actual prerequisites and produce one committed outcome.
- AC-QUEST-004-02: NPC dialogue cannot invent discoveries, injuries, items or completed actions.

**Test cases**
- TC-QUEST-004-01: TC-QUEST-004-01 choice prerequisites and branch persistence
- TC-QUEST-004-02: TC-QUEST-004-02 dialogue facts match authoritative game state

**Prerequisite feature IDs:** ENT-014.

### QUEST-005 — Collect, craft, explore, defeat, escort objectives

**Requirement:** REQ-QUEST-005  
**Purpose:** Define objective adapters for inventory, crafting, POI discovery, combat and NPC escort events.  
**Target mapping:** Shared objective semantics with target-specific event sources.

**Acceptance criteria**
- AC-QUEST-005-01: Objectives complete only from committed events and count only eligible items/actors/locations.
- AC-QUEST-005-02: Repeated event delivery does not duplicate objective progress or reward.

**Test cases**
- TC-QUEST-005-01: TC-QUEST-005-01 objective event evidence across gameplay systems
- TC-QUEST-005-02: TC-QUEST-005-02 duplicate event cannot double progress

**Prerequisite feature IDs:** QUEST-001, ITEM-001, ENT-003.

### QUEST-006 — Quest prerequisites and progression flags

**Requirement:** REQ-QUEST-006  
**Purpose:** Define quest dependency graphs, flags, optional branches and soft-lock safeguards.  
**Target mapping:** Shared graph with target-specific storage and trigger adapters.

**Acceptance criteria**
- AC-QUEST-006-01: Hard prerequisite cycles are rejected and critical paths have alternate route or explicit optionality.
- AC-QUEST-006-02: Quest flags migrate safely and cannot be set by untrusted presentation/UI state.

**Test cases**
- TC-QUEST-006-01: TC-QUEST-006-01 quest dependency cycle and soft-lock detection
- TC-QUEST-006-02: TC-QUEST-006-02 flag persistence and authorization

**Prerequisite feature IDs:** QUEST-001, PLY-013.

### QUEST-007 — Rewards, reputation, unlocks

**Requirement:** REQ-QUEST-007  
**Purpose:** Define reward bundles, reputation changes, unlocks and one-time/recurring reward policy.  
**Target mapping:** Shared reward transaction with target-specific inventory and faction adapters.

**Acceptance criteria**
- AC-QUEST-007-01: Rewards commit atomically with quest completion and cannot duplicate on replay.
- AC-QUEST-007-02: Reward values respect economy scarcity and progression ownership; no free currency/item grant.

**Test cases**
- TC-QUEST-007-01: TC-QUEST-007-01 atomic reward/reputation transaction
- TC-QUEST-007-02: TC-QUEST-007-02 quest reward replay and economy conservation

**Prerequisite feature IDs:** QUEST-001, ECON-001, SOC-003.

### QUEST-008 — Quest journal, tracking, map guidance

**Requirement:** REQ-QUEST-008  
**Purpose:** Provide journal, objective tracking, map markers and contextual hints.  
**Target mapping:** Java/Bedrock UI implementations may differ but read shared quest/POI state.

**Acceptance criteria**
- AC-QUEST-008-01: Journal reflects authoritative objective state and never reveals undiscovered locations without valid intel.
- AC-QUEST-008-02: Tracking preferences persist and can be disabled without blocking quest completion.

**Test cases**
- TC-QUEST-008-01: TC-QUEST-008-01 journal and map marker consistency
- TC-QUEST-008-02: TC-QUEST-008-02 undiscovered POI information boundary

**Prerequisite feature IDs:** QUEST-001, STRUCT-010.

### QUEST-009 — Timed missions and world events

**Requirement:** REQ-QUEST-009  
**Purpose:** Define time windows, deadlines, warning cues, failure and rescheduling behavior.  
**Target mapping:** Shared world clock; target adapters present warnings and event state.

**Acceptance criteria**
- AC-QUEST-009-01: Deadlines use the authoritative world clock and pause/sleep behavior is explicitly configured.
- AC-QUEST-009-02: Missed timed content follows a documented fail/retry/expire policy without deleting unrelated progress.

**Test cases**
- TC-QUEST-009-01: TC-QUEST-009-01 deadline and clock synchronization
- TC-QUEST-009-02: TC-QUEST-009-02 missed event recovery and persistence

**Prerequisite feature IDs:** WORLD-010, QUEST-001.

### QUEST-010 — Dynamic events, waves, invasions, emergencies

**Requirement:** REQ-QUEST-010  
**Purpose:** Connect quests to Encounter Director, horde, siege, fire, disease and rescue events.  
**Target mapping:** Target-specific event triggers with shared encounter budgets and world-state contracts.

**Acceptance criteria**
- AC-QUEST-010-01: Event director owns spawn/phase scheduling; quest system observes events and records objectives only.
- AC-QUEST-010-02: Dynamic events cannot spawn unlimited zombies or create duplicate reward/quest completion events.

**Test cases**
- TC-QUEST-010-01: TC-QUEST-010-01 encounter budget and quest event integration
- TC-QUEST-010-02: TC-QUEST-010-02 emergency event reset/idempotency

**Prerequisite feature IDs:** ENT-003, ENT-012, WORLD-009.

### QUEST-011 — Narrative triggers and world-state changes

**Requirement:** REQ-QUEST-011  
**Purpose:** Define narrative state changes, radio discoveries, research milestones and persistent consequences.  
**Target mapping:** Shared narrative flags and target-specific triggers/presentation.

**Acceptance criteria**
- AC-QUEST-011-01: Narrative changes are triggered by validated discoveries and committed events, not dialogue alone.
- AC-QUEST-011-02: World changes are revisioned and preserve player-built/discovered state.

**Test cases**
- TC-QUEST-011-01: TC-QUEST-011-01 radio/research narrative trigger evidence
- TC-QUEST-011-02: TC-QUEST-011-02 narrative world-state migration and persistence

**Prerequisite feature IDs:** QUEST-001, WORLD-010.

### QUEST-012 — Multiplayer party/shared quest rules

**Requirement:** REQ-QUEST-012  
**Purpose:** Define future party quest ownership, shared objectives, contribution and reward splitting.  
**Target mapping:** Multiplayer is deferred from first playable; party behavior requires separately approved profiles.

**Acceptance criteria**
- AC-QUEST-012-01: No shared quest completion or reward sharing is enabled in the single-player milestone.
- AC-QUEST-012-02: When multiplayer is enabled, party membership, contribution and reward rules are authoritative and auditable.

**Test cases**
- TC-QUEST-012-01: TC-QUEST-012-01 single-player profile excludes party quest behavior
- TC-QUEST-012-02: TC-QUEST-012-02 future shared objective/reward idempotency

**Prerequisite feature IDs:** BASE-003, QUEST-001.

### ECON-001 — Currency types and balances

**Requirement:** REQ-ECON-001  
**Purpose:** Define currency/item barter types, balances, ownership and transaction invariants.  
**Target mapping:** Shared logical currency records; target-specific UI and persistent storage adapters.

**Acceptance criteria**
- AC-ECON-001-01: Balances cannot become negative and every change has a committed source/sink transaction.
- AC-ECON-001-02: No real-money economy is assumed for the in-game zombie world; currency types are game design data.

**Test cases**
- TC-ECON-001-01: TC-ECON-001-01 balance invariants and transaction ledger
- TC-ECON-001-02: TC-ECON-001-02 unauthorized or duplicate balance change rejected

**Prerequisite feature IDs:** ITEM-008, BASE-007.

### ECON-002 — NPC shops and price lists

**Requirement:** REQ-ECON-002  
**Purpose:** Define survivor/faction shops, stock, prices, services and trading hours.  
**Target mapping:** Shared stock/price contract with target-specific NPC interaction.

**Acceptance criteria**
- AC-ECON-002-01: A purchase validates stock, payment, capacity and access atomically.
- AC-ECON-002-02: Shop stock and prices update from real supply/demand events; no free restock without source.

**Test cases**
- TC-ECON-002-01: TC-ECON-002-01 atomic NPC shop purchase
- TC-ECON-002-02: TC-ECON-002-02 stock and price persistence

**Prerequisite feature IDs:** ECON-001, ENT-014, ITEM-008.

### ECON-003 — Player-to-player trading

**Requirement:** REQ-ECON-003  
**Purpose:** Define future player-to-player trade offers, confirmation and item escrow.  
**Target mapping:** Deferred with multiplayer; no player trade UI in first playable.

**Acceptance criteria**
- AC-ECON-003-01: Single-player build exposes no player-to-player trade route.
- AC-ECON-003-02: Future trade requires explicit confirmation, atomic transfer and rollback on disconnect/failure.

**Test cases**
- TC-ECON-003-01: TC-ECON-003-01 single-player profile blocks player trade
- TC-ECON-003-02: TC-ECON-003-02 future trade escrow and disconnect rollback

**Prerequisite feature IDs:** BASE-003, ECON-001.

### ECON-004 — Buy/sell orders and market listings

**Requirement:** REQ-ECON-004  
**Purpose:** Define market listings, buy/sell orders, expiration and ownership.  
**Target mapping:** Long-term regional market simulation; first slice may use authored NPC shop stock only.

**Acceptance criteria**
- AC-ECON-004-01: Listings reserve real stock/currency and cannot oversell or double-fill.
- AC-ECON-004-02: Expired/cancelled orders release reservations exactly once.

**Test cases**
- TC-ECON-004-01: TC-ECON-004-01 order reservation and fill accounting
- TC-ECON-004-02: TC-ECON-004-02 cancellation/expiry release

**Prerequisite feature IDs:** ECON-001, ECON-002.

### ECON-005 — Dynamic pricing and supply/demand

**Requirement:** REQ-ECON-005  
**Purpose:** Define price curves based on regional stock, scarcity, routes, faction access and demand.  
**Target mapping:** Shared deterministic pricing model with target display adapters.

**Acceptance criteria**
- AC-ECON-005-01: Prices remain within configured bounds and derive from recorded stock/flow inputs.
- AC-ECON-005-02: A single player cannot create infinite buy/sell arbitrage loops or mutate regional stock without transactions.

**Test cases**
- TC-ECON-005-01: TC-ECON-005-01 scarcity price response and bounds
- TC-ECON-005-02: TC-ECON-005-02 arbitrage loop and stock conservation

**Prerequisite feature IDs:** ECON-001, WORLD-010.

### ECON-006 — Loot and reward economy sinks/sources

**Requirement:** REQ-ECON-006  
**Purpose:** Track loot, quest rewards, crafting consumption, repairs and trade as economy sources/sinks.  
**Target mapping:** Shared resource accounting linked to loot and inventory ownership.

**Acceptance criteria**
- AC-ECON-006-01: Every item/currency source and sink is classified; total flows reconcile across transactions.
- AC-ECON-006-02: Loot/reward changes cannot duplicate resources across death, reset, migration or quest replay.

**Test cases**
- TC-ECON-006-01: TC-ECON-006-01 resource source/sink reconciliation
- TC-ECON-006-02: TC-ECON-006-02 reward/loot duplication prevention

**Prerequisite feature IDs:** CRAFT-010, ITEM-001.

### ECON-007 — Land, claims, property, ownership

**Requirement:** REQ-ECON-007  
**Purpose:** Define property claims, abandoned building ownership, settlement plots and permissions.  
**Target mapping:** Shared logical claim state with target-specific region/block enforcement.

**Acceptance criteria**
- AC-ECON-007-01: Claim creation checks eligibility, boundaries and conflicts; one area cannot have conflicting owners.
- AC-ECON-007-02: Player can claim/restore abandoned buildings and build freely within declared rules without overriding protected content.

**Test cases**
- TC-ECON-007-01: TC-ECON-007-01 claim conflict and ownership validation
- TC-ECON-007-02: TC-ECON-007-02 claimed building permissions and persistence

**Prerequisite feature IDs:** WORLD-012, STRUCT-001.

### ECON-008 — Rent, upkeep, taxes, profit sharing

**Requirement:** REQ-ECON-008  
**Purpose:** Define optional settlement upkeep, shared costs and revenue allocation.  
**Target mapping:** Long-term economy only; no rent/tax burden is imposed in first playable unless approved.

**Acceptance criteria**
- AC-ECON-008-01: Upkeep costs are explicit, bounded and shown before commitment; default first-slice policy is no hidden tax.
- AC-ECON-008-02: Profit sharing requires declared ownership shares and atomic settlement.

**Test cases**
- TC-ECON-008-01: TC-ECON-008-01 upkeep preview and bounded payment
- TC-ECON-008-02: TC-ECON-008-02 shared profit accounting

**Prerequisite feature IDs:** ECON-007, ECON-001.

### ECON-009 — Factions, reputation, licenses

**Requirement:** REQ-ECON-009  
**Purpose:** Integrate faction access, reputation and licenses with trade, quests and settlement services.  
**Target mapping:** Shared faction/reputation identity with target-native presentation.

**Acceptance criteria**
- AC-ECON-009-01: Access changes only from committed faction/quest events; dialogue cannot fabricate reputation.
- AC-ECON-009-02: License unlocks and penalties persist and can be audited; no circular reputation reward loop.

**Test cases**
- TC-ECON-009-01: TC-ECON-009-01 faction access and reputation consistency
- TC-ECON-009-02: TC-ECON-009-02 license unlock and penalty audit

**Prerequisite feature IDs:** SOC-002, SOC-003.

### ECON-010 — Transaction history, audit trail, anti-duplication

**Requirement:** REQ-ECON-010  
**Purpose:** Maintain immutable transaction records for currency, item, land, trade and service changes.  
**Target mapping:** Shared transaction semantics with target-specific persistence.

**Acceptance criteria**
- AC-ECON-010-01: Every transaction has unique ID, participants, inputs, outputs, status and idempotency key.
- AC-ECON-010-02: Replay, concurrent requests and partial failures cannot duplicate or lose resources.

**Test cases**
- TC-ECON-010-01: TC-ECON-010-01 transaction replay/idempotency
- TC-ECON-010-02: TC-ECON-010-02 rollback and audit trail integrity

**Prerequisite feature IDs:** ECON-001, QA-015.

### ECON-011 — Permissions, escrow, trade confirmation

**Requirement:** REQ-ECON-011  
**Purpose:** Define permissions and escrow for risky/high-value trade or ownership changes.  
**Target mapping:** Single-player NPC transactions use confirmation where destructive; player escrow is future multiplayer scope.

**Acceptance criteria**
- AC-ECON-011-01: Trade and claim changes validate actor permissions and confirmation before commit.
- AC-ECON-011-02: Escrow releases or refunds exactly once; unauthorized actions fail without partial state.

**Test cases**
- TC-ECON-011-01: TC-ECON-011-01 permission and confirmation gate
- TC-ECON-011-02: TC-ECON-011-02 escrow timeout and refund idempotency

**Prerequisite feature IDs:** ECON-001, BASE-010.

### ECON-012 — Offline player and market consistency

**Requirement:** REQ-ECON-012  
**Purpose:** Define how persistent stock, ownership and trade state behave while players/NPCs are offline or regions inactive.  
**Target mapping:** Distant simulation uses aggregated elapsed-time updates; no remote chunk force-load.

**Acceptance criteria**
- AC-ECON-012-01: Offline stock/need/market updates conserve resources and use the canonical world clock.
- AC-ECON-012-02: Region activation does not double-apply offline production, consumption or transactions.

**Test cases**
- TC-ECON-012-01: TC-ECON-012-01 offline time-step resource reconciliation
- TC-ECON-012-02: TC-ECON-012-02 region activation idempotency

**Prerequisite feature IDs:** ECON-001, BASE-009, QA-013.

### SOC-001 — Teams, parties, groups

**Requirement:** REQ-SOC-001  
**Purpose:** Define player/NPC group identity, membership, roles and group lifecycle for later multiplayer/settlement scope.  
**Target mapping:** Single-player survivor groups and NPC factions can exist; player parties are future multiplayer scope.

**Acceptance criteria**
- AC-SOC-001-01: Group identity and membership have stable IDs, owner and permission rules.
- AC-SOC-001-02: First-slice single-player does not expose unapproved multiplayer party features.

**Test cases**
- TC-SOC-001-01: TC-SOC-001-01 group membership and identity persistence
- TC-SOC-001-02: TC-SOC-001-02 single-player scope enforcement

**Prerequisite feature IDs:** BASE-003, ENT-004.

### SOC-002 — Factions, alliances, rivalries

**Requirement:** REQ-SOC-002  
**Purpose:** Define persistent survivor factions, diplomacy, alliances, hostility and territorial relations.  
**Target mapping:** Shared faction state with target-specific UI and persistence.

**Acceptance criteria**
- AC-SOC-002-01: Faction relations change only through explicit world/quest/trade events and are bounded/auditable.
- AC-SOC-002-02: Faction knowledge and hostility cannot leak undiscovered player/world information.

**Test cases**
- TC-SOC-002-01: TC-SOC-002-01 faction relation transition and persistence
- TC-SOC-002-02: TC-SOC-002-02 knowledge boundary and unauthorized relation change

**Prerequisite feature IDs:** SOC-001, ENT-004.

### SOC-003 — Reputation and relationship scores

**Requirement:** REQ-SOC-003  
**Purpose:** Define player-NPC/faction relationship scores, trust, fear, gratitude and consequences.  
**Target mapping:** Shared reputation semantics with target-specific dialogue/UI.

**Acceptance criteria**
- AC-SOC-003-01: Score changes are tied to committed events with caps and decay rules.
- AC-SOC-003-02: Dialogue reflects stored relationship state and cannot modify reputation by itself.

**Test cases**
- TC-SOC-003-01: TC-SOC-003-01 relationship score event accounting
- TC-SOC-003-02: TC-SOC-003-02 dialogue reads but does not mutate reputation

**Prerequisite feature IDs:** SOC-002, ENT-014.

### SOC-004 — Ranks, roles, permissions

**Requirement:** REQ-SOC-004  
**Purpose:** Define ranks and roles for future groups/servers and NPC settlement responsibilities.  
**Target mapping:** First-slice NPC professions remain separate from multiplayer admin roles; server roles are later scope.

**Acceptance criteria**
- AC-SOC-004-01: Permission checks are server/world authoritative and follow least privilege.
- AC-SOC-004-02: Role changes are audited and cannot grant privileged commands to untrusted actors.

**Test cases**
- TC-SOC-004-01: TC-SOC-004-01 role permission matrix and least privilege
- TC-SOC-004-02: TC-SOC-004-02 unauthorized role escalation blocked

**Prerequisite feature IDs:** SOC-001, BASE-010.

### SOC-005 — Chat channels and communication

**Requirement:** REQ-SOC-005  
**Purpose:** Define future local, group, faction and server communication channels.  
**Target mapping:** Single-player radio/dialogue is in scope; multiplayer chat channels are deferred.

**Acceptance criteria**
- AC-SOC-005-01: Communication channel visibility follows membership and discovery rules.
- AC-SOC-005-02: No private/faction information is leaked to unauthorized recipients.

**Test cases**
- TC-SOC-005-01: TC-SOC-005-01 single-player radio channel scope
- TC-SOC-005-02: TC-SOC-005-02 future channel access control

**Prerequisite feature IDs:** SOC-001, BASE-010.

### SOC-006 — Friend, invite, block, and ignore lists

**Requirement:** REQ-SOC-006  
**Purpose:** Define future friend/invite/block controls for connected multiplayer/community experiences.  
**Target mapping:** Not required for first-slice single-player; platform/account integration is a separate product decision.

**Acceptance criteria**
- AC-SOC-006-01: No account/social connector is assumed in the mod itself.
- AC-SOC-006-02: Future lists are privacy-aware, permissioned and synchronized only with explicit consent.

**Test cases**
- TC-SOC-006-01: TC-SOC-006-01 first-slice excludes account friend integration
- TC-SOC-006-02: TC-SOC-006-02 future block/invite privacy and access rules

**Prerequisite feature IDs:** SOC-001, BASE-003.

### SOC-007 — Shared bases, claims, access lists

**Requirement:** REQ-SOC-007  
**Purpose:** Define co-owned settlement/base access, storage permissions and group construction rights.  
**Target mapping:** Single-player NPC settlement permissions are supported by design; multi-player shared base is later scope.

**Acceptance criteria**
- AC-SOC-007-01: Claim/access lists distinguish owner, trusted, worker and visitor permissions.
- AC-SOC-007-02: Storage, doors, defenses and automation enforce the same access policy across target adapters.

**Test cases**
- TC-SOC-007-01: TC-SOC-007-01 base claim and role permission enforcement
- TC-SOC-007-02: TC-SOC-007-02 unauthorized storage/automation access blocked

**Prerequisite feature IDs:** SOC-001, STRUCT-001, WORLD-012.

### SOC-008 — Group objectives and rewards

**Requirement:** REQ-SOC-008  
**Purpose:** Define future shared goals, contribution tracking and reward distribution.  
**Target mapping:** First-slice quests are solo; shared party objectives are deferred.

**Acceptance criteria**
- AC-SOC-008-01: No shared group reward behavior is enabled in first-slice single-player.
- AC-SOC-008-02: Future rewards are contribution-aware, idempotent and protected against duplicate claim.

**Test cases**
- TC-SOC-008-01: TC-SOC-008-01 solo objective behavior in first slice
- TC-SOC-008-02: TC-SOC-008-02 future shared reward split and replay protection

**Prerequisite feature IDs:** SOC-001, QUEST-001.

### SOC-009 — Faction conflict and territory rules

**Requirement:** REQ-SOC-009  
**Purpose:** Define faction territory, control, conflict escalation, diplomacy and settlement boundaries.  
**Target mapping:** Shared faction/region contract with target-specific enforcement.

**Acceptance criteria**
- AC-SOC-009-01: Territory changes require explicit events and cannot silently overwrite player claims.
- AC-SOC-009-02: Conflict/siege rules respect protected zones, population and encounter budgets.

**Test cases**
- TC-SOC-009-01: TC-SOC-009-01 territory ownership and conflict transition
- TC-SOC-009-02: TC-SOC-009-02 protected claim and siege budget enforcement

**Prerequisite feature IDs:** SOC-002, SOC-007, WORLD-012.

### SOC-010 — Moderation, reporting, sanctions

**Requirement:** REQ-SOC-010  
**Purpose:** Define moderation/reporting/sanctions for future multiplayer and community environments.  
**Target mapping:** Not required for offline single-player gameplay; server/community policy is separate.

**Acceptance criteria**
- AC-SOC-010-01: No moderation infrastructure is falsely presented as active in a local mod.
- AC-SOC-010-02: Future moderation actions are permissioned, logged, appealable and scoped to the correct server/community.

**Test cases**
- TC-SOC-010-01: TC-SOC-010-01 single-player build has no misleading moderation claim
- TC-SOC-010-02: TC-SOC-010-02 future moderation audit and permission check

**Prerequisite feature IDs:** BASE-003, BASE-012, QA-015.

## 4. Supporting design references

- `docs/ZOMBIE_INVASION_EXPANDED_TRANSPORT_NETWORK_DESIGN_V1.md` — convoys, trains, boats, helicopters and logistics.
- `docs/ZOMBIE_INVASION_NPC_DIALOGUE_3D_WEAPONS_AND_VEHICLE_MANUFACTURING_DESIGN_V1.md` — bicycle, buses, trailers, factories and vehicle modification.
- `docs/ZOMBIE_INVASION_RADIO_RESEARCH_AND_STORY_DESIGN_V1.md` — radio, research, story and quest architecture.
- `docs/ZOMBIE_INVASION_CHARACTER_PROGRESSION_AND_ECONOMY_DESIGN_V1.md` — skills, scarcity, trade and rewards.
- `docs/ZOMBIE_INVASION_SURVIVOR_NPC_FACTIONS_AND_SETTLEMENT_DESIGN_V1.md` — recruitment, professions, factions, settlement and trading.
- `docs/ZOMBIE_INVASION_MULTIPLAYER_COOPERATION_AND_SERVER_DESIGN_V1.md` — future co-op/server design proposal.

## 5. First-playable and deferred boundaries

- The first playable remains single-player. Vehicle types beyond the approved entry/progression design must be selected in the manifest; a full vehicle catalogue is not assumed for the first build.
- NPC interaction, survivor recruitment and basic world-state quests may be selected for a later vertical slice; full faction simulation and regional economy are not automatic first-slice requirements.
- Player-to-player trade, party quests, multiplayer vehicle synchronization, friend lists, server chat, PvP, moderation and public server features are deferred.
- Currency model, price curves, upkeep/taxes, market order books and offline regional simulation rates remain open balance/design decisions.
- The three-night extraction scenario and specific campaign ending are not approved by this mapping.

## 6. Implementation boundary

These 48 features are mapped for design traceability only. They remain `not_implemented_verified`; target coverage and parity remain unassessed until Java and Bedrock source, builds, runtime sessions and evidence exist.
