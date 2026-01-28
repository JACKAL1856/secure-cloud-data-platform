# IAM Preventive Guardrails

## 1. Disable Long-Lived Access Keys
- Enforce key rotation < 90 days
- Alert on keys older than 60 days

## 2. Restrict sts:AssumeRole
- Allow only explicitly trusted accounts
- Require ExternalId for cross-account access

## 3. Enforce Least Privilege
- Block AdministratorAccess on human users
- Require approvals for privilege escalation

## 4. Geo-Based Login Restrictions
- Alert on IAM logins outside expected regions

