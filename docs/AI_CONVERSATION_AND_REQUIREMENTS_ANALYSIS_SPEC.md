# AI Conversation and Requirements Analysis Specification

**Document ID:** AIS-CONV-REQ-001  
**Version:** 1.0  
**Status:** Design draft — pending review and approval  
**Product:** Minecraft AI Mod Studio  
**Implementation status:** Not implemented  
**Last updated:** 2026-11-28

## 1. Purpose

Define the conversation system that turns a creator's natural-language idea into a structured, reviewable Minecraft project request. The system must support incremental discovery, technical clarification, transparent assumptions, and an explicit approval boundary before production.

This document specifies product behavior and contracts. It does not claim that an LLM provider, voice pipeline, generator, or production backend is currently implemented.

## 2. Core principles

1. The user may begin with an incomplete, informal, multilingual, or evolving idea.
2. The assistant should ask only questions that materially affect scope, compatibility, feasibility, or output quality.
3. The assistant must distinguish user-stated requirements, inferred requirements, recommendations, and unresolved assumptions.
4. The user can create a single artifact (for example, only a map or only a datapack) or a multi-component project.
5. No artifact generation, external publication, or irreversible project mutation begins before explicit approval of the applicable plan revision.
6. The user can inspect and edit the structured interpretation before approval.
7. The conversation, plan, files, and component graph share one project identity and revision history.
8. A later change should invalidate only affected decisions and dependent components where technically safe; unrelated approved components should remain intact.
9. The system must communicate uncertainty and unsupported requests honestly. It must not present guesses as verified Minecraft capabilities.
10. Text and live voice are two interaction modes over the same conversation state, not separate project histories.

## 3. Conversation experience

### 3.1 Entry points

- New project conversation.
- Continue an existing project.
- Open a specific component and request a change.
- Import or describe an existing project for analysis.
- Ask a general Minecraft creation question without creating a project.

The system must not silently turn every general question into a project.

### 3.2 Input modes

- Text input with multiline composition.
- Live voice conversation with visible listening, processing, and speaking states.
- Voice transcription displayed in the conversation when available.
- User correction of transcription before it becomes a confirmed requirement.
- Attachments such as images, archives, logs, configuration files, and world-related files, subject to supported formats and safety checks.

Text and voice inputs must be timestamped and associated with the same conversation thread. The user must be able to interrupt voice output and switch to text without losing context.

### 3.3 Assistant message types

The UI should visually distinguish:
- Clarifying question.
- Interpretation summary.
- Confirmed requirement.
- Inferred requirement.
- Assumption requiring confirmation.
- Technical warning or incompatibility.
- Proposed alternative.
- Plan revision.
- Approval request.
- Production/build/test status.
- Error and recovery instruction.

Do not use a normal conversational paragraph as the only representation of a critical approval request.

## 4. Request interpretation pipeline

The logical pipeline is:

1. **Capture:** receive text, voice transcript, or supported attachment.
2. **Normalize:** preserve original wording while extracting normalized intent and language.
3. **Classify intent:** general question, new project, continue project, modify project, troubleshoot, or publish.
4. **Extract entities:** Minecraft edition, version, loader/platform, artifact types, gameplay mechanics, content identifiers, target environment, and constraints when present.
5. **Map capabilities:** match requested features to the feature inventory and capability registry.
6. **Detect ambiguity:** identify missing or conflicting details that materially affect the plan.
7. **Resolve ownership:** assign each requested behavior to the correct component type.
8. **Resolve compatibility:** identify version, loader, edition, dependency, and runtime constraints.
9. **Build structured requirements:** create a traceable requirement set with IDs and confidence.
10. **Summarize:** present what the system understood and what remains uncertain.
11. **Plan handoff:** pass only sufficiently resolved requirements to Project Architect.
12. **Approval gate:** request approval for the exact plan revision before production.

The Project Architect remains the orchestration authority. The conversation layer must not bypass its approval and dependency checks.

## 5. Requirement data model

Each requirement should have a stable ID and at least these fields:

| Field | Meaning |
|---|---|
| requirement_id | Stable identifier, e.g. REQ-0001 |
| statement | Atomic, testable requirement |
| source | User statement, attachment, inference, or system constraint |
| source_message_id | Conversation message that supports it, when applicable |
| category | Functional, visual, technical, compatibility, performance, safety, delivery |
| component_scope | Component or components affected |
| priority | Must, should, could, deferred |
| certainty | Confirmed, inferred, assumption, unresolved |
| confidence | Internal confidence indicator; never a substitute for user confirmation |
| acceptance_criteria | Observable condition for completion |
| dependencies | Requirement IDs that must be satisfied first |
| status | Proposed, confirmed, changed, rejected, blocked, implemented, verified |

Requirements must be atomic where practical. Broad requests should be decomposed into smaller requirements without changing their meaning.

## 6. Clarification policy

Ask a question only when the answer can materially change:
- Minecraft edition or platform.
- Target version or loader compatibility.
- Artifact type or component ownership.
- Core gameplay behavior.
- Multiplayer/server behavior.
- World-generation or save compatibility.
- Required external dependencies.
- Delivery format or intended runtime.
- Performance, accessibility, or safety constraints.

Question strategy:
- Ask one high-value question at a time by default.
- Group questions only when they are tightly related and answering them together reduces effort.
- Offer a sensible recommendation when the user is unsure, but label it as a recommendation.
- Do not repeatedly ask for information already confirmed in the project.
- Allow the user to defer optional decisions.
- If a decision can safely be postponed, mark it unresolved and explain what it blocks.
- Never invent a user preference to fill a missing value.

