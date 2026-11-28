# Publishing, Versioning & Update Engine Specification

**Status:** Design draft  **Version:** 1.0  **Implementation status:** Not implemented

## 1. Purpose
Define the lifecycle for packaging, validating, versioning, publishing, distributing, updating, rolling back and retiring Minecraft AI Mod Studio projects and their individual components. Publishing supports a single map, mod, datapack, resource pack, Bedrock add-on, server plugin, modpack, or a complete multi-artifact project. Users are not forced to publish every component.

## 2. Core principles
- Publishing is an explicit action, separate from generation and local export.
- Releases are immutable; changes create a new release.
- Each release pins an exact project-manifest revision and exact component and asset versions.
- Compatibility, provenance and validation evidence accompany the release.
- Draft, private, unlisted, public and withdrawn visibility are distinct.
- Updates are reviewable and reversible where technically possible; never silently apply them to user worlds.
- Build success is not proof of runtime playability.
- Publishing respects ownership, licensing, moderation and security requirements.

## 3. Publishable units
Support individual artifacts, selected compatible component sets, full project bundles, modpacks, server deployment bundles, map/world releases, documentation, source and asset bundles. The release manifest records included and excluded components and unresolved optional dependencies.

## 4. Release lifecycle
Proposed states: draft, validating, ready_for_review, approved, publishing, published, validation_failed, changes_requested, rejected, publishing_failed, withdrawn, deprecated and archived. Record actor, timestamp, reason and revision for every transition. Failed publication must not expose a partial release as complete.

## 5. Release manifest
Each release records release_id, project_id, project revision, semantic version, display metadata, publisher and ownership evidence, target edition and Minecraft version, loader/API/server requirements, exact component versions and hashes, required/optional/incompatible dependencies, runtime and editable-source links, license and attribution, provenance, validation and playtest evidence, changelog, known issues, migration notes, visibility and moderation state, distribution channels, and signature/checksum metadata where supported.

## 6. Versioning policy
Use semantic versioning as a default proposal: MAJOR for breaking changes, MINOR for backward-compatible features, PATCH for compatible fixes. Minecraft version and loader compatibility are separate fields and must not be inferred from semantic version. Pre-release identifiers may represent alpha, beta and release candidates. Imported ecosystems may require native version conventions.

## 7. Compatibility declaration
Declare Java/Bedrock edition, supported Minecraft versions, Java loader and loader versions, required APIs/libraries/plugins/server software, client/server requirements, known conflicts, and world/data migration requirements. Distinguish declared, statically checked, built, load-tested and gameplay-tested combinations. Never claim support for untested combinations.

## 8. Release validation gate
Run applicable checks: manifest and artifact integrity; component completeness; dependency resolution; license and attribution; malware/security scanning; platform/version compatibility; build and package verification; automated load/runtime tests; performance and multiplayer checks; human review and owner approval. Each check is passed, failed, blocked, skipped or not_run. Skipped/not_run is never passed.

## 9. Packaging and reproducibility
Generate deterministic package layouts and checksums. Include runtime files, release manifest, changelog, install instructions, dependency/license notices, validation report, optional editable source and provenance bundle. Preserve build outputs and toolchain metadata. Document non-deterministic steps.

## 10. Signing and integrity
Support cryptographic hashes for artifacts and packages. Evaluate release signing for publisher authenticity and tamper detection. Store keys in managed secrets or secure local storage; never commit private keys or expose them in logs. Signature absence must be displayed honestly.

## 11. Publishing destinations
Use provider-neutral destination adapters for the Studio catalog, downloadable project pages, user-controlled export, external distribution platforms where permitted, and private team/server distribution. Each destination has independent capabilities, policy, metadata and authentication requirements. Do not assume external APIs or upload permissions exist.

## 12. Community catalog and discovery
Catalog entries may represent map-only, mod-only, add-on-only, datapack-only or complete projects. Discovery may include search, filters, compatibility, tags, version history, previews, changelog, author profile, reviews and update notifications. Any sponsored placement must be clearly labeled.

## 13. Ownership and collaboration
Only authorized roles may publish, edit release metadata, withdraw or transfer ownership. Enforce permissions server-side and audit every privileged action. Separate reviewer and publisher roles where team policy requires. Ownership transfer, delegated publishing and organization accounts remain open decisions.

## 14. Update discovery and notifications
Compare installed or subscribed release identifiers with the latest compatible release. Support in-app and authorized external notifications. Users control frequency and channels. Avoid repeated notifications for incompatible or withdrawn releases without actionable information.

