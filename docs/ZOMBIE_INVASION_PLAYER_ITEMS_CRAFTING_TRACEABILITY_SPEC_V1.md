# Zombie Invasion — Player, Items and Crafting Traceability Specification v1

**Status:** Detailed design mapping; several balance and first-slice decisions remain open  
**Date:** 2026-11-28  
**Feature IDs:** PLY-001..PLY-014, ITEM-001..ITEM-016, CRAFT-001..CRAFT-010  
**Primary supporting designs:** player journey, injury/prosthetics, inventory/loot, combat/weapons, crafting/workstation progression and crafting engine specifications

## 1. Purpose and design boundaries

This document maps 40 player, item/equipment and crafting features to requirements, target behavior, acceptance criteria and test cases. It links the broad catalog to the Zombie Invasion-specific design documents. It does not imply that the features are all part of the first playable slice or that any code/tests exist.

Confirmed requirements carried into this mapping include broad food/drink and thirst systems, varied backpacks, melee plus firearms, finite ammunition, weapon noise and durability, injuries including fractures and prosthetics, broad crafting, and the vanilla Crafting Table as the first stage. Death/restart policy, encumbrance, exact item rosters, recipe values and some character customization remain open.

Java 26.3 + Fabric and Bedrock 26.60 + stable Script API 2.11.0 are separate implementation targets. Experimental Bedrock APIs remain disabled.

## 2. Cross-cutting contracts

- One canonical logical ID per player attribute, item, block, recipe, station, effect and progression unlock.
- Every item/recipe transaction is atomic: reserve inputs, validate capacity/permissions, commit once or roll back.
- Player state, item state, world state and progression have explicit owners; UI and dialogue only display authoritative state.
- Food, water, medicine, ammunition, fuel and crafting materials are finite resources with explicit sources and sinks.
- Save/load and migration preserve player inventory, backpack contents, injuries and progression according to approved policy.
- Java and Bedrock share logical outcomes, not binary code or assumed API parity.
- First-slice applicability is set in the approved manifest; broad design scope does not automatically expand the first playable.

## 3. Feature-level mapping

### PLY-001 — Player attributes and attribute modifiers

**Requirement:** REQ-PLY-001  
**Purpose:** Define canonical player attributes and bounded modifiers with one authoritative owner per attribute.  
**Target mapping:** Java attributes use Fabric/Minecraft-native attributes where suitable; Bedrock adapters use supported stable script state and effects.

**Acceptance criteria**
- AC-PLY-001-01: Attribute IDs, base values, modifier sources and stacking rules are explicit; invalid or duplicate modifiers are rejected.
- AC-PLY-001-02: All modifiers have source, duration/persistence and removal rules; reload cannot duplicate bonuses.

**Test cases**
- TC-PLY-001-01: TC-PLY-001-01 attribute registry and modifier stacking
- TC-PLY-001-02: TC-PLY-001-02 duplicate modifier and invalid range rejection

**Prerequisite feature IDs:** BASE-007, BASE-008.

### PLY-002 — Health, absorption, regeneration, damage resistance

**Requirement:** REQ-PLY-002  
**Purpose:** Define player health state, healing, absorption, resistance and damage integration with combat/injury.  
**Target mapping:** Both editions map shared health outcomes to their native runtime while retaining the same gameplay intent.

**Acceptance criteria**
- AC-PLY-002-01: Damage and healing are applied once through an authoritative damage contract; resistance and absorption order is deterministic.
- AC-PLY-002-02: Healing cannot exceed defined caps or bypass severe injuries; state persists as specified.

**Test cases**
- TC-PLY-002-01: TC-PLY-002-01 damage/healing and resistance ordering
- TC-PLY-002-02: TC-PLY-002-02 reload does not duplicate health modifiers

**Prerequisite feature IDs:** BASE-009.

### PLY-003 — Stamina/energy and recovery

**Requirement:** REQ-PLY-003  
**Purpose:** Model exertion and recovery for sprinting, combat, carrying and strenuous actions.  
**Target mapping:** Target adapters may differ in UI/API implementation but expose the same stamina rules and thresholds.

**Acceptance criteria**
- AC-PLY-003-01: Actions consume configured stamina once; recovery obeys rest, movement and injury conditions.
- AC-PLY-003-02: Zero stamina causes defined bounded penalties and cannot create infinite action loops.

**Test cases**
- TC-PLY-003-01: TC-PLY-003-01 action drain and recovery boundaries
- TC-PLY-003-02: TC-PLY-003-02 repeated action events do not double-drain or refill

**Prerequisite feature IDs:** PLY-001, PLY-002.

### PLY-004 — Hunger, thirst, temperature, fatigue, hygiene

