# API Contract v2 — Design Specification

**Status:** Design draft | **Version:** 2.0.0 | **Implementation:** Not implemented

## 1. Purpose and scope
Define a consistent versioned API surface for the Studio control plane and asynchronous production workflows. This is a logical contract proposal; it does not claim endpoints currently exist. REST/JSON is the initial external API style. Internal events and worker messages may use separate contracts.

## 2. Contract principles
- All routes are versioned under `/api/v2`.
- Resource IDs are stable and opaque; IDs never replace authorization.
- Every mutation is authenticated and authorized server-side.
- Project mutations use optimistic concurrency with `If-Match` or an explicit expected revision.
- Long-running work returns a job resource; requests do not hold open connections while builds run.
- Idempotency keys protect retryable create/submit operations.
- Errors use one structured envelope with stable machine-readable codes.
- Pagination, filtering, sorting, rate limits and request IDs are consistent.
- Secrets and provider credentials are write-only; never return their values.
- Every response distinguishes declared state from verified evidence.

## 3. Base conventions
Base path: `/api/v2`. JSON uses UTF-8. Timestamps use ISO 8601 UTC. IDs are opaque strings. Binary payloads use multipart upload or pre-authorized object-storage transfers. Large artifacts are not embedded in JSON.

Mutating requests should include `Idempotency-Key` where retry could create duplicate work. Project-scoped updates include `If-Match: <revision-etag>` or `expected_revision`. A stale write returns `409 REVISION_CONFLICT` with current revision metadata; it must not silently overwrite newer state.

## 4. Standard response and error envelopes
Resource responses include `data`, optional `included`, and `meta` with request_id and pagination/revision details where applicable.

Errors include `error.code`, `error.message`, `error.retryable`, optional `error.details`, and `meta.request_id`. Stable codes include `UNAUTHENTICATED`, `FORBIDDEN`, `NOT_FOUND`, `VALIDATION_FAILED`, `REVISION_CONFLICT`, `APPROVAL_REQUIRED`, `INCOMPATIBLE_TARGET`, `DEPENDENCY_CONFLICT`, `QUOTA_EXCEEDED`, `RATE_LIMITED`, `JOB_CANCELLED`, `PROVIDER_UNAVAILABLE` and `INTERNAL_ERROR`.

## 5. Authentication and account
- `POST /auth/sessions` — create session.
- `POST /auth/sessions/refresh` — rotate session credentials.
- `DELETE /auth/sessions/current` — revoke current session.
- `GET /account` — current account profile and capability summary.
- `GET /account/sessions` — list sessions/devices.
- `DELETE /account/sessions/{session_id}` — revoke a session.

Authentication provider selection, MFA and offline/local mode remain policy decisions. Authorization is checked on each resource request.

## 6. Projects and revisions
- `POST /projects` — create project shell and initial draft.
- `GET /projects` — list projects visible to the caller.
- `GET /projects/{project_id}` — retrieve current project summary and manifest reference.
- `PATCH /projects/{project_id}` — update permitted project metadata with revision precondition.
- `DELETE /projects/{project_id}` — request soft deletion subject to policy.
- `GET /projects/{project_id}/revisions` — list revisions.
- `GET /projects/{project_id}/revisions/{revision_id}` — retrieve immutable revision.
- `POST /projects/{project_id}/revisions/{revision_id}/restore-plan` — prepare a restore proposal, not immediate overwrite.

## 7. Conversation and requirements
- `POST /projects/{project_id}/conversations` — create or resume conversation.
- `GET /projects/{project_id}/conversations/{conversation_id}/messages` — paginated history.
- `POST /projects/{project_id}/conversations/{conversation_id}/messages` — submit text or attachment references; returns normalized response or planning job.
- `POST /projects/{project_id}/requirements/analyze` — request requirement extraction.
- `GET /projects/{project_id}/requirements` — list requirement records.
- `PATCH /projects/{project_id}/requirements/{requirement_id}` — update user-confirmed requirement.

Voice transport is a separate realtime contract. Audio sessions must map to the same conversation and project revision; raw audio is not assumed to be retained.

