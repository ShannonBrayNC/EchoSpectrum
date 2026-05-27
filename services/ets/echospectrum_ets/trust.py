from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, UTC
import uuid


@dataclass(frozen=True)
class ExperimentAuthorization:
    authorization_id: str
    experiment_name: str
    governance_mode: str
    approved: bool
    timestamp_utc: str


def create_authorization(experiment_name: str) -> ExperimentAuthorization:
    return ExperimentAuthorization(
        authorization_id=str(uuid.uuid4()),
        experiment_name=experiment_name,
        governance_mode="rx-only",
        approved=True,
        timestamp_utc=datetime.now(UTC).isoformat(),
    )
