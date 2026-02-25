from core.base_scanner import BaseScanner
from utils.request_handler import send_get
from reports.models import Finding
from config import INJECTION_PAYLOADS
from utils.logger import info, warning

class InjectionScanner(BaseScanner):

    def run(self):
        findings = []
        info("Running Injection Checks...")

        for payload in INJECTION_PAYLOADS:
            response = send_get(self.target_url, params={"input": payload})

            if response and (
                response.status_code == 500 or
                "sql" in response.text.lower() or
                "error" in response.text.lower()
            ):
                findings.append(
                    Finding(
                        "Injection",
                        "Medium",
                        f"Possible injection response detected with payload: {payload}"
                    )
                )
                warning("Potential injection behavior detected.")

        return findings