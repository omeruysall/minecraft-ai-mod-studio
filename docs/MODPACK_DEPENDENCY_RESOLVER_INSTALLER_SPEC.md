# Modpack & Dependency Resolver / Installer Specification

**Document status:** Design draft  
**Version:** 0.1  
**Implementation status:** Not implemented; design requirements only.  
**Approval status:** Awaiting product decisions and baseline approval.

## 1. Purpose
Define how Minecraft AI Mod Studio assembles, resolves, validates, installs, updates, exports, and diagnoses multi-component projects and modpacks. The resolver must ensure that mods, loaders, game versions, libraries, datapacks, resource packs, add-ons, maps, and server requirements form a compatible and reproducible project.

## 2. Ownership boundaries
- This engine owns dependency graph resolution, version constraints, lockfiles, installation plans, package assembly, and conflict reports.
- Java/Bedrock/Datapack/Resource Pack production engines own their artifact contents.
- Minecraft Version Compatibility Engine owns canonical platform/version capability facts.
- Project Architect owns project intent, approval state, and cross-component impact planning.
- Build system owns compilation and packaging execution.
- Runtime/test harness owns actual load and gameplay evidence.
- External launchers and server managers are integration targets, not assumed capabilities.

## 3. Principles
- Resolve exact versions and hashes wherever possible.
- Never silently substitute incompatible dependencies.
- Reproducible builds require lockfiles and recorded repositories.
- License and provenance are checked before inclusion.
- Installation and updates are non-destructive, backed up, and reversible where feasible.
- Client and server dependency sets are distinguished.
- A resolved graph is not proof that the assembled pack launches or plays correctly.

## 4. Scope
In scope: modpack manifests, dependency metadata, loader/version resolution, transitive dependencies, optional/required conflicts, side constraints, version pinning, repositories, checksums, license metadata, install plans, profile isolation, export, update, rollback, diagnostics, and server/client pack parity.

Out of scope: distributing unauthorized copyrighted assets, bypassing platform authentication, silently downloading arbitrary executables, or guaranteeing support for every third-party mod.

## 5. Package manifest
A pack manifest defines stable ID, title, author, description, pack version, target edition, Minecraft version, loader/runtime, side (client/server/both), component references, dependency constraints, optional features, repositories, license/provenance metadata, configuration overlays, and compatibility claims. The manifest is schema-versioned.

## 6. Dependency model
Each dependency declares ID/namespace, version constraint, source/repository, artifact type, platform/loader requirements, side, required/optional status, conflicts, provides/replaces relationships, checksum, license, and provenance. Support semantic or ecosystem-specific version comparison without assuming all mods use semantic versioning.

## 7. Resolution algorithm
Resolution considers root requirements, transitive dependencies, loader constraints, game version, side, conflicts, optional features, and repository availability. It produces either a deterministic solution or a structured unsatisfied-constraints report. Ambiguous candidates require explicit policy or user choice; no silent "latest" selection for locked projects.

## 8. Compatibility matrix
Compatibility is evaluated across Minecraft edition/version, Java loader, mod versions, APIs/libraries, client/server side, datapacks, resource packs, and world requirements. Each result is supported, unsupported, unknown, or conditionally supported with evidence. Unknown is not presented as compatible.

## 9. Conflict detection
Detect version conflicts, duplicate providers, incompatible loaders, missing libraries, side mismatch, dependency cycles, namespace collisions, duplicate resource identifiers, conflicting datapack functions/tags, incompatible world requirements, and license-policy violations. Reports include dependency paths and actionable remedies.

## 10. Lockfile and reproducibility
Lockfiles record exact artifacts, versions, hashes, source repositories, metadata snapshot, resolver version, and selected optional features. Rebuilds should reproduce the same dependency graph. If an artifact becomes unavailable, the resolver reports the failure rather than silently selecting another version.

## 11. Repository and provenance policy
Only configured repositories are queried. Record source URL, publisher identity where available, checksum, license, and retrieval timestamp. Validate redirects and artifact type. Do not execute downloaded code during resolution. Malicious or suspicious artifacts are quarantined and reported.

## 12. Client/server split
A pack may define client-only, server-only, and shared dependencies. Generate separate installation plans and compare required shared content. Identify mismatched versions and missing server/client components. Do not distribute server secrets or private configuration in client packages.

## 13. Installation profiles
Profiles isolate game version, loader, pack version, mods, configurations, worlds, and runtime settings. Installation plans preview all file writes, replacements, downloads, and removals. Existing profiles and worlds are not overwritten without explicit confirmation and backup.

## 14. Safe installation and rollback
Install to a user-selected or managed isolated directory. Verify hashes before use. Stage changes before activation. Maintain a transaction journal for partial failure. Rollback restores prior manifest/configuration and preserves user-created worlds and saves. Never delete unknown files automatically.

