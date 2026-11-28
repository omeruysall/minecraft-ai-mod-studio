# Zombie Invasion — Quality Assurance, Build and Delivery Traceability Specification v1

**Status:** Detailed design proposal; not an implementation or test report  
**Date:** 2026-11-28  
**Feature IDs:** QA-001..QA-018 and SHIP-001..SHIP-012  
**Related matrix:** `catalogs/feature-traceability-matrix.v1.json`  
**Primary owners:** Validation & Test Evidence System; Publishing & Versioning Engine

## 1. Purpose and boundaries

This document closes feature-level design mapping for the 18 quality-assurance features and 12 build/delivery features. It defines target-aware behavior, acceptance criteria, test cases and prerequisite links. It does not claim that any tests, builds, imports, server startups or gameplay sessions have been executed.

The first playable milestone remains single-player on Java 26.3 + Fabric and Bedrock 26.60 + stable `@minecraft/server` 2.11.0 where scripting is required. Dedicated-server and multiplayer QA are retained as future capability gates, not silently added to the first-slice scope. Experimental Bedrock APIs remain disabled.

## 2. Global quality and delivery rules

- Every result binds to exact source revision, manifest digest, target profile, toolchain and artifact hash.
- Java and Bedrock build, import, load, gameplay and save evidence are separate.
- Unit tests do not replace target runtime tests; successful builds do not prove playable behavior.
- A test not executed is `NOT_RUN`; blocked, skipped, failed and passed are distinct states.
- Release artifacts are immutable, checksummed and accompanied by install instructions and limitations.
- No public release proceeds with unresolved redistribution rights or missing required attribution.
- Dedicated-server and multiplayer tests run only when those profiles are explicitly declared; first-slice single-player is not mislabeled as server/multiplayer validation.

## 3. Feature-level specifications

### QA-001 — Schema and manifest validation

**Requirement:** REQ-QA-001  
**Purpose:** Validate the complete project manifest against the pinned schema version; reject unknown fields and invalid cross-references before planning or generation.  
**Target mapping:** Java and Bedrock target profiles are validated independently; shared manifest invariants are checked once.

**Acceptance criteria**
- AC-QA-001-01: Schema-valid manifest is accepted; invalid required fields, enums, types or unknown properties are rejected with JSON-pointer diagnostics.
- AC-QA-001-02: Cross-reference validation rejects missing target, requirement, component and artifact IDs; validation result records schema version and manifest digest.

**Test cases**
- TC-QA-001-01: TC-QA-001-01 valid v2 manifest passes schema validation
- TC-QA-001-02: TC-QA-001-02 malformed manifest and dangling reference are rejected

**Prerequisite feature IDs:** BASE-001, BASE-008.

### QA-002 — Identifier, registry, and reference validation

**Requirement:** REQ-QA-002  
**Purpose:** Check logical IDs, target-native IDs, item/entity/block/recipe registries, asset references and uniqueness.  
**Target mapping:** Shared logical IDs map to Java namespaced IDs and Bedrock identifiers without collisions.

**Acceptance criteria**
- AC-QA-002-01: Duplicate, invalid, reserved or unresolved IDs are blocking errors; valid references resolve to exactly one declared owner.
- AC-QA-002-02: Validation report includes target-specific collisions and orphan references; aliases are required for renamed persistent IDs.

**Test cases**
- TC-QA-002-01: TC-QA-002-01 duplicate and invalid identifiers rejected
- TC-QA-002-02: TC-QA-002-02 all cross-target references resolve

**Prerequisite feature IDs:** BASE-007.

### QA-003 — Dependency graph and cycle detection

**Requirement:** REQ-QA-003  
**Purpose:** Validate graph endpoints, dependency types, cycles, missing prerequisites and topological production order.  
**Target mapping:** Separate Java and Bedrock dependency graphs are checked; shared prerequisites are represented explicitly.

**Acceptance criteria**
- AC-QA-003-01: Unknown nodes, self-edges and unresolvable hard cycles are rejected; valid graph returns deterministic topological order.
- AC-QA-003-02: Optional late-bound integrations are distinguished from hard prerequisites and cannot hide a required cycle.

**Test cases**
- TC-QA-003-01: TC-QA-003-01 valid DAG produces deterministic order
- TC-QA-003-02: TC-QA-003-02 hard cycle and missing node are blocked

**Prerequisite feature IDs:** BASE-005, BASE-006.

### QA-004 — Version and loader compatibility checks

**Requirement:** REQ-QA-004  
**Purpose:** Check game version, loader/API, pack format, toolchain and dependency constraints against pinned registry data.  
**Target mapping:** Java Fabric and Bedrock stable API compatibility are checked in separate reports.

