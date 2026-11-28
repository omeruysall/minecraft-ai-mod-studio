# Minecraft AI Mod Studio — Master Development Roadmap v2.0

**Status:** Proposed roadmap | **Implementation status:** Not started from this roadmap | **Gate:** Design baseline approval required before application coding

## 1. Roadmap purpose

Convert the product and engine specifications into a dependency-aware delivery sequence. This roadmap is not a promise that every listed capability will ship in the first release. It defines the order in which architecture, vertical slices, platform coverage and advanced systems should be delivered and verified.

## 2. Delivery principles

- Finish and approve the design baseline before application coding begins.
- Build a playable vertical slice before attempting every engine in parallel.
- Preserve modular ownership; do not create one microservice per feature by default.
- Use a modular control-plane application with isolated generation/build/test workers as the initial deployment direction, subject to baseline approval.
- Make Java/Bedrock and loader/version compatibility explicit at planning time.
- Generate real source and playable artifacts; do not substitute mock outputs.
- Treat each phase as gated by evidence, not calendar dates.
- Keep the feature catalog as the source of feature IDs and update traceability status only with evidence.
- No production generation before exact-scope user approval.
- Expand scope only after the preceding slice is demonstrably stable.

## 3. Delivery tracks

1. Governance and design baseline.
2. Canonical project data and API contracts.
3. Identity, authorization, audit and persistence.
4. Conversation, requirements analysis and Project Architect.
5. Compatibility and dependency resolution.
6. Production engine adapters and artifact pipeline.
7. Build, test, integration and delivery.
8. Workspace UX, voice and project collaboration.
9. Publishing, community, moderation and updates.
10. Advanced simulation engines and broad platform coverage.
11. Reliability, performance, security and operations.

Tracks may overlap only when their interface contracts are stable and dependencies are satisfied.

## 4. Phase 0 — Design closure and baseline approval

**Goal:** Resolve contradictions and freeze a coherent first implementation baseline.

Work:
- Review Product Requirements, Architecture, Development Plan and all engine specifications.
- Reconcile Component Ownership Matrix, Manifest v2, API Contract v2, State Machine and Permission Matrix.
- Validate all 232 feature mappings and identify missing or duplicate ownership.
- Identify first playable vertical slice, supported target and explicit non-goals.
- Define acceptance criteria, threat model, migration policy and test evidence.
- Record unresolved decisions and obtain explicit user approval of the baseline.

Exit gate:
- Baseline document approved.
- First vertical slice scope and target are explicit.
- Every in-scope feature has owner, manifest representation, dependencies, acceptance criteria and tests.
- Out-of-scope features are retained in roadmap/catalog, not silently deleted.

No application source coding before this gate.

## 5. Phase 1 — Repository and engineering foundation

**Goal:** Establish reproducible development and safe change controls.

Work:
- Confirm repository layout and branch/PR strategy.
- Add automated formatting, linting, type checks and test orchestration.
- Define environment/configuration separation and secret handling.
- Define local development bootstrap and supported runtime versions.
- Establish CI artifact retention, provenance and dependency scanning.
- Add architecture decision record and API/schema change workflows.

Exit gate:
- Clean checkout can install, validate and run the agreed baseline services.
- CI produces reproducible, traceable results.
- Secrets are not committed and security scanning is active.

## 6. Phase 2 — Canonical data, persistence and API foundation

**Goal:** Make project state durable, revisioned and contract-driven.

Work:
- Implement Manifest Service against the approved v2 schema.
- Implement v1 validation and explicit v1-to-v2 migration.
- Implement canonical serialization/digest and optimistic concurrency.
- Add persistent project/revision/requirement/component/dependency records.
- Implement API Contract v2 for the first vertical slice.
- Add event envelope, idempotency and audit foundations.
- Implement schema and API contract tests.

Exit gate:
- Create/read/update/compare/commit project revision works.
- Migration preserves source and reports ambiguous data.
- Concurrent updates cannot silently overwrite.
- Approval-relevant digest is deterministic and tested.

