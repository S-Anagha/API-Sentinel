from core.base_scanner import BaseScanner
from utils.request_handler import send_get
from reports.models import Finding
from utils.logger import info

class BOLAScanner(BaseScanner):

    def run(self):
        findings = []
        info("Running BOLA Checks...")

        response_1 = send_get(self.target_url, params={"id": 1})
        response_2 = send_get(self.target_url, params={"id": 2})

        if response_1 and response_2:
            if response_1.text != response_2.text:
                findings.append(
                    Finding(
                        "BOLA",
                        "High",
                        "Potential object-level authorization weakness detected."
                    )
                )

        return findings