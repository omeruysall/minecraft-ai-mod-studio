# Security & Permission Matrix v1.0

**Status:** Proposed design | **Implementation:** Not implemented | **Approval:** Pending master design baseline

## 1. Purpose and scope

Define role and permission boundaries for personal projects, team collaboration, generated artifacts, local/server installation and community publishing. This is a policy design. It does not claim that the current prototype enforces these controls.

## 2. Security principles

- Deny by default; grant least privilege.
- Authorization is server-side and resource-scoped.
- Authentication proves identity; authorization decides the requested action.
- Project roles do not automatically grant platform-wide administration.
- Workers and AI agents use constrained service identities, never user-equivalent credentials.
- Approval, publication, installation, restore and destructive actions are distinct permissions.
- Every privileged action is auditable.
- UI visibility is not an authorization boundary.
- Secrets are stored in a credential vault and never placed in manifests, prompts, logs or generated artifacts.
- Public community access is separate from private project membership.

## 3. Principal categories

| Principal | Description | Default trust |
|---|---|---|
| Anonymous visitor | Unauthenticated community visitor | Public read only |
| Authenticated user | Signed-in account | Own resources only |
| Project owner | Project creator/current owner | Project administration |
| Project editor | Collaborator with edit grant | Scoped editing |
| Project contributor | Assigned contributor | Assigned component/task only |
| Project reviewer | Reviews plans and outputs | Read/review/comment |
| Project approver | Explicitly granted approval authority | Approve defined scope |
| Project viewer | Read-only member | Project read |
| Moderator | Community moderation staff | Moderation cases, not project ownership |
| Platform administrator | Platform operations and policy administration | Explicit administrative scopes |
| Service principal | Backend service identity | Specific API scopes |
| Worker principal | Isolated build/test/generation worker | Single job and pinned inputs |
| AI provider principal | External model/provider identity | Provider-scoped API use |

Role names are not interchangeable. A moderator does not gain access to private project source solely by being a moderator. A platform administrator's access is logged and should be limited to operational necessity.

## 4. Resource scopes

Permissions are evaluated against:
- platform;
- user account;
- project;
- project revision;
- component;
- conversation/session;
- asset/artifact;
- job/attempt;
- approval;
- release/listing;
- moderation case;
- backup/restore operation;
- provider credential;
- server/deployment target.

A grant may be restricted by target environment, component IDs, action set, expiry and policy conditions.

## 5. Action vocabulary

Core actions:
- read, list, search, download;
- create, update, delete, archive, restore;
- invite, remove_member, change_role, transfer_owner;
- comment, review, request_changes;
- approve, reject, revoke_approval;
- plan, generate, build, test, cancel_job, retry_job;
- export, publish, unpublish, manage_release;
- install, deploy, update, rollback;
- configure_provider, use_provider, rotate_secret, revoke_secret;
- create_backup, restore_backup, delete_backup;
- report, moderate, appeal, resolve_case;
- administer_policy, manage_platform, view_audit.

Actions are explicit. A broad edit grant does not imply approval, publication, deployment, credential access or platform administration.

## 6. Project role matrix

Legend: A = allowed by default in that role; G = only when separately granted; — = denied by default.

| Action | Owner | Editor | Contributor | Reviewer | Approver | Viewer |
|---|---:|---:|---:|---:|---:|---:|
| Read project and revisions | A | A | scoped A | A | A | A |
| Edit project requirements | A | A | scoped G | — | — | — |
| Edit assigned component | A | A | scoped A | — | — | — |
| Create plan revision | A | A | G | — | — | — |
| Request generation | A | A | scoped G | — | — | — |
| Approve plan/scope | G | G | — | — | A | — |
| Review/comment | A | A | A | A | A | G |
| Cancel own job | A | A | scoped A | — | — | — |
| Cancel any project job | A | G | — | — | G | — |
| Download private artifacts | A | A | scoped A | G | G | G |
| Invite/remove members | A | G | — | — | — | — |
| Change project roles | A | G | — | — | — | — |
| Transfer project ownership | A* | — | — | — | — | — |
| Delete/archive project | A* | — | — | — | — | — |
| Publish project/release | A* | G | — | — | G | — |
| Install/deploy to target | G | G | — | — | G | — |
| Manage provider credentials | Own credentials only | Own credentials only | — | — | — | — |
| Restore project backup | A* | G | — | — | — | — |
| View project audit history | A | G | scoped G | G | G | — |

