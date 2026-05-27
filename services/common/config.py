from __future__ import annotations

from dataclasses import dataclass
import os


@dataclass(frozen=True)
class EchoSpectrumConfig:
    environment: str
    governance_mode: str
    telemetry_retention_days: int


def load_config() -> EchoSpectrumConfig:
    return EchoSpectrumConfig(
        environment=os.getenv("ECHOSPECTRUM_ENV", "development"),
        governance_mode=os.getenv("ECHOSPECTRUM_GOVERNANCE", "rx-only"),
        telemetry_retention_days=int(os.getenv("ECHOSPECTRUM_RETENTION_DAYS", "30")),
    )
