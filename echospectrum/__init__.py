"""EchoSpectrum passive signal-integrity simulation package."""

from .simulation.synthetic_generators import (
    generate_signal_integrity_event,
    generate_timing_anomaly_event,
    generate_sensor_degraded_event,
    generate_conflicting_sensor_event,
)

__all__ = [
    "generate_signal_integrity_event",
    "generate_timing_anomaly_event",
    "generate_sensor_degraded_event",
    "generate_conflicting_sensor_event",
]
