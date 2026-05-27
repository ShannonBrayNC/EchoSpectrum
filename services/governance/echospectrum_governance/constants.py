from __future__ import annotations

RX_ONLY_MODE = "rx-only"

PLATFORM_NAME = "EchoSpectrum"

DEFAULT_POLICY_ID = "RF-0001"

PROHIBITED_ACTIONS = {
    "jamming",
    "deauthentication",
    "packet_injection",
    "cellular_interception",
    "imsi_catcher",
    "autonomous_rf_transmission",
}

AUDIT_EVENT_TYPES = {
    "research_session",
    "compliance_decision",
    "mesh_heartbeat",
    "replay_export",
}