`A*` means sensitive action requiring step-up authentication, explicit confirmation and audit. Approval is not implicitly included in ownership for a multi-person team if a separation-of-duties policy is enabled. The first-release policy remains an open decision.

## 7. Separation of duties

Where enabled:
- The actor who proposes a plan cannot approve it for a protected project.
- A worker cannot approve the job it executes.
- A publisher cannot bypass release validation.
- A moderator cannot approve private project production.
- Backup restoration requires a distinct confirmation from ordinary project editing.
- High-risk platform policy changes require a second authorized administrator or documented emergency override.

The exact mandatory separation rules are configurable policy, not hardcoded assumptions.

## 8. Platform role matrix

| Action | User | Moderator | Platform admin |
|---|---:|---:|---:|
| Manage own account/settings | A | A | A |
| Access own projects | A | A | A |
| Read public listings | A | A | A |
| Review community reports | — | A | G |
| Hide/remove violating public listing | — | G | A |
| Suspend community publishing privileges | — | G | A |
| Manage platform-wide roles/policies | — | — | A |
| Access private project content | Own/granted only | Case-scoped G | Break-glass G |
| Read security audit logs | Own activity | Case-scoped G | A |
| Access provider secrets | Own authorized secret only | — | No plaintext by default |

Break-glass access is time-limited, justified, logged, and subject to post-access review.

## 9. Service and worker permissions

Service identities receive narrow machine scopes:
- Project Architect: read requirements/catalog/manifest; request plan and approval evaluation.
- Manifest Service: validate and commit manifest revisions.
- Approval Manager: create/verify/revoke approval records.
- Job Orchestrator: create and dispatch jobs; update job lifecycle.
- Domain worker: read pinned inputs and write outputs to its job namespace only.
- Build/test worker: execute in isolated sandbox; no direct credential vault access or unrestricted network.
- Integration worker: read component artifacts and write integration outputs.
- Release Manager: create immutable release records from approved deliverables.
- Backup service: snapshot/verify/restore according to dedicated policy.

Worker credentials are short-lived, audience-bound and scoped to a single job, project and revision. Workers cannot mutate canonical project ownership, approval, user roles or platform policy.

## 10. AI agent permissions

AI agents are not trusted principals merely because they are part of the product. They may:
- read only context authorized for the user and task;
- propose requirements, plans, code and assets;
- call explicitly allowlisted tools through policy mediation;
- write only to isolated draft/job workspaces.

They may not independently:
- approve plans;
- grant roles or permissions;
- publish or deploy;
- read unrelated projects;
- access raw provider credentials;
- execute arbitrary shell/network operations outside the sandbox;
- bypass user confirmation for destructive operations.

User confirmation is required for high-impact actions, and tool calls are checked server-side.

## 11. Permission evaluation model

Decision inputs:
- principal identity and authentication assurance;
- active role grants;
- resource ownership and membership;
- requested action;
- resource/project/revision scope;
- target environment;
- grant expiry and revocation state;
- risk classification;
- contextual policy (e.g. separation of duties, moderation hold).

Decision outputs: allow, deny or require_step_up/confirmation. A denied or indeterminate decision fails closed.

Policy evaluation is centralized, while enforcement occurs at every API, worker dispatch, artifact download and deployment boundary.

## 12. Ownership, invitations and transfer

Project ownership is a canonical project grant. Invitations are pending until accepted. Invitations have expiry, intended role and project scope. Role changes and removals are audited and revoke relevant sessions/grants promptly.

Ownership transfer requires recipient acceptance, current-owner authorization and step-up confirmation. Recovery of an inaccessible owner account is a separate verified support workflow; moderators cannot silently transfer ownership.

## 13. Approval permissions

Approval permission is separate from edit permission. The approval record binds actor, project, manifest revision digest, plan/scope digest, decision and timestamp. Any scope change invalidates approval for the changed scope. Approval API checks current grants at decision time and stores an immutable audit event.

## 14. Publishing and licensing permissions