## 8. Planning and approval
- `POST /projects/{project_id}/plans` — create/revise plan from requirements.
- `GET /projects/{project_id}/plans/{plan_id}` — retrieve plan, assumptions, open questions and component proposals.
- `POST /projects/{project_id}/plans/{plan_id}/approval` — approve exact plan revision and declared scope.
- `POST /projects/{project_id}/plans/{plan_id}/changes` — submit scope change and create a new plan revision.
- `GET /projects/{project_id}/approvals` — approval history.

Approval request includes `plan_revision`, `scope_hash`, `decision` and optional comment. Production endpoints reject stale, missing or mismatched approvals. Approval does not automatically approve future scope changes.

## 9. Components and dependency graph
- `GET /projects/{project_id}/components` — list component instances.
- `POST /projects/{project_id}/components` — add component to a draft revision.
- `GET /projects/{project_id}/components/{component_id}` — retrieve component spec and artifact references.
- `PATCH /projects/{project_id}/components/{component_id}` — revise component with concurrency precondition.
- `GET /projects/{project_id}/dependencies` — retrieve dependency graph.
- `POST /projects/{project_id}/dependencies/validate` — submit graph validation job.
- `POST /projects/{project_id}/impact-analysis` — calculate affected components after a proposed change.

## 10. Compatibility and catalog
- `GET /compatibility/targets` — discover supported edition/version/loader/runtime targets.
- `POST /compatibility/checks` — evaluate a proposed target and dependency set.
- `GET /catalog/features` — search feature catalog and retrieve feature records.
- `GET /catalog/features/{feature_id}` — retrieve stable feature definition.

Compatibility results must include evidence freshness, source, target tuple and explicit unknown states. A target not listed as supported is not presumed compatible.

## 11. AI provider configuration
- `GET /ai/providers` — list configured provider capabilities without secrets.
- `POST /ai/provider-configurations` — create provider configuration; secret fields are write-only.
- `PATCH /ai/provider-configurations/{configuration_id}` — rotate/update credentials or settings.
- `DELETE /ai/provider-configurations/{configuration_id}` — revoke configuration.
- `POST /ai/route-preview` — explain eligible model routes and expected constraints.

Provider calls must be mediated by the AI Gateway and policy/budget controls. Client code never receives provider secrets.

## 12. Assets
- `POST /projects/{project_id}/assets/briefs` — create asset brief.
- `GET /projects/{project_id}/assets` — list assets and versions.
- `GET /projects/{project_id}/assets/{asset_id}` — retrieve asset metadata.
- `POST /projects/{project_id}/assets/uploads` — create upload intent.
- `POST /projects/{project_id}/assets/jobs` — submit generation/import/conversion job.
- `GET /projects/{project_id}/assets/{asset_id}/versions/{version_id}` — retrieve immutable version metadata.
- `POST /projects/{project_id}/assets/{asset_id}/versions/{version_id}/review` — approve/request changes/reject exact version.

Binary content uses authorized transfer URLs or a controlled upload service. The API returns hashes and provenance, not arbitrary local file paths.

## 13. Production jobs
- `POST /projects/{project_id}/jobs` — submit approved component production job.
- `GET /projects/{project_id}/jobs` — list jobs.
- `GET /jobs/{job_id}` — retrieve status/progress.
- `GET /jobs/{job_id}/logs` — paginated structured logs.
- `POST /jobs/{job_id}/cancel` — request cancellation.
- `POST /jobs/{job_id}/retry` — retry eligible failed job with idempotency and policy checks.

Every job pins project revision, plan approval, component versions, dependency resolution and input hashes. Cancellation is cooperative and reports whether outputs were already committed.

## 14. Validation, build and test evidence
- `POST /projects/{project_id}/validations` — request static/integration validation.
- `POST /projects/{project_id}/builds` — request isolated build.
- `POST /projects/{project_id}/tests` — request a named test suite and target matrix.
- `GET /projects/{project_id}/evidence` — list reports.
- `GET /evidence/{evidence_id}` — retrieve report and artifact references.

Evidence statuses: `not_run`, `queued`, `passed`, `failed`, `blocked`, `skipped`. Evidence records test type, target tuple, toolchain, artifact hash, timestamp, logs and report reference. Build, load, runtime, multiplayer, performance and human playtest remain separate categories.

## 15. Exports and artifacts
- `POST /projects/{project_id}/exports` — assemble export from pinned revision.
- `GET /projects/{project_id}/exports` — list exports.
- `GET /exports/{export_id}` — retrieve export manifest/status.
- `POST /exports/{export_id}/download-intent` — obtain authorized download transfer.

