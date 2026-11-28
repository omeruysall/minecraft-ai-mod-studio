# Zombie Invasion — Foundation, Compatibility and Feature Traceability Specification v1

**Status:** Detailed design proposal for baseline review; not an implementation claim  
**Date:** 2026-11-28  
**Source feature IDs:** BASE-001 through BASE-012  
**Source matrix:** `catalogs/feature-traceability-matrix.v1.json` v1.1.0  
**Primary owner:** Minecraft Compatibility Engine  
**Related contract:** `schemas/project-manifest.v2.schema.json`

## 1. Purpose and scope

This specification closes the first 12 feature-level traceability records in the Project Foundation and Compatibility inventory section. It converts broad feature names into explicit requirements, target mappings, dependency edges, acceptance criteria and test cases.

It is a design contract for the Minecraft AI Mod Studio and the Zombie Invasion reference project. It does not claim that any resolver, build pipeline, mod, add-on, migration system or test runner has been implemented.

The 12 source feature IDs remain stable. The requirement, dependency and test IDs below are deterministic identifiers proposed for the project manifest and traceability matrix.

## 2. Baseline decisions and constraints

### 2.1 User-confirmed target profile

| Target | Confirmed baseline | Constraints |
|---|---|---|
| Java Edition | Minecraft 26.3 + Fabric | Exact Fabric Loader, Loom, mappings, Gradle and Java toolchain versions must be verified and pinned at implementation start |
| Bedrock Edition | Minecraft 26.60 | Use stable `@minecraft/server` 2.11.0 where scripting is required |
| Bedrock experimental APIs | Disabled | No experimental capability may silently enter the approved baseline |

Both target tracks are mandatory for the first playable milestone. A shared gameplay requirement does not imply a shared binary, loader, API, packaging format or test result.

### 2.2 First playable runtime boundary

- First playable gameplay is single-player.
- Java runs as a client with its integrated server for the first slice; dedicated-server deployment is a later validation profile unless a specific feature requires it.
- Bedrock runs in a local world with the relevant behavior/resource packs and stable script runtime.
- Realm, hosted-server and dedicated-server capability must be represented as distinct runtime profiles, not assumed to work because local single-player works.
- The long-term product may support more runtime profiles, but they are not first-slice acceptance requirements.

### 2.3 Non-negotiable compatibility rules

1. Resolve Java and Bedrock independently.
2. Pin target versions and toolchain inputs to an approved manifest revision.
3. Never infer support from a feature name, documentation heading or the other edition's implementation.
4. Unknown compatibility is `NOT_ASSESSED`, not supported.
5. Experimental APIs remain excluded unless the user explicitly changes the policy and approves a new revision.
6. A metadata check, static validation, successful build, successful load, integration test and gameplay test are distinct evidence levels.
7. A test that was not executed is `NOT_RUN`; it is never reported as passed.
8. A target update must produce an impact report and a new manifest revision; it must not silently mutate an approved project.
9. The project manifest is the execution contract. This document is the human-readable specification.
10. Generated code and build tools must execute in isolated workers, not inside the Studio control-plane process.

## 3. Feature traceability summary

| Feature ID | Feature | Requirement ID | Primary target mapping | Proposed dependency edges |
|---|---|---|---|---|
| BASE-001 | Edition selection | REQ-BASE-001 | Java + Bedrock target profiles | DEP-BASE-001-A |
| BASE-002 | Minecraft version/range | REQ-BASE-002 | Exact pinned versions per target | DEP-BASE-002-A |
| BASE-003 | Runtime platform | REQ-BASE-003 | Java integrated server; Bedrock local world | DEP-BASE-003-A |
| BASE-004 | Loader/platform | REQ-BASE-004 | Fabric; Bedrock behavior/resource packs | DEP-BASE-004-A |
| BASE-005 | Required/optional dependencies | REQ-BASE-005 | Separate target dependency sets | DEP-BASE-005-A, DEP-BASE-005-B |
| BASE-006 | Version resolution/conflict detection | REQ-BASE-006 | Independent resolvers and combined project gate | DEP-BASE-006-A, DEP-BASE-006-B |
| BASE-007 | Namespace and identifiers | REQ-BASE-007 | Shared logical IDs; target-safe physical IDs | DEP-BASE-007-A |
| BASE-008 | Configuration/defaults/validation/migration | REQ-BASE-008 | Shared schema intent; target-specific serialization | DEP-BASE-008-A, DEP-BASE-008-B |
| BASE-009 | Save compatibility and migration | REQ-BASE-009 | Separate Java and Bedrock save adapters | DEP-BASE-009-A, DEP-BASE-009-B |
| BASE-010 | Client/server split and distribution | REQ-BASE-010 | Java distribution roles; Bedrock pack/world roles | DEP-BASE-010-A |
| BASE-011 | Environment detection/warnings | REQ-BASE-011 | Preflight checks per target and runtime | DEP-BASE-011-A |
| BASE-012 | Licensing/attribution/assets | REQ-BASE-012 | Shared asset/dependency register; per-artifact notices | DEP-BASE-012-A |

