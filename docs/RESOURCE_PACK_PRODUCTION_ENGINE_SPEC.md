# Resource Pack Production Engine Specification

**Document status:** Design draft  
**Version:** 0.1  
**Implementation status:** Not implemented  
**Scope:** Java Edition resource packs, Bedrock Edition resource packs, and resource-pack components inside multi-artifact projects.

**Governing rule:** This specification does not authorize asset generation, conversion, packaging, installation, or application-code changes. Production begins only after the relevant plan revision receives explicit user approval.

## 1. Purpose and outcomes

The Resource Pack Production Engine creates, imports, edits, validates, packages, and delivers Minecraft visual, audio, interface, and localization assets. It supports standalone packs and resource-pack components coordinated with Java mods, Bedrock add-ons, datapacks, maps, and modpacks.

A completed production run should provide:
- A platform- and version-targeted resource pack.
- Editable source assets and project metadata.
- A distributable Java resource-pack ZIP or Bedrock resource-pack package, as applicable.
- An asset inventory with stable IDs, paths, formats, dimensions, dependencies, provenance, and validation results.
- Preview material and a review history.
- Compatibility and test evidence, including explicit "not run" results.
- A reproducible production record identifying inputs, transformations, tool versions, and outputs.

Generated images or successful archive creation are not proof that a pack works in Minecraft.

## 2. Supported asset domains

The registry should model these asset domains independently:
1. Block textures, visual variants, and connected textures where supported.
2. Item textures, icons, sprites, and variants.
3. Entity, mob, and player-related textures.
4. Model geometry and model references supported by the selected target.
5. Animation resources and controllers where supported.
6. Particle textures and visual effects.
7. Sound effects, ambient audio, and music where permitted by the target format.
8. UI textures, icons, panels, buttons, cursors, and other supported interface resources.
9. Fonts, glyph resources, and localization files.
10. Environment, sky, panorama, and other supported world-presentation assets.
11. Pack metadata, icons, attribution files, and required manifests.
12. Optional documentation, preview sheets, and source-generation metadata.

The Minecraft Version Compatibility Engine determines which domains and features are valid for each Java or Bedrock target. Listing a domain here does not imply identical support across editions or versions.

## 3. Platform and target profiles

Every pack must declare:
- Minecraft edition: Java or Bedrock.
- Exact Minecraft version or supported version range.
- Required pack format or manifest format, resolved by the compatibility engine.
- Companion components and external dependencies.
- Intended use: standalone, mod companion, add-on companion, world companion, or modpack component.
- Distribution and installation expectations.

Each edition/version combination is a separate build profile. A single package must never be assumed portable between Java and Bedrock.

If a feature cannot be represented equivalently across targets, the planner must propose a platform-specific variant, a documented fallback, or an explicit unsupported-feature decision. It must not silently omit the feature.

## 4. Ownership and technical boundaries

The Resource Pack Engine owns presentation assets and resource-pack structure, not gameplay behavior or server logic.

- Java mods own custom runtime behavior, registries, and custom content definitions. Packs may supply corresponding textures, models, sounds, and language entries.
- Bedrock behavior packs and Script API own supported behavior. Bedrock resource packs own presentation assets and references.
- Datapacks own supported data-driven gameplay systems. Packs may supply associated visual/audio resources.
- Worlds own terrain, structures, and placement; worlds may reference one or more packs.
- Server plugins own server-side behavior; pack delivery may integrate where the server platform supports it.

Cross-component references use stable project, component, and asset IDs rather than display names or guessed paths.

## 5. Shared asset registry

Every asset receives a stable ID and a registry record containing:
- Asset ID, name, domain, and type.
- Target platform and version profile(s).
- Canonical project-relative path.
- Source type: user upload, generated, imported, transformed, or project-provided.
- Source reference and provenance.
- MIME type, extension, dimensions, duration, color mode, and file size where applicable.
- Resolution, frame rate, sample rate, channel count, or other type-specific metadata.
- Dependencies, references, and companion assets.
- License/rights status and attribution requirements.
- Current revision, parent revision, and transformation history.
- Validation status and test evidence.
- Ownership and edit/replace permissions.

The registry detects duplicate IDs, conflicting output paths, orphaned references, missing dependencies, and accidental replacement of user-owned assets.

## 6. Asset creation and acquisition

Supported input routes:
1. AI-assisted generation from a user-approved brief.
2. User-uploaded image, audio, model, font, or other supported source files.
3. Import from an existing resource pack or project.
4. Creation/editing in a supported external tool followed by re-import.
5. Reuse of an existing project asset through an explicit reference.

Before generation, AI prepares an asset brief defining intended use, visual/audio direction, target dimensions or technical constraints, target profile, variants, and dependent components. The user reviews and approves the asset plan before bulk generation. Approval binds to the exact asset list and revision.

## 7. Image and texture pipeline

Image workflows should support:
- Prompt and reference-image analysis.
- Pack-wide style and palette consistency.
- Asset-specific composition and silhouette requirements.
- Target resolution and aspect-ratio constraints.
- Transparency and alpha-channel handling.
- Seamless/tileable texture checks when required.
- Sprite-sheet and atlas planning where supported.
- Variants for states, directions, damage, growth, and other supported transitions.
- User review, selection, regeneration, and manual replacement.

