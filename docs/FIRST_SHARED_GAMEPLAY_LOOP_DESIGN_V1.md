# First Shared Gameplay Loop Design v1.0

**Status:** Design proposal — gameplay selection pending user decision  
**Targets:** Java 26.3 + Fabric; Bedrock 26.60 + stable Script API 2.11.0  
**Experimental Bedrock APIs:** Disabled  
**Milestone:** First playable mod/world bundle

## 1. Purpose

Select a compact, repeatable gameplay loop that can be implemented independently in Java and Bedrock, integrated into a playable map/world and tested without relying on experimental Bedrock APIs.

This document presents candidate loops and recommends one. No gameplay option is selected until the user confirms it.

## 2. Design constraints

The first loop must:
- Be playable in both selected editions.
- Include a real Java mod and a real Bedrock add-on/behavior pack, not only a decorative map.
- Include a purpose-built playable world/map.
- Use platform-specific implementations with shared player-facing intent.
- Avoid experimental Bedrock APIs.
- Have a short, repeatable acceptance test.
- Fit a narrow first milestone and avoid requiring complex online services.
- Include a resource pack only where custom visuals/audio are required.
- Include Java datapack functions only where useful; Bedrock logic must use Bedrock-native pack/function/API mechanisms.
- Produce editable sources and target-specific installable deliverables.

## 3. Candidate A — The Lost Temple (recommended)

### Player experience
The player enters an ancient temple, explores three connected chambers, finds three relic fragments, avoids or defeats guarded encounters, activates the central seal and opens the final vault.

### Minimum playable loop
1. Spawn at the temple entrance and receive a short objective.
2. Explore three bounded rooms.
3. Find one relic fragment in each room.
4. Overcome one simple obstacle or enemy encounter per room.
5. Return to the central seal.
6. Activate the seal when all fragments are collected.
7. Open the vault and reach the completion chamber.
8. Restart or replay the challenge.

### Required components
Java target:
- Fabric mod: registers the relic/key item and the seal interaction or equivalent game mechanic.
- Java world/map: bounded temple with spawn, three rooms, central seal and exit.
- Optional Java datapack: room reset/objective functions if they simplify the implementation.
- Resource pack: custom item/block textures and minimal UI/visual cues if approved.

Bedrock target:
- Behavior pack/add-on: equivalent relic item and interaction logic using supported stable components/API.
- Bedrock world/map: equivalent temple layout and gameplay path.
- Resource pack: Bedrock-specific assets and references.
- No experimental API dependency.

### Parity requirements
- Same objective, room count, relic count, unlock condition and completion result.
- Visual layouts may differ if necessary, but navigation and difficulty must be comparable.
- Interaction implementation may differ between Fabric and Bedrock.
- Each target must be tested independently.

### Why recommended
- Clear beginning, middle and end.
- Easy to demonstrate in a short play session.
- Gives every major first-slice layer a meaningful role: mod/add-on, world, assets, objective logic and delivery.
- Does not require a large open world, complex NPCs, multiplayer or advanced simulation.
- Allows a small, measurable acceptance test.

## 4. Candidate B — Outpost Defense

### Player experience
The player defends a small outpost against three timed waves of hostile mobs, activates defenses between waves and survives until extraction.

### Minimum playable loop
1. Spawn and receive a preparation period.
2. Survive wave 1.
3. Collect supplies and repair/reset defenses.
4. Survive waves 2 and 3.
5. Activate the extraction beacon and complete the challenge.

### Required components
- Java mod and Bedrock add-on for wave orchestration, progression and any custom defensive item.
- Separate Java and Bedrock arena worlds.
- Optional datapack/functions for Java wave scheduling.
- Platform-specific resource packs for visual feedback.

### Risks
- Timed wave scheduling and mob lifecycle may need more event handling.
- Difficulty balance and performance require more testing.
- Still feasible with vanilla mobs and bounded spawn rules, but more sensitive to runtime differences than Candidate A.

