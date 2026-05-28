import unittest
from echospectrum.simulation.synthetic_generators import (
    generate_signal_integrity_event,
    generate_timing_anomaly_event,
    generate_sensor_degraded_event,
    generate_conflicting_sensor_event,
)

class TestSyntheticEvents(unittest.TestCase):

    def test_signal_integrity_event(self):
        event = generate_signal_integrity_event()
        self.assertEqual(event['safetyBoundary']['transmitCapable'], False)
        self.assertFalse(event['routing']['publicDashboardAllowed'])
        self.assertIn('Observed', event['labels'])

    def test_timing_anomaly_event(self):
        event = generate_timing_anomaly_event()
        self.assertEqual(event['detectionCategory'], 'GPS_PNT_SPOOFING')
        self.assertFalse(event['safetyBoundary']['transmitCapable'])

    def test_sensor_degraded_event(self):
        event = generate_sensor_degraded_event()
        self.assertIn('Degraded', event['labels'])
        self.assertTrue(event['labels'].count('Requires Human Review') > 0)

    def test_conflicting_sensor_event(self):
        event = generate_conflicting_sensor_event()
        self.assertIn('Unconfirmed', event['labels'])
        self.assertIn('Conflicting Evidence', event['labels'])
        self.assertFalse(event['routing']['publicDashboardAllowed'])

if __name__ == '__main__':
    unittest.main()