## 7. Phase 3 — Identity, permissions and secure execution foundation

**Goal:** Establish trust boundaries before generation or deployment.

Work:
- Implement identity/session and scoped project membership.
- Implement authorization policy evaluation and server-side enforcement.
- Implement audit events and privileged-action confirmation.
- Create worker service identities and short-lived job-scoped credentials.
- Establish isolated build/test/generation sandbox.
- Implement secure artifact access, archive validation and secret redaction.

Exit gate:
- Positive/negative permission matrix tests pass.
- Workers cannot approve, publish, access unrelated projects or read provider secrets.
- Generated code and archives execute only in bounded environments.

## 8. Phase 4 — Conversation and Project Architect

**Goal:** Convert user intent into a clear, reviewable, revision-bound plan.

Work:
- Implement conversation sessions and requirement provenance.
- Implement structured clarification questions and blocking conditions.
- Connect AI Gateway through provider-neutral interfaces.
- Add provider/model capability registry, budget and credential references.
- Implement Project Architect plan revisions and component decomposition.
- Implement exact-revision approval and reapproval on scope change.
- Implement state machine transition guards and lifecycle events.

Exit gate:
- A natural-language request produces a structured plan and explicit questions.
- User can edit/review and approve a specific plan.
- No production job starts without valid approval.
- Provider failure does not fabricate a plan or successful result.

## 9. Phase 5 — Compatibility and dependency resolution

**Goal:** Prevent unsupported target combinations and component conflicts.

Work:
- Implement edition/version/loader target profiles.
- Implement supported-version capability records with source/evidence.
- Implement dependency graph, cycle detection and conflict reporting.
- Add target-specific component planning and install requirements.
- Implement impact analysis for changed requirements/components.

Exit gate:
- Unsupported combinations are blocked or clearly marked unresolved.
- Dependency conflicts are actionable and explainable.
- Component generation inputs are pinned to a target profile.

## 10. Phase 6 — First playable production vertical slice

**Goal:** Deliver one complete, genuinely playable project slice end-to-end.

Scope is selected during Phase 0. It should be deliberately narrow, such as one agreed Java loader/version or one Bedrock target, and a small set of compatible components.

Work:
- Implement one production engine end-to-end for the chosen target.
- Generate editable source files from structured component specifications.
- Build a real artifact using isolated workers.
- Add static validation, build test, loader/import test and runtime test.
- Integrate any required datapack/resource/world companion artifacts.
- Package output with checksums, source and installation instructions.
- Add repair loop for a bounded set of known failure classes.

Exit gate:
- Fresh environment can install/load the output.
- Required feature acceptance tests pass in the actual game/runtime.
- Source and binaries are both delivered.
- No demo/mock artifact is presented as a real build.
- All unrun tests are disclosed.

## 11. Phase 7 — Multi-component integration and asset pipeline

**Goal:** Make multiple engines produce compatible deliverables.

Work:
- Implement Asset Registry and immutable asset versions.
- Implement AI asset generation/conversion with provenance/license checks.
- Implement cross-component integration and reference validation.
- Add resource pack, datapack, world and second production engine as prioritized by approved scope.
- Add incremental regeneration from dependency impact analysis.
- Add full project export and clean-install verification.

Exit gate:
- A multi-component project is generated from one manifest revision.
- Shared assets and cross-component references resolve.
- Updating one component does not corrupt unrelated outputs.
- Final bundle contains editable source and runnable artifacts.

## 12. Phase 8 — Workspace UX, preview and voice

**Goal:** Provide the approved chat-centered creative workspace.

Work:
- Implement responsive workspace shell and project navigation.
- Implement center conversation and right-side hybrid project panel.
- Implement preview area tied to real project state.
- Implement text chat, then realtime voice session lifecycle.
- Add plan review, approval, generation progress and artifact inspection UX.
- Ensure mobile and desktop workflows are both usable.

