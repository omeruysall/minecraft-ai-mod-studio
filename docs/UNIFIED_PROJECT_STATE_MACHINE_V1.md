# Unified Project State Machine v1.0

**Status:** Proposed design | **Implementation:** Not implemented | **Approval:** Pending master design baseline

## 1. Purpose

Define consistent lifecycle states and guarded transitions for a Minecraft AI Mod Studio project from initial conversation through planning, approval, production, integration, testing and delivery. This specification separates the project lifecycle from component, job, approval, release and moderation lifecycles.

## 2. State ownership

- Project Architect owns the project-level workflow decision and transition orchestration.
- Manifest Service persists the canonical project revision and workflow summary.
- Approval Manager owns approval decisions and exact-revision approval evidence.
- Job Orchestrator owns production job and attempt states.
- Each domain engine owns its component-specific production states and evidence.
- Release Manager owns publication/release lifecycle.
- Authorization Policy Engine decides whether an actor may request a transition.
- Audit Service records privileged and lifecycle transitions.

No client or worker may directly set a project to an arbitrary state.

## 3. Project lifecycle states

| State | Meaning | Entry condition |
|---|---|---|
| DRAFT | Project exists; user intent is being collected | Project created |
| ANALYZING | AI and rules are extracting requirements | Conversation input available |
| CLARIFYING | Required information is missing or ambiguous | Analyzer identifies blocking questions |
| PLANNING | Technical plan and component graph are being prepared | Requirements sufficient for planning |
| AWAITING_APPROVAL | A versioned plan is ready for user decision | Plan and scope digest persisted |
| APPROVED | Exact revision and scope have valid approval | Approval Manager confirms |
| QUEUED | Approved production work is scheduled | Execution plan accepted |
| PRODUCING | One or more component jobs are running | Worker job starts |
| INTEGRATING | Component artifacts are being linked and assembled | Required component outputs available |
| VALIDATING | Static/build/load/runtime/gameplay checks are running | Integration candidate created |
| REPAIRING | A bounded repair plan is being executed | Actionable failure and repair authorization |
| READY_FOR_DELIVERY | Required acceptance gates passed | Required evidence complete |
| DELIVERED | User has received the declared outputs | Delivery record committed |
| COMPLETED | Project workflow is closed successfully | Delivery confirmed or configured completion rule met |
| BLOCKED | Progress cannot continue pending an external decision or dependency | Blocking condition recorded |
| FAILED | Unrecoverable failure for current execution/revision | Failure classified and recorded |
| CANCELLED | User or authorized administrator cancelled the workflow | Cancellation accepted |

A project may return to planning after a scope change, but it must create a new revision. Historical states and transitions remain auditable.

## 4. High-level transition map

- DRAFT → ANALYZING
- ANALYZING → CLARIFYING | PLANNING | BLOCKED
- CLARIFYING → ANALYZING | BLOCKED | CANCELLED
- PLANNING → CLARIFYING | AWAITING_APPROVAL | BLOCKED | FAILED
- AWAITING_APPROVAL → APPROVED | PLANNING | CANCELLED
- APPROVED → QUEUED | PLANNING | CANCELLED
- QUEUED → PRODUCING | BLOCKED | CANCELLED
- PRODUCING → INTEGRATING | REPAIRING | BLOCKED | FAILED | CANCELLED
- INTEGRATING → VALIDATING | REPAIRING | BLOCKED | FAILED
- VALIDATING → READY_FOR_DELIVERY | REPAIRING | BLOCKED | FAILED
- REPAIRING → QUEUED | PRODUCING | INTEGRATING | VALIDATING | BLOCKED | FAILED
- READY_FOR_DELIVERY → DELIVERED | VALIDATING | CANCELLED
- DELIVERED → COMPLETED
- BLOCKED → prior safe resumable state | PLANNING | CANCELLED | FAILED
- FAILED → PLANNING (new revision/attempt only) | CANCELLED
- CANCELLED is terminal for that workflow execution; a new execution requires an explicit resume/reopen operation and audit record.

