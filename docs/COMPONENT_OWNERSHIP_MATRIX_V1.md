# Component Ownership Matrix v1.0

**Status:** Design draft | **Implementation:** Not implemented | **Authority:** Proposed logical ownership

## 1. Purpose
Establish one accountable owner for each domain capability, define what each module may change, and prevent overlapping responsibilities. Ownership here means logical product/data responsibility, not a mandatory microservice deployment topology.

## 2. Ownership rules
- Every canonical entity has one authoritative owner.
- Other modules consume published contracts and request changes through the owning module.
- Cross-cutting policies (security, audit, observability) are enforced across modules, not duplicated as independent sources of truth.
- UI components do not own business rules or bypass server-side authorization.
- Workers execute bounded jobs but do not own approvals, project policy or canonical project state.
- Shared libraries contain schemas/utilities, not hidden domain ownership.
- Ownership changes require an architecture decision and migration plan.

## 3. Core control-plane ownership
| Domain/module | Owns | Does not own | Main integrations |
|---|---|---|---|
| Experience Shell | Navigation, workspace composition, client state presentation | Project policy, permissions, production logic | Project Workspace, Chat, Community |
| Project Workspace | Project navigation, project-level views and user interactions | Canonical project data or approval decisions | Project API, Manifest, Collaboration |
| Conversation Service | Conversation sessions, message ordering and conversation references | Final requirements truth or provider secrets | AI Gateway, Requirements Analyzer |
| Requirements Analyzer | Extracted requirements, ambiguity/confidence and user-confirmed requirement records | Project manifest persistence or production | Conversation, Project Architect |
| Project Architect | Plan revisions, clarification workflow, component proposal and approval gate | Artifact-specific code generation | Manifest, Compatibility, Dependency Graph, Engines |
| Approval Manager | Approval records, scope hash, actor and revision binding | User identity lifecycle or artifact production | Project Architect, Security, Jobs |
| Manifest Service | Canonical project schema, revisions, migrations and project state | Binary blob storage or engine-specific generation | All modules |
| Feature Catalog | Stable feature IDs, capability definitions and catalog metadata | Project-specific implementation status without evidence | Project Architect, Traceability |

## 4. Planning and compatibility ownership
| Domain/module | Owns | Does not own | Main integrations |
|---|---|---|---|
| Minecraft Compatibility Engine | Edition/version/loader/runtime support declarations and compatibility evidence | Artifact generation | Project Architect, Dependency Resolver, Engines |
| Dependency Graph Service | Dependency edges, constraints, cycle detection and impact traversal | Choosing product requirements or generating artifacts | Manifest, Component Planner, Integration |
| Component Planner | Component decomposition and target-specific work plans | Canonical component records after plan commit | Project Architect, Manifest, Engines |
| Impact Analyzer | Change impact and affected-component calculation | Mutating components automatically | Dependency Graph, Manifest, Jobs |
| Execution Planner | Job DAG, ordering, resource estimates and retry eligibility | Worker execution or approval | Job Orchestrator, Approval Manager |

## 5. AI and provider ownership
| Domain/module | Owns | Does not own | Main integrations |
|---|---|---|---|
| AI Gateway | Provider-neutral request routing, capability matching, policy and budget enforcement | User-owned secret storage or project approvals | Provider Registry, Project Architect, Asset Pipeline |
| Provider Registry | Provider/model metadata, capability and availability records | Provider billing account or user secrets | AI Gateway, Settings |
| Credential Vault | Encrypted provider credentials, scopes, rotation and revocation | Model selection or prompt policy | AI Gateway, Security |
| Prompt/Policy Registry | Versioned system templates, task policies and prompt-injection boundaries | User conversation history | AI Gateway, Security |
| Realtime Voice Service | Voice session lifecycle, audio transport and speech pipeline orchestration | Conversation ownership or permanent audio retention policy | Conversation, AI Gateway, Voice Studio |

