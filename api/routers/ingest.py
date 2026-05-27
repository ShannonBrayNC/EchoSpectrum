from fastapi import APIRouter

router = APIRouter(prefix="/ingest", tags=["ingest"])


@router.get("/health")
async def ingest_health() -> dict:
    return {
        "service": "ingest",
        "status": "healthy",
        "mode": "rx-only",
    }