Exit gate:
- UI actions map to authorized API operations.
- Preview clearly distinguishes generated, placeholder and unavailable content.
- Voice errors/fallbacks are explicit; text workflow remains complete.
- No UI-only status can impersonate server-side success.

## 13. Phase 9 — Collaboration and project operations

**Goal:** Support safe team workflows.

Work:
- Implement invitations, project roles and component-scoped grants.
- Implement reviewer/approver separation where approved.
- Implement comments, change requests and revision comparison.
- Implement backup snapshots, restore preview and project history.
- Implement conflict resolution and recovery workflows.

Exit gate:
- Multi-user edits are conflict-safe.
- Permission revocation takes effect.
- Restore is previewed, confirmed and audited.

## 14. Phase 10 — Publishing, community and distribution

**Goal:** Allow safe publication of selected project artifacts.

Work:
- Implement immutable releases and release notes.
- Implement public catalog listings and search.
- Support publishing map-only, mod-only, pack-only or full project as applicable.
- Implement licensing/attribution, content review, reports and moderation appeals.
- Implement update discovery, compatibility warnings and rollback plans.
- Implement explicit local/server installation adapters.

Exit gate:
- Public listings expose only selected artifacts.
- Release files are immutable and checksummed.
- Publishing and installation require separate permissions and confirmation.
- Moderation decisions are auditable and appealable.

## 15. Phase 11 — Domain engine expansion

**Goal:** Expand from the playable slice to the full catalog in dependency order.

Suggested order:
1. Items/equipment/loot and crafting/resource production.
2. NPC/character and combat/AI behavior.
3. Quest/story and world interaction.
4. Events, ecology and wildlife simulation.
5. Economy/trade and settlement/city management.
6. Farming/food and survival/needs.
7. Transportation/logistics/infrastructure.
8. Professions/progression and magic/technology.
9. Advanced structure generation, vehicles, automation and specialized systems.

The order is provisional. Dependency graph, user priorities, target support and technical risk determine actual sequencing. Each engine requires its own adapter, validation and playable acceptance evidence.

Exit gate per engine:
- Engine specification approved.
- Feature IDs mapped.
- Ownership and API contracts stable.
- Tests cover target runtime and integration.
- Real artifact is playable in the supported environment.

## 16. Phase 12 — Platform and ecosystem expansion

**Goal:** Expand supported platforms without claiming false cross-platform compatibility.

Work:
- Add additional Java loaders and supported Minecraft versions.
- Add Bedrock behavior/resource packs and Script API capabilities.
- Add server plugins and dedicated-server operations where supported.
- Add modpack assembly and dependency installation.
- Add platform-specific migration and compatibility matrices.

Exit gate:
- Each platform has independently tested adapters and release evidence.
- Unsupported feature parity is documented.
- Cross-edition compatibility is never implied without a real bridge and tests.

## 17. Phase 13 — Reliability, scale and operations

**Goal:** Harden the product for sustained real-world use.

Work:
- Performance profiling for large projects and worlds.
- Worker quotas, queue fairness, cancellation and retry policies.
- Backup/restore drills and disaster recovery.
- Security penetration testing and dependency supply-chain controls.
- Accessibility, localization and usability testing.
- Operational dashboards, alerting, support diagnostics and incident response.

Exit gate:
- Defined service-level targets are measured.
- Recovery drills meet agreed objectives.
- Critical security findings are closed or explicitly accepted.
- Large-project performance limits are documented.

## 18. Cross-phase quality gates

Every phase must provide:
- traceable feature IDs;
- approved scope and versioned contracts;
- unit, integration and negative tests as applicable;
- security and permission checks;
- build/runtime evidence appropriate to the feature;
- documented known limitations;
- migration and rollback considerations;
- user-visible completion report.

No phase is considered complete solely because code was committed or CI compiled.

## 19. Prioritization model

Rank work using:
- dependency criticality;
- user value and first playable outcome;
- compatibility breadth;
- security/privacy risk;
- implementation uncertainty;
- testability and evidence availability;
- maintenance burden.

