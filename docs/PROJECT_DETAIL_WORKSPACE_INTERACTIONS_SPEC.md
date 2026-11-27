# Project Detail Workspace Interaction Specification v1.0

Status: Design specification
Product: Minecraft AI Mod Studio
Scope: Detailed interaction rules for the project detail workspace
Implementation status: Not implemented
Prerequisite: PROJECTS_WORKSPACE_SPEC.md
Design-first rule: This document defines intended behavior; it does not authorize coding.

## 1. Core interaction principles

1. The project detail workspace is the authoritative working context for one project.
2. Text chat, voice sessions, plans, requirements, components, files and test evidence must resolve to the same project identity.
3. AI recommendations are proposals, not applied changes.
4. The user can accept, reject or edit a proposal before it changes project state.
5. Material scope changes create a new plan revision and return the project to the appropriate analysis/approval state.
6. Every consequential action must be attributable to an actor and recorded in project activity.
7. The interface must distinguish persisted facts, AI-generated proposals, generated artifacts and unverified previews.
8. A failed or unavailable operation must not be represented as successful.

## 2. Persistent workspace frame

### Header
Displays:
- Breadcrumb: My Projects / Project name
- Project name and editable description
- Edition and target Minecraft version, if selected
- Project lifecycle status
- Save/sync state
- Share/access control
- More actions

Header actions:
- Rename
- Edit description/tags
- Change project settings
- Share/manage access
- Archive
- Delete (confirmation and policy checks)

Changing edition, Minecraft version, loader or target platform triggers compatibility impact analysis. The interface must show affected components and unresolved incompatibilities before the change is committed.

### Main navigation
Tabs:
1. Overview
2. Conversation
3. Plan & Requirements
4. Components & Dependencies
5. Files & Artifacts
6. Builds & Tests
7. Versions & Releases
8. Team & Access
9. Activity

The active tab is reflected in the URL/deep link where supported. Switching tabs must not discard unsaved edits; prompt or preserve a draft.

### Contextual assistant panel
- Shows current project context and relevant next action.
- Presents suggestions as reviewable proposals.
- Can be collapsed on desktop and shown as a sheet on mobile.
- Does not silently alter project data.
- Must identify which plan revision and component a suggestion refers to.

## 3. Overview interactions

Display:
- Project description and tags
- Edition, version and loader/platform
- Component summary
- Current project state and separate component/build/test states
- Pending approvals and unresolved questions
- Recent verified activity
- Shortcuts to continue conversation, review plan, inspect files or view test evidence

Actions:
- Edit project metadata
- Open a component
- Continue AI conversation
- Review pending proposal
- Review latest build/test evidence

Progress indicators are permitted only when calculated from explicit, persisted task data. No estimated completion percentage without a defined calculation and source data.

## 4. Conversation interactions

### Message composer
- Text input
- Attachment control
- Voice session start/stop
- Send action
- Context indicator identifying the active project

### Conversation behavior
- Messages remain associated with the project.
- The assistant can summarize the request and identify missing information.
- Clarifying questions should be asked before creating a definitive plan when required details are missing.
- The assistant can create a proposed plan revision, but cannot approve it on the user's behalf.
- Voice and text share project context. Voice recording/transcription behavior must follow explicit consent and retention settings.

### Proposal review
A proposal must show:
- Summary of requested change
- Affected requirements
- Affected components and dependencies
- Compatibility/test implications
- What remains unchanged
- Whether a new approval is required

Actions: Accept proposal, Reject proposal, Edit proposal, Ask a question.

Accepting a proposal that materially changes scope creates a new plan revision. It does not automatically authorize artifact production.

## 5. Plan & Requirements interactions

Views:
- Current approved/proposed plan
- Requirements grouped by component or subsystem
- Open questions
- Plan revision history
- Approval history

Each requirement displays:
- Stable requirement ID
- Description
- Component ownership
- Priority
- Status
- Source (user request, accepted AI proposal, system constraint)
- Acceptance criteria
- Dependencies and rationale

Revision comparison:
- Added requirements
- Changed requirements
- Removed requirements
- Affected components
- Compatibility/test impact

Approval flow:
1. User opens a specific plan revision.
2. System displays the complete plan and unresolved warnings.
3. User explicitly approves or requests changes.
4. Approval record binds to the exact revision identifier/hash.
5. Any material change invalidates approval for the changed revision and requires a new approval.

Approval is not the same as build completion or publication.

## 6. Components & Dependencies interactions

Component list:
- Component name and stable ID
- Content type
- Target platform/version
- Technical owner
- Status
- Required/optional dependencies
- Last changed revision

Dependency graph:
- Nodes represent project components.
- Directed edges represent dependency relationships.
- Edge type distinguishes required and optional dependencies.
- Selecting a node opens component details.
- Selecting an edge explains why the dependency exists and what relies on it.

Component actions:
- Add component
- Configure component
- Propose component removal
- Inspect dependency impact
- Compare component revisions

