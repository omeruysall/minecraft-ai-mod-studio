# Item, Inventory, Equipment & Loot Engine Specification

**Document status:** Design draft  
**Version:** 0.1  
**Implementation status:** Not implemented; design requirements only.  
**Approval status:** Awaiting product decisions and baseline approval.

## 1. Purpose
Define custom item content, inventory interactions, equipment slots, durability, item modifiers, rarity, loot generation, containers, and item lifecycle for generated Minecraft projects. The engine must preserve item identity and ownership, prevent duplication/loss, and integrate with crafting, economy, quests, combat, NPCs, and world interactions.

## 2. Ownership boundaries
- This engine owns custom item definitions, item metadata contracts, equipment rules, loot tables, and inventory transaction abstractions where no platform-native owner exists.
- Platform inventory APIs remain authoritative for actual item stacks and slot state.
- Crafting Engine owns recipe execution and production consumption/output.
- Economy Engine owns currency and market transactions.
- Combat Engine owns damage calculations and combat effects.
- Quest Engine owns objective state and reward requests.
- NPC Engine owns NPC identity and equipment assignment requests.
- World/Environment engines own block/container placement and interaction authorization.
- Dependency Resolver owns required item libraries and platform compatibility.

## 3. Principles
- Item identity, stack behavior, metadata, and persistence are explicit.
- All inventory mutations are server-authoritative and transactional.
- Transfers and rewards are idempotent and duplication-resistant.
- Vanilla item behavior is preserved unless project configuration explicitly changes it.
- Custom item capabilities declare exact platform/version support.
- Destructive changes to item IDs or registries require migration analysis.
- Visual assets are separate from item logic and reference Resource Pack assets.

## 4. Scope
In scope: custom items, categories, stack rules, metadata, durability, equipment slots, attributes/modifiers, rarity, item sets, containers, loot tables, drop rules, item binding/ownership, repair, upgrade, identification, custom UI hooks, and item migration.

Out of scope: real-money item sales, gambling/loot-box monetization, unbounded item generation, and bypassing platform inventory security.

## 5. Item definition
Each item has stable namespaced ID, display name, description, category, icon/model references, stack limit, max durability, damage behavior, rarity (if enabled), tags, data schema, platform mappings, recipe/loot references, permissions, version, and migration policy. IDs must never depend on translated display names.

## 6. Stack and metadata model
Define stack identity, merge compatibility, max count, metadata equality, custom data size limits, and split/merge behavior. Metadata must be schema-versioned and bounded. Stacks with distinct ownership, unique state, enchantments, or durability cannot merge unless semantics explicitly permit it.

## 7. Inventory transaction contract
An inventory operation records actor, source/destination, item ID, quantity, preconditions, permissions, transaction ID, and idempotency key. Validate capacity and ownership before mutation. Either commit all related slot changes or recover safely. Domain engines request operations through this contract rather than directly editing unrelated inventory state.

## 8. Containers and storage
Containers define capacity, slot rules, access policy, lock state, ownership, automation access, and persistence. World interaction validates physical access and claims. Storage networks and logistics engines own cross-container routing. Prevent race conditions when multiple players access the same container.

## 9. Equipment slots and loadouts
Equipment profiles define slots, accepted categories/tags, exclusivity, hand/offhand rules, cosmetic slots, and loadout switching. Validate equipment requirements and prevent illegal duplicate placement. Platform-specific slot support is declared. Loadouts must restore safely after disconnect and death according to project policy.

## 10. Durability, repair, and breakage
Define durability units, damage sources, thresholds, break behavior, repair materials/costs, unbreakable rules, and persistence. Repair operations are inventory transactions and may invoke crafting/economy. Prevent negative durability and duplicate repair application.

## 11. Attributes and item modifiers
Modifiers define target attribute, operation order, value bounds, stacking, priority, source, duration, and removal conditions. Combat and Progression engines own final attribute calculations where appropriate. Item engine exposes validated modifier references and does not silently overwrite other systems' modifiers.

## 12. Rarity, sets, and affixes
Optional rarity tiers, set bonuses, randomized affixes, and identification mechanics require bounded pools, deterministic seed policy, and balance constraints. Set bonuses are computed by a single authoritative system. Randomization must not create unbounded power or duplicate unique item identities.

## 13. Loot tables and drop generation
Loot tables define conditions, pools, weights, rolls, guarantees, exclusions, luck modifiers, and source context. Server validates drop events and uses controlled random seeds. Define whether loot is per-player, shared, instanced, or world-drop. Prevent repeated trigger farming and reward duplication.

