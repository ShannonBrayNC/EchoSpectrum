# Governance SDK

EchoSpectrum now includes a centralized governance SDK.

## Goals

- normalize governance propagation
- eliminate duplicated policy constants
- centralize audit generation
- standardize ETS trust metadata
- support Lantern-wide reuse

## Components

| Component | Purpose |
|---|---|
| constants.py | governance constants |
| audit.py | audit event helpers |

## Governance Guarantees

The SDK ensures:
- RX-only propagation
- normalized policy IDs
- audit metadata consistency
- replay-safe governance tagging
- SignalForge-compatible governance routing

## Future Enhancements

- trust-chain signatures
- policy escalation workflows
- centralized compliance middleware
- Lantern-wide governance federation