These are proposed edges for review. They must be added to the machine-readable matrix only after its schema and edge vocabulary are formalized.

## 4. Feature specifications

### 4.1 BASE-001 — Edition selection: Java / Bedrock

**Requirement:** REQ-BASE-001  
**Intent:** A project may target Java, Bedrock or both. Zombie Invasion first playable targets both.

**Rules**
- Edition is a first-class target property, not inferred from output filenames.
- Each target receives its own version, runtime, loader/API, component graph, build job, validation report and deliverable list.
- Shared requirements may link to multiple target components.
- Unsupported or unavailable target capabilities must be represented explicitly; no silent omission.
- A combined release is complete only when all mandatory target gates pass.

**Java mapping:** Java Edition target profile using Fabric and Java-specific mod/world/resource artifacts.  
**Bedrock mapping:** Bedrock Edition target profile using behavior/resource packs and a Bedrock world bundle.  
**Acceptance criteria**
- AC-BASE-001-01: A project can declare Java and Bedrock targets in one manifest.
- AC-BASE-001-02: Each target has an independent component/dependency graph.
- AC-BASE-001-03: A failed or blocked target cannot be hidden by the other target passing.
- AC-BASE-001-04: The combined report identifies per-target status and parity classification.
- AC-BASE-001-05: A target cannot be marked supported without target-specific evidence.

**Tests:** TC-BASE-001-01 manifest with both editions; TC-BASE-001-02 Java failure/Bedrock pass aggregation; TC-BASE-001-03 Bedrock failure/Java pass aggregation; TC-BASE-001-04 missing-target evidence rejection.

### 4.2 BASE-002 — Minecraft version and supported version range

**Requirement:** REQ-BASE-002  
**Intent:** Bind each target to an exact supported game version or an explicitly governed range. The first playable uses exact versions.

**Rules**
- Java baseline: 26.3.
- Bedrock baseline: 26.60.
- Version range support is not inferred from adjacent versions.
- Version metadata must include source, retrieval time, verification state and registry revision.
- The first build must revalidate the selected versions and pin exact toolchain patch versions.
- A newer game update creates a compatibility assessment; it does not automatically rewrite the project target.

**Java mapping:** Exact Minecraft 26.3 profile plus verified Fabric compatibility and pinned build toolchain.  
**Bedrock mapping:** Exact Minecraft 26.60 profile plus stable Script API 2.11.0 when scripting is used.  
**Acceptance criteria**
- AC-BASE-002-01: Both target profiles resolve to the user-approved exact game versions.
- AC-BASE-002-02: Unsupported or unverified version combinations are blocked or explicitly marked unverified.
- AC-BASE-002-03: Registry evidence and toolchain pins are stored against the manifest revision.
- AC-BASE-002-04: A version change produces a compatibility diff and requires renewed approval.
- AC-BASE-002-05: Experimental Bedrock APIs are rejected by the baseline policy.

**Tests:** TC-BASE-002-01 exact target resolution; TC-BASE-002-02 unsupported version rejection; TC-BASE-002-03 stale registry warning; TC-BASE-002-04 version-change impact report; TC-BASE-002-05 experimental API policy rejection.