**Acceptance criteria**
- AC-QA-004-01: Unsupported combinations block generation/build; stale or missing registry evidence is reported as unverified.
- AC-QA-004-02: A target update creates an impact report and cannot silently change an approved manifest.

**Test cases**
- TC-QA-004-01: TC-QA-004-01 approved Java and Bedrock pins resolve independently
- TC-QA-004-02: TC-QA-004-02 unsupported loader or experimental API is rejected

**Prerequisite feature IDs:** BASE-002, BASE-004, BASE-006.

### QA-005 — Static analysis and code quality

**Requirement:** REQ-QA-005  
**Purpose:** Run target-appropriate formatting, lint, type, API-usage, security and packaging static checks before builds.  
**Target mapping:** Java checks Java/Fabric source; Bedrock checks scripts, manifests, JSON and pack assets.

**Acceptance criteria**
- AC-QA-005-01: Findings are severity-classified and tied to file/line/rule; configured blocking findings prevent promotion.
- AC-QA-005-02: Tool versions and rule sets are pinned and recorded for reproducibility.

**Test cases**
- TC-QA-005-01: TC-QA-005-01 clean source passes configured checks
- TC-QA-005-02: TC-QA-005-02 blocking static finding prevents promotion

**Prerequisite feature IDs:** BASE-010, BASE-012.

### QA-006 — Unit tests for isolated logic

**Requirement:** REQ-QA-006  
**Purpose:** Test pure gameplay rules and services without requiring a full Minecraft client where feasible.  
**Target mapping:** Shared logical test vectors run against target adapters where behavior differs; Java and Bedrock suites remain separate.

**Acceptance criteria**
- AC-QA-006-01: Core formulas and state transitions have deterministic tests with boundary and invalid-input coverage.
- AC-QA-006-02: Randomness is seeded or injected; test results are reproducible and do not mutate production saves.

**Test cases**
- TC-QA-006-01: TC-QA-006-01 deterministic unit suite passes on fixed seed
- TC-QA-006-02: TC-QA-006-02 boundary and invalid-input cases fail safely

**Prerequisite feature IDs:** QA-001.

### QA-007 — Integration tests across components

**Requirement:** REQ-QA-007  
**Purpose:** Exercise real component contracts across inventory, loot, combat, injury, crafting, water, power, NPC and world systems.  
**Target mapping:** Each target executes its own integration suite against the same scenario requirements.

**Acceptance criteria**
- AC-QA-007-01: Integration tests verify committed events, resource conservation, ownership boundaries and rollback behavior.
- AC-QA-007-02: A component cannot pass integration solely because mocked dependencies pass; at least one target-native integration path is required.

**Test cases**
- TC-QA-007-01: TC-QA-007-01 cross-system resource transaction is conserved
- TC-QA-007-02: TC-QA-007-02 failed integration rolls back partial state

**Prerequisite feature IDs:** QA-006.

### QA-008 — Build tests for each deliverable

**Requirement:** REQ-QA-008  
**Purpose:** Build every declared Java/Bedrock component and export using pinned toolchain inputs.  
**Target mapping:** Java produces its declared JAR/world/datapack/resource artifacts; Bedrock produces declared packs/world bundle.

**Acceptance criteria**
- AC-QA-008-01: Every mandatory artifact builds from a clean checkout; missing outputs or warnings configured as errors fail the job.
- AC-QA-008-02: Build logs, toolchain pins, source revision and artifact hashes are attached to the exact manifest revision.

**Test cases**
- TC-QA-008-01: TC-QA-008-01 clean Java and Bedrock build jobs produce expected artifacts
- TC-QA-008-02: TC-QA-008-02 missing or corrupted artifact fails build gate

**Prerequisite feature IDs:** QA-004, QA-005, QA-007.

### QA-009 — Dedicated server startup test

**Requirement:** REQ-QA-009  
**Purpose:** Validate dedicated-server startup only for targets/components that declare dedicated-server support.  
**Target mapping:** Java Fabric dedicated server is a later profile; Bedrock hosted/Realm behavior is not inferred from local world tests.

**Acceptance criteria**
- AC-QA-009-01: Server startup, dependency loading and clean shutdown pass for explicitly supported server profiles.
- AC-QA-009-02: First-slice single-player is not blocked by deferred dedicated-server scope, but server support cannot be claimed without this test.

**Test cases**
- TC-QA-009-01: TC-QA-009-01 declared Java dedicated server starts and stops
- TC-QA-009-02: TC-QA-009-02 unsupported Bedrock hosting profile is reported not assessed

**Prerequisite feature IDs:** BASE-003, BASE-010, QA-008.

### QA-010 — World creation/load test

**Requirement:** REQ-QA-010  
**Purpose:** Create a fresh world, load required structures/packs, save, close and reopen without corruption.  
**Target mapping:** Java world/mod data and Bedrock world/pack import/load are tested separately.

