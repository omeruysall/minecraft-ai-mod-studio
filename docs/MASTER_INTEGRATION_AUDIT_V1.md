# Master Integration Audit v1.0

**Status:** Preliminary design audit | **Date:** 2026-11-28 | **Implementation:** Not performed
**Purpose:** Identify integration gaps between the current project foundation, feature catalog, manifest, API contracts and the expanded subsystem specifications before implementation begins.

## 1. Audit scope and evidence
This first-pass audit reads the current main-branch versions of:
- `docs/PRODUCT_REQUIREMENTS.md`
- `docs/ARCHITECTURE.md`
- `docs/DEVELOPMENT_PLAN.md`
- `docs/API_CONTRACT.md`
- `docs/PROJECT_ARCHITECT_DECISION_ENGINE.md`
- `docs/DESIGN_FIRST_DELIVERY_WORKFLOW.md`
- `docs/MOD_SYSTEM_INVENTORY.md`
- `catalogs/mod-system-inventory.v0.2.json`
- `schemas/project.schema.json` and `schemas/project.example.json`
- `docs/STUDIO_INTERFACE_AND_COMMUNITY_SPEC.md`
- AI conversation, provider management and Minecraft compatibility specifications.
- Production-engine specifications created for Java, Bedrock, datapacks, resource packs, maps/worlds, quests, NPCs, combat, environment interaction, events, ecology, economy, crafting, transportation, settlements, professions, achievements, multiplayer, modpacks, items, farming, survival, magic, structures, animation, sound, asset generation, publishing, security and backup/recovery.

This is a document-level design audit, not a codebase, dependency vulnerability, runtime or full test audit. A complete path-by-path traceability audit remains a required task.

## 2. Confirmed repository facts
- The feature catalog contains 232 feature records.
- All 232 catalog records currently have status `planned`.
- No duplicate feature IDs were found in the catalog.
- The inventory explicitly distinguishes planned, designed, approved, implemented, built and tested states.
- The project manifest schema is version `1.0.0` and has a narrow initial structure.
- The initial API contract covers health, plan creation, plan approval, project retrieval and follow-up messages.
- The development plan is an early milestone outline and does not yet sequence the complete set of newly specified engines.
- The product requirements correctly require explicit approval before production and distinguish build success from playability.

## 3. Critical integration findings

### 3.1 Catalog-to-specification traceability is incomplete
The catalog is still entirely `planned`. Detailed subsystem documents do not automatically change catalog records to `designed`. A stable mapping from catalog feature IDs to specification sections, component owners, dependencies and acceptance tests is required. Do not bulk-mark features designed based only on document titles.

### 3.2 Manifest schema is underspecified for the expanded product
The current schema supports a small set of boolean component flags and basic requirements/dependencies. It does not yet provide a complete normalized representation for component instances, stable identifiers, asset versions, dependency constraints, approval history, test evidence, build jobs, release records, collaboration permissions, provider references, backups or migration plans.

### 3.3 Workflow state model is not yet unified
The manifest schema has a small workflow enum, while the Project Architect specification defines a richer multi-stage process and the production engines define their own job states. Define separate but linked state machines for project planning, approval, component production, build/test jobs, asset review and release publication. Avoid one overloaded project status field.

### 3.4 API contract is far behind the design scope
The initial API contract does not yet define authentication/session, project revision concurrency, component CRUD, asset registry, provider configuration, generation jobs, cancellation, logs, dependency graph, validation, builds, tests, exports, publishing, updates, backups, restore, moderation or audit endpoints. The API must be redesigned around versioned resource contracts before coding those services.

### 3.5 Architecture needs explicit service ownership and boundaries
The architecture describes the Project Architect, manifest, dependency graph, generators, integration, workers and export engine, but does not yet allocate all newly designed capabilities to bounded services/modules, define data ownership, or specify synchronous versus asynchronous interactions. Add a service-boundary and ownership matrix.

