---

## Phase 5: Simulated Cloud SOC Threat Detection

### Objective
Demonstrate cloud-native threat detection, investigation, and incident response workflows using **simulated but realistic cloud telemetry**, aligned with real-world SOC operations.

This phase focuses on **detection logic and analyst decision-making**, not cloud billing or UI clicks.

---

### Detection Scenario: IAM Reconnaissance

**Threat Type:** Credential misuse / cloud reconnaissance  
**Detection Source:** GuardDuty-style anomaly detection (simulated)  
**Log Source:** CloudTrail IAM events  

An IAM identity was observed making **unusual enumeration API calls** (`ListUsers`) that deviated from normal baseline behavior.

---

### Artifacts Generated
- Simulated GuardDuty finding (JSON)
- CloudTrail-style IAM log samples
- SOC analysis report
- Incident response playbook
- Investigation screenshots (terminal-based)

All artifacts use **real AWS schemas and log formats**.

---

### SOC Analysis Highlights
- Severity assessed as **Medium**
- MITRE ATT&CK Mapping:
  - **T1087 – Account Discovery**
- Identified as a **pre-privilege escalation reconnaissance pattern**

---

### Incident Response Workflow
1. Detection via anomaly-based alert
2. Analyst triage and validation
3. Access key containment
4. Credential rotation
5. Policy hardening and monitoring

This workflow mirrors **L1–L2 SOC response procedures**.

---

### Why Simulation?
This phase uses **controlled simulation** instead of live cloud services to:
- Avoid unnecessary cost
- Focus on detection and response logic
- Maintain realism using official cloud artifacts

This approach reflects **SOC tabletop exercises and replay-based investigations** used in production environments.

---

### Skills Demonstrated
- Cloud threat detection concepts
- SOC investigation methodology
- MITRE ATT&CK mapping
- Incident response design
- Security-focused Git workflows

---
# secure-cloud-data-platform
