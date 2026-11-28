# Project Manifest v2 — Design Specification

**Version:** 2.0.0  
**Status:** Proposed design; awaiting project-wide baseline approval  
**Implementation status:** Not implemented  
**Compatibility:** v1.0.0 remains valid and immutable; v2 is a versioned migration target.

## 1. Purpose

The Project Manifest is the canonical, revisioned description of one Minecraft project. It connects user intent, requirements, target environment, component definitions, dependency relationships, assets, approvals, production jobs, validation evidence and delivery references.

The manifest is a project contract, not a build script, database dump, binary container or substitute for the domain engines.

## 2. Design principles

1. One canonical manifest per project revision.
2. Every generated or tested artifact is pinned to a manifest revision and component revision.
3. Stable IDs are independent of display names and file paths.
4. Component types are extensible; the initial supported types are not a closed list.
5. Project requirements, planned components, generated artifacts and test evidence are distinct concepts.
6. Approval binds to an immutable revision digest and an explicit scope.
7. Unknown optional extension fields may be preserved; unknown critical semantics must be rejected.
8. Schema migration is explicit, deterministic, auditable and reversible where practical.
9. Secrets, raw credentials, large binaries and unrestricted executable code are never embedded in the manifest.
10. A manifest can describe Java, Bedrock, server-side and mixed deliverables without pretending that incompatible targets are interchangeable.

## 3. Relationship to v1

The existing `schemas/project.schema.json` is schema version 1.0.0. It contains project identity, Minecraft target, workflow, boolean component flags, requirements, dependencies, open questions and a project revision.

V2 must not reinterpret v1 fields in place. A v1 document is parsed by the v1 schema and migrated into a v2 document by a named migration. The v1 source is retained as migration provenance. The boolean component flags are converted into component records with stable IDs; requirement and dependency records are preserved and enriched only where the source provides evidence.

No automatic migration may invent a loader, version, platform, dependency, approval or test result. Unknown or ambiguous values become explicit unresolved fields or migration warnings.

## 4. Top-level document structure

The v2 document contains:
- `manifest_version`: schema version.
- `project`: stable project identity and descriptive metadata.
- `revision`: monotonically increasing revision number, parent reference and content digest.
- `target`: Minecraft edition, version selection, loader/runtime and supported environment matrix.
- `workflow`: lifecycle state, stage, blocking reasons and approval requirement.
- `requirements`: normalized user requirements with provenance and acceptance criteria.
- `components`: typed component records and their own revisions.
- `dependency_graph`: explicit directed edges and constraints.
- `assets`: immutable asset-version references, not embedded asset bytes.
- `generation`: approved plan reference and production configuration references.
- `approvals`: revision-bound approval records or references.
- `validation`: test plans and evidence references, including explicit not-run state.
- `deliverables`: output artifact references and packaging metadata.
- `collaboration`: project membership references and role bindings.
- `extensions`: namespaced extension data with declared schema/version.

## 5. Project identity and revisioning

`project.id` is stable for the lifetime of the project. `revision.number` increases for every accepted canonical manifest change. `revision.parent_digest` points to the prior revision where applicable. `revision.digest` is calculated from a documented canonical serialization that excludes the digest field itself and volatile transport metadata.

Display names, descriptions and tags may change without changing project identity. Component IDs remain stable across revisions unless the component is intentionally replaced; replacement records a supersedes relationship.

A revision is immutable after commit. Edits create a new revision. Draft editing may use a working copy, but the committed manifest revision is never silently mutated.

## 6. Target model

Target selection distinguishes:
- edition: Java or Bedrock;
- Minecraft version: exact, range or user-selected unresolved target;
- loader/runtime: Fabric, Forge, NeoForge, Vanilla Java, Paper/Spigot/Bukkit or Bedrock runtime as applicable;
- Java runtime requirement where relevant;
- client/server deployment role;
- optional environment constraints such as server software, platform and feature flags.

A component may target only a subset of project targets. Mixed Java/Bedrock projects are represented as multiple target profiles and component compatibility declarations, not as one impossible combined runtime.

## 7. Component model

Each component record includes:
- stable `id`;
- `type` (for example java_mod, bedrock_addon, datapack, resource_pack, world, server_plugin, quest_pack, npc_pack, structure_pack, modpack, script_bundle);
- display name and description;
- lifecycle status;
- target profile references;
- requirement references;
- component revision;
- engine owner identifier;
- source and output references;
- dependency references;
- generation configuration reference;
- validation summary;
- optional `supersedes` and `tags`.

