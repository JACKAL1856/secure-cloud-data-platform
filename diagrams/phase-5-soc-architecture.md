# Phase 5 – Simulated Cloud SOC Architecture

## Overview
This diagram represents a simulated cloud-native SOC detection and response workflow,
aligned with AWS GuardDuty / Azure Defender concepts.

---

## Architecture Flow

[ Cloud Environment ]
        |
        |  (API Calls, IAM Activity, Network Logs)
        v
[ Telemetry Layer ]
- CloudTrail (IAM, API activity)
- VPC Flow Logs (network metadata)
        |
        v
[ Detection Layer ]
- GuardDuty / Defender for Cloud (Simulated)
- Anomaly-based detection
        |
        v
[ SOC Analysis ]
- Alert triage
- Severity scoring
- MITRE ATT&CK mapping
        |
        v
[ Incident Response ]
- Credential containment
- Policy hardening
- Monitoring & lessons learned

---

## Key Characteristics
- Cloud-native telemetry formats
- Detection-first SOC mindset
- Cost-free simulation using real schemas

