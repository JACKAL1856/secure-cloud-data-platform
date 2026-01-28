import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

events_path = os.path.join(BASE_DIR, "../detection/suspicious_events.json")
weights_path = os.path.join(BASE_DIR, "risk_weights.json")

events = json.load(open(events_path))
weights = json.load(open(weights_path))

risk_score = 0

for e in events:
    if e.get("geo") and e.get("geo") != "India":
        risk_score += weights["new_country_login"]
    if e.get("policy") == "AdministratorAccess":
        risk_score += weights["privilege_escalation"]

print(f"FINAL RISK SCORE: {risk_score}")

if risk_score >= 70:
    print("THREAT LEVEL: HIGH")
elif risk_score >= 40:
    print("THREAT LEVEL: MEDIUM")
else:
    print("THREAT LEVEL: LOW")

