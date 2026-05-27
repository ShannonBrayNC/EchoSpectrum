from fastapi import APIRouter

router = APIRouter(prefix="/mesh", tags=["mesh"])


@router.get("/nodes")
async def mesh_nodes() -> dict:
    return {
        "nodes": [
            "node-rdu-001",
            "node-fay-002",
            "node-gso-003",
        ]
    }
