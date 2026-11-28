# Zombie Invasion — Death and Restart Policy v1.0

**Status:** Recommended first-slice policy — not user-confirmed  
**Date:** 2026-11-28  
**Scope:** Single-player first playable release, Java 26.3 + Fabric and Bedrock 26.60

## 1. Design goals

- Death must have a clear consequence.
- A failed attempt must be recoverable without rebuilding the world manually.
- Restart must not duplicate zombies, loot, objectives or scheduled attacks.
- The same player-facing rules must be implemented and tested independently in Java and Bedrock.
- No permanent campaign loss is introduced in the first slice.

## 2. Recommended first-slice rule

When the player dies during an active scenario:
1. Mark the current attempt as DEFEAT exactly once.
2. Stop new wave scheduling and safely end or clean up scenario-controlled hostile entities.
3. Freeze scenario progression and show a clear result message.
4. Preserve the world package and the player's ability to restart; do not delete the save.
5. Offer a full scenario restart from the defined starting state.
6. On restart, restore phase counters, objective flags, defence points, fixed loot state, radio progression, extraction state and scenario-managed entities.

This is a recommended default, not a confirmed user decision.

## 3. What restart resets

- Scenario phase and night/wave index.
- Active invasion schedule and pending spawn jobs.
- Scenario-controlled zombies and temporary encounter entities.
- Safehouse defence-point health/state.
- Fixed authored loot containers and their searched/empty flags.
- Mission/radio messages and objective completion flags.
- Extraction availability and completion trigger.
- Attempt-specific result counters.

## 4. What restart does not reset

- The installed mod/add-on or world package itself.
- User-created content outside the scenario's explicitly owned reset region.
- Global Minecraft settings or unrelated worlds.
- Any future persistent campaign data; such a system is out of first-slice scope.

## 5. Death handling details

- Death detection must be idempotent; repeated death events cannot create multiple result screens or reset jobs.
- If the edition's native death screen appears, the scenario must still reach a consistent DEFEAT state.
- Respawn must not accidentally continue the previous active wave.
- The player should return to a safe, deterministic restart location only after selecting restart.
- No automatic restart should erase the defeat feedback before the player can read it.

## 6. Cross-edition requirements

Java and Bedrock may use different event hooks and implementation structures, but must satisfy the same observable contract:
- One death produces one defeat result.
- No further wave is scheduled after defeat.
- Restart returns the scenario to the same baseline state.
- Repeated restart is safe.
- No experimental Bedrock APIs are required.

## 7. Acceptance tests

For each edition independently:
1. Die during preparation; verify a single defeat result and no attack starts afterward.
2. Die during an active wave; verify no new wave or stale spawn job remains.
3. Choose restart; verify the player returns to the scenario start and all owned state is reset.
4. Search a loot point, die, restart and verify the authored loot is restored.
5. Damage a defence point, die, restart and verify its baseline state.
6. Repeat restart at least three times; verify no duplicate zombies, containers, objectives or event handlers.
7. Reload the world after defeat and verify state remains recoverable.
8. Confirm unrelated world areas are not modified by the reset.

Any unexecuted target-runtime test is NOT_RUN.

## 8. Deferred decisions

- Limited lives or permanent-death campaign mode.
- Spectator/revive flow.
- Persistent inventory or partial resource retention after death.
- Automatic checkpoint resume.
- Campaign-wide save slots and meta-progression.

## 9. Approval boundary

This document records a recommendation only. The user has not yet explicitly approved the death/restart rule. Do not mark it as confirmed or implement it before the first-slice baseline approval.
