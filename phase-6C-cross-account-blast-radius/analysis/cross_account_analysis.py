import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_PATH = os.path.join(BASE_DIR, "../logs/iam_trusts.json")

with open(LOG_PATH) as f:
    trusts = json.load(f)

print("=== CROSS-ACCOUNT BLAST RADIUS ===\n")

for t in trusts:
    print(
        f"User {t['sourceUser']} from account {t['sourceAccount']} "
        f"CAN assume role {t['targetRole']} in account {t['targetAccount']}"
    )

