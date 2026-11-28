# Zombie Invasion — Injury, Amputation and Bionic Prosthetics Design V1

Status: USER-REQUESTED SYSTEM — detailed mechanics are design proposals pending balancing
Date: 2026-11-28

## 1. Purpose

Define a consequential injury system for the Zombie Invasion project. The system covers fractures, cracks, dislocations, sprains, bleeding, severe tissue damage, limb loss, prosthetic replacement and advanced bionic limbs. It must create meaningful survival decisions without making ordinary play arbitrarily punishing.

This is a design specification only. It does not implement gameplay or assert that any feature is available in-game.

## 2. Injury categories

The system should support distinct injury records rather than one generic health penalty:

- Bruises and blunt trauma.
- Cuts and lacerations.
- Bleeding with severity levels.
- Burns.
- Sprains and dislocations.
- Bone cracks and fractures.
- Severe crush injuries.
- Infection and wound complications, subject to later scope approval.
- Permanent limb loss in explicitly defined severe events.

Each injury definition must specify cause, severity, affected body region, gameplay effects, treatment pathway, duration or permanence, and recovery conditions.

## 3. Body-region model

Track at minimum: head, torso, left/right arm and left/right leg. Hand/forearm/upper-arm and foot/lower-leg/thigh distinctions may be introduced if they produce meaningful gameplay and are technically feasible on both editions.

Possible gameplay effects:
- Arm/hand injury: slower or less reliable weapon handling, reduced interaction capability, inability to use two-handed equipment while severe.
- Leg/foot injury: reduced movement speed, sprint restriction, impaired jumping.
- Torso injury: stamina/breathing penalty and vulnerability under severe trauma.
- Head injury: vision/aim or consciousness effects only if they can be implemented fairly and accessibly.

Effects must be bounded, clearly communicated and avoid input-locking the player without warning.

## 4. Severity and treatment

Proposed severity ladder:
1. Minor — temporary penalty, basic treatment.
2. Moderate — stronger penalty, treatment item and recovery time.
3. Severe — major functional impairment; advanced treatment and safe recovery location recommended.
4. Critical — life-threatening condition such as uncontrolled bleeding or catastrophic trauma.
5. Permanent — amputation/limb loss where the approved event rules permit it.

Treatment examples:
- Bandage and dressing for bleeding/cuts.
- Splint for selected fractures.
- Support/brace for sprains and dislocations.
- Medical kit for complex wounds.
- Antibiotics or advanced treatment only if infection mechanics are approved.
- Surgery/medical procedure for limb-loss recovery and prosthetic fitting.

Items must have distinct roles; one universal medkit must not instantly cure every condition.

## 5. Amputation and limb loss

Limb loss is a high-severity, long-term gameplay state, not a routine random punishment.

Requirements:
- Only explicitly authored, telegraphed or sufficiently justified severe events may cause permanent limb loss.
- The player receives clear warning and feedback where possible.
- A lost limb changes the relevant character capability and is recorded persistently.
- Immediate stabilization and later treatment are separate stages.
- The system must not silently remove a limb due to an ordinary low-damage hit or an unannounced random roll.
- Death/restart and world persistence interactions must follow a separately approved policy.

## 6. Prosthetic progression

Prosthetics are a multi-stage progression path. A bionic arm cannot be obtained as a single cheap recipe.

Suggested tiers:
- Basic temporary support/prosthesis: limited functionality and accessible materials.
- Mechanical prosthesis: crafted from scavenged mechanical components and fitted at a suitable station.
- Advanced bionic prosthesis: requires rare electronics, power components, precision parts, specialist tools and an advanced workshop.
- Specialized variants: utility, strength, precision or other balanced functions, only after core functionality is stable.

