from services.compliance.echospectrum_compliance.engine import evaluate_action


def test_jamming_is_denied():
    result = evaluate_action("jamming")
    assert result.allowed is False
    assert result.policy_id == "RF-0001"


def test_transmit_workflow_is_denied():
    result = evaluate_action("transmit experimental beacon")
    assert result.allowed is False


def test_receive_only_research_allowed():
    result = evaluate_action("observe 915mhz spectrum")
    assert result.allowed is True