### 3.6 Development plan does not cover the full target product
The existing milestone plan prioritizes a Java mod generator, then datapack/resource pack/world and other ecosystems. It does not yet incorporate the expanded asset, voice, multiplayer, economy, simulation, publishing, security, backup and community scope. Replace it with dependency-driven milestones rather than a flat feature list.

### 3.7 Security and approval boundaries must be enforced end-to-end
Approval must bind to an immutable plan revision and exact component/asset versions. Server-side authorization, isolated untrusted builds, secret handling, upload scanning, provider data disclosure and destructive-operation confirmation must be represented in contracts and tests, not left as prose-only guidance.

### 3.8 Test evidence requires a common model
All engines need a shared evidence vocabulary: not_run, passed, failed, blocked and skipped, plus test type, target matrix, toolchain version, artifact hash, timestamp and report reference. Build, load, runtime, multiplayer, performance and human playtest evidence must remain distinct.

## 4. Canonical cross-system architecture
Proposed high-level flow:
1. Experience layer: workspace, chat, live voice, project browser and community.
2. Project control plane: identity, authorization, Project Architect, requirements, approvals and project manifest.
3. Planning plane: compatibility resolver, component planner, dependency graph, impact analysis and execution planner.
4. AI gateway: provider registry, model capability routing, policy, budget and normalized task interface.
5. Production plane: domain engines for Java, Bedrock, datapack, resource pack, world, gameplay systems and media/assets.
6. Execution plane: isolated generation/build/test workers, queues, logs, cancellation and bounded repair.
7. Integration plane: identifier/reference validation, cross-component compatibility, package assembly and acceptance gates.
8. Data plane: project database, asset registry, object storage, version history, backups and audit records.
9. Distribution plane: exports, release catalog, update service, installation adapters and moderation.

These are logical boundaries. They do not mandate separate deployable microservices. Start with a modular monolith plus isolated workers unless scale, trust boundaries or deployment constraints justify service separation.

## 5. Canonical ownership rules
- Project Architect owns request interpretation, clarification, plan revisions and approval gating.
- Manifest service owns canonical project state and schema migration.
- Compatibility engine owns target support claims and evidence.
- Dependency graph owns component/asset relationships and impact traversal.
- Domain production engines own artifact-specific generation and validation.
- Asset pipeline owns asset briefs, asset versions, provenance and media conversion.
- Build/test workers execute untrusted workloads; they do not own project policy or approvals.
- Integration engine owns cross-artifact consistency and final acceptance aggregation.
- Publishing engine owns immutable release metadata and distribution lifecycle.
- Security/authorization policy is enforced by every service; it is not a standalone permission check UI.
- Backup/history service owns snapshot manifests and restore workflows, not live project mutations without confirmation.

## 6. Manifest v2 design requirements
The next manifest revision should include:
- `schema_version`, project identity, owner, collaborators and timestamps.
- Minecraft target matrix: edition, version, loader/platform, runtime, server/client role and compatibility evidence.
- Component records as objects with stable IDs, type, version, status, configuration, target and artifact references; avoid boolean-only component declarations.
- Requirement records with source, confidence, priority, status, acceptance criteria and traceability links.
- Dependency edges with kind, version constraints, optionality, ownership and cycle validation.
- Asset references pinned to exact asset versions and hashes.
- Revision-bound approvals with actor, scope, timestamp and decision.
- Production jobs, build/test evidence, warnings, known limitations and artifact hashes.
- Release and backup references without embedding large binary payloads.
- Explicit open decisions and unresolved assumptions.

Manifest v2 must be backward-migratable from 1.0.0 or provide a documented import path. Existing schema meanings must not be silently redefined.

## 7. Common resource and state contracts
Define shared contracts for Project, ProjectRevision, Requirement, Component, DependencyEdge, Asset, AssetVersion, Approval, Job, ValidationReport, TestEvidence, Artifact, Release, BackupSnapshot, ModerationCase and AuditEvent.

Each asynchronous job should expose a stable ID, type, owner/project scope, input revision, state, progress, cancellation semantics, timestamps, retry policy, structured logs, outputs and failure classification. Job state must not be conflated with project state.

