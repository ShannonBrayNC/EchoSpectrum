from fastapi import FastAPI
from api.routers import ingest, replay, mesh, governance

app = FastAPI(
    title="EchoSpectrum Observatory API",
    version="0.1.0",
    description="Governance-aware RF observability platform",
)

app.include_router(ingest.router)
app.include_router(replay.router)
app.include_router(mesh.router)
app.include_router(governance.router)


@app.get("/")
async def root() -> dict:
    return {
        "platform": "EchoSpectrum",
        "mode": "rx-only",
        "status": "operational",
    }
