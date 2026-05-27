from fastapi import APIRouter

router = APIRouter(prefix="/replay", tags=["replay"])


@router.get("/sessions")
async def replay_sessions() -> dict:
    return {
        "sessions": [
            "915mhz-survey",
            "adsb-observation",
            "24ghz-density-study",
        ]
    }