**Requirement:** REQ-PLY-004  
**Purpose:** Define survival needs and their effects using the shared world clock and resource systems.  
**Target mapping:** Both targets expose equivalent needs; water/food interactions must use real inventory items and water quality.

**Acceptance criteria**
- AC-PLY-004-01: Food and drink consumption changes the correct need state once; dehydration and hunger thresholds have documented warning/effect stages.
- AC-PLY-004-02: Temperature, fatigue and hygiene remain independently configurable; first-slice inclusion is controlled by approved manifest scope.

**Test cases**
- TC-PLY-004-01: TC-PLY-004-01 food and drink need-state transitions
- TC-PLY-004-02: TC-PLY-004-02 time-based need decay and recovery consistency

**Prerequisite feature IDs:** PLY-002, PLY-003, ITEM-003.

### PLY-005 — Movement: sprint, crouch, crawl, climb, slide, dodge

**Requirement:** REQ-PLY-005  
**Purpose:** Define movement actions, costs, state restrictions and injury interactions.  
**Target mapping:** Use supported movement controls per edition; unsupported movement is reported as adapted/limited rather than faked.

**Acceptance criteria**
- AC-PLY-005-01: Movement state transitions respect stamina, collision, terrain and injury constraints.
- AC-PLY-005-02: Movement actions cannot bypass collision or allow invulnerable animation windows unless explicitly designed.

**Test cases**
- TC-PLY-005-01: TC-PLY-005-01 movement action state and collision
- TC-PLY-005-02: TC-PLY-005-02 injury and stamina restrictions on movement

**Prerequisite feature IDs:** PLY-001, PLY-003.

### PLY-006 — Jumping, falling, swimming, diving, drowning

**Requirement:** REQ-PLY-006  
**Purpose:** Integrate vertical movement, water movement, breath and fall damage with survival health.  
**Target mapping:** Java and Bedrock use target-native movement hooks and equivalent outcome rules.

**Acceptance criteria**
- AC-PLY-006-01: Fall and drowning damage are applied once with defined thresholds; swimming/diving respect movement and breath constraints.
- AC-PLY-006-02: Water and environmental state are read from authoritative world conditions, not duplicated player-only approximations.

**Test cases**
- TC-PLY-006-01: TC-PLY-006-01 fall and drowning threshold behavior
- TC-PLY-006-02: TC-PLY-006-02 water movement and breath persistence

**Prerequisite feature IDs:** PLY-002, PLY-003.

### PLY-007 — Carry weight, inventory capacity, encumbrance

**Requirement:** REQ-PLY-007  
**Purpose:** Define optional capacity/weight rules while preserving the confirmed backpack variety requirement.  
**Target mapping:** Shared item mass/capacity semantics; target UI may differ. Weight penalties remain disabled until explicitly approved.

**Acceptance criteria**
- AC-PLY-007-01: Backpack capacity and item storage are deterministic; nested backpacks are rejected if the approved design retains that safeguard.
- AC-PLY-007-02: No weight/encumbrance rule is silently enabled; capacity changes cannot delete or duplicate stored items.

**Test cases**
- TC-PLY-007-01: TC-PLY-007-01 backpack capacity and nested-container safeguards
- TC-PLY-007-02: TC-PLY-007-02 capacity change preserves or safely rejects contents

**Prerequisite feature IDs:** ITEM-001, ITEM-007.

### PLY-008 — Skills, levels, experience, skill trees

**Requirement:** REQ-PLY-008  
**Purpose:** Define multi-track progression and skill effects tied to valid actions and unlocks.  
**Target mapping:** Both editions share progression IDs and thresholds; target-specific UI and storage are adapters.

**Acceptance criteria**
- AC-PLY-008-01: Experience is awarded only from committed gameplay events and cannot be duplicated by replay.
- AC-PLY-008-02: Skills improve eligible actions but never bypass required tools, stations, materials, injuries or permissions.

**Test cases**
- TC-PLY-008-01: TC-PLY-008-01 idempotent experience award and skill unlock
- TC-PLY-008-02: TC-PLY-008-02 skill modifiers respect prerequisite and cap rules

**Prerequisite feature IDs:** PLY-001.

### PLY-009 — Character creation, appearance, classes, origins

**Requirement:** REQ-PLY-009  
**Purpose:** Define optional player identity and appearance selection without assuming a class system for the first slice.  
**Target mapping:** Use edition-supported appearance/customization capabilities; unsupported features are clearly scoped.

**Acceptance criteria**
- AC-PLY-009-01: Character profile fields have stable IDs and do not overwrite world/player progression on appearance changes.
- AC-PLY-009-02: Class/origin gameplay bonuses remain disabled until an approved balance model exists.

**Test cases**
- TC-PLY-009-01: TC-PLY-009-01 profile creation and appearance persistence
- TC-PLY-009-02: TC-PLY-009-02 appearance update does not reset progression

