# Projects Workspace Specification v1.0

Status: Design specification
Product: Minecraft AI Mod Studio
Scope: Projects list, project detail workspace, lifecycle, filtering, collaboration entry points
Implementation status: Not implemented
Design-first rule: This document defines intended behavior; it does not authorize coding.

## 1. Purpose

The Projects workspace is the user's control center for all Minecraft creation work. It must support independent content projects (for example, a map-only release or a resource-pack-only project) and coordinated multi-component projects. A project is not required to contain a mod.

## 2. Information architecture

Primary navigation:
- Overview
- My Projects
- Drafts
- Shared Projects
- Published Projects (shortcut to creator publications)
- Archive

Projects page header:
- Page title and concise project count
- Search field
- New Project action
- Grid/list view toggle
- Sort control
- Filter control

Project categories:
- All Projects
- Drafts
- Awaiting Approval
- In Progress
- Needs Attention
- Completed
- Archived

Category counts must be derived from persisted project records, not hardcoded demo values.

## 3. Project card

Each card may display:
- Project cover/thumbnail, or a neutral placeholder when absent
- Project title
- Short description
- Project type summary (Mod, World/Map, Datapack, Resource Pack, Server Plugin, Bedrock Add-on, Modpack/Combined)
- Minecraft edition and target version, when selected
- Loader/platform, when applicable
- Lifecycle status
- Last updated timestamp
- Owner/creator and collaborator avatars, subject to access permissions
- Optional progress indicator only when backed by real task/build data

Card actions:
- Open project
- Continue conversation
- Duplicate project (creates a separate project with a new identity and provenance link)
- Share/manage access
- Archive
- Delete, subject to confirmation and retention policy

Do not display fabricated download counts, build success, test status, progress, or collaborator activity.

## 4. Search, filters, and sorting

Searchable fields:
- Project title
- Description
- Stable project identifier
- Component names
- Minecraft version
- Tags

Filters:
- Content type/component
- Edition: Java / Bedrock
- Minecraft version
- Loader/platform
- Lifecycle status
- Owner: mine / shared with me
- Updated date range
- Published / unpublished

Sort options:
- Recently updated
- Recently created
- Alphabetical
- Status
- Last opened

Search and filters must compose; clearing filters restores the unfiltered list. Empty states must explain why no results appear and offer a clear-filter action.

## 5. Project detail workspace

Project detail tabs:
1. Overview
2. Conversation
3. Plan & Requirements
4. Components & Dependencies
5. Files & Artifacts
6. Builds & Tests
7. Versions & Releases
8. Team & Access
9. Activity

Only show data that exists. If a feature is not implemented or a test has not run, label it clearly rather than implying completion.

### 5.1 Overview
- Project title, description, cover, tags
- Edition/version/platform selections
- Current lifecycle state
- Component summary
- Next required user action
- Recent activity backed by event records

### 5.2 Conversation
- Persistent project-specific text history
- Voice sessions and transcripts only with user consent and configured retention
- Attachments associated with the project
- Continue the same project context
- Scope changes create a new plan revision when material

### 5.3 Plan & Requirements
- Requirements grouped by subsystem/component
- Stable requirement identifiers
- Status and rationale
- Open questions
- AI recommendations separated from accepted requirements
- Plan revision history
- Explicit approval bound to a specific revision

### 5.4 Components & Dependencies
- Independent components listed as first-class items
- Dependency graph with required/optional relationships
- Technical ownership and compatibility notes
- Component status vocabulary consistent with the system inventory
- Add/remove/change component actions require impact analysis
- Removing a dependency must identify affected dependents

### 5.5 Files & Artifacts
- Source files and generated assets
- Artifact type, component ownership, version, checksum and provenance
- Download/export actions only when an artifact actually exists
- Preview supported formats in the integrated preview workspace
- Distinguish source project files from built deliverables

### 5.6 Builds & Tests
- Build history and logs
- Test runs, environment, version and results
- Separate static validation, compilation, integration, world-load and in-game tests
- Not-run tests remain explicitly marked Not Run
- Compilation success must never be presented as proof of playability

### 5.7 Versions & Releases
- Project plan revisions
- Source snapshots
- Build artifact versions
- Release records and changelogs
- Published releases are immutable; corrections create a new release
- Rollback creates a new working revision rather than erasing history

### 5.8 Team & Access
- Owner, collaborators and roles
- Invite and revoke access
- Least-privilege permissions
- Private, unlisted and public visibility
- Server-side authorization; UI visibility is not an authorization boundary

### 5.9 Activity
- Auditable events: project created, plan revised, approval granted, component changed, build/test run, release published, collaborator access changed
- Actor, timestamp, action and relevant object
- Do not expose private conversation content in public activity feeds

## 6. Lifecycle and status model

Project lifecycle states:
- Draft
- Analyzing
- Planning
- Awaiting Approval
- Approved
- In Progress
- Build Failed
- Testing
- Needs Attention
- Completed
- Archived

These are project-level states. Component, build, test, publication and release statuses remain separate dimensions. A project may contain components with different statuses.

State changes must be driven by recorded events and validated transitions, not manually fabricated progress percentages.

## 7. Empty, loading, and error states

First-use empty state:
- Explain that no projects have been created yet
- Offer Create New Project
- Offer discovery of public examples as a separate action

Filtered empty state:
- Explain that no projects match current filters
- Provide Clear Filters

Loading state:
- Use skeleton cards/list rows
- Preserve current filter context

Error state:
- Explain whether project data could not be loaded or an action failed
- Offer retry where safe
- Never silently replace failed data with demo content

## 8. Responsive behavior

Desktop:
- Full project navigation and filter sidebar
- Grid/list content area
- Project detail tabs
- Optional right-side contextual inspector

Tablet:
- Collapsible filters
- Two-column cards where space allows
- Detail tabs may scroll horizontally

Mobile:
- Single-column project cards
- Search and filters open in sheets
- Project detail tabs become a compact horizontal tab bar or menu
- Destructive actions require clear confirmation
- Touch targets and text remain accessible

## 9. Accessibility and usability

- Keyboard navigation and visible focus
- Screen-reader labels for icon-only actions
- Status must not rely on color alone
- Responsive text scaling
- Confirm destructive actions and explain consequences
- Provide undo where technically safe (for example, archive)
- Keep critical project actions discoverable

## 10. Data model requirements

Minimum conceptual entities:
- Project
- ProjectMember
- ProjectTag
- ProjectConversation
- ProjectPlanRevision
- Requirement
- Component
- ComponentDependency
- SourceFile
- BuildArtifact
- BuildRun
- TestRun
- Release
- Publication
- ProjectActivityEvent

Every project and component requires stable identifiers. Ownership and permissions must be enforced server-side. Project records must persist across sessions.

## 11. Acceptance criteria

The design is accepted for implementation only when:
1. Users can distinguish their own, shared, archived and published projects.
2. A map-only or other single-component project is fully supported.
3. Combined projects show component ownership and dependencies.
4. Search, filters, sorting and empty states are defined.
5. Project detail tabs and their data requirements are defined.
6. Plan approval is tied to an exact plan revision.
7. Build and test evidence is represented without overstating results.
8. Desktop, tablet and mobile behavior is specified.
9. Access control and destructive-action behavior are specified.
10. No placeholder metrics or fake project activity are presented as real.

## 12. Out of scope for this design document

- Actual UI implementation
- Database migrations
- API implementation
- Minecraft artifact generation
- AI provider integration
- Live collaboration implementation

These are later design and implementation workstreams. This document does not mark any of them as implemented.