**Acceptance criteria**
- AC-QA-010-01: Fresh world creation and subsequent load complete without missing registry, asset or script errors.
- AC-QA-010-02: Test confirms required first-slice landmarks and world-owned state persist across restart.

**Test cases**
- TC-QA-010-01: TC-QA-010-01 fresh Java and Bedrock worlds load required content
- TC-QA-010-02: TC-QA-010-02 save-close-reopen preserves world-owned state

**Prerequisite feature IDs:** BASE-009, QA-008.

### QA-011 — In-game feature acceptance tests

**Requirement:** REQ-QA-011  
**Purpose:** Run player-visible acceptance scenarios against the actual game runtime and approved design criteria.  
**Target mapping:** Java and Bedrock use equivalent scenario intent with edition-specific steps and evidence.

**Acceptance criteria**
- AC-QA-011-01: Each approved first-slice requirement has reproducible steps, expected outcome and recorded actual outcome per target.
- AC-QA-011-02: No feature is called playable based only on unit tests, screenshots or successful packaging.

**Test cases**
- TC-QA-011-01: TC-QA-011-01 approved zombie survival scenario passes in target runtime
- TC-QA-011-02: TC-QA-011-02 missing required gameplay behavior fails acceptance

**Prerequisite feature IDs:** QA-007, QA-010.

### QA-012 — Multiplayer and synchronization tests

**Requirement:** REQ-QA-012  
**Purpose:** Test authority, packet/state synchronization, reconnect, duplicate event handling and concurrent actions when multiplayer is declared.  
**Target mapping:** Multiplayer is deferred from the first single-player slice; Java server/client and Bedrock multiplayer require separate future profiles.

**Acceptance criteria**
- AC-QA-012-01: No multiplayer support claim is made until all declared session and synchronization tests pass.
- AC-QA-012-02: Single-player evidence is explicitly excluded from multiplayer evidence summaries.

**Test cases**
- TC-QA-012-01: TC-QA-012-01 concurrent state changes remain authoritative
- TC-QA-012-02: TC-QA-012-02 reconnect and duplicate message handling are idempotent

**Prerequisite feature IDs:** BASE-010, QA-011.

### QA-013 — Save/reload and migration tests

**Requirement:** REQ-QA-013  
**Purpose:** Verify persistent player/world data, migration, backup and recovery across supported updates.  
**Target mapping:** Java persistent data and Bedrock world dynamic data are tested independently.

**Acceptance criteria**
- AC-QA-013-01: Save/reload preserves inventories, bases, discoveries, NPC state and progression owned by the tested slice.
- AC-QA-013-02: Migration interruption, replay and unsupported downgrade have deterministic recovery outcomes.

**Test cases**
- TC-QA-013-01: TC-QA-013-01 save/reload preserves owned state
- TC-QA-013-02: TC-QA-013-02 migration interruption restores valid backup

**Prerequisite feature IDs:** BASE-009, QA-010.

### QA-014 — Performance profiling and memory tests

**Requirement:** REQ-QA-014  
**Purpose:** Measure tick time, frame impact, memory, entity/pathfinding budgets, chunk work and long-session stability.  
**Target mapping:** Profile both target runtimes on declared reference devices; do not infer Bedrock performance from Java.

**Acceptance criteria**
- AC-QA-014-01: Budgets are defined per scenario and hardware profile; regression thresholds are explicit.
- AC-QA-014-02: Active/near/distant simulation does not force-load remote chunks or exceed configured entity/work budgets.

**Test cases**
- TC-QA-014-01: TC-QA-014-01 representative horde scenario remains within budget
- TC-QA-014-02: TC-QA-014-02 long-session memory and entity counts remain bounded

**Prerequisite feature IDs:** QA-010, QA-011.

### QA-015 — Crash, exploit, duplication, and abuse tests

**Requirement:** REQ-QA-015  
**Purpose:** Probe crash paths, item duplication, resource exploits, permission bypass, malformed data and abusive event loops.  
**Target mapping:** Target-specific exploit surfaces are tested separately; common invariants share test vectors.

**Acceptance criteria**
- AC-QA-015-01: Critical crash, duplication and authority exploits block release; all findings have severity and reproduction steps.
- AC-QA-015-02: Failed transactions leave no partial item/resource changes and repeated events are idempotent.

**Test cases**
- TC-QA-015-01: TC-QA-015-01 inventory and resource duplication attempts are blocked
- TC-QA-015-02: TC-QA-015-02 malformed input and event replay do not corrupt state

**Prerequisite feature IDs:** QA-011, QA-013.

### QA-016 — Accessibility and localization checks