Exports must identify editable source, runtime artifacts, compatibility report, provenance, checksums and test evidence. Download links are short-lived and permission-checked.

## 16. Publishing and releases
- `POST /projects/{project_id}/releases` — create release draft from pinned revision.
- `GET /projects/{project_id}/releases` — list releases.
- `GET /releases/{release_id}` — retrieve release metadata.
- `POST /releases/{release_id}/validate` — validate release gate.
- `POST /releases/{release_id}/publish` — publish approved release.
- `POST /releases/{release_id}/withdraw` — withdraw with reason.
- `GET /releases/{release_id}/updates` — check update relationship.

## 17. Backup and restore
- `POST /projects/{project_id}/snapshots` — create snapshot.
- `GET /projects/{project_id}/snapshots` — list snapshots.
- `GET /snapshots/{snapshot_id}` — inspect snapshot metadata and verification.
- `POST /snapshots/{snapshot_id}/verify` — request integrity verification.
- `POST /snapshots/{snapshot_id}/restore-plans` — prepare restore preview.
- `POST /restore-plans/{restore_plan_id}/confirm` — confirm an exact restore plan.

Restore is never triggered by a GET request. Confirmation includes snapshot ID, destination, overwrite set and expected current revision.

## 18. Collaboration, moderation and audit
- `GET /projects/{project_id}/members` and `POST /projects/{project_id}/invitations`.
- `PATCH /projects/{project_id}/members/{member_id}` and `DELETE /projects/{project_id}/members/{member_id}`.
- `POST /reports` — report community content or behavior.
- `GET /moderation/cases` and `GET /moderation/cases/{case_id}` — moderator-only case access.
- `POST /moderation/cases/{case_id}/actions` — apply authorized moderation action.
- `GET /projects/{project_id}/audit-events` — authorized audit history.

Exact roles, reviewer powers, appeal workflow and retention are governed by the Security and Community specifications.

## 19. Realtime and event delivery
Use a documented WebSocket or server-sent event channel for job updates and realtime voice signaling where selected. Event payloads include event_id, event_type, resource_id, project_id, revision, timestamp and minimal changed fields. Clients must be able to recover missed events through ordinary GET endpoints.

## 20. API security requirements
Enforce object-level authorization, CSRF protection where cookie sessions are used, input validation, output encoding, rate limits, request size limits, idempotency, audit logging, secret redaction and secure transfer URLs. CORS is allowlist-based. No worker or client is trusted to enforce project approval.

## 21. Observability
Every request has a correlation/request ID. Jobs propagate trace IDs across queue, worker and artifact storage. Metrics avoid high-cardinality user content. Logs redact tokens, keys, private prompts and sensitive metadata.

## 22. API versioning and deprecation
Breaking contract changes require a new major API version or an explicit compatibility period. Additive fields are optional for older clients. Publish deprecation dates and migration guides. Manifest schema versioning is independent of API versioning.

## 23. Contract test requirements
Generate schema validation tests for requests/responses. Test authentication, object authorization, stale revisions, approval bypass attempts, idempotency, pagination, cancellation, retries, rate limits, secret redaction, upload isolation, job event recovery and end-to-end export. Maintain compatibility tests for supported client versions.

## 24. Open decisions
1. Cookie sessions or bearer tokens, or a platform-specific hybrid?
2. REST-only or REST plus GraphQL for catalog queries?
3. WebSocket or SSE for job events?
4. Which voice transport is used and where is audio processed?
5. Which upload/download object storage provider is selected?
6. Which API endpoints are required for the first vertical slice?
7. Which roles and permission scopes are enforced in v2?
8. What are rate-limit and payload-size defaults?
9. Which fields are immutable within a project revision?
10. How long are job logs and audit events retained?
11. Which external platform integrations are enabled?
12. What is the local/offline API behavior?

## 25. Implementation boundary
This is a proposed contract. Existing `/health` and `/v1` prototype endpoints are not evidence that these `/api/v2` routes exist. Implementation must follow approved schemas, permission policy, tests and migration design.

## 26. Related specifications
Integrates with Master Integration Audit, Architecture, Project Manifest, Project Architect Decision Engine, Compatibility Engine, AI Gateway, Asset Pipeline, Production Engines, Security, Publishing, Backup/Recovery and Development Plan.