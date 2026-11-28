# Zombie Invasion — Inventory, Scavenging and Loot Design V1

Status: **DESIGN PROPOSAL — inventory limits and survival depth awaiting user approval**
Date: 2026-11-28

## 1. Purpose

Define how the player finds, stores, uses and manages supplies in the abandoned town. This system connects the confirmed functional buildings (Market, Hospital and Police Station) with the approved combat direction (melee + firearms, weapon noise enabled, weapon durability enabled and limited ammunition).

This is a design proposal. It does not settle every inventory size, survival mechanic, loot quantity or randomization policy.

## 2. Design principles

- Loot should support meaningful decisions, not require repetitive container grinding.
- Each functional building has a distinct and understandable supply identity.
- Limited ammunition must create resource pressure without making the scenario unwinnable.
- Melee remains viable when firearm ammunition is exhausted.
- Medical supplies are useful but cannot erase all combat consequences.
- Loot placement must be reproducible for balance testing.
- Java and Bedrock use separate technical implementations but equivalent item identities and gameplay outcomes.
- No personal telemetry or cloud dependency is required.

## 3. Item taxonomy

Proposed first-slice categories:

1. **Food and basic supplies:** food items and general survival supplies.
2. **Medical:** healing/recovery items and basic medical supplies.
3. **Weapons:** approved melee weapons and firearms.
4. **Ammunition:** finite ammo items with explicit weapon compatibility.
5. **Repair and maintenance:** materials or kits used to restore approved weapon/defence durability, if repair is included.
6. **Defence materials:** supplies used at designated barricade/repair points.
7. **Objective items:** keys, access items, radio components or scenario-specific quest objects, only if required by the approved scenario.

Each item definition must have a stable project ID, category, stack policy, acquisition source, use rule, compatibility constraints and target-specific mapping.

## 4. Building loot identities

### 4.1 Market — food and general supplies

Expected categories:
- Food and basic consumables.
- General-purpose supplies.
- Limited repair/utility materials, if approved.

Market loot should not become the best source of firearms or large ammunition caches.

### 4.2 Hospital — medical supplies

Expected categories:
- Basic recovery items.
- More limited advanced medical supplies, if included.
- Scenario-specific medical objective items, if needed.

Medical items must have a clear use effect, cooldown or scarcity rule. No medical item should grant invulnerability or trivialize damage.

### 4.3 Police Station — tactical and defence supplies

Expected categories:
- Firearms and/or approved weapon variants.
- Limited compatible ammunition.
- Melee equipment.
- Defence supplies and repair materials.

The police station must not guarantee enough ammunition to trivialize all encounters. Its supplies must be balanced against the entire scenario.

### 4.4 Residential area and safehouse

- Residential buildings may provide small, low-value supplies.
- Safehouse starts with only the explicitly approved baseline kit.
- The safehouse must not contain an unlimited restock mechanism.

Other landmarks (gas station, military checkpoint, underground shelter) remain future expansion locations unless explicitly added to the first-slice map.

## 5. Loot placement and randomization

Recommended first-slice approach: **curated fixed loot placement**.

- Important resources have authored locations and known quantities.
- Optional low-impact supplies may use bounded seeded variation only if it does not undermine repeatability.
- A scenario reset restores scenario-owned loot to the authored baseline.
- Loot must not duplicate on repeated container open/close, reload, death or restart.
- A failed item grant must not mark the container as permanently looted.
- Container ownership and scenario IDs must distinguish generated loot from unrelated world/player content.

Seeded randomization is a proposal for optional variation, not a confirmed requirement.

## 6. Inventory behavior

The first-slice inventory must support:
- Picking up and dropping supported items.
- Stack limits and item compatibility.
- Weapon selection and equipment.
- Firearm magazine and reserve ammunition accounting.
- Reload transfer without duplication.
- Medical item use and clear feedback.
- Durability state for supported weapons.
- Scenario objective item tracking.
- Safe handling of inventory state during defeat and restart.