**Requirement:** REQ-QA-016  
**Purpose:** Check control accessibility, text readability, localization completeness and fallback behavior.  
**Target mapping:** Java UI/text and Bedrock UI/text are checked within each edition's supported presentation model.

**Acceptance criteria**
- AC-QA-016-01: Critical gameplay instructions have readable labels and non-color-only signals; missing translations fall back safely.
- AC-QA-016-02: Player-facing text supports the declared locale set and avoids truncation in supported UI contexts.

**Test cases**
- TC-QA-016-01: TC-QA-016-01 required gameplay prompts remain readable and discoverable
- TC-QA-016-02: TC-QA-016-02 missing locale keys use deterministic fallback

**Prerequisite feature IDs:** BASE-008, QA-011.

### QA-017 — Test evidence, logs, reproducibility

**Requirement:** REQ-QA-017  
**Purpose:** Store immutable test evidence tied to source revision, manifest digest, target profile, environment and artifact hashes.  
**Target mapping:** Java and Bedrock evidence records are distinct; shared test intent can link to multiple target runs.

**Acceptance criteria**
- AC-QA-017-01: A test result without required provenance cannot advance status; NOT_RUN/BLOCKED/FAILED/PASSED are distinct.
- AC-QA-017-02: Logs are redacted for secrets and retained according to project policy; reruns are reproducible where deterministic.

**Test cases**
- TC-QA-017-01: TC-QA-017-01 evidence without manifest/target identity is rejected
- TC-QA-017-02: TC-QA-017-02 rerun reproduces same result and artifact provenance

**Prerequisite feature IDs:** QA-001, QA-008, QA-011.

### QA-018 — Known limitations and untested areas register

**Requirement:** REQ-QA-018  
**Purpose:** Maintain explicit known limitations, unsupported capabilities, deferred features and tests not run.  
**Target mapping:** Limitations are reported per target and cannot be hidden by combined status.

**Acceptance criteria**
- AC-QA-018-01: Every release report lists blocking issues, non-blocking limitations, deferred scope and NOT_RUN tests.
- AC-QA-018-02: A limitation is removed only after new evidence and revision-bound review.

**Test cases**
- TC-QA-018-01: TC-QA-018-01 release report lists all unresolved and untested items
- TC-QA-018-02: TC-QA-018-02 closed limitation requires linked passing evidence

**Prerequisite feature IDs:** QA-017.

### SHIP-001 — Source project folder structure

**Requirement:** REQ-SHIP-001  
**Purpose:** Define deterministic source layout for shared design, Java source, Bedrock packs, assets, tests and generated outputs.  
**Target mapping:** Separate target roots and shared logical specification; no cross-target source/binary confusion.

**Acceptance criteria**
- AC-SHIP-001-01: Every component has one declared canonical source root and generated outputs are separated from editable source.
- AC-SHIP-001-02: Folder conventions and namespace paths are validated before generation.

**Test cases**
- TC-SHIP-001-01: TC-SHIP-001-01 expected source roots and component ownership validate
- TC-SHIP-001-02: TC-SHIP-001-02 generated output is isolated from editable source

**Prerequisite feature IDs:** BASE-004, BASE-007.

### SHIP-002 — Reproducible build configuration

**Requirement:** REQ-SHIP-002  
**Purpose:** Pin toolchains, dependency locks, environment inputs and build tasks so identical inputs produce equivalent artifacts.  
**Target mapping:** Java build uses pinned Gradle/Loom/loader/mappings; Bedrock packaging uses pinned validators and deterministic pack metadata.

**Acceptance criteria**
- AC-SHIP-002-01: Build config contains no floating dependency or unpinned toolchain for release builds.
- AC-SHIP-002-02: A clean environment can reproduce build outputs or explain nondeterministic fields.

**Test cases**
- TC-SHIP-002-01: TC-SHIP-002-01 clean build reproduces artifact hashes where deterministic
- TC-SHIP-002-02: TC-SHIP-002-02 floating dependency is rejected in release mode

**Prerequisite feature IDs:** QA-004, QA-005.

### SHIP-003 — Mod JAR / add-on package

**Requirement:** REQ-SHIP-003  
**Purpose:** Package the Java Fabric mod JAR and Bedrock behavior/resource add-on components as distinct installable outputs.  
**Target mapping:** Java JAR and Bedrock .mcpack/.mcaddon or declared pack outputs are target-native and independently validated.

**Acceptance criteria**
- AC-SHIP-003-01: Each package contains required metadata, identifiers, dependencies and assets; wrong-target content is rejected.
- AC-SHIP-003-02: Artifact can be imported/loaded by its declared target environment before delivery status is advanced.

**Test cases**
- TC-SHIP-003-01: TC-SHIP-003-01 Java JAR metadata and load validation
- TC-SHIP-003-02: TC-SHIP-003-02 Bedrock pack metadata and import validation

