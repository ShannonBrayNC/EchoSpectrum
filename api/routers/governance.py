from fastapi import APIRouter

router = APIRouter(prefix="/governance", tags=["governance"])


@router.get("/status")
async def governance_status() -> dict:
    return {
        "governanceMode": "rx-only",
        "etsPolicy": "active",
        "transmitAllowed": False,
    }
