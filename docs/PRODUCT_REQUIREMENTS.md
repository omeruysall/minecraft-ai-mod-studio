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


## 2.1 Product delivery surface — standalone web application

The creation experience is delivered through the Minecraft AI Mod Studio website, not through the ChatGPT conversation used to plan this product.

The user opens the Studio website, signs in, creates or opens a project, and describes the desired Minecraft content in the Studio's own chat workspace. The Studio then analyzes the request, presents a structured creation plan and component table, waits for explicit approval, runs the approved generation/build/test workflow, and presents downloadable playable artifacts and evidence.

The website is the user-facing product surface. Backend services, AI orchestration, target-specific generators, isolated build/test workers and artifact storage provide the underlying execution. A chat interface by itself is not sufficient: the product must create real files and packages, validate them, and expose the results in the user's project workspace.

This current ChatGPT conversation is a planning and product-design channel only. It is not the deployed Studio website, does not execute the Studio's generation pipeline, and must not be presented as the place where the user will author or run the finished mod.
