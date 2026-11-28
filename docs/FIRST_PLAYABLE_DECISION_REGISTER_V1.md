# First Playable Decision Register v1.0

**Status:** Active design register — not approved as implementation baseline  
**Last updated:** 2026-11-28

## 1. Purpose

Track user-confirmed decisions, design defaults, unresolved choices and implementation blockers for the first playable Java + Bedrock mod/world milestone. This register prevents open questions from being silently resolved by assumptions.

## 2. Confirmed user decisions

| ID | Decision | Confirmed value |
|---|---|---|
| D-001 | First playable platforms | Minecraft Java Edition and Bedrock Edition |
| D-002 | First playable content scope | Mod/world bundle |
| D-003 | Long-term product scope | Broad Minecraft content creation, tracked through the feature catalog |
| D-004 | Product interaction | Guided conversation with explicit plan approval |
| D-005 | Interface theme/layout | Hybrid theme, workspace layout |
| D-006 | AI interaction | Text and live voice |
| D-007 | Preview area | Enabled |
| D-008 | Right-side project panel | Hybrid AI-suggested and user-controlled |

## 3. Design constraints accepted for the first milestone

- One project identity and shared manifest; separate Java and Bedrock target profiles.
- Java and Bedrock use independent production adapters, dependency graphs, build/import processes and test evidence.
- Java track may include Java mod, world, datapack and resource pack.
- Bedrock track may include behavior pack/add-on, world and resource pack; Java datapack format is not a Bedrock component.
- Both target tracks must independently pass their required playable acceptance gates before the milestone is called complete.
- A shared gameplay requirement does not imply identical implementation or feature parity.
- No production starts without approval bound to the exact plan and manifest revision.
- All required tests not run are reported as NOT_RUN.
- The first slice is deliberately small; it does not attempt all 232 catalog features.

## 4. Blocking decisions

| ID | Decision required | Why it blocks implementation | Current status |
|---|---|---|---|
| B-001 | Exact Java Minecraft version | Determines APIs, pack formats, dependencies and runtime test target | Open |
| B-002 | Java mod loader: Fabric, Forge or NeoForge | Determines project templates, APIs, build plugins and compatibility | Open |
| B-003 | Exact Bedrock version | Determines pack formats and API support | Open |
| B-004 | Bedrock stable/experimental API policy | Controls feature feasibility and world/device requirements | Open |
| B-005 | First shared gameplay feature set | Required to define concrete mod/add-on behavior and playable map | Open |
| B-006 | Target execution/test environments | Required to prove both deliverables actually load and play | Open |
| B-007 | Development order: sequential or parallel target tracks | Impacts CI, schedule and integration strategy | Open |
| B-008 | Local/cloud/hybrid generation and build execution | Determines security boundary, worker architecture and device requirements | Open |

## 5. Important but deferrable decisions

These do not need to block the first local playable slice if explicitly deferred:
- Initial hosted AI provider list and provider priority.
- Managed provider billing versus bring-your-own-key policy.
- Full team collaboration and custom roles.
- Public marketplace monetization and advanced publishing workflows.
- Full multiplayer/server deployment automation.
- Complete offline AI inference.
- Advanced moderation and community operations.
- Long-term support window for every Minecraft version.

Deferral must not remove the design requirement; it must be recorded as post-slice scope.

## 6. Proposed defaults for review

These are recommendations, not user-confirmed decisions:
1. Use one exact, officially supported Java version and one loader for the initial Java slice.
2. Prefer stable Bedrock APIs for the default path; experimental APIs require explicit opt-in and a separate compatibility warning.
3. Select a small gameplay loop that can be represented in both editions with target-specific implementation.
4. Develop the two target tracks sequentially if parallel testing capacity is unavailable, while retaining both as mandatory milestone deliverables.
5. Use isolated workers for builds and tests; never execute generated code in the control-plane process.
6. Keep the first test environment single-player unless the chosen gameplay feature requires multiplayer.
7. Do not select an AI provider before provider privacy, cost and local/offline behavior are agreed.

## 7. Recommended first gameplay feature selection criteria

