# Secure Cloud Data Platform – Architecture Overview

## High-Level Flow
1. Cloud activity logs (IAM, API events) are ingested
2. Anomaly signals are detected and risk-scored
3. High-risk IAM activity triggers automated containment
4. Forensic analysis reconstructs timelines and impact
5. Cross-account lateral movement is assessed
6. Lessons learned are converted into preventive controls

## Core Design Principles
- Least privilege
- Automation-first incident response
- Evidence-driven forensics
- Defense-in-depth

## Incident Lifecycle Coverage
- Detection (Phase 5)
- Response (Phase 6A)
- Forensics (Phase 6B)
- Lateral Risk (Phase 6C)
- Hardening (Phase 7)

