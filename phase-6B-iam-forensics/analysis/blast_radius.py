import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_PATH = os.path.join(BASE_DIR, "../logs/cloudtrail_events.json")

with open(LOG_PATH) as f:
    events = json.load(f)

accessed_resources = set()

for e in events:
    if "resource" in e:
        accessed_resources.add(e["resource"])

print("=== BLAST RADIUS ANALYSIS ===")
for r in accessed_resources:
    print(f"- {r}")

