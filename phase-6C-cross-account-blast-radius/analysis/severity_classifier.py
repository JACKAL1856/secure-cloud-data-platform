import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_PATH = os.path.join(BASE_DIR, "../logs/iam_trusts.json")

with open(LOG_PATH) as f:
    trusts = json.load(f)

severity = "LOW"

for t in trusts:
    if "Billing" in t["targetRole"] or "Admin" in t["targetRole"]:
        severity = "CRITICAL"

print(f"CROSS-ACCOUNT SEVERITY LEVEL: {severity}")

