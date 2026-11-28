# AI Model and Provider Management Specification

**Document ID:** AI-MODEL-PROVIDER-001  
**Version:** 1.0  
**Status:** Design draft — pending review and approval  
**Product:** Minecraft AI Mod Studio  
**Implementation status:** Not implemented  
**Last updated:** 2026-11-28

## 1. Purpose

Define a provider-independent AI integration layer for conversation, requirements analysis, planning assistance, code generation, asset assistance, troubleshooting, and other AI-supported workflows.

The product must not be architecturally locked to one AI vendor, one model family, or one hosting arrangement. Provider and model availability, costs, context limits, capabilities, and terms change over time; these must be represented as configurable metadata rather than hard-coded assumptions.

This document is a design specification. It does not claim that any provider is connected or that a local model currently runs in the application.

## 2. Design goals

1. Support multiple hosted AI providers through a common internal contract.
2. Permit local model runtimes where the user's device and the model support the required workload.
3. Support a mixed strategy: hosted models for demanding tasks and local models for suitable private, offline, or lower-cost tasks.
4. Keep provider credentials out of source code, project files, logs, and client-visible responses.
5. Make model capabilities explicit; do not assume every model can perform every task.
6. Provide transparent provider/model selection and explain why a route was chosen.
7. Control spending with budgets, usage estimates where available, hard limits, and user confirmation for chargeable operations.
8. Degrade gracefully when a provider is unavailable, rate-limited, or unsuitable.
9. Keep the application usable for non-AI project operations when no AI provider is configured.
10. Allow provider integrations to be added or removed without changing Project Architect's core domain logic.

## 3. Architectural position

Introduce an **AI Gateway** between product services and external/local model runtimes.

Product services call task-oriented internal interfaces. The AI Gateway resolves an eligible model, enforces policy, invokes a provider adapter, normalizes the response, records permitted usage metadata, and returns a typed result.

Logical layers:
- Product features: conversation, requirement analysis, planning, code assistance, diagnostics, asset assistance.
- AI task contracts: typed request/response definitions and structured-output schemas.
- Model Router: selects an eligible model based on task, policy, capability, privacy, latency, cost, and availability.
- Provider Registry: stores provider/model metadata and connection state.
- Provider Adapters: translate the internal contract to each provider's API or local runtime.
- Credential Vault: stores encrypted credentials and scoped connection metadata.
- Usage and Budget Manager: tracks usage, estimates, limits, and approval requirements.
- Observability and Safety: redaction, error classification, timeouts, audit events, and policy enforcement.

Project Architect remains the authority for project state, requirements, dependencies, plan revisions, and production approval. The AI Gateway supplies model inference; it must not independently approve plans or start production.

## 4. Provider categories

### 4.1 Hosted API providers

The architecture should support hosted providers through adapters. Specific providers and model identifiers must be maintained in a versioned capability registry and verified before being offered as available.

Provider records should include:
- Provider ID and display name.
- API base configuration and adapter version.
- Authentication method.
- Supported regions, if relevant.
- Connection status and last verification time.
- Data handling and retention information sourced from the provider's current terms.
- Supported model IDs and capability metadata.
- Rate-limit and error information where available.

### 4.2 Local model runtimes

The architecture may support local runtimes through a local connector/agent. Candidate runtime integrations should be evaluated independently; do not promise compatibility until tested on target devices.

Local runtime metadata:
- Runtime type and version.
- Device/host identity label, not a hardware fingerprint.
- Model identifier and quantization, when known.
- Available context window and supported modalities.
- Memory/compute requirements where known.
- Runtime endpoint and connection health.
- Whether inference remains on-device.
- Offline readiness and last successful test.

A local model is not automatically private or safe merely because it is local. Local logs, model files, extensions, and network exposure still require controls.

### 4.3 Hybrid execution

Hybrid execution means a task can be routed to hosted or local inference according to explicit policy. It does not mean silently sending private project content to a cloud provider.

If a task requires cloud processing and the project/user policy disallows it, the system must stop and explain the limitation or offer a local alternative when one is suitable.

