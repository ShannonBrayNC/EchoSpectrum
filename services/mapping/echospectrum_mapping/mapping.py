from __future__ import annotations

from dataclasses import dataclass, asdict
from datetime import datetime, UTC
import json
from math import cos, radians
from pathlib import Path


@dataclass(frozen=True)
class DirectionalObservation:
    latitude: float
    longitude: float
    bearing_degrees: float
    signal_strength_dbfs: float
    center_frequency_hz: float
    timestamp_utc: str


@dataclass
class MappingSession:
    session_id: str
    operator: str
    antenna_profile: str
    sensor_profile: str
    observations: list[DirectionalObservation]

    def add_observation(self, observation: DirectionalObservation) -> None:
        self.observations.append(observation)

    def to_dict(self) -> dict:
        return {
            "session_id": self.session_id,
            "operator": self.operator,
            "antenna_profile": self.antenna_profile,
            "sensor_profile": self.sensor_profile,
            "observation_count": len(self.observations),
            "generated_utc": _utc_now(),
        }


def estimate_signal_centroid(observations: list[DirectionalObservation]) -> tuple[float, float]:
    if not observations:
        raise ValueError("At least one observation is required")

    total_weight = 0.0
    weighted_lat = 0.0
    weighted_lon = 0.0

    for obs in observations:
        weight = max(1.0, abs(obs.signal_strength_dbfs))
        weighted_lat += obs.latitude * weight
        weighted_lon += obs.longitude * weight
        total_weight += weight

    return weighted_lat / total_weight, weighted_lon / total_weight


def export_geojson(session: MappingSession, output_path: str | Path) -> Path:
    features = []

    for obs in session.observations:
        features.append({
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [obs.longitude, obs.latitude],
            },
            "properties": {
                "bearing_degrees": obs.bearing_degrees,
                "signal_strength_dbfs": obs.signal_strength_dbfs,
                "center_frequency_hz": obs.center_frequency_hz,
                "timestamp_utc": obs.timestamp_utc,
            },
        })

    geojson = {
        "type": "FeatureCollection",
        "metadata": session.to_dict(),
        "features": features,
    }

    path = Path(output_path)
    path.write_text(json.dumps(geojson, indent=2), encoding="utf-8")
    return path


def create_observation(
    latitude: float,
    longitude: float,
    bearing_degrees: float,
    signal_strength_dbfs: float,
    center_frequency_hz: float,
) -> DirectionalObservation:
    return DirectionalObservation(
        latitude=latitude,
        longitude=longitude,
        bearing_degrees=bearing_degrees,
        signal_strength_dbfs=signal_strength_dbfs,
        center_frequency_hz=center_frequency_hz,
        timestamp_utc=_utc_now(),
    )


def _utc_now() -> str:
    return datetime.now(UTC).isoformat()
