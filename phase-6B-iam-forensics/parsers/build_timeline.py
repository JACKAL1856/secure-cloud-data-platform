import json
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_PATH = os.path.join(BASE_DIR, "../logs/cloudtrail_events.json")

with open(LOG_PATH) as f:
    events = json.load(f)

timeline = sorted(
    events,
    key=lambda e: datetime.fromisoformat(e["eventTime"].replace("Z", ""))
)

print("=== IAM INCIDENT TIMELINE ===\n")

for e in timeline:
    print(f"{e['eventTime']} | {e['userIdentity']} | {e['eventName']}")

