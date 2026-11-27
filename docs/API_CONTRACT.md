# Initial API Contract

The first backend should expose:

- `GET /health` — service health.
- `POST /v1/projects/plan` — convert a chat request and selected Minecraft target into a draft project plan.
- `POST /v1/projects/{project_id}/approve` — approve a specific plan revision.
- `GET /v1/projects/{project_id}` — retrieve the project manifest.
- `POST /v1/projects/{project_id}/messages` — append a follow-up request and produce a revised plan.

All plan-generation responses must include:
- a plain-language understanding of the request,
- detected requirements,
- proposed components,
- open questions,
- compatibility warnings,
- a revision number,
- `approval_required: true`.

No generation endpoint should be callable for an unapproved plan.