### 4.3 BASE-003 — Runtime platform

**Requirement:** REQ-BASE-003  
**Intent:** Distinguish local single-player, integrated server, dedicated server, Realm and hosted runtime support.

**Rules**
- First playable is single-player.
- Java first-slice runtime is the client plus integrated server.
- Bedrock first-slice runtime is a local world with its packs and stable scripting runtime.
- Dedicated server, Realm and hosted server are separate profiles requiring independent capability and load testing.
- Runtime-dependent features must declare where authoritative state executes.

**Java mapping:** Client presentation and integrated-server authoritative gameplay; dedicated server is a later profile.  
**Bedrock mapping:** Local world/script host; Realm/dedicated hosting is not assumed.  
**Acceptance criteria**
- AC-BASE-003-01: Runtime profile is mandatory for each target build/test job.
- AC-BASE-003-02: First-slice manifests declare single-player only.
- AC-BASE-003-03: Features that require unavailable server-only APIs are identified before generation.
- AC-BASE-003-04: A local-world pass cannot be represented as Realm or dedicated-server validation.

**Tests:** TC-BASE-003-01 valid first-slice runtime profiles; TC-BASE-003-02 unsupported runtime capability rejection; TC-BASE-003-03 evidence-level separation between local and hosted runtime.

### 4.4 BASE-004 — Loader/platform selection

**Requirement:** REQ-BASE-004  
**Intent:** Select a platform-native implementation family per target.

**Rules**
- Java uses Fabric for the confirmed first-slice target.
- Bedrock uses native behavior/resource packs; Script API 2.11.0 is used only where required and supported.
- Java datapacks, Fabric mods and Bedrock behavior packs are different component types.
- A target cannot import the other target's binary or assume equivalent APIs.
- The Studio planner must reject unsupported component/loader combinations before code generation.

**Java mapping:** Fabric mod, Java world/datapack and Java resource pack as individually declared components.  
**Bedrock mapping:** Behavior pack, resource pack and Bedrock world as separately declared components.  
**Acceptance criteria**
- AC-BASE-004-01: Java components resolve only against compatible Java/Fabric profiles.
- AC-BASE-004-02: Bedrock components resolve only against Bedrock formats/APIs.
- AC-BASE-004-03: Component type mismatch is a blocking validation error.
- AC-BASE-004-04: Every generated deliverable declares its target and install/import procedure.

**Tests:** TC-BASE-004-01 valid Fabric component graph; TC-BASE-004-02 valid Bedrock pack graph; TC-BASE-004-03 cross-edition component rejection; TC-BASE-004-04 missing install metadata rejection.

### 4.5 BASE-005 — Required and optional dependencies

**Requirement:** REQ-BASE-005  
**Intent:** Model dependency declarations, scope, target applicability and required/optional behavior.

**Rules**
- Dependency records include stable ID, name, version constraint, target, source, license, required/optional flag and compatibility evidence.
- Java and Bedrock dependency sets are independent.
- Optional dependency absence must disable only the declared optional integration, not silently break core gameplay.
- Transitive dependencies are included in the resolved graph and license inventory.
- No dependency may be downloaded or executed without source validation and policy checks.

**Java mapping:** Fabric Loader/API and any approved Java libraries/mod dependencies, each pinned and checked.  
**Bedrock mapping:** Stable Script API module dependencies and declared pack/module dependencies.  
**Acceptance criteria**
- AC-BASE-005-01: Every dependency has a target and explicit required/optional state.
- AC-BASE-005-02: Required missing dependencies block the target.
- AC-BASE-005-03: Missing optional dependencies produce a warning and a defined fallback.
- AC-BASE-005-04: Transitive dependencies are visible in the report and asset/license register.
- AC-BASE-005-05: Java dependencies are not copied into the Bedrock dependency graph and vice versa.

**Tests:** TC-BASE-005-01 missing required dependency; TC-BASE-005-02 missing optional dependency fallback; TC-BASE-005-03 transitive dependency enumeration; TC-BASE-005-04 target isolation.

### 4.6 BASE-006 — Dependency version resolution and conflict detection

