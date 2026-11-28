# Studio Interface and Community Product Specification
Version: 0.1.0
Status: Draft; pending user review
Date: 2026-11-27

## 1. Product direction

Minecraft AI Mod Studio is both:
1. A guided AI creation workspace for Minecraft content.
2. A community platform where creators can publish, discover, discuss, and collaborate on Minecraft projects.

The interface must support a creator who makes only one asset type (for example, a map) just as well as a creator who builds a complete multi-component project. Publishing must never require unrelated components.

## 2. Main desktop workspace layout

### 2.1 Global header
- Top-left: hamburger menu button.
- Center/top area: product identity and current workspace/project context.
- Top-right: account/profile control.
- Signed-out state: Sign in and Create account entry points.
- Signed-in state: avatar, username, profile, notifications, settings, account actions.
- Header remains visually compact and does not consume the main conversation area.

### 2.2 Left navigation drawer
Opened by the top-left hamburger control. It is primarily for project navigation and community/publishing destinations.

Navigation groups:
- Workspace
  - New project
  - My projects
  - Recent projects
  - Drafts
  - Shared with me / collaborations
- Publish and library
  - Publish a project
  - My published content
  - My downloads / saved items
  - Version and release management
- Discover
  - Discover projects
  - Mods
  - Maps and worlds
  - Datapacks
  - Resource packs
  - Server plugins
  - Modpacks / complete projects
  - Collections and featured content
- Community
  - Project discussions
  - Live rooms / voice discussions
  - Creator profiles
  - Following and activity feed
- Help
  - Guides and documentation
  - Support / report issue

Menu visibility and destinations may be permission- or account-state-aware. Do not expose admin controls to ordinary users.

### 2.3 Central conversation workspace
The central region is the primary creation surface.
- Persistent chat timeline with user and AI messages.
- Composer fixed to the bottom of the central region.
- Text input, send action, attachment/import action where supported.
- Live voice conversation control with clear microphone state, mute/stop controls, and visible transcript.
- Voice and text must share the same project context and conversation history.
- AI responses can include structured project summaries, feature lists, dependency explanations, previews, and approval plans.
- Long-running tasks show explicit stages and honest status.
- The user can discuss a project with AI without immediately creating or modifying files.
- When a request changes approved scope, the assistant produces a revised plan and requests approval.

### 2.4 Right-side request and project scope panel
A persistent panel on the right lets the user choose what they want to create or work on.

Content types:
- Mod
- Map / world
- Datapack
- Resource pack
- Server plugin
- Bedrock add-on
- Modpack / complete project
- Other Minecraft content
- All / combined project

Behavior:
- Single content type can be selected.
- “All / combined project” allows multiple coordinated components.
- The selected type is a scope hint, not an automatic approval to generate.
- If the user's request requires additional components, the Architect explains why and proposes them.
- The user can add or remove component types before plan approval.
- The panel may show target edition, Minecraft version, loader/platform, and project status when a project is active.
- The panel must not overwhelm the chat; on narrow screens it becomes a drawer or collapsible sheet.

## 3. Responsive and mobile behavior

Desktop:
- Left navigation drawer, central chat, right scope panel visible together when viewport permits.
- Central chat receives the largest share of horizontal space.

Tablet:
- Left drawer overlays or collapses.
- Right scope panel can collapse into a button/drawer.
- Conversation remains primary.

Mobile:
- Compact top bar with hamburger on the left and profile on the right.
- Chat occupies the main screen.
- Content type and project settings open in a bottom sheet or side sheet.
- Composer remains accessible above the keyboard.
- Voice controls are reachable with one hand and show recording state clearly.
- Avoid requiring simultaneous three-column layout on a phone.

## 4. Publishing model

Publishing supports independently publishable component types:
- Map/world only
- Mod only
- Datapack only
- Resource pack only
- Server plugin only
- Bedrock add-on only
- Modpack or complete multi-component project
- Supporting assets/documentation where permitted

A publication record must define:
- Creator and project identity
- Title, summary, description, screenshots/media
- Minecraft edition and supported versions
- Loader/platform and dependencies
- Content type(s) and included files
- Installation instructions
- License and attribution
- Release version and changelog
- Known issues and compatibility status
- Test status and evidence
- Visibility: private, unlisted, or public
- Moderation and report status

