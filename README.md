# Minecraft AI Mod Studio

A chat-driven Minecraft project creation platform. The long-term goal is to generate, integrate, validate, and package playable projects containing mods, worlds, datapacks, resource packs, quests, and supporting files.

## Product decisions

- Minecraft version: selected by the user for each project.
- Java mod loaders: NeoForge, Forge, Fabric.
- World generation: hybrid (prebuilt custom worlds + procedural generation).
- Workflow: guided; production requires explicit user approval.
- Scope: Java mods, Bedrock add-ons, server plugins, datapacks, resource packs, and related assets.
- Delivery: editable source/project folder, ZIP archive, and runnable artifacts such as JAR when applicable.

## Current milestone

**Milestone 0 — Project Architect foundation**

This repository currently defines the project manifest, requirement schema, architecture, and initial API contract. It is not yet a complete mod generator and does not claim to produce playable Minecraft builds.

## Planned architecture

- `apps/studio`: web chat and project workspace.
- `core/architect`: requirement analysis and project planning.
- `core/approval`: guided approval gates.
- `core/project_store`: project manifests and history.
- `engines/mod`: Java mod generation.
- `engines/map`: world and map generation.
- `engines/datapack`: datapack generation.
- `engines/resourcepack`: resource pack generation.
- `engines/integration`: cross-component validation.
- `engines/build`: isolated build workers.
- `engines/testing`: automated validation and game tests.
- `engines/export`: ZIP, folder, and artifact packaging.
- `schemas`: versioned JSON schemas.

## Design principles

1. One project manifest is the source of truth.
2. Every component declares dependencies and compatibility.
3. AI-generated changes are reviewable and reversible.
4. Build and test jobs run in isolated workers.
5. A successful JAR build is not treated as proof of in-game correctness.
6. The system reports exactly which tests passed, failed, or were not run.
7. User approval is required before production and other consequential changes.

## Local development

The first backend prototype will use Python and FastAPI. See `docs/DEVELOPMENT_PLAN.md` for the staged implementation plan.