## 15. Update planning and migration
Before applying an update, resolve dependencies and compatibility, compare component versions and hashes, identify breaking changes and data migrations, estimate affected worlds/saves/configuration/server state, create or verify a recoverable backup, present a change summary and request confirmation for risky changes. Never silently update a world or server.

## 16. Installation and deployment
Provide separate workflows for download-only export, local client installation, dedicated server installation, Bedrock pack/world import, modpack installation and Studio-managed synchronization. Detect paths safely, validate permissions, prevent traversal and never overwrite user files without confirmation. Provide manual instructions when automation is unsupported.

## 17. Rollback and recovery
Retain prior release metadata and package hashes. Artifact rollback does not guarantee reversal of world data or external server state. For risky updates, create timestamped backups and verify integrity. Offer rollback only when target version and migration path are known; identify irreversible changes.

## 18. Deprecation and withdrawal
Publishers may mark releases deprecated, superseded or withdrawn with reason and replacement link. Moderators may restrict visibility under policy. Withdrawal preserves audit records and does not silently remove downloaded files. Legal takedown and retention require explicit policy.

## 19. Reviews, reports and moderation
Support reports, review moderation, spam controls, malware reports, copyright complaints and appeals. Technical validation and content moderation are separate gates.

## 20. Analytics and privacy
Potential analytics include downloads, update adoption, compatibility failures and aggregate usage. Minimize collection, disclose telemetry, provide opt-out where appropriate and avoid exposing player identities or private server details. Public metrics must resist abuse.

## 21. API boundaries
Logical capabilities: create release draft; generate manifest; validate; request/revoke approval; publish/withdraw; query release history; check updates; generate update plan; confirm/apply update; create/verify backup; roll back supported artifacts; report/moderate release. Concrete endpoint schemas are deferred to API contract work.

## 22. Security
Treat packages and dependencies as untrusted. Scan artifacts, verify hashes, isolate build/install operations, validate archives, enforce quotas, protect credentials, rate-limit privileged endpoints and audit actions. Dependency downloads require trust policy and integrity checks. Do not execute arbitrary post-install scripts without sandboxing and explicit authorization.

## 23. Failure handling
Classify validation, compatibility, permission, provider, upload, storage, signing, dependency, migration, backup, install and rollback failures. Publication is atomic from the catalog perspective. Failed update application leaves a recoverable state and actionable diagnostics. Preserve logs without leaking secrets.

## 24. Acceptance criteria
- Users can publish one component or a selected subset.
- Releases are immutable and reproducibly identifiable.
- Manifests pin exact component and asset versions.
- Compatibility and test evidence is visible; missing tests are not_run.
- Ownership and permissions are enforced.
- Risky update plans show impact before changes.
- Backups are verified before destructive migration where feasible.
- Rollback limitations are explicit.
- Withdrawn/deprecated releases remain auditable.
- Package integrity and provenance are available.
- No world or server is modified without explicit confirmation.

## 25. Test strategy
Test semantic versioning, manifest pinning, compatibility matrices, dependency conflicts, immutability, permissions, upload atomicity, hash/signature verification, archive traversal, malware scanning, update discovery, migration previews, backup integrity, rollback, withdrawal, moderation, rate limits and concurrent operations. Run end-to-end tests for each supported platform. Human playtesting remains separate.

## 26. Open decisions
1. Which destinations are included in the first release?
2. Is the Studio catalog hosted by the project or federated?
3. Which versioning convention is mandatory for each artifact type?
4. Is signing mandatory, optional or staged?
5. Who can publish within collaborative projects?
6. Which moderation actions require a second reviewer?
7. What is the minimum compatibility test matrix?
8. Which installation paths can be automated safely?
9. What backup strategy and retention period are required?
10. Which migrations require mandatory confirmation?
11. What rollback guarantees can be offered for worlds and servers?
12. Which analytics are collected and what is the opt-out policy?
13. Are paid assets or monetization supported?
14. What appeal and takedown process applies?
15. Which external distribution adapters are approved?

## 27. Implementation boundary
This specification is design only. It does not claim that a catalog, signing service, updater, installer, backup service, moderation system or external integration has been implemented.

## 28. Related specifications
Integrates with Product Requirements, Project Manifest, Project Architect Decision Engine, Modpack Dependency Resolver, all production engines, AI Asset Generation Pipeline, Security/Permissions/Moderation, Storage/Backup/Recovery, API Contract and Community Workspace specifications.