The component type registry is extensible. Unsupported component types must be preserved as opaque records when safe, but cannot be generated or installed by a client that lacks the relevant engine.

## 8. Requirement model

Requirements have stable IDs, human-readable descriptions, category, priority, source/provenance, confidence, lifecycle status, acceptance criteria, target component references and clarification state.

Provenance distinguishes user-authored statements, AI-extracted proposals, imported project data and system constraints. AI-extracted requirements remain proposed until confirmed according to the approval workflow. Acceptance criteria are testable where possible.

## 9. Dependency graph

Dependencies are first-class records with stable IDs, source and target component/feature references, relationship type, version constraints, optionality and resolution status.

Supported relationships include requires, references, generates, packages_with, conflicts_with, loads_before, tests and replaces. The graph must detect cycles where the relationship semantics prohibit them, explain unresolved edges and preserve edge provenance.

Compatibility claims belong to the Compatibility Engine; the graph stores constraints and relationships but does not independently declare a runtime combination compatible.

## 10. Assets and artifact references

The manifest stores references to immutable asset versions: ID, content hash, media type, provenance and optional license metadata. Binary content is stored in the Artifact Store/Asset Registry.

Generated source trees, build outputs, world files, pack archives and exports are artifact references. Paths alone are not identity. Every artifact reference should include an immutable object/version ID and checksum.

## 11. Workflow and state model

Workflow state is a summary, not the sole source of truth for every job. It includes current stage, lifecycle status, blockers and the revision to which the state applies.

The high-level stages are conversation, analysis, planning, awaiting_approval, production, integration, testing, repair, delivery and completed. Terminal or exceptional statuses include failed, blocked and cancelled where applicable. Detailed transition guards are defined in the Unified State Machine specification.

No production job may start unless the required approval record matches the exact manifest revision digest and approved scope. A scope-changing edit invalidates the prior approval for the changed scope and requires re-approval.

## 12. Approval records

An approval record contains approval ID, actor reference, timestamp, manifest revision, revision digest, approved plan/scope digest, decision and optional comment reference.

The manifest may embed a compact immutable approval summary or reference the authoritative Approval Manager record. The Approval Manager remains the canonical owner. Clients cannot forge approval by setting a manifest field.

## 13. Generation configuration

Generation settings are versioned references or typed non-secret values: engine version, template version, deterministic seed where relevant, user constraints and generation profile. Provider credentials, access tokens and secret environment variables are prohibited.

Engine-specific settings live in namespaced component configuration and are validated by the owning engine.

## 14. Validation and evidence

Validation separates planned tests from executed evidence. Each evidence record identifies test type, target, component/revision, tool/engine version, result, timestamp, logs/artifact references and environment metadata.

Allowed result values include passed, failed, blocked, skipped and not_run. Build success must not be represented as runtime or gameplay success. Missing evidence is not a pass.

## 15. Deliverables

A deliverable identifies format, target environment, artifact reference, checksum, source component revisions, packaging metadata and readiness state. Examples include JAR, ZIP source project, datapack ZIP, resource pack ZIP, world folder/archive, MCPACK/MCADDON and modpack archive.

The manifest records what was produced; it does not embed the binary. A release is separately owned by Release Manager and references a frozen manifest revision.

## 16. Collaboration and permissions

The manifest may contain membership references and role identifiers but does not define the global authorization policy. Identity and Authorization services remain authoritative for users, grants and permission decisions.

Sensitive membership details may be external references rather than embedded personal data. Permission checks occur server-side for every mutation and job action.

## 17. Extensibility and schema evolution

Extensions use reverse-domain or registered namespaces and carry their own version. Core fields cannot be shadowed by extensions. Required extension semantics are declared explicitly.

Patch changes add backward-compatible optional fields or clarify validation. Minor changes add compatible structures. Major changes may remove or alter semantics and require a migration. Consumers must reject unsupported major versions and preserve unknown optional extension payloads where possible.

## 18. Canonical serialization and digest

Define a canonical JSON serialization profile before production implementation: deterministic object-key ordering, stable number/string encoding, UTF-8, normalized line endings and exclusion of volatile fields. Hash algorithm and digest prefix are versioned. The digest covers all approval-relevant content and referenced immutable version IDs.

