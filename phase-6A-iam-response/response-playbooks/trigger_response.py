import subprocess
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

RISK_SCORE = 80
THRESHOLD = 70

print(f"[INFO] Risk Score Evaluated: {RISK_SCORE}")

if RISK_SCORE >= THRESHOLD:
    print("[DECISION] High risk detected")
    print("[ACTION] Triggering IAM compromise response playbook\n")

    execute_path = os.path.join(BASE_DIR, "execute_response.py")

    subprocess.run(
        ["python3", execute_path],
        check=True
    )

    print("\n[STATUS] Incident contained successfully")

else:
    print("[DECISION] Risk below threshold")
    print("[ACTION] Monitoring only")
