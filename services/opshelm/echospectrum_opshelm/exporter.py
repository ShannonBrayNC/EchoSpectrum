from __future__ import annotations

from dataclasses import dataclass, asdict
from datetime import datetime, UTC
from typing import List


@dataclass(frozen=True)
class RfFinding:
    finding_id: str
    label: str
    confidence: float
    center_frequency_hz: float
    signal_strength_dbfs: float
    notes: str


@dataclass(frozen=True)
class RfIncidentExport:
    incident_id: str
    platform: str
    severity: str
    summary: str
    timestamp_utc: str
    findings: List[RfFinding]
    governance_mode: str

    def to_dict(self) -> dict:
        payload = asdict(self)
        payload["findings"] = [asdict(f) for f in self.findings]
        return payload


def build_incident_export(
    incident_id: str,
    findings: List[RfFinding],
    summary: str,
    severity: str = "informational",
) -> RfIncidentExport:
    return RfIncidentExport(
        incident_id=incident_id,
        platform="EchoSpectrum",
        severity=severity,
        summary=summary,
        timestamp_utc=_utc_now(),
        findings=findings,
        governance_mode="rx-only",
    )


def _utc_now() -> str:
    return datetime.now(UTC).isoformat()
