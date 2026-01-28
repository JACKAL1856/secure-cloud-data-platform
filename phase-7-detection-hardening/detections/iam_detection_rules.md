# IAM Detection Rules

## Rule 1: Impossible Travel
Trigger if IAM user logs in from two countries within 10 minutes.

## Rule 2: Privilege Escalation
Alert on AttachUserPolicy events involving AdministratorAccess.

## Rule 3: Suspicious API Burst
Detect ListBuckets/GetObject bursts from new IPs.

## Rule 4: Cross-Account Role Abuse
Alert on sts:AssumeRole from unexpected principals.