Open design questions:
- Native Minecraft inventory only, or a custom survival inventory UI?
- Should the first slice impose a weight/carry-capacity limit?
- Should the player be able to store supplies in safehouse containers?
- Should items persist between scenario attempts, or reset to the authored starting state?

Do not implement weight, encumbrance or custom inventory UI without explicit approval.

## 7. Ammunition economy

- Ammunition is finite and weapon-specific.
- Every magazine has a defined capacity.
- Reload consumes the exact number of rounds moved from reserve to magazine.
- Partial reload behavior must be specified and tested.
- Ammo cannot be generated by firing, swapping weapons, dying or restarting.
- The total ammo budget must be sufficient for a viable run but low enough to preserve melee and tactical choices.
- Balance tests should include runs where the player exhausts ranged ammunition.

Exact ammo types, capacities and quantities are unresolved and must be data-driven.

## 8. Medical and food economy

- Food and medical items have distinct functions; do not make every consumable a generic healing item.
- Medical recovery must have clear limits and feedback.
- The first slice should avoid adding thirst, infection, bleeding, disease or complex treatment systems unless separately approved.
- Any use-time interruption and combat restriction must be consistent across both editions.

Whether hunger is native Minecraft hunger, custom scenario hunger or absent from the first slice remains unresolved.

## 9. Cross-edition item contract

Shared logical fields:
- Stable item ID and schema version.
- Item category.
- Display name and localization key.
- Stack limit.
- Durability policy.
- Use effect and cooldown.
- Weapon/ammunition compatibility.
- Loot table eligibility.
- Scenario ownership/reset behavior.

Java/Fabric and Bedrock pack definitions are separate. Do not assume a Java item ID or datapack can be reused directly as a Bedrock item definition.

## 10. Anti-exploit and persistence rules

- Item grants and container looting must be atomic or recoverable.
- Reload must be idempotent and duplication-safe.
- Scenario reset may reset scenario-owned containers and items only.
- Unrelated player-created containers and world regions must not be deleted.
- If the death/restart policy is approved, its inventory retention/reset rules must be explicitly integrated; do not assume the current restart proposal is approved.
- Any persistent project save or inventory migration must be versioned.

## 11. Acceptance tests

Run independently on both editions:
1. Each functional building exposes only its allowed loot categories.
2. Loot is reproducible under the chosen fixed/seeded policy.
3. Container reopening does not duplicate loot.
4. Failed item grants can be retried without loss or duplication.
5. Ammo is compatible with the correct firearm only.
6. Reload transfers exact quantities and handles interruption safely.
7. Weapon durability changes only under defined use events.
8. Medical and food effects match their item definitions.
9. Scenario reset affects scenario-owned loot only.
10. Player can complete a test run with depleted ammunition using melee counterplay.
11. Maximum inventory/container activity remains within performance limits.
12. Java and Bedrock gameplay outcomes meet the shared contract.

Tests not executed must be marked NOT_RUN. Package build success is not evidence of in-game inventory correctness.

## 12. Open user decisions

1. Inventory interface: native Minecraft inventory or custom survival inventory?
2. Carry limit: unlimited normal slots or weight/capacity system?
3. Safehouse storage: should the player be able to store supplies between phases?
4. Loot model: fixed authored loot or seeded random variation?
5. Hunger: native Minecraft hunger, custom hunger, or no hunger mechanic?
6. Scenario restart inventory: reset to starting kit, retain selected items, or retain full inventory? This depends on the still-unapproved death/restart policy.

Recommended first-slice scope: use the native inventory, no weight system, curated fixed loot and no custom thirst/infection mechanics. Treat safehouse storage and between-attempt persistence as separate decisions.

## 13. Implementation boundary

This is a design proposal only. It does not implement inventory UI, items, loot containers, loot tables, survival mechanics, packs, mods or playable artifacts. Application source code remains unchanged.