## 5. Transition guards

Every transition must satisfy:
1. Authenticated actor or authorized system principal.
2. Permission for the project and requested operation.
3. Expected current state and expected manifest revision/digest.
4. Valid transition edge in this state machine.
5. Required preconditions and evidence.
6. Idempotency protection for retried requests.
7. Durable audit event.
8. No unresolved blocking invariant.

A stale revision or unexpected current state returns a conflict; it must not overwrite the latest state.

## 6. Approval gate

Production cannot begin unless:
- The plan is committed and immutable.
- Approval references the exact manifest revision digest.
- Approval references the exact plan/scope digest.
- The actor is authorized to approve.
- The approval has not been revoked.
- The approved target and component scope match the queued jobs.

Any scope-changing edit invalidates approval for the affected scope. The system returns the project to PLANNING or AWAITING_APPROVAL according to the change. Non-semantic metadata changes may avoid reapproval only if an explicit digest policy excludes them and the audit trail explains why.

## 7. Clarification and planning loops

Clarification is a first-class state, not a hidden chat condition. Each question has an ID, blocking/non-blocking classification, expected answer type and resolution state.

When blocking questions are answered, the project returns to ANALYZING. A new plan revision is created when requirement interpretation or component scope changes. Existing plans remain readable and are never overwritten.

## 8. Component lifecycle

Component states are separate from project states:
- PROPOSED
- PLANNED
- AWAITING_APPROVAL
- APPROVED
- QUEUED
- GENERATING
- GENERATED
- BUILDING
- BUILT
- VALIDATING
- TESTED
- INTEGRATED
- DELIVERED
- BLOCKED
- FAILED
- CANCELLED
- NOT_APPLICABLE

A project can have components in different states simultaneously. The project-level state is derived by Project Architect from required component states and workflow gates; it must not be a simple average or overwrite component truth.

## 9. Job lifecycle

Job Orchestrator owns:
- QUEUED
- DISPATCHED
- RUNNING
- RETRY_WAIT
- SUCCEEDED
- FAILED
- CANCEL_REQUESTED
- CANCELLED
- TIMED_OUT
- DEAD_LETTER

Each attempt has a unique ID, worker identity, start/end timestamps, bounded permissions, input revision digest, output references and structured failure. Job retries are idempotent or use isolated attempt outputs. A job success does not automatically mark its component tested or project completed.

## 10. Validation lifecycle and evidence

Test plans and test executions are distinct. Evidence results:
- PASSED
- FAILED
- BLOCKED
- SKIPPED
- NOT_RUN

A required test that is NOT_RUN blocks READY_FOR_DELIVERY unless an authorized waiver is recorded with rationale and scope. Static validation, compilation, loader startup, world load, runtime, multiplayer, performance and human gameplay tests are separate evidence classes.

## 11. Repair loop

Repair requires:
- A classified failure linked to evidence.
- A bounded repair proposal.
- Explicit policy on whether user approval is required for this repair class.
- A snapshot/checkpoint before destructive changes.
- A new attempt ID and traceable diff.
- Revalidation of impacted components and dependencies.

Repair must not silently change approved gameplay requirements or broaden scope. Scope change returns to planning and requires renewed approval.

## 12. Blocked, failed and cancelled semantics

BLOCKED means the workflow may resume when a named condition is resolved. FAILED means the current execution cannot proceed safely; recovery requires a new attempt or revision. CANCELLED means an authorized cancellation was accepted; workers receive cancellation signals and late outputs are quarantined rather than committed automatically.

These states are not interchangeable. Error messages must include stable codes, retryability and responsible owner.

## 13. Delivery and completion

READY_FOR_DELIVERY requires all mandatory deliverables, checksums, source references, installation instructions and required validation evidence. DELIVERED requires a durable delivery record and accessible artifact references. COMPLETED closes the project workflow; it does not imply public publication.

Publication is a separate Release Manager lifecycle. A delivered project can remain private or unpublished.