Publishing requires project-level publish permission, release readiness, required validation evidence, license/attribution checks and content-policy checks. Publishing a map-only or component-only artifact must not expose unrelated private project components.

Unpublish, takedown and appeal are separate actions. A public listing may be removed while immutable audit/release records remain available to authorized reviewers.

## 15. Artifact and data access

Artifact access is mediated by resource authorization, not guessable URLs. Download links are short-lived and scoped. Private artifacts are never exposed through public catalog indexes. Generated archives are scanned and path traversal/symlink hazards are rejected before extraction or installation.

## 16. Provider credentials and external integrations

Credentials are encrypted at rest, masked in UI, scoped by provider, and revocable. AI requests use credential references, never raw secret values in project manifests. Provider usage is attributed to the authorized account/project according to policy. External provider failure must not leak prompts or secrets into public logs.

## 17. Local installation and server deployment

Installation/deployment is a high-impact permission. The user must choose target path/server, review changes and confirm. Backups are created before overwriting existing files where supported. The system does not install to arbitrary paths or execute untrusted artifacts without explicit authorization and security checks.

## 18. Backup and restore permissions

Backup creation and restore are distinct permissions. Restore preview identifies overwritten files, revision conflicts and data loss risks. Restore requires explicit confirmation and creates an audit record. Restore must not bypass project membership or resurrect revoked grants.

## 19. Moderation and appeals

Moderators operate on assigned cases and public/community scope. Actions include warning, hide listing, remove content, restrict publishing and suspend accounts where policy authorizes. Each case stores evidence references, reason codes, actor and appeal status. Moderation does not grant blanket access to private source files.

## 20. Audit requirements

Audit records include actor/principal, action, resource, scope, decision, reason, timestamp, correlation ID, policy version and relevant revision IDs. Record role changes, approvals, publishing, downloads of sensitive artifacts, credential changes, restore, deployment, moderation and break-glass access.

Audit logs are append-oriented, access-controlled and tamper-evident. Sensitive payloads and secret values are excluded.

## 21. Threat and abuse controls

- CSRF/session fixation/replay protections appropriate to the client architecture.
- Rate limits for authentication, invitation, generation and publishing.
- Idempotency keys for privileged mutations.
- Strict input validation and output encoding.
- Sandbox isolation for generated code and archives.
- SSRF/path traversal/zip-slip defenses.
- Dependency and artifact scanning.
- Prompt injection/tool abuse controls for AI agents.
- Tenant isolation and project-bound artifact access.
- Revocation propagation and short-lived worker credentials.
- Safe failure and quarantine for suspicious artifacts.

## 22. Permission testing

Required test classes:
- role/action allow-deny matrix tests;
- resource and tenant isolation tests;
- stale/revoked grant tests;
- approval separation-of-duties tests;
- worker privilege boundary tests;
- private artifact URL/access tests;
- ownership transfer and invitation expiry tests;
- moderation case-scope tests;
- provider secret redaction tests;
- backup/restore authorization tests;
- deployment confirmation and rollback tests;
- concurrency/replay/idempotency tests.

Every protected action requires at least one positive and one negative authorization test. Critical actions require adversarial and cross-tenant tests.

## 23. Acceptance criteria

- Default is deny.
- Every sensitive action has an explicit permission.
- Project roles do not imply platform roles.
- Approval, publish, install, restore and credential access are separate.
- Workers and AI agents are least-privileged and revision-scoped.
- Authorization is enforced server-side at every boundary.
- Public listing access cannot expose private components.
- Privileged actions are audited.
- Revoked permissions take effect for subsequent requests and job dispatch.
- Tests cover allowed and denied paths.

## 24. Open decisions

1. First-release role set and whether custom roles are supported.
2. Whether owner can self-approve or separation of duties is mandatory.
3. Whether reviewers can download source artifacts by default.
4. Ownership transfer and abandoned-project recovery policy.
5. Moderator access to private project material in exceptional cases.
6. Exact step-up authentication requirements for destructive actions.
7. Local-only mode identity and permission model.
8. Retention period and user visibility for audit events.
9. Whether team projects require two-person approval for publish/deploy.
10. Granularity of component-level contributor grants.

## 25. Implementation boundary

This matrix defines intended security policy and test obligations only. It does not establish that the current API, UI, worker runtime or storage layer implements these permissions.
