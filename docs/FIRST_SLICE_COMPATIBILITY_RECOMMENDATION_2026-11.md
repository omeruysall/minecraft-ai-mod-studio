# First Slice Compatibility Recommendation — November 2026

**Status:** Technical recommendation — pending user confirmation  
**Research date:** 2026-11-28  
**Scope:** First playable Java + Bedrock mod/world milestone

## 1. Recommendation summary

| Track | Recommended baseline | Status |
|---|---|---|
| Java Edition | Minecraft 26.3 + Fabric | Recommended, not user-approved |
| Bedrock Edition | Minecraft 26.60 + stable Script API 2.11.0 | Recommended, not user-approved |

This is a first-slice baseline recommendation, not a long-term support policy. The project should keep target versions configurable and record compatibility evidence for each release.

## 2. Java Edition recommendation

Recommend Minecraft Java Edition 26.3 with Fabric as the first Java target.

Evidence:
- Mojang's official Java 26.3 release notes were published 15 September 2026.
- The release changes data pack format to 121.0 and resource pack format to 97.1. These values must be versioned in the compatibility registry.
- Fabric's official 26.3 guidance recommends Loom 1.17 and Gradle 9.6.0 at the time of publication, and identifies Fabric Loader 0.19.5 as the latest stable loader at that time.
- The 26.3 release contains meaningful API and registry changes, so the generator must use the 26.3-specific adapter/template and cannot reuse older templates without migration.

Official references:
- https://www.minecraft.net/en-us/article/minecraft-java-edition-26-3
- https://fabricmc.net/2026/09/15/263.html

Recommended Java baseline profile (pending confirmation):
- Edition: java
- Game version: 26.3
- Loader: Fabric
- Loader version: 0.19.5 (revalidate at implementation start)
- Loom: 1.17 (revalidate at implementation start)
- Gradle: 9.6.0 (revalidate at implementation start)
- Data pack format: 121.0
- Resource pack format: 97.1
- Java runtime: confirm against official 26.3 metadata before implementation; do not hardcode from an unverified third-party claim.

## 3. Bedrock Edition recommendation

Recommend Bedrock 26.60 as the initial broadly released target and stable Script API 2.11.0 where scripting is required.

Evidence:
- Mojang's official Bedrock 26.60 changelog is dated 27 October 2026 and states that 26.60 is out now.
- The changelog identifies @minecraft/server 2.11.0 as released/stable and 2.12.0-beta as beta.
- The changelog also tightens validation of multiple entity and block schemas in 26.60+, so pack validation must target the selected version and reject malformed structures.
- Bedrock 26.63 is a hotfix announced on 11 November 2026 for Windows, Servers and PlayStation 5 rollout. Availability is platform-dependent; do not assume every Bedrock device receives 26.63 at the same time.

Official references:
- https://www.minecraft.net/en-us/article/minecraft--bedrock-edition-26-60-changelog
- https://feedback.minecraft.net/hc/en-us/articles/50306516691853-Minecraft-Bedrock-Edition-26-63-Hotfix-Changelog

Recommended Bedrock baseline profile (pending confirmation):
- Edition: bedrock
- Game version: 26.60
- Script API: @minecraft/server 2.11.0 stable only, if needed
- Experimental APIs: excluded from default first-slice path; require explicit opt-in and a separately identified test profile
- Bedrock 26.63 hotfix: optional follow-up validation per supported device/platform, not the baseline assumption.

## 4. Cross-platform implications

- Java 26.3 and Bedrock 26.60 are different version identifiers and independent target profiles.
- Java datapack format 121.0 does not apply to Bedrock.
- Java Fabric mod code and Bedrock behavior pack content are separate implementations.
- Resource packs use platform-specific formats and packaging even when source assets are shared.
- Every feature must have separate Java and Bedrock compatibility outcomes and evidence.
- The compatibility registry must re-check exact loader/API/toolchain releases when implementation begins; this document's versions are a dated recommendation.

## 5. Risks and mitigations

| Risk | Mitigation |
|---|---|
| Fabric ecosystem updates lag game release | Revalidate loader/API and dependencies immediately before implementation; pin tested versions |
| Java 26.3 changed APIs and data formats | Dedicated 26.3 templates, static validation and loader tests |
| Bedrock schema validation became stricter | Validate against 26.60 schemas and include negative tests |
| Bedrock hotfix availability differs by platform | Use 26.60 as common baseline; test later hotfixes per platform |
| Stable API does not cover a requested mechanic | Redesign feature to avoid experimental APIs or request explicit experimental opt-in |
| Version support drifts over time | Store source, checked date, registry revision and support status |

## 6. Decisions still required from the user

1. Approve or change Java 26.3 + Fabric.
2. Approve or change Bedrock 26.60 + stable Script API 2.11.0.
3. Confirm whether experimental Bedrock APIs are excluded from the first playable milestone (recommended: yes).
4. Confirm whether target tracks can be developed sequentially while both remain required for milestone completion.

## 7. Implementation boundary

This document records a dated compatibility recommendation only. It does not claim that these targets, loaders, APIs or build tools are already supported by the application. All versions must be revalidated from official sources at implementation start.


## 8. User decision — approved baseline

On 2026-11-28 the user explicitly approved the recommended targets:
- Java 26.3 + Fabric.
- Bedrock 26.60 + stable `@minecraft/server` 2.11.0.
- Experimental Bedrock APIs disabled for the first playable milestone.

The above are now confirmed project decisions. This section supersedes the pending-user-confirmation status in section 1 and the open approval questions in section 6. The dated research and toolchain versions remain subject to revalidation before implementation.