## 6. Production engine ownership
| Engine | Owns | Must not own |
|---|---|---|
| Java Mod Engine | Java mod source, loader adapter and mod-specific validation | Shared project manifest, global dependency graph |
| Bedrock Add-on Engine | Behavior/resource pack source and Bedrock validation | Java loader compatibility |
| Datapack Engine | Datapack source, functions, data registries and validation | World engine canonical world state |
| Resource Pack Engine | Pack metadata, textures, models, fonts, sounds and pack validation | Global asset provenance registry |
| Map/World Engine | World generation/edit operations, world metadata and world validation | Server deployment credentials |
| Quest/Story Engine | Quest graph, narrative state definitions and quest validation | NPC runtime implementation |
| NPC/Character Engine | Character definitions, behavior/dialogue bindings and character assets references | General combat balance authority |
| Combat/AI Behavior Engine | Combat state, threat, targeting, attacks and combat balance | General NPC identity/canon |
| Environment Interaction Engine | Interactable blocks/entities, mechanisms, hazards and interaction rules | World event scheduling |
| Events/Simulation Engine | Scheduled events, simulation rules and event lifecycle | Ecology species canonical definitions |
| Ecology/Wildlife Engine | Species, habitats, population and ecological simulation rules | General NPC faction/quest ownership |
| Economy/Trade Engine | Currency, balances, transactions, prices, shops and trade ledger | Crafting recipe definitions |
| Crafting/Production Engine | Recipes, stations, production queues and crafting outputs | Economy ledger authority |
| Transportation/Infrastructure Engine | Routes, vehicles, networks and transport capacity | Settlement governance or player inventory ownership |
| Settlement/City Engine | Settlement entities, districts, zoning and municipal governance | NPC character identity or economy ledger |
| Professions/Progression Engine | Skills, XP, professions, unlock rules and player progression | Combat implementation or quest graph |
| Farming/Food Engine | Crop/livestock cycles, harvest and food production definitions | Global ecology species canon |
| Survival/Needs Engine | Hunger, thirst, temperature, fatigue and status simulation | Player identity or inventory storage |
| Items/Equipment/Loot Engine | Item definitions, equipment slots, modifiers and loot generation | Economy transaction ledger |
| Magic/Technology Engine | Magic/technology capability definitions and their runtime adapters | Generic AI provider routing |
| Structure/Building Engine | Structure templates, placement rules and building assembly | World terrain ownership |
| Animation Engine | Animation definitions, rigs, clips and export validation | Character identity or asset registry |
| Sound/Music Engine | Sound/music asset production and integration metadata | Global asset provenance |

Each production engine emits versioned artifacts and validation evidence, references shared assets by immutable asset-version ID, and consumes the approved project revision. Engine-specific details remain in its dedicated specification.

## 7. Shared production and execution ownership
| Domain/module | Owns | Does not own |
|---|---|---|
| Asset Registry | Asset identity, immutable versions, hashes, provenance and references | Asset generation or project-wide approvals |
| AI Asset Pipeline | Asset briefs, generation/conversion tasks and media-specific quality checks | Canonical asset version registry |
| Job Orchestrator | Job records, queue lifecycle, cancellation, retries and worker dispatch | Domain artifact semantics |
| Build Workers | Isolated compilation/package execution and build logs | Approval, project mutation or secret policy |
| Test Workers | Isolated static/load/runtime/performance test execution and evidence | Declaring unrun tests as passed |
| Integration Engine | Cross-component references, package composition and final integration report | Rewriting domain specifications without owner approval |
| Repair Planner | Failure classification and bounded repair proposals | Unreviewed destructive edits or bypassing approval |
| Artifact Store | Binary object storage, immutable object IDs and transfer metadata | Project manifest or release ownership |
| Export Engine | User-requested export assembly and export manifest | Public release publication |

## 8. Distribution and community ownership
| Domain/module | Owns | Does not own |
|---|---|---|
| Release Manager | Immutable release records, version metadata and release lifecycle | Project source of truth |
| Publishing Adapters | Destination-specific upload/metadata behavior | Release approval or project ownership |
| Update Service | Update discovery, compatibility comparison and update plans | Silent installation or world migration |
| Installer/Deployment Adapters | Explicitly authorized local/server installation operations | Server credentials beyond scoped use |
| Community Catalog | Public listing, search, discovery and listing metadata | Artifact generation or technical certification |
| Moderation Service | Reports, cases, decisions, appeals and enforcement records | Technical compatibility verdicts |
| Review/Rating Service | User reviews, ratings and abuse controls | Moderation case final decision |

