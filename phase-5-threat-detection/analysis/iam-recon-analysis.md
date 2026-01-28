## Threat Summary
A GuardDuty finding indicates anomalous IAM API activity involving repeated enumeration calls.

## Detection Source
- Service: Amazon GuardDuty (Simulated)
- Log Source: CloudTrail IAM events

## Observed Behavior
- Repeated IAM enumeration calls (`ListUsers`)
- Activity deviates from normal baseline

## Severity
Medium (5/10)

## MITRE ATT&CK Mapping
- T1087: Account Discovery

## Potential Impact
- Attacker may be mapping IAM users and roles
- Possible precursor to privilege escalation

## Immediate Response
- Disable affected access key
- Rotate IAM credentials
- Review recent CloudTrail activity

## Long-Term Remediation
- Enforce least privilege
- Enable MFA on IAM users
- Set alerts for enumeration behavior

