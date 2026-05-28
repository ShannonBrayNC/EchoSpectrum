from pathlib import Path
import unittest

FORBIDDEN_TERMS = [
    'transmit_signal(',
    'start_transmitter(',
    'jammer_control',
    'spoof_signal(',
    'deauth_attack',
    'overpower_signal',
]

class TestReceiveOnlyPolicy(unittest.TestCase):

    def test_repository_does_not_include_unsafe_capability_calls(self):
        root = Path(__file__).resolve().parents[1]
        scanned = []
        for path in root.rglob('*'):
            if path.is_file() and path.suffix in {'.py', '.md', '.yml', '.yaml'}:
                text = path.read_text(encoding='utf-8', errors='ignore')
                scanned.append(str(path.relative_to(root)))
                for term in FORBIDDEN_TERMS:
                    self.assertNotIn(term, text, f'Forbidden unsafe capability term found: {term} in {path}')
        self.assertTrue(scanned)

    def test_all_generated_events_disable_public_action_and_transmit(self):
        from echospectrum.simulation.synthetic_generators import generate_all_synthetic_events
        for event in generate_all_synthetic_events():
            self.assertFalse(event['safetyBoundary']['transmitCapable'])
            self.assertFalse(event['safetyBoundary']['publicActionAllowed'])
            self.assertTrue(event['safetyBoundary']['requiresHumanReview'])
            self.assertFalse(event['routing']['publicDashboardAllowed'])

if __name__ == '__main__':
    unittest.main()
