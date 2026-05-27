# Environment Profiles

EchoSpectrum supports environment-separated deployment profiles.

## Planned Environments

| Environment | Purpose |
|---|---|
| development | local observatory development |
| test | CI validation and replay testing |
| staging | distributed mesh validation |
| production | operational observatory deployments |

## Governance Requirements

Every environment must:
- preserve RX-only posture
- propagate ETS metadata
- maintain replay auditability
- support SignalForge orchestration

## Future Enhancements

- Azure Key Vault integration
- environment-specific telemetry retention
- deployment profile manifests
- distributed node enrollment
