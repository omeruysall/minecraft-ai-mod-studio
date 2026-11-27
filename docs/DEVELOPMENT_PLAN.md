# Development Plan

## Milestone 0 — Foundation
- Repository structure
- Product requirements
- Architecture and manifest schema
- Initial API contract

## Milestone 1 — Project Architect MVP
- Chat request endpoint
- Requirement extraction
- Clarification tracking
- Component plan generation
- Explicit approval state
- Persistent project manifest

Acceptance: a user request can become a structured draft plan; no generation starts before approval.

## Milestone 2 — Java mod project generator
- User-selected Minecraft version
- NeoForge, Forge, Fabric adapters
- Valid Gradle project templates
- Source folder and metadata generation

Acceptance: generate a minimal project for a selected supported version/loader and verify the build in CI.

## Milestone 3 — Build and repair
- Isolated Gradle workers
- Build logs and structured errors
- Bounded repair attempts
- Git-based change history

Acceptance: build output and failures are accurately reported; repair changes are reviewable.

## Milestone 4 — Datapack and resource pack generators
- Version-aware pack formats
- JSON/function validation
- Identifier contracts shared with the mod

## Milestone 5 — World/map generator
- Prepared-world workflow
- Structure/POI manifest
- Hybrid procedural generation adapter
- World load checks

## Milestone 6 — Integration and gameplay testing
- Dependency graph validation
- Cross-reference validation
- Dedicated test instances
- Game tests where available

## Milestone 7 — Export and delivery
- Editable source folder
- ZIP bundle
- JAR artifacts
- World/datapack/resource-pack install layout
- Installation and compatibility report

## Milestone 8 — Other ecosystems
- Paper/Spigot/Bukkit plugins
- Bedrock add-ons and Script API
- Datapack-only and resource-pack-only projects
