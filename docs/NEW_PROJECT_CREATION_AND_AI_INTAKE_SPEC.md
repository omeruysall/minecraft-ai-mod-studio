# New Project Creation & AI Intake Specification v1.0

Status: Design specification
Product: Minecraft AI Mod Studio
Scope: New project entry, conversational intake, clarification, project classification and initial plan handoff
Implementation status: Not implemented
Related specifications:
- PRODUCT_REQUIREMENTS.md
- PROJECT_ARCHITECT_DECISION_ENGINE.md
- PROJECTS_WORKSPACE_SPEC.md
- PROJECT_DETAIL_WORKSPACE_INTERACTIONS_SPEC.md
Design-first rule: This document defines intended behavior; it does not authorize coding.

## 1. Purpose

Define how a user turns an initial Minecraft idea into a structured project draft and then an approval-ready plan. The primary interaction is conversation, not a long mandatory form. The system must support simple single-artifact requests and complex multi-component projects.

Examples:
- Create a custom map/world only.
- Create a datapack only.
- Create a Java mod.
- Create a Bedrock add-on.
- Create a server plugin.
- Create a resource pack.
- Create a modpack or coordinated project containing several compatible components.

A project must never be forced to include a mod.

## 2. Entry points

Users can start a project from:
- New Project action in My Projects.
- Create action from the global navigation.
- A public template/example using “Use as starting point”.
- A supported import flow (defined separately).
- A conversation shortcut that explicitly creates a new project.

Before creation, show whether the action starts a blank project, uses a template, or duplicates an existing project. Do not silently modify an existing project when the user intends to start a new one.

## 3. Initial creation surface

The initial screen contains:
- A concise prompt: describe what you want to create.
- Text composer as the primary input.
- Optional live voice input.
- Optional attachment/import entry point where supported.
- Optional content scope selector: Let AI determine / choose content type.
- A small set of example prompts, clearly labelled as examples.
- Create/continue action.

The content scope selector is a hint, not a substitute for analysis. “Let AI determine” is the default. Users can choose a specific type or “combined project”.

Do not require users to know loaders, registries, JSON schemas or technical implementation details at the beginning.

## 4. Conversational intake

### 4.1 First-pass interpretation
The system extracts:
- User goal and intended player experience
- Requested content/artifact types
- Minecraft edition (Java/Bedrock/other supported target)
- Minecraft version, if known
- Loader/platform, if applicable
- Core gameplay/content features
- Multiplayer/server requirements
- Visual/audio/world requirements
- Constraints, exclusions and preferences
- Expected deliverables
- Uncertainties and contradictions

Each extracted item carries provenance: explicit user statement, inferred candidate, system constraint, or unresolved question.

### 4.2 Clarification policy
Ask only questions that materially affect architecture, compatibility, scope, safety, cost or deliverability. Group closely related questions when it reduces user effort, but do not display a large form by default.

Examples of clarification topics:
- Java or Bedrock, when not inferable and required
- Target Minecraft version, when compatibility depends on it
- Single artifact or coordinated multi-component project
- Intended single-player/multiplayer behavior when architecture differs
- Required custom runtime behavior that cannot be supplied by data-driven content alone

If the user does not know a technical answer, explain the practical difference and offer a recommended default as a proposal. Never silently convert a recommendation into a user decision.

### 4.3 Conflict handling
If requirements contradict one another:
- Identify the exact conflict.
- Explain the user-visible consequence.
- Offer compatible alternatives.
- Preserve the original request in conversation history.
- Do not resolve a material conflict by silently dropping a requirement.

### 4.4 Scope control
The user can add, remove or change requested features during intake. The system maintains a draft scope and identifies which prior assumptions are invalidated. No production starts during intake.

## 5. Project classification

The system classifies the request into one or more project component types:
- Java mod
- Bedrock add-on
- Server plugin
- Datapack
- Resource pack
- World/map
- Modpack/combined project
- Other supported artifact type

Classification must include:
- Selected component type(s)
- Confidence level
- Evidence from the user's request
- Alternative interpretations
- Unresolved classification questions

Low-confidence or conflicting classification requires clarification. The user can override classification. The system explains technical consequences when the override creates compatibility constraints.

