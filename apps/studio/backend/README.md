# Backend prototype

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open `/docs` for the interactive API documentation.

This is a deterministic planning scaffold. It is not connected to an AI provider, does not persist data across restarts, and does not generate Minecraft artifacts.