## 14. Revisions and state history

Every transition records event ID, project ID, from/to state, actor/principal, timestamp, manifest revision/digest, reason code, correlation ID and evidence references. State history is append-oriented.

A new project revision may cause a new workflow execution. Historical workflow executions retain their final status and links to the revision they processed.

## 15. Event contract

Lifecycle events use a versioned envelope:
- event_id
- event_type
- event_version
- project_id
- workflow_execution_id
- manifest_revision
- manifest_digest
- previous_state
- current_state
- actor_id or system_principal
- occurred_at
- correlation_id
- reason_code
- evidence_refs

Consumers must be idempotent, tolerate duplicate delivery and reject stale revision-sensitive commands.

## 16. Concurrency and distributed execution

Transitions use compare-and-swap semantics against current state and manifest revision. Workers receive immutable job input snapshots. A late worker result cannot move a newer project revision forward. Cancellation and timeout races are resolved by a documented terminal-state precedence rule and audited.

## 17. Security and abuse resistance

- Enforce permissions server-side for every requested transition.
- Workers cannot approve, publish or grant permissions.
- User-supplied text and generated code are untrusted.
- Rate-limit repeated planning, approval and job requests.
- Protect against replay using idempotency keys and event IDs.
- Record administrative overrides and require reason codes.
- Never expose secrets in transition events or logs.

## 18. Observability

Expose state duration, transition failure counts, blocked reasons, queue wait, job attempt counts, validation coverage and delivery success. Correlate conversation, plan, approval, job, artifact and evidence IDs without logging sensitive prompt content by default.

## 19. Recovery and reconciliation

On restart, reconcile persisted project state against job records and evidence. Do not infer success from missing worker heartbeats. Orphaned jobs are marked interrupted and safely retried or blocked. Inconsistent state is quarantined for reconciliation; no automatic destructive repair is allowed.

## 20. Acceptance criteria

- Every project transition is validated against an explicit transition table.
- Approval is bound to immutable revision and scope digests.
- Component and job lifecycles remain separate.
- Required tests cannot be treated as passed when not run.
- Stale worker results cannot mutate a newer revision.
- Blocked, failed and cancelled states have distinct semantics.
- Delivery and publication are separate.
- All privileged transitions are permission-checked and audited.
- State recovery is deterministic and does not fabricate success.
- State transitions are covered by positive, negative, concurrency and retry tests.

## 21. Open decisions

1. Whether CLARIFYING is a top-level state or a PLANNING substate in the first release.
2. Whether APPROVED is a durable project state or a short-lived gate before QUEUED.
3. Exact transition precedence for simultaneous cancellation, timeout and worker completion.
4. Whether human playtest is mandatory for every project category or selected release profiles.
5. Which repair classes may run without a new user approval.
6. Whether project reopen creates a new workflow execution ID or a new project revision plus execution.
7. Retention period for lifecycle event history.
8. Whether partial delivery is supported and how it affects COMPLETED.
9. Which transitions require multi-party approval for team projects.

## 22. Implementation boundary

This is a proposed lifecycle contract. It does not mean the backend currently implements these states, transition guards, event contracts or reconciliation logic.


## 23. Dual-edition first-slice completion gate

For the user-selected first playable milestone, the project contains separate Java and Bedrock target workflows under one shared project revision. Each target has its own component states, jobs, compatibility report, validation evidence and delivery bundle.

The overall milestone cannot enter READY_FOR_DELIVERY until:
- The Java target passes its required build, loader/world load, integration and gameplay gates.
- The Bedrock target passes its required pack import, world load, integration and gameplay gates.
- Each required target-specific test is PASSED or has an explicitly authorized waiver.
- The combined project export references both target bundles and their independent evidence.

A successful Java target does not compensate for a failed or untested Bedrock target. A successful Bedrock target does not compensate for a failed or untested Java target. Partial delivery may be offered only as a clearly labeled partial result and does not mark the dual-edition milestone complete.