**Prerequisite feature IDs:** BASE-004, QA-008.

### SHIP-004 — Datapack and resource-pack exports

**Requirement:** REQ-SHIP-004  
**Purpose:** Export target-appropriate datapack and resource-pack artifacts with matching metadata and dependency references.  
**Target mapping:** Java datapack/resource pack are distinct from Bedrock resource pack; Bedrock pack format is validated independently.

**Acceptance criteria**
- AC-SHIP-004-01: Each exported pack declares target version/format and resolves all referenced assets.
- AC-SHIP-004-02: Combined bundle preserves required activation order and dependency metadata.

**Test cases**
- TC-SHIP-004-01: TC-SHIP-004-01 Java datapack and resource pack export
- TC-SHIP-004-02: TC-SHIP-004-02 Bedrock resource pack format and references validate

**Prerequisite feature IDs:** BASE-004, QA-008.

### SHIP-005 — World/map export and required metadata

**Requirement:** REQ-SHIP-005  
**Purpose:** Package playable worlds/maps with required structures, world settings, pack dependencies and attribution.  
**Target mapping:** Java world save and Bedrock world bundle are separate deliverables with target-specific activation metadata.

**Acceptance criteria**
- AC-SHIP-005-01: Fresh import creates/loads the intended world and activates required components without missing references.
- AC-SHIP-005-02: World metadata identifies supported game version and required add-ons/packs.

**Test cases**
- TC-SHIP-005-01: TC-SHIP-005-01 Java world export imports and loads cleanly
- TC-SHIP-005-02: TC-SHIP-005-02 Bedrock world export imports and loads cleanly

**Prerequisite feature IDs:** BASE-009, QA-010.

### SHIP-006 — Dependency and installation instructions

**Requirement:** REQ-SHIP-006  
**Purpose:** Generate exact install/import steps, dependency list, compatibility range and troubleshooting guidance.  
**Target mapping:** Instructions differ by Java Fabric and Bedrock import/activation workflows.

**Acceptance criteria**
- AC-SHIP-006-01: Instructions match the actual artifact set and identify required optional dependencies.
- AC-SHIP-006-02: No instruction claims a runtime/platform that was not tested; known limitations are linked.

**Test cases**
- TC-SHIP-006-01: TC-SHIP-006-01 instructions match generated artifact and dependencies
- TC-SHIP-006-02: TC-SHIP-006-02 unsupported runtime is not advertised

**Prerequisite feature IDs:** BASE-005, BASE-012, SHIP-003, SHIP-004, SHIP-005.

### SHIP-007 — Server and client installation profiles

**Requirement:** REQ-SHIP-007  
**Purpose:** Describe and package role-specific installation profiles for client, integrated server and any explicitly supported dedicated/hosted runtime.  
**Target mapping:** First playable profile is single-player; later server/client profiles require separate target validation.

**Acceptance criteria**
- AC-SHIP-007-01: Profile declares role, required files, dependencies, permissions and unsupported capabilities.
- AC-SHIP-007-02: Dedicated/hosted profile is withheld unless its QA gates pass.

**Test cases**
- TC-SHIP-007-01: TC-SHIP-007-01 single-player profile includes correct target artifacts
- TC-SHIP-007-02: TC-SHIP-007-02 unsupported server profile is blocked from publication

**Prerequisite feature IDs:** BASE-003, BASE-010, QA-009, QA-012.

### SHIP-008 — ZIP bundle with editable sources

**Requirement:** REQ-SHIP-008  
**Purpose:** Create an optional source bundle containing editable source, specs, assets, licenses and build instructions without secrets or transient files.  
**Target mapping:** Bundle includes shared project specification plus separate Java and Bedrock source roots.

**Acceptance criteria**
- AC-SHIP-008-01: Archive has deterministic structure, manifest and checksums; secrets, caches and local credentials are excluded.
- AC-SHIP-008-02: Source bundle can be extracted and rebuilt in a clean environment.

**Test cases**
- TC-SHIP-008-01: TC-SHIP-008-01 source bundle passes secret and unwanted-file scan
- TC-SHIP-008-02: TC-SHIP-008-02 extracted source rebuilds from clean environment

**Prerequisite feature IDs:** SHIP-001, SHIP-002, SHIP-003, SHIP-004, SHIP-005, BASE-012.

### SHIP-009 — Versioning, changelog, release notes

**Requirement:** REQ-SHIP-009  
**Purpose:** Assign release versions and produce change notes describing features, fixes, breaking changes and target compatibility.  
**Target mapping:** Java and Bedrock artifacts share project release identity but may have separate artifact versions and compatibility notes.

