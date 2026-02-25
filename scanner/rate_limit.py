from core.base_scanner import BaseScanner
from utils.request_handler import send_get
from reports.models import Finding
from config import RATE_LIMIT_REQUESTS
from utils.logger import info

class RateLimitScanner(BaseScanner):

    def run(self):
        findings = []
        info("Running Rate Limit Checks...")

        rate_limited = False

        for _ in range(RATE_LIMIT_REQUESTS):
            response = send_get(self.target_url)

            if response and response.status_code == 429:
                rate_limited = True
                break

        if not rate_limited:
            findings.append(
                Finding(
                    "Rate Limiting",
                    "Medium",
                    "No rate limiting detected after repeated rapid requests."
                )
            )

        return findings