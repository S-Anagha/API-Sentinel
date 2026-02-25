class Finding:
    def __init__(self, vuln_type, severity, description):
        self.vuln_type = vuln_type
        self.severity = severity
        self.description = description

    def to_dict(self):
        return {
            "type": self.vuln_type,
            "severity": self.severity,
            "description": self.description
        }