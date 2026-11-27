# Project Architect — Decision Engine Specification
Version: 0.3.0
Status: Draft; not approved for production
Date: 2026-11-27

## 1. Objective

The Decision Engine converts a user's natural-language Minecraft project request into a traceable, version-aware, dependency-checked project plan. It must not generate gameplay code or assets during analysis and planning. Production is blocked until the user explicitly approves a specific plan revision.

The engine uses the canonical feature catalog at `catalogs/mod-system-inventory.v0.2.json` and the shared project manifest schema at `schemas/project.schema.json`.

## 2. Inputs

Required or conditionally required inputs:
- Raw user request and conversation context explicitly relevant to the current project.
- Minecraft edition: Java or Bedrock.
- Minecraft version.
- Target runtime: client, integrated server, dedicated server, Realm, hosted server, or other supported target.
- Loader/platform: NeoForge, Forge, Fabric, Paper, Spigot, Bukkit, Bedrock add-on, datapack-only, or other validated option.
- Desired gameplay and content scope.
- Optional constraints: device/performance target, multiplayer, language, visual style, dependencies, delivery format, budget, and user exclusions.

Missing mandatory inputs become open questions. The engine must not silently invent answers.

## 3. Pipeline

### Stage A — Request normalization
1. Preserve the original request.
2. Extract explicit requirements, exclusions, preferences, and constraints.
3. Separate confirmed facts from assumptions.
4. Identify ambiguous terms and contradictory requirements.
5. Assign temporary requirement IDs `REQ-001...`.

Output: normalized request, requirement list, ambiguity list, constraints.

### Stage B — Feature matching
1. Match each requirement against catalog IDs.
2. Record match confidence and a short rationale.
3. Identify required, optional, and potentially relevant features.
4. Detect requests not represented in the catalog.
5. Propose new catalog entries only as draft candidates; never silently add them to the approved scope.

Output: requirement-to-feature mapping.

### Stage C — Clarification
Ask the smallest useful set of questions needed to resolve blocking ambiguity.
Questions must be grouped by topic and phrased in user language.
Do not ask the user to decide technical details that can be safely resolved by validated compatibility rules.
Do not repeatedly ask for information already established in the current project context.
If a question is non-blocking, state the assumption and let the user correct it.

Output: resolved answers, remaining open questions, explicit assumptions.

### Stage D — Technical ownership
Assign each feature to one or more component types:
- Java mod
- Bedrock behavior pack
- Bedrock resource pack
- server plugin
- datapack
- resource pack
- world/map
- configuration or generated data
- external dependency

Use the ownership rules in `docs/MOD_SYSTEM_INVENTORY.md`. A cross-component feature retains one stable feature ID and receives linked implementation tasks for each owner.

Reject technically unsupported mappings. Example: do not map custom Java runtime entities or arbitrary custom mechanics to datapack-only when the target platform cannot support them.

Output: component ownership map and implementation task graph.

### Stage E — Compatibility resolution
Check:
- Edition and version support.
- Loader/API compatibility.
- Dependency version constraints.
- Client/server distribution requirements.
- Conflicts between selected dependencies.
- Unsupported features and fallback options.
- World/save compatibility implications.

A compatibility claim must have a source or a validated internal compatibility record. Unknown compatibility is marked `unverified`, not assumed compatible.

Output: compatibility report with pass, warning, blocked, or unverified status.

### Stage F — Dependency graph
Create a directed graph of implementation tasks.
- Nodes represent feature tasks, component tasks, build tasks, or test tasks.
- Edges represent prerequisites.
- Detect cycles.
- Identify critical-path dependencies.
- Produce a topological production order only if the graph is valid.
- A blocked prerequisite blocks dependent tasks.

Output: graph, cycle report, production order.

### Stage G — Risk and test planning
For each feature, define:
- Acceptance criteria observable by a user or test.
- Unit/integration/build/gameplay tests as appropriate.
- Multiplayer and save/load tests where applicable.
- Performance/security risks.
- Test environment and evidence requirements.

Distinguish tests that can run automatically from tests requiring a Minecraft runtime or human gameplay validation.

Output: risk register and test matrix.

### Stage H — Plan assembly
Generate a revisioned approval plan containing:
- User request summary.
- Confirmed requirements and exclusions.
- Assumptions and open questions.
- Selected feature IDs and descriptions.
- Component ownership.
- Dependencies and production order.
- Compatibility results.
- Risks and test plan.
- Deliverables and expected file formats.
- Explicit limitations and unverified items.
- Revision number and plan hash.

