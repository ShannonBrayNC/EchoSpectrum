# Authorized Research Mode

EchoSpectrum includes an approval-gated Authorized Research Mode intended for controlled academic, government, and laboratory partnerships.

## Purpose

This mode supports:
- university research collaboration
- civic resilience experimentation
- synthetic RF experimentation
- replay analysis
- offline waveform analysis
- governance research

## Important Boundary

EchoSpectrum remains governance-aware.

Production and public deployments remain RX-only by default.

Restricted workflows require:
- signed authorization
- isolated lab environments
- ETS trust-chain metadata
- principal investigator approval
- audit logging
- replay capture

## Supported Research Organizations

Examples include:
- Missouri University of Science and Technology
- University of North Carolina
- Elon University
- DARPA-affiliated research programs
- DoD-sponsored research labs

## Research Authorization Fields

| Field | Purpose |
|---|---|
| research_authorization_id | experiment authorization |
| principal_investigator | responsible researcher |
| spectrum_scope | approved frequencies |
| ethics_review_reference | oversight tracking |
| audit_chain_id | governance traceability |

## Safety Model

EchoSpectrum does NOT remove safeguards globally.

Instead, it:
- preserves RX-only defaults
- gates restricted workflows behind authorization
- records governance metadata
- preserves auditability
- separates simulation from production operations

## Recommended Positioning

EchoSpectrum should be presented as:

> A governance-aware RF experimentation and observability framework.