**Requirement:** REQ-BASE-006  
**Intent:** Resolve constraints deterministically and detect incompatible versions before generation/build.

**Rules**
- Resolution uses pinned registry snapshots and explicit version constraints.
- Conflicts include incompatible ranges, duplicate singleton libraries, API incompatibility, loader mismatch and pack-format mismatch.
- Resolution output is reproducible for the same manifest and registry snapshot.
- No automatic major-version upgrade is allowed after approval.
- Conflict resolution options must be shown as a plan revision for user approval.

**Java mapping:** Resolve Fabric Loader, Fabric API, Java libraries, mappings and build plugins as a coherent pinned toolchain.  
**Bedrock mapping:** Validate pack format, module UUID/dependency declarations and stable Script API module version.  
**Acceptance criteria**
- AC-BASE-006-01: Compatible constraints resolve to a deterministic lock record.
- AC-BASE-006-02: Conflicting constraints produce a blocking diagnostic with affected components.
- AC-BASE-006-03: The resolver never silently selects an incompatible or experimental API.
- AC-BASE-006-04: Lock output records exact versions and registry snapshot identity.
- AC-BASE-006-05: Re-running with unchanged inputs yields the same resolution.

**Tests:** TC-BASE-006-01 deterministic resolution; TC-BASE-006-02 version-range conflict; TC-BASE-006-03 loader/API mismatch; TC-BASE-006-04 registry update creates diff rather than mutation.

### 4.7 BASE-007 — Project namespace, identifiers and naming rules

**Requirement:** REQ-BASE-007  
**Intent:** Maintain stable logical IDs across shared design while generating target-safe physical identifiers.

**Rules**
- Use a project namespace reserved for the project; do not assume the display name is a valid namespace.
- Logical feature, item, entity, block, recipe, event, asset and component IDs are stable and unique.
- Java and Bedrock physical identifiers may differ but map to one shared logical ID.
- Renames require migration aliases; IDs are not reused after deletion.
- Validate case sensitivity, allowed characters, reserved names and length limits per target.

**Java mapping:** Namespaced identifiers suitable for Fabric/Minecraft resource conventions.  
**Bedrock mapping:** Namespaced identifiers and pack UUIDs satisfying Bedrock constraints.  
**Acceptance criteria**
- AC-BASE-007-01: Duplicate logical IDs are rejected.
- AC-BASE-007-02: Every target-specific ID maps to exactly one logical source ID.
- AC-BASE-007-03: Invalid or reserved identifiers are rejected before generation.
- AC-BASE-007-04: Renames preserve migration aliases and do not orphan saved references.

**Tests:** TC-BASE-007-01 duplicate ID; TC-BASE-007-02 invalid identifier; TC-BASE-007-03 cross-target logical mapping; TC-BASE-007-04 rename/migration alias.

### 4.8 BASE-008 — Configuration format, defaults, validation and migration

**Requirement:** REQ-BASE-008  
**Intent:** Define validated, versioned project/gameplay configuration with target-specific serialization.

**Rules**
- Shared configuration expresses gameplay intent and canonical values; platform adapters serialize supported settings into target-native files/data.
- Every setting declares type, default, range/enum, owner, scope, target applicability and migration behavior.
- User configuration overrides defaults only through validated fields.
- Invalid values fail with actionable diagnostics; silent clamping is allowed only where explicitly specified.
- Configuration migrations are deterministic, versioned and reversible where feasible.
- Secrets and provider keys never enter game-pack configuration or public artifacts.

**Java mapping:** Fabric config/data files and supported datapack/world settings as appropriate.  
**Bedrock mapping:** Pack manifests, world settings and supported script configuration/data assets; no unsupported runtime file access assumed.  
**Acceptance criteria**
- AC-BASE-008-01: All settings are schema-validated before generation.
- AC-BASE-008-02: Defaults are deterministic and documented.
- AC-BASE-008-03: Out-of-range and unknown settings produce clear diagnostics.
- AC-BASE-008-04: Migration preserves user values where semantics remain compatible.
- AC-BASE-008-05: Target adapters report settings that cannot be represented on one edition.