### 6.1 Progressive clarification

The assistant should first establish the project's essential shape, then refine details:
- What should be created?
- Which Minecraft edition and target version?
- What should the player experience or observe?
- Is the content single-player, multiplayer, or server-side?
- Which supporting artifacts are needed?
- What delivery and testing expectations apply?

The exact question order is adaptive; this is not a mandatory fixed questionnaire.

## 7. Technical ownership and feasibility

The analysis must use the component ownership rules in the architecture and feature inventory:
- Java mods own custom runtime behavior, custom registries, entities, blocks, items, networking, and other mod-loader capabilities.
- Datapacks own supported data-driven functions, recipes, loot tables, tags, predicates, and advancements.
- Worlds/maps own terrain, structures, spawn points, and placed world content.
- Resource packs own textures, models, sounds, language assets, and supported presentation overrides.
- Bedrock add-ons and server plugins must be mapped to their own supported APIs and packaging constraints.

If a requested behavior cannot be implemented by the selected artifact type, explain why and propose a compatible component or alternative. Do not force unsupported mechanics into datapacks or resource packs.

Every feasibility result should be one of:
- Supported.
- Supported with constraints.
- Requires another component.
- Requires external dependency.
- Unverified; research or prototype needed.
- Unsupported for the selected edition/version/platform.

## 8. Assumptions, conflicts, and changes

Assumptions must be explicit and individually confirmable. A user may accept, edit, or reject an assumption.

When requirements conflict:
1. Identify the conflicting requirement IDs.
2. Explain the practical consequence.
3. Offer a resolution or ask the user.
4. Do not silently discard either requirement.

When a user changes scope:
- Create a new requirement revision.
- Identify affected components and downstream dependencies.
- Preserve unaffected approved artifacts.
- Mark affected plan sections as requiring review.
- Request approval again when the change materially affects the approved plan.

## 9. Conversation memory and traceability

Project memory is scoped to the project and must retain:
- Confirmed requirements and decisions.
- Explicitly rejected options where useful to prevent repeated proposals.
- Current unresolved questions.
- Approved plan revisions.
- Component ownership and dependency decisions.
- User-provided constraints and references.
- Production, build, test, and repair history.

Every generated plan item should trace back to one or more requirement IDs. Every requirement should show whether it is represented in the plan, deferred, blocked, or rejected.

The system should distinguish project memory from general user preferences and must provide a way to inspect and correct project decisions.

## 10. Approval handoff

Before approval, present:
- Plain-language project summary.
- Target edition/version/platform and loader where applicable.
- Component list and each component's responsibility.
- Feature list mapped to requirements.
- Dependencies and compatibility warnings.
- Known limitations and unresolved decisions.
- Deliverables and expected file formats.
- Build/test plan and any tests that cannot be run.
- Estimated complexity or effort only when a defensible basis exists.

The approval action must bind to an immutable plan revision identifier or content hash. Any material change after approval creates a new revision and requires renewed approval before affected production work begins.

## 11. Failure and recovery states

Handle explicitly:
- Speech recognition failure.
- Ambiguous or incomplete user input.
- Unsupported attachment.
- Contradictory requirements.
- Missing capability metadata.
- Version or loader incompatibility.
- Model/provider unavailable.
- Interrupted conversation.
- Lost connection during voice interaction.
- Failed plan generation.

Preserve user input and project state where possible. Provide a retry or correction path. Never fabricate an analysis result when a provider or subsystem failed.

## 12. Privacy and control

- Make microphone activation visible and user-controlled.
- Do not imply voice is being recorded when it is not.
- Explain attachment processing and retention according to the deployed product's actual policy.
- Do not publish project files or conversation content without explicit user action.
- Team members see only projects and actions permitted by their project role.
- Do not expose secrets, API keys, or private credentials in generated logs or shared artifacts.

## 13. Acceptance criteria

The design is acceptable for implementation when:
- A user can start from an incomplete natural-language idea.
- The system distinguishes a general question from a project-creation request.
- Text and voice share one coherent project context.
- Confirmed requirements are separated from assumptions and inferences.
- Clarification is targeted and does not repeat known answers.
- Unsupported mechanics are assigned to the correct component or rejected with an explanation.
- Every plan item traces to requirement IDs.
- Scope changes create traceable revisions.
- Approval is explicit and tied to an exact plan revision.
- No production begins before approval.
- Failure states preserve input and disclose what did not happen.
- The UI communicates what is proposed, confirmed, approved, implemented, built, and tested as separate states.

## 14. Open design decisions

The following remain intentionally unresolved until product review:
- Which AI providers and local models are supported in the first release.
- Whether provider selection is user-facing or automatic.
- Which attachment formats are supported in the first release.
- Voice transcription and speech synthesis provider strategy.
- Whether offline conversation supports full requirement analysis or a reduced local capability.
- Project-memory retention and export controls.
- Whether confidence is shown numerically or only through qualitative labels.

These decisions must be resolved in the provider, voice, attachment, offline, and project-memory specifications. They must not be guessed in implementation.

## 15. Implementation boundary

This is a design specification only. It does not assert that the conversation pipeline, LLM integration, voice stack, requirement database, or approval workflow exists in the current application. Implementation begins only after the full design baseline has been reviewed and explicitly approved.
