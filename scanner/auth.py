from core.base_scanner import BaseScanner
from utils.request_handler import send_get
from reports.models import Finding
from utils.logger import info, warning

class AuthScanner(BaseScanner):

    def run(self):
        findings = []
        info("Running Authentication Checks...")

        response = send_get(self.target_url)

        if response and response.status_code == 200:
            findings.append(
                Finding(
                    "Authentication",
                    "High",
                    "Endpoint accessible without authentication."
                )
            )
            warning("Endpoint does not enforce authentication.")

        return findings