Generated images are intermediate assets until target-specific processing and validation pass. Validate dimensions, color mode, transparency, format, tiling behavior, and platform constraints.

User reference images remain linked to their source records. Uploading a reference does not imply permission to redistribute it or use it for model training.

## 8. Models, geometry, and animation

Model support is profile-driven and distinguishes native target formats, version-specific conventions, external editor formats, and intermediate conversion formats.

A model workflow should validate geometry, texture/material references, UVs where applicable, pivots/origins, hierarchy, animation bindings, scale, and orientation.

Animation must explicitly identify its target mechanism, such as Java model conventions or Bedrock animation resources/controllers. Cross-edition equivalence must not be promised where the platforms differ.

Conversion preserves original sources and records unsupported or lossy transformations. The user receives a report before accepting conversions that alter geometry, materials, animation, or fidelity.

## 9. Audio pipeline

Audio resources may include sound effects, ambience, and music supported by the target profile. Validate:
- Supported codec and container.
- Sample rate, bit depth, channel layout, duration, and file size.
- Loop points and seamless-loop behavior where relevant.
- Sound-event/resource-reference mapping.
- Missing or duplicate event identifiers.
- Relative loudness and clipping where measurable.
- Metadata and attribution.

Preserve original audio. Record lossy conversion. A decodable audio file is not proof that Minecraft references or plays it correctly.

## 10. UI, fonts, glyphs, and localization

UI and font resources are edition- and version-sensitive. Resolve supported paths, formats, glyph definitions, and override behavior from the target profile.

Localization should include:
- A user-selected canonical source language.
- Stable translation keys.
- Target-language files and locale validation.
- Missing/duplicate keys, malformed encoding, and placeholder-consistency checks.
- Preservation of user-authored wording unless a change is approved.
- Text clipping and glyph-availability previews where feasible.

Do not silently overwrite vanilla or other pack resources. Show override conflicts in the plan and final report.

## 11. Consistency and design system

For packs with multiple assets, optional style constraints may cover palette/material conventions, pixel-art or high-resolution direction, outlines and shading, naming/iconography, entity/block/item relationships, audio loudness/sonic identity, and UI typography/spacing.

Consistency checks may flag outliers. They must not automatically modify an approved asset without creating a new revision and obtaining the required approval.

## 12. Import, conversion, and optimization

Import workflow:
1. Inspect archives and source files without executing them.
2. Detect platform, structure, metadata, and probable version targets.
3. Build an import manifest and dependency map.
4. Identify invalid files, unsupported assets, duplicate paths, and licensing uncertainty.
5. Preview proposed path or format migrations.
6. Preserve the original import as an immutable source snapshot.
7. Apply only approved transformations to a new working revision.

Optimization may include image compression, resizing, audio conversion, redundant-file detection, and packaging improvements. Respect target requirements and user-selected quality constraints. Never silently reduce resolution, remove metadata, or degrade audio.

## 13. Dependencies and cross-component integration

The shared dependency graph represents:
- Mod-defined block/item/entity identifiers and presentation assets.
- Bedrock behavior-pack identifiers and resource-pack bindings.
- World/map pack references.
- Datapack-associated visual/audio resources.
- Modpack resource-pack ordering and required dependencies.
- External pack dependencies and declared minimum versions.

Validate that referenced assets exist and identifiers match the owning component's approved specification. If an upstream component changes an identifier or removes an asset, mark affected resources for review or regeneration.

## 14. Validation and testing ladder

Record these levels separately:
1. File integrity: files readable and archives structurally valid.
2. Asset validation: dimensions, formats, metadata, and required properties.
3. Reference validation: identifiers, paths, localization keys, and dependencies resolve.
4. Pack-structure validation: required paths and metadata conform to the target.
5. Compatibility validation: pack format and features match the selected version.
6. Client import validation: target client accepts/imports the pack.
7. In-game visual validation: assets render correctly in representative contexts.
8. Integration validation: companion mods, add-ons, worlds, or modpacks resolve expected resources.
9. Regression validation: changes do not break previously approved assets.

Each result is passed, failed, blocked, or not run, with target profile, tool/client version, timestamp, logs, and evidence references where available. Static checks cannot substitute for client import or in-game testing. If the required client cannot be launched, mark the test "not run".

## 15. Preview and review experience

Where technically possible, the workspace provides:
- Asset gallery filtered by domain, status, platform, and revision.
- Before/after comparison.
- Texture zoom and tiled previews.
- Model preview with orientation and animation controls.
- Audio audition, waveform, and metadata.
- Localization preview and missing-glyph warnings.
- Pack-level preview and dependency summary.
- Per-asset approval, replacement, rejection, and revision history.

Previews are labelled as previews and do not imply in-game correctness unless the relevant client test passed.

## 16. Approval and revision control

