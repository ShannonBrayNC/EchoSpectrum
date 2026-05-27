from services.governance.echospectrum_governance.audit import create_audit_event
from services.governance.echospectrum_governance.constants import (
    DEFAULT_POLICY_ID,
    RX_ONLY_MODE,
)


def test_audit_event_generation():
    event = create_audit_event("research_session")

    payload = event.to_dict()

    assert payload["governance_mode"] == RX_ONLY_MODE
    assert payload["policy_id"] == DEFAULT_POLICY_ID