## 5. Capability registry

Do not select models by marketing name alone. Maintain capability records for each model/version, including:

- Text input and output.
- Structured JSON/schema output.
- Tool/function calling.
- Long-context support and tested context limits.
- Image understanding.
- Audio input/transcription.
- Audio output/speech.
- Code generation and code reasoning.
- Multilingual performance metadata where verified.
- Streaming support.
- Context and output token limits.
- Availability state and last verification.
- Known limitations and supported task classes.

Capability status values:
- Verified.
- Provider-declared, not yet tested.
- Experimental.
- Unavailable.
- Deprecated.

A model may be eligible for one task and ineligible for another. The registry must retain source and verification date for claims that can change.

## 6. Task taxonomy and routing

Initial task classes:
- General conversation.
- Intent classification and request normalization.
- Requirement extraction.
- Clarification question generation.
- Technical feasibility reasoning.
- Minecraft version/loader research assistance.
- Project plan drafting.
- Code generation and code review.
- Build/test log diagnosis.
- Documentation generation.
- Image understanding and visual asset assistance.
- Speech transcription and speech synthesis.

Routing sequence:
1. Identify the task class and required capabilities.
2. Apply user/project privacy and provider restrictions.
3. Exclude unavailable, unverified, or incapable models as policy requires.
4. Apply budget and rate-limit constraints.
5. Rank eligible models using configured quality, latency, cost, and reliability preferences.
6. Select the preferred eligible model or ask the user when selection materially affects cost, privacy, or quality.
7. Invoke through the adapter with timeout and retry policy.
8. Validate response shape and safety constraints.
9. Record allowed usage metadata and route explanation.
10. Return result with provider/model disclosure appropriate to the selected transparency setting.

Routing must be deterministic for the same policy and registry snapshot unless an explicitly configured adaptive strategy is enabled. The system must record which model was used for reproducibility.

## 7. Selection modes

Proposed user-facing modes:

- **Automatic:** system chooses from eligible models according to the user's configured policy.
- **Quality priority:** prefer the strongest eligible model within the configured budget and privacy rules.
- **Cost priority:** prefer the lowest-cost eligible route; local inference may be selected when suitable.
- **Local first:** prefer local inference; ask or fall back only according to the user's explicit fallback setting.
- **Manual:** user selects a connected provider/model for supported tasks.

These are policy presets, not guarantees that a particular model is available or free.

The UI must show when a selected mode cannot be honored, and why. It must not silently override a privacy restriction.

## 8. Cost, quota, and consent controls

Cost controls:
- Per-request estimated cost when reliable pricing data exists.
- Actual usage and charge metadata returned by the provider, when available.
- Daily/monthly budget settings.
- Per-project budget settings, if enabled.
- Request limits and rate-limit handling.
- Warnings before operations likely to incur charges.
- Hard-stop behavior when a configured hard budget is reached.
- No claim that a provider/model is free unless verified under the user's actual account and current terms.

Consent rules:
- Connecting a provider requires explicit user action.
- Entering or replacing a credential requires explicit user action.
- Chargeable use must follow the user's configured consent policy.
- Fallback to a different provider must respect privacy and budget settings.
- No credential or raw secret may be shown again after secure storage.

## 9. Credentials and security

- Store credentials only in an encrypted secret store appropriate to the deployment.
- Never commit API keys, tokens, or secrets to GitHub.
- Never include secrets in project manifests, exported ZIP files, telemetry, crash reports, or model prompts.
- Support credential rotation and revocation.
- Scope credentials to the minimum required permissions.
- Redact authorization headers and secret-like values from logs.
- Keep local runtime endpoints private by default; require explicit configuration before exposing them beyond localhost or a trusted device boundary.
- Separate provider connection status from model availability.
- Apply request timeouts, response-size limits, and error normalization.
- Validate structured outputs before passing them to Project Architect or other services.

## 10. Data handling and privacy

Before a request is sent, classify its data context:
- Public/general prompt.
- Project metadata.
- Private project content or source files.
- User-provided attachment.
- Credentials or other prohibited secret material.

