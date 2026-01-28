# Phase 6C – Cross-Account Blast Radius Analysis

## Objective
Determine whether a compromised IAM identity could pivot into other AWS accounts via role trust relationships.

## Findings
- dev-backend could assume roles in two external AWS accounts
- One role provided administrative/billing-level access

## Risk
CRITICAL – Multi-account lateral movement possible.

## Recommendation
- Restrict sts:AssumeRole permissions
- Apply external ID conditions
- Monitor cross-account role usage