The shared gameplay feature should:
- Be visible and understandable in a short play session.
- Have a measurable success/failure condition.
- Be implementable with one Java mod plus a small world and optional datapack/resource pack.
- Have a Bedrock-native equivalent using behavior/resource packs and world content.
- Avoid dependence on experimental APIs unless the user explicitly accepts that risk.
- Be testable in a fresh world with repeatable steps.
- Avoid requiring complex multiplayer, economy, NPC dialogue or advanced simulation for the first slice.

Possible feature families for later selection: custom hostile mob encounter, survival challenge/objective, dungeon/arena progression, environmental hazard, or resource/objective collection loop. These are options only, not selected scope.

## 8. Approval and change policy

A decision is confirmed only when the user explicitly selects it. Recommendations do not count as approval. Any change to target version, loader/API, feature scope, target parity or deliverables requires impact analysis and may require renewed approval of the plan and manifest revision.

## 9. Next decision sequence

Resolve in this order:
1. Shared gameplay feature family and minimum playable loop.
2. Java version and loader, based on current compatibility evidence.
3. Bedrock version and API policy, based on current compatibility evidence.
4. Test devices/environments available for both editions.
5. Sequential versus parallel target development.
6. Local/cloud execution and AI provider policy.

## 10. Implementation boundary

This register records decisions and recommendations only. It does not implement platform adapters, generators, game artifacts or tests. The master coding gate remains closed until the first-slice decisions are resolved or explicitly deferred and the user approves the master baseline.


## 11. Dated compatibility recommendation (not yet approved)

Based on official release information checked on 2026-11-28:
- Proposed Java baseline: Minecraft 26.3 + Fabric.
- Proposed Bedrock baseline: Minecraft 26.60 + stable `@minecraft/server` 2.11.0 where scripting is required.
- Default recommendation: exclude experimental Bedrock APIs from the first playable path.
- Development may proceed sequentially by target, but both target tracks remain required for milestone completion.

Sources and technical caveats are recorded in `docs/FIRST_SLICE_COMPATIBILITY_RECOMMENDATION_2026-11.md`. These are recommendations only. The user must confirm or change the target profiles before implementation.


## 12. User-approved compatibility targets (2026-11-28)

The user explicitly approved the first-slice target profiles:
- **Java Edition:** Minecraft 26.3 + Fabric.
- **Bedrock Edition:** Minecraft 26.60 + stable `@minecraft/server` 2.11.0 where scripting is required.
- **Experimental Bedrock APIs:** disabled for the first playable milestone.

These are confirmed user decisions and supersede the pending recommendations in section 11. Exact toolchain patch versions and runtime prerequisites must still be revalidated at implementation start and pinned from official metadata.

Both target tracks remain mandatory for milestone completion. A sequential development order is acceptable as a schedule proposal, but requires a separate explicit decision if it changes delivery timing.


## 13. Next gameplay decision

The next unresolved decision is the shared gameplay loop. Three cross-edition candidates have been documented:
- Candidate A — The Lost Temple (recommended): three-room dungeon, collect three relic fragments, unlock the central seal and complete the vault.
- Candidate B — Outpost Defense: survive three waves and activate extraction.
- Candidate C — Survival Expedition: gather resources, overcome an obstacle and reach the final camp.

The comparison, target-specific component outline and acceptance criteria are in `docs/FIRST_SHARED_GAMEPLAY_LOOP_DESIGN_V1.md`. No candidate is selected until the user explicitly chooses one.


## 14. User-selected gameplay direction — Zombie Invasion (2026-11-28)

The user selected **Zombie Invasion** and requested a highly detailed design. This resolves the first gameplay-concept choice. The detailed design is recorded in `docs/ZOMBIE_INVASION_GAMEPLAY_DESIGN_V1.md`.

The selected concept is a survival, scavenging and base-defence experience with escalating zombie attacks. The proposed first playable slice is a compact settlement/safehouse scenario with supplies, limited defence repairs, a basic zombie archetype and three escalating attacks.

The following are not yet confirmed by the user: first-map theme, single-player versus cooperative requirement, death/restart rules, exact victory objective, loot randomization, free-form building versus designated repair points, custom weapons in the first slice and target-track development order. Recommended defaults are documented as proposals, not decisions.