## 8. Integration invariants
1. Every production artifact belongs to a project revision and component ID.
2. Every dependency resolves to a pinned compatible version or an explicit unresolved state.
3. Cross-component identifiers are declared once and referenced consistently.
4. Java and Bedrock compatibility domains remain separate unless a documented bridge exists.
5. No production job starts before the applicable plan revision is approved.
6. A changed requirement invalidates only affected decisions and dependent outputs where safe.
7. Approved artifacts are immutable; revisions create new versions.
8. No build worker receives secrets it does not need.
9. A successful build never implies load, runtime or gameplay success.
10. No world/server install, migration, publish or destructive restore occurs without explicit confirmation.
11. Unavailable or unexecuted checks are reported as `not_run` or `blocked`, not passed.
12. Every delivered package includes a manifest, compatibility declaration and evidence report.

## 9. Required integration test suites
- Manifest schema validation and migration tests.
- Catalog ID to specification and acceptance-test traceability.
- Revision concurrency and stale-approval rejection.
- Dependency graph cycle, missing-edge and version-conflict tests.
- Cross-component identifier and reference consistency.
- Java/Bedrock boundary enforcement.
- Asset provenance, hash integrity and version pinning.
- Queue idempotency, cancellation, retry and recovery.
- Isolated build worker security and resource-limit tests.
- End-to-end approval-to-delivery workflow.
- Backup/restore and release rollback tests.
- Authorization, tenant isolation and moderation audit tests.

## 10. Recommended implementation sequence
Phase 0 — Baseline: approve product scope, decisions, threat model, component ownership, manifest v2 and API v2.
Phase 1 — Control plane: identity, project persistence, revision history, requirement analysis, Project Architect and approval gate.
Phase 2 — Compatibility and graph: target resolver, catalog matching, dependency graph, impact analysis and validation reports.
Phase 3 — First vertical slice: one user-selected Java loader/version, minimal mod, resource assets, isolated build, load test and editable ZIP/JAR delivery.
Phase 4 — Data-driven vertical slice: datapack/resource pack generation and cross-component reference validation.
Phase 5 — World and Bedrock vertical slices: world generation/load validation, then Bedrock add-on path with its own compatibility tests.
Phase 6 — Shared production capabilities: asset pipeline, job orchestration, repair, preview, observability and backup.
Phase 7 — Advanced gameplay engines: add domain systems incrementally behind stable component contracts.
Phase 8 — Multiplayer/server, modpack resolver and deployment workflows.
Phase 9 — Publishing/community, updates, moderation and external distribution.
Phase 10 — Scale, performance, offline sync, additional providers and ecosystem expansion.

This sequence is a proposal. It requires user approval and a feasibility review before implementation.

## 11. Blocking decisions before coding
1. Approve the first vertical-slice target: Java/Bedrock, Minecraft version, loader and runtime.
2. Approve the initial role and permission matrix.
3. Approve manifest v2 component and revision model.
4. Approve API v2 resource and job contracts.
5. Choose local-first/cloud responsibilities and storage boundaries.
6. Choose initial AI provider routing and credential model.
7. Approve build sandbox and dependency repository policy.
8. Define first-release acceptance test matrix and playability evidence.
9. Set initial scope boundaries; full feature inventory is not the same as first-release commitment.

## 12. Audit conclusion
The project has broad subsystem design coverage, but it is not yet ready for full implementation. The most important remaining work is not adding more feature documents; it is converting the documents into traceable catalog mappings, a complete shared manifest, coherent API contracts, service ownership boundaries, security enforcement and a dependency-driven implementation baseline.

**No application source code was changed as part of this audit.**

## 13. Related documents
`docs/PRODUCT_REQUIREMENTS.md`, `docs/ARCHITECTURE.md`, `docs/API_CONTRACT.md`, `docs/DEVELOPMENT_PLAN.md`, `docs/MOD_SYSTEM_INVENTORY.md`, `catalogs/mod-system-inventory.v0.2.json`, `schemas/project.schema.json`, `docs/PROJECT_ARCHITECT_DECISION_ENGINE.md`, and all subsystem specifications.