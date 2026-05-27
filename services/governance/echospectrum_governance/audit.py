from __future__ import annotations

from dataclasses import dataclass, asdict
from datetime import datetime, UTC
import uuid

from services.governance.echospectrum_governance.constants import (
    DEFAULT_POLICY_ID,
    PLATFORM_NAME,
    RX_ONLY_MODE,
)


@dataclass(frozen=True)
class AuditEvent:
    audit_id: str
    event_type: str
    platform: str
    governance_mode: str
    policy_id: str
    timestamp_utc: str

    def to_dict(self) -> dict:
        return asdict(self)


def create_audit_event(event_type: str) -> AuditEvent:
    return AuditEvent(
        audit_id=str(uuid.uuid4()),
        event_type=event_type,
        platform=PLATFORM_NAME,
        governance_mode=RX_ONLY_MODE,
        policy_id=DEFAULT_POLICY_ID,
        timestamp_utc=datetime.now(UTC).isoformat(),
    )
