from pathlib import Path

from services.mapping.echospectrum_mapping.mapping import (
    MappingSession,
    create_observation,
    estimate_signal_centroid,
    export_geojson,
)


def test_centroid_estimation():
    observations = [
        create_observation(35.0, -78.0, 90, -40, 915e6),
        create_observation(35.1, -78.1, 120, -42, 915e6),
    ]

    lat, lon = estimate_signal_centroid(observations)

    assert lat > 35.0
    assert lon < -78.0


def test_geojson_export(tmp_path: Path):
    session = MappingSession(
        session_id="session-001",
        operator="EchoSpectrum",
        antenna_profile="Proxicast LPDA",
        sensor_profile="HackRF One",
        observations=[],
    )

    session.add_observation(
        create_observation(35.0, -78.0, 90, -40, 915e6)
    )

    output_path = tmp_path / "mapping.geojson"
    export_geojson(session, output_path)

    assert output_path.exists()
