# Zombie Invasion — Player Journey, Campaign Structure and Long-Term Progression Design V1

**Status:** Integrated long-term design proposal based on the user-approved survival, crafting, research, NPC, faction, world and economy scope. Specific campaign chapters, endings and progression values remain open. Not implemented.
**Date:** 2026-11-28
**Targets:** Java 26.3 + Fabric; Bedrock 26.60 + stable Script API 2.11.0; experimental Bedrock APIs disabled.

## 1. Purpose

This document defines how a player can enter the world, learn its systems, survive the early outbreak, establish a base, develop specialist capabilities, build relationships, explore the wider region and choose long-term goals. It connects existing combat, survival, crafting, injury, research, radio, economy, settlement, transport, ecology and world simulation designs into one progression structure.

It does not replace the sandbox. The campaign is an optional framework for direction and discovery; players must be able to continue surviving, building and exploring without following a single mandatory story path.

## 2. Progression pillars

- Survival competence: the player learns to manage immediate needs, injuries, threats and expeditions.
- Infrastructure independence: the player moves from scavenged supplies to reliable water, power, storage and production.
- Knowledge progression: documents, samples, observations and experts unlock validated blueprints and methods.
- Social progression: trust, reputation, recruitment, trade and faction relationships open or close opportunities.
- Geographic progression: new routes and regions become accessible through discovery, equipment, transport and security.
- Personal progression: skills improve practical efficiency without replacing tools, materials, workstations or treatment.
- World impact: settlements, routes, habitats and threat levels respond to recorded player decisions.
- Player-directed endgame: long-term goals are multiple and compatible with continued sandbox play.

## 3. Player journey stages

These are progression bands, not mandatory chapter lengths or a fixed number of in-game days.

### Stage A — Immediate survival
Focus: secure basic shelter, understand nearby threats, find food/water/medical supplies and establish a repeatable safe route.
Possible unlocks: basic crafting, simple repairs, scavenging knowledge, first aid, hand tools and rudimentary storage.
Failure pressure: exposure, injury, depleted supplies and unsafe night travel.
The player must have multiple recovery paths; one missed item must not permanently block progress.

### Stage B — Stable safehouse
Focus: reinforce an abandoned building, organize storage, establish basic water collection and create a defensible perimeter.
Possible unlocks: basic traps, barricades, rainwater collection, simple filters, cooking, basic work areas and a first survivor contact.
The player begins choosing between local safety, expedition range and resource investment.

### Stage C — Self-sufficiency
Focus: reliable food, clean water, repair capacity, renewable/backup power and specialist workstations.
Possible unlocks: farming, livestock where supported, water networks, battery storage, solar/wind, generator systems, sewing/backpack work, weapon workbench and vehicle repair.
The player must manage finite inputs, maintenance and network capacity. Infrastructure is not free or automatically reliable.

### Stage D — Community and regional influence
Focus: rescue and recruit survivors, assign professions, secure a settlement, establish trade and negotiate with factions.
Possible unlocks: settlement projects, guards/patrols, logistics tasks, faction contracts, regional market access, radio relays and convoy operations.
Community growth increases demand and creates new responsibilities; it is not a free passive bonus.

### Stage E — Advanced capability and exploration
Focus: access remote and dangerous regions, research advanced technologies, manufacture specialized equipment and operate larger transport.
Possible unlocks: laboratories, advanced medical treatment and prosthetics, complex electronics, factory manufacturing, buses/trucks/boats/trains/helicopters as separately validated content.
High-tier equipment requires real parts, specialist knowledge, suitable facilities and time.

### Stage F — World-shaping endgame
Focus: influence regional recovery, secure transport corridors, stabilize multiple settlements, uncover outbreak evidence, develop advanced infrastructure or pursue a personal sandbox ambition.
Possible objectives: restore a regional power/water network, create a protected trade corridor, establish a self-sustaining settlement network, recover critical research, evacuate or protect survivors, or clear a major threat zone.
These are candidate objective families, not a fixed approved ending list.

## 4. Multiple progression tracks

Progression is not one linear level bar. The player may advance several tracks at different rates:

| Track | Examples of progress | Does not grant automatically |
|---|---|---|
| Survival | cooking, water treatment, hunting, first aid | free supplies or immunity |
| Combat | melee/firearm handling, defensive tactics | unlimited ammunition or invulnerability |
| Engineering | repair, electrical, plumbing, vehicle systems | free components or bypassed workstations |
| Construction | building, reinforcement, maintenance | instant structure completion |
| Medical | first aid, diagnosis knowledge, advanced procedures | healing without valid treatment and inputs |
| Social | negotiation, leadership, trade | guaranteed faction obedience |
| Research | evidence analysis, prototypes, validated blueprints | finished equipment |
| Settlement | services, population, security, production | free NPC labor or infinite stock |
| Exploration | discovered routes, sites and maps | omniscient knowledge of undiscovered regions |

