from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, UTC


@dataclass(frozen=True)
class WebsocketClient:
    client_id: str
    connected_utc: str


class ObservatoryGateway:
    def __init__(self) -> None:
        self.clients: list[WebsocketClient] = []

    def register_client(self, client_id: str) -> WebsocketClient:
        client = WebsocketClient(
            client_id=client_id,
            connected_utc=datetime.now(UTC).isoformat(),
        )
        self.clients.append(client)
        return client

    def connected_client_count(self) -> int:
        return len(self.clients)
