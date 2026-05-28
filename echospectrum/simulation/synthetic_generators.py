from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from hashlib import sha256
from typing import Any
from uuid import uuid4

SCHEMA_VERSION = "1.0.0"

OBSERVATION_LABELS = {
    "Observed",
    "Suspected",
    "Unconfirmed",
    "Verified",
    "Degraded",
    "Conflicting Evidence",
}

REQUIRED_REVIEW_LABELS = {
    "Requires Human Review",
    "Do Not Escalate Automatically",
}

FORBIDDEN_CAPABILITIES = {
    "transmit": False,
    "disrupt": False,
    "spoof": False,
    "overpower": False,
    "exploit": False,
}


@dataclass(frozen=True)
class SyntheticSignalSample:
    scenario_id: str
    category: str
    detection_type: str
    source_system: str
    confidence_score: float
    severity: str
    labels: tuple[str, ...]
    location_zone: str = "SyntheticZone-Alpha"
    sensor_id: str | None = "synthetic-sensor-001"
    privacy_level: str = "ZONE_ONLY"
    notes: str = "Synthetic receive-only simulation event."

    def to_event(self) -> dict[str, Any]:
        timestamp = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
        evidence_seed = f"{self.scenario_id}:{self.category}:{self.detection_type}:{timestamp}"
        evidence_hash = f"sha256-{sha256(evidence_seed.encode('utf-8')).hexdigest()}"

        return {
            "eventId": str(uuid4()),
            "schemaVersion": SCHEMA_VERSION,
            "sourceSystem": self.source_system,
            "originatingProduct": "Lantern-Civic",
            "detectionCategory": self.category,
            "detectionType": self.detection_type,
            "timestampUtc": timestamp,
            "locationZone": self.location_zone,
            "sensorId": self.sensor_id,
            "confidenceScore": self.confidence_score,
            "trustScore": None,
            "severity": self.severity,
            "labels": list(self.labels),
            "safetyBoundary": {
                "mode": "SIMULATION",
                "transmitCapable": False,
                "publicActionAllowed": False,
                "requiresHumanReview": True,
            },
            "evidence": {
                "evidenceHash": evidence_hash,
                "provenanceChain": ["EchoSpectrum", "SignalForge"],
                "rawEvidencePointer": f"synthetic://echospectrum/{self.scenario_id}",
                "privacyLevel": self.privacy_level,
            },
            "routing": {
                "sendToETS": True,
                "sendToChristina": True,
                "sendToOpsHelm": True,
                "sendToLanternCivicDashboard": True,
                "sendToEchoChamber": False,
                "publicDashboardAllowed": False,
            },
            "capabilities": FORBIDDEN_CAPABILITIES.copy(),
            "notes": self.notes,
        }


def generate_signal_integrity_event() -> dict[str, Any]:
    sample = SyntheticSignalSample(
        scenario_id="signal-integrity-anomaly-001",
        category="RF_INTERFERENCE",
        detection_type="SUSPECTED_SIGNAL_DEGRADATION",
        source_system="EchoSpectrum",
        confidence_score=0.74,
        severity="MEDIUM",
        labels=("Observed", "Suspected", "Requires Human Review", "Potential Civic Impact"),
        notes="Synthetic signal-integrity anomaly for passive civic resilience testing.",
    )
    return sample.to_event()


def generate_timing_anomaly_event() -> dict[str, Any]:
    sample = SyntheticSignalSample(
        scenario_id="timing-anomaly-001",
        category="GPS_PNT_SPOOFING",
        detection_type="SUSPECTED_TIMING_DRIFT",
        source_system="EchoSpectrum",
        confidence_score=0.66,
        severity="MEDIUM",
        labels=("Observed", "Suspected", "Requires Human Review", "Potential Civic Impact"),
        notes="Synthetic timing anomaly for PNT resilience testing.",
    )
    return sample.to_event()


def generate_sensor_degraded_event() -> dict[str, Any]:
    sample = SyntheticSignalSample(
        scenario_id="sensor-degraded-001",
        category="SENSOR_SPOOFING_OR_FAKE_TELEMETRY",
        detection_type="SENSOR_HEARTBEAT_LOSS",
        source_system="EchoSpectrum",
        confidence_score=0.91,
        severity="HIGH",
        labels=("Observed", "Degraded", "Requires Human Review", "Potential Civic Impact"),
        notes="Synthetic degraded-coverage event. Sensor silence is treated as a reportable finding.",
    )
    return sample.to_event()


def generate_conflicting_sensor_event() -> dict[str, Any]:
    sample = SyntheticSignalSample(
        scenario_id="conflicting-sensors-001",
        category="SENSOR_SPOOFING_OR_FAKE_TELEMETRY",
        detection_type="CONFLICTING_SENSOR_READINGS",
        source_system="EchoSpectrum",
        confidence_score=0.42,
        severity="MEDIUM",
        labels=("Observed", "Unconfirmed", "Conflicting Evidence", "Requires Human Review"),
        notes="Synthetic conflicting evidence event. Low-confidence findings remain visible and review-gated.",
    )
    return sample.to_event()


def generate_all_synthetic_events() -> list[dict[str, Any]]:
    return [
        generate_signal_integrity_event(),
        generate_timing_anomaly_event(),
        generate_sensor_degraded_event(),
        generate_conflicting_sensor_event(),
    ]
