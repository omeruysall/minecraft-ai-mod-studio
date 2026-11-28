# Economy & Trade Simulation Engine Specification

**Document status:** Design draft  
**Version:** 0.1  
**Implementation status:** Not implemented; design requirements only.  
**Approval status:** Awaiting product decisions and baseline approval.

## 1. Purpose
Define a configurable in-world economy and trade subsystem for Minecraft projects. It supports currencies, barter, shops, NPC vendors, crafting/service costs, settlement economies, supply and demand, player markets, rewards integration, and economic simulation. It must remain optional and compatible with the selected platform and project scope.

## 2. Ownership boundaries
- This engine owns economic rules, currency definitions, price calculation, trade offers, market state, and transaction orchestration.
- Inventory/item storage is owned by the platform adapter or designated inventory subsystem.
- NPC/Character Engine owns vendor identity, dialogue, personality, and schedules.
- Quest Engine owns objectives and quest progression; it requests and consumes economic events.
- World/Settlement systems own settlement location and population data.
- World Events/Ecology systems emit supply/demand and event signals.
- Combat/Encounter systems emit validated reward/drop facts but do not mint currency directly.
- Java/Bedrock/datapack adapters implement platform-specific storage and runtime behavior.

A single authoritative owner must exist for each balance, inventory, and transaction record.

## 3. Principles
- All balances and transactions are server-authoritative in multiplayer.
- Transactions are atomic, auditable, idempotent, and recoverable.
- No hidden currency creation, item duplication, or negative balance exploits.
- Prices and economic changes are explainable and configurable.
- Platform limitations and persistence guarantees are explicit.
- Economy is opt-in per project; no global real-money economy is implied.
- User approval is required before generated economic systems are produced.

## 4. Scope
In scope: currency definitions, wallets, barter, shops, NPC vendors, buy/sell offers, price rules, stock and restocking, supply/demand, settlement markets, services, fees/taxes, rewards integration, player trading, auction/market boards where supported, economic events, anti-exploit controls, persistence, admin tools, and analytics.

Out of scope: real-money payments, external cash-out, gambling, financial investment, unrestricted cross-server transfers, and a universal economy imposed on every generated world.

## 5. Economy configuration
A project economy declares enabled/disabled status, currency model, transaction types, item valuation rules, market scope, persistence, multiplayer model, admin permissions, and platform adapter. Multiple isolated economies may exist only if the project explicitly defines their boundaries and conversion rules.

## 6. Currency model
Currency may be item-based, scoreboard/variable-based, platform-specific wallet, or hybrid. Each currency defines stable ID, display name, symbol, precision, maximum balance, earn/spend rules, transferability, conversion policy, and persistence owner.

The system must define rounding, overflow, negative-balance prevention, deletion/retirement, and migration. No currency is assumed to be globally shared across worlds or servers.

## 7. Wallets and balances
Wallets define owner identity, currency balances, limits, access policy, and transaction history references. Balance changes occur only through validated transactions. Direct arbitrary balance mutation is prohibited outside controlled admin migration/repair flows with audit records.

## 8. Transaction lifecycle
A transaction includes stable ID, idempotency key, actor, source/destination, item/currency lines, quoted price, fees, preconditions, status, timestamps, and audit metadata. Lifecycle may include Proposed, Quoted, Authorized, Reserved, Committed, Rejected, Expired, Reversed, and Failed.

Use atomic commit or compensating rollback. Repeated requests with the same idempotency key must not duplicate effects. Partial failure must not leave currency debited without corresponding items or vice versa.

## 9. Trading and barter
Trade offers define items/currencies offered and requested, quantity limits, validity, eligibility, and acceptance rules. Barter must support explicit exchange ratios and item filters. Both parties must confirm the exact offer where required. Prevent item substitution, stale quotes, race conditions, and duplicated acceptance.

## 10. Shops and vendors
Shop definitions include owner, location, vendor reference, inventory source, buy/sell permissions, stock, restock rules, price policy, opening schedule, and interaction requirements. NPC vendors reference NPC identity and schedule rather than duplicating them. Shop UI and interaction behavior must be platform-aware.

## 11. Pricing and market models
Pricing may be fixed, tiered, formula-based, supply/demand adjusted, reputation-based, event-adjusted, or manually administered. Each rule exposes inputs, bounds, update cadence, rounding, and precedence. Prevent unbounded inflation/deflation and price oscillation. Show players the final price and meaningful modifiers before confirmation.

## 12. Supply, demand, and settlement economies
Optional simulation may use stock levels, production, consumption, trade flows, population, scarcity, and event effects. Define settlement boundaries, update cadence, stock ownership, unloaded-region behavior, and maximum price movement. Prefer aggregate/event-driven simulation over continuous per-NPC economic computation.

## 13. Stock, crafting, and services
Stock operations must be atomic and inventory-aware. Restocking declares source, interval, quantity, and ownership. Crafting/service costs declare required inputs, output, duration, interruption, and refund policy. Recipe execution is delegated to the platform/crafting adapter; this engine records economic costs and outcomes.

