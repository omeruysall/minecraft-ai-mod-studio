# Zombie Invasion — Radio, Communications, Research and Story Design V1

Status: User-approved system scope; detailed mechanics are design proposals. Not implemented.

## 1. Radio and communications
Radio is an exploration, warning, coordination and narrative system. Devices include handheld radios, vehicle radios, base receivers, antennas, repeaters and powered broadcast stations.
- Frequency scanning can discover distress calls, faction broadcasts, weather/emergency messages, rumours and story transmissions.
- Signal quality depends on device tier, antenna, terrain, distance, interference, power and weather only where the simulation can support it.
- Two-way contact requires a known/available endpoint and valid signal; radio is not global omniscient chat.
- Messages may reveal locations, requests, threats, trade opportunities or false information. Reliability/source should be legible.
- Power loss, damaged antennas and depleted batteries affect operation.

## 2. Research and laboratories
Research unlocks knowledge, recipes, treatment methods and advanced equipment. Inputs include documents, samples, components, tools, qualified NPCs and appropriate workstations.
- Research is staged: discovery, analysis, prototype, validation and production unlock.
- Research must not instantly grant a finished item; it unlocks a documented blueprint or capability.
- Laboratory types may include medical/biological, engineering/electronics and materials testing.
- Dangerous outbreak research occurs in designated locations and may trigger controlled hazards only under explicit rules.
- Sample handling and storage use inventory/quest state; no arbitrary hidden item consumption.

## 3. Story and outbreak mystery
The main narrative is built from discoverable evidence: radio logs, letters, reports, lab records, environmental clues, survivor testimony and faction accounts. Clues can conflict; the player assembles a timeline and evaluates credibility. Story milestones should not force a single play style or invalidate sandbox survival.

## 4. Quest architecture
Quest types include main story, faction, survivor rescue, settlement projects, exploration, crafting/research, emergency response and dynamic world events. Each quest has stable ID, prerequisites, objectives, progress source, rewards, failure/expiry rules and state. The quest engine reads system events; it does not own combat, inventory or NPC simulation.

## 5. Player agency and endings
Major choices may affect faction relations, settlement survival, access to research and extraction possibilities. Multiple outcomes are a design direction, not a committed ending list. The previously proposed three-night extraction scenario remains unapproved unless separately confirmed.

## 6. Acceptance criteria
1. Radio discoveries require a valid device, power/battery and signal conditions.
2. Transmissions have identifiable source and reliability metadata.
3. Research consumes defined resources and yields blueprints/knowledge, not fabricated finished goods.
4. Story evidence is persistent and discoverable through more than one route where practical.
5. Quests consume authoritative events from their owning systems.
6. Main story does not force every optional system or invalidate free survival.
7. Narrative choices update recorded world/faction state.

## 7. Open decisions
Exact frequency model, signal simulation fidelity, research time, laboratory tiers, sample catalog, main-story chapter structure, ending count and voice/audio requirements remain open.
