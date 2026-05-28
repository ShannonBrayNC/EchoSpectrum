from __future__ import annotations

from dataclasses import dataclass, asdict
from datetime import datetime, UTC


@dataclass(frozen=True)
class ResearchAuthorizationRequest:
    research_authorization_id: str
    principal_investigator: str
    organization: str
    lab_environment: str
    spectrum_scope: str
    ethics_review_reference: str
    hardware_profile: str
    replay_logging_enabled: bool
    human_approval_recorded: bool


@dataclass(frozen=True)
class ResearchAuthorizationDecision:
    allowed: bool
    reason: str
    governance_mode: str
    timestamp_utc: str

    def to_dict(self) -> dict:
        return asdict(self)


AUTHORIZED_LAB_ENVIRONMENTS = {
    "isolated-lab",
    "shielded-lab",
    "university-controlled-lab",
    "government-controlled-lab",
}

AUTHORIZED_HARDWARE_PROFILES = {
    "synthetic-only",
    "hackrf-rx-only",
    "rtl-sdr-rx-only",
    "shielded-lab-sdr",
}


def evaluate_research_authorization(
    request: ResearchAuthorizationRequest,
) -> ResearchAuthorizationDecision:
    missing = []

    if not request.research_authorization_id:
        missing.append("research_authorization_id")
    if not request.principal_investigator:
        missing.append("principal_investigator")
    if not request.ethics_review_reference:
        missing.append("ethics_review_reference")
    if not request.spectrum_scope:
        missing.append("spectrum_scope")

    if missing:
        return _deny(f"Missing required research authorization fields: {', '.join(missing)}")

    if request.lab_environment not in AUTHORIZED_LAB_ENVIRONMENTS:
        return _deny("Lab environment is not approved for authorized research mode.")

    if request.hardware_profile not in AUTHORIZED_HARDWARE_PROFILES:
        return _deny("Hardware profile is not allowlisted for authorized research mode.")

    if not request.replay_logging_enabled:
        return _deny("Replay logging is mandatory for authorized research mode.")

    if not request.human_approval_recorded:
        return _deny("Human approval record is mandatory for authorized research mode.")

    return ResearchAuthorizationDecision(
        allowed=True,
        reason="Authorized research mode approved with ETS governance controls.",
        governance_mode="authorized_research",
        timestamp_utc=_utc_now(),
    )


def _deny(reason: str) -> ResearchAuthorizationDecision:
    return ResearchAuthorizationDecision(
        allowed=False,
        reason=reason,
        governance_mode="rx-only",
        timestamp_utc=_utc_now(),
    )


def _utc_now() -> str:
    return datetime.now(UTC).isoformat()
