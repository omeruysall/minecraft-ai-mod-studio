# Minecraft AI Mod Studio — Master Design Baseline v1.0

**Baseline status:** Candidate — awaiting explicit user approval  
**Implementation status:** Not implemented by this baseline  
**Coding gate:** CLOSED until this baseline is reviewed, open decisions are resolved or explicitly deferred, and the user approves the first implementation scope.

## 1. Purpose

This document consolidates the current product, architecture, interface, manifest, API, engine, security, lifecycle and delivery designs into one reviewable baseline. It is the proposed authority for deciding when design work is sufficiently coherent to begin application implementation.

This baseline does not claim that all planned engines or features are implemented, nor does it approve all 232 catalog entries for the first release.

## 2. Product definition

Minecraft AI Mod Studio is a guided, conversational creation environment. A user describes a Minecraft project through text or live voice. The system interprets intent, asks clarifying questions, creates a structured project plan, presents components and dependencies for review, obtains explicit approval, generates compatible source/artifacts, validates them and delivers playable outputs with editable sources.

The product supports Java and Bedrock ecosystems, multiple component types and mixed deliverables where technically valid. The platform must clearly distinguish supported, unsupported, unresolved and not-yet-implemented capabilities.

## 3. Approved product direction captured so far

The following decisions have been explicitly selected in prior design work:
- Product scope: all major Minecraft content categories are within the long-term product vision.
- Platform ambition: Java and Bedrock, with platform-specific capability boundaries.
- World generation strategy: hybrid prepared-world plus procedural approach.
- AI workflow: guided, conversational, approval-first.
- Delivery intent: both playable artifacts and editable source.
- Interface theme: hybrid.
- Main layout: workspace.
- AI communication: text plus live voice.
- Main preview area: enabled.
- Right-side project panel: hybrid AI-suggested and user-controlled behavior.
- Community publication may expose a map-only artifact, a single component or a complete project; full-project publication is not mandatory.
- The complete project is governed by a shared manifest/specification and dependency graph.
- Design-first workflow: documentation and GitHub design artifacts are completed before application coding.

These decisions establish product direction. They do not resolve the first-release target, exact loader/version or first vertical-slice component set.

## 4. Core architecture baseline

### 4.1 Logical ownership

One authoritative owner exists for each canonical entity and state. Logical module boundaries are independent of deployment topology. Initial implementation should favor a modular control-plane application and isolated generation/build/test workers, unless the approved architecture decision records a justified alternative.

Reference: `docs/COMPONENT_OWNERSHIP_MATRIX_V1.md`.

### 4.2 Project data

The Project Manifest v2 is the canonical revisioned project contract. It contains project identity, targets, workflow summary, requirements, components, dependency graph, asset references, generation references, approvals, validation evidence, deliverables, collaboration references and extensions.

V1 remains immutable and valid. Migration to v2 is explicit and must not invent missing values or treat a legacy approval flag as a valid revision-bound approval.

References:
- `docs/PROJECT_MANIFEST_V2_DESIGN.md`
- `schemas/project-manifest.v2.schema.json`
- `schemas/project-manifest.v2.example.json`
- Existing `schemas/project.schema.json` remains v1.0.0.

### 4.3 Planning and approval

Project Architect owns requirement-to-plan orchestration and approval gating. Production starts only after Approval Manager confirms that the approval matches the exact manifest revision digest and plan/scope digest. Scope-changing edits require a new plan and renewed approval.

Reference: `docs/PROJECT_ARCHITECT_DECISION_ENGINE.md`.

### 4.4 API and events

API Contract v2 is the proposed logical API boundary. Events are versioned, idempotent and carry project/revision/correlation context. Existing prototype endpoints do not imply that the v2 API is implemented.

Reference: `docs/API_CONTRACT_V2_DESIGN.md`.

### 4.5 State lifecycle

Project, component, job, validation, release and moderation lifecycles are separate. No worker result may mutate a newer revision. Build success is not equivalent to runtime or gameplay success.