## 14. Item ownership, binding, and transfer
Optional rules include soulbound, account/character binding, party ownership, trade locks, quest items, and claim-bound storage. Define death drops, despawn, pickup delay, ownership expiry, trade, mail, and recovery. Economy and permissions validate any purchase or transfer. Avoid locking users out of essential progression items.

## 15. Crafting, economy, quest, and combat integration
Crafting consumes/produces items through inventory transactions. Economy handles prices and currency. Quests reference item facts and reward requests. Combat consumes equipment modifiers and emits loot-source facts. Each integration uses stable IDs and idempotent contracts to avoid duplicate ownership or rewards.

## 16. NPC equipment and trading
NPC Engine owns character identity and behavior. Item engine supplies equipment eligibility and item references. Economy owns trades and payment. Define NPC inventory authority, equipment persistence, restocking ownership, and loot on NPC death. Avoid duplicating NPC storage state.

## 17. UI and accessibility
Provide item catalog, tooltip details, inventory/equipment views, loadout manager, container access, durability/repair preview, loot table editor, and migration warnings. Include keyboard/controller navigation, readable stat descriptions, and non-color-only rarity indicators.

## 18. Authoring experience
Provide item designer, metadata schema editor, equipment slot editor, modifier builder, loot table editor, stack/transfer simulator, and asset references. Conversational item requests become structured definitions with platform support, recipes, balance impact, migration, and security review before approval.

## 19. Persistence and migration
Persist stable IDs, metadata schema versions, item instances where needed, ownership/binding, durability, container contents, and migration state. Registry changes must define rename/remap/removal behavior. Never silently delete unknown item data. Existing worlds require backup before risky migrations.

## 20. Security and exploit prevention
Validate item creation, quantity, metadata, durability, ownership, and transfers server-side. Prevent item duplication, negative stacks, forged custom data, replayed rewards, container race exploits, invalid modifiers, and malicious oversized metadata. Bound loot calculations and random roll counts.

## 21. Validation and testing
Validate IDs, stack limits, metadata schemas, slot rules, modifier bounds, loot weights, reward references, permissions, platform support, and migration mappings. Runtime tests cover stack split/merge, concurrent transfers, full inventory, container access, equipment swap, break/repair, death/drop, loot replay, reconnect, and server restart. Test on real target loaders/editions. Unrun tests are reported as not run.

## 22. Diagnostics and repair
Expose item provenance, transaction IDs, transfer failures, invalid metadata, modifier sources, loot evaluation, and migration traces. Repair plans must preserve legitimate items and avoid duplication. Changes to IDs, stack behavior, ownership, drop rules, or modifier values require renewed approval.

## 23. Delivery
Deliver item catalogs, metadata schemas, equipment profiles, modifier definitions, loot tables, platform adapters, asset references, migration scripts, compatibility report, test evidence, and user guide. Include editable source and runnable artifacts where supported.

## 24. Acceptance criteria
- Every custom item has stable ID and versioned metadata schema.
- Inventory mutations are authoritative, transactional, and idempotent.
- Stack, equipment, and durability rules are explicit.
- Loot generation is bounded, auditable, and duplication-resistant.
- Ownership and transfer policies are explicit.
- Domain integrations do not duplicate authoritative state.
- Registry migrations preserve or safely remap existing items.
- Platform limitations are disclosed.
- Multiplayer and failure recovery tests pass on supported targets.
- Material item balance or identity changes require renewed approval.

## 25. Open decisions
1. Which platforms, versions, and loaders are mandatory at launch?
2. Are custom items a core first-release feature?
3. Which item categories and metadata types are supported initially?
4. What are default stack limits and custom metadata size limits?
5. Which vanilla behaviors can projects override?
6. Which equipment slots are supported per platform?
7. Are loadouts and cosmetic slots included?
8. Which durability and repair models are available?
9. Are rarity tiers, affixes, and set bonuses in scope?
10. Which loot distribution modes are supported?
11. What is the random seed and reproducibility policy?
12. Which ownership/binding rules are required?
13. How do death, despawn, and item recovery work?
14. Which container and automation APIs are supported?
15. What are transaction and concurrency guarantees?
16. Which item modifiers can affect combat or progression?
17. Are NPC inventories and equipment physically simulated or abstracted?
18. What anti-duplication tests are release blockers?
19. Which item registry migrations are supported?
20. What happens to items from removed dependencies?
21. Which external item/loot libraries are allowed and under what licenses?
22. What item catalog, tooltip, and accessibility UI is mandatory?
23. What admin recovery and audit tools are required?
24. What world backup and rollback guarantees apply to item migrations?

## 26. Current status
Design draft only. All open decisions remain unresolved until explicitly decided by the product owner. No custom item registry, inventory transaction service, equipment manager, loot engine, or playable item system is implemented by this document.