Rules:
- Publishing a map must not require a mod, datapack, or resource pack.
- Publishing a complete project may bundle linked components under one release.
- Component dependencies must be declared and validated.
- The platform must distinguish source files, generated packages, and tested playable releases.
- A build-only artifact must not be labelled “verified playable”.
- Creator retains control over draft, update, unpublish, and version release actions, subject to platform safety/moderation rules.

## 5. Community and discussion

Community capabilities:
- Public project detail pages.
- Comments and threaded project discussions.
- Questions, suggestions, issue reports, and feature requests.
- Live voice rooms associated with a project.
- Optional text chat during a live room.
- Creator-hosted project review sessions.
- Collaboration invitations and contributor roles.
- Follow creators and projects.
- Activity feed for updates, releases, and discussions.
- Search and filters by edition, version, content type, tags, popularity, recency, and compatibility.

Discussion modes:
- Asynchronous written discussion attached to a project or release.
- Scheduled or creator-started live voice discussion.
- Optional live transcript/captions where supported and consented to.
- Clear room host/moderator controls, mute, leave, report, and block.
- Voice participation and recording must follow explicit consent and privacy rules. Do not record by default.

## 6. User identity, accounts, and permissions

Account states:
- Guest / signed out: discover public content; sign-in required for publishing, commenting, collaboration, or persistent project ownership.
- Registered user: create projects, save drafts, publish subject to eligibility, comment, join permitted live rooms.
- Creator: manage published projects, releases, collaborators, and discussions.
- Moderator: handle reports and community moderation.
- Administrator: platform configuration and privileged operations.

Profile:
- Avatar and display name
- Bio and creator links
- Published projects and releases
- Community activity
- Followers/following if enabled
- Badges or achievements only when earned under transparent rules

Security:
- Server-side authorization for all privileged actions.
- Users may edit only resources they own or have explicit permission to modify.
- Public profile visibility settings and account deletion/export flows must be designed.
- Never expose secrets or private project files in public listings.

## 7. Project and publication information architecture

A project can contain zero or more components while in draft.
A component is independently versioned where appropriate.
A release is a frozen, publishable snapshot of one component or a coordinated set of components.
A publication page can represent a single component or a complete project.

Core entities:
- User
- CreatorProfile
- Project
- ProjectConversation
- ProjectRequirement
- ProjectPlanRevision
- Component
- ComponentDependency
- BuildArtifact
- TestRun
- Release
- Publication
- Comment
- DiscussionThread
- LiveRoom
- Collaboration
- Notification
- ModerationReport

## 8. Accessibility and usability

- Keyboard navigation and visible focus.
- Screen-reader labels for navigation and controls.
- Text scaling and adequate contrast.
- Captions/transcripts for voice features where available.
- Clear states for listening, speaking, muted, connecting, and disconnected.
- Confirm destructive actions such as deleting a project or unpublishing a release.
- Avoid color-only status communication.

## 9. Proposed primary user flows

### Create
Open new project -> choose content type(s) -> describe in chat or voice -> AI clarifies -> plan and component breakdown -> user approves -> generation -> testing -> editable source and artifacts.

### Publish a single component
Open a map or other component -> validate metadata and files -> choose visibility/license -> preview publication -> publish -> receive public project page.

### Publish a complete project
Select coordinated components -> validate dependencies and version compatibility -> assemble release snapshot -> review included files and test status -> publish.

### Discuss a project
Open project page -> join written discussion or live room -> review requirements/build/test evidence -> propose changes -> creator accepts proposal -> new plan revision and approval workflow.

## 10. Proposed acceptance criteria

1. The primary workspace visibly follows hamburger-left, chat-center, scope-panel-right, profile-top-right layout on wide screens.
2. The chat is the dominant workspace and supports text-first interaction.
3. Voice conversation is available as a first-class mode and shares project context with text.
4. The user can select one content type or a combined project.
5. A map-only project can be created and published without unrelated components.
6. A complete multi-component project can be published as a coordinated release.
7. Public discovery separates content types and supports compatibility filters.
8. Project pages support written discussion and project-linked live voice sessions.
9. Guest and signed-in account states are clearly distinguished.
10. Mobile layout uses drawers/sheets rather than forcing three columns.
11. Publishing exposes accurate build/test/playability status.
12. All account, ownership, publishing, moderation, and collaboration permissions are enforced server-side.

