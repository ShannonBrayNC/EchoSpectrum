from __future__ import annotations

import json
import unittest
from pathlib import Path


class SignalForgeManifestTests(unittest.TestCase):
    def setUp(self) -> None:
        self.repo_root = Path(__file__).resolve().parents[1]
        self.manifest_path = self.repo_root / "signalforge.manifest.json"
        self.manifest = json.loads(self.manifest_path.read_text(encoding="utf-8"))

    def test_manifest_has_required_top_level_sections(self) -> None:
        for key in [
            "schemaVersion",
            "project",
            "governance",
            "crossProductIntegrations",
            "deployment",
            "christina",
        ]:
            self.assertIn(key, self.manifest)

    def test_manifest_identifies_echospectrum_repository(self) -> None:
        self.assertEqual(self.manifest["project"]["name"], "EchoSpectrum")
        self.assertEqual(self.manifest["project"]["repository"], "ShannonBrayNC/EchoSpectrum")

    def test_manifest_preserves_receive_only_safety_boundary(self) -> None:
        prohibited = {item.lower() for item in self.manifest["governance"]["prohibitedCapabilities"]}
        for item in ["transmit", "jam", "spoof", "interfere"]:
            self.assertIn(item, prohibited)

        posture = self.manifest["governance"]["defaultSafetyPosture"].lower()
        self.assertIn("receive-only", posture)
        self.assertIn("synthetic-only", posture)

    def test_no_deployment_targets_are_enabled(self) -> None:
        self.assertEqual(self.manifest["deployment"]["azureTargets"], [])
        self.assertEqual(self.manifest["deployment"]["edgeTargets"], [])


if __name__ == "__main__":
    unittest.main()
