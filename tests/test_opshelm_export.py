from services.opshelm.echospectrum_opshelm.exporter import (
    RfFinding,
    build_incident_export,
)


def test_incident_export_generation():
    finding = RfFinding(
        finding_id="finding-001",
        label="possible_915mhz_ism",
        confidence=0.72,
        center_frequency_hz=915e6,
        signal_strength_dbfs=-41,
        notes="Synthetic research observation",
    )

    export = build_incident_export(
        incident_id="incident-001",
        findings=[finding],
        summary="915 MHz ISM activity observed",
    )

    payload = export.to_dict()

    assert payload["platform"] == "EchoSpectrum"
    assert payload["governance_mode"] == "rx-only"
    assert len(payload["findings"]) == 1