**Acceptance criteria**
- AC-SHIP-009-01: Release notes identify exact supported versions, changed components, migrations and known limitations.
- AC-SHIP-009-02: A release cannot overwrite prior immutable artifacts or erase provenance.

**Test cases**
- TC-SHIP-009-01: TC-SHIP-009-01 release notes match actual component diff
- TC-SHIP-009-02: TC-SHIP-009-02 breaking save change requires migration warning

**Prerequisite feature IDs:** SHIP-003, SHIP-004, SHIP-005.

### SHIP-010 — Checksums and artifact manifest

**Requirement:** REQ-SHIP-010  
**Purpose:** Generate an artifact manifest with IDs, target, version, size, hash, dependencies, license notices and build provenance.  
**Target mapping:** Each Java/Bedrock artifact has its own hash and metadata record; combined release references both.

**Acceptance criteria**
- AC-SHIP-010-01: Every delivered file is listed exactly once and hash verification detects tampering/corruption.
- AC-SHIP-010-02: Manifest is bound to release revision and cannot be silently edited after publication.

**Test cases**
- TC-SHIP-010-01: TC-SHIP-010-01 artifact manifest verifies all package hashes
- TC-SHIP-010-02: TC-SHIP-010-02 altered artifact fails checksum validation

**Prerequisite feature IDs:** SHIP-003, SHIP-004, SHIP-005, SHIP-008.

### SHIP-011 — Clean-install verification

**Requirement:** REQ-SHIP-011  
**Purpose:** Install/import the release into a clean target environment without relying on developer caches or hidden local files.  
**Target mapping:** Java and Bedrock clean installs are separate mandatory gates for the dual-edition milestone.

**Acceptance criteria**
- AC-SHIP-011-01: All required dependencies and instructions are sufficient for clean install; no undeclared local file is required.
- AC-SHIP-011-02: Clean install reaches the declared load/playable evidence level and captures logs.

**Test cases**
- TC-SHIP-011-01: TC-SHIP-011-01 Java clean install loads from release bundle
- TC-SHIP-011-02: TC-SHIP-011-02 Bedrock clean import loads from release bundle

**Prerequisite feature IDs:** QA-008, SHIP-006, SHIP-010.

### SHIP-012 — Final playable acceptance checklist

**Requirement:** REQ-SHIP-012  
**Purpose:** Aggregate feature acceptance, build/load/world/gameplay, install, known limitations and target parity into a release gate.  
**Target mapping:** Both Java and Bedrock must independently pass first playable gates; deferred multiplayer/server features remain explicitly out of scope.

**Acceptance criteria**
- AC-SHIP-012-01: Release is blocked if a mandatory feature, target artifact, clean-install check or required evidence is missing.
- AC-SHIP-012-02: Final report distinguishes playable verified, build-only, not run, blocked and deferred; no blanket green status.

**Test cases**
- TC-SHIP-012-01: TC-SHIP-012-01 both target tracks satisfy first-playable checklist
- TC-SHIP-012-02: TC-SHIP-012-02 missing mandatory evidence blocks playable release

**Prerequisite feature IDs:** QA-011, QA-017, QA-018, SHIP-003, SHIP-004, SHIP-005, SHIP-006, SHIP-010, SHIP-011.

## 4. Dependency graph proposal

Dependency direction is prerequisite → dependent. These are feature-level design edges, not runtime service calls. Every edge remains `proposed` until reviewed.

