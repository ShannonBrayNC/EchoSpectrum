from __future__ import annotations

from dataclasses import dataclass, asdict
from datetime import datetime, UTC


@dataclass(frozen=True)
class MeshNode:
    node_id: str
    sensor_profile: str
    antenna_profile: str
    governance_mode: str
    health_status: str


@dataclass(frozen=True)
class MeshHeartbeat:
    node_id: str
    timestamp_utc: str
    status: str


class MeshCoordinator:
    def __init__(self) -> None:
        self.nodes: dict[str, MeshNode] = {}
        self.heartbeats: list[MeshHeartbeat] = []

    def register_node(self, node: MeshNode) -> None:
        self.nodes[node.node_id] = node

    def record_heartbeat(self, node_id: str, status: str = "healthy") -> MeshHeartbeat:
        heartbeat = MeshHeartbeat(
            node_id=node_id,
            timestamp_utc=datetime.now(UTC).isoformat(),
            status=status,
        )
        self.heartbeats.append(heartbeat)
        return heartbeat

    def summary(self) -> dict:
        return {
            "nodeCount": len(self.nodes),
            "heartbeatCount": len(self.heartbeats),
            "generatedUtc": datetime.now(UTC).isoformat(),
        }
