# Prototype smoke test

1. Start the API with Uvicorn.
2. Call `GET /health`.
3. Call `POST /v1/projects/plan` with a Turkish zombie-survival request, Java edition, a chosen Minecraft version, and `neoforge`.
4. Confirm the response contains a project ID, component table, requirements, questions, and warnings.
5. Fetch the project with `GET /v1/projects/{project_id}`.
6. Approve the exact revision with `POST /v1/projects/{project_id}/approve?revision=1`.
7. Confirm the status changes to `approved`.

This is an API contract smoke test, not a Minecraft gameplay test.
