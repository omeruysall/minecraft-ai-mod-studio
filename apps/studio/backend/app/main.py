from __future__ import annotations

import uuid
from typing import Literal

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(
    title="Minecraft AI Mod Studio — Project Architect",
    version="0.1.0",
    description="Initial deterministic planning API. AI provider integration is not included yet.",
)

Loader = Literal["neoforge", "forge", "fabric", "paper", "spigot", "bukkit"]


class PlanRequest(BaseModel):
    request: str = Field(min_length=10, max_length=12000)
    minecraft_edition: Literal["java", "bedrock"] = "java"
    minecraft_version: str = Field(min_length=1, max_length=32)
    loader: Loader | None = None
    world_strategy: Literal["prepared", "procedural", "hybrid"] = "hybrid"


class PlanResponse(BaseModel):
    project_id: str
    revision: int
    understanding: str
    detected_components: dict[str, bool]
    requirements: list[dict]
    component_plan: list[dict]
    open_questions: list[str]
    warnings: list[str]
    approval_required: bool = True
    status: str = "awaiting_approval"


def analyze_request(req: PlanRequest) -> PlanResponse:
    """Deterministic scaffold only; replace with a provider-backed analyzer later."""
    text = req.request.lower()

    wants_world = any(k in text for k in ["harita", "dünya", "world", "map", "şehir", "şehirler"])
    wants_datapack = any(k in text for k in ["datapack", "data pack", "veri paketi"])
    wants_resource = any(k in text for k in ["resource pack", "texture", "doku", "ses paketi", "kaynak paketi"])
    wants_quests = any(k in text for k in ["görev", "quest", "hikâye", "story"])
    wants_plugin = any(k in text for k in ["paper", "spigot", "bukkit", "sunucu eklentisi"])
    wants_bedrock = req.minecraft_edition == "bedrock"
    wants_mod = not wants_bedrock and not (wants_plugin and not any(k in text for k in ["mod", "modu"]))

    components = {
        "mod": wants_mod,
        "world": wants_world,
        "datapack": wants_datapack,
        "resource_pack": wants_resource,
        "quests": wants_quests,
        "server_plugin": wants_plugin,
        "bedrock_addon": wants_bedrock,
    }

    categories = [
        ("gameplay", "Gameplay systems and mechanics", ["açlık", "susuzluk", "hastalık", "silah", "araç", "zombi", "zombie", "boss", "entity"]),
        ("world", "World layout, structures, and points of interest", ["harita", "dünya", "şehir", "üs", "bunker", "world", "map"]),
        ("progression", "Quests, progression, and objectives", ["görev", "quest", "hikâye", "story"]),
        ("content", "Items, blocks, entities, assets, and loot", ["eşya", "blok", "ganimet", "loot", "item"]),
    ]
    requirements = []
    for idx, (category, label, keywords) in enumerate(categories, start=1):
        if any(k in text for k in keywords):
            requirements.append({
                "id": f"req_{idx:02d}_{category}",
                "description": f"Plan and implement: {label}.",
                "category": category,
                "status": "proposed",
                "target_component": "mod" if category == "gameplay" else ("world" if category == "world" else None),
            })
    if not requirements:
        requirements.append({
            "id": "req_01_general",
            "description": "Analyze the requested gameplay and content features in detail.",
            "category": "general",
            "status": "proposed",
            "target_component": None,
        })

    labels = {
        "mod": ("Java mod", "Custom runtime mechanics, entities, items, blocks, networking, and gameplay logic."),
        "world": ("Minecraft world", "Prepared scenario map, structures, regions, spawn points, and/or procedural generation."),
        "datapack": ("Datapack", "Version-supported functions, loot tables, recipes, tags, predicates, and advancements."),
        "resource_pack": ("Resource pack", "Textures, models, sounds, language files, and visual assets."),
        "quests": ("Quest/story content", "Objectives and progression, implemented in the compatible component."),
        "server_plugin": ("Server plugin", "Server-side integration for the selected plugin platform."),
        "bedrock_addon": ("Bedrock add-on", "Behavior/resource packs and supported Script API content."),
    }
    component_plan = [
        {"component": key, "name": labels[key][0], "purpose": labels[key][1], "status": "planned"}
        for key, enabled in components.items() if enabled
    ]

    questions = []
    if req.minecraft_edition == "java" and req.loader is None:
        questions.append("Which Java platform should be used: NeoForge, Forge, Fabric, or a server plugin platform?")
    if wants_world:
        questions.append("What approximate world size, starting location, and exploration boundaries do you want?")
    if wants_quests:
        questions.append("Should quests be linear story missions, optional exploration tasks, or both?")
    if not wants_world:
        questions.append("Do you also want a custom world/map designed around these mechanics?")
    if not wants_datapack:
        questions.append("Should a compatible datapack be included where it adds value?")
    if not wants_resource:
        questions.append("Do you want custom textures, models, sounds, or a resource pack?")
    questions.append("Review the plan and approve it before any files are generated.")

    warnings = [
        "This initial planner uses keyword rules; it is not yet connected to an AI model.",
        "Minecraft version, loader, Java runtime, mappings, and pack formats must be resolved against authoritative version metadata before generation.",
        "No mod, world, datapack, or JAR has been generated by this planning endpoint.",
    ]
    if req.minecraft_edition == "java" and req.loader is None:
        warnings.append("Loader is not selected yet; build templates cannot be chosen safely.")

    return PlanResponse(
        project_id="project-" + uuid.uuid4().hex[:12],
        revision=1,
        understanding=f"Draft plan for a Minecraft {req.minecraft_edition} project targeting version {req.minecraft_version}.",
        detected_components=components,
        requirements=requirements,
        component_plan=component_plan,
        open_questions=questions,
        warnings=warnings,
    )


PROJECTS: dict[str, PlanResponse] = {}


@app.get("/health")
def health():
    return {"status": "ok", "service": "project-architect", "version": "0.1.0"}


@app.post("/v1/projects/plan", response_model=PlanResponse)
def create_plan(request: PlanRequest):
    plan = analyze_request(request)
    PROJECTS[plan.project_id] = plan
    return plan


@app.post("/v1/projects/{project_id}/approve")
def approve_plan(project_id: str, revision: int):
    plan = PROJECTS.get(project_id)
    if plan is None:
        raise HTTPException(status_code=404, detail="Project not found")
    if revision != plan.revision:
        raise HTTPException(status_code=409, detail="Revision mismatch; fetch the latest plan")
    plan.status = "approved"
    return {"project_id": project_id, "revision": revision, "status": "approved"}


@app.get("/v1/projects/{project_id}", response_model=PlanResponse)
def get_project(project_id: str):
    plan = PROJECTS.get(project_id)
    if plan is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return plan
