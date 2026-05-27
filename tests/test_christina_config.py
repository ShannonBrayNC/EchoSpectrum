import json
from pathlib import Path


def test_christina_runner_config_exists():
    path = Path("config/christina.runner.json")
    assert path.exists()

    config = json.loads(path.read_text(encoding="utf-8"))

    assert config["project"] == "EchoSpectrum"
    assert config["mode"] == "dry-run"
    assert config["maxItems"] >= 1


def test_christina_report_directory_exists():
    path = Path("reports/christina/sprint-runner")
    assert path.exists()
