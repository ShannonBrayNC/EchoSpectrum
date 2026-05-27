from __future__ import annotations

from dataclasses import dataclass, asdict
from datetime import datetime, UTC


@dataclass(frozen=True)
class SignalObservation:
    center_frequency_hz: float
    bandwidth_hz: float
    peak_power_dbfs: float
    sample_rate_hz: float


@dataclass(frozen=True)
class SignalClassification:
    label: str
    confidence: float
    explanation: str
    timestamp_utc: str

    def to_dict(self) -> dict:
        return asdict(self)


CLASSIFICATION_RULES = [
    {
        "label": "possible_915mhz_ism",
        "min": 902e6,
        "max": 928e6,
        "confidence": 0.62,
        "explanation": "Observation falls within the U.S. 902-928 MHz ISM range.",
    },
    {
        "label": "possible_24ghz_ism",
        "min": 2.4e9,
        "max": 2.4835e9,
        "confidence": 0.66,
        "explanation": "Observation falls within the 2.4 GHz ISM range commonly used for BLE/Wi-Fi/Zigbee.",
    },
    {
        "label": "possible_58ghz_ism",
        "min": 5.725e9,
        "max": 5.875e9,
        "confidence": 0.66,
        "explanation": "Observation falls within the 5.8 GHz ISM range.",
    },
    {
        "label": "possible_adsb",
        "min": 1089e6,
        "max": 1091e6,
        "confidence": 0.75,
        "explanation": "Observation overlaps the ADS-B receive-only beacon region.",
    },
]


def classify_observation(observation: SignalObservation) -> SignalClassification:
    for rule in CLASSIFICATION_RULES:
        if rule["min"] <= observation.center_frequency_hz <= rule["max"]:
            return SignalClassification(
                label=rule["label"],
                confidence=rule["confidence"],
                explanation=rule["explanation"],
                timestamp_utc=_utc_now(),
            )

    return SignalClassification(
        label="unknown_receive_only_signal",
        confidence=0.25,
        explanation="Observation does not match a known research profile.",
        timestamp_utc=_utc_now(),
    )


def _utc_now() -> str:
    return datetime.now(UTC).isoformat()