**Prerequisite feature IDs:** PLY-001.

### PLY-010 — Character death, respawn, recovery, permadeath rules

**Requirement:** REQ-PLY-010  
**Purpose:** Provide a configurable death lifecycle while preserving the fact that the exact death/restart policy remains unapproved.  
**Target mapping:** Each edition must implement the same approved policy through its own lifecycle hooks.

**Acceptance criteria**
- AC-PLY-010-01: No death, respawn, inventory retention or permadeath default is silently selected; the active policy must be present in the approved manifest.
- AC-PLY-010-02: Death/restart transitions are idempotent and cannot duplicate loot, rewards, NPCs or world resets.

**Test cases**
- TC-PLY-010-01: TC-PLY-010-01 missing death-policy approval blocks policy activation
- TC-PLY-010-02: TC-PLY-010-02 repeated death/restart event does not duplicate state

**Prerequisite feature IDs:** PLY-002, PLY-014, QA-013.

### PLY-011 — Status effects, injuries, illnesses, cures

**Requirement:** REQ-PLY-011  
**Purpose:** Integrate temporary effects, fractures, bleeding, illness and recovery with the detailed injury system.  
**Target mapping:** Shared injury/effect records map to target-specific status/effect APIs; NPC dialogue reads authoritative injury state.

**Acceptance criteria**
- AC-PLY-011-01: Every effect has source, body region if relevant, severity, duration, treatment and persistence rules.
- AC-PLY-011-02: Cures consume valid items and cannot clear unrelated injuries or fabricate diagnosis.

**Test cases**
- TC-PLY-011-01: TC-PLY-011-01 fracture/bleeding treatment state transitions
- TC-PLY-011-02: TC-PLY-011-02 cure item cannot clear unrelated condition

**Prerequisite feature IDs:** PLY-002, ITEM-003.

### PLY-012 — Player statistics, milestones, achievements

**Requirement:** REQ-PLY-012  
**Purpose:** Record player-visible milestones from committed events and avoid rewarding duplicate/replayed events.  
**Target mapping:** Statistics and achievement definitions are shared; target-specific presentation can differ.

**Acceptance criteria**
- AC-PLY-012-01: Each milestone has stable ID, trigger conditions and persistence policy.
- AC-PLY-012-02: Achievements cannot be granted by untrusted client state or duplicated on save migration.

**Test cases**
- TC-PLY-012-01: TC-PLY-012-01 milestone triggers once from committed event
- TC-PLY-012-02: TC-PLY-012-02 achievement state survives migration

**Prerequisite feature IDs:** PLY-008.

### PLY-013 — Progression gates and unlock conditions

**Requirement:** REQ-PLY-013  
**Purpose:** Define prerequisite graphs for skills, stations, blueprints and advanced capabilities.  
**Target mapping:** Shared unlock logic with target-specific presentation and persistent state.

**Acceptance criteria**
- AC-PLY-013-01: Unlocks require all declared prerequisites and cannot be bypassed by direct item creation.
- AC-PLY-013-02: Every critical progression path has an alternate route or explicit non-blocking optional status to prevent soft locks.

**Test cases**
- TC-PLY-013-01: TC-PLY-013-01 prerequisite graph and unlock validation
- TC-PLY-013-02: TC-PLY-013-02 soft-lock detection on critical progression path

**Prerequisite feature IDs:** PLY-008.

### PLY-014 — Player profile persistence and data migration

**Requirement:** REQ-PLY-014  
**Purpose:** Persist player progression, profile, needs and owned state safely across updates.  
**Target mapping:** Java and Bedrock use separate save adapters with shared logical schema intent.

**Acceptance criteria**
- AC-PLY-014-01: Profile migration is versioned, backed up and idempotent; invalid downgrade is blocked safely.
- AC-PLY-014-02: Inventory, backpack contents, injuries and progression are preserved according to approved save policy.

**Test cases**
- TC-PLY-014-01: TC-PLY-014-01 profile save/reload preserves player state
- TC-PLY-014-02: TC-PLY-014-02 interrupted profile migration restores backup

**Prerequisite feature IDs:** BASE-009, QA-013.

### ITEM-001 — Item registry, identifiers, rarity, stack limits

**Requirement:** REQ-ITEM-001  
**Purpose:** Create canonical item definitions and target-native registry entries.  
**Target mapping:** Shared logical item IDs map to Java registry IDs and Bedrock identifiers; stack behavior is explicit per item.

**Acceptance criteria**
- AC-ITEM-001-01: Every item has unique ID, category, stack limit, rarity policy, tags and target mappings.
- AC-ITEM-001-02: Registry collisions and unsupported target properties block generation; no item silently falls back to a vanilla item.

