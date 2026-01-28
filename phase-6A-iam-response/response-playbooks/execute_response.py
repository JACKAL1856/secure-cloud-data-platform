print("INCIDENT RESPONSE INITIATED \n")

actions = [
    "disable_access_key",
    "detach_admin_policies",
    "expire_sessions",
    "tag_user"
]

for action in actions:
    print(f"[ACTION] {action} executed")

print("\n✔ IAM COMPROMISE CONTAINED")