**Tests:** TC-BASE-008-01 default materialization; TC-BASE-008-02 invalid value rejection; TC-BASE-008-03 schema migration; TC-BASE-008-04 unsupported target setting report; TC-BASE-008-05 secret leakage scan.

### 4.9 BASE-009 — Save compatibility, upgrades and downgrade policy

**Requirement:** REQ-BASE-009  
**Intent:** Protect world and player state across mod/pack updates.

**Rules**
- Save data has explicit schema version, project identity and component ownership.
- Migration runs against a backup or recoverable snapshot.
- Migrations are ordered, deterministic and idempotent.
- Downgrade is blocked when data loss or incompatible semantics are detected, unless the user explicitly exports/restores a compatible backup.
- Java and Bedrock save formats are independently handled; shared logical data does not imply shared binary save files.
- Player-built bases, discovered locations, inventory, NPC state and progression must not be reset by routine updates.

**Java mapping:** Versioned Java mod persistent data and world data migration.  
**Bedrock mapping:** Supported world/pack dynamic data and schema migration within Bedrock constraints.  
**Acceptance criteria**
- AC-BASE-009-01: Every persistent schema declares a version.
- AC-BASE-009-02: Update migration creates or verifies a recoverable backup.
- AC-BASE-009-03: Re-running a completed migration does not duplicate or corrupt state.
- AC-BASE-009-04: Unsupported downgrade is blocked with a recovery path.
- AC-BASE-009-05: Java and Bedrock save validation is performed independently.

**Tests:** TC-BASE-009-01 forward migration; TC-BASE-009-02 interrupted migration recovery; TC-BASE-009-03 idempotent replay; TC-BASE-009-04 incompatible downgrade block; TC-BASE-009-05 preservation of player-built world state.

### 4.10 BASE-010 — Client/server feature split and distribution

**Requirement:** REQ-BASE-010  
**Intent:** Declare where logic executes and which artifact is distributed to each runtime role.

**Rules**
- Gameplay-authoritative state must not rely solely on client presentation state.
- Client-only assets/UI and authoritative gameplay logic are classified separately.
- First-slice single-player does not remove the need for clear authority boundaries.
- Future dedicated-server support requires explicit server-safe code and distribution checks.
- Deliverables declare installation role, dependencies and whether a restart/world activation is required.

**Java mapping:** Separate client presentation from integrated/server-side gameplay logic within Fabric architecture; validate dedicated-server compatibility later.  
**Bedrock mapping:** Use supported behavior-pack/script execution and resource-pack presentation roles; document world/pack activation requirements.  
**Acceptance criteria**
- AC-BASE-010-01: Every component declares client, server, shared or world-pack role.
- AC-BASE-010-02: Server-authoritative gameplay cannot be bypassed by client-only state.
- AC-BASE-010-03: Deliverables identify install role and dependencies.
- AC-BASE-010-04: Unsupported dedicated-server use is clearly marked, not implied by single-player success.

**Tests:** TC-BASE-010-01 role declaration validation; TC-BASE-010-02 client-only authority violation; TC-BASE-010-03 packaging role completeness; TC-BASE-010-04 runtime compatibility report.

### 4.11 BASE-011 — Environment detection and unsupported-platform warnings

**Requirement:** REQ-BASE-011  
**Intent:** Detect actual target/runtime conditions before build, import and test.

**Rules**
- Preflight records game version, edition, loader/API, pack format, runtime role, required capabilities and relevant environment metadata.
- Unsupported combinations block the affected operation.
- Warnings distinguish unsupported, unverified, degraded and optional capability states.
- Do not collect unnecessary personal/device data; retain only technical data needed for compatibility and diagnostics.
- Environment checks are repeated at test/import boundaries when runtime conditions may have changed.

**Java mapping:** Verify Minecraft version, Fabric Loader/API, Java runtime and required mod dependencies.  
**Bedrock mapping:** Verify Bedrock version, pack format, stable Script API availability and required world settings.  
**Acceptance criteria**
- AC-BASE-011-01: Preflight produces a structured target report.
- AC-BASE-011-02: Unsupported target/runtime combinations are blocked before execution.
- AC-BASE-011-03: Unverified states are not displayed as supported.
- AC-BASE-011-04: Diagnostic records contain no secrets or unrelated personal information.

