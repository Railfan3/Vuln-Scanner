import json
from datetime import datetime

def save_report(vulnerabilities, filename="report.json"):
    report = {
        "scan_date": datetime.now().isoformat(),
        "vulnerabilities": vulnerabilities
    }
    with open(filename, "w") as f:
        json.dump(report, f, indent=4)
    return filename
