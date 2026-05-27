from __future__ import annotations

from dataclasses import dataclass, asdict
from datetime import datetime, UTC
from typing import Iterable


DEFAULT_PROHIBITED_ACTIONS = {
    "jam",
    "jamming",
    "deauth",
    "deauthentication",
    "packet_injection",
    "cellular_interception",
    "imsi_catcher",
    "spoof_public_safety",
    "autonomous_rf_transmission",
}


@dataclass(frozen=True)
class ComplianceDecision:
    allowed: bool
    reason: str
    policy_id: str
    timestamp_utc: str

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass(frozen=True)
class CompliancePolicy:
    policy_id: str
    prohibited_actions: set[str]
    rx_only_mode: bool = True


class ComplianceEngine:
    def __init__(self, policy: CompliancePolicy):
        self.policy = policy

    def evaluate(self, action: str) -> ComplianceDecision:
        normalized = _normalize(action)

        if normalized in self.policy.prohibited_actions:
            return _deny(
                policy_id=self.policy.policy_id,
                reason=f"Action '{action}' is prohibited by EchoSpectrum policy.",
            )

        if self.policy.rx_only_mode and "transmit" in normalized:
            return _deny(
                policy_id=self.policy.policy_id,
                reason="Transmit-capable workflows require separate review and authorization.",
            )

        return ComplianceDecision(
            allowed=True,
            reason="Action appears compatible with receive-only research.",
            policy_id=self.policy.policy_id,
            timestamp_utc=_utc_now(),
        )


def evaluate_action(action: str, prohibited: Iterable[str] | None = None) -> ComplianceDecision:
    policy = CompliancePolicy(
        policy_id="RF-0001",
        prohibited_actions=set(prohibited or DEFAULT_PROHIBITED_ACTIONS),
    )
    engine = ComplianceEngine(policy)
    return engine.evaluate(action)


def _normalize(value: str) -> str:
    return value.strip().lower().replace("-", "_").replace(" ", "_")


def _utc_now() -> str:
    return datetime.now(UTC).isoformat()


def _deny(policy_id: str, reason: str) -> ComplianceDecision:
    return ComplianceDecision(
        allowed=False,
        reason=reason,
        policy_id=policy_id,
        timestamp_utc=_utc_now(),
    )