Enforce the shared project approval model:
- AI proposes an asset plan and records its revision.
- User reviews scope, briefs, target profiles, dependencies, and rights information.
- Production starts only after explicit approval of that exact revision.
- Material changes to platform, scope, source, quality constraints, or dependencies invalidate affected approvals.
- Generated assets enter a review state before acceptance into the approved component.
- User originals are preserved; replacement creates a new revision.
- Rejected assets remain in revision history unless deletion is requested under the retention policy.

Approval of one component does not approve unrelated project components.

## 17. Packaging and delivery

Package separately for each approved target profile. Expected outputs:
- Java Edition resource-pack ZIP with target-correct structure and metadata.
- Bedrock resource-pack package, such as an MCPACK archive, when supported by the target.
- Editable source asset directory or archive.
- Asset registry and dependency manifest.
- Rights and attribution report.
- Validation/test report.
- Preview gallery or review summary.
- Reproducibility record.

Inspect the package after creation: verify archive integrity, expected paths, metadata, and referenced files. Packaging success does not establish successful import or in-game behavior.

## 18. Installation and activation safety

Installation is optional and separate from export. It requires explicit user approval. Prefer export/import instructions or supported safe installation interfaces over direct game-directory modification.

If direct installation is supported later:
- Detect the intended game installation/profile.
- Show exact destination and files to be added or changed.
- Preserve existing packs and configuration.
- Never overwrite an existing pack without explicit confirmation.
- Support rollback/removal of only files installed by this operation.
- Record installation results separately from package validation.

Do not access unrelated user files or execute imported content during inspection.

## 19. Security, privacy, and rights

- Treat imported archives and assets as untrusted input.
- Reject path traversal, archive bombs, malformed metadata, and unsafe file types.
- Do not execute scripts or binaries during inspection/conversion.
- Isolate conversion and preview workloads with resource limits.
- Scan archives and validate paths before extraction.
- Protect uploads through project access controls.
- Record origin and declared license of imported/generated assets.
- Require user confirmation of redistribution rights where licensing is unclear.
- Do not represent generated or external assets as official Mojang/Microsoft assets.
- Preserve attribution and license notices during optimization and packaging.

Rights uncertainty must block or flag distribution when material.

## 20. Observability and failure handling

Each job records job/project/component IDs, approved plan revision, target profile, engine/tool versions, input asset IDs and checksums, generation/conversion/optimization steps, warnings/errors/retries/resource usage, per-asset and pack-level test outcomes, and output artifact IDs/checksums/storage references.

Failures must be scoped and actionable. A failed asset must not silently invalidate unrelated assets. Retries should be deterministic where possible and must not overwrite an approved output revision.

## 21. Non-functional requirements

Design for reproducible builds, traceable asset lineage, incremental regeneration, safe cancellation, resumable jobs, large asset handling, storage quotas and cleanup, performant previews on desktop/mobile, accessible review controls, clear local/cloud processing boundaries, and offline access to downloaded assets and metadata where supported.

Performance targets, storage limits, and maximum asset sizes remain open.

## 22. Open design decisions

These are not approved decisions and must be resolved or explicitly deferred during design review:

1. First-release Java/Bedrock version matrix and minimum versions.
2. Whether both editions ship in the first release or one is prioritized.
3. Approved AI image-generation providers and local-model support.
4. Whether 3D model generation is first-release functionality or import/edit only.
5. Supported model editors and interchange formats.
6. First-release animation authoring scope.
7. Audio generation providers, codec policy, and licensing controls.
8. Font/glyph authoring scope, including UI override support.
9. Default texture resolutions and quality presets.
10. Texture atlas and connected-texture scope.
11. Local/cloud split for generation, conversion, storage, and preview.
12. Automated visual regression and in-game screenshot testing strategy.
13. Supported client-launch/testing environments.
14. Packaging and direct-installation support by edition and operating system.
15. Asset retention, quota, backup, and deletion policy.
16. External pack import policy and license-verification responsibilities.
17. Whether standalone pack publishing requires separate moderation.
18. Whether generated assets require individual approval or can be approved in batches.
19. Required provenance metadata for generated and user-provided reference assets.
20. Mobile preview capabilities versus desktop-only advanced model/audio tools.

No default should be treated as approved merely because it is convenient to implement.

## 23. Design acceptance criteria

This specification is ready for baseline review when:
- Java and Bedrock profiles are represented separately.
- Asset domains, ownership boundaries, and registry fields are defined.
- Uploads, generated/imported assets, and conversions have traceable provenance.
- Approval is bound to an exact asset-plan revision.
- Cross-component references use the shared dependency graph.
- Static checks, client import, in-game behavior, and integration tests are distinct.
- Packaging outputs and limitations are explicit.
- Installation is separate from export and requires approval.
- Rights, security, and preservation of user originals are addressed.
- Open decisions are resolved or explicitly deferred.
- No implementation status is claimed by this document.

## 24. Related specifications

This document must remain consistent with the product requirements, overall architecture, Project Architect Decision Engine, approval workflow, Minecraft Version Compatibility Engine, Java Mod Production Engine, Bedrock Add-on Production Engine, Datapack Production Engine, shared project manifest/schemas/dependency graph, and Studio interface/project workspace/delivery workflow.

Conflicts must be recorded and resolved before implementation. This document does not authorize source-code changes or production execution.