Skills should have readable effects and reasonable training routes. Basic actions remain possible without specialized skill levels unless a task genuinely requires expert qualification.

## 5. Unlock model and prerequisite graph

Every unlock is a typed record:
- Knowledge unlock: information, recipe or system understanding.
- Blueprint unlock: permission to attempt a defined design.
- Capability unlock: a supported action or workstation function.
- Access unlock: a door, region, facility, route or faction service becomes available.
- Relationship unlock: a new dialogue/trade/mission option based on recorded trust.
- World-state unlock: a site, settlement or event becomes available due to a valid world change.

An unlock can require one or more of:
- Discovery evidence or quest completion.
- Skill/qualification threshold.
- Physical materials and tools.
- Workstation/laboratory/factory tier.
- Power, water, clean-room or safety conditions.
- NPC expertise or faction access.
- Location-specific machinery or rare components.

The prerequisite graph must be acyclic for production unlock dependencies unless a deliberately designed alternative path resolves the cycle. A blueprint cannot depend on a component that can only be made from that same blueprint without another valid acquisition route.

## 6. Critical progression and soft-lock prevention

Critical paths require at least one viable fallback where practical:
- If a key NPC dies or leaves, critical knowledge must have another discoverable source or a recoverable alternative.
- If a facility is destroyed, the player must have a repair, relocation or alternate production path.
- If a rare component is consumed incorrectly, an alternate region, salvage source, trade route or research method should exist.
- If a faction becomes hostile, essential baseline survival should remain possible without its services.
- If the player misses a time-limited signal, the information should not permanently vanish unless that consequence is clearly communicated and noncritical.
- If a route is blocked, alternate routes or a meaningful route-repair objective should exist for required progression.

Optional high-tier content may be genuinely rare. Main survival continuity must not depend on a single unmarked random drop.

## 7. Quests, projects and player goals

The quest system supports:
- Main narrative and outbreak investigation.
- Survivor rescue and personal stories.
- Faction missions and diplomacy.
- Settlement construction and infrastructure projects.
- Research, sample collection and laboratory work.
- Exploration, maps and landmark discovery.
- Crafting, manufacturing and transport projects.
- Dynamic emergencies, defense and recovery.
- Player-created goals tracked through optional notes/checklists.

A settlement project is distinct from a quest: projects are persistent multi-step work plans with materials, labor, facilities and status. A quest can reference a project but does not own its construction or resource state.

## 8. Narrative structure and player freedom

Story delivery is distributed across radio, documents, environmental clues, NPC testimony, research and faction records. The player assembles evidence and may encounter contradictory accounts.

Main narrative milestones should:
- Be discoverable through more than one channel where practical.
- Avoid requiring one exact NPC to remain alive.
- Respect player-created world changes.
- Allow postponement while the player pursues survival or building.
- Record choices and consequences without secretly rewriting earlier facts.
- Avoid forcing a single moral answer when multiple reasonable choices exist.

The previously proposed three-night extraction scenario remains a proposal and is not adopted as the complete campaign structure by this document.

## 9. Player choice and consequences

Major choices may influence:
- Survivor trust, faction reputation and access.
- Which settlements survive, relocate or become abandoned.
- Which trade routes remain open.
- Research access and information credibility.
- Regional security and horde pressure.
- Allocation of scarce medicine, fuel, food and power.
- Whether infrastructure is centralized, shared or independently operated.

Consequences are stored as explicit events and world-state changes. Dialogue and quest text read those records; they cannot invent outcomes.

## 10. Endgame without a forced ending

The game should not end automatically when a main-story objective is completed. Candidate endgame directions include:
- Regional restoration: rebuild essential services and connect settlements.
- Community survival: maintain a network of safe settlements and supply routes.
- Research resolution: uncover and document the outbreak's origin and possible responses.
- Exploration: discover all major regions, facilities and hidden sites.
- Industrial independence: establish advanced production and transport.
- Personal sandbox: continue building, farming, collecting, trading and exploring indefinitely within world limits.

An ending or epilogue may acknowledge the player's achievements, but it should not delete the world or prevent continued play unless a separately approved mode explicitly does so.

## 11. Difficulty and pacing controls

Difficulty configuration should adjust pressure without changing the truth of resource accounting:
- Threat frequency, warning time and encounter budget.
- Resource abundance and loot distribution within bounded tables.
- Injury severity and recovery windows.
- NPC needs and settlement demand.
- Spoilage and environmental hazard rates.
- Research and manufacturing durations.
- Faction hostility and trade access.

