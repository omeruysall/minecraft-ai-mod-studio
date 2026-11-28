# Minecraft Version and Compatibility Engine Specification

**Document ID:** MC-COMPAT-001  
**Version:** 1.0  
**Status:** Design draft — pending review and approval  
**Product:** Minecraft AI Mod Studio  
**Implementation status:** Not implemented  
**Last updated:** 2026-11-28

## 1. Purpose

Define the compatibility system that determines whether a requested Minecraft project can be created, packaged, installed, and run on the user's selected edition, version, loader, server environment, and dependency set.

The engine must prevent the product from treating "code generated" or "build succeeded" as proof that a Minecraft artifact is compatible or playable.

This specification defines architecture and behavior. It does not claim that any current version, loader, or platform is already supported by the application.

## 2. Scope

The engine covers:
- Minecraft Java Edition and Bedrock Edition as separate compatibility domains.
- User-selected game versions and release channels where applicable.
- Java mod loaders and their version constraints.
- Bedrock add-on format and engine capability constraints.
- Server/client environment constraints.
- Datapack, resource pack, map/world, plugin, and modpack compatibility.
- Third-party dependencies and optional integrations.
- Cross-component compatibility in multi-artifact projects.
- Compatibility metadata, validation, warnings, and test evidence.

It does not replace the individual artifact generators. It supplies compatibility decisions and constraints to Project Architect, planners, generators, packagers, and test runners.

## 3. Core rules

1. The user chooses the target edition and version, or explicitly authorizes a recommended target.
2. Java and Bedrock are separate platforms. Their artifacts and APIs must not be mixed without an explicitly supported bridge.
3. Loader families are distinct compatibility targets; Forge, NeoForge, and Fabric are not interchangeable.
4. A dependency must be compatible with the selected edition, version, loader, environment, and relevant dependency versions.
5. Compatibility is evidence-based and time-sensitive. Registry entries must include source, verification date, and status.
6. Unknown compatibility must be reported as unknown, not compatible.
7. A project may contain components with different compatibility scopes only when their integration path is explicitly supported and tested.
8. The engine must not silently change the user's selected Minecraft version or loader.
9. A target change creates a new compatibility evaluation and may require a new plan revision and user approval.
10. Build success is one validation signal, not proof of in-game behavior or playability.

## 4. Compatibility dimensions

Every compatibility evaluation should consider the relevant dimensions:

| Dimension | Examples |
|---|---|
| Edition | Java Edition, Bedrock Edition |
| Game version | Exact version or verified version range |
| Loader/runtime | Fabric, Forge, NeoForge, Bedrock runtime, server platform |
| Environment | Client, dedicated server, integrated server, Realms or other supported target |
| Artifact type | Mod, plugin, datapack, resource pack, world, add-on, modpack |
| Java/runtime requirements | Required runtime version and platform constraints |
| Dependencies | Required, optional, incompatible, or bundled libraries |
| API/format level | Mod loader API, pack format, add-on schema/format |
| Side support | Client-only, server-only, both, or unknown |
| Distribution | Launcher, server, marketplace, manual install, export format |
| Integration | Whether components can coexist and communicate as designed |

Only applicable dimensions should be required for a given artifact type. For example, a pure world export should not be forced to declare a Java mod loader.

## 5. Platform profiles

### 5.1 Java Edition

A Java project profile should capture:
- Exact Minecraft version or explicitly permitted version range.
- Loader selection where mods require one.
- Loader version and supported game-version mapping.
- Java runtime requirement.
- Client/server side expectations.
- Mod dependencies and conflicts.
- Datapack and resource-pack format compatibility.
- World and server requirements.

Loader families are separate profiles:
- Fabric.
- Forge.
- NeoForge.

The system must not infer that a mod built for one loader works on another. Porting is a separate task and requires explicit planning.

### 5.2 Bedrock Edition

A Bedrock project profile should capture:
- Exact target game version or verified range.
- Add-on type and supported behavior/resource pack features.
- Manifest and module format requirements.
- Script/API dependencies where applicable.
- Experimental feature requirements.
- Target device/platform constraints where relevant.
- World template and pack dependencies.

Bedrock support must be driven by verified Bedrock APIs and schemas. Java mod-loader concepts must not be applied to Bedrock projects.

### 5.3 Server and plugin targets

Server plugin projects require a separate runtime profile that records:
- Server implementation and version.
- API compatibility range.
- Java runtime requirement where applicable.
- Required server-side dependencies.
- Client-side requirements, if any.
- Whether the plugin is compatible with the selected server implementation.

A server plugin is not a Java client mod. If a feature requires both, the plan must explicitly include the relevant client and server components.

## 6. Version and capability registry

Maintain a versioned registry rather than hard-coding compatibility assumptions in generators.