## 6. Technical feasibility and ownership preview

Before creating an approval-ready plan, the system maps requested features to technically appropriate components.

Examples:
- Custom runtime behavior, registries, entities, blocks, items and networking belong in an appropriate mod/plugin/add-on layer.
- Data-driven recipes, loot, tags, advancements and functions may belong in datapacks or platform-specific equivalents.
- Terrain, structures and world layout belong to the world/map component where appropriate.
- Textures, models, sounds and localization belong to resource-pack or platform-specific asset layers.

The system must not force unsupported behavior into a datapack or other unsuitable component.

The feasibility preview shows:
- Feature
- Proposed owning component
- Required dependencies
- Compatibility concerns
- Whether custom code/runtime support is required
- Alternative implementation if applicable

These mappings remain proposals until included in an approved plan.

## 7. Project draft creation

When enough information exists to identify a coherent project:
- Create a persistent project draft with a stable project ID.
- Save the original request and conversation reference.
- Save normalized requirements and provenance.
- Save unresolved questions and assumptions.
- Save proposed component classification.
- Save target edition/version/loader only when explicitly selected or clearly marked as a proposed default.
- Set project state to Draft or Analyzing according to the workflow state machine.
- Do not create production artifacts.

The user must be able to resume the draft later without losing context.

## 8. Initial plan assembly

The AI Project Architect prepares a proposed plan containing:
1. Project objective and scope summary
2. Target Minecraft edition/version/platform
3. Components and their responsibilities
4. Feature-to-component ownership map
5. Dependency graph
6. Functional requirements
7. Non-functional requirements
8. Compatibility and feasibility findings
9. Open questions and assumptions
10. Proposed milestones
11. Build and test strategy
12. Expected deliverables
13. Risks and limitations

Each requirement must have a stable ID and acceptance criteria. The plan must identify which statements came directly from the user and which are AI proposals.

## 9. Plan review and approval handoff

The plan review screen must provide:
- Plain-language summary
- Technical details expandable on demand
- Component list and dependency graph
- Included and excluded scope
- Assumptions and open questions
- Risk and compatibility warnings
- Deliverables and test criteria
- Revision identifier

User actions:
- Approve this plan revision
- Request changes
- Edit requirements
- Remove a feature
- Add a feature
- Ask AI to explain a decision

Approval applies only to the exact revision. Any material scope or architecture change creates a new revision and requires a new approval. Approval does not itself mean generation has started.

## 10. Accessibility and input modes

Text and voice are first-class input modes and share the same project context. Voice must have clear recording state, stop/cancel controls, and explicit consent/retention behavior. Users must be able to review and correct recognized content before it becomes an accepted requirement.

The flow must remain usable with keyboard navigation, screen readers, mobile layouts and slow connections. Text entry remains available when voice is unavailable.

## 11. Error and recovery behavior

- If AI interpretation fails, preserve the user's original input and allow retry or manual continuation.
- If an attachment cannot be processed, explain the failure without discarding the rest of the request.
- If compatibility data is unavailable, mark the result unknown/unverified.
- If project persistence fails, do not claim that a draft was saved.
- If a plan cannot be assembled due to unresolved blockers, show the blockers and continue clarification.
- Never fabricate compatibility, build or playability results.

## 12. Acceptance criteria

1. User can start from a short natural-language idea.
2. User can create map-only, datapack-only, resource-pack-only, mod-only or combined projects.
3. Conversation is the default intake method; no large mandatory form is imposed.
4. Clarifying questions are limited to material unknowns.
5. Inferences are distinguished from explicit user requirements.
6. Contradictions are surfaced rather than silently resolved.
7. Feature ownership and dependency proposals are visible before approval.
8. User can correct classification and requirements.
9. Draft persists and can be resumed.
10. Approval binds to a specific plan revision.
11. No artifact production starts before explicit approval and production handoff.
12. Voice and text share context and preserve user review/control.
13. Errors do not result in false saved/approved/generated states.

## 13. Out of scope

- Implementation of AI providers/models
- Actual project database and API
- Artifact generation
- Template marketplace
- Import implementation
- Billing or quota enforcement
- Production execution and background job orchestration

These require separate specifications and approval.
