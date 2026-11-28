# Zombie Invasion — Multiplayer Cooperation, PvP and Server Architecture Design V1

Status: DESIGN PROPOSAL — prepared for user review; not yet explicitly approved as a gameplay requirement.
Date: 2026-11-28
Target editions: Java 26.3 + Fabric; Bedrock 26.60 + stable APIs only. Exact multiplayer compatibility must be verified against the target release and server software.

## 1. Purpose and design principles

This document proposes optional multiplayer for Zombie Invasion while preserving a complete single-player experience.

Principles:
- Single-player remains playable without an internet connection or external account service, subject to the base game's own requirements.
- Multiplayer is opt-in and must not be required to access core survival progression.
- Co-op is the default recommended experience; PvP is configurable and off by default in the recommended profile.
- The authoritative world owner/server validates inventory, damage, claims, crafting, trade, quests and world events.
- Java and Bedrock are separate multiplayer compatibility targets. Native cross-edition play is not assumed.
- No feature is called multiplayer-ready until server-side behavior, persistence, security and edition-specific tests pass.

## 2. Multiplayer modes

### 2.1 Single-player
- Full intended survival loop remains available.
- The local world owner controls pause, save, difficulty and world settings.
- NPC and faction systems use the same gameplay rules, with bounded local simulation.

### 2.2 Invite-only co-op
- A player hosts a world and invites selected players through the platform's supported mechanisms.
- Host controls world settings, access and session lifecycle.
- Joining players receive explicit role/permission grants.
- If the host leaves, session behavior follows the selected host policy; no silent world ownership transfer.

### 2.3 LAN / local network
- Optional local-network sessions where the edition and server environment support them.
- No cloud account or public listing is required for private LAN play beyond platform requirements.

### 2.4 Dedicated server
- Long-term option for persistent worlds that can continue while individual players are offline.
- Requires server deployment, backups, admin tools, moderation, performance budgets and version-pinned content.
- Dedicated server operation is not part of the first playable milestone by default.

### 2.5 Public/community servers
- Optional future server discovery and community operation.
- Requires moderation, reporting, rules, anti-cheat/abuse controls and privacy policy.
- Public matchmaking or a global official server network is not assumed.

## 3. Co-op gameplay

Players can:
- Explore, scavenge, fight infected and complete quests together.
- Share or separately own inventory and equipment.
- Build and maintain a shared settlement.
- Assign base roles and NPC responsibilities.
- Operate vehicles and convoys together.
- Trade resources and exchange crafted items.
- Rescue survivors and negotiate with factions.
- Coordinate via in-game voice/text only if supported and separately approved; radio gameplay remains an in-world system and is not a replacement for platform voice chat.

Co-op rewards and progression must avoid duplicate reward exploitation. Quest rewards, loot containers and one-time discoveries need clear ownership/claim rules.

## 4. Player identity, roles and permissions

Suggested roles:
- World Owner: full world configuration, access, backup and moderation powers.
- Administrator: operational controls delegated by owner.
- Builder: construction and approved base modification.
- Member: ordinary survival participation.
- Guest: limited access.
- Temporary visitor: explicitly scoped and time-limited permissions.

Permissions are resource-scoped:
- Enter/use a claimed base.
- Open containers and storage.
- Build, break and repair blocks.
- Operate power/water/fuel infrastructure.
- Use vehicles and stations.
- Assign NPC tasks.
- Start research or settlement projects.
- Trade, invite or remove players.
- Change world settings and use moderation actions.

Default policy is deny-by-default for sensitive actions. Permissions must be enforced by the authoritative host/server, not merely hidden in the client UI.

## 5. Base claims, shared settlements and conflict

- Existing base-claim ownership model extends to player groups/settlements.
- A settlement can have an owner and an explicitly assigned member list/roles.
- Storage can be private, group-shared or public according to container permissions.
- Power, water, fuel and workshop networks follow access permissions and ownership.
- Members can be assigned work zones and responsibilities.
- Ownership transfer, member removal and settlement abandonment require explicit confirmation and audit events.
- Offline protection and raid rules are configurable. The recommended default prevents destructive offline PvP raids; PvE horde events may continue only under a fair, bounded and clearly disclosed world policy.
- Griefing protection must not make every block indestructible or bypass intended zombie damage.

## 6. PvP and player conflict

Recommended default: PvP disabled.
Possible server profiles:
- PvE co-op: players cannot damage each other; shared threats are zombies and world events.
- Consent PvP: combat is enabled only in designated zones or by mutual consent.
- Faction PvP: group hostility is explicit and configurable.
- Full PvP: optional high-risk server rule set, with clear warnings and anti-grief controls.

PvP must not be silently enabled by a quest or faction event. Safe zones, friendly fire, retaliation, loot-on-death and base damage rules are separate settings. Exact policy requires user approval.

## 7. Shared world state and simulation ownership

- One authoritative world state per session/server.
- Player actions are validated and committed once; clients receive replicated state.
- Inventory, loot, crafting, currency/barter, damage, injuries, water, power, fuel, vehicles, claims, faction relations and quest progress cannot be independently decided by clients.
- NPC simulation has one authoritative owner per world region; clients do not spawn duplicate NPCs.
- Encounter Director owns horde scheduling; server validates budgets and event lifecycle.
- Zombie AI remains responsible for individual infected behavior.
- Fire, disease, wildlife and other environmental events use the existing authoritative subsystem ownership.
- Shared state updates use stable IDs and idempotent event handling to prevent duplicate rewards, transactions or damage on reconnect.

