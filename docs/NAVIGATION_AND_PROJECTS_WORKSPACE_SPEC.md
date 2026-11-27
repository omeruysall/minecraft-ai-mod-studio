# Navigation and My Projects Workspace Specification

Version: 1.0.0
Status: Design draft; pending user review
Date: 2026-11-27

## 1. Purpose

Define the left navigation and the My Projects workspace for Minecraft AI Mod Studio. This is product and UX design documentation only. No frontend or backend implementation is authorized by this document.

The navigation must make it easy to move between creation, owned work, collaboration, publishing, discovery, and community without mixing those concepts.

## 2. Global navigation model

The global header contains:
- Hamburger button at the top-left.
- Product identity and current workspace breadcrumb.
- Search entry point.
- Notifications.
- Profile/account menu at the top-right.

The navigation drawer is collapsible on desktop and overlays the workspace when opened on narrow screens. On mobile, it must not permanently consume the chat/working area.

### 2.1 Navigation groups

**Workspace**
- Overview
- New project
- My projects
- Recent projects
- Drafts
- Shared with me

**Publishing and library**
- Publish content
- My publications
- Saved items / downloads
- Releases and version history

**Discover**
- Featured
- All content
- Mods
- Maps and worlds
- Datapacks
- Resource packs
- Server plugins
- Bedrock add-ons
- Modpacks / complete projects
- Collections

**Community**
- Project discussions
- Live rooms
- Creator directory
- Following / activity feed

**Account and help**
- Profile
- Settings
- Help and documentation
- Report a problem

Admin and moderation destinations are not shown to ordinary users. They are exposed only to authorized roles and are specified separately.

## 3. My Projects workspace

My Projects is the user's private project library and management surface. It must distinguish project lifecycle state from publication state and build/test state.

### 3.1 Primary views

- All projects
- In progress
- Awaiting my approval
- Drafts
- Completed
- Archived
- Shared with me

These are views/filters over project records, not separate copies of projects.

### 3.2 Project card information

Each project card should show:
- Project title and optional cover/preview.
- Short description.
- Content scope: mod, map/world, datapack, resource pack, plugin, Bedrock add-on, or combined project.
- Minecraft edition and target version, if selected.
- Loader/platform, when applicable.
- Last updated timestamp.
- Project owner and collaboration indicator.
- Project lifecycle status.
- Latest plan revision and whether approval is pending.
- Latest build/test status, if a build or test exists.
- Publication status, if published.

Do not use one generic status badge to imply all lifecycle, approval, build, test, and publication states. Show these as distinct facts.

### 3.3 Project lifecycle states

Suggested lifecycle values:
- Draft
- Analyzing
- Clarification needed
- Plan ready
- Awaiting approval
- Approved
- In production
- Integrating
- Testing
- Repair needed
- Completed
- Blocked
- Archived

A project can be completed but unpublished. A published project can have a newer draft revision. These states must not be conflated.

### 3.4 Search, sorting, and filters

Search:
- Project title
- Description
- Tags
- Component names
- Minecraft version

Filters:
- Content type
- Edition (Java / Bedrock)
- Minecraft version
- Loader/platform
- Lifecycle state
- Approval state
- Build/test state
- Publication visibility
- Owner/collaborator

Sort options:
- Recently updated
- Recently created
- Name
- Lifecycle activity

Filters must combine predictably and be clearable. Empty states should explain why no projects match and provide a relevant action, such as New project or Clear filters.

## 4. Project detail workspace

Opening a project card enters a project-specific workspace with:
- Overview
- Conversation
- Requirements
- Plan and revisions
- Components and dependency graph
- Preview
- Files and artifacts
- Build and test history
- Collaborators and activity
- Publication/releases, when applicable

Only relevant tabs should be enabled. For example, a draft with no generated files should not present an empty artifact view as if files existed.

### 4.1 Project actions

Available actions depend on role, ownership, and project state:
- Open / continue
- Rename
- Duplicate
- Invite collaborator
- Export project specification
- Archive
- Delete, with explicit confirmation

Destructive actions require confirmation. Deleting a project must explain the effect on generated artifacts, publications, and collaborators. Public releases must not silently disappear because a private working draft is deleted.

## 5. Collaboration model

- Owner is the default project authority.
- Collaborators receive explicit roles and scoped permissions.
- Shared projects appear under Shared with me and remain distinguishable from owned projects.
- Suggestions from collaborators do not silently modify approved requirements.
- Scope-changing proposals enter the same plan-revision and approval process.
- The project activity feed records meaningful changes and who initiated them.

Initial role proposal:
- Owner: full project control.
- Editor: edit requirements and draft components within granted scope; cannot transfer ownership or delete the project.
- Reviewer: comment and review plans/artifacts; cannot directly modify project files.
- Viewer: read-only access.

Exact permission matrix is to be finalized in the account, security, and collaboration design phase.

## 6. Responsive behavior

Desktop:
- Drawer can remain expanded or collapse to icons.
- My Projects uses a responsive card/list layout.
- Filters can appear in a side panel or toolbar.

Tablet:
- Drawer overlays or collapses.
- Filters open in a sheet.
- Project cards adapt to available width.

Mobile:
- Navigation opens as a full-height drawer.
- My Projects uses a single-column card list.
- Filters open in a bottom sheet.
- Project details use a compact tab strip or section menu.
- Important status and primary action remain visible without horizontal scrolling.

## 7. Empty, loading, and error states

- Empty library: explain that no projects exist yet and offer New project.
- No search results: show active filters and Clear filters.
- Loading: use stable skeleton cards and preserve the user's current filter state.
- Access denied: explain that the project is shared but the user lacks the required permission.
- Offline or service failure: preserve unsent form/chat content where safe and provide retry.
- Archived: visually distinguish from active work and provide restore where authorized.

## 8. Acceptance criteria

1. Users can reach My Projects from global navigation.
2. Owned projects and shared projects are clearly distinguished.
3. Lifecycle, approval, build/test, and publication statuses are not conflated.
4. Search, filters, and sorting can be combined and cleared.
5. A project card exposes enough compatibility and status information to decide whether to open it.
6. Project detail separates conversation, requirements, plan, components, preview, files, tests, and publication.
7. Permissions are role-aware and enforced server-side in the eventual implementation.
8. Mobile navigation and project lists work without horizontal scrolling.
9. Empty, loading, access-denied, and error states are designed.
10. Destructive actions require explicit confirmation.

## 9. Open decisions

- Final project-card density: compact list, visual cards, or user-selectable.
- Whether users can create custom folders or collections.
- Whether archived projects count toward storage quotas.
- Exact collaborator role permissions.
- Whether project templates are surfaced in My Projects or New project.
- Bulk actions such as archive/export.
- Whether project ownership transfer is supported.

## 10. Implementation boundary

This specification describes intended UX and product behavior only. It does not mean navigation, project storage, search, filters, collaboration, or project detail screens are implemented.