**Test cases**
- TC-ITEM-001-01: TC-ITEM-001-01 item registry uniqueness and target mapping
- TC-ITEM-001-02: TC-ITEM-001-02 stack limit and metadata validation

**Prerequisite feature IDs:** BASE-007.

### ITEM-002 — Raw materials, ores, drops, processed materials

**Requirement:** REQ-ITEM-002  
**Purpose:** Define resource materials, sources, yields, processing states and scarcity ownership.  
**Target mapping:** Equivalent material identities across editions; target-native drops and blocks map to shared resource records.

**Acceptance criteria**
- AC-ITEM-002-01: Every material has source, finite/renewable classification, processing path and conservation rules.
- AC-ITEM-002-02: Resource generation, harvesting and processing cannot create negative stock or duplicate output.

**Test cases**
- TC-ITEM-002-01: TC-ITEM-002-01 material source and processing accounting
- TC-ITEM-002-02: TC-ITEM-002-02 harvest/reload does not duplicate resource

**Prerequisite feature IDs:** BASE-007.

### ITEM-003 — Food, drinks, consumables, medicine

**Requirement:** REQ-ITEM-003  
**Purpose:** Define food, potable/unsafe drinks, medicines and consumables with effect, spoilage and usage contracts.  
**Target mapping:** Shared item/effect definitions with separate Java/Bedrock item components and interaction adapters.

**Acceptance criteria**
- AC-ITEM-003-01: Consumption removes exactly one valid quantity and applies only declared effects; spoiled/contaminated items have explicit outcomes.
- AC-ITEM-003-02: Food, water and medicine are not interchangeable; treatment effects match the injury/need record.

**Test cases**
- TC-ITEM-003-01: TC-ITEM-003-01 consume food/drink/medicine once
- TC-ITEM-003-02: TC-ITEM-003-02 spoiled or contaminated consumable applies defined effect

**Prerequisite feature IDs:** ITEM-001, CRAFT-001.

### ITEM-004 — Tools and tool tiers

**Requirement:** REQ-ITEM-004  
**Purpose:** Define tools, tool classes, tier gates, durability and action compatibility.  
**Target mapping:** Target adapters register tool properties and mining/action behavior independently.

**Acceptance criteria**
- AC-ITEM-004-01: Actions require compatible tool class/tier and consume durability according to the shared rule.
- AC-ITEM-004-02: Wrong tool or broken tool cannot yield full output or bypass a station requirement.

**Test cases**
- TC-ITEM-004-01: TC-ITEM-004-01 tool tier and block/action compatibility
- TC-ITEM-004-02: TC-ITEM-004-02 broken tool and durability boundary

**Prerequisite feature IDs:** CRAFT-001.

### ITEM-005 — Weapons and ammunition

**Requirement:** REQ-ITEM-005  
**Purpose:** Define melee/firearm item identity, ammo compatibility, magazine/reload state and customization hooks.  
**Target mapping:** Java and Bedrock implement separate weapon handling but preserve approved melee+firearm outcomes.

**Acceptance criteria**
- AC-ITEM-005-01: Firearms consume finite compatible ammunition; melee remains usable when ammo is depleted.
- AC-ITEM-005-02: Weapon noise, durability, reload and inventory state are authoritative and exploit-resistant.

**Test cases**
- TC-ITEM-005-01: TC-ITEM-005-01 ammo type, magazine and reload integrity
- TC-ITEM-005-02: TC-ITEM-005-02 weapon noise and durability state consistency

**Prerequisite feature IDs:** ITEM-001, CRAFT-001.

### ITEM-006 — Armor, clothing, protective equipment

**Requirement:** REQ-ITEM-006  
**Purpose:** Define wearable equipment, protection zones, condition and environmental protection.  
**Target mapping:** Shared protection semantics mapped to edition-specific equipment slots/visual capabilities.

**Acceptance criteria**
- AC-ITEM-006-01: Protection is applied once in damage resolution and has explicit durability/repair behavior.
- AC-ITEM-006-02: Clothing warmth, armor protection and medical gear functions remain distinct properties.

**Test cases**
- TC-ITEM-006-01: TC-ITEM-006-01 equipment slot and damage mitigation
- TC-ITEM-006-02: TC-ITEM-006-02 worn condition and repair persistence

**Prerequisite feature IDs:** PLY-002.

### ITEM-007 — Backpacks, containers, storage items

**Requirement:** REQ-ITEM-007  
**Purpose:** Implement varied backpack families and storage items as gameplay containers.  
**Target mapping:** Shared capacity and item rules; Java and Bedrock use separate UI/container adapters.

**Acceptance criteria**
- AC-ITEM-007-01: Small, hiking, tactical, medical and large expedition backpacks have distinct declared capacities/roles; exact values remain balance data.
- AC-ITEM-007-02: Nested backpacks are prohibited in the current design proposal; contents persist and capacity reduction cannot silently delete items.