A digest cannot be used as an authorization credential; it only binds records to content.

## 19. Migration from v1.0.0

Migration procedure:
1. Validate input against the v1 schema.
2. Preserve original bytes and source schema version as migration provenance.
3. Create project identity and revision metadata without changing the original project ID.
4. Convert each true component flag to a component record; false flags remain absent or explicitly disabled according to migration policy.
5. Map Minecraft edition/version/loader fields into a target profile without guessing missing values.
6. Preserve requirements, dependencies and open questions with stable IDs.
7. Convert the old workflow state using a documented mapping; do not treat legacy `approved` as sufficient evidence of a revision-digest-bound approval.
8. Emit warnings for ambiguous values and unresolved references.
9. Validate the v2 result and produce a migration report.
10. Require review before the migrated project can enter production.

Migration must be idempotent for the same source document and migration version.

## 20. Persistence and concurrency

The Manifest Service is the authoritative owner. Writes use optimistic concurrency with expected revision/digest. Concurrent edits produce a conflict requiring merge/review; they must not silently overwrite one another.

Large assets and artifacts are stored outside the manifest. Events announce committed revisions only after durable persistence.

## 21. API and event integration

The API exposes versioned read, create, draft, validate, commit, compare and migrate operations. Mutations include expected revision/digest and an idempotency key where retries are possible.

Events include project_id, revision_number, revision_digest, event_id, event_version and timestamp. Consumers must be idempotent and reject stale revision-sensitive commands.

## 22. Security and privacy

Validate schema, size limits, identifiers, references and extension namespaces. Reject path traversal, unsafe archive references and embedded secrets. Treat user/AI text as untrusted data. Authorization is checked at the service boundary and again before privileged worker actions. Logs redact credentials and sensitive user content.

## 23. Acceptance criteria

- v1 documents remain valid under the v1 schema.
- v1-to-v2 migration preserves known user data and reports ambiguity.
- A v2 project can contain multiple typed components and multiple target profiles.
- Every component has a stable ID and revision.
- Dependencies are explicit and independently resolvable.
- Assets and artifacts are referenced immutably by ID/hash.
- Approval is bound to a specific revision and scope digest.
- Tests distinguish not-run from passed.
- No secret or binary payload is stored in the manifest.
- Concurrent revision updates cannot silently overwrite one another.
- Unknown optional extension data is handled according to the compatibility policy.

## 24. Open decisions

1. Canonical digest algorithm and canonical JSON profile.
2. Whether project revisions use integer sequence only or include immutable UUIDs.
3. Exact target-profile model for projects spanning Java and Bedrock.
4. Whether component configurations are inline or always external references.
5. Which membership metadata is safe to embed.
6. Whether a v1 legacy approved state is always reset to awaiting_review.
7. First-release extension registry governance.
8. Retention and archival policy for old manifest revisions.
9. Whether artifact references are stored directly in the manifest or through a separate artifact index.
10. Which component types are included in the first playable vertical slice.

## 25. Implementation boundary

This document defines the v2 contract and migration requirements. It does not mean the Manifest Service, v2 API, migration tool, digest implementation or production engines have been implemented.

## 26. Related documents

Component Ownership Matrix v1, Master Integration Audit v1, API Contract v2 Design, Project Architect Decision Engine, Minecraft Version Compatibility Engine, production engine specifications, Security/Permissions/Moderation and Backup/Recovery.


## 27. Dual-edition first playable project

The first user-selected milestone targets both Java and Bedrock. A single manifest must contain separate target records with independent edition, version selection, runtime, loader/API constraints and deployment roles.

Rules:
- Java target uses `edition: java`; Bedrock target uses `edition: bedrock`.
- Every component lists the target IDs it belongs to.
- A Java mod/JAR, Java datapack, Bedrock behavior pack and Bedrock resource pack are distinct component/artifact types.
- A shared user requirement may link to multiple target-specific component implementations.
- Java and Bedrock components must not share a build job or be treated as interchangeable binaries.
- Target-specific dependency graphs and validation evidence must be preserved.
- A project export may contain both target bundles, but each bundle remains independently installable and testable.
- Datapack components are Java-specific. Bedrock behavior must be represented through Bedrock-native pack/API components, not a Java datapack flag.

The updated example manifest demonstrates two target profiles and separate components. Exact versions and loader/API levels intentionally remain unresolved.
