from services.research.echospectrum_research.authorization import (
    ResearchAuthorizationRequest,
    evaluate_research_authorization,
)


def test_authorized_research_approval():
    request = ResearchAuthorizationRequest(
        research_authorization_id="ets-001",
        principal_investigator="Dr. Example",
        organization="Missouri University of Science and Technology",
        lab_environment="isolated-lab",
        spectrum_scope="915 MHz ISM",
        ethics_review_reference="IRB-2026-001",
        hardware_profile="hackrf-rx-only",
        replay_logging_enabled=True,
        human_approval_recorded=True,
    )

    decision = evaluate_research_authorization(request)

    assert decision.allowed is True
    assert decision.governance_mode == "authorized_research"


def test_research_denied_without_logging():
    request = ResearchAuthorizationRequest(
        research_authorization_id="ets-002",
        principal_investigator="Dr. Example",
        organization="Elon University",
        lab_environment="isolated-lab",
        spectrum_scope="2.4 GHz",
        ethics_review_reference="IRB-2026-002",
        hardware_profile="hackrf-rx-only",
        replay_logging_enabled=False,
        human_approval_recorded=True,
    )

    decision = evaluate_research_authorization(request)

    assert decision.allowed is False