**Test cases**
- TC-ITEM-007-01: TC-ITEM-007-01 backpack family and capacity differentiation
- TC-ITEM-007-02: TC-ITEM-007-02 nested backpack rejection and content persistence

**Prerequisite feature IDs:** ITEM-001.

### ITEM-008 — Utility, quest, key, currency, and collectible items

**Requirement:** REQ-ITEM-008  
**Purpose:** Define non-consumable utility, access, quest and collectible items with ownership and use rules.  
**Target mapping:** Shared IDs and effect contracts; target-specific registration and interaction.

**Acceptance criteria**
- AC-ITEM-008-01: Keys/access items validate the correct lock/quest; quest items cannot be consumed or duplicated unexpectedly.
- AC-ITEM-008-02: Currency and collectibles have explicit ownership and transaction rules.

**Test cases**
- TC-ITEM-008-01: TC-ITEM-008-01 key/quest item access and ownership
- TC-ITEM-008-02: TC-ITEM-008-02 collectible/currency duplication prevention

**Prerequisite feature IDs:** PLY-013.

### ITEM-009 — Durability, repair, degradation, quality

**Requirement:** REQ-ITEM-009  
**Purpose:** Define item condition, degradation sources, repair ceilings, quality tiers and break states.  
**Target mapping:** Shared durability math with edition-specific persistence and item components.

**Acceptance criteria**
- AC-ITEM-009-01: Use events consume durability once; repair consumes actual materials and cannot exceed item maximum.
- AC-ITEM-009-02: Broken/degraded items cannot retain full performance unless a declared special rule applies.

**Test cases**
- TC-ITEM-009-01: TC-ITEM-009-01 durability loss and break transition
- TC-ITEM-009-02: TC-ITEM-009-02 repair consumes materials and respects maximum

**Prerequisite feature IDs:** ITEM-001.

### ITEM-010 — Enchantments, modifiers, affixes, upgrades

**Requirement:** REQ-ITEM-010  
**Purpose:** Provide a general modifier framework for equipment and weapon attachments without assuming vanilla enchantment compatibility.  
**Target mapping:** Use target-native modifier systems; weapon attachments are represented as validated component/modifier records.

**Acceptance criteria**
- AC-ITEM-010-01: Each modifier has allowed slots, compatibility, stat delta, cost and removal rules.
- AC-ITEM-010-02: Incompatible modifiers and duplicate stacking are rejected; effects remain bounded and explainable.

**Test cases**
- TC-ITEM-010-01: TC-ITEM-010-01 modifier compatibility and stacking
- TC-ITEM-010-02: TC-ITEM-010-02 attachment install/remove preserves item identity

**Prerequisite feature IDs:** PLY-008, CRAFT-009.

### ITEM-011 — Custom block families and block states

**Requirement:** REQ-ITEM-011  
**Purpose:** Define custom building, infrastructure, workstation and environment block families.  
**Target mapping:** Java Fabric block registration and Bedrock block definitions are separate target implementations.

**Acceptance criteria**
- AC-ITEM-011-01: Every block declares state properties, collision, hardness, drops, interaction and persistence behavior.
- AC-ITEM-011-02: Block state combinations are bounded and valid; unsupported target state is reported before generation.

**Test cases**
- TC-ITEM-011-01: TC-ITEM-011-01 block state registry and valid combinations
- TC-ITEM-011-02: TC-ITEM-011-02 block placement/save/load preserves state

**Prerequisite feature IDs:** BASE-004, SHIP-004.

### ITEM-012 — Block hardness, resistance, mining tools, drops

**Requirement:** REQ-ITEM-012  
**Purpose:** Define block breaking, resistance, tool requirements and drop outcomes.  
**Target mapping:** Shared rule contract mapped to Java block behavior and Bedrock block components.

**Acceptance criteria**
- AC-ITEM-012-01: Hardness/resistance and tool gates produce deterministic break outcomes; drops are bounded.
- AC-ITEM-012-02: Unbreakable/protected/claimed blocks respect ownership and permissions.

**Test cases**
- TC-ITEM-012-01: TC-ITEM-012-01 tool-gated block breaking and drop result
- TC-ITEM-012-02: TC-ITEM-012-02 protected block and ownership enforcement

**Prerequisite feature IDs:** ITEM-011, ITEM-004.

### ITEM-013 — Functional blocks with inventories or interfaces

**Requirement:** REQ-ITEM-013  
**Purpose:** Define containers, workstations, power/water interfaces and interactive blocks.  
**Target mapping:** Target-native inventory/UI/interaction implementations with shared logical contracts.

**Acceptance criteria**
- AC-ITEM-013-01: Block inventory capacity and access permissions are validated; insertion/removal is atomic.
- AC-ITEM-013-02: Functional block state persists across chunk/world reload and cannot duplicate contents.

