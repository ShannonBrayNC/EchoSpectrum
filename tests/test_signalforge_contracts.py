import json
from pathlib import Path


CONTRACTS = [
    "contracts/rf.researchSession.v1.schema.json",
    "contracts/rf.complianceDecision.v1.schema.json",
    "contracts/rf.sensorNode.v1.schema.json",
]


def test_contracts_are_valid_json():
    for contract in CONTRACTS:
        path = Path(contract)
        assert path.exists()

        with path.open("r", encoding="utf-8") as handle:
            parsed = json.load(handle)

        assert "$schema" in parsed
        assert "title" in parsed
