import json
from datetime import datetime
import os

def generate_report(findings):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    report_data = {
        "scan_time": timestamp,
        "total_findings": len(findings),
        "findings": [f.to_dict() for f in findings]
    }

    os.makedirs("output", exist_ok=True)
    filepath = f"output/scan_report_{timestamp}.json"

    with open(filepath, "w") as f:
        json.dump(report_data, f, indent=4)

    print(f"\nReport saved to {filepath}")