# Design-First Delivery Workflow

Version: 1.0.0
Status: Active project process
Date: 2026-11-27

## 1. Governing decision

Minecraft AI Mod Studio will complete product and UX design before application coding begins.

During the design phase, GitHub is the source of truth for approved and draft specifications, architecture decisions, inventories, schemas, and project decisions. The repository may receive documentation and design assets, but application source code must not be added or changed as part of this phase unless the product owner explicitly changes this rule.

## 2. Work phases

### Phase A — Product and UX design
- Product scope and personas
- Main workspace and responsive behavior
- Navigation and My Projects
- Project detail and collaboration
- Creation conversation and voice UX
- Planning, requirements, and approval UX
- Content preview and artifact inspection
- Publishing, discovery, and community
- Account, roles, privacy, moderation, and security UX

### Phase B — Technical design
- System architecture and service boundaries
- Project manifest and data model
- API contracts
- Component ownership and dependency graph
- Version/loader compatibility resolution
- AI provider abstraction and conversation memory
- Build workers, testing, packaging, and artifact storage
- Security, privacy, observability, and operations
- Cost and deployment plan

### Phase C — Design review and freeze
- Cross-document consistency review
- Requirement-to-design traceability
- Open decisions resolved or explicitly deferred
- Acceptance criteria defined
- Product owner reviews the complete design baseline
- A versioned design baseline is recorded in GitHub

### Phase D — Implementation
Coding starts only after the design baseline is approved.
- Implement in small milestones.
- Preserve existing architecture and stable IDs.
- Each milestone includes tests and evidence.
- Update documentation when implementation behavior changes.
- No feature is marked implemented or tested without evidence.

### Phase E — Integration and release validation
- Component integration
- Compatibility validation
- Build and artifact checks
- World/game testing where applicable
- Security and permission tests
- Packaging and release verification
- Report tests not run; never claim playability without in-game evidence.

## 3. GitHub operating rules

- Repository: omeruysall/minecraft-ai-mod-studio.
- Default branch: main.
- Use docs/ for product and technical specifications.
- Use catalogs/ for machine-readable inventories.
- Use schemas/ for versioned data contracts.
- Keep design drafts clearly labelled Draft / Pending review.
- Record approved decisions with date and version.
- Use focused commits with descriptive messages.
- Do not overwrite existing documents without fetching and reviewing the current version first.
- Do not add application code during Phases A–C.
- Do not claim a document is approved merely because it was committed.
- Keep user approval separate from GitHub commit success.

## 4. Approval and change control

- The product owner can approve individual design decisions or a complete design baseline.
- An unapproved proposal remains a draft.
- A material scope change updates the affected specification and its revision.
- Changes to approved scope require renewed approval before implementation.
- Existing decisions remain in force unless explicitly superseded.

## 5. Current position

- Product direction, project architecture, feature inventory, decision-engine design, and initial interface/community specification exist.
- Main workspace visual direction v1.2 has been approved as a design direction.
- Navigation and My Projects specification is a draft pending review.
- No implementation work is authorized by this process until the complete design baseline is reviewed and approved.