Accessibility options may reduce repetitive management, improve warnings, expose network status and simplify nonessential UI interactions. Difficulty must not silently disable core player agency.

## 12. Rewards and progression economy

Rewards may include materials, tools, knowledge, blueprints, reputation, access, safe passage, maps, companions or project support. Rewards must respect source ownership:
- Item rewards are created through valid item transactions.
- Reputation changes through faction records.
- Knowledge/blueprints are committed by research/story services.
- NPC recruitment changes population and assignment state.
- Access rewards update permissions or route state.
- Project completion consumes reserved inputs and records the output.

Avoid quest rewards that flood the economy with scarce ammunition, fuel or advanced components. Reward variety should reinforce the player's chosen path.

## 13. Death, injury and recovery compatibility

This progression framework does not decide the unresolved death/restart policy. It must integrate with the existing injury and prosthetics specification:
- Injury state remains authoritative.
- Skills may improve valid treatment quality but cannot erase injury state.
- Amputation/prosthetic progression requires the designed components, expertise, facilities and installation process.
- NPC dialogue reflects actual recorded condition and knowledge.
- Death, respawn, item retention and world continuation follow a separately approved policy.

## 14. NPC and settlement progression

NPCs may contribute through profession, training, mentorship, research, production, medical care, logistics, defense and diplomacy. Contribution requires:
- A valid recruited/available NPC record.
- A suitable skill/qualification.
- Required tools, inputs and workstation.
- A safe and reachable work location.
- A task assignment and bounded time budget.

NPCs do not generate resources from nothing. If an NPC is injured, missing, frightened, hostile or occupied, the task result must reflect that state. Settlement growth increases food, water, shelter, sanitation, medical and security demand.

## 15. World simulation and progression synchronization

The campaign consumes authoritative world events:
- A route becomes known only after discovery or credible information.
- A site is restored only after base/infrastructure services commit the change.
- A research milestone completes only after its required analysis and validation.
- A faction alliance requires a committed diplomacy outcome.
- A region is safer only when threat/structure conditions support that conclusion.
- A settlement project completes only after required inputs and work are committed.

The quest service tracks objectives and rewards; it does not duplicate the underlying system's state.

## 16. Save persistence and campaign migration

Persist campaign chapter/quest state, evidence, choices, unlocks, skill progression, project records and associated event IDs. On migration, stable quest and objective IDs remain intact. Removed or changed content requires explicit migration rules; no silent reset of completed progress.

A save backup is required before migrations that change progression schema. Failed migrations must not leave a partially committed quest, reward or unlock.

## 17. Java/Bedrock parity

Both editions share:
- Progression track definitions and unlock intent.
- Stable IDs, prerequisites, quest outcomes and evidence rules.
- Player-facing objective text and critical-path alternatives.
- Save-state expectations and acceptance scenarios.

Each edition separately validates UI, interactions, persistence, scripting capability, NPC/quest integration and rewards. If one edition cannot provide the same interaction under the stable API constraints, document the limitation and propose an equivalent outcome before marking parity.

## 18. First playable boundary

The first playable remains the compact abandoned-town survival/defense vertical slice with its already approved features. The complete multi-stage player journey, advanced research, settlement network, high-tier production, regional restoration and multiple endgame paths are long-term scope.

The first playable does not need a full campaign, skill tree, branching endings, persistent regional economy or advanced NPC society to prove its core loop.

## 19. Acceptance criteria

1. The sandbox remains playable without following the main narrative.
2. Progression is multi-track and skill effects are explicit.
3. Unlocks have stable IDs, prerequisites and valid acquisition paths.
4. Critical progression has recovery/fallback routes and avoids accidental soft locks.
5. Quests read authoritative events and do not duplicate item, NPC, faction or world-state ownership.
6. Major choices create persistent, inspectable consequences.
7. Research unlocks knowledge/blueprints, not free finished goods.
8. NPC work requires real capability, inputs, tools, access and time.
9. Endgame objectives support continued world play.
10. Death/restart policy remains separately governed until approved.
11. Java and Bedrock independently pass progression and persistence tests.
12. First playable scope is not silently expanded.

## 20. Open decisions

- Exact chapter/act structure and whether the main story has a defined completion state.
- Final set of endings/epilogues, if any.
- Skill XP, caps, training and respec rules.
- Number and length of progression stages.
- Which unlocks are shared, faction-specific or region-specific.
- Quest expiry and failure behavior.
- Player-created project UI and objective tracking.
- Exact first-slice progression and rewards.
- Death/restart policy and persistent-world consequences.
- Edition-specific interaction and persistence feasibility.

## 21. Implementation boundary

This document is a design proposal and integration specification only. It does not implement quests, skills, campaign logic, NPC behavior, items, world files or playable artifacts. No runtime, save migration, balance or cross-edition test is claimed.