**Test cases**
- TC-ITEM-013-01: TC-ITEM-013-01 container transaction atomicity
- TC-ITEM-013-02: TC-ITEM-013-02 functional block save/reload preserves contents

**Prerequisite feature IDs:** ITEM-011.

### ITEM-014 — Fluids, gases, fuel, temperature interactions

**Requirement:** REQ-ITEM-014  
**Purpose:** Define resource types and interaction contracts for water, fuel, gas and temperature-sensitive materials.  
**Target mapping:** Use target-native fluid/block/entity capabilities; unsupported simulation fidelity is reported as adapted/limited.

**Acceptance criteria**
- AC-ITEM-014-01: Fluid/fuel quantities are conserved across transfer, storage and consumption.
- AC-ITEM-014-02: Contamination, temperature and fuel properties affect only declared compatible systems.

**Test cases**
- TC-ITEM-014-01: TC-ITEM-014-01 fluid/fuel transfer conservation
- TC-ITEM-014-02: TC-ITEM-014-02 temperature and contamination interaction boundaries

**Prerequisite feature IDs:** ITEM-001.

### ITEM-015 — Placement, rotation, orientation, multiblock rules

**Requirement:** REQ-ITEM-015  
**Purpose:** Define placement validation and orientation for structures, machines and larger buildable objects.  
**Target mapping:** Target adapters map rotation/placement to supported block-state and structure APIs.

**Acceptance criteria**
- AC-ITEM-015-01: Placement validates collision, support, permissions and required footprint before consuming items.
- AC-ITEM-015-02: Multiblock structures detect missing/invalid parts and recover safely after reload.

**Test cases**
- TC-ITEM-015-01: TC-ITEM-015-01 placement collision and orientation validation
- TC-ITEM-015-02: TC-ITEM-015-02 multiblock incomplete/reload recovery

**Prerequisite feature IDs:** ITEM-011.

### ITEM-016 — Item/block model, texture, sound, localization references

**Requirement:** REQ-ITEM-016  
**Purpose:** Bind each item/block to target-compatible models, textures, sounds and localization keys.  
**Target mapping:** Java resource assets and Bedrock resource pack assets are independently mapped and validated.

**Acceptance criteria**
- AC-ITEM-016-01: Every visible item/block has a valid model/texture reference and fallback policy; required 3D weapon models are included in the asset plan.
- AC-ITEM-016-02: Missing assets are reported before packaging; sound and localization keys resolve without cross-target path assumptions.

**Test cases**
- TC-ITEM-016-01: TC-ITEM-016-01 asset reference completeness for item/block registry
- TC-ITEM-016-02: TC-ITEM-016-02 3D weapon model and localization references resolve

**Prerequisite feature IDs:** BASE-012, SHIP-004.

### CRAFT-001 — Crafting recipes and recipe categories

**Requirement:** REQ-CRAFT-001  
**Purpose:** Define recipes, categories, ingredients, outputs, stations, tools, unlocks and target mappings.  
**Target mapping:** Normal vanilla Crafting Table remains the first crafting stage; specialist stations are added progressively.

**Acceptance criteria**
- AC-CRAFT-001-01: Every recipe declares exact inputs/output, station, time, unlock and byproducts; no free-output recipe exists.
- AC-CRAFT-001-02: Java and Bedrock recipe definitions produce equivalent intended outcomes and preserve ingredient conservation.

**Test cases**
- TC-CRAFT-001-01: TC-CRAFT-001-01 recipe input/output conservation
- TC-CRAFT-001-02: TC-CRAFT-001-02 basic Crafting Table and specialist station gating

**Prerequisite feature IDs:** ITEM-001, ITEM-002, BASE-007.

### CRAFT-002 — Furnace, smelting, blasting, smoking

**Requirement:** REQ-CRAFT-002  
**Purpose:** Define thermal processing recipes and fuel/heat requirements.  
**Target mapping:** Use native furnace/smoker/blast furnace where appropriate, with target-specific custom stations only when needed.

**Acceptance criteria**
- AC-CRAFT-002-01: Processing consumes correct input and fuel and produces declared output/byproduct once.
- AC-CRAFT-002-02: Interrupted jobs preserve or refund reserved inputs according to the declared policy.

**Test cases**
- TC-CRAFT-002-01: TC-CRAFT-002-01 thermal recipe and fuel accounting
- TC-CRAFT-002-02: TC-CRAFT-002-02 interrupted processing recovery

**Prerequisite feature IDs:** ITEM-003, ITEM-014.

### CRAFT-003 — Machines and processing chains

**Requirement:** REQ-CRAFT-003  
**Purpose:** Define multi-stage machines, input/output buffers, production queues and automation contracts.  
**Target mapping:** Java and Bedrock adapters implement supported machine behavior separately.

