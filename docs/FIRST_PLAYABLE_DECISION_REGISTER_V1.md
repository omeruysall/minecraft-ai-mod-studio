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