| Prerequisite | Dependent | Reason |
|---|---|---|
| BASE-001 | QA-001 | QA-001 consumes the validated contract or evidence from BASE-001 |
| BASE-008 | QA-001 | QA-001 consumes the validated contract or evidence from BASE-008 |
| BASE-007 | QA-002 | QA-002 consumes the validated contract or evidence from BASE-007 |
| BASE-005 | QA-003 | QA-003 consumes the validated contract or evidence from BASE-005 |
| BASE-006 | QA-003 | QA-003 consumes the validated contract or evidence from BASE-006 |
| BASE-002 | QA-004 | QA-004 consumes the validated contract or evidence from BASE-002 |
| BASE-004 | QA-004 | QA-004 consumes the validated contract or evidence from BASE-004 |
| BASE-006 | QA-004 | QA-004 consumes the validated contract or evidence from BASE-006 |
| BASE-010 | QA-005 | QA-005 consumes the validated contract or evidence from BASE-010 |
| BASE-012 | QA-005 | QA-005 consumes the validated contract or evidence from BASE-012 |
| QA-001 | QA-006 | QA-006 consumes the validated contract or evidence from QA-001 |
| QA-006 | QA-007 | QA-007 consumes the validated contract or evidence from QA-006 |
| QA-004 | QA-008 | QA-008 consumes the validated contract or evidence from QA-004 |
| QA-005 | QA-008 | QA-008 consumes the validated contract or evidence from QA-005 |
| QA-007 | QA-008 | QA-008 consumes the validated contract or evidence from QA-007 |
| BASE-003 | QA-009 | QA-009 consumes the validated contract or evidence from BASE-003 |
| BASE-010 | QA-009 | QA-009 consumes the validated contract or evidence from BASE-010 |
| QA-008 | QA-009 | QA-009 consumes the validated contract or evidence from QA-008 |
| BASE-009 | QA-010 | QA-010 consumes the validated contract or evidence from BASE-009 |
| QA-008 | QA-010 | QA-010 consumes the validated contract or evidence from QA-008 |
| QA-007 | QA-011 | QA-011 consumes the validated contract or evidence from QA-007 |
| QA-010 | QA-011 | QA-011 consumes the validated contract or evidence from QA-010 |
| BASE-010 | QA-012 | QA-012 consumes the validated contract or evidence from BASE-010 |
| QA-011 | QA-012 | QA-012 consumes the validated contract or evidence from QA-011 |
| BASE-009 | QA-013 | QA-013 consumes the validated contract or evidence from BASE-009 |
| QA-010 | QA-013 | QA-013 consumes the validated contract or evidence from QA-010 |
| QA-010 | QA-014 | QA-014 consumes the validated contract or evidence from QA-010 |
| QA-011 | QA-014 | QA-014 consumes the validated contract or evidence from QA-011 |
| QA-011 | QA-015 | QA-015 consumes the validated contract or evidence from QA-011 |
| QA-013 | QA-015 | QA-015 consumes the validated contract or evidence from QA-013 |
| BASE-008 | QA-016 | QA-016 consumes the validated contract or evidence from BASE-008 |
| QA-011 | QA-016 | QA-016 consumes the validated contract or evidence from QA-011 |
| QA-001 | QA-017 | QA-017 consumes the validated contract or evidence from QA-001 |
| QA-008 | QA-017 | QA-017 consumes the validated contract or evidence from QA-008 |
| QA-011 | QA-017 | QA-017 consumes the validated contract or evidence from QA-011 |
| QA-017 | QA-018 | QA-018 consumes the validated contract or evidence from QA-017 |
| BASE-004 | SHIP-001 | SHIP-001 consumes the validated contract or evidence from BASE-004 |
| BASE-007 | SHIP-001 | SHIP-001 consumes the validated contract or evidence from BASE-007 |
| QA-004 | SHIP-002 | SHIP-002 consumes the validated contract or evidence from QA-004 |
| QA-005 | SHIP-002 | SHIP-002 consumes the validated contract or evidence from QA-005 |
| BASE-004 | SHIP-003 | SHIP-003 consumes the validated contract or evidence from BASE-004 |
| QA-008 | SHIP-003 | SHIP-003 consumes the validated contract or evidence from QA-008 |
| BASE-004 | SHIP-004 | SHIP-004 consumes the validated contract or evidence from BASE-004 |
| QA-008 | SHIP-004 | SHIP-004 consumes the validated contract or evidence from QA-008 |
| BASE-009 | SHIP-005 | SHIP-005 consumes the validated contract or evidence from BASE-009 |
| QA-010 | SHIP-005 | SHIP-005 consumes the validated contract or evidence from QA-010 |
| BASE-005 | SHIP-006 | SHIP-006 consumes the validated contract or evidence from BASE-005 |
| BASE-012 | SHIP-006 | SHIP-006 consumes the validated contract or evidence from BASE-012 |
| SHIP-003 | SHIP-006 | SHIP-006 consumes the validated contract or evidence from SHIP-003 |
| SHIP-004 | SHIP-006 | SHIP-006 consumes the validated contract or evidence from SHIP-004 |
| SHIP-005 | SHIP-006 | SHIP-006 consumes the validated contract or evidence from SHIP-005 |
| BASE-003 | SHIP-007 | SHIP-007 consumes the validated contract or evidence from BASE-003 |
| BASE-010 | SHIP-007 | SHIP-007 consumes the validated contract or evidence from BASE-010 |
| QA-009 | SHIP-007 | SHIP-007 consumes the validated contract or evidence from QA-009 |
| QA-012 | SHIP-007 | SHIP-007 consumes the validated contract or evidence from QA-012 |
| SHIP-001 | SHIP-008 | SHIP-008 consumes the validated contract or evidence from SHIP-001 |
| SHIP-002 | SHIP-008 | SHIP-008 consumes the validated contract or evidence from SHIP-002 |
| SHIP-003 | SHIP-008 | SHIP-008 consumes the validated contract or evidence from SHIP-003 |
| SHIP-004 | SHIP-008 | SHIP-008 consumes the validated contract or evidence from SHIP-004 |
| SHIP-005 | SHIP-008 | SHIP-008 consumes the validated contract or evidence from SHIP-005 |
| BASE-012 | SHIP-008 | SHIP-008 consumes the validated contract or evidence from BASE-012 |
| SHIP-003 | SHIP-009 | SHIP-009 consumes the validated contract or evidence from SHIP-003 |
| SHIP-004 | SHIP-009 | SHIP-009 consumes the validated contract or evidence from SHIP-004 |
| SHIP-005 | SHIP-009 | SHIP-009 consumes the validated contract or evidence from SHIP-005 |
| SHIP-003 | SHIP-010 | SHIP-010 consumes the validated contract or evidence from SHIP-003 |
| SHIP-004 | SHIP-010 | SHIP-010 consumes the validated contract or evidence from SHIP-004 |
| SHIP-005 | SHIP-010 | SHIP-010 consumes the validated contract or evidence from SHIP-005 |
| SHIP-008 | SHIP-010 | SHIP-010 consumes the validated contract or evidence from SHIP-008 |
| QA-008 | SHIP-011 | SHIP-011 consumes the validated contract or evidence from QA-008 |
| SHIP-006 | SHIP-011 | SHIP-011 consumes the validated contract or evidence from SHIP-006 |
| SHIP-010 | SHIP-011 | SHIP-011 consumes the validated contract or evidence from SHIP-010 |
| QA-011 | SHIP-012 | SHIP-012 consumes the validated contract or evidence from QA-011 |
| QA-017 | SHIP-012 | SHIP-012 consumes the validated contract or evidence from QA-017 |
| QA-018 | SHIP-012 | SHIP-012 consumes the validated contract or evidence from QA-018 |
| SHIP-003 | SHIP-012 | SHIP-012 consumes the validated contract or evidence from SHIP-003 |
| SHIP-004 | SHIP-012 | SHIP-012 consumes the validated contract or evidence from SHIP-004 |
| SHIP-005 | SHIP-012 | SHIP-012 consumes the validated contract or evidence from SHIP-005 |
| SHIP-006 | SHIP-012 | SHIP-012 consumes the validated contract or evidence from SHIP-006 |
| SHIP-010 | SHIP-012 | SHIP-012 consumes the validated contract or evidence from SHIP-010 |
| SHIP-011 | SHIP-012 | SHIP-012 consumes the validated contract or evidence from SHIP-011 |

