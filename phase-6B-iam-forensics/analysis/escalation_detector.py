import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_PATH = os.path.join(BASE_DIR, "../logs/cloudtrail_events.json")

with open(LOG_PATH) as f:
    events = json.load(f)

for e in events:
    if e.get("policy") == "AdministratorAccess":
        print("PRIVILEGE ESCALATION DETECTED")
        print(f"Time: {e['eventTime']}")
        print(f"User: {e['userIdentity']}")

