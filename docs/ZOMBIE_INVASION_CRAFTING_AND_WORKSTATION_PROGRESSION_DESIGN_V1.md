# Zombie Invasion — Crafting and Workstation Progression Design V1

Status: USER-REQUESTED CRAFTING REQUIREMENT — progression model proposed; recipes and balance unresolved
Date: 2026-11-28

## 1. Core requirement

The user requires crafting to be a broad foundational system: items and equipment across the project should be craftable wherever a coherent recipe and progression path can be designed. Not every item must be available at the start or craftable from the basic grid.

The user explicitly requires the normal Minecraft Crafting Table to remain the first-stage crafting station. Specialized stations such as a Weapon Workbench become available later as the player progresses.

## 2. Progression principle

Crafting follows staged progression:
1. Basic Crafting Table — starting-level recipes and simple components.
2. Field utility stations — cooking, water treatment and simple medical preparation.
3. Specialist workbenches — weapons, ammunition, sewing, mechanics and medicine.
4. Advanced production stations — electronics, vehicle systems and prosthetics.
5. High-tier engineering — rare/advanced components and complex assemblies.

Unlocks may depend on discovering blueprints, finding tools, collecting materials, building a station or completing a milestone. Exact unlock conditions remain open.

## 3. Workstation families

### 3.1 Basic Crafting Table
Must remain available as the initial station. Suitable for:
- Basic survival tools and simple equipment.
- Basic components and repair materials.
- Simple camp items and primitive utility objects.
- Basic backpack or tent components only where recipe complexity permits.

It must not produce high-tier firearms, advanced ammunition, vehicle engines or bionic limbs directly.

### 3.2 Weapon Workbench
- Firearm assembly from compatible parts.
- Weapon attachments and customization.
- Selected repairs and maintenance.
- Weapon-specific component processing.
- Recipe validation for compatibility.

### 3.3 Ammunition/Reloading Bench
- Ammunition production and reloading where supported by the game's item model.
- Cartridge/casing and component management.
- Strict finite-material accounting and anti-duplication rules.

### 3.4 Mechanical/Vehicle Workshop
- Vehicle parts, engines, tires, batteries and fuel-system components.
- Vehicle repair and maintenance.
- Component-level compatibility and assembly.

### 3.5 Sewing and Backpack Workbench
- Backpack variants and upgrades.
- Clothing, straps, tent fabric and sleeping equipment.
- Repair of fabric/leather items.

### 3.6 Medical Workbench
- Bandages, splints, medical kits and treatment supplies.
- Advanced medical components only when unlocked.
- Does not replace any required surgery/prosthetics station.

### 3.7 Cooking Station
- Cooked meals, preserved food and recipes.
- Ingredient quality and preparation rules.
- Food storage and spoilage only if approved as a separate mechanic.

### 3.8 Water Treatment Station
- Water collection, filtration and purification.
- Clean/unsafe water states and compatible containers.
- Drink preparation where included.

### 3.9 Electronics Workbench
- Batteries, circuits, sensors, control units and power components.
- Advanced vehicle and bionic prosthetic subassemblies.

### 3.10 Advanced Engineering/Prosthetics Station
- Precision mechanical assemblies.
- Bionic limb assembly, fitting and calibration.
- Advanced repairs and specialized components.

Stations may be consolidated for the first playable slice if implementation scope requires it, but the progression architecture should not collapse all advanced recipes into the basic Crafting Table.

## 4. Recipe contract

Every recipe must define:
- Stable recipe ID and schema version.
- Input ingredients and exact quantities.
- Required station and station tier.
- Required blueprint/unlock, if any.
- Output item and quantity.
- Processing time, if applicable.
- Tool requirements and durability cost, if applicable.
- Failure/rollback behavior.
- Java and Bedrock target mappings.
- Balance category and intended progression stage.

Recipes must be data-driven and versioned. Avoid hard-coded, target-specific duplication of gameplay logic.

## 5. Crafting economy and scavenging

- Raw materials, components and finished items must have distinct roles.
- Loot remains an important source of rare parts, blueprints and specialist tools.
- Crafting must not remove the value of scavenging.
- A rare item may be craftable only after obtaining a blueprint or rare component.
- Weapon ammunition remains limited and finite; crafting ammunition consumes finite resources and must not make ammunition effectively unlimited.
- Boss rewards may unlock or supply advanced recipes, but exact rewards remain undecided.

## 6. Cross-system links

Crafting must connect with:
- Weapons and attachments.
- Vehicle maintenance and fuel systems.
- Food, cooking and preservation.
- Water collection and purification.
- Backpacks, tents and camping.
- Medical treatment, fractures and limb injuries.
- Mechanical and bionic prosthetics.
- Base defence and repair materials.
- Loot, blueprints and boss rewards.

## 7. Anti-exploit and persistence

- Crafting output must be granted exactly once.
- Interrupted crafting must not duplicate or destroy ingredients unexpectedly.
- Station ownership and access rules must be explicit.
- Recipes must validate input compatibility and quantities.
- Crafting state must survive save/reload safely where jobs are persistent.
- Scenario reset must not delete unrelated player-built stations or items.

## 8. Acceptance tests

1. The normal Minecraft Crafting Table is the initial crafting station.
2. Basic recipes work without specialist stations.
3. Advanced recipes are rejected at the basic table.
4. Specialist stations unlock and accept only compatible recipes.
5. Every recipe consumes exact input quantities and grants exact outputs.
6. Interrupted/failed crafting cannot duplicate or irrecoverably lose items.
7. Blueprint and progression gates work consistently.
8. Ammo crafting consumes finite materials and preserves the limited-ammo economy.
9. Prosthetic components require the correct multi-stage station chain.
10. Java and Bedrock produce equivalent gameplay outcomes.
11. Unexecuted tests are marked NOT_RUN.

## 9. Open decisions

- Which specialist stations are required in the first playable build versus later progression.
- Whether stations are portable, placeable or fixed to specific buildings.
- Whether crafting takes real game time and can be interrupted.
- Whether blueprints are physical items, discoveries or both.
- Whether crafting requires player skill/level progression.
- Exact recipe lists, quantities, processing times and station tiers.

## 10. Implementation boundary

Design only. This document does not implement recipes, workstations, UI, items, mods, add-ons or playable artifacts.
