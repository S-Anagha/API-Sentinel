import argparse
from core.scan_manager import ScanManager
from reports.report_generator import generate_report
from utils.logger import info, success

def main():
    parser = argparse.ArgumentParser(description="API Sentinel - Advanced API Security Scanner")
    parser.add_argument("--url", required=True, help="Target API endpoint")

    args = parser.parse_args()

    info(f"Starting scan on {args.url}")

    manager = ScanManager(args.url)
    findings = manager.execute()

    generate_report(findings)

    success("Scan completed.")

if __name__ == "__main__":
    main()