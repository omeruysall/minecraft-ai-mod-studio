# Zombie Invasion — First Map Design v1.0

**Status:** User-confirmed map direction; detailed layout proposal  
**Decision date:** 2026-11-28  
**Map concept:** Expandable abandoned town  
**First playable target:** One compact, authored town district; future expansion remains planned

## 1. Map vision

The first map is an abandoned town affected by a zombie outbreak. It should feel like a connected place with readable streets, meaningful landmarks, scavenging risk and a defensible safehouse. The town is designed to expand by adding districts later without invalidating the first playable area.

The initial map is authored and bounded, not an open-world procedural map. This keeps navigation, loot placement, spawn control, performance and cross-edition acceptance testing deterministic.

## 2. Confirmed direction and scope boundary

The user approved an abandoned, expandable town as the first map direction. Candidate landmarks include:
- Residential houses.
- Hospital.
- Police station.
- Market.
- Gas station.
- Military checkpoint.
- Underground shelter.

These are approved as the map's planned landmark vocabulary. Their exact inclusion in the first playable build is staged below; the first slice does not need every interior fully functional.

## 3. District layout

The town is organized into connected districts around a central safehouse.

### A. Safehouse district
- Main player start and return point.
- Primary defence objective.
- Storage and preparation area.
- Clearly visible entrances and fallback route.
- Protected spawn zone and reset anchor.

### B. Residential district
- Several compact house shells.
- Small fixed supply caches.
- Interior routes and limited cover.
- Environmental storytelling: barricaded doors, abandoned belongings and warning notes.

### C. Commercial district
- Market as a high-value food and general-supply location.
- Gas station as a utility/scavenging landmark.
- Exposed street approaches that create a risk/reward decision.

### D. Civic / medical district
- Hospital as a high-risk medical supply destination.
- Police station as a tactical supply and story location.
- Strong interior/exterior route distinction.

### E. Military perimeter
- Military checkpoint as a later-stage high-threat location.
- Barricades, observation position and environmental clues.
- Not required to be fully explorable in the first playable build.

### F. Underground shelter
- A distinct lower-level destination and future narrative/progression anchor.
- Access may be sealed or visibly blocked in the first slice.
- Later stages can use it for rescue, extraction, research or endgame objectives.

## 4. First playable map footprint

The first release should implement a compact subset:
- Safehouse district.
- A small residential block.
- One market or supply building.
- One connecting street/approach lane.
- One secondary route for the second/third attack.
- Clear boundary and return path.

Hospital, police station, gas station, military checkpoint and underground shelter may appear as simplified exterior landmarks, inaccessible shells or later-stage locked areas. The exact first-slice subset should be finalized against build effort and testability before map construction.

## 5. Spatial readability

- The safehouse must be visually distinguishable from all other buildings.
- Major landmarks use distinct silhouettes and signage.
- Streets and alleys should communicate likely zombie approach directions.
- Avoid visually identical routes that make navigation confusing.
- Use lighting and environmental landmarks rather than requiring a custom minimap.
- The player should be able to return to safety without relying on coordinates.

## 6. Routes and encounter lanes

The map should support at least two invasion approach lanes:
1. **Main street approach:** broad, visible route that teaches basic defence.
2. **Side-street / residential approach:** narrower route that tests a second perimeter position.

The Horde Director or deterministic wave tables must use controlled spawn zones outside the player's immediate view and outside protected safehouse volumes. Spawn points must never cause unavoidable contact damage.

Expedition routes should connect the safehouse to supply locations with different exposure levels. Do not place critical supplies behind an untested or inaccessible route.

## 7. Landmark gameplay roles

| Landmark | Primary role | First-slice status |
|---|---|---|
| Safehouse | Defence, preparation, restart | Required and functional |
| Residential houses | Basic scavenging and exploration | Small subset functional |
| Market | Food/general supply cache | One functional location recommended |
| Gas station | Utility supplies and future fuel system | Later or exterior landmark |
| Hospital | Medical supplies and rescue story | Later or simplified shell |
| Police station | Tactical supplies and outbreak clues | Later or simplified shell |
| Military checkpoint | High-risk loot and advanced encounters | Later |
| Underground shelter | Narrative/progression destination | Later / sealed landmark |

## 8. Loot placement policy

First-slice loot should be fixed and authored:
- A small, guaranteed supply set supports the tutorial/first attack.
- Optional supplies reward exploration.
- Critical items are never randomized into inaccessible containers.
- Each loot point has a stable identifier for tests.
- Containers must provide clear empty/looted feedback.

Seeded randomization may be added later, but not at the cost of reproducible acceptance tests.

## 9. Environmental storytelling