**Acceptance criteria**
- AC-CRAFT-003-01: Each stage consumes actual inputs and emits outputs once; queues survive save/reload without duplication.
- AC-CRAFT-003-02: Machine throughput, energy/fluid requirements and buffer limits are explicit and bounded.

**Test cases**
- TC-CRAFT-003-01: TC-CRAFT-003-01 multi-stage processing resource conservation
- TC-CRAFT-003-02: TC-CRAFT-003-02 queued job persistence and restart safety

**Prerequisite feature IDs:** CRAFT-002, ITEM-013.

### CRAFT-004 — Custom workstations and interfaces

**Requirement:** REQ-CRAFT-004  
**Purpose:** Define specialist benches including weapon, ammunition, mechanical, sewing, medical, cooking, water, electronics and prosthetics stations.  
**Target mapping:** Normal Crafting Table is preserved; target-native workstation blocks/UI are generated independently.

**Acceptance criteria**
- AC-CRAFT-004-01: A recipe requiring a specialist bench cannot be crafted at the basic table; workstation access and requirements are enforced.
- AC-CRAFT-004-02: Workstation UI shows required inputs, outputs, missing materials and unlock conditions accurately.

**Test cases**
- TC-CRAFT-004-01: TC-CRAFT-004-01 station requirement enforcement
- TC-CRAFT-004-02: TC-CRAFT-004-02 workstation transaction and UI state correctness

**Prerequisite feature IDs:** CRAFT-001, ITEM-013.

### CRAFT-005 — Fuel types, consumption, efficiency

**Requirement:** REQ-CRAFT-005  
**Purpose:** Define fuel classes, burn/energy value, storage compatibility and consumption accounting.  
**Target mapping:** Target-specific fuel representation with shared resource semantics.

**Acceptance criteria**
- AC-CRAFT-005-01: Fuel is consumed once at the declared rate; incompatible fuel/container combinations are rejected.
- AC-CRAFT-005-02: Fuel storage and transfer preserve quantity and enforce capacity/leak/fire rules where designed.

**Test cases**
- TC-CRAFT-005-01: TC-CRAFT-005-01 fuel consumption and efficiency calculation
- TC-CRAFT-005-02: TC-CRAFT-005-02 incompatible fuel and capacity overflow rejection

**Prerequisite feature IDs:** ITEM-014.

### CRAFT-006 — Repair, dismantling, recycling

**Requirement:** REQ-CRAFT-006  
**Purpose:** Define repair, salvage, dismantling and recycling with material recovery rates and condition loss.  
**Target mapping:** Shared recipe/recovery contract mapped to each target's item/block handling.

**Acceptance criteria**
- AC-CRAFT-006-01: Repair and dismantling consume/produce bounded quantities and cannot duplicate original plus recovered items.
- AC-CRAFT-006-02: Protected/player-owned structures and equipment require correct permission/confirmation before dismantling.

**Test cases**
- TC-CRAFT-006-01: TC-CRAFT-006-01 repair and recycling conservation
- TC-CRAFT-006-02: TC-CRAFT-006-02 dismantle permission and item duplication prevention

**Prerequisite feature IDs:** ITEM-009, ITEM-002.

### CRAFT-007 — Farming, harvesting, animal products

**Requirement:** REQ-CRAFT-007  
**Purpose:** Define planting, growth, harvesting, livestock products and resource inputs as crafting/production loops.  
**Target mapping:** Use native farming where possible and custom target adapters for additional crops/animal products.

**Acceptance criteria**
- AC-CRAFT-007-01: Harvest yields follow growth stage, season/environment and resource rules; no harvest occurs twice from one state.
- AC-CRAFT-007-02: Animal products require valid animals, care/time and input resources; no passive infinite output without upkeep.

**Test cases**
- TC-CRAFT-007-01: TC-CRAFT-007-01 crop growth/harvest state transition
- TC-CRAFT-007-02: TC-CRAFT-007-02 animal product upkeep and yield accounting

**Prerequisite feature IDs:** ITEM-002, ITEM-003.

### CRAFT-008 — Resource regeneration and depletion

**Requirement:** REQ-CRAFT-008  
**Purpose:** Define finite, renewable, recoverable and manufactured resource classes and regional regeneration.  
**Target mapping:** Shared resource semantics with target-specific world/block persistence.

**Acceptance criteria**
- AC-CRAFT-008-01: Harvest/depletion changes authoritative resource stock; regeneration follows configured time/ecology rules.
- AC-CRAFT-008-02: Reload and distant simulation preserve total quantities and cannot duplicate resource nodes.

**Test cases**
- TC-CRAFT-008-01: TC-CRAFT-008-01 depletion and regeneration conservation
- TC-CRAFT-008-02: TC-CRAFT-008-02 region unload/reload does not duplicate resources

