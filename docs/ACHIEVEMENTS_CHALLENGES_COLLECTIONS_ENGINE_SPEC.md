# Achievements, Challenges & Collections Engine Specification

**Document status:** Design draft  
**Version:** 0.1  
**Implementation status:** Not implemented; design requirements only.  
**Approval status:** Awaiting product decisions and baseline approval.

## 1. Purpose
Define an extensible system for achievements, milestones, challenges, discovery records, collectible sets, journals, and completion tracking in generated Minecraft projects. It provides a consistent way to recognize player actions and authored goals while delegating quests, progression awards, inventory ownership, and economy transactions to their respective systems.

## 2. Ownership boundaries
- This engine owns achievement/challenge definitions, eligibility evaluation, completion records, collection catalogs, and presentation metadata.
- Quest Engine owns quest chains, objectives, and narrative progression.
- Progression Engine owns XP, levels, skill unlocks, and attribute changes.
- Economy Engine owns currency and item/currency transactions.
- Inventory adapter owns item possession and movement.
- World/Map Engine owns discovery locations and world geometry.
- Combat, Crafting, Ecology, Settlement, and Event engines emit validated gameplay facts.
- Platform adapters implement native advancements/achievements or custom runtime support.

No source system should grant the same reward independently. This engine records recognition and delegates reward delivery to the authoritative owner.

## 3. Principles
- Definitions and completion records are stable, versioned, and auditable.
- Completion is based on validated gameplay facts, not client claims.
- Repeated events cannot duplicate completion or rewards.
- Hidden content is optional and clearly governed by project settings.
- Accessibility and player privacy are respected.
- Native platform achievements are distinguished from project-specific achievements.
- User approval is required before generation and material changes.

## 4. Scope
In scope: achievements, milestones, challenge cards, daily/weekly or world-calendar challenges, exploration discoveries, collectible sets, bestiary/journal entries, completion statistics, leaderboards integration hooks, reward references, secrecy/hints, profile display, and admin tools.

Out of scope: real-money rewards, gambling/loot boxes, external account identity verification, and unmoderated public competitive ranking services.

## 5. Definition model
Each definition includes stable ID, namespace, title/description, category, icon/art reference, rarity/display grouping if used, eligibility conditions, trigger sources, progress model, completion policy, visibility, repeatability, expiration, reward references, platform support, version, and test cases.

## 6. Trigger and evidence model
Triggers consume typed events from owning systems: discovery, combat result, crafting completion, collection acquisition, settlement milestone, quest fact, event completion, or authored interaction. Every trigger declares source, validation authority, filters, aggregation, and deduplication key. Client-originated evidence must be verified server-side.

## 7. Progress models
Supported models may include boolean completion, counter, threshold, sequence, set completion, time-bound challenge, cumulative statistic, and mastery tier. Each model defines reset, decay, season/world scope, and offline behavior. Progress updates must be bounded and deterministic where required.

## 8. Completion and repeatability
Completion policy defines one-time, repeatable, seasonal, per-world, per-character, per-party, or account-like scope. This scope must be explicit and platform-feasible. Completion records are idempotent. Repeatable challenges create new instance IDs and cannot replay one-time rewards accidentally.

## 9. Challenges and schedules
Challenges may be authored, event-triggered, recurring, or milestone-driven. Define time source, eligibility, start/end, grace period, missed-window policy, progress persistence, and cancellation. Daily/weekly semantics must not assume real-world time unless explicitly selected. World-time challenges remain separate from real-time schedules.

## 10. Collections and discovery
Collections may group items, locations, creatures, structures, lore entries, recipes, or custom records. Define whether collection means discovered, crafted, owned, visited, scanned, or completed. Ownership-based collections must verify current or historical possession policy. Discovery records may be persistent even if the item/entity is later lost.

## 11. Bestiary, journal, and lore
Journal entries reference NPC, creature, location, quest, or world facts owned by other systems. Define unlock conditions, spoiler handling, localization, image/audio references, and whether entries persist across world resets. Do not duplicate canonical character or creature data.

## 12. Rewards integration
Rewards may reference XP, items, currency, titles, cosmetics, recipes, access, or quest progression. The owning system validates and delivers each reward. Reward grant uses a unique idempotency key tied to completion instance. Completion must remain recorded if reward delivery temporarily fails, with visible pending/recovery state.

## 13. Native achievements and advancements
Platform adapters may map project definitions to native Java advancements or Bedrock achievement-like mechanisms only where supported. Distinguish platform-owned achievements, server/project achievements, and client/account achievements. Never claim that a custom server advancement grants an official platform account achievement.

