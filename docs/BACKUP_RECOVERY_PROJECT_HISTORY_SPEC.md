# Backup, Recovery & Project History Specification

**Status:** Design draft | **Version:** 1.0 | **Implementation:** Not implemented

## 1. Purpose
Define reliable snapshots, version history, recovery, restore, archival and audit-friendly change tracking for projects, manifests, source files, assets, generated outputs, settings and supported deployment metadata.

## 2. Principles
- Backups are separate from version control and are not a substitute for it.
- Preserve immutable snapshots and identify their exact contents by hashes.
- Make restore scope explicit and preview its impact before applying it.
- Never overwrite newer user work without explicit confirmation.
- Encrypt sensitive backup data and enforce access control.
- Verify backups through integrity checks and restore drills.
- Clearly distinguish backup created, backup verified and restore tested.

## 3. Protected data classes
Project manifests and specifications; source code and configuration; uploaded originals; generated assets and derivatives; build outputs; release metadata; project discussions and approval records where retention is permitted; user preferences; provider configuration references; and deployment metadata. Secrets are backed up only under a separately approved encrypted-secret policy, never as ordinary project files.

## 4. Snapshot types
Support manual snapshots, scheduled snapshots, pre-destructive-operation snapshots, pre-update snapshots, release snapshots and milestone snapshots. Each snapshot records scope, creator/system actor, timestamp, project revision, content hashes, parent snapshot and reason.

## 5. Snapshot consistency
Capture a consistent project state across manifest, files, asset registry, dependency graph and metadata. Use transactional snapshot boundaries or a manifest-based checkpoint protocol. Mark incomplete snapshots and never present them as restorable.

## 6. Version history
Track project revisions, document changes, asset versions, approvals, generated outputs, release tags and restore events. Provide diffs for text/configuration and metadata; binary assets use hashes, previews and version comparison where supported. Preserve authorship and timestamps.

## 7. Retention and lifecycle
Define retention tiers for recent, milestone, release and archived snapshots. Support expiration, legal hold and user-requested deletion subject to policy. Deduplicate by content hash without breaking snapshot reconstruction. Do not delete data still referenced by retained releases.

## 8. Storage architecture
Use a storage-provider abstraction supporting local storage and approved remote object storage. Store snapshot manifests separately from content blobs. Support chunking, deduplication, compression, encryption, integrity hashes and resumable transfer. Storage providers are not assumed to exist until configured.

## 9. Encryption and key management
Encrypt backups in transit and at rest. Define key ownership, rotation, recovery and revocation. Do not store encryption keys beside backup payloads. If a user-controlled key is lost, explain whether recovery is impossible; do not claim recoverability without key access.

## 10. Access control
Apply project roles and resource-level authorization to create, view, download, restore, delete and share snapshots. Shared project access does not automatically grant secret-backup access. Audit all restore and deletion actions.

## 11. Restore planning
Before restore, show selected snapshot, timestamp, included data, current revision, files that will change, files created after the snapshot, dependencies, compatibility concerns and potential data loss. Offer restore to a new branch/copy where supported.

## 12. Restore modes
Candidate modes: full project restore, selected component restore, selected file/asset restore, manifest-only restore, configuration restore and release artifact recovery. Restore modes must declare dependency implications and unsupported data classes.

## 13. Conflict resolution
Detect divergence between current state and snapshot. Offer keep-current, restore-snapshot, compare/merge for supported text formats, or restore-as-copy. Never silently merge binary assets or generated outputs. Require confirmation before replacing current files.

## 14. Recovery after failed operations
Create checkpoints before destructive migrations, bulk regeneration, dependency updates, installation and publishing operations where applicable. On failure, report completed and incomplete steps and offer a safe recovery plan. Automatic rollback is permitted only for operations with verified transactional semantics.

## 15. World and server data
World saves and server data require special handling: stop or quiesce writes where possible, snapshot consistent state, include relevant configuration and plugin/mod metadata, and verify world integrity after restore. Do not promise rollback of external player actions or third-party services.

## 16. Offline and local-first behavior
Support local snapshots when remote services are unavailable. Queue remote synchronization without overwriting newer revisions. Show local-only, syncing, synced, conflict and failed states. Define device-loss limitations for snapshots that never left the device.

## 17. Synchronization
Use immutable snapshot IDs and content hashes. Detect concurrent edits and divergent histories. Avoid last-write-wins for project source or manifests unless a specific field is explicitly safe for that strategy. Resolve conflicts through compare/merge or user selection.

## 18. Backup verification
Verify manifest signatures where used, blob hashes, completeness, decryptability and required dependency references. A successful upload is not proof that a backup can be restored. Schedule restore drills in isolated environments.

## 19. Disaster recovery
Define recovery objectives by data class: recovery point objective (RPO), recovery time objective (RTO), geographic redundancy, provider outage behavior and recovery ownership. These targets remain open until hosting and budget decisions are approved.

## 20. Export and portability
Allow users to export a portable project archive containing selected source, manifests, assets, metadata and optionally history. Document excluded data such as secrets, private discussions or unsupported external references. Include hashes and a restore/import manifest.

## 21. Audit and observability
Record snapshot creation, verification, restore preview, restore confirmation, deletion, retention expiry, synchronization conflict and recovery outcome. Include actor, timestamp, snapshot ID, project revision and result. Redact secrets.

## 22. Security
Protect against unauthorized restore, malicious archives, path traversal, backup poisoning, ransomware, tampered manifests, key theft and cross-project data leakage. Scan imported backups and restore into an isolated staging area before activation.

## 23. Performance and cost controls
Use incremental snapshots, content-addressed deduplication, compression and resumable transfer where appropriate. Expose storage usage, retention impact and estimated transfer size. Enforce quotas without deleting the only recoverable copy silently.

## 24. Acceptance criteria
- Snapshots identify exact project and component revisions.
- Snapshot consistency and completeness are recorded.
- Integrity verification is distinct from restore testing.
- Restore previews identify overwritten and missing data.
- Conflicts are never silently resolved for critical project data.
- Secrets are excluded unless a separate encrypted policy is approved.
- Local-first backup works without remote connectivity where configured.
- Restore operations are permission-checked and audited.
- World/server restore limitations are explicit.
- Users can export portable project data.

## 25. Test strategy
Test snapshot consistency under concurrent writes, incremental snapshot reconstruction, hash mismatch, interrupted uploads, encryption/key loss, unauthorized restore, archive traversal, cross-project isolation, retention expiry, conflict detection, partial restore, world restore in staging, offline synchronization, provider outage and full disaster-recovery drills.

## 26. Open decisions
1. Which data classes are included in the first release?
2. What is the default local snapshot location and quota?
3. Which remote storage providers are supported?
4. What are RPO/RTO targets for each data class?
5. What retention tiers and defaults apply?
6. Are backups encrypted with platform-managed or user-managed keys?
7. Is secret backup supported at all?
8. Which restore modes are required initially?
9. Is restore-to-new-copy mandatory where possible?
10. How are world/server snapshots coordinated with running processes?
11. What history is synchronized between devices?
12. How are concurrent edits and conflicts presented?
13. Which backup verification schedule is required?
14. What happens when storage quotas are reached?
15. What deletion/legal-hold rules apply?

## 27. Implementation boundary
This document is design only. It does not assert that snapshots, remote sync, encryption, retention, restore or disaster recovery currently exist.

## 28. Related specifications
Integrates with Project Manifest, Project Workspace, Asset Registry, AI Asset Generation Pipeline, Production Engines, Multiplayer/Server, Publishing/Versioning/Updates, Security/Permissions/Moderation, Storage Architecture and API Contract.