Storytelling is conveyed through the environment:
- Barricaded doors and broken windows.
- Emergency notices and evacuation markings.
- Abandoned supply carts and overturned furniture.
- Police/military warning signs.
- Damaged street lighting and blocked roads.
- Signs of residents attempting to reach the shelter.

No long cinematic or dialogue system is required for the first playable slice. Text clues should be short, optional and readable.

## 10. Construction and defence geometry

The first slice uses designated repair/reinforcement points at the safehouse:
- Main gate.
- One vulnerable window or side entrance.
- One secondary barricade point.

The map geometry must make these positions understandable and testable. Arbitrary destruction of every block is not required. Any later free-form construction must include bounds, block protection rules, repair costs and reset behaviour.

## 11. Cross-edition map parity

Java and Bedrock maps should preserve:
- Landmark purpose and relative navigation logic.
- Safehouse location and defence layout.
- Supply point identifiers and intended rewards.
- Attack lanes and protected spawn areas.
- Objective sequence and player route options.

Exact block palette, asset format, pack references and technical implementation may differ by edition. A parity checklist records functional equivalence rather than demanding identical internal files.

## 12. Performance and world bounds

- Keep the first map compact and avoid unnecessary entity-heavy decoration.
- Use a clear playable boundary.
- Limit active AI entities and avoid large numbers of ticking blocks.
- Prefer static environmental props where possible.
- Validate chunk loading, spawn regions and world reset on both target editions.
- Measure performance on identified test devices; do not infer performance from successful packaging.

## 13. Expansion plan

Future districts can be added in controlled stages:
1. Hospital and medical block.
2. Police station and civic block.
3. Gas station and outer road.
4. Military checkpoint and fortified perimeter.
5. Underground shelter and lower-level complex.
6. Additional residential/commercial blocks and connected outskirts.

Expansion must preserve existing player progress where the later persistence model supports it. New districts should connect through readable roads, gates or tunnels rather than arbitrary teleports.

## 14. Map acceptance criteria

### First playable
- Player spawns at the intended safehouse location.
- Safehouse is visually recognizable and reachable after exploration.
- At least one residential/supply route is navigable.
- At least one supply location can be looted.
- Two attack lanes are functional and validated.
- Spawn zones respect safehouse protection and minimum player distance.
- Defence points are accessible and interact as specified.
- Map boundaries prevent accidental escape from the test scenario.
- Reset restores the authored map state and loot state.
- Java and Bedrock each pass independent load and gameplay checks.

### Future map expansion
- Every new landmark has an explicit gameplay purpose.
- New routes do not break existing attack lanes or safehouse navigation.
- Added entities/blocks remain within target performance budgets.
- Cross-edition parity status is recorded per landmark.

## 15. Open map decisions

The user has approved the abandoned expandable town direction and the proposed landmark set. The following are still open:
1. Which additional landmark (market, hospital or police station) is fully functional in the first playable slice besides the safehouse.
2. Whether the first slice ends by surviving the third night or by activating an extraction objective.
3. Whether the map uses a fixed daylight/night cycle duration or phase-triggered time control.
4. Whether the military checkpoint and underground shelter are visible but locked, or omitted until later.

## 16. Implementation boundary

This document defines map design only. It does not create a world file, structures, terrain, loot containers, spawn markers or playable map. Application source code remains unchanged until the design baseline and implementation gate are approved.


## 17. User decision — all three core service buildings functional in first slice (2026-11-28)

The user selected **all three**: Market, Hospital and Police Station. Each must be a genuinely functional, explorable and testable gameplay location in the first playable map, not merely a decorative exterior.

### Required first-slice roles

**Market**
- Searchable supply containers.
- Food and general survival supplies.
- Clear looted/empty feedback.
- A risk/reward expedition route from the safehouse.

**Hospital**
- Searchable medical supply points.
- At least one usable recovery/medical item or interaction.
- A distinct, more exposed or encounter-prone route.
- Medical loot must be useful within the first-slice survival rules.

**Police Station**
- Searchable tactical supply points.
- First-slice combat/defence supplies compatible with the chosen vanilla-baseline combat scope.
- A distinct interior layout and defensible access points.
- Do not introduce firearm systems solely because the location is a police station; custom weapons remain a separate decision.

### Map scope impact

The first playable map must now include a functional safehouse, residential section, market, hospital and police station, plus two validated attack lanes. The first slice is larger than the earlier minimum map proposal. Keep each building compact and focused; do not expand into full-scale interiors or add unrelated systems.

Each building must have stable loot-point identifiers, accessible routes, clear interaction feedback and resettable state. The same gameplay role and intended supply value must be represented in both Java and Bedrock, with separate edition-specific implementations.

This decision closes the earlier open question about which one of the three buildings would be functional: all three are required.