Reference: `docs/UNIFIED_PROJECT_STATE_MACHINE_V1.md`.

### 4.6 Security

Authorization is deny-by-default, resource-scoped and enforced server-side. Project editing, approval, publishing, installation, restore, provider credentials and platform administration are distinct permissions. AI agents and workers are least-privileged principals.

Reference: `docs/SECURITY_PERMISSION_MATRIX_V1.md`.

## 5. Production engine portfolio

The product design portfolio includes dedicated specifications for:
- Java mods;
- Bedrock add-ons;
- datapacks;
- resource packs;
- maps/worlds and structures;
- quests and narrative;
- NPCs and characters;
- combat and AI behavior;
- world interaction/environment behavior;
- dynamic events and simulation;
- ecology and wildlife;
- economy and trade;
- crafting and resource production;
- transportation, logistics and infrastructure;
- asset generation;
- publishing, versioning and updates;
- security, permissions and moderation;
- backup, recovery and project history.

Additional domain systems in the feature inventory include player progression, items/equipment/loot, settlement/city management, farming/food, survival/needs, magic/technology, multiplayer/server operations and studio UX. Their specifications and exact first-release inclusion must be tracked through the feature catalog and roadmap.

A specification is a design artifact, not proof of a working engine.

## 6. Feature traceability baseline

The source inventory contains 232 stable feature records. The traceability matrix preserves all 232 IDs and proposes a logical owner, primary specification, manifest component category and required traceability links.

Current evidence:
- Source inventory records: 232.
- Source statuses: 232 planned.
- Traceability matrix records: 232.
- Unique feature IDs in matrix: 232.
- Proposed owner/spec mapping: requires review.
- Implemented/built/tested status inferred from documentation: none.

References:
- `catalogs/mod-system-inventory.v0.2.json`
- `catalogs/feature-traceability-matrix.v1.json`

A feature may be marked designed, approved, implemented, built or tested only when the corresponding evidence and approvals exist. Documentation presence alone does not advance implementation status.

## 7. User experience baseline

The target workspace is Minecraft-friendly and chat-centered:
- Hamburger navigation at the top-left.
- Central conversation workspace.
- Right-side project/request panel with hybrid AI and user control.
- Project preview area.
- Profile/account access at the top-right.
- Project, discovery and publishing navigation.
- Responsive mobile and desktop behavior.
- Text-first functionality remains available if voice is unavailable.

The interface must accurately distinguish real outputs from placeholders and unavailable features. It cannot claim that a generation, build or test succeeded based only on client-side state.

References:
- `docs/STUDIO_INTERFACE_AND_COMMUNITY_SPEC.md`
- `docs/NAVIGATION_AND_PROJECTS_WORKSPACE_SPEC.md`
- `docs/PROJECTS_WORKSPACE_SPEC.md`
- `docs/PROJECT_DETAIL_WORKSPACE_INTERACTIONS_SPEC.md`
- `docs/AI_CONVERSATION_AND_REQUIREMENTS_ANALYSIS_SPEC.md`
- `docs/REALTIME_VOICE_COMMUNICATION_SPEC.md`

## 8. Delivery and quality baseline

A complete project delivery should include the relevant playable artifact(s), editable source, checksums, dependency/install information, target compatibility declaration, test evidence and known limitations.

Validation evidence distinguishes:
- schema/static validation;
- source/build success;
- loader/import/startup;
- world or pack load;
- runtime behavior;
- multiplayer behavior;
- performance;
- human gameplay acceptance.

Unrun tests are explicitly marked not_run. No result is fabricated. Release publication is separate from private project delivery.

References:
- `docs/PUBLISHING_VERSIONING_UPDATE_ENGINE_SPEC.md`
- `docs/BACKUP_RECOVERY_PROJECT_HISTORY_SPEC.md`
- engine-specific production specifications.

## 9. Development sequence baseline