## 5. Candidate C — Survival Expedition

### Player experience
The player travels through a small wilderness map, gathers a defined set of resources, crafts or activates a tool, survives environmental hazards and reaches a final camp.

### Minimum playable loop
1. Spawn with minimal supplies.
2. Explore a bounded route.
3. Gather a defined resource set.
4. Craft/activate a progression item.
5. Overcome one environmental obstacle.
6. Reach the final camp and complete the expedition.

### Required components
- Java mod and Bedrock add-on for one progression item and objective logic.
- Separate worlds with equivalent route and resource placement.
- Optional Java datapack and platform-specific resource packs.

### Risks
- Open-ended exploration makes objective completion less deterministic.
- Resource availability, world generation and player route variation increase test complexity.

## 6. Comparative assessment

| Criterion | Lost Temple | Outpost Defense | Survival Expedition |
|---|---|---|---|
| Clear short demo | High | High | Medium |
| Deterministic testing | High | Medium | Medium |
| World/map showcase | High | Medium | High |
| Mod/add-on relevance | High | High | High |
| Stable Bedrock feasibility | High, subject to component validation | High, subject to event validation | High, subject to progression validation |
| First-slice scope risk | Low–medium | Medium | Medium |
| Replayability | Medium | High | High |

## 7. Recommended minimum feature set for Candidate A

If the user selects The Lost Temple, the first implementation scope should be restricted to:
- One relic item type with three collectible instances or counters.
- One central seal/door interaction.
- Three compact rooms.
- One simple hostile encounter or hazard per room.
- One completion trigger and clear success message.
- One reset/replay path.
- One world/map per edition.
- Minimal custom resource assets only where needed.

No custom boss, complex NPC dialogue, procedural dungeon generation, economy, multiplayer, persistent cloud profile or advanced AI is required for the first slice.

## 8. Acceptance criteria

- Fresh world loads on the selected Java target and Bedrock target.
- Player can start the challenge without admin commands.
- All three relic fragments can be collected.
- The seal remains locked before all fragments are collected.
- The seal opens after all fragments are collected.
- The final room and completion trigger work.
- Reset/replay returns the world to a valid start state.
- No experimental Bedrock API is required.
- The Java and Bedrock implementations produce equivalent gameplay outcomes.
- Target-specific evidence includes game version, loader/API, environment and test steps.
- Any test not run is marked NOT_RUN; no unverified claim of playability.

## 9. Decisions required from the user

1. Select Candidate A — The Lost Temple, Candidate B — Outpost Defense, Candidate C — Survival Expedition, or describe a different idea.
2. If Candidate A is selected, confirm whether the relic/seal mechanic is acceptable as the central gameplay feature.
3. Confirm whether the first map should be a compact designed level rather than a procedurally generated world. Recommendation: compact designed level for deterministic testing.

## 10. Implementation boundary

This document is a gameplay design proposal only. It does not generate code, assets, maps or playable artifacts. The chosen loop must be added to the manifest, feature traceability matrix and acceptance tests after user confirmation.


## 11. User-selected direction — Zombie Invasion (2026-11-28)

The user selected **Zombie Invasion** and requested the most detailed treatment. This selection supersedes the three earlier candidate options in this document. The Lost Temple, Outpost Defense and Survival Expedition are no longer the active first-slice selection.

The authoritative gameplay design is now `docs/ZOMBIE_INVASION_GAMEPLAY_DESIGN_V1.md`. It defines the survival/scavenging/base-defence loop, staged attacks, zombie archetype roadmap, target-specific implementation boundaries, test strategy, expansion roadmap and unresolved decisions.

The first playable scope is a compact settlement with a safehouse, scavenging, limited repairs, a basic zombie archetype and three escalating attacks. Advanced survival, survivor NPCs, vehicles, complex special zombies and multiplayer remain later-stage systems unless the user explicitly promotes them into the first slice.