Before removing or changing a component, show dependent components, affected requirements, files and tests. Block unsafe removal until dependencies are resolved or explicitly redesigned.

A component can be independently deliverable and publishable when its own requirements and release checks are satisfied.

## 7. Files & Artifacts interactions

Views:
- Project source tree
- Generated assets
- Build outputs
- Export packages

Each item displays:
- Name and file type
- Owning component
- Source/generated/build classification
- Revision or build association
- Size and checksum when available
- Validation state

Actions:
- Preview supported files
- Download existing artifacts
- Inspect metadata
- Compare revisions
- Export project source
- Export selected component

Rules:
- Do not show download actions for artifacts that do not exist.
- Do not label source files as runnable deliverables.
- Generated content must retain provenance to its plan revision and component.
- File replacement or deletion requires confirmation and dependency checks.

## 8. Builds & Tests interactions

Build history entries display:
- Build identifier
- Source/plan revision
- Minecraft edition/version
- Loader/platform
- Environment/toolchain
- Start/end time
- Result and logs

Test history separates:
- Schema and static validation
- Identifier/reference validation
- Dependency and compatibility validation
- Component build/compile
- Cross-component integration
- World load
- In-game or runtime behavior

Each test result is one of: Passed, Failed, Blocked, Not Run, or Inconclusive.

Rules:
- A compilation pass does not establish in-game playability.
- A test result is valid only for the tested revision and environment.
- Re-running tests creates a new test record; it does not overwrite prior evidence.
- Failed tests may generate repair proposals; repairs require review and follow the approval rules when scope changes.

## 9. Versions & Releases interactions

Separate concepts:
- Plan revision: changes to agreed requirements and scope
- Source revision: changes to project source/content
- Build artifact: output produced by a specific build
- Release: immutable published package/version

Actions:
- Compare plan/source revisions
- View changelog
- Create release candidate
- Run release checks
- Publish release (authorized explicit action)
- Create a corrective release

A rollback creates a new working revision based on prior content; history is not erased. Published releases remain immutable.

## 10. Team & Access interactions

Roles:
- Owner
- Editor
- Reviewer
- Viewer

Permission matrix must be enforced by the backend, not merely by hiding UI controls.

Minimum behavior:
- Owner manages project ownership, members, visibility and deletion.
- Editor changes project content within granted scope.
- Reviewer reviews plans/proposals and submits review feedback; approval authority is separately configurable.
- Viewer can inspect permitted project data but cannot modify it.

Invitations:
- Invite by supported account identifier
- Choose role
- Show pending/accepted/expired state
- Revoke access
- Record access changes in activity

Private project conversation and unpublished assets must not leak into public publication/community views.

## 11. Activity interactions

Activity events include:
- Project metadata changed
- Conversation proposal created/accepted/rejected
- Plan revision created/approved
- Component/dependency changed
- File/artifact generated or replaced
- Build/test started and completed
- Release created/published
- Member invited/role changed/access revoked
- Project archived/restored/deleted

Each event records actor, timestamp, event type and affected object. Sensitive conversation content is not copied into public activity summaries.

## 12. Confirmation and recovery patterns

Require explicit confirmation for:
- Deleting a project or component
- Removing dependencies
- Replacing/deleting source or generated files
- Publishing a release
- Changing visibility from private to public
- Transferring ownership
- Revoking a collaborator's access where unsaved work may be affected

Where safe, provide undo for reversible actions such as archive or metadata edits. Irreversible actions must explain consequences before confirmation.

## 13. Responsive behavior

Desktop:
- Persistent project header and tab navigation
- Main content with optional contextual assistant panel
- Split views for plan comparison and dependency inspection

Tablet:
- Collapsible contextual panel
- Scrollable tab row
- Dialogs become full-height sheets when necessary

Mobile:
- Compact header with project identity and status
- Tabs become horizontally scrollable or a navigation sheet
- Assistant panel becomes a bottom sheet
- File tree and dependency graph use focused drill-in views
- Critical actions remain accessible without hover

## 14. Acceptance criteria

1. All tabs use one stable project identity and consistent context.
2. AI suggestions cannot silently mutate project data.
3. Material scope changes create a new plan revision.
4. Approval is tied to an exact plan revision.
5. Component changes expose dependency impact.
6. Independent components can be exported and published separately where valid.
7. Files and artifacts are clearly distinguished.
8. Build and test records are revision- and environment-specific.
9. Compilation is never equated with playability.
10. Access control is enforced server-side.
11. Destructive and public-facing actions have appropriate confirmation.
12. Desktop, tablet and mobile interaction behavior is defined.

## 15. Open design decisions

The following product decisions remain open and must be resolved before the complete design baseline is approved:
- Whether Reviewer can approve a plan or only submit review feedback.
- Whether ownership transfer is supported at initial release or deferred.
- Whether project deletion is immediate after confirmation or uses a recoverable trash/retention period.
- Whether release publication is always Owner-only or can be delegated.