## 15. User decision — first-slice player count (2026-11-28)

**Decision: Single-player is sufficient for the first playable slice.**

- First-slice acceptance target: one player.
- Cooperative multiplayer and dedicated-server support: deferred to a later milestone.
- This does not permanently exclude multiplayer from the product roadmap.
- The first-slice architecture should remain reasonably extensible, without implementing multiplayer infrastructure prematurely.


## 16. User decision — first map direction (2026-11-28)

**Decision: Abandoned, expandable town.**

The planned town landmark set includes residential houses, hospital, police station, market, gas station, military checkpoint and underground shelter. The first playable build uses a compact authored subset centred on the safehouse; later districts and fully interactive landmarks are staged expansions.

Detailed map layout and acceptance criteria: `docs/ZOMBIE_INVASION_MAP_DESIGN_V1.md`.


## 17. User decision — Market + Hospital + Police Station (2026-11-28)

**Decision: All three buildings must be functional in the first playable slice.**

- Market: searchable food and general supplies.
- Hospital: searchable medical supplies and at least one usable recovery/medical interaction.
- Police Station: searchable tactical/combat/defence supplies within the approved first-slice combat scope.

These are functional gameplay locations, not decorative shells. The first map scope therefore includes the safehouse, residential section and all three buildings, while remaining compact and authored. The gas station, military checkpoint and underground shelter may remain later-stage landmarks.

Detailed roles, constraints and acceptance requirements: `docs/ZOMBIE_INVASION_MAP_DESIGN_V1.md`.


## 18. Death and restart policy — recommendation only (2026-11-28)

A separate proposal recommends that player death ends the current attempt with a DEFEAT result, then allows the player to manually restart the complete scenario from a clean authored baseline. Restart would reset scenario-owned wave state, zombies, defence points, fixed loot, objectives, radio progression and extraction state without deleting the world save or unrelated user content.

This is **not a confirmed user decision**. The user has not yet approved the death/restart rule. Detailed requirements and acceptance tests: `docs/ZOMBIE_INVASION_DEATH_AND_RESTART_POLICY_V1.md`.


## 19. Zombie roster — proposal awaiting user approval (2026-11-28)

A staged roster proposal has been added in `docs/ZOMBIE_INVASION_ZOMBIE_ROSTER_DESIGN_V1.md`:

- Walker: baseline enemy.
- Runner: fast, less durable pressure enemy.
- Brute: slow, durable breach-pressure enemy.
- Screamer, Exploder, Poisoner, Crawler and Armored variants: deferred candidates.

The proposed first-slice choice is Option C (Walker + Runner + Brute), with strict encounter-budget limits and solo-player balance tests. This is a recommendation only. The user has not yet approved the roster or the inclusion of special archetypes.

The next required decision is to select Option A (Walker only), Option B (Walker + Runner) or Option C (Walker + Runner + Brute). No roster implementation is authorized by this proposal.


## 20. User-approved first-slice zombie roster (2026-11-28)

**Decision: Option C — Walker + Runner + Brute.**

- Walker: baseline common enemy.
- Runner: fast, less durable pressure enemy.
- Brute: slow, durable threat that pressures defence positions.
- Screamer, Exploder, Poisoner, Crawler and Armored variants remain deferred.

The roster scope is approved. Exact health, speed, damage, spawn counts, encounter timings and balance values remain open for implementation-time tuning and repeatable solo-player tests. The approved design is documented in `docs/ZOMBIE_INVASION_ZOMBIE_ROSTER_DESIGN_V1.md`.

This decision does not mean the roster has been implemented or tested in-game.


## 21. Combat and weapon scope — proposal awaiting user approval (2026-11-28)

A cross-edition combat design proposal is recorded in `docs/ZOMBIE_INVASION_COMBAT_AND_WEAPON_SYSTEM_DESIGN_V1.md`. It covers melee and ranged weapon models, optional firearms, ammunition scarcity, reload behavior, damage resolution, zombie-specific counterplay, noise interaction, inventory integration, exploit prevention and Java/Bedrock acceptance tests.