## 14. Fees, taxes, and sinks
Optional fees/taxes define payer, recipient, rate, caps, exemptions, timing, and visibility. Currency sinks may include services, repairs, travel, licenses, or custom project mechanics. No tax or fee may be silently introduced after approval. All deductions appear in the quote.

## 15. Player-to-player trade and markets
Player trade is optional. Define direct trade, listing/market board, auction-like mechanics if permitted, escrow, expiration, cancellation, dispute/admin recovery, and transfer limits. Market listings must not create an uncontrolled external economy. Any auction or chance-based feature requires separate product and policy review before inclusion.

## 16. Reputation and access
Reputation/standing may affect vendor access or prices, but the owning reputation/faction system must be explicit. Define source events, decay, bounds, visibility, reset, and appeal/admin correction. Do not infer real-world identity or behavior.

## 17. Rewards and progression integration
Quest, combat, and event systems emit reward eligibility facts. Economy engine validates and commits economic rewards. Reward grants are idempotent and linked to source event/quest IDs. Prevent duplicated rewards on reconnect, retries, server restart, or concurrent completion.

## 18. Multiplayer and persistence
Server authority validates balances, inventory movement, quotes, stock, and transactions. Define shared versus personal economy, party/group wallets, server boundaries, offline transactions, and reconnect behavior. Persist versioned wallet/market/transaction state with migrations and integrity checks.

## 19. Admin and moderation controls
Provide role-based controls for currency issuance/removal, transaction review, freezes, market suspension, refunds, and migration. Every privileged action requires reason, actor, timestamp, before/after state, and audit trail. Separate routine moderation from emergency repair.

## 20. Security and anti-exploit
Protect against duplication, replay, race conditions, forged client prices, negative balances, overflow, stale quotes, inventory desync, unauthorized transfers, and reward replay. Rate-limit requests, validate server-side, use idempotency keys, and isolate generated scripts. Do not expose secrets or allow unrestricted external payment/network actions.

## 21. Authoring UX
Provide currency editor, wallet/transaction rules, shop builder, offer editor, price-rule builder, market/settlement dashboard, trade permissions, economy preview, and transaction simulator. Conversational requirements must become a reviewable economic plan with examples, limits, exploit risks, and dependencies before approval.

## 22. Validation and testing
Validate currency IDs/precision/bounds, wallet ownership, transaction state transitions, idempotency, item/currency conservation, price formulas, stock constraints, permission rules, persistence migrations, and cross-system reward references. Runtime tests cover simultaneous trades, retries, crashes during commit, reconnect, stock contention, market updates, admin corrections, and multiplayer. Stress-test transaction volume and market size. Unrun tests are reported as not run.

## 23. Observability and recovery
Provide audit logs and diagnostics for quotes, authorization, reservations, commit/rollback, balance changes, stock movements, and reward handoffs. Sensitive data must be minimized. Recovery tools must reconcile ledger and inventory state, detect duplication, and require privileged approval for manual corrections.

## 24. Delivery
Depending on project scope: currency definitions, economy schemas/configuration, vendor/shop definitions, price rules, transaction adapter, migration scripts, admin controls, compatibility/dependency report, test evidence, and player-facing economy guide. Manifest identifies platform, game version, persistence owner, enabled markets, and dependencies.

## 25. Acceptance criteria
- Every balance has one authoritative owner.
- Transactions are atomic or recoverable and idempotent.
- Currency/item conservation is validated.
- Prices, fees, and modifiers are visible before confirmation.
- Multiplayer and persistence rules are explicit.
- Admin actions are auditable.
- Platform limitations are disclosed.
- No real-money payment or cash-out is implied.
- Tests cover concurrency, replay, crash recovery, and duplication.
- Approved economic changes require renewed approval when materially altered.

## 26. Open decisions
1. Is an economy included in the first release or optional module only?
2. Which Java loaders and Bedrock API versions are required?
3. Which currency models are supported initially: item, virtual, or hybrid?
4. Can a project define multiple currencies and exchange rates?
5. Are wallets personal, shared, settlement-based, or configurable?
6. Which persistence guarantees are mandatory?
7. Are NPC shops and vendor stock required at launch?
8. Which pricing models are first-release requirements?
9. Should supply/demand simulation be included initially?
10. What are maximum balance, transaction, and listing limits?
11. Is player-to-player trade in first-release scope?
12. Are public market boards/listings permitted?
13. Which escrow, cancellation, and dispute mechanisms are required?
14. Are fees/taxes part of the initial design?
15. Which reputation system owns vendor access and discounts?
16. How are combat, quest, and event rewards authorized and deduplicated?
17. What admin roles may mint, remove, freeze, or refund currency?
18. What audit retention and privacy rules apply?
19. Which anti-exploit tests define launch readiness?
20. Are cross-world or cross-server transfers allowed?
21. What economic telemetry is visible to project owners?
22. Which external libraries or platform plugins may be used?
23. What rollback and ledger reconciliation guarantees are required?
24. Which human playtests define a stable and understandable economy?

## 27. Current status
Design draft only. All open decisions remain unresolved until explicitly decided by the product owner. No code, wallet, currency, shop, transaction, or playable economy is implemented by this document.