## 5. Release evidence ladder

1. Schema/metadata validated.
2. Static checks passed.
3. Dependency resolution passed.
4. Target build passed.
5. Artifact import/load passed.
6. World creation/save/reload passed.
7. Required gameplay acceptance passed.
8. Clean-install verification passed.
9. Final release checklist passed for both mandatory target tracks.

A higher level cannot be inferred from a lower level. Each level requires its own evidence record.

## 6. First-playable versus later capability

| Capability | First playable | Later milestone / conditional |
|---|---|---|
| Manifest/schema, IDs, dependencies, static checks | Required | Continuous |
| Java and Bedrock builds/import/load | Required | Continuous |
| World creation, save/reload, gameplay acceptance | Required | Continuous |
| Clean install and checksums | Required | Continuous |
| Dedicated server startup | Not required | Required only for a declared server profile |
| Multiplayer synchronization | Not required | Required only when multiplayer is enabled |
| Performance profiling | Required for the first-slice scenario | Expanded for larger worlds and systems |
| Full editable source bundle | Optional delivery format | Product/package policy |

## 7. Implementation order

1. QA-001..QA-004: schema, IDs, graph and compatibility gates.
2. QA-005..QA-008: static checks, unit/integration suites and target builds.
3. QA-010 and QA-013: world creation, save/reload and migration.
4. QA-011, QA-014..QA-018: gameplay, performance, exploit, accessibility and evidence reporting.
5. SHIP-001..SHIP-005: source layout and target-native artifacts.
6. SHIP-006..SHIP-011: instructions, profiles, source bundle, release metadata, checksums and clean install.
7. SHIP-012: final dual-target playable gate.

## 8. Open constraints

- Exact Fabric Loader, Fabric API, Loom, Gradle, mappings and Java runtime versions must be verified and pinned before builds.
- Actual Bedrock 26.60 pack format and stable API availability must be verified on the target runtime.
- Reference hardware, automated launch environment and manual test device inventory remain to be recorded.
- Performance thresholds must be set from representative target hardware rather than invented in advance.
- Dedicated-server and multiplayer support remain outside first-slice acceptance until explicitly scheduled.

## 9. Implementation boundary

This specification is design-only. QA-001..QA-018 and SHIP-001..SHIP-012 implementation statuses remain `not_implemented_verified` until code, actual target builds, imports, runtime tests and revision-bound evidence exist. The presence of test case definitions is not evidence that tests have run.
