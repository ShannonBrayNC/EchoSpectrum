from fastapi.testclient import TestClient

from api.main import app

client = TestClient(app)


def test_root_route():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["platform"] == "EchoSpectrum"


def test_governance_route():
    response = client.get("/governance/status")

    assert response.status_code == 200
    assert response.json()["governanceMode"] == "rx-only"
