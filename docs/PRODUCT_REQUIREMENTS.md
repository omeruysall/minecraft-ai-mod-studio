# Product Requirements — v1.0

## User journey

1. The user describes a Minecraft idea in a chat.
2. The assistant restates the request in clear terms.
3. The assistant asks only essential clarification questions.
4. The assistant prepares a component creation table.
5. The assistant proposes compatible Minecraft version, loader, dependencies, and component boundaries.
6. The user reviews and approves the plan.
7. Generators create the approved components against one shared project manifest.
8. Integration checks validate identifiers, references, dependencies, versions, world content, and datapack links.
9. Build and test workers run in isolation.
10. The assistant prepares a delivery bundle containing the project folder, ZIP, JAR (when applicable), world, datapack, resource pack, documentation, and test report.

## Fixed product decisions

- Version is selected by the user per project.
- World creation is hybrid: prepared worlds and procedural generation.
- Workflow is guided.
- Scope includes all major Minecraft creation types.
- Delivery includes editable files and packaged outputs.

## Approval rules

- No code/world/package production before plan approval.
- New features are analyzed as changes to the existing project, not automatically treated as a new project.
- Changes that alter public IDs, save compatibility, world generation, dependencies, or existing gameplay require explicit approval.
- The user can request a plan revision before approval.

## Definition of done

A project is only labelled playable after the supported launch and integration tests have passed. Build success alone is insufficient. The report must distinguish:
- source validation,
- build validation,
- datapack/resource validation,
- world-load validation,
- integration validation,
- in-game or automated game-test validation.

Unsupported tests must be marked “not run”, never silently treated as passed.