Prefer a complete thin vertical slice over broad, shallow, disconnected features.

## 20. Roadmap governance

The roadmap is revised through versioned changes. A phase scope change updates dependencies, estimates, acceptance gates and affected feature IDs. The user approves material scope changes. Feature catalog statuses are updated only when implementation evidence exists.

## 21. Open decisions

The following decisions remain for the first playable milestone:
1. Exact Java version and mod loader.
2. Exact Bedrock version and API stability policy.
3. Shared gameplay feature family and acceptance loop.
4. Sequential or parallel development of the Java and Bedrock tracks.
5. Test devices and runtime environments for both editions.
6. Local/cloud/hybrid generation and build execution.
7. AI provider, privacy, budget and offline fallback policy.
8. First-slice identity and approval policy.

The platform and broad content scope are no longer open: both Java and Bedrock are selected, and the first bundle is mod/world with target-specific packs and data components as applicable.

Detailed register: `docs/FIRST_PLAYABLE_DECISION_REGISTER_V1.md`.
First playable scope: `docs/FIRST_PLAYABLE_VERTICAL_SLICE_SPEC_V1.md`.



## 22. Implementation boundary

This roadmap is a proposed sequence, not a delivery guarantee or evidence of implementation. Existing prototype functionality must be audited and either retained, replaced or migrated during the relevant phase. No application code changes are authorized by this document alone.


## 23. User-selected first playable scope update (2026-11-28)

The first playable milestone is now defined as **both Java Edition and Bedrock Edition**, with a **mod/world bundle**.

The milestone is split into two target-specific vertical slices sharing one product workflow and project manifest:

### 23.1 Java vertical slice
- Java mod.
- Playable Java world/map.
- Datapack.
- Resource pack.
- One exact Minecraft version and one loader to be selected before implementation.
- Produce editable source plus the appropriate runnable/distributable artifacts.

### 23.2 Bedrock vertical slice
- Behavior-pack/add-on implementation of the agreed gameplay feature.
- Playable Bedrock world/map.
- Resource pack.
- Script API use only when required and verified for the selected version.
- Produce editable source plus importable Bedrock package(s).

### 23.3 Shared workflow
Conversation → requirements → one shared project manifest → separate Java/Bedrock compatibility and dependency graphs → explicit scope approval → target-specific generation → integration → target-specific validation → separate playable bundles and a combined project export.

### 23.4 Revised phase sequencing
- Phase 0 must now define a cross-platform feature parity table and approve both target profiles.
- Phase 5 must resolve Java and Bedrock compatibility independently.
- Phase 6 becomes two vertical-slice tracks. They may be developed sequentially if the user approves the schedule, but both must pass their own playable acceptance gates before the milestone is declared complete.
- Phase 7 must verify shared intent and asset references without merging incompatible runtime artifacts.
- CI/test infrastructure must distinguish Java build/load/gameplay tests from Bedrock import/load/gameplay tests.

### 23.5 Scope guard
The first slice does not include all 232 catalog features. It includes a small, explicit set of gameplay requirements selected during design closure. Advanced simulation systems remain later phases unless required by that approved gameplay slice.

### 23.6 Remaining blockers
Exact Java version/loader, Bedrock version/API policy, common gameplay feature set, test environments, local/cloud execution and provider policy remain unresolved. No source-code implementation begins until these are resolved or explicitly deferred and the master baseline is approved.


## 24. User-approved platform baseline (2026-11-28)

The first playable milestone target profiles are confirmed:
- Java Edition 26.3 with Fabric.
- Bedrock Edition 26.60 with stable `@minecraft/server` 2.11.0 when scripting is required.
- Experimental Bedrock APIs disabled.

Phase 0 no longer needs to ask the user to select these versions/loaders/API stability settings. It must instead verify the official toolchain metadata and pin tested patch versions before implementation. The common gameplay feature set and test environment decisions remain open.
