# Sprint 10: ETS-Authorized Research Gating Middleware

## Purpose

Establish a governance-first authorization layer for EchoSpectrum research workflows.

This sprint creates the enforcement backbone required for:
- ETS trust propagation
- authorization gating
- replay-aware audit logging
- restricted workflow isolation
- governance-compatible orchestration
- SignalForge interoperability

---

# Architectural Goals

## Core Principles

1. RX-only remains the default posture.
2. All restricted workflows require explicit authorization.
3. Governance metadata must survive all routing operations.
4. Replay logging is mandatory for elevated operations.
5. Environment integrity validation is required before execution.
6. Human review remains available for escalation states.

---

# Proposed Module Layout

```text
api/
  middleware/
    ets_authorization.py
    governance_context.py
    replay_guard.py

core/
  governance/
    authorization_models.py
    trust_chain.py
    authorization_registry.py
    escalation_hooks.py
    replay_tracking.py

tests/
  governance/
    test_authorization_middleware.py
    test_replay_enforcement.py
    test_environment_validation.py
```

---

# Middleware Responsibilities

## ETS Authorization Middleware

Responsibilities:
- validate authorization token presence
- validate ETS trust-chain signature metadata
- validate workflow classification
- enforce authorization requirements
- attach governance context to request lifecycle
- reject unauthorized elevated operations

Expected request metadata:

```json
{
  "authorization_level": "restricted",
  "trust_chain_id": "uuid",
  "principal_investigator": "approved-user",
  "replay_required": true,
  "environment_profile": "isolated-lab"
}
```

---

# Governance Context

Governance context should persist:
- workflow classification
- authorization state
- replay identifiers
- escalation state
- trust-chain lineage
- operator identity

Suggested DTO:

```python
class GovernanceContext(BaseModel):
    request_id: str
    authorization_level: str
    trust_chain_id: str
    replay_id: str
    operator_id: str
    environment_profile: str
    escalation_required: bool
```

---

# Environment Verification

Restricted workflows must validate:
- isolated execution profile
- approved environment class
- hardware allowlist match
- replay subsystem availability
- governance logger availability

Failure state:
- execution blocked
- audit event generated
- escalation hook triggered

---

# Replay Enforcement

Replay logging must:
- generate immutable replay IDs
- preserve governance metadata
- attach authorization lineage
- support observatory replay inspection
- support downstream SignalForge routing

Replay should be mandatory for:
- restricted workflows
- elevated research execution
- governance override paths
- authorization failures

---

# Escalation Hooks

Escalation triggers:
- unauthorized access attempts
- invalid trust chain
- hardware mismatch
- replay logging unavailable
- conflicting governance metadata
- environment verification failure

Escalation payload fields:
- request_id
- trust_chain_id
- operator identity
- workflow classification
- replay identifier
- event timestamp
- environment state

---

# Validation Matrix

| Scenario | Expected Result |
|---|---|
| Missing token | Block request |
| Invalid trust chain | Escalate + deny |
| RX-only workflow | Permit |
| Restricted workflow without approval | Deny |
| Missing replay logger | Deny + escalate |
| Approved isolated workflow | Permit + replay |
| Hardware mismatch | Deny |

---

# Recommended Immediate Implementation Order

1. governance DTOs
2. authorization middleware
3. replay tracking service
4. environment verification layer
5. escalation hooks
6. SignalForge authorization adapter
7. observatory replay integration
8. integration tests

---

# Definition of Done

Sprint considered complete when:

- unauthorized workflows are blocked
- replay logging is enforced
- governance metadata propagates end-to-end
- escalation events emit reliably
- restricted workflows require authorization
- isolated environment validation works
- audit trails are replay-compatible
- SignalForge routing compatibility validated