## 14. Profiles, privacy, and visibility
Define public/private/friends/party visibility, hidden achievement rules, profile sharing, export, and deletion behavior. Do not expose player identifiers or behavioral data unnecessarily. Public display requires explicit project configuration and appropriate moderation.

## 15. Multiplayer and party challenges
Define individual versus shared progress, party eligibility, contribution, join/leave behavior, late join, disconnect handling, and tie-breaking. Server authority validates progress. Prevent duplicate progress from event replay or multiple clients reporting the same action.

## 16. Leaderboards integration
Leaderboards are optional and owned by a separate ranking/service layer. This engine may emit verified score facts but must not create public rankings without an approved ranking policy. Define metric, tie-break, reset period, anti-cheat evidence, privacy, moderation, and retention.

## 17. User interface
Provide achievement catalog, progress view, challenge board, collection pages, discovery journal, completion summary, reward status, filters, and accessibility controls. Hidden entries may show a spoiler-safe silhouette or remain undisclosed according to project policy. Users should understand why progress did or did not count.

## 18. Authoring experience
Provide condition builder, progress model editor, schedule editor, collection catalog, reward reference selector, secrecy/hint controls, preview, and test simulator. Conversational requests become a structured definition with sample event traces, edge cases, reward ownership, and platform limitations before approval.

## 19. Persistence and migration
Persist definition versions, player progress, completion instances, challenge windows, collection evidence, and reward-delivery status. Define world-scoped versus player-scoped data, reset/import/export, and schema migration. Migrations must preserve legitimate completion and prevent replayed rewards.

## 20. Security and anti-cheat
Validate trigger evidence server-side. Protect against event spoofing, counter inflation, replay, client clock manipulation, duplicate collection claims, and leaderboard manipulation. Rate-limit progress events and audit privileged corrections. Generated scripts remain bounded and isolated.

## 21. Validation and testing
Validate IDs, trigger source references, progress model constraints, schedule semantics, scope, repeatability, reward ownership, localization, platform mapping, and migration integrity. Runtime tests cover trigger verification, progress increments, completion, repeat windows, party races, reward retry, reset, reconnect, and server restart. Human tests assess clarity, fairness, spoiler handling, and accessibility. Unrun tests are reported as not run.

## 22. Diagnostics and repair
Provide opt-in evidence trace, progress evaluation reason, completion state, reward handoff, schedule window, and migration history. Repair plans must preserve valid player progress and avoid reward duplication. Changes to eligibility, thresholds, repeatability, or rewards require renewed approval.

## 23. Delivery
Deliver achievement/challenge/collection definitions, schemas, localization and asset references, platform adapter artifacts, reward dependency report, migration data, compatibility report, test evidence, and user guide. Manifest records platform/version, progress scope, and reward dependencies.

## 24. Acceptance criteria
- Every definition has stable ID, trigger evidence, scope, and completion policy.
- Progress is validated by authoritative source systems.
- Repeatability and schedule semantics are explicit.
- Reward delivery is delegated and idempotent.
- Native and project-specific achievements are clearly distinguished.
- Privacy and visibility controls are explicit.
- Multiplayer progress cannot be duplicated through replay.
- Migrations preserve valid records without duplicate rewards.
- Tests cover completion, reset, concurrency, and recovery.
- Material changes to approved definitions require renewed approval.

## 25. Open decisions
1. Which platforms and versions are first-release targets?
2. Are achievements core or optional per project?
3. Which native advancement/achievement mappings are supported?
4. What progress scopes are supported: world, player, character, party, or server?
5. Are daily/weekly real-time challenges permitted or world-time only?
6. Which progress models are mandatory at launch?
7. Are hidden achievements and spoiler-safe hints required?
8. Which collection categories are included initially?
9. Is a bestiary/journal part of this engine or a separate UI module?
10. Which rewards can be referenced in the first release?
11. What happens when reward delivery fails after completion?
12. Are repeatable challenges supported at launch?
13. Which party/shared progress rules apply?
14. Are leaderboards in scope or deferred to a separate service?
15. What privacy defaults apply to profile and achievement visibility?
16. How are seasonal challenges reset and migrated?
17. What evidence is sufficient for exploration/discovery completion?
18. Which admin correction tools and audit retention are required?
19. What anti-cheat tests are release blockers?
20. Which localization and accessibility requirements are mandatory?
21. What export/import format is required for achievements and collections?
22. What happens to progress when a world is copied, reset, or transferred?
23. Which external platform APIs or libraries are allowed and under what license?
24. What human playtests define fair, understandable achievement pacing?

## 26. Current status
Design draft only. All open decisions remain unresolved until explicitly decided by the product owner. No source code, achievement catalog, challenge board, collection tracker, or playable progression feature is implemented by this document.