**Tests:** TC-BASE-011-01 valid environment; TC-BASE-011-02 unsupported version; TC-BASE-011-03 missing API/capability; TC-BASE-011-04 diagnostic privacy scan.

### 4.12 BASE-012 — Licensing, attribution and third-party asset register

**Requirement:** REQ-BASE-012  
**Intent:** Track provenance and permitted use of code, libraries, models, textures, audio, fonts and other assets.

**Rules**
- Every third-party dependency and imported/generated-from-reference asset has a provenance record.
- Record creator/source, license or terms, attribution text, version/hash, modifications and redistribution permissions where known.
- Unknown or incompatible license status blocks public redistribution until resolved.
- Generated assets must not be mislabeled as original if derived from restricted references.
- Notices and attributions are packaged in the relevant deliverables.
- User-supplied assets retain declared ownership/permission metadata; Studio does not infer rights merely from upload.

**Java mapping:** Include dependency notices and asset attributions in the Java mod/distribution bundle.  
**Bedrock mapping:** Include notices in the relevant behavior/resource/world package distribution.  
**Acceptance criteria**
- AC-BASE-012-01: Every third-party dependency/asset has a provenance record or an explicit unresolved state.
- AC-BASE-012-02: Redistribution-blocking licenses prevent public release.
- AC-BASE-012-03: Required attribution is included in the correct target bundle.
- AC-BASE-012-04: Asset hashes and license metadata are revision-bound.
- AC-BASE-012-05: Missing rights metadata is surfaced before publication.

**Tests:** TC-BASE-012-01 missing license metadata; TC-BASE-012-02 redistribution restriction; TC-BASE-012-03 attribution bundle check; TC-BASE-012-04 asset hash/provenance mismatch.

## 5. Proposed dependency graph

The following edges describe prerequisite relationships. They are not runtime service calls.

| Edge ID | Prerequisite | Dependent | Rationale |
|---|---|---|---|
| DEP-BASE-001-A | BASE-001 | BASE-002, BASE-004, BASE-005 | Edition determines version and platform domains |
| DEP-BASE-002-A | BASE-002 | BASE-004, BASE-006, BASE-011 | Exact version bounds loader/API and environment compatibility |
| DEP-BASE-003-A | BASE-003 | BASE-010, BASE-011 | Runtime role determines execution and preflight requirements |
| DEP-BASE-004-A | BASE-004 | BASE-005, BASE-006, BASE-010 | Loader/platform constrains dependencies and distribution |
| DEP-BASE-005-A | BASE-005 | BASE-006, BASE-012 | Declared dependencies must be resolved and licensed |
| DEP-BASE-005-B | BASE-005 | BASE-010 | Dependency roles affect client/server distribution |
| DEP-BASE-006-A | BASE-006 | BASE-011 | Resolved graph is checked against actual environment |
| DEP-BASE-006-B | BASE-006 | Build/test planning | Build jobs consume a reproducible dependency lock |
| DEP-BASE-007-A | BASE-007 | Configuration, assets, components and persistent state | Stable IDs are prerequisites for safe references/migration |
| DEP-BASE-008-A | BASE-008 | BASE-009 | Persistent configuration changes require migration rules |
| DEP-BASE-008-B | BASE-008 | Target generation adapters | Native configuration serialization consumes validated settings |
| DEP-BASE-009-A | BASE-009 | Save/load and update delivery | Migration safety gates updates |
| DEP-BASE-009-B | BASE-009 | Backup/recovery workflow | Recoverable snapshots are required for risky migrations |
| DEP-BASE-010-A | BASE-010 | Packaging and runtime tests | Distribution roles determine artifact layout and test target |
| DEP-BASE-011-A | BASE-011 | Build/import/load test execution | Preflight must pass before the target operation |
| DEP-BASE-012-A | BASE-012 | Asset pipeline and publication | Rights checks gate redistribution |

No edge may create a cycle. If future dependency modelling introduces one, the planner must distinguish a true prerequisite cycle from a late-bound optional integration and require an explicit bootstrap or alternate route.

