# EchoSpectrum

EchoSpectrum is the passive spectrum-observability and synthetic simulation layer for the Lantern Protocol stack.

## Sprint 2 Scope

Sprint 2 establishes a receive-only, synthetic-only baseline for civic signal integrity testing.

The project generates safe synthetic Lantern threat events for:

- RF interference and suspected jamming indicators
- GPS/PNT timing and location anomalies
- Sensor outage and degraded coverage conditions
- Conflicting sensor evidence
- Low-confidence observations requiring human review

## Safety Boundary

EchoSpectrum must not transmit, disrupt, spoof, overpower, exploit, or interfere with any communications, navigation, identity, infrastructure, or civic system.

This repository is for simulation, passive observation modeling, evidence-shape validation, and cross-product safety testing only.

## Run Tests

```powershell
pwsh -NoProfile -Command "python -m unittest discover -s tests"
```

or:

```bash
python -m unittest discover -s tests
```

## Generate Synthetic Events

```bash
python scripts/run_synthetic_simulation.py
```

Generated events are intended for downstream validation by SignalForge, ETS, Christina, OpsHelm, and Lantern-Civic.
