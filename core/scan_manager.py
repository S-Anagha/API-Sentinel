from scanner.injection import InjectionScanner
from scanner.auth import AuthScanner
from scanner.rate_limit import RateLimitScanner
from scanner.bola import BOLAScanner

class ScanManager:

    def __init__(self, target_url):
        self.target_url = target_url

    def execute(self):
        scanners = [
            InjectionScanner(self.target_url),
            AuthScanner(self.target_url),
            RateLimitScanner(self.target_url),
            BOLAScanner(self.target_url)
        ]

        findings = []

        for scanner in scanners:
            findings.extend(scanner.run())

        return findings