The system must block secrets from being sent as ordinary prompt content where detectable. Provider routing must honor project/user data policies.

The UI should disclose:
- Which provider receives the request.
- Whether processing is local or hosted.
- Which project content or attachments are included.
- Whether the request may incur cost.
- Whether the selected route conflicts with privacy settings.

Provider retention/training claims must be sourced from current provider documentation and presented with a verification date. Do not make blanket claims about all providers.

## 11. Reliability and fallback

Normalize common failures:
- Authentication failure.
- Invalid model or unsupported capability.
- Rate limit or quota exhausted.
- Billing/budget restriction.
- Provider outage.
- Network timeout.
- Invalid or incomplete structured output.
- Context length exceeded.
- Local runtime unavailable.
- Model load failure or insufficient device resources.

Fallback rules:
- Retry transient failures only within bounded limits.
- Do not retry authentication or billing failures as if they were transient.
- Use another provider only if the configured privacy, budget, capability, and consent policies permit it.
- If fallback changes cost or data destination materially, request confirmation unless the user explicitly pre-authorized that exact fallback policy.
- Preserve the original task and disclose partial completion.
- Do not fabricate a successful model response when inference failed.

## 12. Streaming and long-running tasks

The gateway should support streaming where the provider and task contract permit it. Streaming output must be clearly marked as provisional until validated.

Long-running operations should use job IDs and observable states, such as:
- QUEUED
- ROUTING
- RUNNING
- VALIDATING
- COMPLETED
- FAILED
- CANCELLED

Cancellation must be best-effort and its actual result disclosed. A cancelled inference must not be represented as a completed generation.

## 13. Observability and audit

Record only the minimum necessary operational metadata:
- Request/task ID.
- Project ID and revision where applicable.
- Provider and model identifiers.
- Adapter and registry versions.
- Start/end time and outcome.
- Token/usage/cost metadata when returned.
- Retry/fallback reason.
- Validation result.
- User consent or policy decision reference.

Do not store full prompts, attachments, or model responses in operational logs by default. Project conversation history is governed by the separate project-memory and privacy specifications.

## 14. Non-AI fallback behavior

If no AI provider is configured:
- Users can browse and manage existing projects and files.
- Static documentation, templates, schemas, and local validation can remain available.
- The UI must explain which AI-dependent functions are unavailable.
- The application must not simulate AI analysis with deterministic keyword matching while presenting it as real AI.
- Any rule-based helper must be explicitly labeled as rule-based.

## 15. Acceptance criteria

- Product services depend on internal task contracts, not vendor-specific SDKs.
- At least two independent provider adapters can be added without changing Project Architect's domain model.
- Local runtime integration is isolated behind the same task contracts where capabilities permit.
- The router checks capability, privacy, budget, and availability before invocation.
- Credentials never appear in source, project exports, or logs.
- Provider/model usage is traceable for each completed task.
- Fallback obeys user consent, privacy, and budget restrictions.
- Missing provider configuration produces honest degraded behavior.
- Model capability claims carry verification status and date.
- Project Architect retains exclusive control over plan approval and production handoff.

## 16. Open design decisions

The following are proposals requiring product review:
1. Initial provider list and priority order.
2. Whether the first release ships with one hosted adapter, multiple hosted adapters, or a hosted-plus-local pair.
3. Whether users bring their own API keys only, or whether a managed service is ever considered.
4. Default routing mode.
5. Default cloud-data policy for private projects.
6. Whether chargeable requests always require per-request confirmation or may use a user-defined budget authorization.
7. Target local runtime(s) and minimum supported device classes.
8. Whether offline mode provides full AI planning or a reduced feature set.
9. Whether provider/model identity is always shown or available in request details.
10. Which usage and cost history is retained and exportable.

Do not resolve these decisions by assumption during implementation. Record approved choices in an Architecture Decision Record and update this specification.

## 17. Implementation boundary

This document defines intended behavior only. No provider adapter, model router, credential vault, usage meter, local runtime connector, or AI inference integration is asserted to exist in the current application. Implementation begins only after the complete design baseline is reviewed and explicitly approved.