The proposed implementation sequence is:
1. Design closure and explicit baseline approval.
2. Repository/CI engineering foundation.
3. Manifest v2, persistence, migration and API foundation.
4. Identity, authorization, audit and isolated execution.
5. Conversation, requirements analysis, Project Architect and approval.
6. Compatibility and dependency resolution.
7. One narrow but complete playable vertical slice.
8. Asset pipeline and multi-component integration.
9. Workspace UI and realtime voice.
10. Collaboration, backup and recovery.
11. Publishing, community, moderation and updates.
12. Domain-engine expansion and platform coverage.
13. Reliability, performance and operational hardening.

The first playable target and exact component scope remain open until the user selects them.

Reference: `docs/MASTER_DEVELOPMENT_ROADMAP_V2.md`.

## 10. Mandatory implementation gates

Application coding may begin only after:
- The user explicitly approves this baseline or a superseding revision.
- First vertical-slice target, loader/runtime and Minecraft version are selected.
- First vertical-slice features and explicit non-goals are listed.
- Feature traceability mapping is reviewed for the selected scope.
- Manifest and API contracts are reconciled.
- Security/permission decisions required for the slice are resolved.
- Acceptance criteria and test environment are defined.
- Repository/CI and development environment requirements are agreed.

Approval of this baseline does not authorize every catalog feature for immediate implementation. Scope is approved phase by phase.

## 11. Open decisions blocking first implementation

1. First playable vertical slice: which experience and which component combination?
2. First target: Java or Bedrock?
3. If Java: exact Minecraft version and loader?
4. If Bedrock: exact target version and supported APIs?
5. First execution model: local-first, cloud-assisted or hybrid for the initial slice?
6. First AI provider strategy and minimum provider-independent capability?
7. Initial authentication and local/offline identity behavior?
8. Which role can approve a plan in a single-user project and in a team project?
9. Which validation gates are mandatory for the first deliverable?
10. Which first-release community/publishing capabilities are deferred?

These questions must be resolved or explicitly deferred with documented consequences before implementation of affected areas.

## 12. Known limitations and risks

- The repository contains an incomplete prototype; it is not the complete product described by this baseline.
- The prototype's deterministic analyzer is not a full LLM-backed requirements engine.
- In-memory project storage is not production persistence.
- An approval endpoint that changes a status is not a complete revision-bound approval system.
- No complete playable mod/add-on/world generation capability is implied by the current prototype.
- Broad multi-engine and multi-platform scope creates significant integration and test burden.
- Minecraft version and loader changes can invalidate generated code and assets; compatibility data must be evidence-based.
- AI-generated code/assets require sandboxing, provenance, licensing review and validation.
- First-release scope must remain deliberately narrow to avoid a non-playable breadth-first implementation.

## 13. Baseline acceptance checklist

- [ ] Product scope and non-goals for first slice approved.
- [ ] Component ownership boundaries approved.
- [ ] Manifest v2 contract and migration policy approved.
- [ ] API v2 contract reconciled with manifest and state machine.
- [ ] Feature traceability reviewed for first slice.
- [ ] State machine transitions and approval guards approved.
- [ ] Security/permission policy for first slice approved.
- [ ] Compatibility target and dependency constraints selected.
- [ ] Build/test/runtime acceptance environment defined.
- [ ] Delivery format and evidence requirements agreed.
- [ ] Roadmap phase gates accepted.
- [ ] User explicitly approves this baseline revision.

## 14. Change control

Any material change to target platforms, approval semantics, manifest core model, ownership boundaries, permission model or first-release scope requires a baseline revision. Changes must identify impacted specifications, schemas, API contracts, feature IDs, tests and migration consequences.

## 15. Approval record

**Current decision:** PENDING USER APPROVAL.

No approval actor, timestamp or approval digest is pre-filled. Approval must be recorded through the designated workflow and must bind to the exact baseline revision/digest.

## 16. Implementation boundary

This document consolidates proposed design decisions and records open issues. It does not create backend functionality, production engines, user-interface behavior, database migrations or working game artifacts.