## 8. NPCs, factions and player groups

- NPC recruitment and faction reputation are stored in shared world state.
- Party membership and NPC faction membership are distinct concepts.
- NPCs can be assigned to shared settlement roles only by players with permission.
- Dialogue reads the current speaker's relevant game state and does not expose another player's private inventory or personal data unless explicitly shared by gameplay.
- Faction diplomacy may be affected by group actions under a configurable attribution policy: individual, settlement, or both.
- Offline players do not retain control over NPCs or settlement tasks unless a dedicated server's explicit delegation rules allow it.

## 9. Death, revival and disconnect handling

- Existing death/restart policy remains unresolved and authoritative; multiplayer does not silently choose a death penalty.
- Candidate options include normal Minecraft respawn, limited recovery, teammate medical revival, or configurable hardcore rules.
- Teammate revival requires a valid state, item/tool and time window; it cannot erase injuries without the injury system's treatment rules.
- Disconnect during combat, transport, trade or crafting must resolve safely and prevent item duplication.
- Reconnect restores the player's authoritative inventory and location from the last committed state.
- Server shutdown and crash recovery must use atomic save/transaction boundaries where feasible.

## 10. Vehicles and convoys in multiplayer

- Vehicle control is server-authoritative and has one driver at a time.
- Passengers have defined seats and permissions.
- Convoy roles and NPC/driver automation use the existing transport design.
- Cargo, fuel and damage changes are committed by the server.
- Vehicle ownership, keys/access tokens and storage permissions are explicit.
- Vehicle collision and movement must be tested for latency, desynchronization and cross-edition differences.

## 11. Trade and economy integrity

- Every transaction is atomic: both sides' items/currency are validated before commit.
- Trade interfaces show offered and requested items and require confirmation from both parties.
- Disconnect, timeout or server failure cannot duplicate or destroy items through partial commits.
- Player shops and faction markets use finite inventories and existing economy rules.
- Currency remains an open design decision; barter can be the initial supported path.
- Duplication exploits, rapid transaction spam and automated farming must be tested.

## 12. Security, privacy and moderation

- Authenticate players through the edition/server's supported identity mechanism; never invent a custom credential scheme inside the mod.
- Server validates all privileged state changes.
- Rate-limit chat, invites, trade, claims and repeated interactions.
- Provide mute, block, kick, ban and report tools where server capabilities permit.
- Admin actions and sensitive ownership changes are auditable.
- Do not expose private player data, IP addresses or account identifiers through gameplay UI.
- Public/community servers need a separate moderation policy, retention policy and administrator guidance.
- Client-side anti-cheat alone is insufficient; server validation is required.

## 13. Versioning, compatibility and cross-edition boundary

- Java Fabric and Bedrock stable Script API have separate server adapters and capability matrices.
- A Java modded server and Bedrock world/server are not assumed to share a protocol.
- Cross-play between Java and Bedrock is a separate optional bridge project requiring security, feature parity and compatibility tests; it is not promised by this design.
- Server and client must agree on mod/add-on version, content manifest revision and required dependencies before joining.
- Incompatible clients receive a clear version mismatch message.
- Experimental Bedrock APIs remain disabled under the current decision.

## 14. Performance and persistence

- Server tick budget is explicit; entity, NPC, horde, fire, automation and network graph work is capped.
- Distant NPCs, wildlife and vehicles use bounded abstract simulation.
- Interest management sends only relevant state to each client.
- Large bases and player counts require profiling; no arbitrary player-count promise is made.
- Save checkpoints, world backups, restore procedures and crash recovery are required for persistent servers.
- World event IDs and transaction IDs prevent duplicate processing after reconnect/restart.

## 15. Acceptance criteria

1. Single-player remains fully usable without multiplayer services.
2. A private co-op session can be created and joined on each supported edition/server configuration.
3. Host/server is authoritative for inventory, crafting, damage, loot, trade and world state.
4. Permissions prevent unauthorized base, storage, vehicle and infrastructure access.
5. PvP follows the configured profile and defaults to disabled in the recommended profile.
6. Reconnect and crash recovery do not duplicate or silently lose committed inventory/transactions.
7. NPCs, hordes, fires and world events are not duplicated across clients.
8. Trade is atomic and resistant to disconnect duplication.
9. Vehicle seats, control and cargo remain synchronized under tested latency.
10. Server admin actions are permission-checked and auditable.
11. Version mismatches are detected before joining.
12. Java/Bedrock capabilities and any cross-play limitation are explicit and tested.

## 16. Open decisions requiring user review

- Approve multiplayer as a long-term feature or keep it as a future optional expansion.
- Preferred default: co-op PvE, PvP disabled (recommendation only).
- Hosting priority: invite-only host, LAN, dedicated server, public server.
- Whether players can join an existing world while host is offline.
- Whether group settlements and shared storage are enabled by default.
- Death/revival policy in co-op.
- Offline raid policy.
- Whether cross-edition bridging is desired despite its separate complexity.
- Maximum intended players per session/server; no number is assumed.
- Whether voice chat is in scope or only in-game radio/text.
- Whether public server discovery/community moderation is in scope.

## 17. First playable boundary

Multiplayer is not automatically part of the first playable vertical slice. The first slice remains a bounded single-player Java + Bedrock experience unless the user explicitly changes the milestone. Multiplayer should be scheduled only after the core shared gameplay loop, persistence, server authority and edition-specific compatibility are proven.