**Prerequisite feature IDs:** ITEM-002.

### CRAFT-009 — Recipe unlocks, research, progression requirements

**Requirement:** REQ-CRAFT-009  
**Purpose:** Gate recipes by discovery, skill, research, blueprint, station and faction/quest requirements.  
**Target mapping:** Shared unlock IDs; Java and Bedrock each enforce the same prerequisite outcomes.

**Acceptance criteria**
- AC-CRAFT-009-01: Locked recipes cannot be invoked through hidden/direct recipe paths; unlocks are persisted once.
- AC-CRAFT-009-02: Critical recipes have alternate discovery/acquisition routes or are explicitly optional to prevent soft locks.

**Test cases**
- TC-CRAFT-009-01: TC-CRAFT-009-01 recipe unlock prerequisite enforcement
- TC-CRAFT-009-02: TC-CRAFT-009-02 research/blueprint unlock idempotency and soft-lock check

**Prerequisite feature IDs:** PLY-008.

### CRAFT-010 — Loot tables, drops, rewards, weighted outcomes

**Requirement:** REQ-CRAFT-010  
**Purpose:** Define container/entity/block loot pools, weights, seeded variation and finite reward rules.  
**Target mapping:** Shared loot identities and seeded test vectors; target-specific loot table/data implementation.

**Acceptance criteria**
- AC-CRAFT-010-01: Loot outcomes are reproducible under a fixed seed and cannot exceed declared resource/reward budgets.
- AC-CRAFT-010-02: Container ownership, one-time loot and scenario reset rules prevent duplicate claims.

**Test cases**
- TC-CRAFT-010-01: TC-CRAFT-010-01 seeded loot distribution and budget bounds
- TC-CRAFT-010-02: TC-CRAFT-010-02 one-time loot claim and reset idempotency

**Prerequisite feature IDs:** ITEM-001, ITEM-002, ITEM-003.

## 4. Supporting specification links

- `docs/ZOMBIE_INVASION_PLAYER_JOURNEY_CAMPAIGN_AND_LONG_TERM_PROGRESSION_DESIGN_V1.md` — player progression, unlocks, persistence and long-term stages.
- `docs/ZOMBIE_INVASION_INJURY_AMPUTATION_AND_BIONIC_PROSTHETICS_DESIGN_V1.md` — injuries, fractures, limb loss, treatment and prosthetic progression.
- `docs/ZOMBIE_INVASION_INVENTORY_SCAVENGING_AND_LOOT_DESIGN_V1.md` — item families, backpacks, building loot, inventory and anti-exploit rules.
- `docs/ZOMBIE_INVASION_COMBAT_AND_WEAPON_SYSTEM_DESIGN_V1.md` — approved first-slice melee/firearms, ammo, noise and durability.
- `docs/ZOMBIE_INVASION_CRAFTING_AND_WORKSTATION_PROGRESSION_DESIGN_V1.md` — vanilla Crafting Table first, specialist stations and staged production.
- `docs/CRAFTING_RESOURCE_PRODUCTION_ENGINE_SPEC.md` — recipe model, processing, production queues, resource conservation and integration contracts.

## 5. Open decisions preserved

- Exact death, respawn, recovery and permadeath policy remains unapproved.
- Carry-weight/encumbrance behavior and backpack capacity values remain open; backpack variety itself is required.
- Exact hunger, thirst, temperature, fatigue and hygiene rates/effects require balance and first-slice scope decisions.
- Exact character creation, classes/origins and player appearance scope is not confirmed for the first slice.
- Full item, weapon, armor, food, drink, medicine, material, block and recipe catalogs remain data-authoring work.
- Exact recipe quantities, processing times, fuel values, spoilage rates, loot weights and resource regeneration values remain open.
- Weapon customization and 3D weapon models are required design directions; attachment catalogue and asset production remain future work.
- Farming and animal product breadth belongs to the long-term ecology loop; first-slice crops/animals remain to be selected.

## 6. Implementation order

1. Item IDs, registry, stack rules and player profile persistence.
2. Health, injury, needs and stamina state contracts.
3. Inventory/backpack containers, loot and consumables.
4. Basic Crafting Table recipes and specialist station gating.
5. Weapon/ammunition, durability and equipment integration.
6. Progression/research unlocks, processing and resource loops.
7. Farming, regeneration, advanced blocks and multi-stage production.
8. Target-specific Java/Bedrock implementation and independent acceptance tests.

## 7. Implementation boundary

These 40 features are mapped for design traceability only. They remain `not_implemented_verified`; Java, Bedrock and parity statuses remain unassessed until actual target-specific code, builds, runtime tests and evidence are linked. Proposed dependencies require review and do not establish implementation order by themselves.