## 15. Update and migration
Updates compare old and new lockfiles, identify removed/added/changed artifacts, configuration migrations, world/data risks, and server/client coordination. Breaking updates require approval. Provide staged rollout and rollback plan. Preserve pinned versions unless user approves update policy.

## 16. Configuration management
Configuration overlays are typed, versioned, and scoped to client/server/world. Track generated defaults separately from user overrides. Migrations show diffs and conflicts. Secrets remain external and are never embedded in public pack artifacts.

## 17. World and save compatibility
Pack changes may alter registries, blocks, entities, dimensions, recipes, or data formats. Before applying updates to an existing world, compare required content and migration capabilities. Require backup and explicit consent for potentially destructive changes. Never claim a world is safe solely because a dependency graph resolves.

## 18. Security and sandboxing
Downloaded artifacts are treated as untrusted. Resolution never executes them. Build and test execution occurs in isolated environments with resource limits and no unnecessary secrets/network access. Validate archive paths against traversal, symlink abuse, oversized files, and decompression bombs. Keep install permissions scoped to the selected profile.

## 19. License and content policy
Record license identifiers and source attribution. Flag missing, incompatible, or restrictive license metadata. Respect redistribution restrictions: a pack may reference a dependency without bundling it where redistribution is not permitted. User approval does not override legal or platform restrictions.

## 20. UI and authoring experience
Provide pack builder, dependency graph, compatibility matrix, conflict explorer, client/server split, lockfile view, install preview, update diff, license/provenance report, and rollback controls. Conversational pack requests become a plan listing all components, versions, constraints, disk/network requirements, and risks before approval.

## 21. Validation and testing
Validate manifest schema, dependency constraints, graph cycles, checksums, repository policy, license metadata, side assignments, platform compatibility, and archive safety. Test clean install, interrupted install, rollback, update, downgrade where supported, client/server parity, missing repository, corrupted artifact, and existing-world safety. Launch tests must run against actual supported game profiles. Unrun tests are reported as not run.

## 22. Diagnostics and repair
Provide structured reasons for unresolved constraints, dependency paths, hash mismatch, install failures, startup errors, and version conflicts. Repair suggestions may pin, replace, remove, or upgrade dependencies, but require approval if they change project scope or compatibility. Never auto-remove a dependency that owns world data without migration analysis.

## 23. Delivery
Deliver pack manifest, lockfile, client/server installation plans, compatible artifacts or lawful references, configuration overlays, license/provenance report, install/update/rollback instructions, compatibility matrix, and test evidence. Include editable source project and exportable pack archive.

## 24. Acceptance criteria
- Resolution is deterministic for a fixed manifest and repository snapshot.
- Exact artifacts and hashes are recorded in lockfiles.
- Incompatibilities and unknown support are reported distinctly.
- Client/server dependency sets are correct and auditable.
- Installation is isolated, staged, and recoverable.
- Updates preserve user data and require approval for risky changes.
- License/provenance constraints are enforced.
- Archive extraction is safe against traversal and resource abuse.
- Launch and gameplay evidence is separate from graph resolution.
- Rollback and restore have been tested.

## 25. Open decisions
1. Which launchers and game profile formats are supported initially?
2. Is installation managed by Studio, exported as instructions, or both?
3. Which repositories are trusted and enabled by default?
4. Which metadata sources are authoritative for each ecosystem?
5. Which dependency version syntaxes must be supported?
6. What is the default version policy: pinned, compatible range, or user-selected?
7. How are unknown compatibility claims handled?
8. Are third-party mod downloads performed automatically or user-confirmed?
9. Which client/server pack formats are generated?
10. Is server deployment integrated or handled separately?
11. What license policy blocks bundling versus allows reference-only dependencies?
12. What malware scanning or reputation service, if any, is used?
13. Where are lockfiles and artifact caches stored?
14. What are cache size, retention, and cleanup rules?
15. Which install locations and operating systems are supported?
16. What backup policy applies to existing profiles and worlds?
17. Which configuration migration formats are supported?
18. How are world registry/data migrations assessed?
19. Are downgrade operations supported, and under what restrictions?
20. What happens if a repository disappears or changes an artifact?
21. What package size and download limits apply?
22. Which external launcher/server APIs are allowed and under what licenses?
23. What audit and telemetry data is retained?
24. Which clean-install, update, rollback, and real-world launch tests are release blockers?

## 26. Current status
Design draft only. All open decisions remain unresolved until explicitly decided by the product owner. No dependency resolver, modpack installer, lockfile generator, launcher integration, or installation workflow is implemented by this document.
