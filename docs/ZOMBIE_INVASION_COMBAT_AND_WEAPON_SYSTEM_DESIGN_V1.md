# Zombie Invasion — Combat and Weapon System Design V1

Status: **DESIGN PROPOSAL — first-slice weapon scope awaiting user approval**
Date: 2026-11-28

## 1. Purpose

Define a readable, balanced and cross-edition combat system for the single-player Zombie Invasion first playable slice. The user-approved enemy roster is Walker, Runner and Brute. This document proposes combat rules and weapon categories; it does not approve every proposed weapon category or numeric balance value.

## 2. Combat principles

- Combat must reward positioning, preparation and resource management rather than unlimited attacks.
- Each approved zombie archetype must have understandable strengths and counterplay.
- Player feedback must clearly communicate hit, damage, reload, ammunition shortage, stagger (if enabled) and defeat.
- The first slice remains balanced for one player.
- Java Edition 26.3 + Fabric and Bedrock Edition 26.60 + stable `@minecraft/server` 2.11.0 must provide equivalent player-facing rules.
- Experimental Bedrock APIs remain disabled.
- No weapon may require a cloud connection or external account to function.

## 3. Weapon category model

### 3.1 Melee weapons

Proposed baseline category:
- Improvised melee tool (low damage, readily available).
- Heavy melee tool (higher impact, slower recovery).
- Durable utility tool that can serve both combat and approved repair/resource interactions, if balance permits.

Melee properties:
- Damage profile.
- Attack interval and recovery.
- Effective reach.
- Durability or wear policy.
- Optional knockback/stagger, only if consistently testable.
- Repair/crafting requirements, if crafting is included in the approved scope.

Melee attacks must not cause uncontrolled block destruction. Hit registration and cooldowns must prevent unintended rapid-hit exploits.

### 3.2 Ranged weapons — candidate scope

Possible ranged category:
- A basic firearm intended for controlled single-player use.
- A more powerful but slower or rarer firearm, if scope and balance allow.
- A simple ranged non-firearm alternative, if firearms are deferred.

Ranged weapon properties:
- Damage profile and effective range.
- Fire mode (single shot by default).
- Magazine capacity and reserve ammunition.
- Reload duration and interruption rules.
- Accuracy/spread and optional recoil.
- Sound/noise radius and encounter consequences.
- Durability/maintenance, only if needed and consistently supported.

Firearms are a **proposal**, not a confirmed first-slice requirement. Weapon names, models, exact counts and real-world representations are not fixed here.

## 4. Ammunition and scarcity

If ranged weapons are approved:
- Ammunition is a finite inventory resource.
- Ammo types must be explicit and compatible with their weapon IDs.
- Reloading transfers ammunition from reserve inventory to the magazine; it must not create ammunition.
- Empty magazines and insufficient reserve ammo produce clear feedback.
- Loot placement and total ammunition budget must be balanced for a solo run.
- No infinite-ammo default unless a later difficulty/accessibility setting explicitly provides it.
- Ammo pickup limits and stack sizes must be validated on both editions.

The first slice should prefer curated, reproducible supply placement over uncontrolled random drops, unless the user approves seeded randomization.

## 5. Damage and hit resolution

The shared combat contract should define:
- Attacker and target identity.
- Weapon/archetype IDs.
- Base damage and any approved modifiers.
- Range and line-of-sight validation.
- Cooldown and attack-state validation.
- Damage result and feedback event.
- Knockback/stagger outcome, if enabled.
- Kill/cleanup notification.

Avoid double application of damage when native Minecraft damage events and custom logic interact. Each attack must resolve once. Damage values remain configurable and require playtesting.

## 6. Zombie-specific combat interaction

- **Walker:** baseline damage and durability; teaches the player the core combat loop.
- **Runner:** lower durability but higher approach pressure; player should benefit from early detection and accurate attacks.
- **Brute:** high durability and slow movement; should reward distance, focused attacks and route management. Do not grant arbitrary immunity to common weapons.

The design must not make any archetype a mandatory ammunition sink. A player should retain at least one viable counterplay path if ranged ammunition is depleted.

## 7. Noise and encounter interaction

If weapon noise is enabled:
- Weapon noise is a scenario event with a configurable radius/strength.
- Noise may influence eligible zombie investigation/targeting, but must not spawn unlimited enemies.
- Noise feedback must be understandable and consistent.
- Suppression/silencers are deferred unless explicitly approved.
- Noise simulation must be bounded and performant on both editions.

## 8. Inventory integration

The combat system depends on a shared item identity contract:
- Stable item ID and schema version.
- Item category and stack policy.
- Weapon/ammunition compatibility.
- Magazine/reserve representation where supported.
- Durability and repair metadata, if enabled.
- Loot-source eligibility.
- Java and Bedrock item mapping.

The user-facing inventory may use different native UI and implementation details on each edition. Cross-edition parity means equivalent rules and outcomes, not identical code or screen rendering.

## 9. First-slice exclusions unless separately approved

- Complex attachments and weapon modification benches.
- Weapon crafting trees.
- Ballistic simulation, bullet drop and advanced penetration.
- Weapon jamming and detailed maintenance.
- Suppressors and stealth weapon systems.
- Large weapon catalogues and rarity affixes.
- Player skill trees and class-specific combat perks.
- PvP, multiplayer balancing and dedicated-server combat.

## 10. Security, reliability and exploit prevention

- Validate attack cooldowns and reload state server-side/runtime-authoritatively where platform architecture allows.
- Do not trust client-only damage or inventory changes.
- Prevent ammunition duplication during reload, death, restart and inventory transfer.
- Ensure scenario reset does not duplicate or delete unrelated user items.
- Bound projectile/entity counts and clean up scenario-owned projectiles.
- Log test diagnostics without collecting personal telemetry.

## 11. Cross-edition acceptance tests

Run independently on Java and Bedrock:
1. Each approved weapon category can be acquired and used as configured.
2. Attack cooldown and damage resolve once per valid hit.
3. Range and line-of-sight rules behave within agreed tolerances.
4. Walker, Runner and Brute receive correct damage and feedback.
5. Reload transfers ammunition correctly without duplication or loss.
6. Empty ammunition produces the correct blocked-action feedback.
7. Death, defeat, restart and scenario cleanup do not corrupt inventory.
8. Weapon noise, if enabled, triggers only bounded encounter responses.
9. Performance remains acceptable under the maximum approved hostile budget.
10. A solo player has a viable combat option when ranged ammunition is exhausted.

Tests not executed must be marked NOT_RUN. A successful build does not prove in-game combat correctness.

## 12. User decisions required

The following must be explicitly decided before the combat scope is frozen:

1. First-slice weapon scope:
   - A — melee only.
   - B — melee + ranged non-firearm weapons.
   - C — melee + firearms and finite ammunition.
2. Should weapon noise attract or alert nearby zombies in the first slice?
3. Should weapons use durability, or should balance rely on ammunition and cooldowns?
4. Is limited, curated ammunition supply acceptable as the default?

Recommended starting point: Option C only if the user wants a stronger zombie-apocalypse combat identity; otherwise Option A or B reduces first-slice implementation and balance risk. No option is approved by this document.

## 13. Implementation boundary

This is a design proposal only. It does not implement weapons, damage logic, ammunition, inventory changes, entities, packs, mods or playable artifacts. Application source code remains unchanged.