For a bionic arm, the staged path should include:
1. Stabilize the injury and survive.
2. Discover a prosthetics/engineering blueprint or unlock the recipe.
3. Scavenge required components from appropriate locations.
4. Recover or craft subassemblies (frame, joints, actuators, control unit, power module, connectors and casing).
5. Process/assemble parts at the correct advanced workstations.
6. Complete fitting/installation at a dedicated medical or prosthetics station.
7. Calibrate and test the limb.
8. Maintain, repair or recharge it according to its design.

The player must not be able to bypass the progression by placing all raw ingredients into the basic crafting grid.

## 7. Prosthetic gameplay contract

Each prosthesis must define:
- Supported limb and compatibility.
- Functional capabilities and limitations.
- Weight/encumbrance impact, if such a system is later approved.
- Durability/condition.
- Energy or fuel requirements, if applicable.
- Repair and maintenance recipes.
- Installation/removal rules.
- Visual model and animation requirements.
- Save/load persistence and migration behavior.

Prostheses must not grant unbalanced combat advantages by default. Any special strength, grip, tool use or weapon handling benefit must be offset by cost, power, maintenance or other explicit trade-offs.

## 8. Crafting and station dependencies

The first stage must retain the normal Minecraft Crafting Table as the entry-level crafting station. More advanced workstations are unlocked or constructed later through progression. The prosthetics path should depend on specialist stations rather than the basic table alone.

Potential station chain:
- Crafting Table: basic survival items, simple tools, basic components.
- Medical Workbench: dressings, splints and medical supplies.
- Sewing/Leatherworking Bench: straps, harnesses, fabric and bag components.
- Mechanical Workbench: frames, joints, gears and mechanical prosthesis parts.
- Electronics Bench: circuits, sensors, control modules and power systems.
- Advanced Engineering/Prosthetics Station: final assembly, fitting and calibration.

Exact station names, unlock conditions and recipes remain proposals pending full crafting design.

## 9. Fairness, accessibility and balance

- Injury events must be legible through UI, sound and/or status feedback.
- Critical injuries need a recoverable treatment path; avoid unavoidable death loops.
- Permanent limb loss must be rare, consequential and consistently governed.
- Provide difficulty/configuration controls if permanent injury proves too punitive.
- Keep visual injury representation non-graphic by default; gameplay clarity takes priority.
- The same logical injury outcomes must exist on Java and Bedrock, even if implementation differs.

## 10. Persistence and anti-exploit requirements

- Injury state and prosthesis ownership must persist correctly through save/reload.
- Dropping, swapping, death and restart must not duplicate or erase prostheses.
- Installation and removal must be transactional or recoverable.
- A failed installation must not consume all components without granting the result.
- Scenario reset must not silently alter unrelated player/world data.
- Data schema must be versioned for future injury types and prosthetic variants.

## 11. Acceptance tests

1. Each injury type applies only its documented effects.
2. Treatment items affect only compatible conditions.
3. Fractures and cracks remain distinct states if both are exposed to players.
4. Severe injury feedback is clear and timely.
5. Limb loss occurs only under approved, testable conditions.
6. A player can follow the full prosthetic progression from blueprint/scavenging to installation.
7. Basic Crafting Table cannot bypass advanced prosthetic stages.
8. Missing or incompatible components prevent installation without consuming valid inventory.
9. Installed prostheses persist across save/reload.
10. Repair, power and condition behavior match the item definition.
11. Java and Bedrock pass equivalent gameplay acceptance tests.
12. Any test not actually executed is marked NOT_RUN.

## 12. Open decisions

- Whether permanent limb loss is enabled in the first playable milestone or introduced in a later milestone.
- Whether injury affects only player characters or also NPCs.
- Exact body-region granularity and injury probabilities.
- Whether infection, pain, blood loss, stamina and temperature are separate simulated systems.
- Prosthetic tiers, special abilities, power source and maintenance cadence.
- Whether a dedicated surgery interaction is required.
- Difficulty settings and accessibility options.

## 13. Implementation boundary

Design only. No injury engine, medical items, prosthetics, animations, recipes or playable files have been implemented by this document.