Registry entities:
- Edition and game release.
- Loader and loader release.
- Server implementation and API release.
- Pack format and schema revision.
- Runtime requirement.
- Dependency and library release.
- Artifact compatibility declaration.
- Feature/API capability.
- Known incompatibility or migration note.

Each registry record should include:
- Stable ID.
- Display name.
- Version identifier.
- Supported ranges or exact versions.
- Source URL or authoritative source reference.
- Source type and publisher.
- Verification timestamp.
- Registry revision.
- Status: verified, provider-declared, community-reported, experimental, deprecated, unsupported, unknown.
- Notes and known constraints.

Do not present a community-reported compatibility claim as official verification. Preserve provenance and confidence.

## 7. Compatibility resolver

The resolver evaluates a target profile against project requirements and selected components.

Logical process:
1. Read the approved or proposed target profile.
2. Normalize edition, version, loader, runtime, and environment.
3. Resolve applicable registry entries.
4. Evaluate each requested feature against platform capabilities.
5. Resolve loader and API constraints.
6. Resolve required and optional dependencies.
7. Detect version conflicts and unsupported combinations.
8. Evaluate cross-component compatibility.
9. Produce a compatibility report and recommended resolutions.
10. Return blocking issues to Project Architect before plan approval or production.

Resolver outcomes:
- COMPATIBLE_VERIFIED
- COMPATIBLE_WITH_CONSTRAINTS
- COMPATIBILITY_UNVERIFIED
- INCOMPATIBLE
- MISSING_DEPENDENCY
- CONFLICT
- UNSUPPORTED_TARGET
- INSUFFICIENT_INFORMATION

The report must explain each outcome and identify affected requirements and components.

## 8. Dependency resolution

Dependencies should be modeled as a directed graph.

Each dependency edge should record:
- Source component.
- Target dependency.
- Required/optional/recommended status.
- Version constraint.
- Compatibility scope.
- Reason for dependency.
- Source/provenance.
- Resolution status.

Rules:
- Detect cycles and invalid dependency chains.
- Prefer a compatible, verified dependency version satisfying all constraints.
- Do not silently upgrade or downgrade user-pinned dependencies.
- Distinguish bundled dependencies from externally installed dependencies.
- Identify license and distribution constraints for bundled third-party artifacts.
- If no valid resolution exists, block the affected plan or propose alternatives.
- Re-evaluate the full affected dependency subgraph when a version changes.

## 9. Multi-component project compatibility

A project manifest should define one or more target profiles and component-specific compatibility declarations.

Examples:
- A Java mod plus a datapack and resource pack targeting the same Java version.
- A Bedrock behavior pack plus a resource pack and world.
- A server plugin plus a compatible server deployment profile.
- A modpack that pins the game version, loader, mods, and dependencies.

The engine must verify:
- Each component's individual compatibility.
- Cross-component version alignment.
- Identifier, namespace, and reference consistency.
- Dependency availability.
- Packaging and installation layout.
- Server/client side compatibility.
- Whether the intended gameplay behavior is actually implemented by the assigned components.

If a component cannot operate in the selected environment, the system must not hide it inside a successful overall project status.

## 10. Version changes and migrations

When the user changes target version, edition, loader, or server platform:
1. Create a proposed target revision.
2. Identify affected components and requirements.
3. Re-evaluate compatibility and dependencies.
4. Determine whether a migration, port, or regeneration is required.
5. Preserve unaffected files and components.
6. Produce a change-impact report.
7. Request approval if scope, deliverables, or production actions materially change.

Do not assume an older artifact can be upgraded by changing only a metadata field. Migration requires artifact-specific rules and validation.

## 11. Validation and evidence levels

Compatibility claims should be reported with evidence levels:

- **Metadata checked:** declarations and registry constraints were compared.
- **Static validation passed:** schemas, identifiers, manifests, and references passed.
- **Dependency resolution passed:** all required dependencies resolved.
- **Build passed:** artifact compiled or packaged successfully.
- **Load test passed:** artifact loaded in the target runtime.
- **Integration test passed:** relevant project components worked together in the target environment.
- **Gameplay test passed:** required behavior was exercised in Minecraft or a defined automated test environment.
- **Manual verification:** a human tested the artifact, with environment and steps recorded.

A level must not imply a higher level. For example, BUILD_PASSED does not imply LOAD_TEST_PASSED or PLAYABLE_VERIFIED.

If a test cannot run, mark it NOT_RUN and explain why.

## 12. Compatibility report

The report should contain:
- Target profile and revision.
- Registry snapshot/revision used.
- Overall outcome.
- Per-component outcome.
- Dependency graph summary.
- Blocking issues.
- Warnings and constraints.
- Recommended alternatives.
- Evidence level and test results.
- Source and verification timestamps.
- User decisions required.

The report must be visible before approval and again before production if relevant registry data has changed materially.

## 13. Integration contracts