The user has not yet approved whether the first playable slice includes melee only, melee plus non-firearm ranged weapons, or melee plus firearms. Weapon noise, durability and ammunition policy also remain open. No weapon or combat implementation is authorized by the proposal.


## 22. User-approved first-slice combat decisions (2026-11-28)

The user approved the following:
- **Weapons:** Option C — melee weapons and firearms.
- **Weapon noise:** enabled; gunfire generates a bounded event that can alert/investigate nearby zombies.
- **Durability:** enabled; weapons degrade through use.
- **Ammunition:** limited and finite; it must be acquired through gameplay.

Melee remains a viable fallback when firearm ammunition is exhausted. Noise must not spawn unlimited zombies or bypass encounter budgets. Reloading, durability, inventory, death and restart interactions require duplication/loss prevention tests.

Exact weapon catalogue, damage, fire rate, magazine capacity, reload timing, durability values, noise radius, ammunition stack sizes, loot quantities and repair rules remain open for detailed design and balance testing.

Approved scope specification: `docs/ZOMBIE_INVASION_COMBAT_AND_WEAPON_SYSTEM_DESIGN_V1.md`. This approval is a design decision, not evidence of implementation or in-game testing.


## 23. Inventory, scavenging and loot — next design proposal (2026-11-28)

A detailed cross-edition proposal has been added in `docs/ZOMBIE_INVASION_INVENTORY_SCAVENGING_AND_LOOT_DESIGN_V1.md`. It defines the distinct loot identities of Market (food/general supplies), Hospital (medical supplies), Police Station (tactical/defence supplies), residential buildings and safehouse; it also covers finite ammunition, durability, reload integrity, container ownership, scenario reset and acceptance tests.

Recommended first-slice defaults are native Minecraft inventory, no weight/encumbrance system, curated fixed loot, and no custom thirst/infection mechanics. These are recommendations only. Inventory UI, carry limits, safehouse storage, loot variation, hunger behavior and inventory persistence across attempts remain unresolved. No inventory or loot implementation is authorized by this proposal.


## 24. Backpack variety — user-confirmed first-slice requirement (2026-11-28)

The user explicitly stated that multiple backpack varieties must be included. Backpack variety is therefore a **confirmed first-playable requirement**, not an optional future feature or cosmetic-only idea.

The inventory design now proposes distinct small daypack, hiking, tactical, medical and large expedition variants. Their exact capacity, rarity, appearance, loot placement and any specialist effects remain to be balanced. The current proposal uses one equipped backpack with separate slot-based storage, no nested backpacks and persistent contents across ordinary save/load; the final interaction and death/restart behavior still require decisions and tests.

Updated specification: `docs/ZOMBIE_INVASION_INVENTORY_SCAVENGING_AND_LOOT_DESIGN_V1.md`.

This decision authorizes design work only; it does not mean backpack items, storage UI or either edition's add-on/mod have been implemented.


## 25. User-requested injury, amputation and bionic prosthetics system (2026-11-28)

The user requested a comprehensive injury system including bone fractures, cracks and other injuries, with possible limb loss. The user specifically described a progression path where a lost arm can eventually be replaced with a bionic arm, but only after a substantial staged process: finding components, producing required parts and completing assembly/installation. This is recorded as a required design scope; exact injury rules, limb-loss conditions, prosthetic tiers and first-slice availability remain unresolved.

Design specification: `docs/ZOMBIE_INVASION_INJURY_AMPUTATION_AND_BIONIC_PROSTHETICS_DESIGN_V1.md`.

No injury or prosthetic feature is implemented or approved for immediate production by this design entry.

## 26. User-requested staged crafting and workstation progression (2026-11-28)

The user requires broad crafting across the mod and explicitly requires the normal Minecraft Crafting Table to remain the first-stage crafting station. Specialist workstations such as a Weapon Workbench are introduced later through progression. Advanced equipment (including firearms, vehicle systems and bionic prostheses) must not be bypassable through the basic Crafting Table.

Design specification: `docs/ZOMBIE_INVASION_CRAFTING_AND_WORKSTATION_PROGRESSION_DESIGN_V1.md`.

The full workstation list, unlocks, recipes, station placement and which stations are included in the first playable slice remain open for detailed design. This is a design requirement, not an implementation claim.
