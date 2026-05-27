from __future__ import annotations

import json
from pathlib import Path


CONTRACT_ROOT = Path("contracts")


def validate_contracts() -> list[str]:
    errors: list[str] = []

    if not CONTRACT_ROOT.exists():
        return ["contracts directory does not exist"]

    for path in sorted(CONTRACT_ROOT.glob("*.schema.json")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"{path}: invalid JSON: {exc}")
            continue

        for required_key in ("$schema", "title", "type"):
            if required_key not in data:
                errors.append(f"{path}: missing {required_key}")

    return errors


if __name__ == "__main__":
    failures = validate_contracts()
    if failures:
        for failure in failures:
            print(failure)
        raise SystemExit(1)

    print("All EchoSpectrum contracts validated.")
