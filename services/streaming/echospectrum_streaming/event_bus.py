from __future__ import annotations

import asyncio
from dataclasses import dataclass, asdict
from datetime import datetime, UTC


@dataclass(frozen=True)
class TelemetryEvent:
    event_type: str
    source_node: str
    payload: dict
    governance_mode: str
    timestamp_utc: str


class AsyncTelemetryBus:
    def __init__(self) -> None:
        self.queue: asyncio.Queue[TelemetryEvent] = asyncio.Queue()

    async def publish(self, event: TelemetryEvent) -> None:
        await self.queue.put(event)

    async def consume(self) -> TelemetryEvent:
        return await self.queue.get()


def create_event(event_type: str, source_node: str, payload: dict) -> TelemetryEvent:
    return TelemetryEvent(
        event_type=event_type,
        source_node=source_node,
        payload=payload,
        governance_mode="rx-only",
        timestamp_utc=datetime.now(UTC).isoformat(),
    )
