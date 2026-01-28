## Response Playbook: IAM Reconnaissance

### Detection
Triggered via GuardDuty anomaly detection.

### Triage
- Validate API call frequency
- Confirm source IP legitimacy

### Containment
- Disable access key
- Block IP if malicious

### Eradication
- Rotate credentials
- Remove unnecessary IAM permissions

### Recovery
- Restore least-privilege access
- Monitor for recurrence

### Lessons Learned
- Enumeration detection should be automated
- IAM access logging is critical

