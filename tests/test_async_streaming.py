import asyncio

from services.streaming.echospectrum_streaming.event_bus import (
    AsyncTelemetryBus,
    create_event,
)
from services.streaming.echospectrum_streaming.websocket_gateway import ObservatoryGateway


async def _stream_test():
    bus = AsyncTelemetryBus()

    event = create_event(
        event_type="mesh.telemetry",
        source_node="node-rdu-001",
        payload={"signal": "915mhz"},
    )

    await bus.publish(event)
    consumed = await bus.consume()

    assert consumed.source_node == "node-rdu-001"


def test_async_bus():
    asyncio.run(_stream_test())


def test_gateway_client_registration():
    gateway = ObservatoryGateway()
    gateway.register_client("client-001")

    assert gateway.connected_client_count() == 1