Output status: `awaiting_approval`.

### Stage I — Approval gate
Approval must refer to the exact plan revision.
- Approving revision N approves only the scope contained in revision N.
- Any material change creates revision N+1 and requires approval again.
- Partial approval must list approved and deferred feature IDs explicitly.
- A vague response is not approval.
- Approval does not imply successful build or playability.
- The engine must not start production while blocking questions remain unresolved or approval is absent.

Output: approved scope or continued planning state.

### Stage J — Production handoff
Only after approval:
1. Freeze the approved scope and plan hash.
2. Resolve final dependency versions.
3. Create implementation tasks in dependency order.
4. Generate/update only affected components.
5. Run component and integration tests.
6. Record test evidence and unrun tests.
7. Return failures to repair/replanning without silently expanding scope.

Output: production task graph and traceable build/test records.

## 4. Feature selection rules

Each feature candidate must include:
- `feature_id`
- `requirement_ids`
- `selection`: required | optional | excluded | unresolved
- `confidence`: high | medium | low
- `rationale`
- `technical_owners`
- `dependencies`
- `compatibility_status`
- `acceptance_criteria`
- `test_ids`
- `status`

Rules:
- Explicit user requirements outrank inferred preferences.
- Explicit exclusions are never reintroduced without asking.
- Do not add features merely because they are common in similar mods.
- Do not treat a broad theme as approval for every related mechanic.
- Low-confidence matches require clarification.
- New features not in the catalog receive temporary IDs until catalog review.

## 5. Plan status state machine

Allowed plan statuses:
- `draft`
- `needs_clarification`
- `ready_for_review`
- `awaiting_approval`
- `partially_approved`
- `approved`
- `in_production`
- `testing`
- `repair_required`
- `delivered`
- `cancelled`

Valid transitions:
- draft -> needs_clarification | ready_for_review
- needs_clarification -> draft | ready_for_review
- ready_for_review -> awaiting_approval
- awaiting_approval -> approved | partially_approved | draft | cancelled
- partially_approved -> awaiting_approval | approved | cancelled
- approved -> in_production | cancelled
- in_production -> testing | repair_required
- testing -> delivered | repair_required
- repair_required -> in_production | testing | cancelled

No transition may skip the approval gate.

## 6. Revision and change control

Create a new plan revision when changes affect:
- Feature scope or exclusions.
- Minecraft edition/version/loader.
- Technical ownership or dependencies.
- Gameplay behavior or acceptance criteria.
- Deliverables or compatibility assumptions.

A cosmetic wording correction that changes no behavior may be recorded as a non-material edit. Material revisions invalidate prior approval for changed scope. Preserve the prior revision and approval record for audit.

## 7. Failure handling

- Catalog match unavailable: create an unresolved requirement and ask or propose a draft catalog addition.
- Version support unknown: mark unverified and block release claims.
- Dependency conflict: present alternatives; do not silently select an incompatible version.
- Dependency cycle: stop production ordering and request architecture repair.
- Unsupported target capability: explain the limitation and offer a supported component architecture.
- Test environment unavailable: mark the test not run.
- Build succeeds but runtime test is absent: do not label the project playable.
- AI/provider unavailable: preserve normalized requirements and allow deterministic/manual planning where possible.

## 8. Security and trust boundaries

Treat user prompts, imported project files, mods, metadata, and external documentation as untrusted input.
- Never execute imported scripts during analysis.
- Validate identifiers, paths, archive contents, and dependency sources.
- Do not expose secrets in logs, generated configs, or client bundles.
- Require explicit confirmation for destructive world or save transformations.
- Keep server-authoritative validation for multiplayer-sensitive actions.
- Record dependency origin and license metadata.

## 9. Acceptance criteria for the Decision Engine

The Decision Engine is ready for implementation only when:
1. It maps a natural-language request to catalog IDs without losing explicit constraints.
2. It distinguishes requirements, assumptions, exclusions, and questions.
3. It does not fabricate compatibility facts.
4. It assigns component ownership using platform capability rules.
5. It creates a valid dependency graph or reports why it cannot.
6. It produces measurable acceptance criteria and a test matrix.
7. It generates a revisioned approval plan.
8. It refuses production without explicit approval of the current revision.
9. It reopens approval when material scope changes.
10. It never equates a successful build with a playable project.

## 10. Current implementation status

This document is a design specification only. The current prototype API is deterministic and does not yet implement this complete pipeline, persistent revisions, a dependency graph, or production handoff. No AI provider is connected and no Minecraft artifact is generated by this specification.