## 9. Security, data and governance ownership
| Domain/module | Owns | Enforcement expectation |
|---|---|---|
| Identity Service | Account identity and authentication session records | Authentication at trust boundary |
| Authorization Policy Engine | Roles, permissions, scoped grants and policy evaluation | Every protected API and job action |
| Audit Service | Append-oriented security and lifecycle events | All privileged/destructive actions |
| Backup/Recovery Service | Snapshot manifests, verification, retention and restore plans | Explicit confirmation before overwrite |
| Storage/Sync Service | Local/remote synchronization metadata and conflict detection | No unsafe last-write-wins on critical data |
| Moderation Policy | Community content rules and enforcement criteria | Human review/appeal according to policy |
| Observability | Metrics, traces and redacted operational logs | No secret or private prompt leakage |

## 10. Canonical data ownership map
- Project and ProjectRevision: Manifest Service.
- Requirement and PlanRevision: Requirements Analyzer / Project Architect, with canonical persistence through Manifest Service.
- Approval: Approval Manager.
- Component and DependencyEdge: Manifest Service and Dependency Graph Service respectively.
- CompatibilityClaim and CompatibilityEvidence: Compatibility Engine.
- Asset and AssetVersion: Asset Registry.
- Job and JobAttempt: Job Orchestrator.
- BuildArtifact and TestEvidence: respective workers produce; Evidence Registry/Manifest references canonicalize.
- Release: Release Manager.
- BackupSnapshot and RestorePlan: Backup/Recovery Service.
- User, Session, RoleGrant and PermissionDecision: Identity and Authorization services.
- ModerationCase: Moderation Service.
- AuditEvent: Audit Service.

## 11. Cross-module contract rules
1. Modules exchange stable IDs and versioned schemas, not private database table access.
2. Mutations to canonical records pass through their owning service.
3. Events are versioned, idempotent and include project/revision context.
4. Consumers tolerate unknown optional fields and reject unsupported major schema versions.
5. Workers receive least-privilege, revision-pinned job inputs.
6. Artifact references include hashes and immutable version IDs.
7. Failures are returned as typed results; no silent fallback to fabricated success.
8. Ownership boundaries are reflected in API contracts, tests and operational logs.

## 12. Deployment topology guidance
Begin with a modular monolith for control-plane domains and isolated worker processes for untrusted generation/build/test tasks. Keep provider adapters and storage behind interfaces. Split into separately deployed services only when scaling, availability, security isolation or independent release cadence justifies it. Logical ownership does not require one microservice per row.

## 13. Ownership conflict resolution
If two modules claim the same canonical field or state transition, the Manifest/Architecture owner records an architecture decision. The decision identifies the authoritative owner, migration impact, API/event changes and test updates. Until resolved, conflicting writes are blocked rather than duplicated.

## 14. Acceptance criteria
- Every domain capability has one named logical owner.
- Canonical data has one authoritative owner.
- No UI or worker bypasses server-side policy.
- Production engines consume pinned project revisions and shared asset versions.
- Cross-engine references are validated by Integration Engine.
- Security and audit controls apply across module boundaries.
- Logical modules can be tested independently through contracts.
- Deployment topology remains free to evolve without changing ownership semantics.

## 15. Open decisions
1. Which modules are in-process packages versus isolated worker services in the first release?
2. Is Evidence Registry a dedicated module or part of Manifest/Job services?
3. Is Asset Registry a separate service or a bounded context within project storage?
4. Which domain engine is selected for the first vertical slice?
5. Which modules may own player runtime persistence in multiplayer projects?
6. What is the final permission model for module-level administrative operations?
7. Which events require durable delivery and replay?
8. What is the approved local/cloud deployment split?

## 16. Implementation boundary
This matrix defines proposed responsibility boundaries only. It does not establish that these modules, services, databases, workers or APIs have been implemented.

## 17. Related specifications
Master Integration Audit, Architecture, API Contract v2, Project Manifest v2, Project Architect Decision Engine, all production-engine specifications, Security/Permissions/Moderation, Publishing/Versioning and Backup/Recovery.