## 11. Open design decisions

The following remain to be specified before implementation:
- Whether live voice uses browser/native voice infrastructure or an external provider.
- Whether live rooms are public, invite-only, or both.
- Whether publishing is open to all registered users or subject to initial creator eligibility.
- Moderation policy and reporting workflow.
- Storage limits and upload size policy.
- Whether comments and live rooms are available to guests as read-only.
- Monetization, if any; no payment model is assumed.
- Exact visual design system, typography, colors, and component library.

## 12. Current status

This document records the requested product direction and proposed UX behavior. It is not a working UI implementation. Authentication, live voice, publishing, community discussions, and responsive UI are not yet implemented.


## 13. Approved main workspace visual direction — v1.2

Status: Main workspace design decisions approved by the product owner on 2026-11-27. This approval covers the design direction and interaction model only; it does not authorize implementation or production code.

### 13.1 Visual identity
- Hybrid visual identity: modern professional software workspace with restrained Minecraft-inspired visual details.
- Dark-first interface direction with legible contrast and restrained green accents.
- Minecraft textures and voxel imagery are used as contextual accents and content previews, not as a distracting full-screen background.
- The interface must remain suitable for both Minecraft players and technically advanced creators.

### 13.2 Workspace layout
- Desktop: left navigation, central creation workspace, right project controller, compact global header.
- The central conversation remains the primary interaction surface.
- The right project controller is a contextual panel with Project, Plan, and Files views.
- The left navigation can collapse or open as a drawer.
- Mobile: conversation-first layout; navigation and project controller open as drawers or sheets. No forced three-column layout.

### 13.3 Conversation and voice
- Text and live voice are first-class interaction modes.
- Both modes share one project context, conversation history, and requirement state.
- Voice UI must expose connection, listening, speaking, muted, and disconnected states.
- Transcript visibility is supported; recording is not enabled by default and requires explicit consent.

### 13.4 Live content preview
- A preview workspace is part of the main design, not an optional future add-on.
- Preview content adapts to the artifact type: world/map, 3D model or item, datapack structures, resource-pack assets, and other supported formats.
- Planned controls include zoom, camera/orbit where applicable, previous/next revision comparison, file inspection, and change review.
- Preview must distinguish illustrative placeholders from actual generated artifacts.
- Unsupported formats must show a clear file/detail view rather than pretending to provide an interactive preview.

### 13.5 Hybrid project controller
- The AI may recommend components, settings, dependencies, and plan changes.
- Recommendations are visibly marked as suggestions and are not silently applied.
- The user can accept, reject, or edit each recommendation.
- Changes affecting the approved project scope create a new plan revision and require approval before production.
- The user remains the final decision-maker.

### 13.6 Main workspace acceptance criteria
1. Desktop layout presents navigation, conversation, preview, and project controller without obscuring the chat.
2. The preview area is present in the workspace and accurately identifies placeholder versus generated content.
3. The controller supports Project, Plan, and Files views.
4. AI recommendations never silently alter project scope or approved requirements.
5. Text and voice share project context.
6. Mobile uses responsive drawers/sheets and preserves access to chat, preview, and project controls.

### 13.7 Implementation boundary
The decisions in this section are design specifications only. They do not indicate that the preview renderer, voice system, responsive UI, project controller, or any other frontend feature has been implemented.


## 2.5 Product boundary and real creation workflow

This interface is the standalone Minecraft AI Mod Studio web application. The central conversation is an in-product project workspace, not an external ChatGPT conversation.

The intended user journey is:
1. Open the Studio website and sign in (or use the explicitly supported guest mode, if later approved).
2. Create a project or open an existing project.
3. Describe the mod, map, datapack, resource pack or complete project in the Studio chat.
4. Review the AI-generated requirements summary, component creation table, target versions and dependency plan.
5. Approve a specific plan revision.
6. Monitor real generation, integration, build and test jobs with truthful status.
7. Inspect previews, source files, logs and test evidence.
8. Download the actual generated deliverables from the project workspace.

The web application must not display simulated success as completed work. A chat response saying that an artifact was created is not a substitute for a persisted artifact record, a real file/package and corresponding validation evidence. If a capability is unavailable, show it as unavailable or not run.

The present ChatGPT conversation is used only to design and plan this product; it is not the production authoring interface and does not itself generate the mod.