The engine exposes internal contracts to:
- Project Architect: compatibility decisions and blockers.
- Requirement Analyzer: feasibility constraints and clarification prompts.
- Component Planner: valid component assignments.
- Dependency Manager: graph and version constraints.
- Generators: pinned target configuration.
- Build/Test Orchestrator: target runtime and test matrix.
- Packaging/Export: correct artifact layout and metadata.
- Project Memory: decisions, reports, and registry snapshot references.

Generators must consume a pinned target profile rather than independently choosing versions.

## 14. Failure and update behavior

Handle:
- Missing version metadata.
- Stale registry data.
- Unavailable official source.
- Conflicting compatibility declarations.
- Dependency version conflict.
- Unsupported loader/version combination.
- Deprecated APIs or pack formats.
- Target runtime unavailable for testing.
- Incomplete component metadata.
- Registry update during an active project.

A registry update must not silently mutate an approved project. It may raise a notice and request re-evaluation. Approved target pins remain stable until the user accepts a change.

## 15. Acceptance criteria

- Java and Bedrock compatibility domains are separate.
- Loader families are not treated as interchangeable.
- Every compatibility claim has provenance and verification status.
- Unknown compatibility is never presented as verified.
- Dependency conflicts are detected before production.
- Multi-component projects are checked both per-component and as an integrated set.
- Target version changes create an impact report and revision.
- Generators consume a pinned target profile.
- Build, load, integration, and gameplay test results are separate.
- Unavailable tests are explicitly marked NOT_RUN.
- The system blocks or requests a decision when compatibility is materially unresolved.
- Compatibility data can be updated without rewriting product-domain logic.

## 16. Open design decisions

1. First-release Java and Bedrock version support policy.
2. Whether the initial release supports all currently maintained versions or a curated support window.
3. Which official/community metadata sources are accepted for each platform and loader.
4. Whether users can pin end-of-life versions.
5. Initial server implementations and plugin APIs to support.
6. Whether compatibility research may use external services at runtime or only pre-synced registry data.
7. Registry refresh frequency and stale-data policy.
8. Which target environments are available for automated load and gameplay testing.
9. How licenses and redistribution constraints are represented in dependency metadata.
10. Whether a project can declare multiple target profiles in the first release.

These decisions require a separate support policy and source registry. Do not guess current support coverage during implementation.

## 17. Implementation boundary

This document defines intended compatibility behavior only. It does not assert that version resolution, loader detection, dependency solving, registry synchronization, migration, or in-game testing exists in the current application. Implementation begins only after the complete design baseline is reviewed and explicitly approved.


## 18. Dual-edition first milestone

The first playable milestone explicitly selects both Java and Bedrock. The resolver must create and evaluate two separate target profiles, even when they share the same user-facing gameplay requirements.

For every shared requirement, the report must provide:
- Java target support outcome and evidence.
- Bedrock target support outcome and evidence.
- Platform-specific implementation notes.
- Dependency and runtime constraints for each target.
- Parity classification: native, adapted, limited, unsupported or unverified.

Java loader selection and Bedrock API/format selection remain independent. No cross-edition compatibility may be inferred from a common feature name or manifest requirement. The first milestone cannot be marked fully playable until both target profiles pass their own agreed gates.


## 19. Dated first-slice compatibility research

The 2026-11-28 research note proposes Java 26.3 + Fabric and Bedrock 26.60 + stable Script API 2.11.0 as candidate baselines. Bedrock 26.63 was announced as a platform-dependent hotfix rollout, so it must not be assumed available on every device.

Reference: `docs/FIRST_SLICE_COMPATIBILITY_RECOMMENDATION_2026-11.md`.

These values are dated recommendations, not universal compatibility declarations. The registry must revalidate exact game, loader, API and toolchain versions from authoritative sources at implementation start and bind test evidence to the actual target profile.


## Current Zombie Invasion target profile research (2026-11-28)

The current Zombie Invasion project target profile is Java Edition 26.3 + Fabric and Bedrock Edition 26.60 + stable `@minecraft/server` 2.11.0, with Bedrock experimental APIs disabled.

For Java 26.3, the current Fabric Develop selector lists Fabric Loader 0.20.1, Fabric Loom 1.19-SNAPSHOT and Fabric API 0.166.0+26.3. Java runtime baseline is 25+. Gradle wrapper selection remains an explicit compatibility-resolution step; do not copy the older release-day Loom 1.17 / Gradle 9.6.0 / Loader 0.19.5 values as current pins without checking the selected Loom build.

For Bedrock 26.60, the official 2026-10-27 changelog confirms `@minecraft/server` 2.11.0 as released stable and identifies 2.12.0-beta separately. The target pack format, peer dependencies and actual import/load behavior must still be verified.

References and evidence boundaries are maintained in `docs/ZOMBIE_INVASION_TARGET_TOOLCHAIN_COMPATIBILITY_RESEARCH_2026-11.md`. These are current documentation recommendations, not build/runtime evidence.