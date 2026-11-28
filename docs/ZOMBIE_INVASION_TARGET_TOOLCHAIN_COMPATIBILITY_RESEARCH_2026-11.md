# Zombie Invasion — Target Toolchain Compatibility Research (2026-11)

**Status:** Documentation-based compatibility research; not a successful build or runtime test  
**Research date:** 2026-11-28  
**Targets:** Java Edition 26.3 + Fabric; Bedrock Edition 26.60 + stable Script API 2.11.0

## 1. Executive result

The user's selected Minecraft targets are supported by current ecosystem documentation at the time of this research. The exact toolchain can now be narrowed to current candidate versions, but a reproducible project build and in-game launch have not been run. The manifest therefore records recommendations as candidates and keeps build verification false.

## 2. Java Edition 26.3

The current official Fabric Develop page's generated recommendation for Minecraft 26.3 lists:

| Component | Current candidate | Status |
|---|---:|---|
| Minecraft | 26.3 | User-approved exact target |
| Fabric Loader | 0.20.1 | Current Fabric recommendation |
| Fabric Loom | 1.19-SNAPSHOT | Current Fabric recommendation; snapshot pin needs deliberate handling |
| Fabric API | 0.166.0+26.3 | Current Fabric recommendation |
| Java runtime | 25+ | Minecraft runtime baseline derived from Mojang launcher metadata |
| Gradle | Unresolved | Must be pinned against the selected Loom build and wrapper compatibility |

Sources:
- Fabric's current version selector and recommended project properties: https://fabricmc.net/develop/
- Fabric Loader 0.20.1 release history: https://github.com/FabricMC/fabric-loader/releases
- Fabric Loom release history: https://github.com/FabricMC/fabric-loom/releases
- Minecraft 26.3 release notes: https://www.minecraft.net/en-us/article/minecraft-java-edition-26-3
- Java 25 runtime metadata for 26.3 is exposed from Mojang's version manifest; a current mirror that reads that manifest reports 25+: https://mcreference.com/minecraft-versions/26.3

The September 15, 2026 Fabric 26.3 announcement initially listed Loom 1.17, Gradle 9.6.0 and Loader 0.19.5. Those were time-of-release recommendations. The current Fabric Develop selector now lists Loader 0.20.1, Loom 1.19-SNAPSHOT and Fabric API 0.166.0+26.3; the current selector supersedes the earlier release-day versions for a new project. The Gradle wrapper must be selected after resolving the chosen Loom artifact rather than copied blindly from the older post.

### Java build decisions still open

1. Whether to use the current documented Loom 1.19-SNAPSHOT or a stable Loom 1.19 release after confirming its Minecraft 26.3 support.
2. The exact Gradle wrapper version compatible with that Loom selection.
3. The exact JDK distribution and patch build for Java 25.
4. Dependency lock/checksum and reproducible build verification.
5. A clean Fabric client launch and mod loading test on Minecraft 26.3.

The official Fabric 26.3 notes also document material API changes, including removed registry APIs and new item-component/data-driven paths. Code generation must target the 26.3 APIs, not copy older 1.21-era examples without review.

## 3. Bedrock Edition 26.60

The official Minecraft Bedrock 26.60 changelog, posted 2026-10-27, explicitly states that `@minecraft/server` 2.11.0 was released as stable. It also identifies 2.12.0-beta separately. The project must therefore pin stable 2.11.0 and must not use beta/experimental APIs under the user's decision.

Sources:
- Official Bedrock 26.60 changelog: https://feedback.minecraft.net/hc/en-us/articles/49852828563853-Minecraft-Bedrock-Edition-26-60-Changelog
- Official Minecraft-hosted changelog: https://www.minecraft.net/nb-no/article/minecraft--bedrock-edition-26-60-changelog
- Microsoft Learn Script API module documentation: https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server/minecraft-server?view=minecraft-bedrock-stable

### Bedrock validation still open

1. Confirm the actual 26.60 pack format fields and supported minimum engine versions for the chosen behavior/resource packs.
2. Confirm the stable 2.11.0 module declaration and peer dependencies in the generated manifest.
3. Check every planned API call against stable 2.11.0 rather than beta documentation.
4. Import the behavior/resource packs into a clean 26.60 world and validate warnings/errors.
5. Run actual gameplay tests on the target runtime/device.

## 4. Compatibility implications for the Zombie Invasion design

- Java and Bedrock must remain separate build targets. Shared gameplay contracts do not imply shared source code or binaries.
- Java 26.3 uses its own item, registry, world-generation and resource/data pack formats. Target formats must be generated from the 26.3 version metadata and official docs.
- Bedrock 26.60 has stricter entity/AI schema parsing for multiple components. Entity JSON must be schema-validated and tested on the exact target.
- Experimental Bedrock features are excluded. A feature requiring an experimental API must be redesigned, deferred or marked unsupported; it must not silently enable an experiment.
- The feature matrix's Java, Bedrock and parity states remain `not_assessed` until target-specific implementation evidence exists.

## 5. Manifest update

`schemas/zombie-invasion.project-manifest.v2.draft.json` now records the current Fabric candidates (Loader 0.20.1, Loom 1.19-SNAPSHOT, Fabric API 0.166.0+26.3), Java 25+, and stable Bedrock Script API 2.11.0. Gradle and Bedrock pack format remain unresolved. The manifest's toolchain build verification flag remains false.

## 6. Implementation boundary

This research narrows toolchain selection. It does not prove that the project compiles, that Fabric supports every selected feature, that Bedrock exposes equivalent capabilities, or that a generated package loads. These claims require a reproducible build and target runtime evidence for each edition.