## 6. Manifest binding proposal

The v2 project manifest already provides the required structural locations:

- `targets[]`: edition, exact version selection, loader, runtime and deployment roles.
- `requirements[]`: REQ-BASE-001 through REQ-BASE-012, each with user provenance, status and acceptance criteria.
- `components[]`: target-specific Java/Bedrock components, engine owner, requirement IDs and dependency IDs.
- `dependency_graph`: typed directed edges with stable IDs and source/target references.
- `assets[]`: provenance, license and hash metadata.
- `generation`: pinned toolchain and generator inputs.
- `approvals`: approval bound to exact manifest revision/digest.
- `validation`: target-specific plans and evidence.
- `deliverables[]`: target bundle, artifact identity and install instructions.

Suggested requirement IDs:
- REQ-BASE-001 through REQ-BASE-012.

Suggested target IDs:
- `java-26-3-fabric`
- `bedrock-26-60-stable`

These are proposed stable IDs. Before materializing them into a project manifest, validate them against the current schema and project namespace rules. Do not invent exact Fabric Loader/Loom/Gradle/Java patch pins before checking authoritative compatibility metadata.

## 7. Test evidence model

Each test record should include:
- Stable test ID from this specification.
- Feature ID and requirement ID.
- Target ID and manifest revision/digest.
- Test type: schema, static, dependency, build, import/load, integration, gameplay, migration, privacy or licensing.
- Preconditions and reproducible steps.
- Expected result and actual result.
- Status: NOT_RUN, PASSED, FAILED, BLOCKED or SKIPPED.
- Runtime/toolchain versions and environment fingerprint.
- Log/report references and artifact hash.
- Timestamp and runner identity.

A test is not evidence unless it is tied to the exact manifest revision and target profile. Build success alone is not playable verification.

## 8. First implementation sequence for this layer

1. Validate the v2 manifest schema and establish the canonical project/target IDs.
2. Create target profile registry records for Java 26.3 + Fabric and Bedrock 26.60 + stable Script API 2.11.0.
3. Add stable logical IDs and target-specific ID mapping.
4. Implement dependency declaration and deterministic lock generation.
5. Implement compatibility preflight and actionable conflict reports.
6. Implement versioned configuration validation and migration contracts.
7. Implement save migration/backup interfaces before changing persistent gameplay state.
8. Implement target role classification and packaging metadata.
9. Implement asset/dependency provenance and license checks.
10. Add automated tests for all TC-BASE-* cases before claiming this foundation layer is complete.

## 9. Open items and explicit non-assumptions

- Exact Fabric Loader, Fabric API, Loom, Gradle, mappings and Java runtime pins require fresh authoritative verification at implementation start.
- Exact Bedrock pack format and stable API availability must be checked against the actual 26.60 runtime.
- The user has approved single-player as sufficient for the first playable slice; dedicated server, Realm and multiplayer remain later validation scopes.
- Licensing policy for user-provided assets and generated assets needs a product-level legal/policy review.
- Exact target hardware and automated game-launch environments remain to be recorded.
- No claim is made that all 12 features are approved or implemented merely because this specification maps them.

## 10. Implementation boundary

This specification defines feature-level design, target mappings, dependencies and acceptance tests. All BASE-001..BASE-012 implementation statuses remain `not_implemented_verified` until repository code, builds, target runtime loads and required tests produce linked evidence. Target coverage remains unverified until Java and Bedrock are independently assessed.

## 11. Related documents

- `docs/MINECRAFT_VERSION_COMPATIBILITY_ENGINE_SPEC.md`
- `docs/ZOMBIE_INVASION_MASTER_FEATURE_DEPENDENCY_AND_IMPLEMENTATION_MAP_V1.md`
- `docs/ZOMBIE_INVASION_FEATURE_TRACEABILITY_GAP_ASSESSMENT_V1.md`
- `docs/FIRST_PLAYABLE_DECISION_REGISTER_V1.md`
- `docs/ZOMBIE_INVASION_CROSS_SYSTEM_INTEGRATION_AND_CONFLICT_AUDIT_V1.md`
- `schemas/project-manifest.v2.schema.json`
